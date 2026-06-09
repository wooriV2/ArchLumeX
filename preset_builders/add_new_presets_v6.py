"""
LumineX - 프리셋 추가 스크립트 v3.9
실행: python add_new_presets_v6.py
기존 카테고리 보완 + 관능적 계열 추가
총 25개
"""

import json
import os

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")
os.makedirs(PRESETS_DIR, exist_ok=True)

NEW_PRESETS_V39 = {

    # ── 계절/여름 (신규) ─────────────────────────────────────
    "summer_beach": {
        "tag": "Summer Beach",
        "subject": "a radiant summer beach goddess female model",
        "body": "athletic fitness model, toned body, sun-kissed beach goddess, long legs",
        "outfit": "luxury string bikini, high-cut sides, beach glamour editorial",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "pristine white sand beach, crystal turquoise water, golden summer",
        "lighting": "intense golden hour backlight, skin luminosity, beach goddess glow",
        "style": "Sports Illustrated beach editorial, luxury summer photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },
    "golden_summer": {
        "tag": "Golden Summer",
        "subject": "a glamorous golden summer female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "golden summer dress, flowing slit maxi dress, summer glamour editorial",
        "material": "liquid gold satin, ultra-glossy wet-look finish",
        "environment": "Amalfi Coast golden summer, Italian seaside, warm amber sky",
        "lighting": "intense golden hour backlight, Amalfi golden glow, skin luminosity",
        "style": "Vogue summer editorial, Italian glamour photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "tropical_night": {
        "tag": "Tropical Night",
        "subject": "a mysterious tropical night female model",
        "body": "glamour curvy model, dramatic waist-to-hip ratio, tropical exotic presence",
        "outfit": "tropical night outfit, slinky sequin dress, exotic night glamour",
        "material": "iridescent sequins, tropical shimmer textile",
        "environment": "Bali tropical night, tiki torches, ocean breeze, exotic night",
        "lighting": "warm tiki torch light, tropical night atmosphere, mysterious glow",
        "style": "tropical night editorial, exotic luxury photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },
    "pool_goddess": {
        "tag": "Pool Goddess",
        "subject": "a stunning pool goddess female model",
        "body": "VS 앤젤 — 완벽한 VS 글래머",
        "outfit": "luxury high-cut one-piece swimsuit, pool goddess editorial",
        "material": "metallic liquid fabric, iridescent pool shimmer",
        "environment": "luxury infinity pool, blue water reflection, summer paradise",
        "lighting": "underwater pool light reflection, rippling aqua light patterns",
        "style": "luxury pool editorial, summer glamour photography",
        "quality": "shot on Hasselblad H6D, cool blue color grade, portrait 2:3 vertical"
    },

    # ── 계절/봄 보완 ─────────────────────────────────────────
    "lavender_field": {
        "tag": "Lavender Field",
        "subject": "a ethereal lavender field female model",
        "body": "slim toned model, lean elegant figure, romantic spring presence",
        "outfit": "Provence lavender outfit, flowing purple dress, romantic spring fashion",
        "material": "lightweight chiffon fabric, soft lavender textile",
        "environment": "Provence lavender field, rows of purple lavender, French countryside",
        "lighting": "soft golden hour light, lavender purple atmosphere, dreamy glow",
        "style": "Provence lavender editorial, French countryside photography",
        "quality": "shot on Hasselblad H6D, soft pink glamour grade, rose gold tones, portrait 2:3 vertical"
    },

    # ── 판타지/신화 보완 ─────────────────────────────────────
    "dark_mermaid": {
        "tag": "Dark Mermaid",
        "subject": "a seductive dark mermaid female model",
        "body": "glamour curvy model, dramatic curves, mysterious underwater presence",
        "outfit": "dark mermaid costume, iridescent scale bodysuit, dramatic fin tail, seductive underwater",
        "material": "iridescent scale fabric, deep ocean textile, dark mermaid material",
        "environment": "dark deep ocean, bioluminescent creatures, mysterious underwater darkness",
        "lighting": "bioluminescent blue-green glow, deep sea mysterious light",
        "style": "dark mermaid editorial, underwater fantasy photography",
        "quality": "shot on Sony A7R V, cool blue color grade, cold steel tones, portrait 2:3 vertical"
    },
    "vampire_queen": {
        "tag": "Vampire Queen",
        "subject": "a powerful vampire queen female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, immortal dark glamour",
        "outfit": "vampire queen gown, deep plunging neckline, dramatic black cape, gothic luxury",
        "material": "black velvet, blood red silk lining, vampire luxury textile",
        "environment": "gothic vampire castle, moonlight through stained glass, dramatic darkness",
        "lighting": "moonlight dramatic shadows, gothic candlelight, vampire atmosphere",
        "style": "vampire queen editorial, dark gothic luxury photography",
        "quality": "shot on Phase One XF IQ4, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },
    "angel_fallen": {
        "tag": "Fallen Angel",
        "subject": "a dramatic fallen angel female model",
        "body": "slim toned model, ethereal powerful presence, fallen divine figure",
        "outfit": "fallen angel costume, tattered white dress, dark feather wings, dramatic divine",
        "material": "torn silk fabric, dark feather textile, fallen angel material",
        "environment": "dramatic storm sky, lightning, dark clouds, fallen from heaven",
        "lighting": "dramatic storm lightning, dark divine atmosphere, fallen light",
        "style": "fallen angel editorial, dark divine fashion photography",
        "quality": "shot on Nikon Z9, dark moody color grade, portrait 2:3 vertical"
    },
    "moon_goddess": {
        "tag": "Moon Goddess",
        "subject": "a ethereal moon goddess female model",
        "body": "slim toned model, ethereal divine presence, lunar goddess figure",
        "outfit": "moon goddess gown, silver flowing robes, crescent moon crown, ethereal divine",
        "material": "silver silk fabric, moonlight iridescent textile",
        "environment": "full moon night, silver moonlight, cosmic atmosphere, stars",
        "lighting": "moonlight, silvery blue natural light, mysterious outdoor glow",
        "style": "moon goddess editorial, celestial fantasy photography",
        "quality": "shot on Hasselblad H6D, cool blue color grade, cold steel tones, portrait 2:3 vertical"
    },
    "demon_goddess": {
        "tag": "Demon Goddess",
        "subject": "a powerful demon goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dark powerful goddess",
        "outfit": "demon goddess costume, dark armor, dramatic horns, seductive dark power",
        "material": "dark metallic fabric, demon luxury textile, obsidian material",
        "environment": "dark underworld, volcanic fire, dramatic darkness, infernal atmosphere",
        "lighting": "red under-glow, dramatic volcanic light, demon fire atmosphere",
        "style": "demon goddess editorial, dark fantasy photography",
        "quality": "shot on Sony A7R V, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },

    # ── 사이버/미래 보완 ─────────────────────────────────────
    "holographic_city": {
        "tag": "Holographic City",
        "subject": "a futuristic holographic city female model",
        "body": "slim toned model, sleek futuristic presence, digital goddess figure",
        "outfit": "holographic fashion, light-reactive iridescent outfit, futuristic digital couture",
        "material": "holographic translucent fabric, digital iridescent material",
        "environment": "futuristic holographic city, floating data projections, neon holograms",
        "lighting": "holographic blue-purple light, digital glow, futuristic city atmosphere",
        "style": "holographic city editorial, futuristic fashion photography",
        "quality": "shot on Nikon Z9, purple moody color grade, portrait 2:3 vertical"
    },
    "neon_dystopia": {
        "tag": "Neon Dystopia",
        "subject": "a fierce neon dystopia female model",
        "body": "power fitness model, very muscular defined body, dystopian warrior presence",
        "outfit": "neon dystopia outfit, cyberpunk armor, neon accents, dystopian warrior fashion",
        "material": "dark matte performance fabric, neon accent textile",
        "environment": "neon dystopian city, rain-soaked streets, dark future atmosphere",
        "lighting": "multi-colored neon edge glow, cyberpunk light, wet reflections",
        "style": "neon dystopia editorial, cyberpunk warrior photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },

    # ── 겨울 보완 ────────────────────────────────────────────
    "ice_palace": {
        "tag": "Ice Palace",
        "subject": "a regal ice palace queen female model",
        "body": "slim toned model, ethereal regal presence, ice queen figure",
        "outfit": "ice palace queen gown, crystal ice dress, frozen couture, winter queen",
        "material": "crystal ice texture fabric, frozen luxury textile",
        "environment": "magical ice palace interior, crystal walls, frozen throne room",
        "lighting": "cold blue crystal light, ice palace glow, frozen magical atmosphere",
        "style": "ice palace editorial, frozen fantasy photography",
        "quality": "shot on Hasselblad H6D, cool blue color grade, cold steel tones, portrait 2:3 vertical"
    },

    # ── 문화/예술 보완 ───────────────────────────────────────
    "museum_glamour": {
        "tag": "Museum Glamour",
        "subject": "a sophisticated museum glamour female model",
        "body": "slender elegant model, intellectual refined presence, museum goddess",
        "outfit": "museum glamour outfit, elegant sculptural dress, artistic accessories",
        "material": "structured luxury fabric, museum editorial textile",
        "environment": "The Louvre Museum interior, grand ornate gallery halls, classical artwork",
        "lighting": "museum spotlight, classical gallery light, artistic atmosphere",
        "style": "museum glamour editorial, Louvre fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "jazz_age": {
        "tag": "Jazz Age",
        "subject": "a glamorous 1920s jazz age female model",
        "body": "slim toned model, 1920s flapper figure, art deco glamour presence",
        "outfit": "1920s flapper dress, art deco beading, feather headband, jazz age glamour",
        "material": "beaded art deco fabric, 1920s luxury textile, fringe detail",
        "environment": "1920s jazz speakeasy, art deco interior, smoky jazz club",
        "lighting": "warm jazz age amber light, art deco chandelier, vintage glow",
        "style": "jazz age editorial, 1920s glamour photography",
        "quality": "shot on Leica SL2, vintage film grain, faded colors, portrait 2:3 vertical"
    },
    "bohemian_paris": {
        "tag": "Bohemian Paris",
        "subject": "a free-spirited bohemian Paris female model",
        "body": "slim toned model, effortless Parisian presence, bohemian elegance",
        "outfit": "Parisian bohemian outfit, flowing layers, vintage accessories, effortless chic",
        "material": "lightweight chiffon fabric, vintage Parisian textile",
        "environment": "Montmartre Paris, artist studios, cobblestone streets, Seine river",
        "lighting": "soft Parisian golden hour, romantic French atmosphere",
        "style": "Parisian bohemian editorial, French lifestyle photography",
        "quality": "shot on Leica SL2, warm golden film grade, portrait 2:3 vertical"
    },

    # ── 완전 신규 ────────────────────────────────────────────
    "zombie_apocalypse": {
        "tag": "Zombie Apocalypse",
        "subject": "a fierce zombie apocalypse survivor female model",
        "body": "power fitness model, very muscular defined body, battle-hardened survivor",
        "outfit": "post-apocalyptic survivor outfit, torn tactical wear, battle scars, survivor glamour",
        "material": "distressed tactical fabric, post-apocalyptic textile",
        "environment": "abandoned destroyed city, zombie apocalypse wasteland, dramatic ruins",
        "lighting": "dramatic emergency red light, apocalyptic atmosphere, survival tension",
        "style": "zombie apocalypse editorial, post-apocalyptic fashion photography",
        "quality": "shot on Canon EOS R5, dark moody color grade, portrait 2:3 vertical"
    },
    "maasai_warrior": {
        "tag": "Maasai Warrior",
        "subject": "a powerful Maasai warrior goddess female model",
        "body": "slim toned model, powerful African presence, Maasai warrior goddess",
        "outfit": "Maasai warrior fashion, traditional shuka fabric, beaded jewelry, tribal glamour",
        "material": "traditional Maasai shuka fabric, beaded tribal textile",
        "environment": "East African savanna, acacia trees, golden African sunset",
        "lighting": "golden African hour, savanna warm glow, tribal atmosphere",
        "style": "Maasai warrior editorial, African tribal glamour photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },

    # ── 관능적/글래머 계열 ───────────────────────────────────
    "wet_look_goddess": {
        "tag": "Wet Look Goddess",
        "subject": "a glistening wet look goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "luxury bikini, wet look swimwear, soaking wet editorial",
        "material": "wet-look spandex, soaking wet appearance, body-hugging",
        "environment": "dramatic ocean wave, rain-soaked luxury, water goddess",
        "lighting": "strong rim backlight, silhouette definition, water glistening halo",
        "style": "Sports Illustrated wet editorial, water goddess photography",
        "quality": "shot on Canon EOS R5, cinematic teal and orange color grade, portrait 2:3 vertical"
    },
    "body_paint_art": {
        "tag": "Body Paint Art",
        "subject": "a artistic body paint female model",
        "body": "athletic fitness model, defined abs, toned body, body art canvas",
        "outfit": "full body paint art, intricate painted patterns, artistic body coverage",
        "material": "body paint, artistic painted skin, fine art body canvas",
        "environment": "pure white minimalist studio, seamless backdrop, art studio",
        "lighting": "professional studio strobe, high-contrast glamour lighting",
        "style": "body paint art editorial, fine art fashion photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },
    "goddess_draped": {
        "tag": "Goddess Draped",
        "subject": "a divine draped goddess female model",
        "body": "glamour curvy model, dramatic waist-to-hip ratio, goddess proportions",
        "outfit": "minimal draped silk, strategic fabric draping only, goddess minimal coverage",
        "material": "liquid silk satin, ultra-glossy draped fabric, goddess textile",
        "environment": "ancient marble temple, golden columns, divine atmosphere",
        "lighting": "golden divine light, marble column shadows, goddess atmosphere",
        "style": "goddess draped editorial, divine fashion photography",
        "quality": "shot on Phase One XF IQ4, warm golden film grade, portrait 2:3 vertical"
    },
    "lingerie_noir": {
        "tag": "Lingerie Noir",
        "subject": "a mysterious lingerie noir female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dark glamour presence",
        "outfit": "luxury dark lingerie editorial, silk lace set, noir glamour, fashion editorial",
        "material": "silk lace luxury fabric, noir lingerie textile",
        "environment": "dark baroque chamber, candlelight, opulent dark interior",
        "lighting": "flickering candlelight shadows, deep chiaroscuro, noir atmosphere",
        "style": "lingerie noir editorial, dark luxury fashion photography",
        "quality": "shot on Sony A7R V, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },
    "barely_there": {
        "tag": "Barely There",
        "subject": "a stunning barely there glamour female model",
        "body": "VS 앤젤 — 완벽한 VS 글래머",
        "outfit": "barely there luxury bikini, crystal embellished minimal swimwear, high fashion editorial",
        "material": "crystal embellished couture fabric, luxury minimal textile",
        "environment": "luxury private beach, crystal clear water, exclusive paradise",
        "lighting": "golden hour warm backlight, skin luminosity, paradise glow",
        "style": "Sports Illustrated barely there editorial, luxury swimwear photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
}


def main():
    print("\n  ✦ LumineX v3.9 프리셋 추가 시작...\n")
    created = 0
    skipped = 0

    for name, data in NEW_PRESETS_V39.items():
        path = os.path.join(PRESETS_DIR, f"{name}.json")
        if os.path.exists(path):
            print(f"  ⏭️  건너뜀: {name}.json")
            skipped += 1
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  ✅ 생성: {name}.json")
            created += 1

    print(f"\n  완료: 생성 {created}개 / 건너뜀 {skipped}개")
    total = len([f for f in os.listdir(PRESETS_DIR) if f.endswith('.json')])
    print(f"  총 프리셋: {total}개\n")
    print("  📋 추가된 카테고리:")
    print("  - 계절/여름 신규 (summer_beach/golden_summer/tropical_night/pool_goddess) × 4")
    print("  - 계절/봄 보완 (lavender_field)                                          × 1")
    print("  - 판타지/신화 보완 (dark_mermaid/vampire_queen/angel_fallen/moon/demon)   × 5")
    print("  - 사이버/미래 보완 (holographic_city/neon_dystopia)                      × 2")
    print("  - 겨울 보완 (ice_palace)                                                 × 1")
    print("  - 문화/예술 보완 (museum_glamour/jazz_age/bohemian_paris)                × 3")
    print("  - 완전 신규 (zombie_apocalypse/maasai_warrior)                           × 2")
    print("  - 관능적/글래머 (wet_look/body_paint/goddess_draped/lingerie_noir/barely) × 5")
    print(f"  총 23개 신규 프리셋\n")


if __name__ == "__main__":
    main()