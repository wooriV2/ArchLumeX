"""
ArchLumeX core/data.py
건축/인테리어 AI 이미지 프롬프트 엔진 — 데이터 딕셔너리
대상: 집주인/일반인 (리모델링 참고용)
"""

# ─── 공통 ───────────────────────────────────────────────

ASPECT_RATIOS = {
    "세로 2:3 — 외관 기본 ★":        "portrait 2:3 vertical",
    "정방형 1:1 — 인스타 피드":        "square 1:1",
    "가로 16:9 — 와이드 전경":         "landscape 16:9 cinematic wide",
    "가로 4:3 — 화보/카탈로그":        "landscape 4:3 editorial wide",
    "가로 3:2 — 클래식 가로":          "landscape 3:2 horizontal",
    "세로 9:16 — 모바일/릴스":         "portrait 9:16 vertical, mobile optimized",
}

# ─── 실외 (Exterior) ────────────────────────────────────

BUILDING_TYPES = {
    "단독주택 — 1~2층 가정집":             "single-family detached house, residential home",
    "타운하우스 — 연립 다세대":             "townhouse, attached row house, urban residential",
    "빌라/다가구 — 소형 공동주택":          "small multi-family villa, urban residential building",
    "전원주택 — 시골/교외 넓은 대지":       "country house, rural estate, large garden property",
    "펜션/게스트하우스 — 숙박용":           "pension guesthouse, vacation rental, countryside inn",
    "상가주택 — 1층 상업+위층 주거":        "mixed-use building, ground floor commercial upper residential",
    "협소주택 — 좁은 대지 효율 설계":       "narrow lot house, compact urban dwelling, efficient design",
    "컨테이너하우스 — 모듈형 컨테이너":     "container house, modular shipping container architecture",
    "한옥 — 전통 한국 목조 가옥":           "traditional Korean hanok, timber frame, tiled roof",
    "캐빈/로그하우스 — 통나무집":           "log cabin, wooden cabin, rustic forest dwelling",
}

ARCHITECTURAL_STYLES = {
    "모던 미니멀 — 깔끔한 직선, 흰 벽":          "modern minimalist architecture, clean lines, white walls, flat roof",
    "컨템포러리 — 현대적 세련미":                 "contemporary architecture, sleek modern design, sophisticated",
    "스칸디나비안 — 북유럽 심플 우드":            "Scandinavian architecture, simple wood and white, cozy Nordic",
    "인더스트리얼 — 노출 콘크리트, 철골":         "industrial architecture, exposed concrete, steel frame, raw materials",
    "재패니즈 모던 — 일본 미니멀 자연소재":       "Japanese modern architecture, wabi-sabi, natural materials, Zen",
    "한옥 모던 — 전통+현대 퓨전":                 "modern hanok, traditional Korean fusion, contemporary hanok design",
    "프로방스 — 남프랑스 시골 로맨틱":            "Provencal style, French countryside, stone walls, warm romantic",
    "지중해 — 흰 벽, 파란 창틀, 아치":            "Mediterranean style, white walls, blue accents, arched windows",
    "바우하우스 — 기능주의 모던 클래식":           "Bauhaus architecture, functionalist modernism, geometric forms",
    "아르데코 — 1920s 화려한 기하학":             "Art Deco architecture, geometric ornament, glamorous 1920s",
    "미드센추리 모던 — 1950s 유기적 곡선":        "mid-century modern, organic curves, large windows, 1950s American",
    "바르나큘러 — 지역 전통 재료 자연스러운":     "vernacular architecture, local materials, organic natural building",
    "하이테크 — 유리 철골 미래지향":              "high-tech architecture, glass and steel, futuristic precision",
    "브루탈리즘 — 거친 노출 콘크리트 매스감":     "brutalist architecture, raw concrete mass, bold geometric forms",
    "코티지 — 영국식 아늑한 전원 소주택":         "cottage style, English countryside, thatched roof, cozy garden",
}

