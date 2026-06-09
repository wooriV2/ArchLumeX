# -*- coding: utf-8 -*-
"""
add_new_presets_v24.py
LumineX — 애니 프리셋 9개 (A: 실사 컨셉 7 + B: 2D 그림체 파일럿 2)

설계:
  A. 실사 컨셉형 (7) — succubus_anime 공식 계승
     · 실사 사진 (shot on ...), 애니에서 딴 캐릭터 컨셉
     · 특정 IP 회피, 일반 아키타입만 (저작권 안전)
     · body 글래머 실루엣 포함, 엔진 강점 활용 → 확실히 잘 나옴
  B. 2D 그림체 파일럿 (2) — 그림체 자체를 전환하는 실험 라인
     · style/quality를 "anime illustration, cel-shaded, 2D"로 전환
     · 'shot on' 카메라 문구 제거 (실사 신호 차단)
     · 실사 엔진(ArienMixXL 등)에서 그림체가 먹는지 테스트용
     · 추가 후 각 2~3장 뽑아 검증 필수 — 어정쩡하면 제거/조정

실행: 프로젝트 루트(C:\\Dev\\LumineX\\)에서  python add_new_presets_v24.py
출력: presets/anime_*.json 9개
"""

import json
import os

PRESETS_DIR = "presets"

# A형 공통 글래머 실루엣 (succubus_anime body 라인 계승)
GLAM_BODY = "super glamour anime model, tiny waist, wide round hips, hourglass silhouette, long legs"


def A(tag, subject, outfit, material, environment, lighting, style, grade):
    """A형 — 실사 컨셉 애니 (실사 사진, 캐릭터만 애니)"""
    return {
        "tag": tag,
        "subject": subject,
        "body": GLAM_BODY,
        "outfit": outfit,
        "material": material,
        "environment": environment,
        "lighting": lighting,
        "style": style,
        "quality": f"shot on Leica SL2, {grade}, portrait 2:3 vertical, photorealistic",
    }


def B(tag, subject, outfit, environment, lighting, style):
    """B형 — 2D 그림체 파일럿 (실사 신호 제거, 그림체 전환)"""
    return {
        "tag": tag,
        "subject": subject,
        "body": "anime-style female character, stylized proportions, large expressive eyes",
        "outfit": outfit,
        "material": "illustrated rendering, anime-style shading",
        "environment": environment,
        "lighting": lighting,
        "style": style,
        "quality": "high-quality anime illustration, clean 2D linework, vivid cel coloring, NOT photorealistic, NO 3D render",
    }


PRESETS = {
    # ───────────── A. 실사 컨셉형 (7) ─────────────
    "anime_swordmistress": A(
        "Anime Swordmistress",
        "a fierce anime swordmistress female model",
        "elegant battle outfit, fitted armored bodice, high-slit combat skirt, holding a katana",
        "polished armor accents, flowing fabric, leather straps",
        "ancient dojo at dusk, cherry blossom petals drifting",
        "dramatic golden-hour rim light, cinematic",
        "anime warrior glamour editorial, cinematic fantasy photography",
        "warm cinematic grade",
    ),
    "anime_mecha_pilot": A(
        "Anime Mecha Pilot",
        "a futuristic anime mecha pilot female model",
        "skin-tight pilot bodysuit, sleek plug-suit design, glowing accent lines",
        "high-tech glossy bodysuit fabric, luminous circuit accents",
        "futuristic hangar bay, towering mecha silhouette behind",
        "cool blue tech lighting, glowing HUD accents",
        "anime mecha glamour editorial, sci-fi cinematic photography",
        "cool sci-fi grade",
    ),
    "anime_shrine_maiden": A(
        "Anime Shrine Maiden",
        "a graceful anime shrine maiden female model",
        "modernized miko outfit, white top with red hakama, sheer flowing sleeves",
        "crisp white and crimson fabric, silk ribbons",
        "traditional shrine at twilight, paper lanterns, torii gate",
        "soft warm lantern glow, serene atmosphere",
        "anime shrine maiden glamour editorial, ethereal cinematic photography",
        "warm serene grade",
    ),
    "anime_demon_slayer": A(
        "Anime Demon Slayer",
        "a determined anime demon-slayer female model",
        "patterned haori-inspired jacket over fitted combat outfit, ornate sword",
        "patterned fabric, lacquered armor pieces, leather",
        "moonlit forest, mist, glowing embers in air",
        "dramatic moonlight, blue-and-amber contrast",
        "anime demon-slayer glamour editorial, dark cinematic fantasy photography",
        "moody contrast grade",
    ),
    "anime_galaxy_idol": A(
        "Anime Galaxy Idol",
        "a dazzling anime galaxy-idol female model",
        "holographic idol stage costume, star-motif accents, sparkling mini outfit",
        "iridescent holographic fabric, crystal and sequin accents",
        "cosmic concert stage, nebula backdrop, stage lights",
        "vibrant multicolor stage lighting, lens flares",
        "anime idol glamour editorial, vibrant concert photography",
        "vivid neon grade",
    ),
    "anime_battle_angel": A(
        "Anime Battle Angel",
        "a celestial anime battle-angel female model",
        "radiant armored angel outfit, feathered wings, glowing halo accents",
        "luminous white-gold armor, large feathered wings",
        "heavenly sky realm, glowing clouds, divine light beams",
        "radiant heavenly backlight, golden divine glow",
        "anime battle-angel glamour editorial, ethereal cinematic photography",
        "luminous golden grade",
    ),
    "anime_cyber_ninja": A(
        "Anime Cyber Ninja",
        "a sleek anime cyber-ninja female model",
        "skin-tight stealth bodysuit, glowing neon accents, tech mask pushed up",
        "matte black stealth fabric, neon-glow tech lines",
        "neon cyberpunk rooftop at night, holographic city below",
        "neon cyberpunk lighting, pink-and-cyan glow",
        "anime cyber-ninja glamour editorial, cyberpunk cinematic photography",
        "neon cyberpunk grade",
    ),

    # ───────────── B. 2D 그림체 파일럿 (2) ─────────────
    "anime_cel_shaded": B(
        "Anime Cel Shaded",
        "an anime female character, cel-shaded illustration",
        "stylish anime outfit, bold colorful design, dynamic flowing details",
        "vibrant anime cityscape, dynamic background",
        "flat cel-shaded lighting, bold highlights and shadows",
        "classic cel-shaded anime illustration style, bold clean lines, flat vivid colors",
    ),
    "anime_webtoon_style": B(
        "Anime Webtoon Style",
        "a Korean webtoon-style female character, soft digital illustration",
        "trendy modern outfit, fashionable casual-chic design",
        "soft pastel webtoon background, gentle gradients",
        "soft ambient webtoon lighting, gentle glow",
        "Korean webtoon (manhwa) illustration style, soft digital coloring, clean lineart, glossy highlights",
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
        tag = "A:실사컨셉" if name not in ("anime_cel_shaded", "anime_webtoon_style") else "B:그림체파일럿"
        print(f"[OK]   {name}.json   ({tag})")
        created += 1
    print(f"\n완료: 생성 {created}개 / 건너뜀 {skipped}개 / 총 정의 {len(PRESETS)}개")
    print("\n다음 단계:")
    print("  1) dashboard.py PRESET_CATEGORIES '🎌 애니 & 글래머'에 9개 등록 (별도 패치)")
    print("  2) B형 2개(anime_cel_shaded, anime_webtoon_style) 각 2~3장 뽑아 그림체 검증 필수")


if __name__ == "__main__":
    main()
