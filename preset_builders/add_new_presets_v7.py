"""
LumineX - 관능적 컨셉 프리셋 추가 스크립트 v4.0
실행: python add_new_presets_v7.py
관능적/글래머 컨셉 55개
"""

import json
import os

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")
os.makedirs(PRESETS_DIR, exist_ok=True)

NEW_PRESETS_V40 = {

    # ── 소재/질감 특화 ───────────────────────────────────────
    "oil_goddess": {
        "tag": "Oil Goddess",
        "subject": "a glistening oil goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "luxury minimal bikini, heavily oiled body, glistening skin editorial",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "luxury infinity pool edge, tropical resort, golden light",
        "lighting": "golden hour warm backlight, skin luminosity, oiled glow",
        "style": "Sports Illustrated oil goddess editorial, luxury body photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "chrome_skin": {
        "tag": "Chrome Skin",
        "subject": "a futuristic chrome skin female model",
        "body": "athletic fitness model, defined abs, toned body, metallic goddess",
        "outfit": "chrome metallic bodysuit, mirror-finish skin effect, futuristic glamour",
        "material": "reflective metallic vinyl, chrome-like mirror sheen",
        "environment": "pure white minimalist studio, seamless backdrop",
        "lighting": "professional studio strobe, chrome reflections, high contrast",
        "style": "chrome skin editorial, futuristic fashion photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },
    "crystal_goddess": {
        "tag": "Crystal Goddess",
        "subject": "a sparkling crystal goddess female model",
        "body": "VS 앤젤 — 완벽한 VS 글래머",
        "outfit": "crystal embellished minimal outfit, rhinestone coverage, crystal goddess glamour",
        "material": "crystal mesh, rhinestone-embellished sheer fabric",
        "environment": "luxury crystal cave, glittering formations, magical light",
        "lighting": "crystal light refraction, rainbow sparkle, magical atmosphere",
        "style": "crystal goddess editorial, luxury sparkle photography",
        "quality": "shot on Phase One XF IQ4, high key bright white tone, portrait 2:3 vertical"
    },
    "veil_goddess": {
        "tag": "Veil Goddess",
        "subject": "a mysterious veil goddess female model",
        "body": "glamour curvy model, dramatic waist-to-hip ratio, divine goddess proportions",
        "outfit": "sheer flowing veil only, minimal coverage, goddess veil draping",
        "material": "sheer silk organza, translucent veil fabric",
        "environment": "ancient temple ruins, golden columns, divine light",
        "lighting": "golden divine backlight, veil glow, ethereal atmosphere",
        "style": "veil goddess editorial, divine fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "silhouette_only": {
        "tag": "Silhouette Only",
        "subject": "a powerful silhouette female model",
        "body": "hot glamour model, dramatic hourglass silhouette, powerful figure",
        "outfit": "silhouette editorial, backlit figure only, dramatic outline",
        "material": "silhouette light effect",
        "environment": "dramatic sunset horizon, ocean backdrop, powerful sky",
        "lighting": "strong rim backlight, silhouette definition, halo effect",
        "style": "silhouette editorial, fine art fashion photography",
        "quality": "shot on Canon EOS R5, dark moody color grade, portrait 2:3 vertical"
    },
    "shadow_play": {
        "tag": "Shadow Play",
        "subject": "a mysterious shadow play female model",
        "body": "slim toned model, elegant figure, shadow art presence",
        "outfit": "minimal outfit, dramatic shadow patterns on skin, artistic shadow editorial",
        "material": "shadow light textile effect",
        "environment": "dark studio, geometric shadow patterns, venetian blind shadows",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "shadow play editorial, dark artistic photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },
    "mirror_goddess": {
        "tag": "Mirror Goddess",
        "subject": "a glamorous mirror goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, mirror goddess",
        "outfit": "mirror-inspired outfit, reflective minimal fashion, vanity glamour",
        "material": "patent leather, shiny mirror-like high-gloss surface",
        "environment": "ornate mirror room, infinite reflections, luxury vanity",
        "lighting": "soft beauty dish light, mirror reflections, glamour atmosphere",
        "style": "mirror goddess editorial, vanity luxury photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },
    "backlit_silk": {
        "tag": "Backlit Silk",
        "subject": "a ethereal backlit silk female model",
        "body": "slim toned model, graceful figure, backlit ethereal presence",
        "outfit": "sheer silk dress, backlit transparency, ethereal fabric glow",
        "material": "lightweight chiffon, sheer silk fabric, backlit transparency",
        "environment": "golden hour window, strong backlight, ethereal atmosphere",
        "lighting": "strong rim backlight, silhouette definition, halo effect",
        "style": "backlit silk editorial, ethereal fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },

    # ── 장소/배경 특화 ───────────────────────────────────────
    "rooftop_midnight": {
        "tag": "Rooftop Midnight",
        "subject": "a mysterious rooftop midnight female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, midnight goddess",
        "outfit": "midnight rooftop outfit, sleek black mini dress, city night glamour",
        "material": "liquid satin, ultra-glossy finish",
        "environment": "luxury rooftop, city skyline at midnight, twinkling lights",
        "lighting": "city neon glow, midnight atmospheric light, urban mystery",
        "style": "midnight rooftop editorial, urban glamour photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },
    "balcony_goddess": {
        "tag": "Balcony Goddess",
        "subject": "a sensual balcony goddess female model",
        "body": "glamour curvy model, dramatic waist-to-hip ratio, balcony goddess",
        "outfit": "sheer silk robe, flowing balcony goddess styling, morning glamour",
        "material": "sheer silk organza, flowing luxury fabric",
        "environment": "luxury penthouse balcony, Mediterranean view, golden morning",
        "lighting": "golden morning backlight, balcony glow, luxury atmosphere",
        "style": "balcony goddess editorial, luxury lifestyle photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "beach_bonfire": {
        "tag": "Beach Bonfire",
        "subject": "a wild beach bonfire female model",
        "body": "athletic fitness model, toned sun-kissed body, beach goddess",
        "outfit": "beach bonfire outfit, minimal bikini, fire dancer glamour",
        "material": "tropical print fabric, exotic beach textile",
        "environment": "midnight beach bonfire, flames reflecting on ocean, tropical night",
        "lighting": "firelight, warm flickering flames, dramatic orange glow",
        "style": "beach bonfire editorial, tropical night photography",
        "quality": "shot on Canon EOS R5, cinematic teal and orange color grade, portrait 2:3 vertical"
    },
    "midnight_bath": {
        "tag": "Midnight Bath",
        "subject": "a luxurious midnight bath female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, bath goddess",
        "outfit": "luxury bath editorial, rose petals, minimal coverage, spa glamour",
        "material": "water reflection, rose petal textile effect",
        "environment": "luxury marble bathroom, rose petals, candlelight, midnight spa",
        "lighting": "warm candlelight, bath luxury atmosphere, intimate glow",
        "style": "midnight bath editorial, luxury spa photography",
        "quality": "shot on Phase One XF IQ4, warm golden film grade, portrait 2:3 vertical"
    },
    "poolside_noir": {
        "tag": "Poolside Noir",
        "subject": "a mysterious poolside noir female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, pool goddess",
        "outfit": "poolside noir bikini, dark luxury swimwear, night pool glamour",
        "material": "wet-look spandex, dark pool textile",
        "environment": "midnight luxury pool, dark water reflection, city lights below",
        "lighting": "underwater pool light reflection, rippling aqua light patterns",
        "style": "poolside noir editorial, dark luxury photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },

    # ── 빛/조명 특화 ─────────────────────────────────────────
    "candlelight_noir": {
        "tag": "Candlelight Noir",
        "subject": "a mysterious candlelight noir female model",
        "body": "glamour curvy model, dramatic curves, candlelight goddess",
        "outfit": "minimal dark editorial, candlelight glamour, shadow-draped",
        "material": "dark velvet, rich luxurious texture",
        "environment": "dark baroque chamber, dozens of candles, opulent darkness",
        "lighting": "flickering candlelight shadows, deep chiaroscuro, intimate noir",
        "style": "candlelight noir editorial, dark baroque photography",
        "quality": "shot on Leica SL2, dark moody color grade, portrait 2:3 vertical"
    },
    "golden_oil": {
        "tag": "Golden Oil",
        "subject": "a radiant golden oil goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, golden goddess",
        "outfit": "golden minimal bikini, heavily oiled golden skin, sun goddess",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Sahara desert dunes, golden hour sunset, dramatic sky",
        "lighting": "golden hour warm backlight, oiled skin luminosity, desert glow",
        "style": "golden oil editorial, desert goddess photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "neon_body": {
        "tag": "Neon Body",
        "subject": "a electric neon body female model",
        "body": "athletic fitness model, defined abs, toned body, neon goddess",
        "outfit": "minimal dark outfit, neon light painting on body, electric editorial",
        "material": "dark matte fabric, neon light effect",
        "environment": "dark studio, neon light installations, electric atmosphere",
        "lighting": "multi-colored neon edge glow, cyberpunk light, body illumination",
        "style": "neon body art editorial, electric fashion photography",
        "quality": "shot on Sony A7R V, purple moody color grade, portrait 2:3 vertical"
    },

    # ── 컬러/무드 특화 ───────────────────────────────────────
    "all_black_goddess": {
        "tag": "All Black Goddess",
        "subject": "a fierce all-black goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, all black goddess",
        "outfit": "all-black minimal outfit, monochrome glamour, black on black editorial",
        "material": "patent leather, shiny mirror-like high-gloss surface",
        "environment": "pure black studio, seamless dark backdrop",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "all black goddess editorial, monochrome luxury photography",
        "quality": "shot on Hasselblad H6D, dark moody color grade, portrait 2:3 vertical"
    },
    "ivory_silk": {
        "tag": "Ivory Silk",
        "subject": "a ethereal ivory silk female model",
        "body": "slim toned model, graceful elegant figure, ivory goddess",
        "outfit": "ivory silk draping, minimal coverage, pure elegance editorial",
        "material": "liquid satin ivory, flowing silk fabric",
        "environment": "pure white studio, soft white backdrop, ethereal space",
        "lighting": "soft beauty dish light, high key white, pure glamour",
        "style": "ivory silk editorial, pure elegance photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },
    "red_temptress": {
        "tag": "Red Temptress",
        "subject": "a fierce red temptress female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, red goddess",
        "outfit": "dramatic red minimal outfit, red satin temptress, bold red editorial",
        "material": "liquid satin red, ultra-glossy red finish",
        "environment": "dark baroque chamber, red roses, dramatic darkness",
        "lighting": "dramatic chiaroscuro, red atmospheric glow, seductive shadows",
        "style": "red temptress editorial, dark luxury photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },
    "gold_temptress": {
        "tag": "Gold Temptress",
        "subject": "a powerful gold temptress female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, gold goddess",
        "outfit": "gold minimal editorial, gilded body glamour, golden temptress",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Versailles golden hall, ornate chandeliers, luxury interior",
        "lighting": "golden chandelier light, jewel reflections, opulent atmosphere",
        "style": "gold temptress editorial, opulent luxury photography",
        "quality": "shot on Phase One XF IQ4, warm golden film grade, portrait 2:3 vertical"
    },

    # ── 감각/터치 특화 ───────────────────────────────────────
    "feather_touch": {
        "tag": "Feather Touch",
        "subject": "a delicate feather touch female model",
        "body": "slim toned model, graceful elegant figure, feather goddess",
        "outfit": "feather-draped minimal coverage, luxury plumes, showgirl feather glamour",
        "material": "feather-trimmed fabric, showgirl glamour, luxury plumes",
        "environment": "luxury boudoir, soft romantic interior, feather atmosphere",
        "lighting": "soft beauty dish light, feather glow, romantic atmosphere",
        "style": "feather touch editorial, luxury boudoir photography",
        "quality": "shot on Hasselblad H6D, soft pink glamour grade, portrait 2:3 vertical"
    },
    "silk_wrap": {
        "tag": "Silk Wrap",
        "subject": "a sensual silk wrap female model",
        "body": "glamour curvy model, dramatic curves, silk goddess",
        "outfit": "single silk sheet wrap, minimal coverage, elegant silk draping",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "luxury bedroom, silk sheets, morning golden light",
        "lighting": "golden morning backlight, silk glow, intimate luxury",
        "style": "silk wrap editorial, intimate luxury photography",
        "quality": "shot on Leica SL2, warm golden film grade, portrait 2:3 vertical"
    },
    "ribbon_goddess": {
        "tag": "Ribbon Goddess",
        "subject": "a artistic ribbon goddess female model",
        "body": "slim toned model, graceful figure, ribbon art goddess",
        "outfit": "ribbon-wrapped artistic editorial, colorful ribbon coverage, art fashion",
        "material": "silk ribbon textile, artistic wrap material",
        "environment": "pure white studio, seamless backdrop, art space",
        "lighting": "soft beauty dish light, ribbon color play, artistic atmosphere",
        "style": "ribbon goddess editorial, art fashion photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },
    "chain_goddess": {
        "tag": "Chain Goddess",
        "subject": "a powerful chain goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, chain goddess",
        "outfit": "gold chain body jewelry, chain mail coverage, luxury chain editorial",
        "material": "gold chain mail mesh, metallic chainlink fabric",
        "environment": "dark luxury interior, gold accents, opulent darkness",
        "lighting": "dramatic chiaroscuro, gold chain reflections, luxury shadows",
        "style": "chain goddess editorial, dark luxury photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },
    "petal_goddess": {
        "tag": "Petal Goddess",
        "subject": "a ethereal petal goddess female model",
        "body": "slim toned model, graceful feminine figure, petal goddess",
        "outfit": "flower petal coverage, rose petal artistry, botanical goddess",
        "material": "fresh flower petals, botanical luxury textile",
        "environment": "lush botanical garden, thousands of rose petals, floral paradise",
        "lighting": "soft golden hour, petal bokeh, dreamy botanical atmosphere",
        "style": "petal goddess editorial, botanical luxury photography",
        "quality": "shot on Hasselblad H6D, soft pink glamour grade, portrait 2:3 vertical"
    },

    # ── 날씨/자연 특화 ───────────────────────────────────────
    "rain_soaked": {
        "tag": "Rain Soaked",
        "subject": "a dramatic rain soaked female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, wet goddess",
        "outfit": "minimal soaking wet outfit, rain-drenched glamour, wet editorial",
        "material": "wet-look spandex, soaking wet appearance",
        "environment": "dramatic rain, wet urban street, city lights reflection",
        "lighting": "rain-soaked neon reflections, wet pavement glow, dramatic rain",
        "style": "rain soaked editorial, wet glamour photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },
    "mist_goddess": {
        "tag": "Mist Goddess",
        "subject": "a mysterious mist goddess female model",
        "body": "slim toned model, ethereal elegant figure, mist goddess",
        "outfit": "sheer flowing dress, mist-draped ethereal styling",
        "material": "sheer organza, semi-transparent, ethereal fabric",
        "environment": "misty forest morning, dense fog, mysterious mist atmosphere",
        "lighting": "volumetric fog cinematic light, atmospheric mood, mist glow",
        "style": "mist goddess editorial, ethereal nature photography",
        "quality": "shot on Hasselblad H6D, cool blue color grade, portrait 2:3 vertical"
    },
    "waterfall_goddess": {
        "tag": "Waterfall Goddess",
        "subject": "a wild waterfall goddess female model",
        "body": "athletic fitness model, toned body, waterfall goddess",
        "outfit": "minimal waterfall outfit, soaking wet natural glamour",
        "material": "wet-look spandex, natural water textile",
        "environment": "tropical forest waterfall paradise, cascading water, lush jungle",
        "lighting": "natural waterfall light, water spray glow, jungle atmosphere",
        "style": "waterfall goddess editorial, natural glamour photography",
        "quality": "shot on Canon EOS R5, emerald green color grade, portrait 2:3 vertical"
    },
    "ocean_surge": {
        "tag": "Ocean Surge",
        "subject": "a powerful ocean surge female model",
        "body": "athletic fitness model, powerful toned body, ocean goddess",
        "outfit": "minimal ocean editorial, wave-soaked glamour, sea goddess",
        "material": "wet-look spandex, ocean water effect",
        "environment": "dramatic ocean wave, crashing surf, powerful sea",
        "lighting": "dramatic ocean backlight, wave spray halo, powerful atmosphere",
        "style": "ocean surge editorial, powerful nature photography",
        "quality": "shot on Nikon Z9, cinematic teal and orange color grade, portrait 2:3 vertical"
    },
    "snowflake_skin": {
        "tag": "Snowflake Skin",
        "subject": "a ethereal snowflake skin female model",
        "body": "slim toned model, pale ethereal figure, winter goddess",
        "outfit": "minimal white winter editorial, snowflake-dusted skin, ice goddess",
        "material": "ice crystal effects, frozen breath, winter frost",
        "environment": "snowy winter forest, falling snowflakes, magical winter",
        "lighting": "soft winter diffused light, snow reflection glow, magical atmosphere",
        "style": "snowflake skin editorial, winter goddess photography",
        "quality": "shot on Hasselblad H6D, cool blue color grade, portrait 2:3 vertical"
    },

    # ── 시간대 특화 ──────────────────────────────────────────
    "blue_hour_goddess": {
        "tag": "Blue Hour Goddess",
        "subject": "a mysterious blue hour goddess female model",
        "body": "glamour curvy model, dramatic curves, blue hour goddess",
        "outfit": "minimal blue hour editorial, twilight goddess styling",
        "material": "liquid satin, cool blue shimmer fabric",
        "environment": "city rooftop at blue hour, pre-dawn atmosphere, mysterious light",
        "lighting": "blue hour just before dawn, mystical pre-sunrise light, cool blue glow",
        "style": "blue hour goddess editorial, twilight fashion photography",
        "quality": "shot on Sony A7R V, cool blue color grade, portrait 2:3 vertical"
    },
    "golden_nude": {
        "tag": "Golden Nude",
        "subject": "a radiant golden nude editorial female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, golden goddess",
        "outfit": "golden hour backlit editorial, minimal coverage, skin-tone luxury",
        "material": "body oil, golden skin finish",
        "environment": "desert sand dunes, golden hour sunset, warm amber sky",
        "lighting": "intense golden hour backlight, skin luminosity, radiant glow",
        "style": "golden nude editorial, fine art fashion photography",
        "quality": "shot on Phase One XF IQ4, warm golden film grade, portrait 2:3 vertical"
    },
    "midnight_goddess": {
        "tag": "Midnight Goddess",
        "subject": "a powerful midnight goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, midnight goddess",
        "outfit": "midnight minimal editorial, moonlit goddess styling, dark luxury",
        "material": "liquid satin, dark shimmer fabric",
        "environment": "rooftop at midnight, full moon, city lights below",
        "lighting": "moonlight, silvery blue natural light, mysterious outdoor glow",
        "style": "midnight goddess editorial, lunar fashion photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },
    "dawn_awakening": {
        "tag": "Dawn Awakening",
        "subject": "a ethereal dawn awakening female model",
        "body": "slim toned model, graceful awakening figure, dawn goddess",
        "outfit": "dawn awakening editorial, sheer morning fabric, sunrise goddess",
        "material": "sheer silk organza, translucent morning fabric",
        "environment": "cliff edge at dawn, first light breaking, magical sunrise",
        "lighting": "golden hour just after sunrise, warm amber first light, dawn glow",
        "style": "dawn awakening editorial, sunrise fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },

    # ── 아트/회화 특화 ───────────────────────────────────────
    "renaissance_nude": {
        "tag": "Renaissance Nude",
        "subject": "a classical renaissance nude female model",
        "body": "soft curvy model, wide round hips, classical feminine beauty, renaissance figure",
        "outfit": "renaissance nude editorial, classical draping, fine art inspired",
        "material": "classical draped fabric, renaissance textile",
        "environment": "renaissance painter studio, classical artwork, warm candlelight",
        "lighting": "warm candlelight, renaissance painting atmosphere, classical glow",
        "style": "renaissance fine art editorial, classical painting photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "sculpture_goddess": {
        "tag": "Sculpture Goddess",
        "subject": "a statuesque sculpture goddess female model",
        "body": "athletic fitness model, perfectly defined muscles, sculpture goddess",
        "outfit": "sculpture-inspired minimal editorial, marble goddess styling",
        "material": "marble texture effect, classical sculpture material",
        "environment": "classical museum, white marble columns, sculpture gallery",
        "lighting": "clean museum spotlight, marble white light, classical atmosphere",
        "style": "sculpture goddess editorial, classical fine art photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },
    "ink_wash_body": {
        "tag": "Ink Wash Body",
        "subject": "a artistic ink wash body female model",
        "body": "slim toned model, graceful figure, ink art goddess",
        "outfit": "ink wash body art, flowing ink patterns on skin, Asian art inspired",
        "material": "ink body art effect, watercolor textile",
        "environment": "minimalist Japanese studio, rice paper backdrop, zen atmosphere",
        "lighting": "soft diffused light, ink wash atmosphere, artistic glow",
        "style": "ink wash body editorial, Asian fine art photography",
        "quality": "shot on Hasselblad H6D, black and white photography, portrait 2:3 vertical"
    },
    "tableau_vivant": {
        "tag": "Tableau Vivant",
        "subject": "a living painting tableau vivant female model",
        "body": "glamour curvy model, classical painting proportions, living art",
        "outfit": "living painting editorial, classical masterpiece inspired, art tableau",
        "material": "classical draped fabric, masterpiece textile",
        "environment": "baroque painting setting, dramatic classical composition",
        "lighting": "dramatic chiaroscuro, old master painting light, baroque atmosphere",
        "style": "tableau vivant editorial, living painting photography",
        "quality": "shot on Phase One XF IQ4, warm golden film grade, portrait 2:3 vertical"
    },
    "fresco_goddess": {
        "tag": "Fresco Goddess",
        "subject": "a ancient fresco goddess female model",
        "body": "slim toned model, classical Mediterranean figure, fresco goddess",
        "outfit": "ancient fresco-inspired styling, classical Mediterranean draping",
        "material": "ancient fresco texture fabric, Mediterranean textile",
        "environment": "ancient Roman villa, fresco walls, Mediterranean courtyard",
        "lighting": "warm Mediterranean light, ancient fresco atmosphere",
        "style": "fresco goddess editorial, ancient Mediterranean photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },

    # ── 거울/반사 특화 ───────────────────────────────────────
    "mirror_room": {
        "tag": "Mirror Room",
        "subject": "a infinite mirror room female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, mirror goddess",
        "outfit": "mirror room minimal editorial, infinite reflection glamour",
        "material": "patent leather, shiny mirror-like surface",
        "environment": "infinity mirror room, infinite reflections, art installation",
        "lighting": "mirror reflection light, infinite glow, surreal atmosphere",
        "style": "mirror room editorial, infinity reflection photography",
        "quality": "shot on Canon EOS R5, high key bright white tone, portrait 2:3 vertical"
    },
    "water_reflection": {
        "tag": "Water Reflection",
        "subject": "a dreamy water reflection female model",
        "body": "slim toned model, graceful figure, water reflection goddess",
        "outfit": "minimal editorial, water reflection glamour, reflection goddess",
        "material": "liquid satin, water reflection effect",
        "environment": "perfectly still lake, mirror water reflection, symmetrical paradise",
        "lighting": "golden hour reflection, water mirror light, dreamy atmosphere",
        "style": "water reflection editorial, fine art photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "glass_floor": {
        "tag": "Glass Floor",
        "subject": "a mysterious glass floor female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, glass goddess",
        "outfit": "glass floor editorial, minimal luxury outfit, transparent floor glamour",
        "material": "liquid satin, glass-like fabric",
        "environment": "glass floor luxury space, city below, transparent floor glamour",
        "lighting": "dramatic under-glow from glass floor, mysterious light",
        "style": "glass floor editorial, architectural luxury photography",
        "quality": "shot on Sony A7R V, cool blue color grade, portrait 2:3 vertical"
    },
    "prism_light": {
        "tag": "Prism Light",
        "subject": "a radiant prism light female model",
        "body": "slim toned model, graceful figure, prism goddess",
        "outfit": "minimal white editorial, prism rainbow light on skin, light art",
        "material": "white minimal fabric, prism light effect",
        "environment": "pure white studio, prism crystal light installation",
        "lighting": "prism glass effect, rainbow light dispersion, colorful light refraction",
        "style": "prism light editorial, light art photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },

    # ── 건축/공간 특화 ───────────────────────────────────────
    "marble_goddess": {
        "tag": "Marble Goddess",
        "subject": "a regal marble goddess female model",
        "body": "glamour curvy model, classical proportions, marble goddess",
        "outfit": "marble palace minimal editorial, classical luxury draping",
        "material": "liquid satin white, marble-like fabric",
        "environment": "grand marble palace, white columns, classical luxury",
        "lighting": "clean white marble light, classical luxury atmosphere",
        "style": "marble goddess editorial, classical luxury photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },
    "cathedral_light": {
        "tag": "Cathedral Light",
        "subject": "a divine cathedral light female model",
        "body": "slim toned model, ethereal divine figure, cathedral goddess",
        "outfit": "cathedral inspired minimal editorial, divine light goddess",
        "material": "sheer silk organza, divine light fabric",
        "environment": "grand cathedral interior, stained glass light, divine atmosphere",
        "lighting": "stained glass light rays, divine cathedral atmosphere, colored light",
        "style": "cathedral light editorial, divine fashion photography",
        "quality": "shot on Phase One XF IQ4, warm golden film grade, portrait 2:3 vertical"
    },
    "ruins_goddess": {
        "tag": "Ruins Goddess",
        "subject": "a mysterious ruins goddess female model",
        "body": "hot glamour model, dramatic curves, ancient ruins goddess",
        "outfit": "ruins goddess editorial, ancient draped minimal styling",
        "material": "ancient draped fabric, ruins textile",
        "environment": "ancient ruins, crumbling columns, overgrown with nature",
        "lighting": "dramatic golden hour through ruins, ancient atmosphere",
        "style": "ruins goddess editorial, ancient world photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },
    "greenhouse_eden": {
        "tag": "Greenhouse Eden",
        "subject": "a lush greenhouse eden female model",
        "body": "slim toned model, natural goddess figure, botanical eden",
        "outfit": "botanical minimal editorial, nature goddess, greenhouse eden",
        "material": "natural botanical fabric, eden textile",
        "environment": "lush greenhouse interior, tropical plants, botanical paradise",
        "lighting": "soft greenhouse diffused light, botanical glow, eden atmosphere",
        "style": "greenhouse eden editorial, botanical luxury photography",
        "quality": "shot on Hasselblad H6D, emerald green color grade, portrait 2:3 vertical"
    },
    "library_secret": {
        "tag": "Library Secret",
        "subject": "a mysterious library secret female model",
        "body": "slim toned model, intellectual sensual figure, library goddess",
        "outfit": "dark academia sensual editorial, library goddess styling, intellectual allure",
        "material": "dark velvet fabric, rich luxurious library textile",
        "environment": "ancient dark library, leather books, candlelight, secret knowledge",
        "lighting": "warm candlelight, library amber glow, intimate secret atmosphere",
        "style": "library secret editorial, dark academia luxury photography",
        "quality": "shot on Leica SL2, dark moody color grade, portrait 2:3 vertical"
    },

    # ── 퍼포먼스/댄스 특화 ──────────────────────────────────
    "tango_passion": {
        "tag": "Tango Passion",
        "subject": "a passionate tango female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, tango goddess",
        "outfit": "dramatic tango dress, high-slit red dress, passionate dance glamour",
        "material": "liquid satin, flowing tango fabric",
        "environment": "Buenos Aires milonga, dramatic tango atmosphere, dim lights",
        "lighting": "dramatic stage spotlight, tango atmosphere, passionate shadows",
        "style": "tango passion editorial, dance glamour photography",
        "quality": "shot on Canon EOS R5, dark moody color grade, portrait 2:3 vertical"
    },
    "cabaret_star": {
        "tag": "Cabaret Star",
        "subject": "a dazzling cabaret star female model",
        "body": "glamour curvy model, dramatic hourglass, cabaret goddess",
        "outfit": "cabaret costume, corset, fishnet stockings, feather headpiece, showgirl",
        "material": "satin corset fabric, luxury cabaret textile, feathers",
        "environment": "vintage Parisian cabaret, red curtains, spotlight stage",
        "lighting": "dramatic cabaret spotlight, vintage theater atmosphere",
        "style": "cabaret star editorial, Moulin Rouge glamour photography",
        "quality": "shot on Leica SL2, warm golden film grade, portrait 2:3 vertical"
    },
    "ribbon_dance": {
        "tag": "Ribbon Dance",
        "subject": "a graceful ribbon dance female model",
        "body": "slim toned model, graceful athletic figure, ribbon goddess",
        "outfit": "ribbon dance minimal costume, flowing colorful ribbons, artistic dance",
        "material": "silk ribbon textile, flowing dance material",
        "environment": "dramatic dark stage, colorful ribbon trails, dance performance",
        "lighting": "dramatic stage spotlight, ribbon color trails, performance atmosphere",
        "style": "ribbon dance editorial, artistic performance photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },
    "fire_dancer": {
        "tag": "Fire Dancer",
        "subject": "a fierce fire dancer female model",
        "body": "athletic fitness model, powerful toned body, fire goddess",
        "outfit": "fire dancer costume, minimal fire performance wear, flame goddess",
        "material": "dark performance fabric, fire-resistant glamour textile",
        "environment": "dark outdoor stage, fire torches, dramatic fire performance",
        "lighting": "firelight, warm flickering flames, dramatic orange glow",
        "style": "fire dancer editorial, fire performance photography",
        "quality": "shot on Canon EOS R5, cinematic teal and orange color grade, portrait 2:3 vertical"
    },
    "aerial_silk": {
        "tag": "Aerial Silk",
        "subject": "a spectacular aerial silk female model",
        "body": "athletic fitness model, defined muscles, flexible acrobatic figure",
        "outfit": "aerial silk performance costume, minimal acrobatic wear, silk wrapped",
        "material": "silk aerial fabric, performance stretch textile",
        "environment": "dramatic aerial performance space, high ceiling, dramatic height",
        "lighting": "dramatic aerial spotlight, silk fabric glow, performance atmosphere",
        "style": "aerial silk editorial, Cirque du Soleil photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },

    # ── 신체 특화 ────────────────────────────────────────────
    "back_beauty": {
        "tag": "Back Beauty",
        "subject": "a elegant back beauty female model",
        "body": "hot glamour model, elegant back, dramatic shoulder line, back goddess",
        "outfit": "open back editorial, backless luxury dress, spine emphasis",
        "material": "liquid satin backless fabric, open back textile",
        "environment": "luxury interior, dramatic architecture, elegant space",
        "lighting": "strong rim backlight, back definition, elegant atmosphere",
        "style": "back beauty editorial, elegant fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },
    "collarbone_focus": {
        "tag": "Collarbone Focus",
        "subject": "a refined collarbone focus female model",
        "body": "slim toned model, elegant collarbone, refined neck and shoulder",
        "outfit": "off-shoulder minimal editorial, collarbone emphasis, elegant neckline",
        "material": "luxury off-shoulder fabric, elegant textile",
        "environment": "pure white minimalist studio, seamless backdrop",
        "lighting": "soft beauty dish light, collarbone shadow definition",
        "style": "collarbone focus editorial, luxury beauty photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },
    "neck_elegance": {
        "tag": "Neck Elegance",
        "subject": "a graceful neck elegance female model",
        "body": "slim toned model, swan neck elegance, refined upper body presence",
        "outfit": "neck emphasis editorial, deep V or bare neck styling, elegant neckline",
        "material": "luxury structured fabric, neck elegance textile",
        "environment": "luxury studio, dramatic minimal backdrop",
        "lighting": "dramatic chiaroscuro, neck shadow definition, elegant contrast",
        "style": "neck elegance editorial, luxury beauty photography",
        "quality": "shot on Leica SL2, dark moody color grade, portrait 2:3 vertical"
    },
    "long_legs_focus": {
        "tag": "Long Legs Focus",
        "subject": "a statuesque long legs female model",
        "body": "슈퍼 슬림 — 마른 런웨이",
        "outfit": "leg-emphasis editorial, extreme mini dress, leg-elongating styling",
        "material": "liquid satin micro fabric, leg-emphasis textile",
        "environment": "luxury staircase, architectural glamour, elegant space",
        "lighting": "low angle upward shot, leg definition light, powerful perspective",
        "style": "long legs editorial, fashion editorial photography",
        "quality": "shot on Sony A7R V, cinematic teal and orange color grade, portrait 2:3 vertical"
    },
}


def main():
    print("\n  ✦ LumineX v4.0 관능적 컨셉 프리셋 추가 시작...\n")
    created = 0
    skipped = 0

    for name, data in NEW_PRESETS_V40.items():
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
    print("  - 소재/질감 특화  (oil/chrome/crystal/veil/silhouette/shadow/mirror/backlit) × 8")
    print("  - 장소/배경 특화  (rooftop/balcony/bonfire/bath/poolside)                   × 5")
    print("  - 빛/조명 특화    (candlelight/golden_oil/neon_body)                        × 3")
    print("  - 컬러/무드 특화  (all_black/ivory/red/gold)                                × 4")
    print("  - 감각/터치 특화  (feather/silk/ribbon/chain/petal)                         × 5")
    print("  - 날씨/자연 특화  (rain/mist/waterfall/ocean/snowflake)                     × 5")
    print("  - 시간대 특화     (blue_hour/golden_nude/midnight/dawn)                     × 4")
    print("  - 아트/회화 특화  (renaissance/sculpture/ink/tableau/fresco)                × 5")
    print("  - 거울/반사 특화  (mirror_room/water/glass_floor/prism)                     × 4")
    print("  - 건축/공간 특화  (marble/cathedral/ruins/greenhouse/library)               × 5")
    print("  - 퍼포먼스/댄스   (tango/cabaret/ribbon/fire/aerial)                        × 5")
    print("  - 신체 특화       (back/collarbone/neck/long_legs)                          × 4")
    print(f"  총 57개 신규 프리셋\n")


if __name__ == "__main__":
    main()