EXTERIOR_MATERIALS = {
    "화이트 스터코 — 밝고 깔끔한 미장":        "white stucco finish, smooth plaster exterior, bright clean walls",
    "노출 콘크리트 — 거친 질감 모던":           "exposed concrete, raw textured finish, brutalist modern",
    "적벽돌 — 따뜻한 클래식 벽돌":             "red brick, warm classic masonry, traditional residential",
    "화이트 벽돌 — 모던 화이트 벽돌":           "white painted brick, modern clean masonry",
    "목재 사이딩 — 자연스러운 나무 외벽":       "wood siding, natural timber cladding, warm organic texture",
    "탄화목 — 검은 그을린 나무 (야키스기)":     "charred wood siding, yakisugi, dark burned timber, Japanese style",
    "유리 커튼월 — 전면 유리 반사":             "glass curtain wall, full glass facade, reflective modern exterior",
    "금속 패널 — 알루미늄/아연 현대적":         "metal panel cladding, aluminum zinc facade, contemporary industrial",
    "코르텐 스틸 — 녹슨 갈색 내후성 강판":      "corten steel, weathering steel, rust-brown patina, industrial chic",
    "천연석 — 화강암/석회암 고급스러운":        "natural stone cladding, granite limestone, premium exterior",
    "테라코타 타일 — 따뜻한 지중해 느낌":       "terracotta tile facade, warm Mediterranean clay finish",
    "시멘트 패널 — 현대적 무광 회색":           "fiber cement panel, modern matte grey cladding",
}

ROOF_STYLES = {
    "평지붕 — 모던 플랫 루프":              "flat roof, modern minimalist roofline",
    "박공지붕 — 삼각형 클래식 지붕":         "gabled roof, classic triangular pitched roof",
    "모임지붕 — 사방 경사 피라미드형":       "hip roof, four-sided sloped roof, pyramid form",
    "나비지붕 — V자 역경사 모던":            "butterfly roof, inverted V-shape, modern dramatic roofline",
    "외경사지붕 — 한쪽만 경사진 모던":       "shed roof, mono-pitch single slope, modern asymmetric",
    "한옥 기와지붕 — 전통 곡선 기와":        "traditional Korean tile roof, curved hanok eaves, clay tiles",
    "초가지붕 — 전통 볏짚 지붕":             "thatched roof, traditional straw roofing, cottage rustic",
    "그린루프 — 옥상 정원 녹화 지붕":        "green roof, rooftop garden, living grass roof, eco sustainable",
    "금속 지붕 — 징크/알루미늄 현대적":      "metal roof, zinc aluminum standing seam, modern industrial",
}

LANDSCAPING = {
    "없음 — 지붕/건물만":                       "",
    "미니멀 정원 — 잔디+자갈 심플":             "minimal garden, manicured lawn, gravel path, clean landscaping",
    "자연 정원 — 야생화+자연스러운 식재":        "naturalistic garden, wildflowers, organic planting, lush greenery",
    "일본 정원 — 모래+돌+소나무 선 정원":        "Japanese zen garden, raked gravel, stone lantern, pine bonsai",
    "지중해 정원 — 올리브+라벤더+테라코타":      "Mediterranean garden, olive trees, lavender, terracotta pots",
    "영국 코티지 정원 — 장미+덩굴 로맨틱":       "English cottage garden, roses, climbing vines, romantic flowers",
    "옥상 테라스 — 루프탑 데크 정원":            "rooftop terrace, deck garden, urban rooftop outdoor space",
    "수공간 — 연못/수영장/분수":                 "water feature, pond pool fountain, reflective water element",
    "대나무 — 프라이버시 대나무 스크린":          "bamboo screen, privacy bamboo grove, Asian garden element",
    "모던 데크 — 목재 데크+야외 가구":           "modern wood deck, outdoor furniture, contemporary terrace",
    "잔디마당 — 넓은 잔디 마당":                 "large lawn yard, green grass, open garden space",
    "자갈/쇄석 — 관리 쉬운 저유지 정원":         "gravel garden, pebble landscaping, low maintenance xeriscaping",
}

