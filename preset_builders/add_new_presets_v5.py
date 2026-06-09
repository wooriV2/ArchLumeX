"""
LumineX - 상황/계절/날씨 프리셋 추가 스크립트 v3.8
실행: python add_new_presets_v5.py
상황 + 계절/날씨 특화 컨셉 30개
"""

import json
import os

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")
os.makedirs(PRESETS_DIR, exist_ok=True)

NEW_PRESETS_V38 = {

    # ── 스포츠/액티비티 ──────────────────────────────────────
    "boxing_glamour": {
        "tag": "Boxing Glamour",
        "subject": "a fierce glamorous boxing female model",
        "body": "power fitness model, very muscular defined body, strong arms and legs, athletic powerful build",
        "outfit": "boxing glamour outfit, satin boxing shorts, sports bra, boxing gloves, champion belt",
        "material": "satin performance fabric, athletic luxury textile",
        "environment": "luxury boxing ring, dramatic spotlight, smoke effects",
        "lighting": "dramatic boxing ring spotlight, powerful athletic atmosphere",
        "style": "boxing glamour editorial, champion sports photography",
        "quality": "shot on Canon EOS R5, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },
    "pole_art": {
        "tag": "Pole Art",
        "subject": "a spectacular pole dance artist female model",
        "body": "athletic fitness model, defined abs, toned muscular legs, acrobatic powerful physique",
        "outfit": "pole dance performance costume, sequin bodysuit, artistic acrobatic styling",
        "material": "iridescent sequin fabric, performance stretch textile",
        "environment": "dramatic dark stage, single chrome pole, spotlight",
        "lighting": "dramatic stage spotlight, dark atmosphere, pole chrome reflections",
        "style": "pole art editorial, Cirque du Soleil inspired photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },
    "yoga_goddess": {
        "tag": "Yoga Goddess",
        "subject": "a serene yoga goddess female model",
        "body": "slim toned model, lean athletic build, graceful flexible figure",
        "outfit": "luxury yoga outfit, high-waist leggings, sports bra, ethereal flowing layers",
        "material": "luxury performance fabric, soft stretch textile",
        "environment": "Bali cliff temple, ocean sunrise, golden morning light",
        "lighting": "golden hour sunrise, warm spiritual atmosphere, skin luminosity",
        "style": "luxury yoga editorial, mindful beauty photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "ski_chalet": {
        "tag": "Ski Chalet",
        "subject": "a glamorous ski resort female model",
        "body": "slim toned model, lean elegant figure, athletic refined presence",
        "outfit": "luxury ski resort outfit, fitted ski suit, fur trim, glamorous winter fashion",
        "material": "luxury performance ski fabric, fur trim textile",
        "environment": "luxury Alpine ski chalet, snow-covered mountains, fireplace warmth",
        "lighting": "warm golden firelight, snowy Alpine atmosphere, cozy luxury",
        "style": "luxury ski resort editorial, Alpine glamour photography",
        "quality": "shot on Canon EOS R5, cool blue color grade, cold steel tones, portrait 2:3 vertical"
    },
    "scuba_goddess": {
        "tag": "Scuba Goddess",
        "subject": "a ethereal underwater goddess female model",
        "body": "athletic fitness model, toned body, long legs, underwater grace",
        "outfit": "luxury diving wetsuit, sleek fitted underwater suit, ocean goddess styling",
        "material": "sleek neoprene fabric, underwater performance textile",
        "environment": "crystal clear tropical ocean, coral reef, underwater paradise",
        "lighting": "underwater caustic light, turquoise ocean glow, magical underwater illumination",
        "style": "underwater editorial, ocean goddess fashion photography",
        "quality": "shot on Hasselblad H6D, emerald green color grade, portrait 2:3 vertical"
    },

    # ── 파티/나이트라이프 ────────────────────────────────────
    "red_carpet": {
        "tag": "Red Carpet",
        "subject": "a spectacular red carpet female model",
        "body": "VS 앤젤 — 완벽한 VS 글래머",
        "outfit": "dramatic red carpet gown, plunging neckline, dramatic train, crystal embellished",
        "material": "crystal embellished couture fabric, luxury red carpet textile",
        "environment": "Hollywood movie premiere, red carpet, paparazzi flashes, velvet rope",
        "lighting": "paparazzi flash lights, red carpet glamour lighting, star atmosphere",
        "style": "Hollywood red carpet editorial, Academy Awards glamour photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },
    "masquerade_ball": {
        "tag": "Masquerade Ball",
        "subject": "a mysterious masquerade ball female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "Venetian masquerade gown, ornate mask, corseted bodice, dramatic ball gown",
        "material": "rich brocade fabric, jeweled masquerade textile, gold embroidery",
        "environment": "Venice carnival palazzo, ornate ballroom, candlelight, masked guests",
        "lighting": "warm candlelight, mysterious masquerade atmosphere, golden glow",
        "style": "Venetian masquerade editorial, dark luxury ball photography",
        "quality": "shot on Phase One XF IQ4, dark moody color grade, portrait 2:3 vertical"
    },
    "music_festival": {
        "tag": "Music Festival",
        "subject": "a vibrant music festival female model",
        "body": "athletic fitness model, toned body, energetic festival presence",
        "outfit": "Coachella festival outfit, crop top, high-waist shorts, bohemian accessories, body glitter",
        "material": "festival fashion fabric, boho chic textile, holographic accents",
        "environment": "Coachella outdoor festival, stage lights, palm trees, desert sunset",
        "lighting": "festival stage lights, golden desert sunset, colorful atmosphere",
        "style": "Coachella fashion editorial, music festival glamour photography",
        "quality": "shot on Sony A7R V, warm golden film grade, portrait 2:3 vertical"
    },
    "nightclub_vip": {
        "tag": "Nightclub VIP",
        "subject": "a fierce nightclub VIP female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "nightclub VIP outfit, metallic mini dress, strappy heels, club glamour",
        "material": "metallic mirror fabric, high-gloss club textile",
        "environment": "exclusive VIP nightclub, neon lights, bottle service, luxury club",
        "lighting": "neon club lighting, strobe effects, dark luxury nightclub atmosphere",
        "style": "nightclub VIP editorial, club glamour photography",
        "quality": "shot on Sony A7R V, purple moody color grade, portrait 2:3 vertical"
    },
    "rooftop_party": {
        "tag": "Rooftop Party",
        "subject": "a glamorous rooftop cocktail party female model",
        "body": "slim toned model, lean elegant figure, sophisticated party presence",
        "outfit": "cocktail party dress, elegant mini dress, city party glamour, champagne in hand",
        "material": "silk satin fabric, luxury cocktail textile",
        "environment": "luxury rooftop bar, city skyline at dusk, cocktail atmosphere",
        "lighting": "golden dusk city light, rooftop party atmosphere, warm champagne glow",
        "style": "rooftop party editorial, urban luxury photography",
        "quality": "shot on Canon EOS R5, cinematic teal and orange color grade, portrait 2:3 vertical"
    },

    # ── 럭셔리 라이프스타일 ──────────────────────────────────
    "luxury_shopping": {
        "tag": "Luxury Shopping",
        "subject": "a glamorous luxury shopping female model",
        "body": "slender elegant model, slim narrow frame, refined fashion presence",
        "outfit": "luxury shopping outfit, chic designer ensemble, shopping bags, Chanel accessories",
        "material": "luxury fashion fabric, designer textile",
        "environment": "Champs-Elysées Paris, luxury boutique, designer shopping, elegant street",
        "lighting": "Parisian golden hour, luxury boutique lighting, elegant atmosphere",
        "style": "luxury shopping editorial, Paris fashion photography",
        "quality": "shot on Leica SL2, warm golden film grade, portrait 2:3 vertical"
    },
    "art_gallery": {
        "tag": "Art Gallery",
        "subject": "a sophisticated art gallery female model",
        "body": "slender elegant model, intellectual refined presence, artistic elegance",
        "outfit": "art gallery opening outfit, minimalist luxury dress, artistic accessories",
        "material": "structured minimal fabric, luxury gallery textile",
        "environment": "contemporary art gallery opening, modern art on walls, white cube gallery",
        "lighting": "gallery spotlight, clean white gallery light, artistic atmosphere",
        "style": "art gallery editorial, contemporary luxury photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },
    "private_jet": {
        "tag": "Private Jet",
        "subject": "a ultra-luxury private jet female model",
        "body": "slim toned model, lean elegant figure, ultra-luxury presence",
        "outfit": "private jet luxury outfit, cashmere loungewear, diamond jewelry, ultra-luxury casual",
        "material": "cashmere luxury fabric, ultra-premium textile",
        "environment": "private jet interior, leather seats, champagne, clouds outside window",
        "lighting": "soft private jet cabin lighting, luxury aviation atmosphere",
        "style": "private jet lifestyle editorial, ultra-luxury photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "wine_tasting": {
        "tag": "Wine Tasting",
        "subject": "a sophisticated wine tasting female model",
        "body": "slender elegant model, refined sophisticated presence",
        "outfit": "wine tasting elegant outfit, silk blouse, tailored trousers, wine glass prop",
        "material": "silk luxury fabric, refined wine country textile",
        "environment": "Bordeaux wine cellar, vintage barrels, stone walls, candlelight",
        "lighting": "warm candlelight, wine cellar amber glow, intimate luxury",
        "style": "wine country editorial, Bordeaux luxury photography",
        "quality": "shot on Leica SL2, warm golden film grade, portrait 2:3 vertical"
    },
    "helipad": {
        "tag": "Helipad",
        "subject": "a powerful helipad glamour female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, commanding presence",
        "outfit": "power outfit on helipad, structured blazer, mini skirt, wind-blown drama",
        "material": "structured power fabric, luxury urban textile",
        "environment": "skyscraper helipad, dramatic city panorama, helicopter in background",
        "lighting": "dramatic golden hour, wind effect, powerful urban atmosphere",
        "style": "power editorial, urban luxury helipad photography",
        "quality": "shot on Canon EOS R5, cinematic teal and orange color grade, portrait 2:3 vertical"
    },

    # ── 자연/야외 ────────────────────────────────────────────
    "sunflower_field": {
        "tag": "Sunflower Field",
        "subject": "a radiant sunflower field female model",
        "body": "soft glamour model, feminine gentle curves, warm natural beauty",
        "outfit": "summer dress in sunflower field, flowing yellow sundress, natural beauty",
        "material": "lightweight chiffon fabric, flowing summer textile",
        "environment": "vast sunflower field, golden hour sunlight, Provence landscape",
        "lighting": "intense golden hour backlight, sunflower glow, warm summer light",
        "style": "sunflower field editorial, golden summer photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },
    "autumn_forest": {
        "tag": "Autumn Forest",
        "subject": "a romantic autumn forest female model",
        "body": "slim toned model, lean elegant figure, romantic autumn presence",
        "outfit": "autumn fashion outfit, burgundy wrap coat, knee-high boots, fall glamour",
        "material": "luxury wool fabric, rich autumn textile",
        "environment": "autumn forest, golden red leaves, misty morning, magical fall atmosphere",
        "lighting": "dappled autumn golden light, warm orange atmosphere, fall magic",
        "style": "autumn editorial, fall fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "vineyard_harvest": {
        "tag": "Vineyard Harvest",
        "subject": "a romantic vineyard harvest female model",
        "body": "soft glamour model, feminine gentle curves, rustic romantic presence",
        "outfit": "vineyard harvest outfit, flowing linen dress, grape harvest basket, rustic glamour",
        "material": "natural linen fabric, rustic luxury harvest textile",
        "environment": "Tuscany vineyard at harvest, golden vine rows, Italian countryside",
        "lighting": "Tuscany golden hour, warm harvest atmosphere, Italian countryside glow",
        "style": "Tuscany vineyard editorial, harvest luxury photography",
        "quality": "shot on Leica SL2, warm golden film grade, portrait 2:3 vertical"
    },
    "cliff_edge": {
        "tag": "Cliff Edge",
        "subject": "a powerful cliff edge female model",
        "body": "slim toned model, powerful athletic presence, commanding cliff figure",
        "outfit": "dramatic cliff edge outfit, windswept flowing dress, powerful editorial",
        "material": "lightweight chiffon fabric, dramatic windswept textile",
        "environment": "dramatic coastal cliff edge, crashing waves below, stormy sky",
        "lighting": "dramatic storm light, powerful coastal atmosphere, wind and spray",
        "style": "dramatic cliff editorial, powerful nature photography",
        "quality": "shot on Nikon Z9, dark moody color grade, portrait 2:3 vertical"
    },

    # ── 문화/예술 ────────────────────────────────────────────
    "opera_night": {
        "tag": "Opera Night",
        "subject": "a glamorous opera night female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic elegance",
        "outfit": "opera night gown, dramatic floor-length dress, opera gloves, diamond jewelry",
        "material": "rich silk satin, opera luxury textile, diamond embellishment",
        "environment": "grand opera house interior, red velvet, gold balconies, chandelier",
        "lighting": "warm opera house chandelier, dramatic stage glow, luxury atmosphere",
        "style": "opera night editorial, grand luxury photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },
    "jazz_club": {
        "tag": "Jazz Club",
        "subject": "a sultry jazz club female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, jazz age glamour",
        "outfit": "jazz club outfit, vintage sequin dress, feather boa, jazz age glamour",
        "material": "vintage sequin fabric, jazz era luxury textile",
        "environment": "intimate jazz club, dim lighting, saxophone player, smoke atmosphere",
        "lighting": "dim warm jazz club lighting, intimate smoky atmosphere, vintage glow",
        "style": "jazz club editorial, vintage glamour photography",
        "quality": "shot on Leica SL2, vintage film grain, faded colors, portrait 2:3 vertical"
    },

    # ── 봄 계절 ──────────────────────────────────────────────
    "cherry_blossom": {
        "tag": "Cherry Blossom",
        "subject": "a ethereal cherry blossom female model",
        "body": "soft glamour model, feminine gentle curves, delicate spring presence",
        "outfit": "spring cherry blossom outfit, flowing pink dress, delicate floral accessories",
        "material": "lightweight chiffon fabric, soft pink floral textile",
        "environment": "cherry blossom tunnel, Japan spring, falling pink petals, Kyoto path",
        "lighting": "soft spring diffused light, pink petal bokeh, dreamy atmosphere",
        "style": "cherry blossom editorial, Japanese spring photography",
        "quality": "shot on Hasselblad H6D, soft pink glamour grade, rose gold tones, portrait 2:3 vertical"
    },
    "tulip_field": {
        "tag": "Tulip Field",
        "subject": "a vibrant tulip field female model",
        "body": "slim toned model, lean elegant figure, fresh spring presence",
        "outfit": "spring tulip field outfit, colorful midi dress, fresh spring fashion",
        "material": "lightweight cotton fabric, vibrant spring textile",
        "environment": "Netherlands tulip field, rows of colorful tulips, windmill background",
        "lighting": "bright spring daylight, vibrant color saturation, fresh atmosphere",
        "style": "Dutch tulip field editorial, spring fashion photography",
        "quality": "shot on Canon EOS R5, high key bright white tone, portrait 2:3 vertical"
    },
    "spring_rain": {
        "tag": "Spring Rain",
        "subject": "a romantic spring rain female model",
        "body": "soft glamour model, feminine gentle curves, romantic spring presence",
        "outfit": "spring rain outfit, elegant trench coat, clear umbrella, fresh spring glamour",
        "material": "luxury trench coat fabric, spring rain textile",
        "environment": "Paris spring rain, wet cobblestones, cherry blossoms, romantic street",
        "lighting": "soft overcast spring light, rain reflection glow, romantic atmosphere",
        "style": "Paris spring rain editorial, romantic fashion photography",
        "quality": "shot on Leica SL2, soft pink glamour grade, rose gold tones, portrait 2:3 vertical"
    },

    # ── 가을 계절 ────────────────────────────────────────────
    "halloween_queen": {
        "tag": "Halloween Queen",
        "subject": "a fierce Halloween queen female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dark glamour presence",
        "outfit": "Halloween queen costume, dark witch dress, spider web accessories, dramatic dark glamour",
        "material": "dark velvet fabric, Halloween luxury textile, spider web lace",
        "environment": "haunted mansion, pumpkins, full moon, Halloween atmosphere",
        "lighting": "moonlight through trees, Halloween orange glow, spooky dramatic atmosphere",
        "style": "Halloween glamour editorial, dark festive photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },

    # ── 겨울 계절 ────────────────────────────────────────────
    "winter_forest": {
        "tag": "Winter Forest",
        "subject": "a ethereal winter forest female model",
        "body": "slim toned model, lean elegant figure, ethereal winter presence",
        "outfit": "winter forest outfit, white fur coat, knee-high boots, winter goddess styling",
        "material": "luxury white fur fabric, winter luxury textile",
        "environment": "snow-covered birch forest, falling snowflakes, magical winter wonderland",
        "lighting": "soft winter diffused light, snow reflection glow, magical atmosphere",
        "style": "winter forest editorial, snow glamour photography",
        "quality": "shot on Hasselblad H6D, cool blue color grade, cold steel tones, portrait 2:3 vertical"
    },
    "blizzard_queen": {
        "tag": "Blizzard Queen",
        "subject": "a powerful blizzard queen female model",
        "body": "power fitness model, very muscular defined body, powerful winter goddess",
        "outfit": "blizzard queen costume, ice armor, dramatic white fur cape, winter warrior",
        "material": "ice crystal texture fabric, winter warrior textile, white fur",
        "environment": "dramatic Arctic blizzard, swirling snow, ice and wind, frozen tundra",
        "lighting": "cold blue blizzard light, dramatic storm atmosphere, ice reflections",
        "style": "blizzard queen editorial, ice warrior photography",
        "quality": "shot on Nikon Z9, cool blue color grade, cold steel tones, portrait 2:3 vertical"
    },
    "christmas_glamour": {
        "tag": "Christmas Glamour",
        "subject": "a glamorous Christmas female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, festive glamour",
        "outfit": "Christmas glamour outfit, red velvet mini dress, white fur trim, festive luxury",
        "material": "red velvet fabric, white fur trim, Christmas luxury textile",
        "environment": "luxury Christmas interior, decorated Christmas tree, fireplace, golden lights",
        "lighting": "warm Christmas tree lights, golden festive glow, cozy luxury atmosphere",
        "style": "Christmas glamour editorial, festive luxury photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },
    "new_year_countdown": {
        "tag": "New Year Countdown",
        "subject": "a spectacular New Year countdown female model",
        "body": "VS 앤젤 — 완벽한 VS 글래머",
        "outfit": "New Year glamour outfit, silver sequin mini dress, champagne glass, celebration",
        "material": "silver iridescent sequin fabric, New Year celebration textile",
        "environment": "New Year countdown celebration, fireworks, champagne, city skyline midnight",
        "lighting": "fireworks light, champagne sparkle, midnight celebration atmosphere",
        "style": "New Year glamour editorial, celebration luxury photography",
        "quality": "shot on Sony A7R V, high key bright white tone, portrait 2:3 vertical"
    },
}


def main():
    print("\n  ✦ LumineX v3.8 상황/계절/날씨 프리셋 추가 시작...\n")
    created = 0
    skipped = 0

    for name, data in NEW_PRESETS_V38.items():
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
    print("  - 스포츠/액티비티 (복싱/폴댄스/요가/스키/스쿠버)        × 5")
    print("  - 파티/나이트라이프 (레드카펫/가면무도회/페스티벌/클럽 등) × 5")
    print("  - 럭셔리 라이프스타일 (쇼핑/갤러리/제트/와인/헬리패드)    × 5")
    print("  - 자연/야외 (해바라기/단풍/포도원/절벽)                  × 4")
    print("  - 문화/예술 (오페라/재즈클럽)                           × 2")
    print("  - 봄 (벚꽃/튤립/봄비)                                  × 3")
    print("  - 가을 (할로윈)                                        × 1")
    print("  - 겨울 (설원/눈보라여왕/크리스마스/새해)                 × 4")
    print(f"  총 29개 신규 프리셋\n")


if __name__ == "__main__":
    main()