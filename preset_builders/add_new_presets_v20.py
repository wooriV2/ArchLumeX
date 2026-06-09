"""
add_new_presets_v20.py
신규 바디페인팅 프리셋 39개

🗺️ 지도 계열 (13개) → 🖌️ 바디페인팅 & 스킨 트랜스폼
  world_map_body, topographic_body, ocean_depth_body, thermal_map_body,
  weather_map_body, subway_map_body, europe_political_body, africa_tribes_body,
  japan_prefecture_body, ancient_map_body, fantasy_map_body, star_map_body,
  usa_county_map_body

🔬 과학/자연현상 (5개) → 🖌️ 바디페인팅 & 스킨 트랜스폼
  thermal_scan_body, xray_body, circuit_board_body, galaxy_nebula_body,
  crystal_geode_body

🏛️ 문명/문자 (6개) → 🖌️ 바디페인팅 & 스킨 트랜스폼
  hieroglyph_body, aztec_calendar_body, celtic_knot_body,
  arabic_calligraphy_body, islamic_geometric_body, greek_mosaic_body

🌿 식물/자연 (3개) → 🖌️ 바디페인팅 & 스킨 트랜스폼
  autumn_leaves_body, coral_reef_body, mushroom_forest_body

🎨 건축/패턴 (2개) → 🖌️ 바디페인팅 & 스킨 트랜스폼
  stained_glass_body, bauhaus_body

🚩 국기 (8개) → 🏺 문명 & 신화
  union_jack_body, brazil_flag_body, usa_stars_stripes_body,
  japan_rising_sun_body, south_africa_flag_body, india_flag_body,
  mexico_flag_body, ukraine_flag_body

🏚️ 환경융합 (2개) → 🖌️ 바디페인팅 & 스킨 트랜스폼
  urban_decay_body, forest_stone_body

총 프리셋: 697 → 736개
"""

import json
from pathlib import Path

PRESETS_DIR = Path("presets")
PRESETS_DIR.mkdir(exist_ok=True)