EXTERIOR_VIEWPOINTS = {
    "정면 — 건물 앞 직선 시점":           "straight-on front elevation view, architectural facade photography",
    "사선 45도 — 입체감 있는 코너뷰":     "45-degree corner view, three-quarter perspective, dynamic composition",
    "가로변 시점 — 길에서 바라보는 뷰":   "street-level view, pedestrian perspective, urban context",
    "원경 — 멀리서 전체 조망":            "wide establishing shot, full building in landscape context",
    "조감 — 드론 위에서 내려다보기":      "aerial drone view, bird's eye perspective, overhead shot",
    "정원 안쪽 — 마당에서 바라보기":      "garden interior view, looking toward house from garden",
    "야간 — 조명 켜진 밤 외관":           "night exterior, building lights glowing, dramatic evening atmosphere",
}

# ─── 실내 (Interior) ────────────────────────────────────

SPACE_TYPES = {
    "거실 — 메인 생활 공간":              "living room, main living area, lounge",
    "주방 — 요리/다이닝 공간":            "kitchen, cooking space, culinary area",
    "주방+거실 오픈 — 오픈플랜 LDK":      "open plan living dining kitchen, LDK open floor plan",
    "침실 — 마스터/일반 침실":            "bedroom, master bedroom, sleeping space",
    "욕실 — 메인 욕실/화장실":            "bathroom, main bathroom, wet room",
    "드레스룸 — 옷장/워크인 클로젯":      "walk-in closet, dressing room, wardrobe space",
    "홈오피스 — 재택근무 서재":           "home office, study room, work from home space",
    "다이닝룸 — 독립 식사 공간":          "dining room, formal dining space, dinner area",
    "현관 — 입구 엔트런스":               "entrance foyer, entryway, hallway",
    "계단실 — 계단+복도":                 "staircase, stairwell, interior stairs",
    "다용도실 — 세탁/수납 공간":          "utility room, laundry room, storage space",
    "테라스/발코니 — 실내외 연결 공간":   "terrace balcony, indoor outdoor transition space",
}

INTERIOR_STYLES = {
    "모던 미니멀 — 화이트+우드 깔끔함":          "modern minimalist interior, white walls, clean lines, uncluttered",
    "스칸디나비안 — 북유럽 따뜻한 화이트":        "Scandinavian interior, hygge, light wood, white, cozy warmth",
    "인더스트리얼 — 노출 벽돌+철제 파이프":       "industrial interior, exposed brick, metal pipes, raw urban loft",
    "재패니즈 — 와비사비 자연소재 선선함":         "Japanese wabi-sabi interior, natural materials, zen calm, simplicity",
    "보헤미안 — 레이어드 패턴 자유로운":           "bohemian interior, layered textiles, eclectic patterns, free-spirited",
    "클래식 — 몰딩+우아한 전통 유럽":             "classic European interior, crown molding, elegant traditional",
    "미드센추리 모던 — 1950s 레트로 유기적":      "mid-century modern interior, retro 1950s, organic curves, teak wood",
    "아르데코 — 골드+기하학 화려한 럭셔리":        "Art Deco interior, gold accents, geometric patterns, glamorous luxury",
    "컨트리/러스틱 — 자연소재 따뜻한 시골":        "rustic country interior, natural wood stone, warm farmhouse",
    "모던 럭셔리 — 고급 소재 세련된 호텔급":       "modern luxury interior, premium materials, hotel-like sophistication",
    "한옥 현대화 — 전통 목재+현대 감각":           "modern hanok interior, traditional Korean wood, contemporary fusion",
    "코티지 코어 — 꽃무늬+빈티지 아늑한":          "cottagecore interior, floral patterns, vintage charm, cozy nook",
    "테크 모던 — 스마트홈 첨단 미래적":            "tech modern interior, smart home, sleek futuristic, high-tech",
    "웜 모던 — 따뜻한 중성 톤 현대적":             "warm modern interior, neutral warm tones, cozy contemporary",
}

