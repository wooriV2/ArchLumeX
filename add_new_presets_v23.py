# -*- coding: utf-8 -*-
"""
add_new_presets_v23.py
LumineX — 개방형(Open-ended) 바디페인팅 프리셋 20개 생성

설계 원칙 (body_paint_nude / body_paint_art 공식 계승):
- 주제(무엇을 그릴지)를 비우고, 변주 축(어떻게)만 지정 → Gemini가 매번 다르게 해석
- outfit 필드에 "painted on bare skin as fine art, NO clothing, NO fabric" 명시 → 의상 오인 방지
- 환경은 갤러리/미니멀 스튜디오로 통일 → 페인팅 자체가 주인공
- 특정 작가/문명/동물 등 고정 모티프는 절대 박지 않음 (개방성 유지)

축 구성:
  A. 질감/기법 (6) — 재료 물성만 지정, 형태 자유
  B. 무드/색조 (6) — 분위기만 지정, 모티프 자유
  C. 스타일 사조 (5) — 화풍만 열되 특정 작가 X
  D. 조명/연출 (3) — 빛으로 변주

실행: 프로젝트 루트(C:\\Dev\\LumineX\\)에 두고  python add_new_presets_v23.py
출력: presets/body_paint_*.json 20개
"""

import json
import os

PRESETS_DIR = "presets"

# 공통 조각 (개방성 유지를 위한 핵심 문구)
NUDE = "painted on bare skin as fine art, NO clothing, NO fabric, body paint as sole covering"
QUALITY = "ultra-sharp, 8K, professional fine art photography"


def P(tag, outfit, material, environment, lighting, style):
    """개방형 프리셋 dict 생성 — subject/quality는 공통 고정"""
    return {
        "tag": tag,
        "subject": "a fine art female model, body paint as sole artistic covering",
        "outfit": outfit + ", " + NUDE,
        "material": material,
        "environment": environment,
        "lighting": lighting,
        "style": style,
        "quality": QUALITY,
    }


