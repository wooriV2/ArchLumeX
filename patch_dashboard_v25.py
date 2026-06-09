# -*- coding: utf-8 -*-
"""
patch_dashboard_v25.py
LumineX — dashboard.py에 '🎨 애니 아트스타일' 카테고리 신설 + 32개 등록

방식:
- PRESET_CATEGORIES 안 '🎌 애니 & 글래머' 카테고리의 마지막 항목
  'anime_webtoon_style' 을 앵커로 사용
- 그 항목이 끝나는 리스트 닫기 '],' 직후에 새 카테고리 블록을 삽입
- 백업 dashboard.py.bak_v25 생성 후 수정

실행: 프로젝트 루트(C:/Dev/LumineX/)에서  python patch_dashboard_v25.py
"""

import re
import shutil
import os

DASH = "dashboard.py"
ANCHOR_LAST = "anime_webtoon_style"   # 애니&글래머 카테고리의 마지막 항목

# 새 카테고리 32개 (v25에서 생성한 키와 1:1)
NEW = [
    # JP 11
    "anime_jp_90s_retro", "anime_jp_80s_citypop", "anime_jp_modern_glossy",
    "anime_jp_shoujo_soft", "anime_jp_shounen_action", "anime_jp_seinen_gritty",
    "anime_jp_makoto_watercolor", "anime_jp_ghibli_soft", "anime_jp_ecchi_glossy",
    "anime_jp_gekiga_noir", "anime_jp_pinup_retro",
    # KR 7
    "anime_kr_webtoon_glossy", "anime_kr_romance_soft", "anime_kr_action_manhwa",
    "anime_kr_lezhin_mature", "anime_kr_pastel_dream", "anime_kr_lofi_chill",
    "anime_kr_noir_mature",
    # CN 4
    "anime_cn_donghua_xianxia", "anime_cn_guofeng_ink", "anime_cn_modern_donghua",
    "anime_cn_palace_drama",
    # US 6
    "anime_us_cartoon_bold", "anime_us_comic_ink", "anime_us_pixar_stylized",
    "anime_us_disney_classic", "anime_us_pinup_classic", "anime_us_badgirl_comic",
    # EU 3
    "anime_eu_ligne_claire", "anime_eu_graphic_novel", "anime_eu_erotic_bd",
    # mood 1
    "anime_noir_silhouette",
]
NEW_CAT_LABEL = "\U0001F3A8 \uC560\uB2C8 \uC544\uD2B8\uC2A4\uD0C0\uC77C"  # 🎨 애니 아트스타일


def main():
    if not os.path.exists(DASH):
        print(f"[ERROR] {DASH} not found. Run from project root.")
        return

    src = open(DASH, encoding="utf-8").read()

    if NEW_CAT_LABEL in src:
        print(f"[SKIP] '{NEW_CAT_LABEL}' 카테고리가 이미 존재합니다. 중단.")
        return

    # 앵커: anime_webtoon_style 항목이 든 줄을 찾고, 그 항목이 끝나는 리스트 닫기 '],' 위치 탐색
    idx = src.find("'" + ANCHOR_LAST + "'")
    if idx < 0:
        idx = src.find('"' + ANCHOR_LAST + '"')
    if idx < 0:
        print(f"[ERROR] 앵커 '{ANCHOR_LAST}' 를 dashboard.py에서 찾지 못했습니다.")
        return

    # 앵커 이후 첫 '],' (애니&글래머 카테고리 리스트의 닫기) 위치
    close = src.find("],", idx)
    if close < 0:
        print("[ERROR] 앵커 뒤에서 리스트 닫기 '],' 를 찾지 못했습니다.")
        return
    insert_at = close + 2   # '],' 다음

    # 들여쓰기 추정: 앵커 줄의 카테고리 항목 들여쓰기를 재사용하기보다,
    # 새 카테고리는 카테고리 레벨 들여쓰기(보통 4칸)로 작성
    # 항목 리스트는 보기 좋게 8칸 들여쓰기 + 줄바꿈
    items = ",\n".join("        '" + k + "'" for k in NEW)
    block = (
        "\n\n    # \u2500\u2500 \U0001F3A8 \uC560\uB2C8 \uC544\uD2B8\uC2A4\uD0C0\uC77C (2026-06-09 \uC2E0\uC124, \uADF8\uB9BC\uCCB4 32\uC885) \u2500\u2500\n"
        "    \"" + NEW_CAT_LABEL + "\": [\n"
        + items + ",\n"
        "    ],"
    )

    new_src = src[:insert_at] + block + src[insert_at:]

    shutil.copy(DASH, DASH + ".bak_v25")
    with open(DASH, "w", encoding="utf-8") as f:
        f.write(new_src)

    print("[OK] dashboard.py 패치 완료 (백업: dashboard.py.bak_v25)")
    print(f"     새 카테고리 '{NEW_CAT_LABEL}' + {len(NEW)}개 항목 삽입")
    print("\n검증:")
    print("  python -c \"import dashboard; print('카테고리 수:', len(dashboard.PRESET_CATEGORIES)); print('애니 아트스타일:', len(dashboard.PRESET_CATEGORIES.get('" + NEW_CAT_LABEL + "', [])))\"")


if __name__ == "__main__":
    main()
