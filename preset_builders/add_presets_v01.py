"""
ArchLumeX add_presets_v01.py
WOW SS tier 10개 프리셋 자동 생성 스크립트

실행: python add_presets_v01.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path(__file__).parent / "presets"
PRESETS_DIR.mkdir(exist_ok=True)

PRESETS = [
    {
        "name": "forest_glass_house_night",
        "category": "WOW",
        "tier": "SS",
        "label": "숲속 유리집 야경",
        "description": "울창한 숲 속 유리집, 어둠 속에 빛나는 따뜻한 실내. 스크롤 멈추는 대표 WOW 장면.",
        "preset_prompt": "Professional architectural photography of a stunning glass house nestled deep in a dense forest at night. Floor-to-ceiling glass walls reveal a warmly lit interior glowing amber against the dark forest. Ancient tall trees surround the house, their bark and leaves softly illuminated by interior light spilling outward. Reflections of the interior shimmer on the glass. A stone path leads to the entrance. Mist drifts between the trees. The contrast between warm golden interior light and the cool blue-black forest creates a breathtaking atmosphere. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "single-family detached house, residential home",
        "arch_style": "high-tech architecture, glass and steel, futuristic precision",
        "ext_material": "glass curtain wall, full glass facade, reflective modern exterior",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "naturalistic garden, wildflowers, organic planting, lush greenery",
        "lighting": "night lighting, artificial lights glowing, evening atmosphere",
        "time_of_day": "night time, dark sky, artificial lighting, nocturnal atmosphere",
        "weather": "foggy misty atmosphere, mysterious soft focus",
        "mood": "dramatic intense mood, powerful bold atmosphere",
        "color_grade": "warm golden color grade, cozy inviting tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["야경", "유리집", "숲속", "안개", "골든라이트", "WOW"],
    },
    {
        "name": "arctic_glass_igloo",
        "category": "WOW",
        "tier": "SS",
        "label": "오로라 유리 이글루",
        "description": "북극 오로라 아래 유리 이글루 호텔. 오로라 반사 + 따뜻한 실내빛 대비.",
        "preset_prompt": "Professional architectural photography of a luxury glass igloo hotel under the Northern Lights in the Arctic. A perfectly domed transparent glass structure sits on pristine white snow. The aurora borealis blazes across the sky in vivid green, violet, and teal, reflecting off the curved glass surface. Inside, warm amber light glows invitingly — a bed with fur blankets visible through the glass. The snow around the igloo sparkles under the aurora. Absolute silence and magic. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography, National Geographic quality.",
        "building_type": "pension guesthouse, vacation rental, countryside inn",
        "arch_style": "high-tech architecture, glass and steel, futuristic precision",
        "ext_material": "glass curtain wall, full glass facade, reflective modern exterior",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "",
        "lighting": "night lighting, artificial lights glowing, evening atmosphere",
        "time_of_day": "night time, dark sky, artificial lighting, nocturnal atmosphere",
        "weather": "snowfall, snow-covered, winter white landscape",
        "mood": "romantic soft warm mood, tender dreamy atmosphere",
        "color_grade": "cool blue color grade, crisp clean tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["오로라", "이글루", "북극", "유리돔", "눈", "WOW", "판타지경계"],
    },
    {
        "name": "cliffside_infinity_pool",
        "category": "WOW",
        "tier": "SS",
        "label": "지중해 절벽 인피니티풀",
        "description": "지중해 절벽 위 빌라의 인피니티풀. 수평선과 풀이 하나로 이어지는 극적 장면.",
        "preset_prompt": "Professional architectural photography of a stunning cliffside villa with an infinity pool overlooking the Mediterranean Sea. The infinity pool's edge perfectly merges with the turquoise sea horizon far below. White limestone terraces cascade down the dramatic cliff face. Bougainvillea in vivid magenta spills over stone walls. Sleek sun loungers and a minimalist pavilion frame the pool. The late afternoon golden sun casts long warm shadows. The sea below is an impossible shade of blue. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "country house, rural estate, large garden property",
        "arch_style": "Mediterranean style, white walls, blue accents, arched windows",
        "ext_material": "natural stone cladding, granite limestone, premium exterior",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "Mediterranean garden, olive trees, lavender, terracotta pots",
        "lighting": "golden hour warm light, late afternoon sun, amber glow",
        "time_of_day": "late afternoon warm sunlight, relaxed golden atmosphere",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "luxurious elegant mood, premium sophisticated atmosphere",
        "color_grade": "warm golden color grade, cozy inviting tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["인피니티풀", "절벽", "지중해", "골든아워", "빌라", "WOW"],
    },
    {
        "name": "hygge_snowcabin_night",
        "category": "WOW",
        "tier": "SS",
        "label": "눈밭 오두막 야경",
        "description": "폭설 속 통나무 오두막. 굴뚝 연기 + 창문 따뜻한 빛 + 눈 쌓인 지붕. 포근함의 극치.",
        "preset_prompt": "Professional architectural photography of a cozy log cabin in a winter wonderland at night. Heavy snow blankets the roof, the ground, and the surrounding pine trees. Warm golden light pours from every window, casting soft amber pools on the snow. Smoke curls lazily from the stone chimney. A wreath on the wooden door, firewood stacked neatly on the porch. Snowflakes fall gently. The contrast between the freezing blue-white exterior and the impossibly warm glowing interior is heart-stopping. A single lantern lights the snow path to the door. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "log cabin, wooden cabin, rustic forest dwelling",
        "arch_style": "Scandinavian architecture, simple wood and white, cozy Nordic",
        "ext_material": "wood siding, natural timber cladding, warm organic texture",
        "roof_style": "gabled roof, classic triangular pitched roof",
        "landscaping": "naturalistic garden, wildflowers, organic planting, lush greenery",
        "lighting": "warm candlelight ambiance, cozy warm lighting, intimate glow",
        "time_of_day": "night time, dark sky, artificial lighting, nocturnal atmosphere",
        "weather": "snowfall, snow-covered, winter white landscape",
        "mood": "cozy warm inviting mood, homey comfortable atmosphere",
        "color_grade": "warm golden color grade, cozy inviting tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["오두막", "눈", "야경", "굴뚝", "포근함", "hygge", "WOW"],
    },
    {
        "name": "brutalist_light_cathedral",
        "category": "WOW",
        "tier": "SS",
        "label": "빛의 콘크리트 성당",
        "description": "거대한 노출 콘크리트 성당. 천장 틈새로 쏟아지는 극적인 빛기둥. 안도 타다오 스타일.",
        "preset_prompt": "Professional architectural interior photography of a breathtaking brutalist cathedral carved from raw exposed concrete. Monolithic concrete walls soar upward. Narrow slits in the ceiling and walls channel brilliant shafts of sunlight that pierce the dim interior, creating dramatic beams of light through dusty air. The geometry is severe, powerful, and deeply spiritual. A long empty nave stretches toward a single cross of light at the far end. Silence made visible in stone and light. Inspired by Tadao Ando and Le Corbusier. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "single-family detached house, residential home",
        "arch_style": "brutalist architecture, raw concrete mass, bold geometric forms",
        "ext_material": "exposed concrete, raw textured finish, brutalist modern",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "",
        "lighting": "dramatic chiaroscuro lighting, strong shadows and highlights",
        "time_of_day": "midday harsh sunlight, strong direct light, high contrast",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "dramatic intense mood, powerful bold atmosphere",
        "color_grade": "dark moody grade, deep shadows, dramatic contrast",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["콘크리트", "성당", "빛기둥", "브루탈리즘", "극적", "안도타다오", "WOW"],
    },
    {
        "name": "underwater_corridor",
        "category": "WOW",
        "tier": "SS",
        "label": "수중 유리 복도",
        "description": "산호초 한가운데를 관통하는 유리 터널 복도. 물고기와 빛 산란이 비현실적 아름다움을 연출.",
        "preset_prompt": "Professional architectural photography of a stunning underwater glass tunnel corridor in a tropical ocean. Crystal-clear turquoise water surrounds the curved glass walkway on all sides. Vibrant coral reefs in orange, purple, and red grow against the glass exterior. Schools of tropical fish — parrotfish, angelfish, mantas — glide past. Dappled sunlight filters down from the surface above, creating shimmering caustic light patterns on the white floor. The tunnel stretches into a luminous blue infinity. Otherworldly beauty made real. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "small multi-family villa, urban residential building",
        "arch_style": "high-tech architecture, glass and steel, futuristic precision",
        "ext_material": "glass curtain wall, full glass facade, reflective modern exterior",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "water feature, pond pool fountain, reflective water element",
        "lighting": "natural daylight, bright sunlight streaming in, clear day",
        "time_of_day": "midday harsh sunlight, strong direct light, high contrast",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "biophilic natural mood, organic earthy serene atmosphere",
        "color_grade": "cool blue color grade, crisp clean tones",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["수중", "유리터널", "산호초", "열대어", "빛산란", "WOW", "판타지경계"],
    },
    {
        "name": "vertical_forest_tower",
        "category": "WOW",
        "tier": "SS",
        "label": "수직 숲 타워",
        "description": "온 몸이 나무와 식물로 뒤덮인 초고층 타워. 도심 한가운데 자연이 폭발하는 장면.",
        "preset_prompt": "Professional architectural photography of a spectacular vertical forest skyscraper in a dense urban cityscape. Every balcony, terrace, and facade of the soaring tower is covered in thousands of real trees, shrubs, and plants — a living vertical forest erupting from concrete and glass. Oak, birch, and pine trees grow from each floor, their branches reaching outward. Lush greenery cascades down the sides. The tower stands in dramatic contrast against a blue sky, surrounded by conventional glass office towers. Birds circle the canopy levels. A city-within-a-nature miracle. Inspired by Bosco Verticale Milan. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "small multi-family villa, urban residential building",
        "arch_style": "contemporary architecture, sleek modern design, sophisticated",
        "ext_material": "glass curtain wall, full glass facade, reflective modern exterior",
        "roof_style": "green roof, rooftop garden, living grass roof, eco sustainable",
        "landscaping": "naturalistic garden, wildflowers, organic planting, lush greenery",
        "lighting": "natural daylight, bright sunlight streaming in, clear day",
        "time_of_day": "late afternoon warm sunlight, relaxed golden atmosphere",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "biophilic natural mood, organic earthy serene atmosphere",
        "color_grade": "natural color grading, true-to-life realistic colors",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["수직숲", "타워", "바이오필릭", "도심", "나무", "보스코베르티칼레", "WOW"],
    },
    {
        "name": "desert_monolith_resort",
        "category": "WOW",
        "tier": "SS",
        "label": "사막 모노리스 리조트",
        "description": "사막 한가운데 솟아오른 검은 모노리스형 리조트. 별하늘 + 붉은 모래의 압도적 스케일.",
        "preset_prompt": "Professional architectural photography of a monumental black monolith resort rising from an endless red desert under a breathtaking Milky Way sky. A single massive obsidian-black rectangular tower stands alone in the vast Saharan landscape, dramatically lit from within — thin horizontal windows glow warm amber against the dark stone. The red sand dunes stretch to the horizon in every direction. Above, the Milky Way arcs across the night sky in brilliant detail. A lone camel silhouette in the far distance. The scale is humbling, the silence deafening. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "pension guesthouse, vacation rental, countryside inn",
        "arch_style": "brutalist architecture, raw concrete mass, bold geometric forms",
        "ext_material": "corten steel, weathering steel, rust-brown patina, industrial chic",
        "roof_style": "flat roof, modern minimalist roofline",
        "landscaping": "gravel garden, pebble landscaping, low maintenance xeriscaping",
        "lighting": "night lighting, artificial lights glowing, evening atmosphere",
        "time_of_day": "night time, dark sky, artificial lighting, nocturnal atmosphere",
        "weather": "clear blue sky, bright sunny weather, sharp shadows",
        "mood": "dramatic intense mood, powerful bold atmosphere",
        "color_grade": "dark moody grade, deep shadows, dramatic contrast",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["사막", "모노리스", "별하늘", "은하수", "리조트", "압도적", "WOW"],
    },
    {
        "name": "courtyard_rain_lantern",
        "category": "WOW",
        "tier": "SS",
        "label": "중정 빗속 등불",
        "description": "중정 안마당에 빗소리, 나무 한 그루, 등불 하나. 고요하고 감성적인 동양적 아름다움.",
        "preset_prompt": "Professional architectural photography of a serene Japanese-Korean courtyard house in the rain. A single ancient gnarled tree stands at the center of the stone-paved inner courtyard. Rain falls softly, creating ripples in a shallow reflecting pool at the base of the tree. A single traditional stone lantern glows with warm amber light, its reflection dancing in the water. The surrounding wooden and concrete architecture frames the courtyard with deep overhanging eaves, sheltering the walkways. Rain streaks catch the lantern light. The sound of rain on leaves is almost audible. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "traditional Korean hanok, timber frame, tiled roof",
        "arch_style": "Japanese modern architecture, wabi-sabi, natural materials, Zen",
        "ext_material": "wood siding, natural timber cladding, warm organic texture",
        "roof_style": "traditional Korean tile roof, curved hanok eaves, clay tiles",
        "landscaping": "Japanese zen garden, raked gravel, stone lantern, pine bonsai",
        "lighting": "warm candlelight ambiance, cozy warm lighting, intimate glow",
        "time_of_day": "night time, dark sky, artificial lighting, nocturnal atmosphere",
        "weather": "rainy weather, wet ground reflections, rain atmosphere",
        "mood": "romantic soft warm mood, tender dreamy atmosphere",
        "color_grade": "dark moody grade, deep shadows, dramatic contrast",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["중정", "비", "등불", "한옥", "일본정원", "고요함", "WOW"],
    },
    {
        "name": "treehouse_canopy_mist",
        "category": "WOW",
        "tier": "SS",
        "label": "숲 캐노피 트리하우스",
        "description": "고목 위에 지어진 트리하우스. 새벽 안개가 캐노피를 감싸는 신비롭고 포근한 장면.",
        "preset_prompt": "Professional architectural photography of a magical treehouse perched high in the forest canopy at dawn. The treehouse is built seamlessly into and around several massive ancient oak trees, with wooden platforms, rope bridges, and a glass-walled sleeping pod. Morning mist drifts through the canopy, softening everything in a dreamy blue-white haze. Dappled early dawn light filters through the leaves, catching the mist in golden shafts. The treehouse seems to float above the world. Below, the forest floor is invisible in the mist. A perfect escape. Shot on Hasselblad medium format, ultra-sharp, 8K resolution, award-winning architectural photography.",
        "building_type": "log cabin, wooden cabin, rustic forest dwelling",
        "arch_style": "vernacular architecture, local materials, organic natural building",
        "ext_material": "wood siding, natural timber cladding, warm organic texture",
        "roof_style": "shed roof, mono-pitch single slope, modern asymmetric",
        "landscaping": "naturalistic garden, wildflowers, organic planting, lush greenery",
        "lighting": "natural daylight, bright sunlight streaming in, clear day",
        "time_of_day": "early morning soft light, fresh dawn atmosphere, quiet morning",
        "weather": "foggy misty atmosphere, mysterious soft focus",
        "mood": "romantic soft warm mood, tender dreamy atmosphere",
        "color_grade": "high key bright airy, overexposed clean white tone",
        "render_style": "photorealistic architectural photography, completed building photo",
        "tags": ["트리하우스", "안개", "새벽", "캐노피", "신비로운", "포근함", "WOW"],
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