INTERIOR_MATERIALS = {
    "원목 플로어링 — 따뜻한 나무 바닥":         "solid wood flooring, warm oak hardwood floors",
    "헤링본 우드 — 헤링본 패턴 나무 바닥":       "herringbone wood floor, parquet pattern, elegant timber",
    "폴리싱 콘크리트 — 광택 콘크리트 바닥":      "polished concrete floor, smooth industrial finish",
    "대리석 — 고급스러운 마블 바닥/벽":          "marble flooring, luxurious stone, veined marble surface",
    "테라조 — 빈티지 모던 테라조":               "terrazzo floor, vintage modern speckled surface",
    "타일 — 세라믹/포슬린 타일":                 "ceramic porcelain tile, clean hygienic surface",
    "헥사곤 타일 — 육각형 패턴 타일":            "hexagon tile, geometric pattern floor, retro modern",
    "모르타르/마이크로시멘트 — 매끄러운 회색":    "microcement mortar finish, seamless grey smooth surface",
    "리넨/패브릭 벽지 — 부드러운 텍스처":        "linen fabric wallpaper, soft textured wall covering",
    "루버/슬랫 우드 — 세로 목재 루버 벽":         "wood slat wall, vertical louvre panel, warm texture accent",
    "노출 벽돌 — 인더스트리얼 벽돌 벽":           "exposed brick wall, industrial raw masonry interior",
}

FURNITURE_STYLES = {
    "없음 — 빈 공간/건축 위주":              "",
    "미니멀 빌트인 — 군더더기 없는 붙박이":   "built-in minimalist furniture, seamless cabinetry, integrated storage",
    "스칸디나비안 — 라이트 오크 심플 가구":   "Scandinavian furniture, light oak wood, simple clean design",
    "미드센추리 — 레트로 유기적 곡선 가구":   "mid-century modern furniture, organic curves, tapered legs, retro",
    "모던 럭셔리 — 벨벳+골드 고급 가구":      "modern luxury furniture, velvet upholstery, gold accents, premium",
    "인더스트리얼 — 철제+목재 워크숍 스타일": "industrial furniture, metal and wood, workshop loft style",
    "재패니즈 로우 — 낮은 좌식 일본 가구":    "Japanese low furniture, floor-level seating, zen minimal",
    "클래식 유럽 — 몰딩 우아한 앤티크":       "classic European furniture, ornate molding, antique elegant",
    "IKEA 스타일 — 실용적 모던 북유럽":       "IKEA-style practical modern Scandinavian furniture, affordable design",
}

COLOR_PALETTE = {
    "없음 — 스타일 기본값":                    "",
    "올화이트 — 순백 미니멀":                  "all-white color scheme, pure white walls ceiling floor, minimal",
    "화이트+우드 — 밝고 따뜻한":               "white and natural wood tones, bright warm neutral palette",
    "그레이+화이트 — 세련된 모노톤":            "grey and white palette, sophisticated monochromatic scheme",
    "웜 베이지+테라코타 — 따뜻한 어스톤":       "warm beige terracotta earth tones, cozy warm palette",
    "블랙+화이트 — 극적인 대비":                "black and white high contrast, bold dramatic palette",
    "네이비+골드 — 고급스러운 다크":            "navy blue and gold, rich luxurious dark palette",
    "그린+내추럴 — 자연 바이오필릭":            "green and natural tones, biophilic nature-inspired palette",
    "블ush 핑크+골드 — 로맨틱 럭셔리":          "blush pink and gold, romantic feminine luxury palette",
    "미드나잇 — 어두운 드라마틱 다크":           "dark moody midnight palette, dramatic deep tones, dark interior",
    "스카이블루+화이트 — 지중해 상쾌한":        "sky blue and white Mediterranean palette, fresh airy",
}

