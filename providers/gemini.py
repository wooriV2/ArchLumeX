import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from providers.base import ImageProvider, GenerationResult
from config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiProvider(ImageProvider):
    """Google Gemini 이미지 생성 프로바이더"""

    def __init__(self):
        self._client = None

    @property
    def name(self) -> str:
        return "gemini"

    def is_available(self) -> bool:
        return bool(GEMINI_API_KEY)

    def _get_client(self):
        if self._client is None:
            try:
                from google import genai
                from google.genai import types as genai_types
                self._client = genai.Client(api_key=GEMINI_API_KEY)
                self._types = genai_types
            except ImportError:
                raise RuntimeError("google-genai 패키지가 필요합니다: pip install google-genai")
        return self._client

    def generate(self, prompt: str, output_path: str) -> GenerationResult:
        if not self.is_available():
            return GenerationResult(success=False, error="GEMINI_API_KEY가 설정되지 않았습니다.")

        try:
            client = self._get_client()

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=self._types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"],
                ),
            )

            image_data = None
            for part in response.candidates[0].content.parts:
                if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                    image_data = part.inline_data.data
                    break

            if not image_data:
                return GenerationResult(
                    success=False,
                    error="이미지 데이터를 찾을 수 없습니다. 안전 필터로 인해 차단되었을 수 있습니다.",
                    prompt_used=prompt,
                )

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(image_data)

            return GenerationResult(success=True, image_path=output_path, prompt_used=prompt)

        except Exception as e:
            return GenerationResult(success=False, error=str(e), prompt_used=prompt)