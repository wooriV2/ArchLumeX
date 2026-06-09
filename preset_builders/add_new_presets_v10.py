"""
add_new_presets_v10.py
신규 프리셋 28개 추가

카테고리:
👘 전통 & 문화의상 (10개)
  kimono_silk, ao_dai_sheer, thai_temple, indian_bridal, moroccan_kaftan,
  persian_court, yoruba_glamour, balinese_goddess, chinese_qipao_slit, scottish_corset

🌸 계절 & 테마 (8개)
  first_snow, golden_autumn, midsummer_heat, rainy_season,
  harvest_moon, winter_solstice, cherry_blossom_night, tropical_monsoon

🍬 팝 & 카와이 신규 (10개)
  y2k_fairy, pink_champagne, cotton_candy, angel_baby, idol_stage,
  kitty_glam, strawberry_milk, cherry_pop, neon_kawaii, fairy_kei

※ 기존 에디토리얼에서 이동 (별도 작업):
  bubble_tea, doll_house, harajuku_doll, pastel_fairy, candy_rave, pop_art_glamour
  → 🍬 팝 & 카와이로 카테고리 재분류
"""

import json
import os
from pathlib import Path

PRESETS_DIR = Path("presets")
PRESETS_DIR.mkdir(exist_ok=True)

new_presets = {
    "kimono_silk": {
        "tag": "Kimono Silk",
        "subject": "a seductive Japanese kimono female model",
        "body": "slim elegant model, graceful elongated figure, delicate yet sensual presence",
        "outfit": "luxurious silk kimono sensuously draped open, obi sash loosened, deep neckline reveal, trailing fabric",
        "material": "ultra-glossy liquid satin silk, hand-painted floral kimono textile, gold obi sash",
        "environment": "traditional Japanese room, shoji screens, soft candlelight, tatami floor",
        "lighting": "warm amber candlelight, soft paper lantern glow, intimate golden atmosphere",
        "style": "sensual Japanese kimono editorial, haute couture Eastern glamour",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "ao_dai_sheer": {
        "tag": "Ao Dai Sheer",
        "subject": "a glamorous Vietnamese ao dai female model",
        "body": "slim elegant model, long graceful legs, slender waist, refined sensual silhouette",
        "outfit": "sheer transparent ao dai, form-fitting Vietnamese traditional dress, plunging neckline, side slit panels revealing silhouette",
        "material": "sheer silk organza, semi-transparent Vietnamese textile, delicate embroidered overlay",
        "environment": "ancient Vietnamese temple courtyard, lantern festival lights, lotus pond reflection",
        "lighting": "warm lantern glow, soft golden bokeh, romantic atmospheric light",
        "style": "sensual Vietnamese ao dai editorial, exotic Eastern fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden grade, portrait 2:3 vertical"
    },
    "thai_temple": {
        "tag": "Thai Temple",
        "subject": "a radiant Thai goddess female model",
        "body": "glamour model, elegant curves, powerful divine feminine presence",
        "outfit": "elaborate Thai traditional costume, golden chest piece, jeweled crown, draped silk panels, bare midriff",
        "material": "heavy gold brocade, silk satin panels, ornate gemstone encrusted accessories",
        "environment": "grand Thai Buddhist temple interior, golden Buddha backdrop, incense smoke",
        "lighting": "golden temple light, warm ceremonial glow, dramatic god rays through temple",
        "style": "Thai goddess editorial, divine Southeast Asian luxury fashion",
        "quality": "shot on Phase One XF IQ4, rich jewel tones, portrait 2:3 vertical"
    },
    "indian_bridal": {
        "tag": "Indian Bridal",
        "subject": "a breathtaking Indian bridal female model",
        "body": "glamour curvy model, dramatic hourglass figure, voluptuous feminine curves",
        "outfit": "opulent Indian bridal lehenga, heavily embroidered red and gold choli crop top, bare midriff, dramatic dupatta veil",
        "material": "rich silk brocade, zardozi gold embroidery, crystal and ruby encrusted fabric",
        "environment": "Mughal palace courtyard, marble archways, rose petals, golden dusk light",
        "lighting": "warm Mughal golden hour, dramatic directional light, jewel-toned atmosphere",
        "style": "Bollywood bridal editorial, Indian luxury fashion photography",
        "quality": "shot on Hasselblad H6D, rich warm golden grade, portrait 2:3 vertical"
    },
    "moroccan_kaftan": {
        "tag": "Moroccan Kaftan",
        "subject": "a seductive Moroccan kaftan female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "luxurious open-front kaftan revealing silhouette, intricate gold embroidery, plunging neckline, side-split hem",
        "material": "heavy silk kaftan fabric, hand-embroidered gold threadwork, sheer inner lining",
        "environment": "ornate Moroccan riad, mosaic tile courtyard, arched doorways, candlelight",
        "lighting": "warm Moroccan lantern light, intricate shadow patterns from mashrabiya screens",
        "style": "Moroccan luxury kaftan editorial, sensual North African fashion photography",
        "quality": "shot on Hasselblad H6D, warm amber color grade, portrait 2:3 vertical"
    },
    "persian_court": {
        "tag": "Persian Court",
        "subject": "a mesmerizing Persian court female model",
        "body": "luxury glamour model, defined waist, wide round hips, sophisticated voluptuous elegance",
        "outfit": "elaborate Persian court ensemble, jeweled bra top, flowing sheer harem pants, ornate headdress, layered veils",
        "material": "gossamer silk veils, heavily jeweled brocade, intricate Persian embroidery, gold chainmail",
        "environment": "ancient Persian palace, columned hall, silk curtains, oil lamp firelight",
        "lighting": "warm flickering oil lamp light, golden atmospheric haze, dramatic shadows",
        "style": "Persian court goddess editorial, ancient luxury fashion photography",
        "quality": "shot on Phase One XF IQ4, rich amber jewel grade, portrait 2:3 vertical"
    },
    "yoruba_glamour": {
        "tag": "Yoruba Glamour",
        "subject": "a powerful Yoruba goddess female model",
        "body": "Black beauty hourglass, dramatically wide round hips, ultra-narrow waist, thick thighs, African goddess proportions",
        "outfit": "elaborate Yoruba aso-oke ensemble reimagined, gele headwrap, bare midriff wrapper skirt, bold gold jewelry",
        "material": "rich woven aso-oke fabric, bold geometric textile, heavy gold jewelry",
        "environment": "Nigerian palace courtyard, tropical garden, golden afternoon light",
        "lighting": "warm golden African sunlight, rich skin luminosity, dramatic natural light",
        "style": "Yoruba goddess editorial, African luxury fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden skin grade, portrait 2:3 vertical"
    },
    "balinese_goddess": {
        "tag": "Balinese Goddess",
        "subject": "a divine Balinese goddess female model",
        "body": "glamour model, elegant curves, powerful divine feminine presence",
        "outfit": "sacred Balinese temple dancer costume, golden crown headdress, jeweled breast plate, wrapped silk kain, bare midriff",
        "material": "gold embossed silk, ornate gilded accessories, sacred temple dancer textiles",
        "environment": "Balinese Hindu temple, stone carvings, tropical flowers, incense smoke, golden sunset",
        "lighting": "warm Bali golden hour, sacred temple glow, lush tropical atmosphere",
        "style": "Balinese divine goddess editorial, spiritual luxury fashion photography",
        "quality": "shot on Phase One XF IQ4, warm tropical golden grade, portrait 2:3 vertical"
    },
    "chinese_qipao_slit": {
        "tag": "Chinese Qipao Slit",
        "subject": "a seductive Chinese qipao female model",
        "body": "slim elegant model, long graceful legs, slender silhouette, refined sensual presence",
        "outfit": "ultra high-slit qipao cheongsam, thigh-high leg reveal, form-fitting silk silhouette, mandarin collar",
        "material": "liquid satin silk qipao, embroidered dragon phoenix pattern, mirror-finish fabric",
        "environment": "Shanghai art deco interior, red lanterns, vintage Chinese elegance",
        "lighting": "dramatic film noir lighting, red lantern warm glow, cinematic shadows",
        "style": "noir Shanghai qipao editorial, vintage Chinese glamour photography",
        "quality": "shot on Leica SL2, cinematic warm grade, portrait 2:3 vertical"
    },
    "scottish_corset": {
        "tag": "Scottish Corset",
        "subject": "a fierce Scottish glamour female model",
        "body": "athletic fitness model, toned defined body, powerful commanding presence",
        "outfit": "tartan corset boned bodice, ultra-high slit tartan skirt, dramatic plaid draping, bare midriff",
        "material": "authentic tartan wool reimagined in satin finish, boned corset structure, leather accents",
        "environment": "Scottish highland dramatic landscape, misty mountains, ancient castle ruins",
        "lighting": "dramatic moody Scottish sky, cold natural light, misty atmospheric glow",
        "style": "Scottish highland glamour editorial, fierce Celtic fashion photography",
        "quality": "shot on Hasselblad H6D, cool moody film grade, portrait 2:3 vertical"
    },
    "first_snow": {
        "tag": "First Snow",
        "subject": "a breathtaking first snow female model",
        "body": "slim elegance model, graceful delicate figure, ethereal yet sensual presence",
        "outfit": "sheer white silk slip dress, snowflakes landing on bare skin, translucent flowing layers",
        "material": "sheer white silk chiffon, semi-transparent organza layers, delicate lace trim",
        "environment": "silent snowfall outdoor, bare winter trees, white snow ground, blue-white atmosphere",
        "lighting": "cold blue-white winter light, soft diffused snowfall glow, ethereal pale luminosity",
        "style": "first snow sensual editorial, winter glamour fashion photography",
        "quality": "shot on Hasselblad H6D, cool blue-white grade, portrait 2:3 vertical"
    },
    "golden_autumn": {
        "tag": "Golden Autumn",
        "subject": "a radiant golden autumn female model",
        "body": "VS Angel body, toned flat abs, long legs, curvaceous yet athletic silhouette",
        "outfit": "burnt orange satin slip dress, deep neckline, thigh slit, fallen leaves swirling around",
        "material": "liquid satin in amber and burnt orange, ultra-glossy warm finish",
        "environment": "peak autumn forest, blazing red and gold foliage, fallen leaves, golden afternoon",
        "lighting": "golden autumn hour, warm amber light filtering through leaves, glowing skin luminosity",
        "style": "golden autumn glamour editorial, warm luxury fashion photography",
        "quality": "shot on Canon EOS R5, warm amber golden grade, portrait 2:3 vertical"
    },
    "midsummer_heat": {
        "tag": "Midsummer Heat",
        "subject": "a scorching midsummer female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, glistening bronzed skin",
        "outfit": "barely-there micro bikini, sun-heated body, heat shimmer rising, minimal coverage",
        "material": "minimal metallic micro bikini, sun-kissed bronzed oiled skin as texture",
        "environment": "scorching midsummer desert or rooftop, heat haze shimmer, blazing sun overhead",
        "lighting": "harsh midday sun, extreme skin glow, heat shimmer distortion, intense shadows",
        "style": "midsummer heat editorial, Sports Illustrated swimsuit scorching glamour",
        "quality": "shot on Sony A7R V, teal and orange cinematic grade, portrait 2:3 vertical"
    },
    "rainy_season": {
        "tag": "Rainy Season",
        "subject": "a seductive rainy season female model",
        "body": "slim toned model, lean athletic build, glistening wet skin",
        "outfit": "soaking wet sheer white dress clinging to body, rain-drenched transparent fabric",
        "material": "wet-look transparent cotton voile, rain-soaked clinging fabric, second-skin wet effect",
        "environment": "monsoon rain street, wet pavement reflections, heavy rainfall, warm city lights",
        "lighting": "neon city light reflections on wet ground, rain-blurred bokeh, moody warm atmosphere",
        "style": "rain-soaked sensual editorial, wet glamour fashion photography",
        "quality": "shot on Canon EOS R5, moody warm rain grade, portrait 2:3 vertical"
    },
    "harvest_moon": {
        "tag": "Harvest Moon",
        "subject": "a mystical harvest moon female model",
        "body": "soft glamour model, feminine gentle curves, mysterious sensual presence",
        "outfit": "flowing amber silk gown, deep plunging neckline, thigh slit, moonlight catching fabric",
        "material": "liquid amber satin, gossamer sheer overlay, moonlight-reflective silk",
        "environment": "open field under enormous full harvest moon, golden wheat, cool night air",
        "lighting": "enormous harvest moon backlight, warm amber moonrise glow, dramatic silhouette",
        "style": "harvest moon mystical editorial, sensual autumn night photography",
        "quality": "shot on Hasselblad H6D, warm amber moonlight grade, portrait 2:3 vertical"
    },
    "winter_solstice": {
        "tag": "Winter Solstice",
        "subject": "a powerful winter solstice goddess female model",
        "body": "sculpted power model, defined muscles, commanding powerful presence",
        "outfit": "dramatic ice crystal armor, crystalline structured bodysuit, bare arms, frost crown",
        "material": "ice crystal formations, frozen glass-like structural pieces, silver metallic accents",
        "environment": "ice cave interior, crystal blue ice formations, winter solstice darkness",
        "lighting": "ethereal blue-white ice cave glow, cold crystalline reflections, dramatic shadows",
        "style": "winter solstice goddess editorial, dark ice glamour fashion photography",
        "quality": "shot on Phase One XF IQ4, cool crystal blue grade, portrait 2:3 vertical"
    },
    "cherry_blossom_night": {
        "tag": "Cherry Blossom Night",
        "subject": "a mesmerizing cherry blossom night female model",
        "body": "slim elegance model, graceful elongated figure, ethereal sensual presence",
        "outfit": "dark silk kimono-inspired gown, deep contrast against pale pink petals, plunging neckline",
        "material": "deep indigo liquid satin, contrast against soft pink blossom petals",
        "environment": "cherry blossom night, dark sky, illuminated pink blossoms, petals falling",
        "lighting": "dramatic uplight on blossoms, dark moody night, pink petal bokeh glow",
        "style": "cherry blossom night noir editorial, dark Japanese spring glamour photography",
        "quality": "shot on Leica SL2, dark moody pink contrast grade, portrait 2:3 vertical"
    },
    "tropical_monsoon": {
        "tag": "Tropical Monsoon",
        "subject": "a fierce tropical monsoon female model",
        "body": "sports glamour model, toned athletic body with curves, bronzed glistening wet skin",
        "outfit": "barely-there tropical print bikini, monsoon rain drenching body, water cascading",
        "material": "minimal tropical print swimwear, rain-soaked glistening bronzed skin",
        "environment": "tropical jungle in heavy monsoon, lush green foliage, dramatic rainfall, warm air",
        "lighting": "dramatic tropical storm light, warm rain glow, intense contrast, jungle atmosphere",
        "style": "tropical monsoon power editorial, Sports Illustrated wet glamour photography",
        "quality": "shot on Canon EOS R5, vibrant warm tropical grade, portrait 2:3 vertical"
    },
    "y2k_fairy": {
        "tag": "Y2K Fairy",
        "subject": "a playful Y2K fairy female model",
        "body": "slim toned model, lean athletic build, youthful vibrant presence",
        "outfit": "Y2K butterfly top, low-rise micro mini skirt, iridescent fairy wings, butterfly clips, platform boots",
        "material": "iridescent holographic fabric, glittery butterfly print, sheer pastel layers",
        "environment": "Y2K aesthetic digital dreamscape, holographic backdrop, pastel clouds",
        "lighting": "rainbow prism light, holographic shimmer, soft pastel glow",
        "style": "Y2K fairy glamour editorial, early 2000s pop star fashion photography",
        "quality": "shot on Canon EOS R5, holographic pastel grade, portrait 2:3 vertical"
    },
    "pink_champagne": {
        "tag": "Pink Champagne",
        "subject": "a bubbly pink champagne female model",
        "body": "VS Angel body, toned flat abs, long legs, curvaceous yet glamorous silhouette",
        "outfit": "blush pink sequin mini dress, plunging neckline, champagne bubbles surrounding, playful glamour",
        "material": "blush pink iridescent sequins, rose gold metallic accents, champagne bubble effects",
        "environment": "luxury champagne celebration, pink champagne tower, rose gold balloons, glitter",
        "lighting": "warm rose gold glow, champagne bubble bokeh, soft celebratory sparkle",
        "style": "pink champagne glamour editorial, luxury celebration fashion photography",
        "quality": "shot on Canon EOS R5, pink glamour rose gold grade, portrait 2:3 vertical"
    },
    "cotton_candy": {
        "tag": "Cotton Candy",
        "subject": "a sweet cotton candy female model",
        "body": "slim elegance model, delicate frame, sweet playful yet sensual presence",
        "outfit": "pastel cotton candy colored mini dress, fluffy tulle layers, bare shoulders, candy accessories",
        "material": "soft pastel tulle, cotton candy pink and blue ombre fabric, sheer overlay",
        "environment": "dreamlike candy fair, cotton candy clouds, pastel sunset, carnival lights",
        "lighting": "soft pastel carnival glow, warm pink and blue bokeh, dreamy diffused light",
        "style": "cotton candy dream editorial, sweet glamour fashion photography",
        "quality": "shot on Canon EOS R5, pastel pink blue grade, portrait 2:3 vertical"
    },
    "angel_baby": {
        "tag": "Angel Baby",
        "subject": "a heavenly angel baby female model",
        "body": "soft glamour model, feminine gentle curves, innocent yet sensual presence",
        "outfit": "white lace corset mini dress, feather angel wings, golden halo crown, thigh-high white stockings",
        "material": "delicate white lace, soft feather wings, golden metallic halo, sheer white silk",
        "environment": "heavenly white cloud dreamscape, golden light rays, soft mist",
        "lighting": "divine golden backlight, soft heavenly glow, warm angelic luminosity",
        "style": "angel baby glamour editorial, Victoria's Secret angel meets innocent beauty",
        "quality": "shot on Hasselblad H6D, soft warm white golden grade, portrait 2:3 vertical"
    },
    "idol_stage": {
        "tag": "Idol Stage",
        "subject": "a dazzling K-pop idol stage female model",
        "body": "slim toned model, lean athletic build, powerful stage presence with playful edge",
        "outfit": "K-pop idol stage costume, sparkly crop top, micro mini skirt, thigh-high boots, stage glam",
        "material": "crystal-encrusted performance fabric, holographic stage costume, iridescent sequins",
        "environment": "grand K-pop concert stage, dramatic stage lighting, confetti, fan lightsticks",
        "lighting": "dramatic concert stage lighting, colorful spot beams, glitter confetti glow",
        "style": "K-pop idol stage editorial, performance glamour fashion photography",
        "quality": "shot on Canon EOS R5, vibrant concert light grade, portrait 2:3 vertical"
    },
    "kitty_glam": {
        "tag": "Kitty Glam",
        "subject": "a seductive kitty glam female model",
        "body": "slim elegance model, graceful feline figure, playful yet deeply sensual presence",
        "outfit": "sleek black cat ears, form-fitting catsuit, long tail accessory, paw gloves, choker",
        "material": "glossy patent leather catsuit, velvet cat ears, metallic choker",
        "environment": "dark luxurious boudoir, velvet furnishings, dim moody lighting",
        "lighting": "dramatic low-key boudoir light, feline shadow play, moody intimate glow",
        "style": "kitty glamour editorial, sexy feline fashion photography",
        "quality": "shot on Leica SL2, dark moody contrast grade, portrait 2:3 vertical"
    },
    "strawberry_milk": {
        "tag": "Strawberry Milk",
        "subject": "a sweet strawberry milk female model",
        "body": "soft glamour model, feminine gentle curves, fresh youthful yet sensual presence",
        "outfit": "strawberry pink satin slip dress, fresh strawberry accessories, milky skin glow",
        "material": "soft satin strawberry pink fabric, sheer lace trim, milky smooth skin finish",
        "environment": "dreamy strawberry field, pastel pink sky, strawberry blossoms, warm afternoon",
        "lighting": "warm pink golden hour, soft strawberry bloom bokeh, creamy skin luminosity",
        "style": "strawberry milk sweet editorial, Korean beauty glamour fashion photography",
        "quality": "shot on Canon EOS R5, warm strawberry pink grade, portrait 2:3 vertical"
    },
    "cherry_pop": {
        "tag": "Cherry Pop",
        "subject": "a vivacious cherry pop female model",
        "body": "VS Angel body, toned flat abs, long legs, playful confident presence",
        "outfit": "cherry red micro dress, bold red lips, cherry accessories, flirty mini length",
        "material": "glossy cherry red satin, patent leather accents, bold red statement pieces",
        "environment": "retro diner or cherry orchard, vibrant red and white aesthetic",
        "lighting": "bright playful pop lighting, cherry red accent light, vibrant high-key glow",
        "style": "cherry pop glamour editorial, bold retro-meets-modern fashion photography",
        "quality": "shot on Canon EOS R5, vivid cherry red pop grade, portrait 2:3 vertical"
    },
    "neon_kawaii": {
        "tag": "Neon Kawaii",
        "subject": "a electric neon kawaii female model",
        "body": "slim toned model, lean playful figure, energetic neon presence",
        "outfit": "neon pastel rave outfit, holographic mini skirt, neon crop top, platform sneakers, candy accessories",
        "material": "neon holographic fabric, iridescent pastel vinyl, UV-reactive neon accents",
        "environment": "neon kawaii paradise, pastel neon signs, arcade lights, Tokyo Harajuku night",
        "lighting": "vivid neon multicolor light, UV glow, holographic shimmer, electric atmosphere",
        "style": "neon kawaii editorial, electric Harajuku glamour fashion photography",
        "quality": "shot on Sony A7R V, neon vivid holographic grade, portrait 2:3 vertical"
    },
    "fairy_kei": {
        "tag": "Fairy Kei",
        "subject": "a enchanting fairy kei female model",
        "body": "slim elegance model, delicate graceful figure, whimsical sensual presence",
        "outfit": "layered pastel fairy kei outfit, tulle skirts, lace sleeves, star accessories, platform mary janes",
        "material": "layered soft pastel tulle, delicate lace, velvet ribbon accents, sheer fairy fabric",
        "environment": "enchanted fairy garden, oversized flowers, butterfly wings, soft pastel dreamscape",
        "lighting": "magical soft pastel light, fairy dust sparkle, dreamy diffused glow",
        "style": "fairy kei glamour editorial, Japanese street fashion luxury photography",
        "quality": "shot on Canon EOS R5, soft pastel dream grade, portrait 2:3 vertical"
    },
}

added = 0
skipped = 0
for name, data in new_presets.items():
    path = PRESETS_DIR / f"{name}.json"
    if path.exists():
        print(f"⏭️  skip (exists): {name}")
        skipped += 1
    else:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ added: {name}")
        added += 1

print(f"\n완료: {added}개 추가, {skipped}개 스킵")
print(f"총 추가 예정: 28개")
print("""
카테고리 재분류 안내 (별도 작업 불필요 — engine.py에서 카테고리 매핑 시 반영):
🍬 팝 & 카와이로 이동:
  bubble_tea, doll_house, harajuku_doll, pastel_fairy, candy_rave, pop_art_glamour
""")