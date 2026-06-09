import os
import requests
from urllib.parse import quote
from providers.base import ImageProvider, GenerationResult


class PollinationsProvider(ImageProvider):

    @property
    def name(self) -> str:
        return "pollinations"

    def is_available(self) -> bool:
        return True  # API 키 불필요

    def generate(self, prompt: str, output_path: str) -> GenerationResult:
        try:
            encoded = quote(prompt)
            url = f"https://image.pollinations.ai/prompt/{encoded}?width=768&height=1024&nologo=true"

            response = requests.get(url, timeout=60)

            if response.status_code != 200:
                return GenerationResult(success=False, error=f"HTTP {response.status_code}", prompt_used=prompt)

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(response.content)

            return GenerationResult(success=True, image_path=output_path, prompt_used=prompt)

        except Exception as e:
            return GenerationResult(success=False, error=str(e), prompt_used=prompt)