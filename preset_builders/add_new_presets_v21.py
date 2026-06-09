"""
add_new_presets_v21.py
신규 섹시/글래머 프리셋 48개

💫 럭셔리 글래머 (13개) → 💫 럭셔리 글래머
  luxury_noir, diamond_couture, velvet_serpent, opera_glam, silver_screen,
  lace_noir, white_silk_goddess, crystal_bodycon, penthouse_glam,
  midnight_couture, crimson_gown, serpentine_dress, baroque_glam

🔥 핫 & 섹시 (19개) → 🔥 핫 & 섹시
  fishnet_goddess, see_through_gown, wet_tshirt, string_bikini, lace_bodysuit,
  satin_slip, velvet_corset, body_chain_only, strappy_dress, cut_out_swimsuit,
  monokini_goddess, champagne_drip, neon_bodysuit, bikini_top_only,
  white_linen_sheer, oil_drip_body, yoga_pants_glam, micro_skirt, halter_glam

💋 에로틱 & 페티쉬 (16개) → 💋 에로틱 & 페티쉬
  latex_catsuit_red, rubber_goddess, harness_only, rope_bondage_art,
  vinyl_goddess, corset_stockings, catsuit_zipper, bodystocking,
  secretary_after_hours, nurse_sensual, maid_sensual, leather_bodysuit,
  wet_latex, fetish_boots_only, dominatrix_red, fishnet_bodysuit

총 프리셋: 729 → 777개
"""

import json
from pathlib import Path

PRESETS_DIR = Path("presets")
PRESETS_DIR.mkdir(exist_ok=True)

