"""
ArchLumeX add_presets_v02.py
LIVE 카테고리 10개 프리셋 — "실제로 짓고 살고 싶다"

실행: python add_presets_v02.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path(__file__).parent / "presets"
PRESETS_DIR.mkdir(exist_ok=True)

PRESETS = [
    {
        "name": "scandinavian_lakehouse",
        "category": "LIVE",
        "tier": "SS",
        "label": "북유럽 호수변 목조 주택",
        "description": "고요한 호수가에 자리한 북유럽 스타일 목조 주택. 새벽 안개와 수면 반사가 꿈처럼 아름답고 실제로 살고 싶은 포근함.",
        "preset_prompt": "Professional architectural photography of a stunning Scandinavian lakehouse at dawn. A beautifully crafted timber and glass house sits directly on the edge of a perfectly still Nordic lake. The house features warm cedar cladding, a wide overhanging roof, and floor-to-ceiling windows that reflect the glassy water below. Morning mist drifts low over the lake surface. Inside, warm amber light glows through the windows. A simple wooden dock extends into the mirror-still water. Pine and birch trees surround the property. The entire scene is reflected perfectly in the lake. Breathtakingly peaceful. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "country house, rural estate, large garden property",
        "arch_style": "Scandinavian architecture, simple wood and white, cozy Nordic",
        "ext_material": "wood siding, natural timber cladding, warm organic texture",
        "roof_style": "shed roof, mono-pitch single slope, modern asymmetric",
        "landscaping": "naturalistic garden, wildflowers, organic planting, lush greenery",
        "lighting": "natural daylight, bright sunlight streaming in, clear day",
        "time_of_day": "early morning soft light, fresh dawn atmosphere, quiet morning",
        "weather": "foggy misty atmosphere, mysterious soft focus",
        "mood": "cozy warm inviting mood, homey comfortable atmosphere",
        "color_grade": "cool blue color grade, crisp clean tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["북유럽", "호수", "목조", "새벽안개", "수면반사", "LIVE", "살고싶다"],
    },
    {
        "name": "japanese_engawa_autumn",
        "category": "LIVE",
        "tier": "SS",
        "label": "일본 툇마루 단풍 석양",
        "description": "처마 아래 툇마루(縁側)에서 바라보는 단풍 정원과 석양. 고요하고 따뜻한 일본 목조 주택의 계절감 극대화.",
        "preset_prompt": "Professional architectural photography of a serene Japanese wooden house with a traditional engawa veranda at golden hour in autumn. The wide timber veranda stretches along the entire facade, sheltered by deep overhanging eaves. A meticulously maintained Japanese garden beyond — maple trees blazing in crimson, amber, and gold. The low autumn sun casts warm long shadows across the worn wooden floor. Shoji paper screens glow softly from within. A single stone lantern among the fallen leaves. The garden path curves between moss-covered stones. Pure wabi-sabi perfection. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "traditional Korean hanok, timber frame, tiled roof",
        "arch_style": "Japanese modern architecture, wabi-sabi, natural materials, Zen",
        "ext_material": "wood siding, natural timber cladding, warm organic texture",
        "roof_style": "traditional Korean tile roof, curved hanok eaves, clay tiles",
        "landscaping": "Japanese zen garden, raked gravel, stone lantern, pine bonsai",
        "lighting": "golden hour warm light, late afternoon sun, amber glow",
        "time_of_day": "late afternoon warm sunlight, relaxed golden atmosphere",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "romantic soft warm mood, tender dreamy atmosphere",
        "color_grade": "warm golden color grade, cozy inviting tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["툇마루", "단풍", "석양", "일본주택", "정원", "와비사비", "LIVE"],
    },
    {
        "name": "korean_hanok_snow",
        "category": "LIVE",
        "tier": "SS",
        "label": "현대한옥 설경 야경",
        "description": "전통 기와지붕 위에 눈이 쌓인 현대한옥. 마당의 고요한 설경과 창문으로 새어나오는 따뜻한 불빛의 대비.",
        "preset_prompt": "Professional architectural photography of a stunning modern Korean hanok house in winter snow at night. The traditional curved clay tile roof is blanketed in pristine white snow, its elegant lines even more beautiful under the weight. A central stone-paved courtyard holds a single ancient pine tree dusted with snow. Warm amber light pours from the hanji paper screen windows and sliding doors, casting a golden glow on the snow. The wooden eaves and exposed timber frame are highlighted by subtle exterior lighting. Snow falls gently. The combination of 600-year-old architectural tradition with modern comfort is deeply moving. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "traditional Korean hanok, timber frame, tiled roof",
        "arch_style": "modern hanok, traditional Korean fusion, contemporary hanok design",
        "ext_material": "wood siding, natural timber cladding, warm organic texture",
        "roof_style": "traditional Korean tile roof, curved hanok eaves, clay tiles",
        "landscaping": "Japanese zen garden, raked gravel, stone lantern, pine bonsai",
        "lighting": "warm candlelight ambiance, cozy warm lighting, intimate glow",
        "time_of_day": "night time, dark sky, artificial lighting, nocturnal atmosphere",
        "weather": "snowfall, snow-covered, winter white landscape",
        "mood": "cozy warm inviting mood, homey comfortable atmosphere",
        "color_grade": "warm golden color grade, cozy inviting tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["한옥", "눈", "야경", "기와지붕", "마당", "설경", "LIVE", "살고싶다"],
    },
    {
        "name": "brick_cafe_golden",
        "category": "LIVE",
        "tier": "SS",
        "label": "노출벽돌 카페 골든아워",
        "description": "노출벽돌+아치+아이비로 뒤덮인 카페 골든아워. 따뜻한 빛과 식물이 어우러진 '이런 카페 하고 싶다' 느낌.",
        "preset_prompt": "Professional architectural photography of a charming exposed brick cafe at golden hour. The facade is warm red brick with graceful arched windows, partially covered in lush climbing ivy and wisteria in full bloom. Warm amber light floods through the large arched windows, revealing a cozy interior with wooden shelves of books and plants. Small cafe tables and chairs spill onto the cobblestone terrace outside. Hanging Edison bulb string lights begin to glow in the fading light. Terracotta flower pots overflow with lavender and geraniums. The golden hour sun paints everything in the most inviting warm light. A place you never want to leave. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "mixed-use building, ground floor commercial upper residential",
        "arch_style": "Provencal style, French countryside, stone walls, warm romantic",
        "ext_material": "red brick, warm classic masonry, traditional residential",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "English cottage garden, roses, climbing vines, romantic flowers",
        "lighting": "golden hour warm light, late afternoon sun, amber glow",
        "time_of_day": "late afternoon warm sunlight, relaxed golden atmosphere",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "cozy warm inviting mood, homey comfortable atmosphere",
        "color_grade": "warm golden color grade, cozy inviting tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["카페", "벽돌", "아이비", "골든아워", "아치", "로맨틱", "LIVE"],
    },
    {
        "name": "rammed_earth_sunset",
        "category": "LIVE",
        "tier": "SS",
        "label": "흙다짐 주택 사막 석양",
        "description": "붉은 흙다짐 벽체의 현대 주택과 사막 석양. 흙의 따뜻한 토색과 하늘의 극적인 색감이 완벽히 어우러짐.",
        "preset_prompt": "Professional architectural photography of a stunning rammed earth modern house in a desert landscape at sunset. The house features thick layered rammed earth walls in warm ochre, terracotta, and sienna tones — the compressed earth layers visible as beautiful horizontal strata. Large steel-framed windows and a flat roof create a perfect modern-primitive tension. The setting sun blazes the sky in deep orange, magenta, and purple. The warm earth walls glow in the last light. A long infinity lap pool reflects the burning sky. Desert scrub and cacti surround the property. The house looks as if it grew from the earth itself. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "country house, rural estate, large garden property",
        "arch_style": "vernacular architecture, local materials, organic natural building",
        "ext_material": "natural stone cladding, granite limestone, premium exterior",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "gravel garden, pebble landscaping, low maintenance xeriscaping",
        "lighting": "golden hour warm light, late afternoon sun, amber glow",
        "time_of_day": "dusk twilight, dramatic sunset colors, sky ablaze",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "dramatic intense mood, powerful bold atmosphere",
        "color_grade": "cinematic teal and orange, film look color grade",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["흙다짐", "사막", "석양", "어스톤", "현대주택", "LIVE", "이국적"],
    },
    {
        "name": "stone_cottage_spring",
        "category": "LIVE",
        "tier": "SS",
        "label": "영국 돌집 봄 꽃정원",
        "description": "코츠월즈 스타일 꿀빛 석회암 돌집과 활짝 핀 봄 꽃정원. 동화 속 집처럼 아늑하고 로맨틱한 최고의 LIVE 장면.",
        "preset_prompt": "Professional architectural photography of an idyllic English Cotswolds stone cottage in full spring bloom. The honey-golden limestone cottage glows warmly in soft afternoon light. The cottage garden is an explosion of colour — roses, hollyhocks, foxgloves, lavender, and wisteria cascade over the stone walls and wooden gate. A flagstone path winds through the blooms to the arched wooden front door. Window boxes overflow with flowers. The thatched roof is thick and perfectly maintained. A white picket fence borders the overflowing garden. Bees and butterflies hover over the blooms. The most romantic and inviting home imaginable. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "country house, rural estate, large garden property",
        "arch_style": "cottage style, English countryside, thatched roof, cozy garden",
        "ext_material": "natural stone cladding, granite limestone, premium exterior",
        "roof_style": "thatched roof, traditional straw roofing, cottage rustic",
        "landscaping": "English cottage garden, roses, climbing vines, romantic flowers",
        "lighting": "natural daylight, bright sunlight streaming in, clear day",
        "time_of_day": "late afternoon warm sunlight, relaxed golden atmosphere",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "romantic soft warm mood, tender dreamy atmosphere",
        "color_grade": "natural color grading, true-to-life realistic colors",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["돌집", "꽃정원", "봄", "코츠월즈", "영국", "로맨틱", "LIVE", "살고싶다"],
    },
    {
        "name": "modern_courtyard_house",
        "category": "LIVE",
        "tier": "SS",
        "label": "모던 중정 수공간 주택",
        "description": "도심형 현대 주택의 중정에 얕은 수공간과 조각 나무 한 그루. 콘크리트+목재+물의 완벽한 균형.",
        "preset_prompt": "Professional architectural photography of a sophisticated modern courtyard house in an urban setting. The house wraps around a central open-air courtyard featuring a shallow reflecting pool with a single sculptural Japanese maple tree growing from its center. Raw concrete walls meet warm teak wood screens and panels. The interior rooms open fully to the courtyard through floor-to-ceiling sliding glass. Evening light makes the water surface shimmer and reflects the surrounding architecture. Carefully curated plants soften the concrete. The courtyard is the heart of the home — a private sky-lit oasis in the city. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "single-family detached house, residential home",
        "arch_style": "modern minimalist architecture, clean lines, white walls, flat roof",
        "ext_material": "exposed concrete, raw textured finish, brutalist modern",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "water feature, pond pool fountain, reflective water element",
        "lighting": "spot accent lighting, highlighted focal points, dramatic spots",
        "time_of_day": "dusk twilight, dramatic sunset colors, sky ablaze",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "minimal clean restrained mood, quiet understated atmosphere",
        "color_grade": "natural color grading, true-to-life realistic colors",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["중정", "수공간", "모던", "콘크리트", "목재", "도시주택", "LIVE"],
    },
    {
        "name": "forest_cabin_morning",
        "category": "LIVE",
        "tier": "SS",
        "label": "침엽수림 목조 오두막 아침",
        "description": "침엽수림 속 아늑한 목조 오두막. 아침 햇살이 숲을 관통하고 커피 한 잔이 생각나는 전원생활의 이상향.",
        "preset_prompt": "Professional architectural photography of a perfect woodland cabin nestled among tall pine and fir trees on a crisp autumn morning. The cabin is beautifully crafted from dark stained timber with a metal roof dusted with pine needles. A wide covered porch with a rocking chair and a steaming coffee mug faces the forest. Morning sunlight filters through the tall trees in golden shafts, illuminating the forest floor of ferns and moss. Smoke curls from the stone chimney. A small vegetable garden and wood pile complete the scene. Through the large cabin windows, warm bookshelves and a fireplace are visible. The ultimate retreat. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "log cabin, wooden cabin, rustic forest dwelling",
        "arch_style": "vernacular architecture, local materials, organic natural building",
        "ext_material": "wood siding, natural timber cladding, warm organic texture",
        "roof_style": "gabled roof, classic triangular pitched roof",
        "landscaping": "naturalistic garden, wildflowers, organic planting, lush greenery",
        "lighting": "natural daylight, bright sunlight streaming in, clear day",
        "time_of_day": "early morning soft light, fresh dawn atmosphere, quiet morning",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "cozy warm inviting mood, homey comfortable atmosphere",
        "color_grade": "warm golden color grade, cozy inviting tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["오두막", "침엽수림", "아침", "전원생활", "커피", "포근함", "LIVE", "살고싶다"],
    },
    {
        "name": "rooftop_garden_dusk",
        "category": "LIVE",
        "tier": "SS",
        "label": "옥상정원 황혼 도시뷰",
        "description": "도심 고층 건물 옥상의 럭셔리 정원. 황혼에 물드는 도시 스카이라인과 초록 정원의 완벽한 대비.",
        "preset_prompt": "Professional architectural photography of a breathtaking rooftop garden terrace on a luxury urban building at dusk. The expansive rooftop is transformed into a lush garden oasis — mature olive trees, lavender hedges, ornamental grasses, and a long lap pool run parallel to the city skyline. Comfortable outdoor sofas and dining tables are set among the plantings. The city skyscrapers glow in the blue-hour light behind the green garden foreground. String lights begin to illuminate the space. The contrast between the organic garden and the geometric city creates a magical tension. Urban living at its absolute finest. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "small multi-family villa, urban residential building",
        "arch_style": "contemporary architecture, sleek modern design, sophisticated",
        "ext_material": "glass curtain wall, full glass facade, reflective modern exterior",
        "roof_style": "green roof, rooftop garden, living grass roof, eco sustainable",
        "landscaping": "rooftop terrace, deck garden, urban rooftop outdoor space",
        "lighting": "blue hour twilight, mystical cool blue atmospheric glow",
        "time_of_day": "dusk twilight, dramatic sunset colors, sky ablaze",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "luxurious elegant mood, premium sophisticated atmosphere",
        "color_grade": "cool blue color grade, crisp clean tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["옥상정원", "황혼", "도시뷰", "블루아워", "럭셔리", "도심", "LIVE"],
    },
    {
        "name": "bamboo_house_rain",
        "category": "LIVE",
        "tier": "SS",
        "label": "대나무숲 현대 주택 빗속",
        "description": "빽빽한 대나무숲 속 현대 주택. 빗소리와 대나무 흔들림, 따뜻한 실내빛의 동양적 고요함.",
        "preset_prompt": "Professional architectural photography of a serene modern house enveloped by a dense bamboo grove in the rain. The house features clean horizontal lines, dark steel and wood construction, with large floor-to-ceiling windows that frame the surrounding bamboo forest. Rain falls steadily, causing the tall bamboo culms to sway gently and glisten. The bamboo forest fills every window view, creating a living green wall on all sides. Warm interior light glows through the glass, reflecting on the wet stone terrace. A shallow water basin collects raindrops, creating circular ripples. The sound of rain on bamboo is almost audible in the image. Profound tranquility. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "single-family detached house, residential home",
        "arch_style": "Japanese modern architecture, wabi-sabi, natural materials, Zen",
        "ext_material": "wood siding, natural timber cladding, warm organic texture",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "bamboo screen, privacy bamboo grove, Asian garden element",
        "lighting": "warm candlelight ambiance, cozy warm lighting, intimate glow",
        "time_of_day": "late afternoon warm sunlight, relaxed golden atmosphere",
        "weather": "rainy weather, wet ground reflections, rain atmosphere",
        "mood": "biophilic natural mood, organic earthy serene atmosphere",
        "color_grade": "dark moody grade, deep shadows, dramatic contrast",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["대나무", "비", "고요함", "현대주택", "동양적", "선", "LIVE", "살고싶다"],
    },
]


def main():
    created = 0
    skipped = 0

    for preset in PRESETS:
        path = PRESETS_DIR / f"{preset['name']}.json"
        if path.exists():
            print(f"  SKIP  {preset['name']}.json (이미 존재)")
            skipped += 1
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(preset, f, ensure_ascii=False, indent=2)
            print(f"  OK    {preset['name']}.json")
            created += 1

    print(f"\n완료: {created}개 생성, {skipped}개 건너뜀")
    print(f"총 프리셋: {len(list(PRESETS_DIR.glob('*.json')))}개")


if __name__ == "__main__":
    main()
