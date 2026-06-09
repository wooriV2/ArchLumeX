"""
LumineX - 프리셋 일괄 생성 스크립트
실행: python generate_presets.py
"""

import json
import os

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")
os.makedirs(PRESETS_DIR, exist_ok=True)

PRESETS = {
    "desert_mirage": {
        "tag": "Desert Mirage",
        "subject": "a stunning glamorous female model",
        "body": "tall athletic glamorous figure, long toned legs, hourglass silhouette, full body shot",
        "outfit": "shimmering sand-silk barely-there ensemble, midriff-baring, flowing yet revealing",
        "material": "shimmering sand-silk, iridescent fabric",
        "environment": "Sahara desert dunes, golden hour",
        "lighting": "overhead zenith sun, golden warm glow, skin luminosity",
        "style": "Vogue Arabia editorial, luxury desert fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "urban_vanguard": {
        "tag": "Urban Vanguard",
        "subject": "a fierce glamorous female model",
        "body": "tall athletic glamorous figure, long toned legs, confident stance, full body shot",
        "outfit": "glossy distressed leather micro skirt, crop corset top, bold cutouts, street-luxe",
        "material": "glossy distressed leather, high-sheen vinyl",
        "environment": "industrial rooftop, urban cityscape at dusk",
        "lighting": "low-angle warm street lamp, dramatic rim light",
        "style": "Harper's Bazaar street editorial, luxury urban fashion",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "velvet_darkness": {
        "tag": "Velvet Darkness",
        "subject": "a sultry glamorous female model",
        "body": "voluptuous curvy figure, hourglass silhouette, décolletage emphasis, full body shot",
        "outfit": "ultra-black velvet-latex bodycon mini dress, deep plunging neckline, thigh-high slit",
        "material": "ultra-black velvet-latex, second-skin finish",
        "environment": "dark baroque chamber, opulent candlelit interior",
        "lighting": "flickering candlelight shadows, deep chiaroscuro",
        "style": "Versace dark editorial, luxury gothic fashion photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "solar_flare": {
        "tag": "Solar Flare",
        "subject": "a radiant glamorous female model",
        "body": "tall athletic glamorous figure, toned midriff, long legs, full body shot",
        "outfit": "metallic gold foil bandeau top, ultra-micro skirt, navel-baring, high-gloss",
        "material": "metallic gold foil, mirror-finish fabric",
        "environment": "modernist glass villa, poolside",
        "lighting": "intense golden hour backlight, skin luminosity, lens flare",
        "style": "Sports Illustrated gold edition, luxury resort photography",
        "quality": "shot on Nikon Z9, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "arctic_minimal": {
        "tag": "Arctic Minimal",
        "subject": "a fierce editorial female model",
        "body": "tall slender modelesque figure, statuesque proportions, full body shot",
        "outfit": "frosted translucent polymer bodysuit, barely-there coverage, ice-queen aesthetic",
        "material": "frosted translucent polymer, crystal-clear material",
        "environment": "ice cave interior, frozen crystal walls",
        "lighting": "cool blue ambient light, ethereal glow",
        "style": "W Magazine avant-garde editorial, ice fashion photography",
        "quality": "shot on Phase One XF IQ4, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "onyx_tension": {
        "tag": "Onyx Tension",
        "subject": "a powerful fitness model",
        "body": "extremely toned athletic physique, defined abs, muscular legs, full body shot",
        "outfit": "onyx latex sports bra, high-cut micro shorts, body-hugging, muscle-baring",
        "material": "onyx latex, vacuum-seal finish",
        "environment": "brutalist gym, industrial fitness studio",
        "lighting": "top-down industrial strobe, muscle definition emphasis",
        "style": "fitness magazine power editorial, Sports Illustrated body issue",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "pearl_essence": {
        "tag": "Pearl Essence",
        "subject": "a luminous glamorous female model",
        "body": "soft glamour figure, feminine curves, elegant décolletage, full body shot",
        "outfit": "iridescent mother-of-pearl slip dress, plunging neckline, thigh-high slit",
        "material": "iridescent mother-of-pearl, pearlescent fabric",
        "environment": "white marble hall, luxury palazzo",
        "lighting": "diffused skylight, soft pearlescent glow",
        "style": "Vogue Italia luxury editorial, high-fashion glamour photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "toxic_bloom": {
        "tag": "Toxic Bloom",
        "subject": "a fierce exotic female model",
        "body": "tall athletic glamorous figure, long legs, powerful stance, full body shot",
        "outfit": "acid-green glossy vinyl micro dress, cutouts, barely-there coverage",
        "material": "acid-green glossy vinyl, high-sheen polymer",
        "environment": "cyber-botanic garden, futuristic greenhouse",
        "lighting": "bioluminescent plant glow, neon green accent light",
        "style": "Dazed and Confused avant-garde editorial, cyberpunk fashion",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "midnight_monolith": {
        "tag": "Midnight Monolith",
        "subject": "a powerful statuesque female model",
        "body": "tall statuesque figure, commanding presence, long legs, full body shot",
        "outfit": "dark basalt-texture bodycon gown, plunging neckline, thigh slit, dramatic",
        "material": "dark basalt stone-texture, matte-finish fabric",
        "environment": "night mountain peak, dramatic sky",
        "lighting": "full moon moonlight, ethereal blue glow",
        "style": "Vogue editorial dark glamour, cinematic fashion photography",
        "quality": "shot on Nikon Z9, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "glass_house": {
        "tag": "Glass House",
        "subject": "a delicate yet powerful female model",
        "body": "slender modelesque figure, elegant posture, long legs, full body shot",
        "outfit": "clear liquid-glass polymer micro dress, sheer and transparent, barely-there",
        "material": "clear liquid-glass polymer, transparent fabric",
        "environment": "rainy glass conservatory, botanical garden",
        "lighting": "overcast soft shadows, diffused natural light",
        "style": "Helmut Newton inspired editorial, artistic fashion photography",
        "quality": "shot on Phase One XF IQ4, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "lava_flow": {
        "tag": "Lava Flow",
        "subject": "a fierce volcanic female model",
        "body": "athletic glamorous figure, powerful stance, toned physique, full body shot",
        "outfit": "glowing thermochromic latex bodysuit, heat-reactive, skin-tight, dramatic",
        "material": "glowing thermochromic latex, heat-reactive material",
        "environment": "volcanic rock plateau, lava fields",
        "lighting": "red under-glow, dramatic volcanic light",
        "style": "avant-garde editorial, cinematic fashion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "ivory_tower": {
        "tag": "Ivory Tower",
        "subject": "a pure minimalist female model",
        "body": "tall slender figure, elegant statuesque proportions, full body shot",
        "outfit": "matte ivory ceramic-finish mini dress, structured bodice, thigh-baring",
        "material": "matte ivory ceramic, structured fabric",
        "environment": "cloud-level balcony, mountain resort",
        "lighting": "high-altitude crisp sun, pure white light",
        "style": "Celine editorial, minimalist luxury fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "emerald_city": {
        "tag": "Emerald City",
        "subject": "a glamorous jewel-toned female model",
        "body": "voluptuous curvy figure, hourglass silhouette, décolletage emphasis, full body shot",
        "outfit": "glossy emerald velvet corset mini dress, deep plunging neckline, high slit",
        "material": "glossy emerald velvet, jewel-tone fabric",
        "environment": "luxury casino vault, opulent interior",
        "lighting": "warm tungsten spot, jewel-toned reflections",
        "style": "Versace casino glamour editorial, luxury fashion photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "platinum_elite": {
        "tag": "Platinum Elite",
        "subject": "an ultra-luxury glamorous female model",
        "body": "tall athletic glamorous figure, sleek silhouette, long legs, full body shot",
        "outfit": "polished platinum bodycon dress, metallic mirror-finish, body-hugging",
        "material": "polished platinum plate, mirror-finish metal fabric",
        "environment": "private jet interior, luxury aviation",
        "lighting": "indirect cabin lighting, platinum reflections",
        "style": "NetJets luxury editorial, ultra-premium fashion photography",
        "quality": "shot on Phase One XF IQ4, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "champagne_mist": {
        "tag": "Champagne Mist",
        "subject": "an elegant glamorous female model",
        "body": "soft glamour figure, feminine curves, elegant décolletage, full body shot",
        "outfit": "translucent gloss organza slip dress, sheer overlay, navel-baring, ethereal",
        "material": "translucent gloss organza, sheer luxury fabric",
        "environment": "golden hour balcony, champagne toast setting",
        "lighting": "volumetric lens flare, warm champagne glow",
        "style": "Harper's Bazaar champagne editorial, luxury lifestyle photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "void_secret": {
        "tag": "Void Secret",
        "subject": "a mysterious powerful female model",
        "body": "statuesque figure, commanding silhouette, long legs, full body shot",
        "outfit": "matte-finish carbon bodysuit, architectural cutouts, barely-there panels",
        "material": "matte-finish carbon, structured void material",
        "environment": "brutalist concrete void, minimalist architecture",
        "lighting": "extreme chiaroscuro, deep shadows and highlights",
        "style": "Rick Owens editorial, dark minimalist fashion photography",
        "quality": "shot on Nikon Z9, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "elite_lingerie": {
        "tag": "Elite Lingerie",
        "subject": "a glamorous editorial female model",
        "body": "voluptuous curvy figure, hourglass silhouette, décolletage emphasis, full body shot",
        "outfit": "high-gloss silk-latex lingerie set, bra and brief, Victoria's Secret editorial style",
        "material": "high-gloss silk-latex, luxury lingerie fabric",
        "environment": "luxury penthouse suite, opulent bedroom",
        "lighting": "soft sunset rim light, golden warm glow",
        "style": "Victoria's Secret fashion show editorial, luxury lingerie photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
}

NEW_PRESETS = {
    # ── 신규 6개 ──────────────────────────────────────────
    "latex_venom": {
        "tag": "Latex Venom",
        "subject": "a dangerously alluring female model",
        "body": "hourglass figure, full bust, narrow waist, long legs, full body shot",
        "outfit": "toxic latex catsuit, poison green and black, ultra skin-tight, dangerous allure",
        "material": "high-gloss toxic latex, venom-green sheen",
        "environment": "dark industrial chamber, toxic atmosphere",
        "lighting": "sickly green accent light, dramatic shadows, danger glow",
        "style": "Thierry Mugler venom editorial, dark haute couture photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "power_suit": {
        "tag": "Power Suit",
        "subject": "a powerful commanding female model",
        "body": "tall statuesque figure, confident stance, long legs, full body shot",
        "outfit": "ultra-fitted power blazer, plunging neckline, micro skirt, no shirt underneath, corporate dominance",
        "material": "structured matte crepe, sharp tailoring",
        "environment": "glass corporate tower, city power view",
        "lighting": "cool office light, sharp shadows, power ambiance",
        "style": "Versace power editorial, luxury corporate fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "savage_leather": {
        "tag": "Savage Leather",
        "subject": "a fierce savage female model",
        "body": "athletic glamorous figure, powerful stance, toned physique, full body shot",
        "outfit": "destroyed leather micro dress, savage cutouts, chains, rock editorial",
        "material": "distressed black leather, raw edge finish",
        "environment": "abandoned warehouse, gritty urban decay",
        "lighting": "harsh industrial light, raw shadows",
        "style": "Saint Laurent rock editorial, savage fashion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "after_dark_minimal": {
        "tag": "After Dark Minimal",
        "subject": "a mysterious minimal female model",
        "body": "slender elegant figure, clean lines, full body shot",
        "outfit": "ultra-minimal black micro dress, barely-there straps, clean geometry",
        "material": "matte crepe, minimal construction",
        "environment": "empty dark room, single spotlight",
        "lighting": "single dramatic spotlight, deep darkness surrounding",
        "style": "Celine after-dark editorial, minimalist luxury photography",
        "quality": "shot on Phase One XF IQ4, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "zero_gravity": {
        "tag": "Zero Gravity",
        "subject": "a weightless ethereal female model",
        "body": "tall slender figure, floating pose, elongated limbs, full body shot",
        "outfit": "flowing zero-gravity gown, fabric floating in air, otherworldly",
        "material": "weightless chiffon, anti-gravity silk",
        "environment": "white void space, levitating elements",
        "lighting": "pure white ethereal light, no shadows, celestial",
        "style": "avant-garde zero gravity editorial, otherworldly fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "light_driven": {
        "tag": "Light Driven",
        "subject": "a luminous radiant female model",
        "body": "glamorous figure, skin luminosity emphasis, full body shot",
        "outfit": "light-reactive iridescent bodysuit, refracts light dramatically",
        "material": "prismatic light-reactive material, rainbow refractions",
        "environment": "pure light studio, prism environment",
        "lighting": "multiple colored light beams, rainbow prism light, dramatic",
        "style": "Vogue light art editorial, prismatic fashion photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── LUXURY / EDITORIAL ────────────────────────────────
    "golden_hour_editorial": {
        "tag": "Golden Hour Editorial",
        "subject": "a radiant glamorous female model",
        "body": "Victoria's Secret Angel body, long legs, full bust, hourglass, full body shot",
        "outfit": "liquid gold satin mini dress, deep plunging neckline, thigh slit",
        "material": "liquid gold satin, molten metallic fabric",
        "environment": "rooftop terrace, golden hour sunset, warm amber sky",
        "lighting": "intense golden hour backlight, skin luminosity, lens flare",
        "style": "Vogue golden hour editorial, luxury fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "monaco_nights": {
        "tag": "Monaco Nights",
        "subject": "a ultra-luxury glamorous female model",
        "body": "tall glamorous figure, full bust, hourglass silhouette, full body shot",
        "outfit": "backless crystal-embellished gown, plunging neckline, high slit",
        "material": "crystal-embellished silk, hand-sewn rhinestones",
        "environment": "Monaco casino terrace, Mediterranean night, superyachts",
        "lighting": "warm casino lights, sparkling crystal reflections",
        "style": "Monaco luxury editorial, ultra-premium fashion photography",
        "quality": "shot on Phase One XF IQ4, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "velvet_gold": {
        "tag": "Velvet Gold",
        "subject": "a opulent glamorous female model",
        "body": "voluptuous hourglass figure, full bust, full body shot",
        "outfit": "deep gold velvet corset mini dress, extreme cleavage, thigh slit",
        "material": "crushed gold velvet, rich opulent texture",
        "environment": "Versailles-inspired gold palace interior",
        "lighting": "warm golden chandelier light, opulent glow",
        "style": "Versace Versailles editorial, opulent luxury photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "noir_opulence": {
        "tag": "Noir Opulence",
        "subject": "a mysterious opulent female model",
        "body": "statuesque glamorous figure, long legs, full body shot",
        "outfit": "black velvet opera gown, extreme plunging, open back, dramatic",
        "material": "midnight black velvet, matte luxury finish",
        "environment": "dark opulent opera house, red velvet interior",
        "lighting": "dramatic stage lighting, deep chiaroscuro",
        "style": "Yves Saint Laurent noir editorial, luxury dark photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "couture_heat": {
        "tag": "Couture Heat",
        "subject": "a fierce haute couture female model",
        "body": "Victoria's Secret body, full bust, long legs, full body shot",
        "outfit": "fierce red haute couture mini dress, architectural cutouts, bold",
        "material": "structured red satin, architectural fabric",
        "environment": "Paris haute couture atelier, dramatic white space",
        "lighting": "high-key studio strobe, fashion week lighting",
        "style": "Paris haute couture editorial, Valentino fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "imperial_silk": {
        "tag": "Imperial Silk",
        "subject": "a regal imperial female model",
        "body": "tall elegant figure, graceful posture, long legs, full body shot",
        "outfit": "imperial silk slip dress, deep neckline, side slit, flowing",
        "material": "imperial pure silk, liquid drape",
        "environment": "imperial palace garden, cherry blossoms",
        "lighting": "soft diffused daylight, silk luminosity",
        "style": "Dior imperial editorial, regal luxury photography",
        "quality": "shot on Phase One XF IQ4, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── RESORT / SWIM / SUMMER ────────────────────────────
    "riviera_heat": {
        "tag": "Riviera Heat",
        "subject": "a stunning riviera female model",
        "body": "toned glamorous figure, long legs, full bust, full body shot",
        "outfit": "French Riviera micro bikini, barely-there coverage, gold accessories",
        "material": "luxury micro fabric, gold hardware",
        "environment": "French Riviera cliff, azure Mediterranean sea",
        "lighting": "harsh Mediterranean sun, skin glow, warm light",
        "style": "Sports Illustrated Riviera editorial, luxury resort photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "miami_afterglow": {
        "tag": "Miami Afterglow",
        "subject": "a glamorous Miami female model",
        "body": "voluptuous fitness figure, bronzed skin, full bust, full body shot",
        "outfit": "neon Miami string bikini, barely-there, bold color",
        "material": "neon stretch fabric, wet-look finish",
        "environment": "Miami Beach sunset, Ocean Drive neon lights",
        "lighting": "Miami sunset afterglow, neon reflections, warm pink",
        "style": "Sports Illustrated Miami editorial, beach glamour photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "infinity_pool": {
        "tag": "Infinity Pool",
        "subject": "a luxury resort female model",
        "body": "athletic glamorous figure, toned body, long legs, full body shot",
        "outfit": "designer luxury one-piece swimsuit, cutouts, high cut legs",
        "material": "metallic luxury swimwear fabric, iridescent",
        "environment": "infinity pool edge, Maldives overwater villa, ocean horizon",
        "lighting": "tropical golden hour, water caustics, skin luminosity",
        "style": "Vogue swimwear editorial, luxury Maldives photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "yacht_club": {
        "tag": "Yacht Club",
        "subject": "a ultra-luxury yacht female model",
        "body": "tall slender glamorous figure, bronzed skin, full body shot",
        "outfit": "yacht club micro dress, nautical luxury, barely-there white",
        "material": "crisp white luxury fabric, nautical details",
        "environment": "superyacht deck, Monaco harbor, Mediterranean blue",
        "lighting": "bright Mediterranean sun, ocean reflection, clean light",
        "style": "Slim Aarons yacht editorial, ultra-luxury photography",
        "quality": "shot on Phase One XF IQ4, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "azure_nights": {
        "tag": "Azure Nights",
        "subject": "a mysterious azure female model",
        "body": "glamorous figure, long legs, sultry presence, full body shot",
        "outfit": "azure blue sequin micro dress, plunging neckline, thigh slit",
        "material": "azure iridescent sequins, ocean-blue shimmer",
        "environment": "Santorini cliff at night, blue dome lights, Aegean sea",
        "lighting": "Santorini night lights, azure glow, moonlight",
        "style": "Vogue Greece editorial, luxury Mediterranean photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── DARK / CINEMATIC ──────────────────────────────────
    "black_mirror": {
        "tag": "Black Mirror",
        "subject": "a futuristic dark female model",
        "body": "sleek powerful figure, long legs, commanding presence, full body shot",
        "outfit": "mirror-black latex catsuit, reflective surface, futuristic",
        "material": "mirror-finish black latex, perfect reflection",
        "environment": "dark mirror room, infinite reflections",
        "lighting": "single cold light, mirror reflections, dramatic",
        "style": "Black Mirror tech editorial, dark futuristic photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "cyber_silk": {
        "tag": "Cyber Silk",
        "subject": "a cyberpunk silk female model",
        "body": "tall athletic figure, powerful stance, full body shot",
        "outfit": "cyber silk bodysuit, neon trim details, tech-fashion hybrid",
        "material": "liquid cyber silk, iridescent tech fabric",
        "environment": "neon cyberpunk city, rain-slicked streets",
        "lighting": "cyan and magenta neon, wet reflections, cinematic",
        "style": "cyberpunk Vogue editorial, tech fashion photography",
        "quality": "shot on Nikon Z9, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "phantom_gloss": {
        "tag": "Phantom Gloss",
        "subject": "a phantom-like female model",
        "body": "ethereal slender figure, mysterious presence, full body shot",
        "outfit": "phantom white gloss bodysuit, ghost-like, barely visible",
        "material": "high-gloss white latex, phantom finish",
        "environment": "white fog environment, ethereal mist",
        "lighting": "pure white backlight, gloss reflections, ethereal",
        "style": "avant-garde phantom editorial, ethereal fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "void_glamour": {
        "tag": "Void Glamour",
        "subject": "a void-like mysterious female model",
        "body": "powerful statuesque figure, commanding aura, full body shot",
        "outfit": "void black micro dress, anti-light fabric, absolute darkness",
        "material": "vantablack-inspired ultra-matte fabric",
        "environment": "absolute void space, nothingness",
        "lighting": "single rim light only, void darkness, dramatic silhouette",
        "style": "avant-garde void editorial, conceptual fashion photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── FITNESS / POWER GLAM ──────────────────────────────
    "sculpted_power": {
        "tag": "Sculpted Power",
        "subject": "a powerfully sculpted female model",
        "body": "extreme fitness physique, defined abs, round glutes, full bust, full body shot",
        "outfit": "sculpted minimal sports bra, high-cut micro shorts, body-defining",
        "material": "compression performance fabric, body-sculpting",
        "environment": "luxury black gym, sculpted equipment",
        "lighting": "dramatic overhead strobe, muscle definition emphasis",
        "style": "fitness power editorial, Sports Illustrated body issue",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "power_curve": {
        "tag": "Power Curve",
        "subject": "a powerful curvy fitness female model",
        "body": "powerful curvy figure, full bust, defined abs, round hips, full body shot",
        "outfit": "power curve latex bodysuit, extreme hourglass emphasis, skin-tight",
        "material": "power latex, curve-enhancing material",
        "environment": "luxury power gym, industrial aesthetic",
        "lighting": "dramatic side lighting, curve emphasis, powerful shadows",
        "style": "power curve editorial, glamour fitness photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "titanium_body": {
        "tag": "Titanium Body",
        "subject": "a titanium-hard fitness female model",
        "body": "extreme athletic physique, titanium-hard muscles, defined everywhere, full body shot",
        "outfit": "titanium metallic sports set, ultra-minimal, muscle-baring",
        "material": "titanium metallic fabric, hard-surface finish",
        "environment": "industrial titanium facility, cold metal environment",
        "lighting": "cold industrial light, metallic skin reflections",
        "style": "titanium power editorial, extreme fitness photography",
        "quality": "shot on Nikon Z9, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "elite_motion": {
        "tag": "Elite Motion",
        "subject": "a dynamic elite female model in motion",
        "body": "elite athletic figure, powerful motion, toned body, full body shot",
        "outfit": "elite performance bodysuit, dynamic cutouts, motion-designed",
        "material": "elite performance fabric, aerodynamic design",
        "environment": "elite training facility, clean modern space",
        "lighting": "motion freeze strobe, dynamic light, action emphasis",
        "style": "Nike elite editorial, sports performance photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── LIQUID & METALLIC ─────────────────────────────────
    "mercury_rising": {
        "tag": "Mercury Rising",
        "subject": "a mercury-like fluid female model",
        "body": "sleek powerful figure, liquid movement, full body shot",
        "outfit": "liquid mercury bodysuit, flowing silver metal, fluid couture",
        "material": "liquid mercury metal, flowing silver finish",
        "environment": "silver mercury pool environment, reflective floor",
        "lighting": "pure silver light, mercury reflections, liquid glow",
        "style": "liquid metal editorial, Mugler mercury fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "molten_chrome": {
        "tag": "Molten Chrome",
        "subject": "a molten chrome female model",
        "body": "powerful glamorous figure, chrome-covered, full body shot",
        "outfit": "molten chrome bodysuit, liquid metal dripping effect, surreal",
        "material": "molten chrome liquid metal, surreal finish",
        "environment": "chrome foundry, molten metal environment",
        "lighting": "extreme chrome reflections, molten orange glow",
        "style": "surreal chrome editorial, hyperrealistic fashion photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "frozen_latex": {
        "tag": "Frozen Latex",
        "subject": "a frozen crystal female model",
        "body": "sleek tall figure, frozen pose, full body shot",
        "outfit": "frozen latex bodysuit, ice crystal formations on surface, cold",
        "material": "frozen latex with ice crystal texture, cold finish",
        "environment": "ice crystal cave, frozen environment",
        "lighting": "cold blue crystal light, ice reflections, frozen atmosphere",
        "style": "frozen crystal editorial, ice fashion photography",
        "quality": "shot on Phase One XF IQ4, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "oil_slick_noir": {
        "tag": "Oil Slick Noir",
        "subject": "a iridescent dark female model",
        "body": "powerful dark figure, mysterious presence, full body shot",
        "outfit": "oil slick iridescent noir bodysuit, rainbow-black sheen, mysterious",
        "material": "oil slick iridescent fabric, rainbow-on-black effect",
        "environment": "dark wet industrial floor, oil puddles",
        "lighting": "iridescent light, oil-slick reflections, dark rainbow",
        "style": "oil slick editorial, dark iridescent fashion photography",
        "quality": "shot on Nikon Z9, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── ETHEREAL ATMOSPHERE ───────────────────────────────
    "storm_couture": {
        "tag": "Storm Couture",
        "subject": "a fierce storm female model",
        "body": "powerful figure, wind-blown dynamic, full body shot",
        "outfit": "storm couture gown, fabric violently windswept, dramatic movement",
        "material": "storm-reactive silk, wind-dynamic fabric",
        "environment": "dramatic storm cliff, lightning sky, powerful wind",
        "lighting": "lightning flash light, storm atmosphere, dramatic",
        "style": "Alexander McQueen storm editorial, dramatic fashion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "mist_vanguard": {
        "tag": "Mist Vanguard",
        "subject": "a mysterious mist female model",
        "body": "ethereal slender figure, silhouette emphasis, full body shot",
        "outfit": "mist-white minimal bodysuit, silhouette-defining, ethereal",
        "material": "mist-white fabric, translucent ethereal material",
        "environment": "dense white mist forest, mysterious fog",
        "lighting": "diffused mist light, silhouette emphasis, mysterious",
        "style": "Nick Knight mist editorial, ethereal fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "desert_sand_glam": {
        "tag": "Desert Sand Glam",
        "subject": "a desert goddess female model",
        "body": "glamorous toned figure, bronzed skin, long legs, full body shot",
        "outfit": "desert sand micro dress, windswept fabric, earth tones",
        "material": "sand-silk, earth-tone iridescent fabric",
        "environment": "Sahara sand storm, swirling golden sand particles",
        "lighting": "zenith desert sun, sand particle scatter, golden haze",
        "style": "Sahara desert editorial, sand glamour photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── ARCHITECTURAL MINIMAL ─────────────────────────────
    "brutalist_glam": {
        "tag": "Brutalist Glam",
        "subject": "a powerful brutalist female model",
        "body": "powerful statuesque figure, smooth skin contrast, full body shot",
        "outfit": "minimal concrete-grey bodysuit, brutalist design, architectural",
        "material": "concrete-texture fabric, brutalist aesthetic",
        "environment": "raw concrete brutalist architecture, Le Corbusier building",
        "lighting": "harsh directional light, concrete shadow texture",
        "style": "brutalist fashion editorial, architectural photography",
        "quality": "shot on Phase One XF IQ4, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "marble_minimal": {
        "tag": "Marble Minimal",
        "subject": "a marble-cold minimal female model",
        "body": "statuesque elegant figure, marble-smooth skin, full body shot",
        "outfit": "pure white marble-finish bodysuit, cold minimal aesthetic",
        "material": "marble-texture white fabric, cold surface finish",
        "environment": "pure white marble hall, Carrara marble",
        "lighting": "cold diffused marble light, pure white atmosphere",
        "style": "marble minimal editorial, cold luxury photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"
    },

    # ── CLASSIC REBELLION ─────────────────────────────────
    "baroque_punk": {
        "tag": "Baroque Punk",
        "subject": "a baroque punk rebel female model",
        "body": "powerful voluptuous figure, rebel attitude, full body shot",
        "outfit": "baroque PVC corset, gold ornate details, punk rebellion mix",
        "material": "baroque PVC with gold embroidery, rebellion fabric",
        "environment": "baroque palace with punk elements, gold and grunge",
        "lighting": "baroque candlelight with harsh punk strobe",
        "style": "Vivienne Westwood baroque punk editorial, rebellion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "noir_ballet": {
        "tag": "Noir Ballet",
        "subject": "a dark ballet female model",
        "body": "ballet figure, graceful yet dark, long legs, full body shot",
        "outfit": "noir ballet bodysuit, dark tutu, dramatic black pointe shoes",
        "material": "dark silk tulle, noir ballet fabric",
        "environment": "dark dramatic stage, single spotlight on dancer",
        "lighting": "dramatic ballet spotlight, dark stage atmosphere",
        "style": "Black Swan editorial, dark ballet fashion photography",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    },
}

def main():
    print("\n  ✦ LumineX 프리셋 생성 시작...\n")
    created = 0
    skipped = 0

    all_presets = {**PRESETS, **NEW_PRESETS}

    for name, data in all_presets.items():
        path = os.path.join(PRESETS_DIR, f"{name}.json")
        if os.path.exists(path):
            print(f"  ⏭️  건너뜀 (이미 존재): {name}.json")
            skipped += 1
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  ✅ 생성: {name}.json")
            created += 1

    print(f"\n  완료: 생성 {created}개 / 건너뜀 {skipped}개")
    print(f"  총 프리셋: {len(os.listdir(PRESETS_DIR))}개\n")

if __name__ == "__main__":
    main()