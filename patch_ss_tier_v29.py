"""
patch_ss_tier_v29.py
애니 아트스타일 SS tier 10종 추가
대상: dashboard.py
실행: python patch_ss_tier_v29.py
"""

from pathlib import Path

DASHBOARD_PATH = Path("dashboard.py")

ANCHOR = '    "vampire_seduction","witch_sensual","latex_venom",\n}'

NEW_BLOCK = '    "vampire_seduction","witch_sensual","latex_venom",\n    # 2026-06-09 애니 아트스타일 SS 10종 확정 (JP4/KR3/CN2/EU1)\n    "anime_jp_80s_citypop","anime_jp_shoujo_soft","anime_jp_seinen_gritty","anime_jp_makoto_watercolor",\n    "anime_kr_webtoon_glossy","anime_kr_action_manhwa","anime_kr_lofi_chill",\n    "anime_cn_donghua_xianxia","anime_cn_palace_drama",\n    "anime_eu_ligne_claire",\n}'

def patch():
    if not DASHBOARD_PATH.exists():
        print(f"[ERROR] {DASHBOARD_PATH} 를 찾을 수 없습니다.")
        return

    text = DASHBOARD_PATH.read_text(encoding="utf-8")

    # SS_TIER 섹션에만 있는지 확인 (PRESET_CATEGORIES 제외)
    ss_start = text.find("SS_TIER = {")
    ss_end = text.find("\n}", ss_start) + 2
    ss_block = text[ss_start:ss_end]

    if "anime_eu_ligne_claire" in ss_block:
        print("[WARN] SS_TIER에 이미 패치됐습니다.")
        return

    if ANCHOR not in text:
        print("[ERROR] 앵커 미발견.")
        return

    new_text = text.replace(ANCHOR, NEW_BLOCK)
    DASHBOARD_PATH.write_text(new_text, encoding="utf-8")
    print("[OK] SS tier 10종 추가 완료 → dashboard.py 저장됨")

if __name__ == "__main__":
    patch()