new_presets = {

    # ═══════════════════════════════════════
    # 🗺️ 지도 계열 (13개)
    # ═══════════════════════════════════════

    "world_map_body": {
        "tag": "World Map Body",
        "subject": "a fine art body painting model with world map cartography painted across her entire body",
        "body": "elegant figure, living atlas, continents mapped across skin",
        "outfit": "entire body painted as a detailed world map — blue oceans, green-brown continents, country borders, latitude longitude grid lines painted directly on bare skin, NO clothing, NO fabric, painted illusion only",
        "material": "cartographic body paint pigment, atlas color palette, ocean blue and earth tone pigments applied directly on bare skin",
        "environment": "minimalist white studio with faint globe projection backdrop",
        "lighting": "soft diffused studio light, cartographic clarity",
        "style": "fine art body painting editorial, living atlas concept, world geography body art",
        "quality": "shot on Hasselblad, hyperrealistic body paint art, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "topographic_body": {
        "tag": "Topographic Body",
        "subject": "a fine art body painting model with topographic contour map painted across her entire body",
        "body": "sculptural figure, living terrain, elevation lines following body curves",
        "outfit": "entire body painted as topographic map — brown and green contour elevation lines flowing across skin following body curves, mountain peaks at shoulders, valley lines at waist, painted directly on bare skin, NO clothing, NO fabric",
        "material": "topographic survey body paint, earth tone contour line pigments, elevation gradient colors applied directly on bare skin",
        "environment": "geological survey aesthetic, relief map backdrop, natural earth tones",
        "lighting": "overhead map-light, clinical cartographic illumination",
        "style": "fine art topographic body art editorial, living terrain sculpture, contour map body painting",
        "quality": "shot on Phase One, ultra-precise line detail, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "ocean_depth_body": {
        "tag": "Ocean Depth Body",
        "subject": "a fine art body painting model with ocean depth bathymetric map painted across her entire body",
        "body": "flowing figure, living ocean, depth gradients from surface to abyss",
        "outfit": "entire body painted as ocean depth map — deep navy abyss at core, electric teal mid-depths, turquoise shallow zones, white seafloor ridges, abyssal trenches as dark lines, painted directly on bare skin, NO clothing, NO fabric",
        "material": "bathymetric body paint, ocean depth gradient pigments — navy, cobalt, teal, aquamarine applied directly on bare skin",
        "environment": "deep ocean blue studio, submarine light shafts, bioluminescent atmosphere",
        "lighting": "deep underwater blue ambient, abyssal glow",
        "style": "oceanographic body art editorial, living bathymetric chart, deep sea body painting",
        "quality": "shot on Nikon Z9, hyperrealistic gradient paint, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "thermal_map_body": {
        "tag": "Thermal Map Body",
        "subject": "a fine art body painting model with thermal heat map painted across her entire body",
        "body": "dynamic figure, living heat signature, thermal energy radiating from skin",
        "outfit": "entire body painted as thermal heat map — fiery red-orange hotspots at core and joints, yellow warm zones at limbs, green neutral areas, blue-purple cool extremities, painted directly on bare skin, NO clothing, NO fabric",
        "material": "thermal imaging body paint pigments — infrared red, orange, yellow, green, blue gradient spectrum applied directly on bare skin",
        "environment": "dark studio with faint heat wave distortion, thermal camera aesthetic",
        "lighting": "dramatic rim lighting suggesting heat radiation, thermal glow",
        "style": "thermal imaging body art editorial, living heat signature, infrared body painting",
        "quality": "shot on Canon R5, vivid thermal gradient precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "weather_map_body": {
        "tag": "Weather Map Body",
        "subject": "a fine art body painting model with meteorological weather map painted across her entire body",
        "body": "atmospheric figure, living weather system, storm fronts across skin",
        "outfit": "entire body painted as weather map — isobars and pressure lines, cold front blues, warm front reds, storm spiral at torso, rain cloud grey patches, sunshine yellow zones, painted directly on bare skin, NO clothing, NO fabric",
        "material": "meteorological body paint — weather system colors, isobar line pigments, storm and sunshine palette applied directly on bare skin",
        "environment": "sky blue studio backdrop, cloud formations, atmospheric mood",
        "lighting": "dramatic storm light mixed with golden sunshine, weather contrast",
        "style": "meteorological body art editorial, living weather system, atmospheric body painting",
        "quality": "shot on Sony A1, atmospheric detail precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "subway_map_body": {
        "tag": "Subway Map Body",
        "subject": "a fine art body painting model with metropolitan subway transit map painted across her entire body",
        "body": "geometric figure, living transit network, colored lines flowing across skin",
        "outfit": "entire body painted as subway map — bold colored transit lines (red, blue, green, orange, yellow, purple) flowing across skin like veins, station dots at joints, route intersections at major points, painted directly on bare skin, NO clothing, NO fabric",
        "material": "transit map body paint — bold primary and secondary color line pigments, clean graphic precision applied directly on bare skin",
        "environment": "urban white tile backdrop suggesting subway station, metropolitan aesthetic",
        "lighting": "clean bright urban transit light, flat graphic illumination",
        "style": "metropolitan transit body art editorial, living subway map, urban graphic body painting",
        "quality": "shot on Leica M11, graphic precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "europe_political_body": {
        "tag": "Europe Political Body",
        "subject": "a fine art body painting model with European political map painted across her entire body",
        "body": "continental figure, living Europe, nations mapped across skin",
        "outfit": "entire body painted as European political map — each country in distinct color (France blue, Germany grey, Italy green, Spain orange, UK purple, Scandinavia yellow, Eastern Europe warm tones), borders clearly delineated, painted directly on bare skin, NO clothing, NO fabric",
        "material": "political map body paint — distinct country color pigments, border line precision applied directly on bare skin",
        "environment": "European architectural backdrop, classical marble aesthetic",
        "lighting": "Renaissance gallery lighting, continental grandeur",
        "style": "geopolitical body art editorial, living European atlas, political map body painting",
        "quality": "shot on Hasselblad X2D, cartographic precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "africa_tribes_body": {
        "tag": "Africa Tribes Body",
        "subject": "a fine art body painting model with African tribal territory map painted across her entire body",
        "body": "powerful figure, living Africa, tribal territories in rich earth tones",
        "outfit": "entire body painted as African tribal map — rich earth tones (ochre, sienna, terracotta, deep brown, forest green, gold) marking distinct tribal territories, ancient boundary lines, sahara gold in upper regions, equatorial green at center, painted directly on bare skin, NO clothing, NO fabric",
        "material": "African tribal map body paint — ochre, sienna, terracotta, gold, forest green pigments applied directly on bare skin",
        "environment": "savanna golden light, African landscape backdrop, ancient earth atmosphere",
        "lighting": "warm African golden hour, ancient land glow",
        "style": "African tribal geography body art editorial, living African atlas, tribal map body painting",
        "quality": "shot on Canon R3, rich earth tone precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "japan_prefecture_body": {
        "tag": "Japan Prefecture Body",
        "subject": "a fine art body painting model with Japanese prefecture map painted across her entire body",
        "body": "elegant figure, living Japan, prefectures in traditional colors",
        "outfit": "entire body painted as Japanese prefecture map — each prefecture in distinct traditional color (Hokkaido deep blue, Tokyo red, Kyoto gold, Osaka orange, Okinawa turquoise), island chains across limbs, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Japanese prefecture map body paint — traditional Japanese color palette pigments applied directly on bare skin",
        "environment": "minimalist Japanese aesthetic backdrop, zen white space",
        "lighting": "clean Japanese studio light, zen clarity",
        "style": "Japanese geographic body art editorial, living prefecture map, Japanese cartographic body painting",
        "quality": "shot on Sony A7R V, precise geographic detail, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "ancient_map_body": {
        "tag": "Ancient Map Body",
        "subject": "a fine art body painting model with ancient parchment world map painted across her entire body",
        "body": "timeless figure, living antiquity, terra incognita across skin",
        "outfit": "entire body painted as ancient cartography — aged parchment sepia tones, hand-drawn coastlines, mythological sea monsters at edges, Latin inscriptions, compass rose at chest, terra incognita zones, painted directly on bare skin, NO clothing, NO fabric",
        "material": "antique cartography body paint — aged sepia, parchment brown, ink black, gold pigments applied directly on bare skin",
        "environment": "aged library backdrop, candlelight, antique globe atmosphere",
        "lighting": "warm candlelight, antique golden glow, ancient mystery",
        "style": "antique cartographic body art editorial, living ancient map, historical geography body painting",
        "quality": "shot on Leica Q3, aged parchment texture precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "fantasy_map_body": {
        "tag": "Fantasy Map Body",
        "subject": "a fine art body painting model with fantasy world map painted across her entire body",
        "body": "mythical figure, living fantasy realm, imaginary kingdoms across skin",
        "outfit": "entire body painted as fantasy world map — illustrated kingdoms, dragon territories, enchanted forests in deep greens, ocean of storms in dark blue, mountain ranges as ridgelines, runic inscriptions, treasure markers, painted directly on bare skin, NO clothing, NO fabric",
        "material": "fantasy cartography body paint — illustrated map color palette, medieval manuscript pigments applied directly on bare skin",
        "environment": "fantasy realm backdrop, mystical fog, ancient runes",
        "lighting": "fantasy magical glow, torchlight and moonlight combined",
        "style": "fantasy world map body art editorial, living middle earth atlas, mythical cartography body painting",
        "quality": "shot on Nikon Z9, illustrated map aesthetic, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "star_map_body": {
        "tag": "Star Map Body",
        "subject": "a fine art body painting model with celestial star map and constellation chart painted across her entire body",
        "body": "cosmic figure, living star atlas, celestial sphere across skin",
        "outfit": "entire body painted as star map — deep midnight blue base, golden star clusters at Milky Way core, constellation line art connecting bright stars, nebula color clouds in purple and pink, zodiac belt across torso, painted directly on bare skin, NO clothing, NO fabric",
        "material": "celestial star map body paint — midnight blue, gold, silver, nebula purple and pink pigments applied directly on bare skin",
        "environment": "observatory dome backdrop, dark starfield, telescope silhouettes",
        "lighting": "starlight glow, deep space ambient, moonlight clarity",
        "style": "astronomical body art editorial, living star atlas, celestial map body painting",
        "quality": "shot on Sony A1, deep space color precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "usa_county_map_body": {
        "tag": "USA County Map Body",
        "subject": "a fine art body painting model with detailed USA county map painted across her entire body",
        "body": "expansive figure, living America, county grid across skin",
        "outfit": "entire body painted as US county map — thousands of county divisions in alternating distinct colors (red, blue, green, orange, purple, yellow mosaic), state borders thicker, coastlines defined, Great Lakes blue, painted directly on bare skin, NO clothing, NO fabric",
        "material": "political county map body paint — dense multicolor mosaic pigments applied directly on bare skin",
        "environment": "American flag inspired backdrop, stars and stripes atmosphere",
        "lighting": "bold American editorial light, patriotic clarity",
        "style": "American geographic body art editorial, living county map, USA cartographic body painting",
        "quality": "shot on Canon R5, dense mosaic color precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    # ═══════════════════════════════════════
    # 🔬 과학/자연현상 (5개)
    # ═══════════════════════════════════════

    "thermal_scan_body": {
        "tag": "Thermal Scan Body",
        "subject": "a fine art body painting model with thermal infrared scan painted across her entire body",
        "body": "radiating figure, living heat signature, infrared energy visible on skin",
        "outfit": "entire body painted as thermal infrared scan — fiery white-yellow hotspot at core, red-orange heat zones at torso and joints, yellow-green transitional warmth at limbs, cool blue-purple at extremities, thermal gradient rainbow spectrum, painted directly on bare skin, NO clothing, NO fabric",
        "material": "thermal imaging body paint — infrared spectrum pigments: white, yellow, red, orange, green, blue, purple gradient applied directly on bare skin",
        "environment": "dark thermal imaging studio, heat distortion atmosphere, infrared aesthetic",
        "lighting": "thermal imaging aesthetic lighting, heat glow rim light",
        "style": "thermal imaging body art editorial, living infrared scan, scientific body painting",
        "quality": "shot on Sony A7R V, perfect thermal gradient precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "xray_body": {
        "tag": "X-Ray Body",
        "subject": "a fine art body painting model with X-ray skeletal and anatomy scan painted across her entire body",
        "body": "translucent figure, living radiograph, skeleton visible through painted skin",
        "outfit": "entire body painted as X-ray scan — dark grey-black base, luminous white skeleton bones painted on skin surface (ribcage at torso, spine at back, femur at thigh, skull at face), joint structures at knees and elbows, painted directly on bare skin, NO clothing, NO fabric",
        "material": "X-ray radiograph body paint — black base, luminous white bone pigments, medical imaging palette applied directly on bare skin",
        "environment": "clinical radiology backdrop, light box illumination, medical X-ray atmosphere",
        "lighting": "X-ray light box backlight, clinical medical glow",
        "style": "medical imaging body art editorial, living radiograph, anatomical X-ray body painting",
        "quality": "shot on Hasselblad, medical precision detail, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "circuit_board_body": {
        "tag": "Circuit Board Body",
        "subject": "a fine art body painting model with electronic circuit board PCB pattern painted across her entire body",
        "body": "cybernetic figure, living motherboard, circuit pathways tracing skin",
        "outfit": "entire body painted as circuit board — dark green PCB base, gold and silver trace lines running across skin like veins, solder point dots at joints, microchip rectangles at shoulder blades, capacitor cylinders at arms, circuit pathway network, painted directly on bare skin, NO clothing, NO fabric",
        "material": "PCB circuit body paint — dark green base, gold trace, silver solder pigments applied directly on bare skin",
        "environment": "dark tech lab backdrop, blue LED ambient glow, circuit board magnification aesthetic",
        "lighting": "cool blue LED tech lighting, circuit glow",
        "style": "cyberpunk circuit body art editorial, living motherboard, electronic body painting",
        "quality": "shot on Nikon Z9, precise circuit trace detail, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "galaxy_nebula_body": {
        "tag": "Galaxy Nebula Body",
        "subject": "a fine art body painting model with galaxy and nebula cosmic cloud painted across her entire body",
        "body": "cosmic figure, living nebula, star-forming clouds across skin",
        "outfit": "entire body painted as galaxy and nebula — swirling Milky Way spiral at torso, nebula color clouds in vivid purple, electric blue, rose pink, golden star clusters scattered throughout, cosmic dust lanes, painted directly on bare skin, NO clothing, NO fabric",
        "material": "nebula galaxy body paint — cosmic color spectrum: deep purple, electric blue, rose, gold, black pigments applied directly on bare skin",
        "environment": "deep space backdrop, observatory darkness, cosmic atmosphere",
        "lighting": "nebula glow, cosmic light, starfield ambient",
        "style": "astrophotography body art editorial, living galaxy, cosmic nebula body painting",
        "quality": "shot on Sony A1, nebula color depth precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "crystal_geode_body": {
        "tag": "Crystal Geode Body",
        "subject": "a fine art body painting model with crystal geode cross-section painted across her entire body",
        "body": "crystalline figure, living geode, mineral formations across skin",
        "outfit": "entire body painted as geode crystal cross-section — outer dark rock crust at edges, amethyst purple crystal clusters at core, quartz white shards at ribs, citrine yellow formations at limbs, agate banding rings across torso, painted directly on bare skin, NO clothing, NO fabric",
        "material": "geode crystal body paint — amethyst purple, quartz white, citrine yellow, agate banding pigments applied directly on bare skin",
        "environment": "geological museum backdrop, mineral specimen display, crystal grotto atmosphere",
        "lighting": "crystal refraction light, gem sparkle illumination",
        "style": "geological body art editorial, living geode, crystal mineral body painting",
        "quality": "shot on Canon R5, crystal formation precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    # ═══════════════════════════════════════
    # 🏛️ 문명/문자 (6개)
    # ═══════════════════════════════════════

    "hieroglyph_body": {
        "tag": "Hieroglyph Body",
        "subject": "a fine art body painting model with ancient Egyptian hieroglyph inscriptions painted across her entire body",
        "body": "pharaonic figure, living papyrus, sacred scripts across skin",
        "outfit": "entire body painted with dense Egyptian hieroglyph inscriptions — cartouche panels, Ankh symbols, Eye of Horus, falcon gods, scarab beetles, lotus flowers, all rendered in black ink on golden skin tone, columns of sacred text, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Egyptian hieroglyph body paint — black kohl ink, gold leaf pigments, sacred papyrus palette applied directly on bare skin",
        "environment": "ancient Egyptian temple backdrop, hieroglyph walls, torchlight atmosphere",
        "lighting": "ancient torch and sunbeam light, Egyptian golden glow",
        "style": "Egyptology body art editorial, living papyrus scroll, hieroglyph body painting",
        "quality": "shot on Leica M11, dense inscription detail, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "aztec_calendar_body": {
        "tag": "Aztec Calendar Body",
        "subject": "a fine art body painting model with Aztec sun calendar stone painted across her entire body",
        "body": "powerful figure, living sun stone, Aztec cosmos across skin",
        "outfit": "entire body painted with Aztec calendar patterns — sun stone concentric rings at torso, Tonatiuh sun face at chest, twenty day signs radiating outward, serpent borders, warrior eagle motifs at shoulders, densely packed geometric symbols, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Aztec body paint — terracotta, gold, turquoise, obsidian black pigments applied directly on bare skin",
        "environment": "Mesoamerican temple backdrop, jungle clearing, sun-drenched ancient stone",
        "lighting": "dramatic equinox sunlight, Aztec solar radiance",
        "style": "Mesoamerican body art editorial, living sun calendar, Aztec body painting",
        "quality": "shot on Canon R3, dense geometric symbol precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "celtic_knot_body": {
        "tag": "Celtic Knot Body",
        "subject": "a fine art body painting model with intricate Celtic knot interlace patterns painted across her entire body",
        "body": "ancient figure, living Celtic manuscript, endless knot across skin",
        "outfit": "entire body painted with Celtic knotwork — endless interlace patterns covering every surface, trinity knot at chest, serpent interlace at arms, knotwork border bands, illuminated manuscript style green and gold, densely woven, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Celtic knotwork body paint — forest green, gold, black, crimson manuscript pigments applied directly on bare skin",
        "environment": "ancient Celtic stone circle backdrop, misty highland atmosphere",
        "lighting": "Celtic twilight, misty highland glow, golden hour",
        "style": "Celtic manuscript body art editorial, living Book of Kells, knotwork body painting",
        "quality": "shot on Hasselblad, intricate interlace precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "arabic_calligraphy_body": {
        "tag": "Arabic Calligraphy Body",
        "subject": "a fine art body painting model with flowing Arabic calligraphy script painted across her entire body",
        "body": "elegant figure, living manuscript, flowing Arabic script across skin",
        "outfit": "entire body painted with Arabic calligraphy — flowing Thuluth script covering every surface, Bismillah at chest, poetry verses flowing down arms and legs, geometric arabesque borders, gold ink on dark skin, densely written, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Arabic calligraphy body paint — black and gold ink pigments, manuscript illumination palette applied directly on bare skin",
        "environment": "Islamic library backdrop, arabesques and geometric patterns, warm amber light",
        "lighting": "warm amber manuscript light, golden calligraphy glow",
        "style": "Islamic calligraphy body art editorial, living manuscript, Arabic script body painting",
        "quality": "shot on Sony A7R V, flowing script precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "islamic_geometric_body": {
        "tag": "Islamic Geometric Body",
        "subject": "a fine art body painting model with intricate Islamic geometric star pattern painted across her entire body",
        "body": "mathematical figure, living geometric art, infinite pattern across skin",
        "outfit": "entire body painted with Islamic geometric patterns — dense star polygon tessellations, eight-pointed star at chest, hexagonal grid across torso, interlocking geometric network covering every surface, turquoise and gold on white, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Islamic geometric body paint — turquoise, lapis lazuli blue, gold, white pigments applied directly on bare skin",
        "environment": "Alhambra palace backdrop, geometric tilework, blue dome atmosphere",
        "lighting": "Andalusian golden light, mosaic refraction glow",
        "style": "Islamic geometric art body painting editorial, living zellige tilework, geometric body art",
        "quality": "shot on Phase One, tessellation precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "greek_mosaic_body": {
        "tag": "Greek Mosaic Body",
        "subject": "a fine art body painting model with ancient Greek mosaic tile art painted across her entire body",
        "body": "classical figure, living mosaic, tesserae across skin",
        "outfit": "entire body painted as Greek mosaic — terracotta, blue, white, black, gold tesserae tiles covering entire surface, mythological scene at torso, geometric meander border bands, mosaic texture with visible grout lines, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Greek mosaic body paint — terracotta, Aegean blue, white, gold tile pigments applied directly on bare skin",
        "environment": "ancient Greek ruins backdrop, Aegean light, classical antiquity atmosphere",
        "lighting": "Mediterranean golden sun, classical antiquity glow",
        "style": "Greco-Roman mosaic body art editorial, living tesserae, Greek mosaic body painting",
        "quality": "shot on Leica Q3, tile texture precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    # ═══════════════════════════════════════
    # 🌿 식물/자연 (3개)
    # ═══════════════════════════════════════

    "autumn_leaves_body": {
        "tag": "Autumn Leaves Body",
        "subject": "a fine art body painting model with autumn fallen leaves pattern painted across her entire body",
        "body": "seasonal figure, living autumn forest, leaf cascade across skin",
        "outfit": "entire body painted with autumn leaves — densely overlapping maple, oak, ginkgo leaves in fiery orange, crimson red, golden yellow, burnt sienna covering every surface, leaf veins as body veins, painted directly on bare skin, NO clothing, NO fabric",
        "material": "autumn foliage body paint — fiery orange, crimson, gold, burnt sienna leaf pigments applied directly on bare skin",
        "environment": "autumn forest floor, fallen leaves, golden canopy backdrop",
        "lighting": "warm autumn golden hour, leaf-filtered amber light",
        "style": "autumn nature body art editorial, living fallen leaf tapestry, seasonal body painting",
        "quality": "shot on Nikon Z9, leaf detail precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "coral_reef_body": {
        "tag": "Coral Reef Body",
        "subject": "a fine art body painting model with tropical coral reef ecosystem painted across her entire body",
        "body": "marine figure, living reef, underwater ecosystem across skin",
        "outfit": "entire body painted as coral reef — branching coral formations in pink, orange, purple, white, tropical fish painted between corals, sea anemone at joints, brain coral at torso, coral polyps covering every surface, painted directly on bare skin, NO clothing, NO fabric",
        "material": "coral reef body paint — tropical pink, orange, purple, white, turquoise ocean pigments applied directly on bare skin",
        "environment": "underwater tropical reef backdrop, crystal clear blue water, tropical fish",
        "lighting": "underwater caustic light patterns, tropical reef illumination",
        "style": "marine biology body art editorial, living coral reef, underwater ecosystem body painting",
        "quality": "shot on Canon R5, coral formation precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "mushroom_forest_body": {
        "tag": "Mushroom Forest Body",
        "subject": "a fine art body painting model with enchanted mushroom forest mycelium network painted across her entire body",
        "body": "fungal figure, living mycelium, mushroom network across skin",
        "outfit": "entire body painted with mushroom forest — fly agaric red caps with white spots at torso, mycelium white network veins across skin, chanterelle orange at shoulders, bioluminescent blue ghost mushrooms at legs, spore patterns, painted directly on bare skin, NO clothing, NO fabric",
        "material": "mycological body paint — red, white, orange, bioluminescent blue, earth brown fungal pigments applied directly on bare skin",
        "environment": "enchanted forest floor, giant mushrooms, bioluminescent atmosphere",
        "lighting": "bioluminescent mushroom glow, enchanted forest ambient",
        "style": "mycological body art editorial, living mycelium network, mushroom forest body painting",
        "quality": "shot on Sony A1, spore and mycelium detail, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    # ═══════════════════════════════════════
    # 🎨 건축/패턴 (2개)
    # ═══════════════════════════════════════

    "stained_glass_body": {
        "tag": "Stained Glass Body",
        "subject": "a fine art body painting model with Gothic cathedral stained glass window painted across her entire body",
        "body": "luminous figure, living stained glass, cathedral light across skin",
        "outfit": "entire body painted as stained glass window — vivid jewel-toned panels (sapphire blue, ruby red, emerald green, topaz gold, amethyst purple) separated by black lead lines, rose window mandala at chest, gothic arch panels at torso, painted directly on bare skin, NO clothing, NO fabric",
        "material": "stained glass body paint — jewel-toned pigments: sapphire, ruby, emerald, topaz, amethyst with black lead line detail applied directly on bare skin",
        "environment": "Gothic cathedral interior, stained glass light shafts, sacred atmosphere",
        "lighting": "cathedral stained glass backlight, jewel-tone color shafts",
        "style": "Gothic cathedral body art editorial, living stained glass, sacred glass body painting",
        "quality": "shot on Hasselblad X2D, jewel tone precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "bauhaus_body": {
        "tag": "Bauhaus Body",
        "subject": "a fine art body painting model with Bauhaus geometric primary color design painted across her entire body",
        "body": "architectural figure, living Bauhaus design, geometric form across skin",
        "outfit": "entire body painted as Bauhaus design — primary color geometric blocks (red, yellow, blue), black lines dividing sections, circle at chest, triangle at torso, rectangle panels at limbs, Kandinsky-inspired geometric composition, clean modernist aesthetic, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Bauhaus body paint — primary red, yellow, blue, black geometric pigments applied directly on bare skin",
        "environment": "Weimar Bauhaus school backdrop, modernist architecture, white space",
        "lighting": "clean modernist studio light, Bauhaus clarity",
        "style": "Bauhaus design body art editorial, living geometric manifesto, modernist body painting",
        "quality": "shot on Leica M11, geometric precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    # ═══════════════════════════════════════
    # 🚩 국기 (8개)
    # ═══════════════════════════════════════

    "union_jack_body": {
        "tag": "Union Jack Body",
        "subject": "a fine art body painting model with Union Jack British flag painted across her entire body",
        "body": "regal figure, living Union Jack, British flag across skin",
        "outfit": "entire body painted as Union Jack — bold diagonal red cross of Saint Patrick, diagonal white-edged red lines of Saint Andrew, vertical horizontal blue Saint George cross, geometric precision covering every surface, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Union Jack body paint — royal blue, bright red, pure white flag pigments applied directly on bare skin",
        "environment": "London backdrop — Big Ben, red phone box, British aesthetic",
        "lighting": "British overcast with dramatic breaks, editorial fashion light",
        "style": "British fashion body art editorial, living Union Jack, patriotic body painting",
        "quality": "shot on Hasselblad, flag geometry precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "brazil_flag_body": {
        "tag": "Brazil Flag Body",
        "subject": "a fine art body painting model with Brazilian flag painted across her entire body",
        "body": "vibrant figure, living Brazilian flag, tropical energy across skin",
        "outfit": "entire body painted as Brazilian flag — vivid green base covering skin, gold diamond rhombus at torso, deep blue celestial globe at center with white band and stars, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Brazilian flag body paint — vivid green, gold, deep blue, white pigments applied directly on bare skin",
        "environment": "Rio de Janeiro backdrop, carnival atmosphere, tropical Brazil",
        "lighting": "tropical golden hour, vibrant Brazilian light",
        "style": "Brazilian carnival body art editorial, living flag, tropical patriotic body painting",
        "quality": "shot on Canon R3, vivid tropical color precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "usa_stars_stripes_body": {
        "tag": "USA Stars Stripes Body",
        "subject": "a fine art body painting model with American Stars and Stripes flag painted across her entire body",
        "body": "bold figure, living Stars and Stripes, American flag across skin",
        "outfit": "entire body painted as American flag — bold red and white horizontal stripes covering torso and legs, blue canton with white stars at shoulder, stripes flowing down limbs, stars scattered across blue field, painted directly on bare skin, NO clothing, NO fabric",
        "material": "American flag body paint — patriot red, white, navy blue star-spangled pigments applied directly on bare skin",
        "environment": "American landscape backdrop, Monument Valley or NYC skyline",
        "lighting": "dramatic American editorial light, patriotic golden hour",
        "style": "American patriotic body art editorial, living Stars and Stripes, flag body painting",
        "quality": "shot on Nikon Z9, stripe and star precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "japan_rising_sun_body": {
        "tag": "Japan Rising Sun Body",
        "subject": "a fine art body painting model with Japanese Hinomaru and rising sun rays painted across her entire body",
        "body": "serene figure, living Hinomaru, Japanese sun across skin",
        "outfit": "entire body painted as Japanese rising sun — white base with crimson red circle at chest, radiating red and gold sun rays extending across all limbs, dramatic rising sun pattern, red ray lines covering every surface, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Japanese rising sun body paint — white base, crimson red, gold ray pigments applied directly on bare skin",
        "environment": "Mount Fuji backdrop, cherry blossom, Japanese sunrise atmosphere",
        "lighting": "Japanese sunrise golden light, zen clarity",
        "style": "Japanese patriotic body art editorial, living Hinomaru, rising sun body painting",
        "quality": "shot on Sony A7R V, radial ray precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "south_africa_flag_body": {
        "tag": "South Africa Flag Body",
        "subject": "a fine art body painting model with South African rainbow nation flag painted across her entire body",
        "body": "powerful figure, living rainbow nation, South African flag across skin",
        "outfit": "entire body painted as South African flag — green Y-shaped plow from center, black triangle at left, red and blue horizontal bands with white borders, golden yellow and black, rainbow nation colors covering entire surface, painted directly on bare skin, NO clothing, NO fabric",
        "material": "South African flag body paint — green, black, gold, red, blue, white rainbow nation pigments applied directly on bare skin",
        "environment": "South African savanna backdrop, Table Mountain silhouette",
        "lighting": "African golden hour, dramatic cape light",
        "style": "South African body art editorial, living rainbow nation flag, African patriotic body painting",
        "quality": "shot on Canon R5, geometric flag precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "india_flag_body": {
        "tag": "India Flag Body",
        "subject": "a fine art body painting model with Indian tricolor flag and Ashoka Chakra painted across her entire body",
        "body": "radiant figure, living Indian tricolor, saffron wheel across skin",
        "outfit": "entire body painted as Indian flag — saffron orange at upper body, white center band across torso, India green at lower body, navy blue Ashoka Chakra wheel at center with 24 spokes, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Indian tricolor body paint — saffron, white, India green, navy blue Chakra pigments applied directly on bare skin",
        "environment": "Taj Mahal backdrop, golden Indian sunrise, Rajasthani atmosphere",
        "lighting": "golden Indian sunrise, Taj Mahal glow",
        "style": "Indian patriotic body art editorial, living tricolor, Ashoka body painting",
        "quality": "shot on Hasselblad, tricolor band and Chakra precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "mexico_flag_body": {
        "tag": "Mexico Flag Body",
        "subject": "a fine art body painting model with Mexican flag and eagle serpent emblem painted across her entire body",
        "body": "fierce figure, living Mexican flag, eagle and serpent across skin",
        "outfit": "entire body painted as Mexican flag — vivid green at left torso and arm, white center with eagle devouring serpent on cactus emblem, vivid red at right torso and arm, Aztec-inspired emblem at chest, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Mexican flag body paint — vivid green, white, vivid red, eagle emblem detail pigments applied directly on bare skin",
        "environment": "Mexico City backdrop, Aztec pyramid silhouette, agave landscape",
        "lighting": "Mexican golden hour, vibrant Latin American light",
        "style": "Mexican patriotic body art editorial, living tricolor, eagle emblem body painting",
        "quality": "shot on Leica Q3, tricolor and emblem precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    "ukraine_flag_body": {
        "tag": "Ukraine Flag Body",
        "subject": "a fine art body painting model with Ukrainian sky and wheat field flag painted across her entire body",
        "body": "resilient figure, living Ukrainian flag, sky and wheat across skin",
        "outfit": "entire body painted as Ukrainian flag — azure blue sky covering upper body from waist up, golden wheat yellow covering lower body, clean bold bicolor division at waist, painted directly on bare skin, NO clothing, NO fabric",
        "material": "Ukrainian flag body paint — azure blue, golden wheat yellow pigments applied directly on bare skin",
        "environment": "Ukrainian wheat field backdrop, open sky, sunflower field",
        "lighting": "golden wheat field light, azure sky reflected",
        "style": "Ukrainian patriotic body art editorial, living bicolor flag, sky and wheat body painting",
        "quality": "shot on Sony A1, clean bicolor precision, painted directly on bare skin not fabric, portrait 2:3 vertical",
    },

    # ═══════════════════════════════════════
    # 🏚️ 환경융합 (2개)
    # ═══════════════════════════════════════

    "urban_decay_body": {
        "tag": "Urban Decay Body",
        "subject": "a fine art trompe-l'oeil body painting model merging into a derelict crumbling wall",
        "body": "still figure, living wall, skin becomes crumbling plaster",
        "outfit": "entire body painted as crumbling wall surface — grey-blue peeling plaster, rust stain streaks, exposed brick patches, crack network lines, aged paint layers, face and feet also fully painted, entire body blends into wall behind, painted directly on bare skin, NO clothing, NO fabric",
        "material": "trompe-l'oeil wall camouflage body paint — crumbling plaster grey-blue, rust brown, peeling paint pigments applied directly on bare skin including face and feet",
        "environment": "derelict abandoned building interior, crumbling concrete walls, peeling paint, debris on floor, window light, viewed from behind",
        "lighting": "natural window light from side, abandoned building ambient, documentary realism",
        "style": "trompe-l'oeil fine art body painting editorial, urban decay camouflage, wall fusion body art",
        "quality": "shot on Leica M11, hyperrealistic camouflage precision, full body including face and feet painted, painted directly on bare skin not fabric, landscape 3:2 horizontal",
    },

    "forest_stone_body": {
        "tag": "Forest Stone Body",
        "subject": "a fine art trompe-l'oeil body painting model merging into a moss-covered ancient stone wall in forest",
        "body": "still figure, living stone, skin becomes moss and lichen",
        "outfit": "entire body painted as moss-covered stone — grey stone texture, green moss patches, white lichen, earth tone rock surface, face and feet also fully painted, entire body blends into stone wall behind, painted directly on bare skin, NO clothing, NO fabric",
        "material": "trompe-l'oeil nature camouflage body paint — grey stone, green moss, white lichen, earth tone pigments applied directly on bare skin including face and feet",
        "environment": "ancient forest, moss-covered stone wall ruins, ferns, dappled forest light, viewed from behind",
        "lighting": "dappled forest natural light, ancient stone ambient, green forest glow",
        "style": "trompe-l'oeil fine art body painting editorial, nature camouflage, stone fusion body art",
        "quality": "shot on Sony A7R V, hyperrealistic nature camouflage, full body including face and feet painted, painted directly on bare skin not fabric, landscape 3:2 horizontal",
    },
}

# ─── dashboard.py PRESET_CATEGORIES 추가 코드 안내 ────────
BODYPAINT_ADDITIONS = [
    # 지도 계열
    "world_map_body", "topographic_body", "ocean_depth_body", "thermal_map_body",
    "weather_map_body", "subway_map_body", "europe_political_body", "africa_tribes_body",
    "japan_prefecture_body", "ancient_map_body", "fantasy_map_body", "star_map_body",
    "usa_county_map_body",
    # 과학/자연현상
    "thermal_scan_body", "xray_body", "circuit_board_body", "galaxy_nebula_body",
    "crystal_geode_body",
    # 문명/문자
    "hieroglyph_body", "aztec_calendar_body", "celtic_knot_body",
    "arabic_calligraphy_body", "islamic_geometric_body", "greek_mosaic_body",
    # 식물/자연
    "autumn_leaves_body", "coral_reef_body", "mushroom_forest_body",
    # 건축/패턴
    "stained_glass_body", "bauhaus_body",
    # 환경융합
    "urban_decay_body", "forest_stone_body",
]

CIVILIZATION_ADDITIONS = [
    # 국기
    "union_jack_body", "brazil_flag_body", "usa_stars_stripes_body",
    "japan_rising_sun_body", "south_africa_flag_body", "india_flag_body",
    "mexico_flag_body", "ukraine_flag_body",
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
print(f"총 프리셋: 697 → {697 + added}개")
print(f"\n─── dashboard.py PRESET_CATEGORIES 추가 필요 ───")
print(f"\n🖌️ 바디페인팅 카테고리 끝에 추가 ({len(BODYPAINT_ADDITIONS)}개):")
for name in BODYPAINT_ADDITIONS:
    print(f'        "{name}",')
print(f"\n🏺 문명 & 신화 카테고리 끝에 추가 ({len(CIVILIZATION_ADDITIONS)}개):")
for name in CIVILIZATION_ADDITIONS:
    print(f'        "{name}",')
