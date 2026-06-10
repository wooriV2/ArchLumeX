"""
ArchLumeX add_presets_v03_patch.py
기존 프리셋 20개에 mode 필드 추가 패치

실행: python add_presets_v03_patch.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path(__file__).parent / "presets"

# 프리셋명 → mode 매핑
EXTERIOR_PRESETS = {
    "arctic_glass_igloo", "brutalist_light_cathedral", "cliffside_infinity_pool",
    "courtyard_rain_lantern", "desert_monolith_resort", "forest_glass_house_night",
    "hygge_snowcabin_night", "treehouse_canopy_mist", "underwater_corridor",
    "vertical_forest_tower",
    "scandinavian_lakehouse", "japanese_engawa_autumn", "korean_hanok_snow",
    "brick_cafe_golden", "rammed_earth_sunset", "stone_cottage_spring",
    "modern_courtyard_house", "forest_cabin_morning", "rooftop_garden_dusk",
    "bamboo_house_rain",
}

def main():
    patched = 0
    skipped = 0

    for path in sorted(PRESETS_DIR.glob("*.json")):
        with open(path, encoding="utf-8") as f:
            preset = json.load(f)

        if "mode" in preset:
            print(f"  SKIP  {path.name} (mode 이미 존재: {preset['mode']})")
            skipped += 1
            continue

        mode = "exterior" if path.stem in EXTERIOR_PRESETS else "interior"
        preset["mode"] = mode

        with open(path, "w", encoding="utf-8") as f:
            json.dump(preset, f, ensure_ascii=False, indent=2)

        print(f"  OK    {path.name} → mode: {mode}")
        patched += 1

    print(f"\n완료: {patched}개 패치, {skipped}개 건너뜀")

if __name__ == "__main__":
    main()
