"""
patch_model_types_v27.py
글로벌 체형 3종 텍스트 강화 패치
대상: core/data.py
실행: python patch_model_types_v27.py
"""

import re
from pathlib import Path

DATA_PATH = Path("core/data.py")

PATCHES = {
    # 브라질 부티 글램
    '    "🇧🇷 브라질 부티 글램 — 카니발 여신 극강 힙": "Brazilian carnival goddess proportions, extremely dramatic bubble buttocks, ultra-wide round hips, tiny athletic waist, toned thick thighs, sun-bronzed glistening voluptuous curves",':
    '    "🇧🇷 브라질 부티 글램 — 카니발 여신 극강 힙": "Brazilian carnival goddess, massive round bubble butt dominating silhouette, extremely wide hips with very narrow waist, powerfully thick thighs, heavy full rounded buttocks projecting dramatically, bronzed voluptuous body, samba dancer curves",',

    # 카리브 댄스홀
    '    "🏝️ 카리브 댄스홀 — 탄력 극강 부티": "Caribbean dancehall queen proportions, explosively round firm buttocks, snatched narrow waist, powerful thick thighs, bouncy athletic curves, glistening deep brown skin",':
    '    "🏝️ 카리브 댄스홀 — 탄력 극강 부티": "Caribbean dancehall queen, powerfully athletic bubble butt with spring-like firmness, snatched tiny waist, explosively wide round hips, muscular thick thighs built for dancing, deeply bronzed Caribbean skin, high-energy dancehall body, tight toned voluptuous curves",',

    # 폴리네시안 여신
    '    "🌺 폴리네시안 여신 — 강건한 풍만미": "Polynesian goddess proportions, powerful voluptuous frame, broad strong shoulders, full rounded hips and thighs, statuesque island goddess curves, warm glowing tan skin",':
    '    "🌺 폴리네시안 여신 — 강건한 풍만미": "Polynesian goddess proportions, full heavy rounded hips and thighs, broad powerful shoulders framing voluptuous figure, dramatically wide lower body, thick full thighs, abundant rounded curves, statuesque large-framed island goddess, warm bronzed glowing skin, majestic full-figured Polynesian beauty",',
}

def patch():
    if not DATA_PATH.exists():
        print(f"[ERROR] {DATA_PATH} 를 찾을 수 없습니다. 프로젝트 루트에서 실행하세요.")
        return

    text = DATA_PATH.read_text(encoding="utf-8")
    changed = 0

    for old, new in PATCHES.items():
        if old in text:
            text = text.replace(old, new)
            key = old.split('"')[3]  # 키 이름 추출
            print(f"[OK] 패치 완료: {key}")
            changed += 1
        else:
            key = old.split('"')[3]
            print(f"[WARN] 원본 텍스트 미발견 (이미 패치됐거나 텍스트 불일치): {key}")

    if changed > 0:
        DATA_PATH.write_text(text, encoding="utf-8")
        print(f"\n총 {changed}개 항목 패치 완료 → {DATA_PATH} 저장됨")
    else:
        print("\n변경 사항 없음.")

if __name__ == "__main__":
    patch()
