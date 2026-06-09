import json
import os
from pathlib import Path
from typing import Optional


PRESETS_DIR = Path(__file__).parent.parent / "presets"


def load_preset(preset_name: str) -> dict:
    """JSON 프리셋 파일 로드"""
    path = PRESETS_DIR / f"{preset_name}.json"
    if not path.exists():
        available = list_presets()
        raise FileNotFoundError(
            f"프리셋 '{preset_name}'을 찾을 수 없습니다.\n"
            f"사용 가능한 프리셋: {available}"
        )
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def list_presets() -> list[str]:
    """사용 가능한 프리셋 목록 반환"""
    return sorted([p.stem for p in PRESETS_DIR.glob("*.json")])


def build_prompt(preset: dict, overrides: Optional[dict] = None) -> str:
    """
    프리셋 데이터로 Gemini용 프롬프트 조립
    overrides: 특정 필드만 덮어쓰기 가능
    """
    p = {**preset, **(overrides or {})}

    prompt = (
        f"Professional fashion photograph of {p.get('subject', 'a female model')}. "
        f"Body: {p.get('body', '')}. "
        f"Wearing: {p.get('outfit', '')}. "
        f"Environment: {p.get('environment', '')}. "
        f"Lighting: {p.get('lighting', '')}. "
        f"Style: {p.get('style', '')}. "
        f"{p.get('quality', 'ultra-sharp, 8K, professional photography')}."
    )
    return prompt.strip()


def build_prompt_from_name(preset_name: str, overrides: Optional[dict] = None) -> str:
    """프리셋 이름으로 바로 프롬프트 생성"""
    preset = load_preset(preset_name)
    return build_prompt(preset, overrides)