INTERIOR_VIEWPOINTS = {
    "정면 — 공간 정면에서 직선":           "straight-on interior elevation, architectural interior photography",
    "사선 코너 — 대각선 깊이감":           "diagonal corner perspective, depth and dimension, interior shot",
    "와이드앵글 — 전체 공간 넓게":         "wide angle interior, full room capture, spacious perspective",
    "디테일 클로즈업 — 소재/디테일 강조":  "detail close-up, material texture emphasis, architectural detail",
    "창문에서 — 창밖 뷰 포함":             "window view, interior with outside view, indoor-outdoor connection",
    "위에서 — 하이앵글 오버헤드":          "high angle overhead shot, top-down interior perspective",
    "침대/소파 시점 — 낮은 눈높이":        "low eye-level from bed or sofa, intimate interior perspective",
}

# ─── 공통 (실내외 공용) ──────────────────────────────────

LIGHTING = {
    "자연광 — 맑은 낮 햇살":                  "natural daylight, bright sunlight streaming in, clear day",
    "골든아워 — 따뜻한 석양빛":               "golden hour warm light, late afternoon sun, amber glow",
    "오버캐스트 — 흐린 날 부드러운 확산광":    "overcast soft diffused light, cloudy day, even gentle illumination",
    "야간 조명 — 실내외 조명 켜진 밤":         "night lighting, artificial lights glowing, evening atmosphere",
    "드라마틱 — 강한 명암 대비":              "dramatic chiaroscuro lighting, strong shadows and highlights",
    "스튜디오 — 전문 건축 사진 조명":          "professional architectural studio lighting, controlled even light",
    "캔들/따뜻한 — 아늑한 따뜻한 빛":         "warm candlelight ambiance, cozy warm lighting, intimate glow",
    "블루아워 — 해질 무렵 신비로운 파란빛":    "blue hour twilight, mystical cool blue atmospheric glow",
    "스팟 조명 — 포인트 조명 강조":            "spot accent lighting, highlighted focal points, dramatic spots",
}

TIME_OF_DAY = {
    "없음": "",
    "이른 아침 — 부드러운 아침 햇살":      "early morning soft light, fresh dawn atmosphere, quiet morning",
    "한낮 — 강한 직사광선":                "midday harsh sunlight, strong direct light, high contrast",
    "오후 — 따뜻한 오후 햇살":             "late afternoon warm sunlight, relaxed golden atmosphere",
    "황혼 — 드라마틱 노을":                "dusk twilight, dramatic sunset colors, sky ablaze",
    "야간 — 어두운 밤 조명":               "night time, dark sky, artificial lighting, nocturnal atmosphere",
}

WEATHER = {
    "없음": "",
    "맑음 — 파란 하늘 선명한":             "clear blue sky, bright sunny weather, sharp shadows",
    "흐림 — 구름 낀 부드러운":             "overcast cloudy sky, soft diffused light, moody atmosphere",
    "비 — 빗속 젖은 바닥 반사":            "rainy weather, wet ground reflections, rain atmosphere",
    "눈 — 눈 내리는 겨울":                 "snowfall, snow-covered, winter white landscape",
    "안개 — 신비로운 안개":                "foggy misty atmosphere, mysterious soft focus",
    "바람 — 나무 흔들리는 바람":           "windy, trees swaying, dynamic wind effect",
}

CAMERA_ANGLES = {
    "없음": "",
    "아이레벨 — 눈높이 수평":              "eye level straight-on, natural human perspective",
    "로우앵글 — 아래서 위로 웅장한":       "low angle upward, monumental powerful perspective",
    "하이앵글 — 위에서 내려다보기":        "high angle downward, elevated overview perspective",
    "드론 — 공중 조감":                    "drone aerial view, bird's eye overhead shot",
    "사선 — 45도 역동적":                  "45-degree diagonal, dynamic three-quarter angle",
}

COLOR_GRADES = {
    "없음": "",
    "내추럴 — 자연스러운 실제 색감":       "natural color grading, true-to-life realistic colors",
    "웜 — 따뜻한 황금빛 톤":               "warm golden color grade, cozy inviting tones",
    "쿨 — 차갑고 세련된 블루톤":           "cool blue color grade, crisp clean tones",
    "흑백 — 클래식 모노크롬":              "black and white, classic monochrome architectural",
    "시네마틱 — 영화적 틸트앤오렌지":      "cinematic teal and orange, film look color grade",
    "하이키 — 밝고 에어리":                "high key bright airy, overexposed clean white tone",
    "다크무드 — 어둡고 드라마틱":          "dark moody grade, deep shadows, dramatic contrast",
    "빈티지 — 필름 질감 레트로":           "vintage film grain, faded retro analog look",
}

