"""
ArchLumeX core/engine.py
건축/인테리어 AI 이미지 프롬프트 엔진 — 프리셋 로더 & 빌더
"""

import json
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
    if not PRESETS_DIR.exists():
        return []
    return sorted([p.stem for p in PRESETS_DIR.glob("*.json")])


def list_presets_by_category(category: str) -> list[str]:
    """카테고리별 프리셋 목록 반환 (WOW / LIVE / DREAM)"""
    result = []
    for p in PRESETS_DIR.glob("*.json"):
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
        if data.get("category", "").upper() == category.upper():
            result.append(p.stem)
    return sorted(result)


def list_presets_by_tier(tier: str) -> list[str]:
    """티어별 프리셋 목록 반환 (SS / S / A)"""
    result = []
    for p in PRESETS_DIR.glob("*.json"):
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
        if data.get("tier", "").upper() == tier.upper():
            result.append(p.stem)
    return sorted(result)


def build_prompt(preset: dict, overrides: Optional[dict] = None) -> str:
    """
    프리셋 데이터로 Gemini용 프롬프트 조립
    preset_prompt 필드가 있으면 우선 사용
    """
    p = {**preset, **(overrides or {})}

    if p.get("preset_prompt"):
        return p["preset_prompt"]

    parts = []
    if p.get("building_type"):
        parts.append(f"Building: {p['building_type']}.")
    if p.get("arch_style"):
        parts.append(f"Architectural style: {p['arch_style']}.")
    if p.get("ext_material"):
        parts.append(f"Exterior material: {p['ext_material']}.")
    if p.get("lighting"):
        parts.append(f"Lighting: {p['lighting']}.")
    if p.get("mood"):
        parts.append(f"Mood: {p['mood']}.")
    parts.append("Ultra-sharp photorealistic image, 8K resolution, award-winning architectural photography.")

    return " ".join(parts)


def build_prompt_from_name(preset_name: str, overrides: Optional[dict] = None) -> str:
    """프리셋 이름으로 바로 프롬프트 생성"""
    preset = load_preset(preset_name)
    return build_prompt(preset, overrides)


def get_preset_info(preset_name: str) -> dict:
    """프리셋 메타 정보 반환"""
    preset = load_preset(preset_name)
    return {
        "name":        preset.get("name", preset_name),
        "label":       preset.get("label", ""),
        "category":    preset.get("category", ""),
        "tier":        preset.get("tier", ""),
        "description": preset.get("description", ""),
        "tags":        preset.get("tags", []),
    }