# -*- coding: utf-8 -*-
"""
add_new_presets_v25.py
LumineX — 애니 아트스타일(2D 그림체) 프리셋 32개 생성/덮어쓰기

배경: v24 파일럿(anime_cel_shaded / anime_webtoon_style)이 실사 엔진에서
      2D 그림체 전환에 성공 → 본격 확장. 국가/문화권 × 그림체 조합 32종.
      의상은 에로틱까지 전면 개방(2D라 필터 관대).

구성: 일본 11 / 한국 7 / 중국 4 / 미국 6 / 유럽 3 / 무드 1

설계 원칙 (검증된 파일럿 공식):
- quality에 "NOT photorealistic, NO 3D render" 박아 2D 강제
  (예외: us_pixar_stylized 만 3D 스타일라이즈 허용)
- 그림체·문화권만 지정, 주제(포즈)는 비움 → 개방형, 매번 다르게 생성
- 의상은 그림체 컨셉별로 글램/핫/에로틱 배분
- 특정 IP/작가 회피. makoto/ghibli/manara/vargas 등은 "풍(style of)"으로만
  무드 참조 (고유명사 직접 차용 아님 → 저작권 안전선)

신규 8개 (이번 추가): jp_ecchi_glossy, jp_gekiga_noir, jp_pinup_retro,
  kr_noir_mature, us_pinup_classic, us_badgirl_comic, eu_erotic_bd, noir_silhouette
기존 24개는 의상을 중립 → 에로틱/글램으로 전면 수정 (덮어쓰기, OVERWRITE=True)

실행: 프로젝트 루트(C:/Dev/LumineX/)에서  python add_new_presets_v25.py
출력: presets/anime_*.json 32개
"""

import json
import os

PRESETS_DIR = "presets"
OVERWRITE = True   # 기존 24개 의상 수정 반영 위해 덮어쓰기

# 2D 그림체 공통 마무리 (실사/3D 신호 차단)
NO3D = "high-quality 2D illustration, clean linework, NOT photorealistic, NO 3D render, NO real photo"


def S(tag, subject, outfit, environment, lighting, style, quality_extra=None):
    """그림체 프리셋 — body는 애니 캐릭터 고정, 주제(포즈)는 열어둠"""
    return {
        "tag": tag,
        "subject": subject,
        "body": "anime-style female character, glamour proportions, expressive eyes",
        "outfit": outfit,
        "material": "illustrated rendering, stylized shading",
        "environment": environment,
        "lighting": lighting,
        "style": style,
        "quality": quality_extra if quality_extra else NO3D,
    }


PRESETS = {
    # ─────────────────────────────── 일본 (11) ───────────────────────────────
    "anime_jp_90s_retro": S(
        "Anime JP 90s Retro",
        "a 1990s retro anime female character",
        "form-fitting 90s outfit, cropped top and mini skirt, vintage glamour fashion",
        "retro Japanese city street, vintage neon signage",
        "warm nostalgic cel lighting, soft film grain feel",
        "1990s retro cel anime style, bold outlines, vivid saturated colors, vintage anime aesthetic",
    ),
    "anime_jp_80s_citypop": S(
        "Anime JP 80s Citypop",
        "an 80s citypop anime female character",
        "retro 80s glamour, off-shoulder bodycon dress, bold sensual fashion",
        "neon-lit 80s Tokyo street at dusk, citypop aesthetic",
        "warm sunset neon glow, vaporwave color palette",
        "1980s citypop anime illustration, retro airbrush feel, pastel-neon palette, nostalgic glamour",
    ),
    "anime_jp_modern_glossy": S(
        "Anime JP Modern Glossy",
        "a modern digital anime female character",
        "trendy bodycon outfit, plunging neckline, sleek sexy design",
        "clean modern cityscape, soft bokeh background",
        "polished digital lighting, glossy highlights",
        "modern digital anime style, clean glossy cel shading, vibrant crisp colors, high production value",
    ),
    "anime_jp_shoujo_soft": S(
        "Anime JP Shoujo Soft",
        "a shoujo manga female character",
        "delicate feminine glamour dress, soft romantic lace, elegant figure-flattering design",
        "dreamy garden with floating petals, sparkles in air",
        "soft glowing shoujo lighting, dreamy sparkle",
        "shoujo manga illustration style, sparkling large eyes, soft pastel colors, delicate fine lines, flower motifs",
    ),
    "anime_jp_shounen_action": S(
        "Anime JP Shounen Action",
        "a shounen action anime female character",
        "tight battle bodysuit, high-slit combat outfit, bold sexy design",
        "dramatic action backdrop, motion-blur energy lines",
        "high-contrast dramatic lighting, action highlights",
        "shounen action anime style, dynamic bold linework, high contrast, energetic motion, vivid colors",
    ),
    "anime_jp_seinen_gritty": S(
        "Anime JP Seinen Gritty",
        "a seinen manga female character",
        "mature provocative outfit, sleek latex bodysuit, sophisticated edgy fashion",
        "moody urban night, atmospheric shadows",
        "dramatic low-key lighting, deep shadows",
        "seinen manga illustration style, rough detailed penwork, muted moody palette, mature realistic proportions",
    ),
    "anime_jp_makoto_watercolor": S(
        "Anime JP Makoto Watercolor",
        "an anime female character in Makoto-style watercolor",
        "soft summer dress, gentle figure-flattering fashion, delicate glamour",
        "breathtaking sky with volumetric clouds, lush scenery, lens flare",
        "luminous backlight, radiant god rays, golden glow",
        "Makoto Shinkai-style anime illustration, hyper-detailed luminous backgrounds, watercolor light, emotional atmosphere",
    ),
    "anime_jp_ghibli_soft": S(
        "Anime JP Ghibli Soft",
        "a hand-drawn anime female character, Ghibli-inspired",
        "flowing elegant dress, graceful feminine fashion, soft glamour",
        "lush green natural landscape, rolling hills, warm sky",
        "soft warm natural daylight, gentle ambient glow",
        "Ghibli-inspired hand-drawn anime style, soft watercolor backgrounds, warm gentle palette, wholesome atmosphere",
    ),
    "anime_jp_ecchi_glossy": S(
        "Anime JP Ecchi Glossy",
        "an ecchi-style glamour anime female character",
        "skimpy micro bikini, revealing lingerie-inspired outfit, bold ecchi fanservice design",
        "sunny beach or steamy onsen, glossy bright backdrop",
        "bright glossy lighting, sensual highlights",
        "glossy ecchi anime style, glamorous curvy proportions, shiny rendering, vivid fanservice aesthetic",
    ),
    "anime_jp_gekiga_noir": S(
        "Anime JP Gekiga Noir",
        "a gekiga-style mature anime female character",
        "sleek black latex catsuit, fishnet stockings, edgy fetish-noir fashion",
        "gritty noir alley at night, hard shadows and smoke",
        "harsh chiaroscuro lighting, deep noir contrast",
        "gekiga (dramatic adult manga) style, gritty heavy ink, realistic mature anatomy, hard-boiled noir mood",
    ),
    "anime_jp_pinup_retro": S(
        "Anime JP Pinup Retro",
        "a Showa-era pinup anime female character",
        "vintage pin-up lingerie, retro garter and stockings, playful seductive outfit",
        "retro Showa interior, vintage pin-up calendar setting",
        "warm retro glamour lighting, soft pin-up glow",
        "Showa retro pin-up illustration style, glossy vintage rendering, playful cheesecake glamour, warm nostalgic palette",
    ),

    # ─────────────────────────────── 한국 (7) ───────────────────────────────
    "anime_kr_webtoon_glossy": S(
        "Anime KR Webtoon Glossy",
        "a Korean webtoon female character, full-color glossy",
        "trendy chic K-fashion, plunging bodycon dress, sexy stylish design",
        "modern Seoul street, soft pastel gradient background",
        "soft ambient lighting, glossy skin highlights",
        "Korean webtoon (manhwa) full-color style, glossy digital coloring, clean lineart, K-beauty aesthetic, vivid trendy palette",
    ),
    "anime_kr_romance_soft": S(
        "Anime KR Romance Soft",
        "a romance webtoon female character",
        "soft feminine glamour outfit, elegant off-shoulder chic, alluring casual",
        "cozy cafe interior, warm soft-focus background",
        "warm soft romantic lighting, gentle glow",
        "Korean romance webtoon style, soft pastel digital coloring, delicate features, dreamy emotional mood",
    ),
    "anime_kr_action_manhwa": S(
        "Anime KR Action Manhwa",
        "an action manhwa female character",
        "sleek skin-tight combat suit, high-slit tactical outfit, edgy sexy design",
        "dramatic urban setting, dynamic perspective",
        "high-contrast cinematic lighting, sharp highlights",
        "Korean action manhwa style, sharp detailed lineart, high contrast cinematic coloring, dynamic dramatic composition",
    ),
    "anime_kr_lezhin_mature": S(
        "Anime KR Mature Webtoon",
        "a mature webtoon female character, sophisticated sensual style",
        "sheer lingerie, revealing silk slip dress, sophisticated seductive fashion",
        "sleek modern bedroom or city night, neon ambient glow",
        "moody cinematic lighting, refined sensual shadows",
        "mature Korean webtoon style, polished sophisticated rendering, refined sensual shading, cinematic intimate mood",
    ),
    "anime_kr_pastel_dream": S(
        "Anime KR Pastel Dream",
        "a pastel webtoon female character",
        "soft dreamy mini dress, pastel glamour fashion, sweet alluring design",
        "dreamy pastel gradient backdrop, floating soft light",
        "soft diffused dreamy lighting",
        "Korean pastel webtoon style, soft airy digital coloring, dreamy gradient palette, ethereal clean lineart",
    ),
    "anime_kr_lofi_chill": S(
        "Anime KR Lofi Chill",
        "a lofi-aesthetic anime female character",
        "cozy oversized shirt over lingerie, relaxed alluring loungewear",
        "cozy room or quiet street, warm muted tones",
        "soft warm ambient lighting, calm mood",
        "lofi aesthetic illustration style, muted warm palette, cozy chill atmosphere, soft textured shading",
    ),
    "anime_kr_noir_mature": S(
        "Anime KR Noir Mature",
        "a noir mature webtoon female character",
        "black latex bodysuit, sheer mesh accents, dark seductive fetish fashion",
        "dark rain-slick city night, neon reflections",
        "moody noir lighting, deep neon shadows",
        "dark mature Korean webtoon style, polished sensual rendering, high-contrast noir coloring, sultry cinematic mood",
    ),

    # ─────────────────────────────── 중국 (4) ───────────────────────────────
    "anime_cn_donghua_xianxia": S(
        "Anime CN Xianxia Donghua",
        "a xianxia donghua female character",
        "flowing sheer hanfu-inspired immortal robes, elegant revealing ethereal design",
        "mystical mountain peaks, floating petals, ethereal mist",
        "ethereal glowing light, soft immortal radiance",
        "Chinese xianxia donghua style, flowing elegant linework, ethereal soft coloring, traditional immortal-cultivation aesthetic",
    ),
    "anime_cn_guofeng_ink": S(
        "Anime CN Guofeng Ink",
        "a guofeng (national-style) female character",
        "elegant traditional Chinese-inspired attire, graceful figure-flattering design",
        "ink-wash mountain landscape, misty traditional scenery",
        "soft traditional lighting, ink-wash atmosphere",
        "Chinese guofeng ink-painting style, blending traditional shuimo ink-wash with anime, elegant flowing brushwork",
    ),
    "anime_cn_modern_donghua": S(
        "Anime CN Modern Donghua",
        "a modern Chinese donghua female character",
        "contemporary bodycon outfit, sleek sexy modern fashion",
        "modern Chinese cityscape, polished urban backdrop",
        "vibrant polished lighting, high saturation",
        "modern Chinese donghua style, high-saturation digital coloring, polished cel shading, vivid crisp rendering",
    ),
    "anime_cn_palace_drama": S(
        "Anime CN Palace Drama",
        "a Chinese palace-drama female character",
        "ornate sheer imperial robes, luxurious embroidered alluring costume, elaborate headdress",
        "opulent imperial palace interior, red and gold decor",
        "warm regal lighting, golden glow",
        "Chinese palace-drama illustration style, ornate detailed costume rendering, rich imperial palette, elegant refined lineart",
    ),

    # ─────────────────────────────── 미국 (6) ───────────────────────────────
    "anime_us_cartoon_bold": S(
        "Anime US Cartoon Bold",
        "an American cartoon-style female character",
        "tight crop top and mini, bold graphic sexy fashion",
        "stylized urban backdrop, flat graphic shapes",
        "flat bold lighting, graphic shadows",
        "modern American cartoon style, bold thick outlines, flat vivid colors, exaggerated stylized shapes",
    ),
    "anime_us_comic_ink": S(
        "Anime US Comic Ink",
        "an American comic-book female character",
        "skin-tight superheroine bodysuit, bold revealing comic costume",
        "dramatic comic-panel backdrop, action setting",
        "dramatic comic lighting, bold ink shadows",
        "American comic-book style, heavy ink shading, halftone dots, bold dynamic linework, saturated comic palette",
    ),
    "anime_us_pixar_stylized": S(
        "Anime US Pixar Stylized",
        "a stylized 3D-animation female character",
        "charming fitted outfit, appealing flattering stylized fashion",
        "warm inviting stylized environment, soft depth",
        "soft cinematic 3D lighting, warm global illumination",
        "Pixar-inspired stylized 3D animation style, appealing rounded forms, soft subsurface skin, cinematic render",
        "Pixar-inspired stylized 3D render, appealing animation look, soft cinematic shading, NOT photorealistic",
    ),
    "anime_us_disney_classic": S(
        "Anime US Disney Classic",
        "a classic-cartoon-style female character",
        "charming elegant gown, timeless flattering animated fashion",
        "storybook background, warm classic scenery",
        "warm classic cel lighting, soft glow",
        "classic hand-drawn cartoon style, smooth clean cel animation, warm expressive features, timeless animated look",
    ),
    "anime_us_pinup_classic": S(
        "Anime US Pinup Classic",
        "a classic American pin-up style female character",
        "vintage pin-up lingerie, retro corset and stockings, playful seductive glamour",
        "retro 1950s American interior, classic pin-up setting",
        "warm glamour lighting, soft retro glow",
        "classic American pin-up illustration style, glossy airbrushed rendering, playful cheesecake glamour, vintage saturated palette",
    ),
    "anime_us_badgirl_comic": S(
        "Anime US Badgirl Comic",
        "a 90s bad-girl comic female character",
        "skimpy revealing battle outfit, torn fishnets, edgy provocative comic costume",
        "dark gritty comic backdrop, dramatic action setting",
        "high-contrast dramatic lighting, bold ink shadows",
        "1990s bad-girl comic style, exaggerated curvy proportions, heavy ink, dynamic provocative rendering, saturated palette",
    ),

    # ─────────────────────────────── 유럽 (3) ───────────────────────────────
    "anime_eu_ligne_claire": S(
        "Anime EU Ligne Claire",
        "a European bande-dessinee female character",
        "clean chic dress, refined figure-flattering European fashion",
        "detailed European city or interior, clear flat backdrop",
        "even clear lighting, flat uniform shadows",
        "European ligne claire (clear line) style, uniform clean outlines, flat solid colors, detailed precise backgrounds",
    ),
    "anime_eu_graphic_novel": S(
        "Anime EU Graphic Novel",
        "a European graphic-novel female character",
        "sophisticated revealing outfit, artful sensual European fashion",
        "atmospheric European setting, moody detailed backdrop",
        "moody atmospheric lighting, painterly shadows",
        "European graphic-novel style, painterly textured coloring, mature sophisticated rendering, artful atmospheric mood",
    ),
    "anime_eu_erotic_bd": S(
        "Anime EU Erotic BD",
        "a sensual European adult bande-dessinee female character",
        "sheer lingerie, revealing silk and lace, sophisticated erotic European fashion",
        "elegant boudoir or moody European interior",
        "soft sensual lighting, warm intimate glow",
        "European erotic BD illustration style, fluid sensual linework, refined painterly coloring, sophisticated adult mood",
    ),

    # ─────────────────────────────── 무드 (1) ───────────────────────────────
    "anime_noir_silhouette": S(
        "Anime Noir Silhouette",
        "a noir silhouette-style anime female character",
        "sleek revealing silhouette outfit, sheer accents catching light, seductive minimal fashion",
        "dark noir backdrop, single dramatic light source, deep shadow",
        "extreme high-contrast rim light, silhouette-defining glow",
        "noir silhouette illustration style, dramatic backlit forms, minimal high-contrast rendering, sultry shadow-play",
    ),
}


def main():
    if not os.path.isdir(PRESETS_DIR):
        print(f"[ERROR] '{PRESETS_DIR}' folder not found. Run from project root.")
        return
    by_region = {"jp": 0, "kr": 0, "cn": 0, "us": 0, "eu": 0, "noir": 0}
    created, overwritten = 0, 0
    for name, data in PRESETS.items():
        path = os.path.join(PRESETS_DIR, f"{name}.json")
        exists = os.path.exists(path)
        if exists and not OVERWRITE:
            print(f"[SKIP] {name}.json already exists")
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        region = name.split("_")[1] if name != "anime_noir_silhouette" else "noir"
        by_region[region] = by_region.get(region, 0) + 1
        if exists:
            print(f"[OVERWRITE] {name}.json")
            overwritten += 1
        else:
            print(f"[OK]        {name}.json")
            created += 1
    print(f"\nDONE: new {created} / overwritten {overwritten} / total defined {len(PRESETS)}")
    print(f"by region: JP {by_region['jp']} / KR {by_region['kr']} / CN {by_region['cn']} / US {by_region['us']} / EU {by_region['eu']} / mood {by_region['noir']}")
    print("\nNext: dashboard.py에 '애니 아트스타일' 카테고리 신설 + 32개 등록 (별도 패치)")
    print("      us_pixar_stylized는 3D 스타일이라 그림체 검증 시 따로 확인")


if __name__ == "__main__":
    main()