MOOD = {
    "없음": "",
    "아늑한 — 따뜻하고 편안한":            "cozy warm inviting mood, homey comfortable atmosphere",
    "럭셔리 — 고급스럽고 우아한":          "luxurious elegant mood, premium sophisticated atmosphere",
    "미니멀 — 깔끔하고 절제된":            "minimal clean restrained mood, quiet understated atmosphere",
    "드라마틱 — 강렬하고 극적인":          "dramatic intense mood, powerful bold atmosphere",
    "로맨틱 — 부드럽고 따뜻한":            "romantic soft warm mood, tender dreamy atmosphere",
    "자연친화 — 유기적 바이오필릭":        "biophilic natural mood, organic earthy serene atmosphere",
    "미래지향 — 첨단 미래적":              "futuristic forward-looking mood, high-tech sleek atmosphere",
    "레트로 — 빈티지 향수로운":            "retro nostalgic mood, vintage charming atmosphere",
}

SPECIAL_FEATURES = {
    "없음": "",
    "수영장 — 야외/실내 풀":               "swimming pool, architectural pool, water reflection",
    "스카이라이트 — 채광창 천장":          "skylight, roof window, natural light from above",
    "대형 창문 — 파노라믹 뷰 창":          "floor-to-ceiling windows, panoramic glazing, expansive view",
    "오픈 계단 — 떠있는 플로팅 계단":      "floating staircase, open riser stairs, sculptural staircase",
    "중정 — 안뜰 코트야드":                "courtyard, interior garden, open-air atrium",
    "벽난로 — 실내 벽난로":                "fireplace, hearth, warm interior focal point",
    "북카페 — 책장 가득한 서재 벽":        "floor-to-ceiling bookshelf, library wall, book collection",
    "식물 — 실내 녹색 식물 플랜트":        "indoor plants, lush greenery, biophilic plant decor",
    "아트월 — 갤러리 아트 벽면":           "art gallery wall, curated artwork display, statement wall",
    "루프탑 테라스 — 옥상 정원":           "rooftop terrace, rooftop garden, urban outdoor space",
}

CAMERAS = {
    "하셀블라드 — 중형 건축 사진":         "Hasselblad medium format, architectural photography, ultra detail",
    "캐논 EOS R5 — 광각 인테리어":         "Canon EOS R5 wide angle lens, interior architectural photography",
    "소니 A7R V — 고해상도 디테일":        "Sony A7R V high resolution, fine detail architectural shot",
    "라이카 — 독일 감성 정밀":             "Leica precision, German optics, fine art architectural photography",
    "드론 카메라 — 공중 촬영":             "drone camera, aerial photography, DJI Mavic Pro",
    "아이폰 — 자연스러운 일상적":          "iPhone natural realistic style, casual everyday photography",
}

RENDER_STYLES = {
    "실사 사진 — 완성된 실제 건물 같은":       "photorealistic architectural photography, completed building photo",
    "CGI 렌더링 — 3D 시각화 고품질":           "high quality CGI architectural visualization, 3D render",
    "수채화 스케치 — 손 그린 건축 스케치":      "watercolor architectural sketch, hand-drawn illustration style",
    "라인드로잉 — 건축 선화 도면 느낌":         "architectural line drawing, blueprint sketch style",
    "무드보드 — 소재/색상 콜라주":              "mood board collage, material and color palette presentation",
}

# ─── 실내 환경 키워드 (날씨 충돌 감지용) ──────────────────
INDOOR_SPACES = {
    "거실", "주방", "주방+거실 오픈", "침실", "욕실",
    "드레스룸", "홈오피스", "다이닝룸", "현관", "계단실", "다용도실",
}
