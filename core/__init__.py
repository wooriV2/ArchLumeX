from providers.base import ImageProvider, GenerationResult
from providers.gemini import GeminiProvider


def get_provider(name: str) -> ImageProvider:
    providers = {
        "gemini": GeminiProvider,
        # 추후 추가:
        # "stability": StabilityProvider,
        # "midjourney": MidjourneyProvider,
    }
    if name not in providers:
        raise ValueError(f"알 수 없는 프로바이더: {name}. 사용 가능: {list(providers.keys())}")
    return providers[name]()