"""Unified LLM client supporting both OpenRouter and AWS Bedrock APIs."""

import base64
import json
import time
import asyncio
import aiohttp
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

import boto3


# =============================================================================
# MODEL REGISTRY
# =============================================================================

MODELS = {
    "gpt-5.4": {
        "provider": "openrouter",
        "model_id": "openai/gpt-5.4",
        "display_name": "GPT-5.4",
    },
    "sonnet-4.6": {
        "provider": "openrouter",
        "model_id": "anthropic/claude-sonnet-4.6",
        "display_name": "Claude Sonnet 4.6",
    },
    "qwen-3.6": {
        "provider": "openrouter",
        "model_id": "qwen/qwen3.6-plus:free",
        "display_name": "Qwen 3.6 Plus",
    },
    "gemini-3.1-pro": {
        "provider": "openrouter",
        "model_id": "google/gemini-3.1-pro-preview",
        "display_name": "Gemini 3.1 Pro",
    },
}


@dataclass
class LLMResponse:
    """Response from an LLM API call."""
    content: str
    model_key: str
    latency_ms: float
    input_tokens: int = 0
    output_tokens: int = 0
    raw_response: Optional[dict] = None


# =============================================================================
# IMAGE HELPERS
# =============================================================================

def load_image_base64(image_path: str, max_bytes: int = 5_000_000) -> str:
    """Load image file and return base64-encoded string.

    If the raw file exceeds *max_bytes*, resize it down so the base64 payload
    stays under typical API limits (~10 MB base64 ≈ ~7.5 MB raw).
    """
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    raw = path.read_bytes()

    if len(raw) > max_bytes:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(raw))
        # Shrink until under limit (preserve aspect ratio)
        quality = 85
        while len(raw) > max_bytes and quality >= 30:
            buf = io.BytesIO()
            # Convert to RGB if necessary (e.g. RGBA PNGs)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            # Scale down by 75% each iteration if still too big
            if quality < 85 or len(raw) > max_bytes * 2:
                w, h = img.size
                img = img.resize((int(w * 0.75), int(h * 0.75)), Image.LANCZOS)
            img.save(buf, format="JPEG", quality=quality)
            raw = buf.getvalue()
            quality -= 10

    return base64.b64encode(raw).decode("utf-8")


def get_image_media_type(image_path: str) -> str:
    """Determine MIME type from file extension."""
    ext = Path(image_path).suffix.lower()
    return {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }.get(ext, "image/jpeg")


# =============================================================================
# OPENROUTER CLIENT
# =============================================================================

class OpenRouterClient:
    """Client for OpenRouter API (GPT, Gemini, Qwen)."""

    API_BASE = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def complete(
        self,
        model_id: str,
        system_prompt: str,
        user_prompt: str,
        image_path: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> dict:
        """Send a completion request to OpenRouter."""
        session = await self._get_session()

        # Build user content
        user_content = []
        if image_path:
            img_b64 = load_image_base64(image_path)
            media_type = get_image_media_type(image_path)
            user_content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:{media_type};base64,{img_b64}"
                }
            })
        user_content.append({"type": "text", "text": user_prompt})

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]

        payload = {
            "model": model_id,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://llm-art-auction.research",
        }

        async with session.post(self.API_BASE, json=payload, headers=headers, timeout=aiohttp.ClientTimeout(total=180)) as resp:
            if resp.status != 200:
                error_text = await resp.text()
                raise RuntimeError(f"OpenRouter API error {resp.status}: {error_text}")
            return await resp.json()


# =============================================================================
# BEDROCK CLIENT
# =============================================================================

class BedrockClient:
    """Client for AWS Bedrock API (Claude Sonnet 4.6)."""

    def __init__(self, region: str = "us-east-1"):
        self.client = boto3.client("bedrock-runtime", region_name=region)

    def complete(
        self,
        model_id: str,
        system_prompt: str,
        user_prompt: str,
        image_path: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> dict:
        """Send a completion request to Bedrock (synchronous)."""
        # Build user content
        user_content = []
        if image_path:
            img_b64 = load_image_base64(image_path)
            media_type = get_image_media_type(image_path)
            user_content.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": media_type,
                    "data": img_b64,
                }
            })
        user_content.append({"type": "text", "text": user_prompt})

        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "temperature": temperature,
            "system": system_prompt,
            "messages": [
                {"role": "user", "content": user_content}
            ],
        }

        response = self.client.invoke_model(
            modelId=model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body),
        )

        result = json.loads(response["body"].read())
        return result


# =============================================================================
# UNIFIED CLIENT
# =============================================================================

class UnifiedLLMClient:
    """Unified client that routes to OpenRouter or Bedrock based on model."""

    def __init__(self, openrouter_api_key: str):
        self.openrouter = OpenRouterClient(openrouter_api_key)
        self.bedrock = BedrockClient()

    async def close(self):
        await self.openrouter.close()

    async def complete(
        self,
        model_key: str,
        system_prompt: str,
        user_prompt: str,
        image_path: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        max_retries: int = 3,
    ) -> LLMResponse:
        """Send completion request to the appropriate provider with retry logic."""
        model_info = MODELS[model_key]
        provider = model_info["provider"]
        model_id = model_info["model_id"]

        last_error = None
        for attempt in range(max_retries):
            start_time = time.time()
            try:
                if provider == "openrouter":
                    raw = await self.openrouter.complete(
                        model_id=model_id,
                        system_prompt=system_prompt,
                        user_prompt=user_prompt,
                        image_path=image_path,
                        temperature=temperature,
                        max_tokens=max_tokens,
                    )
                    latency = (time.time() - start_time) * 1000
                    content = raw["choices"][0]["message"]["content"]
                    usage = raw.get("usage", {})
                    return LLMResponse(
                        content=content,
                        model_key=model_key,
                        latency_ms=latency,
                        input_tokens=usage.get("prompt_tokens", 0),
                        output_tokens=usage.get("completion_tokens", 0),
                        raw_response=raw,
                    )

                elif provider == "bedrock":
                    # Bedrock is synchronous — run in executor to avoid blocking
                    loop = asyncio.get_event_loop()
                    raw = await loop.run_in_executor(
                        None,
                        lambda: self.bedrock.complete(
                            model_id=model_id,
                            system_prompt=system_prompt,
                            user_prompt=user_prompt,
                            image_path=image_path,
                            temperature=temperature,
                            max_tokens=max_tokens,
                        ),
                    )
                    latency = (time.time() - start_time) * 1000
                    content = raw["content"][0]["text"]
                    usage = raw.get("usage", {})
                    return LLMResponse(
                        content=content,
                        model_key=model_key,
                        latency_ms=latency,
                        input_tokens=usage.get("input_tokens", 0),
                        output_tokens=usage.get("output_tokens", 0),
                        raw_response=raw,
                    )

            except Exception as e:
                last_error = e
                wait = 2 ** attempt * 2  # 2s, 4s, 8s
                print(f"    [Retry {attempt+1}/{max_retries}] {model_key} error: {e}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(wait)

        raise RuntimeError(f"All {max_retries} attempts failed for {model_key}: {last_error}")