new_presets = {

    # ═══════════════════════════════════════
    # 💫 럭셔리 글래머 (13개)
    # ═══════════════════════════════════════

    "luxury_noir": {
        "tag": "Luxury Noir",
        "subject": "a sophisticated female model in black satin gown with opera gloves",
        "outfit": "floor-length black satin gown, long opera gloves, pearl choker, stilettos",
        "material": "lustrous black satin, fine pearl",
        "environment": "grand ballroom with crystal chandeliers, black marble floors",
        "lighting": "dramatic rim lighting, deep shadows, single key light",
        "style": "Vogue editorial, monochrome luxury fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography, cinematic",
    },

    "diamond_couture": {
        "tag": "Diamond Couture",
        "subject": "an ultra-glamorous female model in diamond-encrusted gala gown",
        "outfit": "structured strapless ball gown with diamond crystal embellishments, elbow gloves",
        "material": "duchess satin, Swarovski crystals, diamond detailing",
        "environment": "grand opera house, crystal chandelier, marble staircase",
        "lighting": "golden chandelier light, sparkling diamond reflections",
        "style": "haute couture editorial, Vanity Fair gala",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "velvet_serpent": {
        "tag": "Velvet Serpent",
        "subject": "a powerful female model in deep green velvet gown with snake motif",
        "outfit": "deep forest green velvet gown, power shoulders, snake scale texture accents, thigh slit",
        "material": "crushed velvet, snakeskin embossing, emerald jewels",
        "environment": "dark luxury penthouse, floor-to-ceiling windows, city lights",
        "lighting": "moody green accent lighting, dramatic shadows",
        "style": "power glamour editorial, fierce luxury",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "opera_glam": {
        "tag": "Opera Glam",
        "subject": "a classically glamorous female model in strapless gown with fur stole",
        "outfit": "strapless silk column gown, long opera gloves, white fur stole, diamond earrings",
        "material": "silk charmeuse, white mink fur, fine kid leather gloves",
        "environment": "grand opera house interior, red velvet seats, gold ornaments",
        "lighting": "warm theatrical spotlight, golden ambient",
        "style": "classic Hollywood glamour, 1950s haute couture",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "silver_screen": {
        "tag": "Silver Screen",
        "subject": "a classic Hollywood glamour female model with finger waves",
        "outfit": "silver bias-cut satin gown, finger wave hair, elbow gloves, vintage brooch",
        "material": "silver liquid satin, silk charmeuse",
        "environment": "1940s Hollywood studio, art deco set, silver backdrop",
        "lighting": "classic Hollywood three-point lighting, silver gelatin tone",
        "style": "1940s Hollywood golden age, silver screen goddess",
        "quality": "ultra-sharp, 8K, cinematic black and silver tones",
    },

    "lace_noir": {
        "tag": "Lace Noir",
        "subject": "a mysterious female model in black lace full-length dress with veil",
        "outfit": "floor-length black Chantilly lace gown, face veil, lace gloves, stilettos",
        "material": "Chantilly lace, silk underlining, fine tulle veil",
        "environment": "gothic candlelit chapel, stone arches, flickering candles",
        "lighting": "candlelight only, dramatic chiaroscuro, deep shadows",
        "style": "dark luxury editorial, gothic glamour",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "white_silk_goddess": {
        "tag": "White Silk Goddess",
        "subject": "a goddess-like female model draped in flowing white silk",
        "outfit": "draped white silk toga-style gown, one shoulder, flowing fabric, barefoot",
        "material": "pure white silk charmeuse, liquid drape",
        "environment": "ancient Greek marble temple, white columns, Mediterranean light",
        "lighting": "soft golden Mediterranean sunlight, white marble reflections",
        "style": "Greco-Roman goddess, neoclassical fashion editorial",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "crystal_bodycon": {
        "tag": "Crystal Bodycon",
        "subject": "a dazzling female model in crystal-encrusted mini bodycon dress",
        "outfit": "crystal Swarovski-encrusted mini bodycon dress, strappy heels",
        "material": "stretch jersey base, Swarovski crystal embellishment all over",
        "environment": "exclusive VIP nightclub, mirror walls, purple neon",
        "lighting": "prismatic crystal light reflections, purple UV glow",
        "style": "VIP club glamour, sparkle fashion editorial",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "penthouse_glam": {
        "tag": "Penthouse Glam",
        "subject": "an elite glamorous female model in designer dress with city skyline",
        "outfit": "designer structured cocktail dress, strappy heels, statement jewelry",
        "material": "silk crepe, fine jewelry",
        "environment": "luxury penthouse, floor-to-ceiling windows, city night skyline, wine glass",
        "lighting": "city glow through windows, warm interior accent lights",
        "style": "elite lifestyle editorial, luxury penthouse fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "midnight_couture": {
        "tag": "Midnight Couture",
        "subject": "an ethereal female model in midnight blue couture gown",
        "outfit": "midnight blue structured couture gown, dramatic train, sapphire jewelry",
        "material": "silk faille, hand-beaded midnight blue, sapphire stones",
        "environment": "moonlit rooftop terrace, dark blue sky, scattered stars",
        "lighting": "moonlight, soft blue ambient, star reflections",
        "style": "couture fashion editorial, midnight blue palette",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "crimson_gown": {
        "tag": "Crimson Gown",
        "subject": "a statuesque female model in crimson floor-length column gown",
        "outfit": "deep crimson floor-length column gown, strapless, thigh slit, red stilettos",
        "material": "heavy silk duchess satin, rich crimson",
        "environment": "grand theater lobby, red velvet curtains, golden details",
        "lighting": "dramatic theater lighting, red atmosphere",
        "style": "dramatic fashion editorial, power red glamour",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "serpentine_dress": {
        "tag": "Serpentine Dress",
        "subject": "a sleek female model in snakeskin print slip dress on NYC rooftop",
        "outfit": "figure-hugging snakeskin print slip dress, barely-there straps, mule heels",
        "material": "silk-blend snakeskin print, bias cut",
        "environment": "New York City rooftop, Manhattan skyline at dusk",
        "lighting": "golden hour city glow, warm ambient",
        "style": "New York fashion editorial, urban chic glamour",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "baroque_glam": {
        "tag": "Baroque Glam",
        "subject": "an opulent female model in baroque gold-embellished velvet gown",
        "outfit": "baroque gold brocade velvet gown, jeweled bodice, pearl and gold accessories",
        "material": "gold brocade velvet, baroque pearl, ornate gold jewelry",
        "environment": "baroque palace interior, gilded mirrors, crystal chandeliers",
        "lighting": "chandelier warmth, gilded reflections, baroque drama",
        "style": "baroque luxury editorial, opulent fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 🔥 핫 & 섹시 (19개)
    # ═══════════════════════════════════════

    "fishnet_goddess": {
        "tag": "Fishnet Goddess",
        "subject": "a rock-chic sexy female model in full-body fishnet",
        "outfit": "full-body fishnet stocking worn as top, leather mini skirt, platform boots",
        "material": "black fishnet, leather",
        "environment": "rock club with neon signs, brick walls, red and purple neon",
        "lighting": "neon glow, moody club lighting, rim light",
        "style": "rock chic editorial, edgy sexy fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "see_through_gown": {
        "tag": "See Through Gown",
        "subject": "a sensual female model in fully sheer chiffon floor-length gown",
        "outfit": "fully sheer chiffon floor-length gown, body visible through fabric, minimal underneath",
        "material": "ultra-sheer chiffon, translucent silk organza",
        "environment": "luxury hotel suite, soft morning light through curtains",
        "lighting": "soft diffused backlight through sheer fabric, angelic glow",
        "style": "sheer fashion editorial, sensual luxury",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "wet_tshirt": {
        "tag": "Wet T-Shirt",
        "subject": "a sexy female model in soaking wet white t-shirt on summer beach",
        "outfit": "soaking wet white fitted t-shirt, denim cutoff shorts, barefoot",
        "material": "wet cotton, clinging fabric",
        "environment": "golden sandy beach, ocean waves, golden hour",
        "lighting": "warm golden sunset, natural beach light",
        "style": "summer beach editorial, natural sexy",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "string_bikini": {
        "tag": "String Bikini",
        "subject": "a toned female model in triangle string bikini on tropical beach",
        "outfit": "minimal triangle string bikini top, string bikini bottom, gold body chain",
        "material": "thin string, minimal triangle fabric",
        "environment": "tropical beach, turquoise water, white sand, golden hour",
        "lighting": "warm golden hour sunlight, tropical glow",
        "style": "Sports Illustrated swimwear editorial, beach goddess",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "lace_bodysuit": {
        "tag": "Lace Bodysuit",
        "subject": "a glamorous female model in intricate lace bodysuit with garter",
        "outfit": "full lace bodysuit, garter straps visible, thigh-high stockings, stilettos",
        "material": "delicate French lace, silk stockings",
        "environment": "boudoir bedroom, velvet chaise lounge, soft rose lighting",
        "lighting": "warm rose-gold ambient, soft candlelight",
        "style": "boudoir glamour editorial, intimate fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "satin_slip": {
        "tag": "Satin Slip",
        "subject": "a sensual female model in satin slip dress in morning light",
        "outfit": "bias-cut satin slip dress, thin spaghetti straps, mid-thigh length, barefoot",
        "material": "liquid silk satin, champagne or blush color",
        "environment": "luxury bedroom, white linen sheets, morning sunlight through sheer curtains",
        "lighting": "soft morning backlight, golden hour warmth",
        "style": "intimate bedroom editorial, sensual morning",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "velvet_corset": {
        "tag": "Velvet Corset",
        "subject": "a vintage-sexy female model in burgundy velvet corset",
        "outfit": "burgundy velvet boned corset, high-waist skirt, stockings, Victorian-inspired",
        "material": "crushed burgundy velvet, boning, lace trim",
        "environment": "Victorian boudoir, antique mirror, warm candlelight",
        "lighting": "warm candlelight, vintage amber tones",
        "style": "vintage boudoir editorial, corset fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "body_chain_only": {
        "tag": "Body Chain Only",
        "subject": "a sculpted female model wearing only layered golden body chain jewelry",
        "outfit": "layered gold body chain jewelry only, artfully draped across body, oiled skin",
        "material": "14k gold body chains, delicate linked chains",
        "environment": "minimalist white studio OR desert dunes at golden hour",
        "lighting": "strong directional light emphasizing body contours and gold reflections",
        "style": "high fashion body jewelry editorial, sculptural",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "strappy_dress": {
        "tag": "Strappy Dress",
        "subject": "a sexy female model in strappy mini dress at neon-lit club",
        "outfit": "strappy minimal mini dress, multiple thin straps, barely-there coverage, strappy heels",
        "material": "stretchy matte jersey, thin straps",
        "environment": "exclusive nightclub, neon purple and pink lighting, VIP area",
        "lighting": "neon club lights, purple and pink glow",
        "style": "nightlife fashion editorial, club sexy",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "cut_out_swimsuit": {
        "tag": "Cut Out Swimsuit",
        "subject": "a fit female model in dramatic cut-out one-piece swimsuit",
        "outfit": "one-piece swimsuit with extreme cut-out panels, side and midriff exposed",
        "material": "high-quality stretch swimwear fabric",
        "environment": "infinity pool overlooking ocean, luxury resort, blue sky",
        "lighting": "bright tropical sunlight, pool reflections, sparkling water",
        "style": "luxury resort swimwear editorial",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "monokini_goddess": {
        "tag": "Monokini Goddess",
        "subject": "a toned female model in daring monokini at sunset pool",
        "outfit": "daring monokini with strategic cut-outs and connecting straps, minimal coverage",
        "material": "stretch fabric, thin connecting straps",
        "environment": "outdoor infinity pool, sunset orange and pink sky, palm trees",
        "lighting": "golden sunset light, warm orange tones, pool shimmer",
        "style": "luxury pool editorial, swimwear goddess",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "champagne_drip": {
        "tag": "Champagne Drip",
        "subject": "a playful sexy female model with champagne dripping on her dress",
        "outfit": "wet white or gold mini dress, champagne dripping down body, stilettos",
        "material": "wet clinging fabric, champagne soaked",
        "environment": "luxury party setting, golden confetti, champagne tower",
        "lighting": "warm party lighting, golden sparkle, flash photography style",
        "style": "luxury party editorial, wet and wild glamour",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "neon_bodysuit": {
        "tag": "Neon Bodysuit",
        "subject": "a sexy female model in neon bodysuit under UV club lights",
        "outfit": "neon green or pink bodysuit, thong cut, UV reactive, strappy heels",
        "material": "UV-reactive neon spandex, second-skin fit",
        "environment": "underground UV club, black light, neon paint splashes on walls",
        "lighting": "UV black light, neon glow, electric atmosphere",
        "style": "UV rave editorial, neon sexy",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "bikini_top_only": {
        "tag": "Bikini Top Only",
        "subject": "a carefree sexy female model in bikini top and denim cutoffs at festival",
        "outfit": "bright bikini top, distressed denim cutoff shorts, festival accessories",
        "material": "bikini fabric, distressed denim",
        "environment": "outdoor music festival, crowd behind, sunny day, colorful flags",
        "lighting": "bright festival sunlight, warm and vibrant",
        "style": "festival fashion editorial, summer carefree sexy",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "white_linen_sheer": {
        "tag": "White Linen Sheer",
        "subject": "a sun-kissed female model in sheer white linen at Greek island beach",
        "outfit": "sheer white linen beach cover-up, barely covering bikini underneath, barefoot",
        "material": "ultra-sheer white linen, natural fabric",
        "environment": "Santorini beach, blue Aegean sea, white buildings, warm sunlight",
        "lighting": "bright Mediterranean sunlight, translucent fabric backlit",
        "style": "resort lifestyle editorial, Mediterranean sexy",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "oil_drip_body": {
        "tag": "Oil Drip Body",
        "subject": "a glistening female model with oil dripping on sleek mini dress",
        "outfit": "sleek black or gold mini dress, oil dripping down shoulders and legs, strappy heels",
        "material": "PU leather or vinyl mini dress, body oil",
        "environment": "minimalist dark studio, reflective floor",
        "lighting": "strong side lighting highlighting oil drips and body contours",
        "style": "high contrast body editorial, oil and skin",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "yoga_pants_glam": {
        "tag": "Yoga Pants Glam",
        "subject": "a sporty-sexy female model in high-waist yoga pants and sports bra",
        "outfit": "high-waist sculpting yoga pants, matching sports bra crop top, perfect fit",
        "material": "high-performance compression fabric, second-skin",
        "environment": "luxury fitness studio OR rooftop with city view at golden hour",
        "lighting": "warm golden hour light, body-flattering",
        "style": "athleisure editorial, sporty sexy fitness",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "micro_skirt": {
        "tag": "Micro Skirt",
        "subject": "a leggy female model in micro mini skirt and crop top",
        "outfit": "micro mini skirt barely covering, fitted crop top, strappy heeled sandals",
        "material": "stretch fabric, minimal",
        "environment": "chic Parisian street OR rooftop bar",
        "lighting": "golden hour natural light, warm and flattering",
        "style": "street chic editorial, European sexy fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "halter_glam": {
        "tag": "Halter Glam",
        "subject": "a sun-kissed female model in halter top showing midriff on luxury cruise",
        "outfit": "tied halter neck top, low-rise wide-leg pants or mini skirt, midriff exposed",
        "material": "silk halter, lightweight fabric",
        "environment": "luxury cruise deck, ocean horizon, sunset",
        "lighting": "sunset golden light, ocean breeze atmosphere",
        "style": "cruise fashion editorial, Mediterranean halter glam",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 💋 에로틱 & 페티쉬 (16개)
    # ═══════════════════════════════════════

    "latex_catsuit_red": {
        "tag": "Latex Catsuit Red",
        "subject": "a fierce female model in red latex full-body catsuit",
        "outfit": "fire engine red latex full-body catsuit, high collar, stiletto boots",
        "material": "shiny red latex, second-skin fit",
        "environment": "industrial warehouse, dramatic red spotlights, smoke",
        "lighting": "red dramatic spotlight, high contrast, latex sheen",
        "style": "fetish fashion editorial, red latex power",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "rubber_goddess": {
        "tag": "Rubber Goddess",
        "subject": "a futuristic female model in high-gloss rubber full bodysuit",
        "outfit": "high-gloss black rubber full bodysuit, futuristic styling, platform boots",
        "material": "high-gloss rubber, PVC",
        "environment": "sci-fi set, metallic silver backdrop, geometric shapes",
        "lighting": "cold blue-white light, metallic reflections, futuristic",
        "style": "sci-fi fetish editorial, rubber couture",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "harness_only": {
        "tag": "Harness Only",
        "subject": "a bold female model wearing only intricate leather body harness",
        "outfit": "intricate leather body harness worn alone, artfully covering key areas, boots",
        "material": "fine leather straps, metal hardware",
        "environment": "industrial loft, exposed brick, dramatic single spotlight",
        "lighting": "single strong key light, deep shadows, dramatic",
        "style": "editorial fetish fashion, body harness art",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "rope_bondage_art": {
        "tag": "Rope Bondage Art",
        "subject": "a graceful female model in Japanese shibari rope art",
        "outfit": "artistic shibari rope binding as garment, minimal underneath, cultural art context",
        "material": "natural jute rope, artistic knots",
        "environment": "Japanese minimalist studio, tatami, shoji screen",
        "lighting": "soft diffused Japanese paper lamp light, rope shadow patterns",
        "style": "shibari body art editorial, Japanese rope art",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "vinyl_goddess": {
        "tag": "Vinyl Goddess",
        "subject": "a cyberpunk female model in shiny vinyl micro skirt and crop top",
        "outfit": "shiny vinyl micro skirt, matching vinyl crop top, thigh-high PVC boots",
        "material": "shiny vinyl, PVC",
        "environment": "cyberpunk alley, neon signs, rain-slicked streets",
        "lighting": "neon reflection on vinyl, cyberpunk colors, rain glow",
        "style": "cyberpunk fetish editorial, vinyl fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "corset_stockings": {
        "tag": "Corset Stockings",
        "subject": "a vintage-erotic female model in full corset and stocking set",
        "outfit": "waist-cinching satin corset, suspender garter belt, silk stockings, heels",
        "material": "boned satin corset, silk stockings, lace trim",
        "environment": "Victorian boudoir, red velvet, ornate mirror, rose petals",
        "lighting": "warm candlelight, intimate boudoir glow",
        "style": "Victorian boudoir editorial, vintage erotic",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "catsuit_zipper": {
        "tag": "Catsuit Zipper",
        "subject": "a provocative female model in partially unzipped black catsuit",
        "outfit": "black catsuit with front zipper pulled down showing cleavage, unzipped detail",
        "material": "matte or shiny stretch fabric, metal zipper",
        "environment": "luxury hotel corridor OR dark rooftop at night",
        "lighting": "moody low key lighting, single accent light",
        "style": "edgy fashion editorial, zipper detail",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "bodystocking": {
        "tag": "Bodystocking",
        "subject": "a sultry female model in full-body sheer stocking bodysuit",
        "outfit": "full-body sheer stocking bodysuit, body silhouette visible through mesh",
        "material": "ultra-sheer nylon mesh, full-body coverage",
        "environment": "minimalist white studio, clean aesthetic",
        "lighting": "soft even lighting showing silhouette through fabric",
        "style": "avant-garde fashion editorial, body stocking art",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "secretary_after_hours": {
        "tag": "Secretary After Hours",
        "subject": "a seductive female model as after-hours secretary in unbuttoned suit",
        "outfit": "tight pencil skirt, suit jacket unbuttoned low, silk blouse open, reading glasses, heels",
        "material": "tailored wool suit, silk blouse",
        "environment": "executive office at night, city lights through window, desk with papers",
        "lighting": "desk lamp spotlight, city glow, intimate office night",
        "style": "power fantasy editorial, office after-hours",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "nurse_sensual": {
        "tag": "Nurse Sensual",
        "subject": "a sensual female model in ultra form-fitting nurse uniform",
        "outfit": "ultra form-fitting white nurse dress, very short hem, stockings, white heels",
        "material": "stretch white uniform fabric, silk stockings",
        "environment": "clinical white room OR moody hospital corridor",
        "lighting": "clinical white light OR moody corridor lighting",
        "style": "role-play fashion editorial, sensual uniform",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "maid_sensual": {
        "tag": "Maid Sensual",
        "subject": "a flirtatious female model in ultra-short French maid costume",
        "outfit": "ultra-short French maid dress, white lace apron, stockings, kitten heels, feather duster",
        "material": "black dress fabric, white lace apron, silk stockings",
        "environment": "luxury mansion interior, ornate bedroom, velvet curtains",
        "lighting": "warm interior lighting, intimate manor atmosphere",
        "style": "role-play fashion editorial, French maid glamour",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "leather_bodysuit": {
        "tag": "Leather Bodysuit",
        "subject": "a fierce female model in studded leather bodysuit",
        "outfit": "black leather bodysuit, metal stud details, cutout panels, combat boots",
        "material": "genuine leather, metal studs, hardware",
        "environment": "rock venue backstage OR industrial setting",
        "lighting": "dramatic stage lighting, hard shadows, rock atmosphere",
        "style": "rock goddess editorial, leather fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "wet_latex": {
        "tag": "Wet Latex",
        "subject": "a drenched female model in wet shiny latex in rain",
        "outfit": "wet shiny black latex mini dress, rain soaked, stilettos",
        "material": "shiny latex, water droplets",
        "environment": "rain-soaked urban street at night, street lights, puddles reflecting neon",
        "lighting": "street light reflections on wet latex, rain atmosphere, neon glow",
        "style": "wet fetish editorial, rain and latex",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "fetish_boots_only": {
        "tag": "Fetish Boots Only",
        "subject": "a dominant female model in thigh-high over-knee boots as statement piece",
        "outfit": "thigh-high over-knee boots as focus, minimal micro outfit above, boots as main statement",
        "material": "patent leather or latex over-knee boots",
        "environment": "minimalist dark studio OR catwalk stage",
        "lighting": "spotlight on boots, high contrast, dramatic",
        "style": "fetish boot editorial, dominant fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "dominatrix_red": {
        "tag": "Dominatrix Red",
        "subject": "a powerful female dominatrix in red latex with riding crop",
        "outfit": "red latex corset, red latex thigh-highs, red stiletto boots, riding crop prop",
        "material": "shiny red latex, patent leather",
        "environment": "dark dramatic set, red lighting, high contrast shadows",
        "lighting": "dramatic red lighting, high contrast shadows",
        "style": "dominatrix fashion editorial, red power",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "fishnet_bodysuit": {
        "tag": "Fishnet Bodysuit",
        "subject": "a sultry female model in fishnet bodysuit with lingerie underneath",
        "outfit": "large-weave fishnet bodysuit over matching bra and thong, garter clips visible",
        "material": "black fishnet, satin lingerie underneath",
        "environment": "boudoir with velvet and mirrors OR moody editorial studio",
        "lighting": "warm intimate boudoir lighting, low key",
        "style": "lingerie editorial, fishnet boudoir",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },
}

# ─── dashboard.py PRESET_CATEGORIES 추가 코드 안내 ────────
LUXURY_ADDITIONS = [
    "luxury_noir", "diamond_couture", "velvet_serpent", "opera_glam", "silver_screen",
    "lace_noir", "white_silk_goddess", "crystal_bodycon", "penthouse_glam",
    "midnight_couture", "crimson_gown", "serpentine_dress", "baroque_glam",
]

HOT_SEXY_ADDITIONS = [
    "fishnet_goddess", "see_through_gown", "wet_tshirt", "string_bikini", "lace_bodysuit",
    "satin_slip", "velvet_corset", "body_chain_only", "strappy_dress", "cut_out_swimsuit",
    "monokini_goddess", "champagne_drip", "neon_bodysuit", "bikini_top_only",
    "white_linen_sheer", "oil_drip_body", "yoga_pants_glam", "micro_skirt", "halter_glam",
]

EROTIC_ADDITIONS = [
    "latex_catsuit_red", "rubber_goddess", "harness_only", "rope_bondage_art",
    "vinyl_goddess", "corset_stockings", "catsuit_zipper", "bodystocking",
    "secretary_after_hours", "nurse_sensual", "maid_sensual", "leather_bodysuit",
    "wet_latex", "fetish_boots_only", "dominatrix_red", "fishnet_bodysuit",
]

# ─── JSON 파일 생성 ────────────────────────────────────────
added = 0
skipped = 0
for name, data in new_presets.items():
    path = PRESETS_DIR / f"{name}.json"
    if path.exists():
        print(f"⏭️  skip: {name}")
        skipped += 1
    else:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ added: {name}")
        added += 1

print(f"\n완료: {added}개 추가, {skipped}개 스킵")
print(f"총 프리셋: 729 → {729 + added}개")
print(f"\n─── dashboard.py PRESET_CATEGORIES 추가 필요 ───")
print(f"\n💫 럭셔리 글래머 끝에 추가 ({len(LUXURY_ADDITIONS)}개):")
for name in LUXURY_ADDITIONS:
    print(f'        "{name}",')
print(f"\n🔥 핫 & 섹시 끝에 추가 ({len(HOT_SEXY_ADDITIONS)}개):")
for name in HOT_SEXY_ADDITIONS:
    print(f'        "{name}",')
print(f"\n💋 에로틱 & 페티쉬 끝에 추가 ({len(EROTIC_ADDITIONS)}개):")
for name in EROTIC_ADDITIONS:
    print(f'        "{name}",')
