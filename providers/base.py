from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class GenerationResult:
    success: bool
    image_path: Optional[str] = None
    error: Optional[str] = None
    prompt_used: Optional[str] = None


class ImageProvider(ABC):
    """모든 이미지 생성 프로바이더의 기반 클래스"""

    @abstractmethod
    def generate(self, prompt: str, output_path: str) -> GenerationResult:
        """프롬프트로 이미지를 생성하고 저장"""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """API 키 등 사용 가능 여부 확인"""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass