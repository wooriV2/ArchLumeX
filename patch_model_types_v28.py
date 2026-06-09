"""
patch_model_types_v28.py
약한 체형 3종 처리 패치
- 콜롬비안 레게톤: 극단 8자 강화
- 사하라 투아레그: 장신 슬림 강화
- 북유럽 발키리: 글로벌 극단 계열 → 슬림 계열 강등 + 키명 변경
대상: core/data.py
실행: python patch_model_types_v28.py
"""

from pathlib import Path

DATA_PATH = Path("core/data.py")

PATCHES = {
    # 콜롬비안 레게톤 강화
    '    "🇨🇴 콜롬비안 레게톤 — 조각된 극단 8자": "Colombian reggaeton goddess, surgically dramatic hourglass, tiny cinched waist with explosively wide round hips, full sculpted bust, lifted round buttocks, bronzed reggaeton glamour",':
    '    "🇨🇴 콜롬비안 레게톤 — 조각된 극단 8자": "Colombian reggaeton goddess, extreme exaggerated hourglass figure, impossibly tiny cinched waist, explosively wide dramatic round hips, full sculpted bust, lifted prominent round buttocks, surgically perfect waist-to-hip ratio, thick powerful thighs, bronzed Latin skin glistening",',

    # 사하라 투아레그 강화
    '    "🏜️ 사하라 투아레그 — 위엄있는 장신 골격": "Saharan Tuareg goddess proportions, tall commanding frame, strong broad shoulders, statuesque powerful hips, regal desert nomad physique, deep matte skin",':
    '    "🏜️ 사하라 투아레그 — 위엄있는 장신 골격": "Saharan Tuareg goddess, towering commanding tall frame, long powerful legs, strong broad shoulders, lean angular physique, regal desert nomad proportions, narrow elegant hips, sculpted athletic build, deep matte dark skin, statuesque elongated silhouette, desert warrior elegance",',

    # 북유럽 발키리 강등 (키명 + 텍스트 동시 변경)
    '    "❄️ 북유럽 발키리 — 차가운 거상 장신": "Nordic Valkyrie proportions, towering Amazonian stature, broad strong shoulders, long powerful legs, statuesque ice goddess frame, pale luminous skin",':
    '    "❄️ 북유럽 발키리 — 차가운 전사 슬림": "Nordic Valkyrie, tall slender warrior physique, broad strong shoulders, long lean legs, flat athletic torso, ice-cold commanding presence, pale luminous arctic skin, platinum blonde Nordic beauty, fierce battle-hardened expression, sleek powerful silhouette",',
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
            key = old.split('"')[3]
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