PRESETS = {
    # ───────────────────────── A. 질감/기법 축 (6) ─────────────────────────
    "body_paint_watercolor_free": P(
        "Body Paint Watercolor Free",
        "free-form full-body watercolor body paint, soft bleeding washes, spontaneous artistic design, no fixed motif",
        "translucent watercolor pigments bleeding on skin, wet-on-wet technique",
        "fine art gallery, white seamless backdrop",
        "soft diffused gallery lighting",
        "free-form watercolor body painting editorial, abstract fine art",
    ),
    "body_paint_metallic_free": P(
        "Body Paint Metallic Free",
        "free-form full-body metallic body paint, flowing liquid-metal design, spontaneous artistic coverage, no fixed motif",
        "gold silver copper metallic pigments, flowing reflective finish on skin",
        "minimalist studio, dark seamless backdrop",
        "dramatic studio strobe, metallic highlight illumination",
        "free-form metallic body painting editorial, abstract fine art",
    ),
    "body_paint_impasto": P(
        "Body Paint Impasto",
        "free-form full-body impasto body paint, thick visible brushstrokes, spontaneous painterly design, no fixed motif",
        "thick textured oil-paint pigments, heavy palette-knife brushstrokes on skin",
        "fine art studio, neutral grey backdrop",
        "raking side light emphasizing paint texture",
        "free-form impasto body painting editorial, painterly fine art",
    ),
    "body_paint_airbrush": P(
        "Body Paint Airbrush",
        "free-form full-body airbrush body paint, smooth seamless gradients, spontaneous artistic design, no fixed motif",
        "airbrushed pigment gradients, soft blended transitions on skin",
        "minimalist studio, white seamless backdrop",
        "even high-key studio lighting",
        "free-form airbrush body painting editorial, smooth abstract fine art",
    ),
    "body_paint_ink_splatter": P(
        "Body Paint Ink Splatter",
        "free-form full-body ink-splatter body paint, dynamic splatters and drips, spontaneous artistic design, no fixed motif",
        "high-contrast ink splatters and droplets scattered on skin",
        "fine art studio, white seamless backdrop",
        "crisp studio strobe, high-contrast lighting",
        "free-form ink-splatter body painting editorial, dynamic abstract fine art",
    ),
    "body_paint_drip_free": P(
        "Body Paint Drip Free",
        "free-form full-body dripping body paint, gravity-flowing vertical drips, spontaneous artistic design, no fixed motif",
        "wet flowing pigments dripping downward on skin, glossy trails",
        "minimalist studio, dark seamless backdrop",
        "dramatic rim light catching wet drips",
        "free-form dripping body painting editorial, fluid abstract fine art",
    ),

    # ───────────────────────── B. 무드/색조 축 (6) ─────────────────────────
    "body_paint_monochrome": P(
        "Body Paint Monochrome",
        "free-form full-body monochrome body paint, black and white tonal design, spontaneous artistic coverage, no fixed motif",
        "black white and grey pigments, tonal gradient on skin",
        "fine art gallery, white seamless backdrop",
        "high-contrast black and white studio lighting",
        "free-form monochrome body painting editorial, minimal abstract fine art",
    ),
    "body_paint_pastel_dream": P(
        "Body Paint Pastel Dream",
        "free-form full-body pastel body paint, soft dreamy color design, spontaneous artistic coverage, no fixed motif",
        "soft pastel pigments, powdery blended hues on skin",
        "minimalist studio, soft pale backdrop",
        "soft diffused dreamy lighting",
        "free-form pastel body painting editorial, ethereal abstract fine art",
    ),
    "body_paint_neon_glow": P(
        "Body Paint Neon Glow",
        "free-form full-body neon body paint, vivid glowing color design, spontaneous artistic coverage, no fixed motif",
        "vivid fluorescent neon pigments, saturated glowing hues on skin",
        "dark minimalist studio, black seamless backdrop",
        "dramatic dark-key lighting, neon color pop",
        "free-form neon body painting editorial, vibrant abstract fine art",
    ),
    "body_paint_earth_tones": P(
        "Body Paint Earth Tones",
        "free-form full-body earth-tone body paint, natural ochre umber sienna design, spontaneous artistic coverage, no fixed motif",
        "natural earth pigments, ochre umber clay tones on skin",
        "fine art studio, warm neutral backdrop",
        "warm natural-toned lighting",
        "free-form earth-tone body painting editorial, organic abstract fine art",
    ),
    "body_paint_jewel_tones": P(
        "Body Paint Jewel Tones",
        "free-form full-body jewel-tone body paint, rich emerald ruby sapphire design, spontaneous artistic coverage, no fixed motif",
        "deep saturated jewel-tone pigments, emerald ruby sapphire amethyst on skin",
        "minimalist studio, dark luxe backdrop",
        "rich dramatic studio lighting, deep color saturation",
        "free-form jewel-tone body painting editorial, opulent abstract fine art",
    ),
    "body_paint_iridescent_free": P(
        "Body Paint Iridescent Free",
        "free-form full-body iridescent body paint, holographic shifting color design, spontaneous artistic coverage, no fixed motif",
        "iridescent holographic pigments, opal pearlescent color-shift on skin",
        "minimalist studio, soft gradient backdrop",
        "soft light catching iridescent shimmer",
        "free-form iridescent body painting editorial, luminous abstract fine art",
    ),

    # ───────────────────────── C. 스타일 사조 축 (5) ─────────────────────────
    "body_paint_abstract_expressionist": P(
        "Body Paint Abstract Expressionist",
        "free-form full-body abstract-expressionist body paint, bold gestural design, spontaneous artistic coverage, no fixed motif, no specific artist",
        "bold gestural pigment strokes, energetic expressive marks on skin",
        "fine art gallery, white seamless backdrop",
        "gallery lighting, high-contrast",
        "free-form abstract-expressionist body painting editorial, gestural fine art",
    ),
    "body_paint_geometric_free": P(
        "Body Paint Geometric Free",
        "free-form full-body geometric body paint, abstract angular shape design, spontaneous artistic coverage, no fixed motif, no specific culture",
        "crisp geometric pigment shapes, abstract angular forms on skin",
        "minimalist studio, white seamless backdrop",
        "clean even studio lighting",
        "free-form geometric body painting editorial, abstract fine art",
    ),
    "body_paint_organic_flow": P(
        "Body Paint Organic Flow",
        "free-form full-body organic-flow body paint, curving fluid line design, spontaneous artistic coverage, no fixed motif",
        "flowing organic pigment curves, fluid natural forms on skin",
        "fine art studio, soft neutral backdrop",
        "soft sculpting light following body curves",
        "free-form organic-flow body painting editorial, fluid abstract fine art",
    ),
    "body_paint_surreal_free": P(
        "Body Paint Surreal Free",
        "free-form full-body surreal body paint, dreamlike impossible design, spontaneous artistic coverage, no fixed motif",
        "surreal blended pigments, dreamlike impossible forms on skin",
        "minimalist studio, gradient dream backdrop",
        "soft surreal atmospheric lighting",
        "free-form surreal body painting editorial, dreamlike abstract fine art",
    ),
    "body_paint_minimalist_free": P(
        "Body Paint Minimalist Free",
        "free-form minimalist body paint, sparse selective design with bare skin negative space, spontaneous artistic placement, no fixed motif",
        "sparse selective pigment accents, generous bare-skin negative space",
        "fine art gallery, pure white seamless backdrop",
        "clean minimal high-key lighting",
        "free-form minimalist body painting editorial, restrained fine art",
    ),

    # ───────────────────────── D. 조명/연출 축 (3) ─────────────────────────
    "body_paint_blacklight": P(
        "Body Paint Blacklight",
        "free-form full-body blacklight-reactive body paint, glowing fluorescent design, spontaneous artistic coverage, no fixed motif",
        "UV-reactive fluorescent pigments glowing under blacklight on skin",
        "blackout studio, pure black environment",
        "ultraviolet blacklight, fluorescent glow",
        "free-form blacklight body painting editorial, glowing abstract fine art",
    ),
    "body_paint_glitter_free": P(
        "Body Paint Glitter Free",
        "free-form full-body glitter body paint, sparkling shimmer design, spontaneous artistic coverage, no fixed motif",
        "fine glitter and pearl pigments scattering light on skin",
        "minimalist studio, dark backdrop",
        "sparkle-catching directional light",
        "free-form glitter body painting editorial, shimmering abstract fine art",
    ),
    "body_paint_uv_reactive": P(
        "Body Paint UV Reactive",
        "free-form full-body UV-reactive neon body paint, electric glowing design, spontaneous artistic coverage, no fixed motif",
        "electric UV-reactive neon pigments, vivid glow on skin",
        "dark studio, deep black backdrop",
        "UV and neon accent lighting",
        "free-form UV-reactive body painting editorial, electric abstract fine art",
    ),
}


def main():
    if not os.path.isdir(PRESETS_DIR):
        print(f"[ERROR] '{PRESETS_DIR}' 폴더가 없습니다. 프로젝트 루트에서 실행하세요.")
        return

    created, skipped = 0, 0
    for name, data in PRESETS.items():
        path = os.path.join(PRESETS_DIR, f"{name}.json")
        if os.path.exists(path):
            print(f"[SKIP] {name}.json 이미 존재")
            skipped += 1
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK]   {name}.json")
        created += 1

    print(f"\n완료: 생성 {created}개 / 건너뜀 {skipped}개 / 총 정의 {len(PRESETS)}개")
    print("\n다음 단계: dashboard.py PRESET_CATEGORIES '바디페인팅 & 스킨 트랜스폼'에 20개 등록 (별도 패치)")


if __name__ == "__main__":
    main()
