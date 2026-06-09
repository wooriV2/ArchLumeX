"""
LumineX core/data.py
모든 데이터 딕셔너리 정의
"""

ASPECT_RATIOS = {
    # ── 기본 (세로) ──
    "세로 2:3 — 인물 기본 ★": "portrait 2:3 vertical",
    "세로 9:16 — 모바일/릴스": "portrait 9:16 vertical, mobile optimized",
    "세로 3:4 — 전신샷": "portrait 3:4 vertical",
    "세로 4:5 — 인스타 세로": "portrait 4:5 vertical, Instagram optimized",
    # ── 정방형 ──
    "정방형 1:1 — 인스타 피드": "square 1:1",
    # ── 가로 ──
    "가로 16:9 — 시네마틱 와이드": "landscape 16:9 cinematic wide",
    "가로 4:3 — 화보/매거진": "landscape 4:3 editorial wide",
    "가로 3:2 — 클래식 가로": "landscape 3:2 horizontal",
    "가로 2:1 — 파노라마": "landscape 2:1 panoramic wide",
    "가로 21:9 — 울트라와이드": "landscape 21:9 ultrawide cinematic",
}

# ─── 데이터 ───────────────────────────────────────────────
MODEL_APPEARANCE = {
    "🇰🇷 한국 — K-beauty, 하얀 피부, 또렷한 이목구비": "Korean beauty, fair porcelain skin, sharp elegant facial features, K-beauty aesthetic",
    "🇯🇵 일본 — J-beauty, 도자기 피부, 섬세한 이목구비": "Japanese beauty, porcelain delicate skin, refined subtle features, J-beauty aesthetic",
    "🇨🇳 중국 — 우아한 골격, 세련된 동양미": "Chinese beauty, elegant facial bone structure, sophisticated Eastern features",
    "🌏 동남아 — 골든 태닝, 이국적 태국/베트남 미녀": "Southeast Asian beauty, golden tan glowing skin, exotic Thai Vietnamese features",
    "🌙 중동 — 올리브 피부, 깊은 눈, 아라비안 뷰티": "Middle Eastern beauty, warm olive skin, deep dark sultry eyes, Arabian exotic features",
    "🇪🇺 유럽 — 백인, 강한 골격, 유러피안 미녀": "European Caucasian beauty, fair skin, strong bone structure, classic European features",
    "🇺🇸 미국 — 올아메리칸, 건강미, 애슬레틱": "All-American beauty, sun-kissed healthy skin, fresh athletic look, girl-next-door glamour",
    "💃 라틴 — 브론즈 태닝, 볼륨감, 브라질/콜롬비안": "Latina beauty, bronzed tan glowing skin, voluptuous curves, Brazilian Colombian exotic",
    "✨ 혼혈 — 이국적 믹스, 독특한 매력": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
    "🖤 흑인 — 짙은 피부, 강렬한 이목구비, 파워풀": "Black beauty, rich deep dark skin, powerful striking features, African goddess",
    "🇧🇷 브라질리언 — 브라질, 구릿빛 피부, 풍만한 글래머": "Brazilian beauty, bronzed tan skin, full voluptuous curves, tropical glamour",
    "🇨🇴 콜롬비안 — 콜롬비아, 이국적 라틴 미녀": "Colombian beauty, exotic Latin features, olive skin, sultry dark eyes",
    "🇸🇪 스칸디나비안 — 북유럽, 금발, 차갑고 우아한": "Scandinavian beauty, platinum blonde, ice blue eyes, tall elegant Nordic features",
    "🇷🇺 동유럽 — 슬라브 미녀, 강한 골격, 매혹적": "Eastern European beauty, Slavic features, high cheekbones, mysterious allure",
    "🇲🇦 모로칸 — 북아프리카, 이국적 중동+아프리카 믹스": "Moroccan beauty, exotic North African features, olive skin, dark almond eyes",
    "🇪🇬 이집트 — 클레오파트라 느낌, 강렬한 눈매": "Egyptian beauty, Cleopatra-like features, intense dark eyes, Mediterranean skin",
    "🇮🇳 인도 — 볼리우드, 황금 피부, 강렬한 눈매": "Indian beauty, golden warm skin, Bollywood glamour, expressive dark eyes, exotic features",
    "🇵🇭 필리핀 — 동남아+스페인 혼혈 미녀": "Filipino beauty, mixed Southeast Asian Spanish features, warm tan skin, exotic mestiza",
    "🇯🇲 자메이카 — 카리브해, 이국적 혼혈": "Jamaican beauty, Caribbean exotic features, warm brown skin, tropical island glamour",
    "🇰🇪 케냐 — 동아프리카, 강렬하고 우아한": "Kenyan beauty, East African features, rich dark skin, powerful elegant presence",
}

AGE_APPEARANCE = {
    "없음": "",
    "18-20 — 어린 성인, 청순한": "18-20 years old young adult, fresh youthful face, college age",
    "20대 초반 — 발랄하고 생기있는": "early 20s, vibrant youthful beauty, 21-24 years old",
    "20대 중반 — 전성기 글래머": "mid 20s, peak glamour beauty, 25-27 years old",
    "20대 후반 — 성숙미 시작": "late 20s, maturing beauty, 28-29 years old, sophisticated",
    "30대 초반 — 세련된 성숙미": "early 30s, refined mature beauty, 30-33 years old, elegant",
    "30대 중반 — 카리스마 있는": "mid 30s, charismatic mature glamour, 34-37 years old",
    "30대 후반 — 원숙한 매력": "late 30s, ripened allure, 38-39 years old, sophisticated confidence",
    "40대 초반 — 우아한 성숙미": "early 40s, elegantly mature, 40-44 years old, refined glamour",
    "40대 후반 — 카리스마 중년": "late 40s, powerful mature charisma, 45-49 years old, distinguished",
    "50대 — 실버 글래머": "50s, silver glamour, mature distinguished beauty, 50-59 years old",
    "60대 — 우아한 시니어": "60s, gracefully aged beauty, senior glamour, distinguished elegance",
    "70대+ — 레전더리 시니어": "70s and above, legendary senior beauty, timeless grace, iconic presence",
}

MODEL_TYPES = {
    # ── 극초슬림 계열 ──
    "울트라 슬림 — 하이패션 극세장": "ultra-slim high fashion model, very slender editorial figure, elongated silhouette, fashion week physique",
    "슈퍼 슬림 — 마른 런웨이": "super slim runway model, thin elegant frame, elongated slender body, editorial fashion model",
    "슬림 런웨이 — 초장신 늘씬": "tall slim runway model, long legs, slender waist, narrow hips, elongated graceful silhouette",
    "슬림 엘레강스 — 날씬하고 우아한": "slender elegant model, slim narrow frame, graceful delicate figure, refined fashion presence",
    # ── 슬림톤 계열 ──
    "슬림 톤 — 날씬하고 탄탄한": "slim toned model, lean athletic build, flat stomach, slim toned silhouette, light but defined",
    "발레리나 — 길고 가늘고 우아한": "ballerina physique, slender elongated figure, narrow hips, graceful elegant posture, dancer's perfect poise",
    "슬림 피트니스 — 날씬한 운동선수": "slim fitness model, lean defined muscles, flat abs, athletic slim silhouette, lightweight athletic",
    # ── 애슬레틱 계열 ──
    "피트니스 — 탄탄한 복근, 근육미": "athletic fitness model, defined six-pack abs, toned muscular legs, round athletic hips, powerful physique",
    "비키니 컴페티션 — 대회용 극강 근육": "bikini competition model, extremely defined muscles, shredded competition physique, round athletic hips, competition-ready body",
    "파워 피트니스 — 강한 근육미": "power fitness model, very muscular defined body, strong arms and legs, muscular powerful build",
    "스포츠 글램 — 탄탄+볼륨": "sports glamour model, toned athletic body with curves, defined abs, round hips, fit and voluptuous",
    # ── 글래머 계열 ──
    "소프트 글램 — 부드러운 여성미": "soft glamour model, feminine gentle curves, round soft hips, elegant graceful figure, naturally beautiful",
    "VS 앤젤 — 완벽한 VS 글래머": "Victoria's Secret Angel body, toned flat abs, long legs, curvaceous yet athletic silhouette, runway perfect",
    "핫 글래머 — 잘록한 허리+볼륨": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
    "슈퍼 글래머 — 극강 모래시계": "super glamour model, tiny waist, very wide round hips, maximum hourglass silhouette, pinup glamour",
    "럭셔리 글램 — 고급스러운 볼륨": "luxury glamour model, defined waist, wide round hips, sophisticated voluptuous elegance, high-end glamour",
    # ── 커브 계열 ──
    "내추럴 커브 — 자연스러운 곡선미": "natural curvy model, round natural hips, soft gentle curves, realistic womanly figure",
    "소프트 커브 — 부드럽고 풍만한": "soft curvy model, wide round hips, full soft thighs, gentle voluptuous curves, feminine warmth",
    "풀 커브 — 볼륨감 있는 커브": "full curvy model, very wide hips, full round thighs, voluptuous hourglass silhouette, abundant curves",
    "글래머 커브 — 커브+글래머 믹스": "glamour curvy model, dramatic waist-to-hip ratio, very wide round hips, thick thighs, glamorous voluptuous",
    # ── 플러스사이즈 계열 ──
    "플러스 내추럴 — 자연스러운 플러스": "natural plus-size model, soft rounded belly, wide hips, full thighs, body positive natural figure",
    "플러스 글램 — 플러스사이즈 글래머": "plus-size glamour model, soft belly, wide full hips, thick thighs, confident couture presence",
    "라지 플러스 — 매우 풍만한": "large plus-size fashion model, round belly, very wide hips, heavy full thighs, body positive editorial",
    "슈퍼 플러스 — 초풍만": "super plus-size runway model, dramatic full-figure silhouette, soft belly, extremely wide hips, maximalist curvy fashion",
    # ── BBW 계열 ──
    "BBW 글래머 — 풍만한 글래머": "BBW glamour model, extremely curvy fashion silhouette, broad hips, thick thighs, soft layered abdomen, luxurious BBW presence, confident couture",
    "슈퍼 BBW — 극풍만 글래머": "super plus-size runway model, massive voluptuous proportions, very heavy curvy physique, broad hips, thick thighs, soft realistic body folds, abundant body volume, maximalist curvy fashion styling",
    # ── 블랙 글래머 계열 ──
    "블랙 글래머 — 극강 모래시계 흑인 체형": "Black beauty hourglass, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, very thick thighs, full heavy round buttocks, abundant voluptuous curves, African goddess proportions",
    # ── 글로벌 글래머 극단 계열 (2026-06-08 추가) ──
    "🇧🇷 브라질 부티 글램 — 카니발 여신 극강 힙": "Brazilian carnival goddess, massive round bubble butt dominating silhouette, extremely wide hips with very narrow waist, powerfully thick thighs, heavy full rounded buttocks projecting dramatically, bronzed voluptuous body, samba dancer curves",
    "🇨🇴 콜롬비안 레게톤 — 조각된 극단 8자": "Colombian reggaeton goddess, extreme exaggerated hourglass figure, impossibly tiny cinched waist, explosively wide dramatic round hips, full sculpted bust, lifted prominent round buttocks, surgically perfect waist-to-hip ratio, thick powerful thighs, bronzed Latin skin glistening",
    "🏝️ 카리브 댄스홀 — 탄력 극강 부티": "Caribbean dancehall queen, powerfully athletic bubble butt with spring-like firmness, snatched tiny waist, explosively wide round hips, muscular thick thighs built for dancing, deeply bronzed Caribbean skin, high-energy dancehall body, tight toned voluptuous curves",
    "🇮🇳 볼리우드 글램 — 황금빛 풍만 곡선": "Bollywood goddess proportions, voluptuous golden curves, dramatic waist-to-hip ratio, full rounded bust and wide hips, warm glistening bronze skin, opulent Indian glamour",
    "🌺 폴리네시안 여신 — 강건한 풍만미": "Polynesian goddess proportions, full heavy rounded hips and thighs, broad powerful shoulders framing voluptuous figure, dramatically wide lower body, thick full thighs, abundant rounded curves, statuesque large-framed island goddess, warm bronzed glowing skin, majestic full-figured Polynesian beauty",
    "👑 누비안 하이패션 — 초장신 극세장": "Nubian high fashion goddess, towering elongated runway physique, impossibly long legs, sharp sculpted collarbones, regal elongated neck, East African editorial proportions, deep luminous skin",
    "🏜️ 사하라 투아레그 — 위엄있는 장신 골격": "Saharan Tuareg goddess, towering commanding tall frame, long powerful legs, strong broad shoulders, lean angular physique, regal desert nomad proportions, narrow elegant hips, sculpted athletic build, deep matte dark skin, statuesque elongated silhouette, desert warrior elegance",
    "🛡️ 마사이 워리어 — 전사의 장신 우아함": "Maasai warrior goddess, towering ultra-tall physique, impossibly long sculpted legs, lean powerful muscle, proud elongated silhouette, deep skin warrior elegance",
    "🦢 소말리 모델 — 섬세 골격 극도 슬림": "Somali fashion goddess, extremely elongated delicate frame, razor-sharp cheekbones, swan-like neck, willowy editorial physique, smooth deep complexion",
    "❄️ 북유럽 발키리 — 차가운 전사 슬림": "Nordic Valkyrie, tall slender warrior physique, broad strong shoulders, long lean legs, flat athletic torso, ice-cold commanding presence, pale luminous arctic skin, platinum blonde Nordic beauty, fierce battle-hardened expression, sleek powerful silhouette",
    "⚔️ 아마조네스 — 근육질 곡선 극단": "Amazon warrior goddess, powerfully muscular sculpted frame, defined abs, strong broad shoulders, yet dramatic feminine waist-to-hip curve, battle-hardened glamour, oiled skin",
    "🔥 누비안 부티빌더 — 극강 힙+선명 복근": "Nubian fitness goddess, shredded defined abs combined with extremely wide round hips, thick muscular thighs, snatched waist, powerful African physique, oiled glistening skin",
    "🎀 벨 에포크 코르셋 — 불가능한 잘록 허리": "Belle Epoque corset silhouette, impossibly tiny corseted waist, full rounded bust above, dramatic flared hips below, Gibson Girl extreme hourglass, porcelain skin",
    "🐉 판타지 여제 — 군림하는 거상 곡선": "Fantasy dragon empress proportions, tall imposing regal frame, dramatic commanding curves, wide powerful hips, statuesque sovereign physique, otherworldly presence",
    "🌹 슬라브 봄셸 — 1950s 조각 핀업 8자": "Slavic pin-up bombshell, sculpted hourglass, impossibly cinched corset waist, full high bust, wide rounded hips, retro bombshell proportions, statuesque porcelain skin",
}

# ── 보정 섹션 (MODEL_TYPES 미세조정용) ──
BODY_WEIGHT = {
    "없음": "",
    "슬림 톤 보정": "additionally slim toned, lean defined muscles, flat stomach",
    "오일드 볼륨 보정": "additionally oiled voluminous body, gleaming full curves",
    "근육 정의 보정": "additionally very muscular defined, visible muscle striations",
    "소프트 배 보정": "additionally soft rounded abdomen, natural belly, realistic body",
    "허벅지 볼륨 보정": "additionally very thick thighs, full heavy legs",
}

BUST_SIZE = {
    "없음": "",
    "플랫 보정": "additionally very flat chest, minimal breast tissue, petite frame",
    "스몰 보정": "additionally small petite bust, modest chest",
    "미디엄 보정": "additionally natural proportionate bust, balanced figure",
    "라지 보정": "additionally very full bust, deep cleavage, editorial glamour",
    "엑스라지 보정": "additionally extremely full heavy bust, maximalist glamour proportions",
    "슈퍼라지 보정": "additionally very generous full chest, maximalist couture proportions",
}

HIP_SIZE = {
    "없음": "",
    "플랫 보정": "additionally very flat hips, minimal buttocks, slim lower body",
    "슬림 보정": "additionally slim narrow hips, small flat buttocks",
    "풀 보정": "additionally full round hips, prominent rounded buttocks, wide hip-to-waist ratio",
    "글래머 보정": "additionally dramatic hourglass hips, large round buttocks, extreme curves",
    "브라질리언 보정": "additionally Brazilian-style round buttocks, very prominent rear, maximum curves, editorial glamour",
    "엑스트림 보정": "additionally dramatically wide hips, very prominent round buttocks, sculptural curvy silhouette",
}

OUTFIT_TYPES = {
    "마이크로 비키니 — 끈 비키니, SI 수영복 화보": {
        "gemini": "micro string bikini, tiny triangle top, string thong bottom, minimal coverage, Sports Illustrated swimsuit style",
        "chatgpt": "designer string bikini, minimalist swimwear, Sports Illustrated editorial style",
    },
    "원피스 수영복 — 하이컷, 컷아웃 디자인": {
        "gemini": "high-cut one-piece swimsuit, bold cutouts, athletic glamour",
        "chatgpt": "high-cut designer one-piece swimsuit, artistic cutouts, Sports Illustrated style",
    },
    "컷아웃 미니드레스 — 전략적 컷아웃, 섹시한 디자인": {
        "gemini": "cutout mini dress, strategic skin-baring cutouts, bold editorial design",
        "chatgpt": "designer cutout mini dress, architectural cutout details, fashion editorial",
    },
    "하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인": {
        "gemini": "ultra-high slit evening gown, deep plunging neckline, red carpet glamour",
        "chatgpt": "high slit evening gown, plunging neckline, luxury red carpet fashion",
    },
    "밴도탑+초미니 — 배꼽 노출, 극초미니 스커트": {
        "gemini": "bandeau crop top, exposed midriff, micro mini skirt, fashion editorial",
        "chatgpt": "bandeau crop top, midriff-baring, micro mini skirt, bold fashion editorial",
    },
    "바디콘 미니드레스 — 몸매 강조, 타이트핏": {
        "gemini": "bodycon mini dress, body-hugging silhouette, glamorous tight fit",
        "chatgpt": "bodycon mini dress, figure-hugging design, glamorous fashion editorial",
    },
    "코르셋 드레스 — 잘록한 허리, 볼륨감 강조": {
        "gemini": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "chatgpt": "fashion corset dress, cinched waist, dramatic neckline, haute couture style",
    },
    "브라탑+하이슬릿 — 브라탑, 롱 하이슬릿": {
        "gemini": "structured crop top, asymmetrical high-slit runway skirt, fashion editorial",
        "chatgpt": "structured couture crop top, asymmetrical runway skirt with elegant slit, Vogue editorial",
    },
    "란제리 에디토리얼 — VS 스타일, 실크 레이스": {
        "gemini": "luxury silk lace fashion set, elegant runway lingerie editorial, glamorous couture",
        "chatgpt": "luxury silk lace fashion set, elegant couture editorial, artistic glamour photography",
    },
    "시스루 바디수트 — 메쉬, 아방가르드": {
        "gemini": "sheer mesh fashion bodysuit, avant-garde couture editorial, artistic runway",
        "chatgpt": "sheer fashion bodysuit, mesh overlay, avant-garde couture editorial style",
    },
    "오픈백 미니드레스 — 등 노출, 플런징 넥": {
        "gemini": "open back mini dress, elegant décolletage, high-fashion editorial",
        "chatgpt": "backless mini dress, structured neckline, high-fashion editorial",
    },
    "스포츠브라+레깅스 — 핫한 피트니스 룩": {
        "gemini": "sports bra, high-waist leggings, midriff bare, fitness editorial",
        "chatgpt": "athletic sports bra, high-waist leggings, fitness editorial, Sports Illustrated",
    },
    "모노키니 — 원피스 수영복 변형, 대담한 컷아웃": {
        "gemini": "monokini swimsuit, bold cutout one-piece, daring swimwear design",
        "chatgpt": "designer monokini, cutout one-piece swimsuit, bold editorial swimwear",
    },
    "웨딩 드레스 — 럭셔리 브라이달, 관능적": {
        "gemini": "luxurious wedding dress, plunging neckline bridal gown, sensual bridal fashion",
        "chatgpt": "luxury bridal gown, dramatic wedding dress, high fashion bridal editorial",
    },
    "코트 only — 롱코트만 입은 미니멀 글래머": {
        "gemini": "oversized structured long coat, fully covered couture fashion, sleek editorial coat styling, luxury outerwear",
        "chatgpt": "oversized luxury long coat, fully covered couture editorial, high-fashion outerwear look",
    },
    "가죽 재킷 + 란제리 — 엣지있는 레이어드": {
        "gemini": "leather jacket with silk camisole, edgy layered fashion editorial, rock glamour styling",
        "chatgpt": "leather jacket layered over camisole, edgy fashion editorial, bold layered style",
    },
    "선드레스 — 민소매 여름 원피스": {
        "gemini": "sundress, sleeveless summer dress, flowy feminine silhouette, casual glamour",
        "chatgpt": "sundress, sleeveless summer dress, elegant casual editorial",
    },
    "홀터넥 드레스 — 목 끈, 등 노출": {
        "gemini": "halter neck dress, tied at neck, open back, summer glamour editorial",
        "chatgpt": "halter neck dress, elegant open back, luxury summer editorial",
    },
    "오프숄더 드레스 — 어깨 드러나는": {
        "gemini": "off-shoulder dress, bardot neckline, elegant shoulder reveal, summer fashion",
        "chatgpt": "off-shoulder dress, bardot style, sophisticated summer editorial",
    },
    "스파게티 스트랩 드레스 — 얇은 끈": {
        "gemini": "spaghetti strap dress, thin shoulder straps, elegant summer silhouette",
        "chatgpt": "spaghetti strap dress, delicate straps, luxury summer editorial",
    },
    "랩 드레스 — 앞 여밈 여름 원피스": {
        "gemini": "wrap dress, front-tie waist, flowing summer dress, feminine editorial",
        "chatgpt": "wrap dress, tied waist, elegant flowing summer editorial",
    },
    "플로럴 맥시 스커트 — 꽃무늬 긴 치마": {
        "gemini": "floral maxi skirt, long flowing floral print, bohemian summer fashion",
        "chatgpt": "floral maxi skirt, elegant long flowing skirt, summer editorial",
    },
    "보헤미안 티어드 스커트 — 레이어드 치마": {
        "gemini": "bohemian tiered skirt, layered flowing fabric, free-spirited summer style",
        "chatgpt": "tiered boho skirt, layered summer skirt, artistic editorial",
    },
    "사롱/파레오 — 해변용 두르는 치마": {
        "gemini": "sarong pareo beach wrap skirt, tied at hip, tropical beach glamour",
        "chatgpt": "sarong beach wrap, elegant tropical editorial, beach fashion",
    },
    "미니 플레어 스커트 — 짧고 퍼지는": {
        "gemini": "mini flare skirt, short A-line flared skirt, playful summer fashion",
        "chatgpt": "mini flare skirt, short A-line, playful summer editorial",
    },
    "골프/테니스 스커트 — 스포티 미니스커트": {
        "gemini": "golf tennis mini skirt, pleated sporty skirt, athletic glamour, country club chic",
        "chatgpt": "golf tennis pleated mini skirt, sporty chic editorial, athletic fashion",
    },
}

# ── 상의/하의 분리 선택 ──
TOP_TYPES = {
    "없음 (의상 타입 사용)": "",
    # ── 수영복/비키니 ──
    "비키니 탑 — 트라이앵글 탑": "luxury triangle bikini top, elegant swimwear editorial",
    "마이크로 비키니 탑 — 미니멀 트라이앵글": "luxury satin bikini top, minimal triangle design, high fashion swimwear",
    "스포츠 비키니 탑 — 피트니스 스포츠브라": "athletic sports bikini top, fitness editorial, sporty glamour",
    "밴도 탑 — 스트랩리스 밴도": "bandeau strapless top, minimalist swimwear, fashion editorial",
    # ── 캐주얼/패션 ──
    "크롭 탑 — 짧은 탑, 배꼽 노출": "crop top, midriff-baring, casual chic",
    "브라렛 — 브라렛 스타일 탑": "bralette top, delicate strappy design, feminine editorial",
    "티셔츠 — 캐주얼 티셔츠": "fitted t-shirt, casual chic, everyday glamour",
    "탱크탑 — 민소매 탑": "tank top, sleeveless, casual athletic editorial",
    "오프숄더 탑 — 어깨 드러나는 탑": "off-shoulder top, bardot neckline, elegant shoulder reveal",
    "홀터넥 탑 — 목 끈 탑": "halter neck top, tied at neck, open back design",
    "코르셋 탑 — 잘록한 허리 강조": "corset top, boned structure, cinched waist emphasis",
    "버튼업 셔츠 — 단추 셔츠 (열린)": "open button-up shirt, relaxed editorial, effortless chic",
    "니트 스웨터 — 타이트 니트": "fitted knit sweater, body-hugging ribbed knit, cozy glamour",
    "블레이저 — 테일러드 재킷": "tailored blazer, structured jacket, power fashion editorial",
}

BOTTOM_TYPES = {
    "없음 (의상 타입 사용)": "",
    # ── 수영복/비키니 ──
    "비키니 바텀 — 하이컷 비키니": "luxury high-cut bikini bottom, elegant swimwear editorial",
    "마이크로 비키니 바텀 — 미니멀 커버리지": "luxury high-cut bikini bottom, minimal coverage, high fashion swimwear",
    "보드숏 — 서퍼 스타일": "board shorts, surfer style, casual beach editorial",
    # ── 스커트 ──
    "미니 스커트 — 짧은 치마": "mini skirt, short hemline, bold fashion editorial",
    "미디 스커트 — 무릎 아래 치마": "midi skirt, below-knee length, elegant editorial",
    "맥시 스커트 — 긴 치마": "maxi skirt, floor-length flowing skirt, dramatic editorial",
    "골프/테니스 스커트 — 스포티 미니": "golf tennis mini skirt, pleated sporty skirt, athletic glamour",
    "플레어 스커트 — 퍼지는 스커트": "flare skirt, A-line silhouette, feminine movement",
    "타이트 미니 — 몸에 딱 붙는 미니": "tight bodycon mini skirt, figure-hugging short skirt",
    "하이슬릿 스커트 — 트임 있는 스커트": "high-slit skirt, dramatic leg reveal, red carpet editorial",
    # ── 팬츠/쇼츠 ──
    "하이웨이스트 쇼츠 — 반바지": "high-waist shorts, cropped legs, casual glamour editorial",
    "데님 쇼츠 — 청반바지": "denim cut-off shorts, casual summer editorial",
    "레깅스 — 타이트 레깅스": "high-waist leggings, fitted athletic pants, fitness editorial",
    "와이드 팬츠 — 넓은 바지": "wide-leg trousers, flowing palazzo pants, elegant editorial",
    "스키니 팬츠 — 슬림 팬츠": "skinny pants, slim-fit trousers, sleek fashion editorial",
}

ENVIRONMENTS = {
    "미니멀 스튜디오 — 흰 배경, 깔끔": "pure white minimalist studio, seamless backdrop",
    "두바이 펜트하우스 루프탑 — 야경": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
    "모나코 테라스 — 지중해 야경": "Monaco luxury terrace, Mediterranean night view, superyachts harbor",
    "베르사유 궁전 — 황금빛 홀": "Palace of Versailles golden hall, ornate chandeliers, luxury interior",
    "뉴욕 루프탑 — 맨하탄 야경": "New York City rooftop, Manhattan skyline at night, urban glamour",
    "파리 오스만 발코니 — 에펠탑 뷰": "Paris Haussmann balcony, Eiffel Tower view, golden hour",
    "럭셔리 인피니티 풀 — 열대 리조트": "luxury infinity pool edge, tropical resort, palm trees",
    "산토리니 절벽 — 에게해 야경": "Santorini cliff, blue dome church, Aegean sea at night",
    "말디브 수상빌라 — 크리스탈 바다": "Maldives overwater villa, crystal turquoise sea, tropical paradise",
    "리비에라 절벽 — 지중해 낮": "French Riviera cliff, azure Mediterranean sea, golden sunlight",
    "마이애미 비치 — 선셋": "Miami Beach sunset, Ocean Drive, warm pink sky",
    "럭셔리 요트 덱 — 지중해": "luxury superyacht deck, Mediterranean sea, ocean horizon",
    "도쿄 네온 거리 — 비 오는 밤": "Shinjuku neon-lit rainy alley, Tokyo cyberpunk night",
    "다크 바로크 — 화려한 실내": "dark baroque opulent chamber, velvet and gold interior",
    "파리 패션위크 런웨이 — 모던 무대": "Paris fashion week modernist runway stage, fashion show",
    "사하라 골든아워 — 황금빛 사막": "Sahara desert dunes, golden hour sunset, dramatic sky",
    "화산 절벽 — 극적인 자연": "dramatic volcanic cliff, stormy ocean, powerful nature",
    "얼음 동굴 — 크리스탈 블루": "ice cave interior, crystal blue formations, ethereal light",
    "부다페스트 온천 — 럭셔리 스파, 증기": "Budapest thermal bath, luxury spa pool, steam and warm water",
    "모로코 리야드 — 이슬람 아치, 타일": "Moroccan riad, ornate Islamic arches, colorful mosaic tiles",
    "싱가포르 인피니티 풀 — 마리나베이 뷰": "Singapore Marina Bay Sands infinity pool, city skyline view",
    "발리 정글 빌라 — 열대 럭셔리, 자연": "Bali jungle villa, tropical luxury, lush greenery, infinity pool",
    "모던 럭셔리 맨션 — 현대적 고급 저택": "modern luxury mansion interior, sleek contemporary design, high ceilings",
    "사이버펑크 네온 도시 — 미래 도시 거리": "cyberpunk neon city street, futuristic urban dystopia, neon signs",
    "미래 SF 복도 — 우주선/미래 건물": "futuristic sci-fi corridor, spaceship interior, glowing panels",
    "럭셔리 호텔 스위트 — 펜트하우스 스위트룸": "luxury hotel suite, penthouse bedroom, floor-to-ceiling windows",
    "빗속 도시 거리 — 비 오는 도시, 반사": "rain-soaked urban street, wet pavement reflections, city lights",
    "지중해 해변 마을 — 화이트 빌리지": "Mediterranean seaside village, white-washed buildings, blue sea",
    "자연 폭포 낙원 — 열대 폭포, 자연": "tropical forest waterfall paradise, lush jungle, cascading water",
    "설산 리조트 — 눈 덮인 산, 스키 럭셔리": "snow-covered mountain luxury resort, alpine chalet, winter scenery",
    "우아한 볼룸 — 샹들리에, 대형 파티홀": "elegant grand ballroom, crystal chandeliers, marble floors, opulent",
    "루프탑 도시 스카이라인 — 도시 전경": "rooftop city skyline, panoramic urban view, golden sunset",
    "도쿄 신사 — 일본 전통+현대 융합": "Tokyo Shinto shrine, traditional Japanese architecture, modern city contrast",
    "인도 궁전 — 무굴 건축, 황금빛": "Indian Mughal palace, ornate architecture, golden opulent interior, Taj Mahal inspired",
    "나미비아 사막 — 붉은 모래, 극적": "Namib desert red dunes, dramatic African landscape, surreal orange sky",
    "아이슬란드 빙하 — 오로라, 신비로운": "Iceland glacier, northern lights aurora borealis, mystical arctic landscape",
    "방콕 사원 — 황금 불탑, 이국적": "Bangkok golden temple, ornate Thai architecture, exotic Southeast Asian glamour",
    "마라케시 수크 — 모로코 시장, 컬러풀": "Marrakech souk market, colorful Moroccan bazaar, exotic North African atmosphere",
    "루브르 박물관 — 파리 루브르, 그랜드 갤러리": "The Louvre Museum interior, grand ornate gallery halls, classical artwork on walls, marble floors, Paris luxury",
    # ── 실내 환경 태그 (날씨 충돌 감지용) ──
    "컨트리클럽 — 골프코스, 잔디밭": "country club golf course, manicured green lawn, preppy glamour",
    "테니스 코트 — 클래식 테니스 클럽": "tennis court, classic tennis club, athletic glamour editorial",
}

# 실내 환경 키워드 목록 (날씨 충돌 감지용)
INDOOR_ENVIRONMENTS = {
    "미니멀 스튜디오", "베르사유 궁전", "다크 바로크", "파리 패션위크 런웨이",
    "부다페스트 온천", "모로코 리야드", "모던 럭셔리 맨션", "미래 SF 복도",
    "럭셔리 호텔 스위트", "우아한 볼룸",
}

STYLES = {
    # ── 빅 하우스 ──
    "빅토리아 시크릿 패션쇼": "Victoria's Secret fashion show editorial, VS Angel body, glamorous lingerie runway",
    "스포츠 일러스트레이티드 수영복": "Sports Illustrated swimsuit editorial, luxury beach photography",
    "보그 이탈리아 하이패션": "Vogue Italia high-fashion editorial, avant-garde luxury photography",
    "베르사체 캠페인 — 대담한 럭셔리": "Versace campaign bold luxury glamour, structured couture editorial",
    "하퍼스 바자 — 관능적 에디토리얼": "Harper's Bazaar sensual fashion editorial, cinematic glamour",
    "발렌티노 — 레드 카펫 럭셔리": "Valentino red carpet luxury editorial, haute couture photography",
    "돌체앤가바나 — 이탈리안 글래머": "Dolce and Gabbana Italian glamour, Mediterranean luxury editorial",
    "티에리 뮈글러 — 파워 패션": "Thierry Mugler power fashion editorial, dark haute couture photography",
    "알렉산더 맥퀸 — 드라마틱": "Alexander McQueen dramatic fashion editorial, dark artistic photography",
    "발렌시아가 — 아방가르드 미래적": "Balenciaga avant-garde futuristic editorial, conceptual luxury fashion",
    "샤넬 — 클래식 럭셔리 우아함": "Chanel classic luxury elegance, timeless couture editorial",
    "지방시 — 다크 럭셔리 강렬함": "Givenchy dark luxury editorial, intense couture glamour",
    "발망 — 파워 글래머 구조적": "Balmain power glamour, structured couture editorial, bold luxury",
    "구찌 — 이클레틱 맥시멀리즘": "Gucci eclectic maximalism, bold prints, luxury fashion editorial",
    "프라다 — 지적인 미니멀 럭셔리": "Prada intellectual minimalist luxury, avant-garde editorial",
    "이브 생 로랑 — 록시크 럭셔리": "Yves Saint Laurent rock chic luxury, bold feminine power editorial",
    "버버리 — 브리티시 럭셔리": "Burberry British luxury editorial, classic heritage fashion photography",
    "에르메스 — 절제된 최상급 럭셔리": "Hermes understated ultimate luxury, quiet elegance editorial",
    "로에베 — 아트 럭셔리": "Loewe art luxury editorial, craft-driven fashion photography",
    # ── 캠페인/무드 ──
    "사이버펑크 — 시네마틱": "cyberpunk cinematic fashion photography",
    "스포츠 럭셔리 — 나이키/아디다스 하이엔드": "luxury sports editorial, high-end athletic fashion",
    "나이키 캠페인 — 파워 스포츠": "Nike campaign editorial, powerful athletic presence, sports performance photography",
    "아디다스 오리지널스 — 스트릿 럭셔리": "Adidas Originals street luxury campaign, urban athletic editorial",
    "올드 머니 — 조용한 럭셔리": "old money aesthetic editorial, quiet luxury fashion photography",
    "클린 걸 — 미니멀 뷰티": "clean girl aesthetic editorial, minimalist beauty fashion photography",
    "다크 아카데미아 — 지적 무드": "dark academia aesthetic editorial, intellectual moody fashion photography",
}

# ── 잡지/화보 커버 ──
COVER_STYLES = {
    "없음": "",
    # ── 패션 잡지 ──
    "보그 커버 — 클래식 화이트": "Vogue magazine cover layout, clean white background, direct camera gaze, text space at top, iconic fashion cover composition",
    "하퍼스 바자 커버 — 다크 럭셔리": "Harper's Bazaar magazine cover layout, dark luxury atmosphere, dramatic lighting, high fashion cover editorial",
    "엘르 커버 — 컬러풀 팝": "Elle magazine cover layout, colorful vibrant background, playful glamour, modern fashion cover shot",
    "코스모폴리탄 커버 — 글래머": "Cosmopolitan magazine cover layout, bold glamour, direct eye contact, confident beauty cover composition",
    "W 매거진 커버 — 아방가르드": "W Magazine cover layout, avant-garde artistic composition, bold editorial cover, luxury fashion",
    "누메로 커버 — 아트 에디토리얼": "Numero magazine cover layout, artistic editorial, high concept fashion cover photography",
    "보그 파리 커버 — 프렌치 시크": "Vogue Paris cover layout, French chic, effortless luxury, Parisian fashion cover",
    "아이-D 커버 — 윙크 시그니처": "i-D magazine cover layout, signature wink pose, street fashion cover photography",
    "다즈드 커버 — 실험적": "Dazed magazine cover layout, experimental editorial, boundary-pushing fashion cover",
    "인터뷰 커버 — 아이코닉 팝아트": "Interview magazine cover layout, iconic pop art inspired, bold graphic cover composition",
    # ── 스포츠/피트니스 ──
    "머슬앤피트니스 커버 — 피트니스": "Muscle and Fitness magazine cover layout, athletic glamour, fitness model cover shot, strong confident pose",
    "셰이프 커버 — 건강미": "Shape magazine cover layout, healthy athletic beauty, fitness lifestyle cover, energetic pose",
    "러너스 월드 커버 — 애슬레틱": "Runner's World magazine cover layout, athletic editorial, dynamic running pose, sports lifestyle",
    "수영복 화보 커버 — SI 스타일": "Sports Illustrated swimsuit issue cover layout, luxury beach photography, iconic swimwear cover",
    "피트니스 RX 커버 — 바디빌딩": "Fitness RX magazine cover layout, bodybuilding glamour, competition physique cover shot",
    # ── 라이프스타일/문화 ──
    "내셔널지오그래픽 — 문화/여행": "National Geographic style cover layout, cultural fashion photography, travel lifestyle cover",
    "롤링스톤 커버 — 록스타 글래머": "Rolling Stone magazine cover layout, rock star glamour, bold artistic cover shot",
    "타임 — 파워풀 포트레이트": "Time magazine cover layout, powerful portrait, strong direct gaze, iconic cover composition",
    "플레이보이 빈티지 — 클래식 글래머": "vintage glamour photography cover layout, classic pin-up editorial, retro glamour cover style",
    "GQ 커버 — 하이엔드 글래머": "GQ magazine cover layout, high-end fashion glamour, sophisticated editorial cover",
}

MATERIALS = {
    "리퀴드 새틴 — 액체처럼 흐르는 광택": "liquid satin, ultra-glossy wet-look finish",
    "페이턴트 레더 — 하이글로스 가죽": "shiny patent leather, mirror-like high-gloss surface",
    "메탈릭 비닐 — 금속 광택, 미래적": "reflective metallic vinyl, chrome-like mirror sheen",
    "시스루 오간자 — 반투명, 살이 비치는": "sheer organza, semi-transparent, skin visible beneath",
    "라텍스 — 피부 밀착, 세컨드스킨": "latex second-skin, body-hugging vacuum-seal finish",
    "시퀸 — 빛을 받으면 반짝이는": "iridescent sequins, light-catching glittering surface",
    "웻룩 스판덱스 — 젖은 듯한 느낌": "wet-look spandex, soaking wet appearance, body-hugging",
    "크리스탈 메쉬 — 망사에 크리스탈": "crystal mesh, rhinestone-embellished sheer fabric",
    "벨벳 — 부드럽고 고급스러운": "crushed velvet, rich luxurious texture",
    "골드 포일 — 황금빛 메탈릭": "metallic gold foil, mirror-finish gold surface",
    "크로셰 — 뜨개 수영복, 보헤미안": "crochet knit fabric, handmade boho swimwear style",
    "골드 체인 메쉬 — 금속 체인 망사": "gold chain mail mesh, metallic chainlink fabric",
    "페더 — 깃털 장식, 쇼걸 글래머": "feather-trimmed fabric, showgirl glamour, luxury plumes",
    "니트 — 몸에 딱 붙는 립 니트": "ribbed knit fabric, body-hugging stretch knit",
    "PVC — 투명 비닐, 미래적": "clear PVC vinyl, transparent plastic material, futuristic",
    "데님 — 청바지 소재, 캐주얼 섹시": "denim fabric, sexy denim, casual glamour",
    "시폰 — 가볍고 나풀거리는": "lightweight chiffon fabric, flowing airy drape, soft feminine movement",
    "린넨 — 자연스러운 여름 소재": "natural linen fabric, breathable summer texture, casual luxury",
    "코튼 보일 — 얇고 시원한": "cotton voile fabric, lightweight sheer cotton, fresh summer feel",
    "플로럴 프린트 — 꽃무늬 패턴": "floral printed fabric, botanical pattern, vibrant summer print",
    "트로피컬 프린트 — 열대 패턴": "tropical print fabric, exotic botanical pattern, vacation glamour",
    "타이다이 — 염색 패턴": "tie-dye fabric, hand-dyed swirling pattern, bohemian editorial",
    "스트라이프 — 줄무늬 여름": "classic stripe fabric, nautical or summer stripe pattern, clean editorial",
    "레이스 — 섬세한 레이스 소재": "delicate lace fabric, intricate lacework, feminine luxury texture",
    "테리클로스 — 수건 소재, 해변": "terry cloth fabric, beach towel texture, casual resort glamour",
    "네오프렌 — 탄탄한 구조적": "neoprene fabric, structured sculpting material, modern couture",
}

LIGHTING = {
    "골든아워 — 따뜻한 피부 발광": "golden hour warm backlight, skin luminosity, glowing",
    "옥타박스 스트로브 — 전문 스튜디오": "professional octabox strobe, high-contrast glamour lighting",
    "네온 엣지 — 멀티컬러 네온 빛": "multi-colored neon edge glow, cyberpunk light",
    "키아로스쿠로 — 극적인 명암": "dramatic chiaroscuro, deep shadows and sharp highlights",
    "소프트 뷰티라이트 — 균일하고 부드러운": "soft beauty dish light, even flattering illumination",
    "하드 스트로브 — 바디 정의 강조": "harsh direct strobe, body muscle definition emphasis",
    "볼류메트릭 포그 — 시네마틱 안개빛": "volumetric fog cinematic light, atmospheric mood",
    "림라이트 실루엣 — 역광 실루엣": "strong rim backlight, silhouette definition, halo effect",
    "문라이트 — 달빛, 신비로운 야외": "moonlight, silvery blue natural light, mysterious outdoor glow",
    "네온 핑크 — 핑크 단색 네온": "pink neon accent light, rose-toned atmospheric glow, fashion editorial lighting",
    "파이어 — 불빛, 따뜻한 드라마틱": "firelight, warm flickering flames, dramatic orange glow",
    "수중 반사 — 수영장 물빛 반사": "underwater pool light reflection, rippling aqua light patterns",
    "스플릿 라이팅 — 얼굴 반반 명암": "split lighting, half face light half shadow, dramatic contrast",
}

# ── 프레이밍 (피사체를 얼마나 담느냐) ──
FRAMING = {
    "없음": "",
    "전신샷 — 머리부터 발끝": "full body head-to-toe shot, model fills the entire frame",
    "7/8 샷 — 발목까지": "7/8 shot ankle to head, almost full body",
    "3/4 샷 — 허벅지까지": "3/4 body shot thigh to head",
    "니어샷 — 무릎 위까지": "knee-up editorial shot, three-quarter length composition",
    "웨이스트샷 — 허리 위 상반신": "waist-up cinematic composition",
    "버스트샷 — 가슴 위 상반신": "bust shot chest to head, upper body portrait",
    "클로즈업 — 얼굴+어깨": "close-up beauty shot, face and shoulder emphasis",
    "익스트림 클로즈업 — 얼굴만": "extreme close-up face only, skin texture detail, intimate portrait",
    "디테일샷 — 신체 부위 클로즈업": "detail shot, specific body part close-up, fashion detail emphasis",
    "환경 포트레이트 — 배경+인물 동등": "environmental portrait, subject and background equal emphasis",
    "매거진 커버 — 텍스트 공간 확보": "magazine cover framing, text space at top, iconic cover composition",
}

# ── 카메라 앵글 (카메라 위치/방향) ──
CAMERA_ANGLES = {
    "없음": "",
    "아이레벨 — 정면 수평": "eye level straight-on shot, direct frontal composition",
    "로우앵글 — 아래서 위로": "low angle upward shot, powerful editorial perspective",
    "하이앵글 — 위에서 내려다보기": "cinematic high-angle composition, elevated fashion perspective",
    "버즈아이 — 45도 하이앵글": "45 degree high angle, elegant elevated editorial perspective",
    "더치앵글 — 기울어진 역동적": "dutch angle tilt, dynamic editorial composition",
    "사이드 프로필 — 옆모습": "side profile shot, elegant silhouette from the side",
    "백샷 — 뒤에서 촬영": "back view shot, elegant over-shoulder composition, fashion editorial",
    "쓰리쿼터 앵글 — 45도 정면": "three-quarter angle, 45 degree front view, classic portrait angle",
}

# 전신 강조 프레이밍 (fills frame suffix 제거 대상)
FULLBODY_ANGLES = {"전신샷 — 머리부터 발끝", "7/8 샷 — 발목까지", "3/4 샷 — 허벅지까지", "니어샷 — 무릎 위까지"}
# 클로즈업 프레이밍 (full body suffix 제거 대상)
CLOSEUP_ANGLES = {"클로즈업 — 얼굴+어깨", "익스트림 클로즈업 — 얼굴만", "버스트샷 — 가슴 위 상반신", "웨이스트샷 — 허리 위 상반신"}

# 아트 스타일 목록 (실사 suffix 제거 대상)
ART_IMAGE_STYLES = {
    "오일페인팅 — 유화 회화 느낌",
    "필름누아르 — 1940s 흑백 시네마",
    "팝아트 — 앤디워홀 스타일",
    "수채화 — 부드러운 수채화",
    "만화 — 코믹북 스타일",
    "글리치 아트 — 디지털 왜곡",
    "타블로 — 르네상스 명화 스타일",
}

FOOTWEAR = {
    "없음": "",
    # ── 힐 계열 ──
    "스틸레토 힐 — 극도로 높은 힐": "wearing extreme stiletto heels, legs elongated",
    "메가 플랫폼 스틸레토 — 초두꺼운 플랫폼+힐": "wearing mega platform stiletto heels, extremely thick platform sole with sky-high heel, towering height",
    "플랫폼 힐 — 두꺼운 앞굽 힐": "wearing platform heels, thick platform sole, elevated glamour",
    "청키 힐 — 두꺼운 굵은 힐": "wearing chunky block heels, thick square heel, bold statement",
    "키튼 힐 — 낮고 섬세한 힐": "wearing kitten heels, delicate low heel, refined elegance",
    "웨지 힐 — 쐐기형 힐": "wearing wedge heels, solid wedge sole, casual glamour",
    "포인티드 토 힐 — 뾰족한 앞코 힐": "wearing pointed toe stiletto pumps, classic glamour",
    "스트래피 샌들 힐 — 얇은 끈 샌들": "wearing strappy high heel sandals, elegant feet",
    "뮬 힐 — 뒤가 없는 슬립온": "wearing mule heels, backless slip-on stiletto",
    "크리스탈 힐 — 반짝이는 투명 힐": "wearing crystal clear transparent heels",
    "골드 힐 — 골드 메탈릭 힐": "wearing gold metallic heels, luxury gold stiletto, glamorous",
    "앵클 스트랩 힐 — 발목 끈 힐": "wearing ankle strap heels, elegant ankle wrap",
    # ── 부츠 계열 ──
    "플랫폼 부츠 — 두꺼운 솔 부츠": "wearing platform boots, thick sole, powerful stance",
    "무릎까지 부츠 — 니하이 부츠": "wearing knee-high boots, sleek long legs",
    "허벅지까지 부츠 — 싸이하이 부츠": "wearing thigh-high boots, bold fashion statement",
    "앵클 부츠 — 발목 부츠": "wearing ankle boots, sleek short boots, edgy chic",
    "카우보이 부츠 — 웨스턴 스타일": "wearing cowboy boots, western style, bold fashion statement",
    "PVC 부츠 — 투명 비닐 부츠": "wearing clear PVC transparent boots, futuristic fashion",
    # ── 샌들/플랫 계열 ──
    "글래디에이터 샌들 — 종아리까지 끈": "wearing gladiator sandals, lace-up straps up the calf",
    "플랫폼 샌들 — 두꺼운 플랫폼 샌들": "wearing platform sandals, thick platform sole sandal, summer glamour",
    "슬라이드 샌들 — 오픈토 슬라이드": "wearing slide sandals, open toe slip-on, luxury resort style",
    "맨발 — 자연스러운": "barefoot, natural",
    # ── 스포츠/캐주얼 ──
    "스포츠 스니커즈 — 운동화": "wearing sporty sneakers, athletic shoes, casual glamour",
    "하이탑 스니커즈 — 높은 운동화": "wearing high-top sneakers, bold statement athletic shoes",
    "골프화 — 스포티 골프 슈즈": "wearing golf shoes, sporty footwear, country club style",
    "테니스화 — 클래식 테니스 슈즈": "wearing tennis shoes, classic court shoes, sporty chic",
}

CAMERAS = {
    "하셀블라드 H6D — 80mm f/2.8": "Hasselblad H6D 80mm f/2.8 ISO 100",
    "캐논 EOS R5 — 85mm f/1.2 인물": "Canon EOS R5 85mm f/1.2 portrait lens ISO 100",
    "소니 A7R V — 50mm f/1.4": "Sony A7R V 50mm f/1.4 ISO 100",
    "니콘 Z9 — 85mm f/1.8": "Nikon Z9 85mm f/1.8 ISO 100",
    "페이즈원 XF IQ4 — 110mm f/2.8 중형": "Phase One XF IQ4 110mm f/2.8 medium format ISO 50",
    "라이카 SL2 — 50mm f/1.4 독일 감성": "Leica SL2 50mm f/1.4 Summilux, German precision",
    "후지 GFX 100S — 중형 110mm": "Fujifilm GFX 100S 110mm f/2 medium format",
    "아이폰 시네마틱 — 모바일 시네마틱 모드": "iPhone cinematic mode, natural realistic style",
}

HAIR_STYLES = {
    "없음": "",
    "롱 웨이브 — 긴 웨이브, 볼륨감": "long wavy hair, voluminous waves, flowing",
    "롱 스트레이트 — 긴 생머리, 실키": "long straight silky hair, sleek and smooth",
    "하이 포니테일 — 높은 포니테일, 섹시": "high ponytail, sleek tight ponytail, polished",
    "업스타일 — 올린 머리, 우아한": "elegant updo, sophisticated chignon, classic",
    "단발 — 깔끔한 보브컷": "sleek bob cut, sharp jawline bob",
    "웨이브 하프업 — 반묶음 웨이브": "half-up half-down wavy hair, romantic style",
    "빅 볼륨 — 풍성하고 글래머러스": "big voluminous glamorous hair, full body",
    "웻룩 — 젖은 듯한 윤기": "wet look slicked back hair, glossy and sleek",
    "바람에 날리는 — 역동적인 플로잉": "windswept flowing hair, dynamic movement",
    "브레이드 — 땋은 머리, 보헤미안": "braided hair, bohemian braids, artistic weave",
    "크롭 픽시컷 — 짧고 대담한": "short pixie cut, bold cropped hair, edgy chic",
    "코르넬로 — 뿔 모양 아방가르드": "avant-garde horn updo, sculptural hair art, editorial",
    "프렌치 보브 — 클래식 파리지앵 단발": "French bob, classic Parisian chin-length cut, sleek fringe",
    "울프컷 — 레이어드 섹시 울프": "wolf cut, layered shaggy style, curtain bangs, effortless editorial",
    "스택드 보브 — 뒤짧고 앞긴 엣지 단발": "stacked bob, shorter back longer front, edgy angled cut",
    "컬리 비치웨이브 — 해변 곱슬 웨이브": "curly beach waves, natural tousled curls, sun-kissed texture",
    "슬릭백 올백 — 뒤로 완전히 넘긴": "sleek slicked back hair, pulled back tight, wet gel look",
    "루즈 업도 — 흘러내리는 웨이브 업": "loose romantic updo, soft tendrils falling, undone elegance",
    "스포티 번 — 높은 번 헤어": "high messy bun, sporty topknot, casual athletic chic",
    "사이드 스웹 — 한쪽으로 넘긴 글래머": "side-swept hair, dramatic one-side drape, old Hollywood glamour",
    # ── 브레이드 계열 ──
    "박스 브레이드 — 아프리칸 박스 브레이드": "box braids, African-inspired box braids, bold editorial statement",
    "콘로우 — 두피 밀착 땋기": "cornrow braids, sleek scalp braids, powerful editorial look",
    "브레이드 크라운 — 머리 위 땋은 왕관": "braided crown, crown braid updo, goddess editorial style",
    "보호 스타일 — 점보 트위스트": "jumbo twists, protective style, editorial natural hair",
    # ── 자연 곱슬 계열 ──
    "아프로 — 자연 곱슬 아프로": "natural afro hair, voluminous coil curls, powerful natural beauty",
    "컬리 내추럴 — 자연 곱슬": "natural curly hair, defined coils, fresh natural editorial",
    "롱 컬리 — 긴 곱슬머리": "long curly hair, voluminous cascading curls, romantic editorial",
    # ── 미디엄 길이 ──
    "미디엄 웨이브 — 중간 길이 웨이브": "medium length wavy hair, shoulder-length waves, effortless editorial",
    "미디엄 스트레이트 — 중간 길이 생머리": "medium straight hair, sleek shoulder-length, clean editorial",
    # ── 개성 있는 스타일 ──
    "투블록 — 언더컷 투블록": "undercut two-block haircut, edgy modern style, bold editorial",
    "딥 사이드파트 — 깊은 가르마": "deep side part, dramatic parting, old Hollywood glamour",
    # ── 귀여움/발랄 ──
    "트윈테일 — 양갈래 발랄한": "twin tails, double pigtails, playful cute kawaii hairstyle",
    "사이드 포니 — 한쪽 묶음 발랄": "side ponytail, one-side tied hair, playful casual cute style",
    "낮은 트윈번 — 양쪽 낮은 번": "low twin buns, double low buns, cute playful hairstyle",
    "헤드밴드 업 — 헤드밴드로 올린": "headband pushed back hair, casual cute style, fresh editorial",
}

HAIR_COLORS = {
    "없음": "",
    "블랙 — 짙은 검정": "jet black hair, deep dark black",
    "다크 브라운 — 짙은 갈색": "dark brown hair, rich chocolate brown",
    "라이트 브라운 — 밝은 갈색": "light brown hair, warm caramel brown",
    "골든 블론드 — 황금빛 금발": "golden blonde hair, sun-kissed golden",
    "플래티넘 블론드 — 밝은 백금 금발": "platinum blonde hair, icy white blonde",
    "레드 — 붉은 빨간 머리": "red hair, vibrant auburn red",
    "버건디 — 와인빛 다크 레드": "burgundy hair, deep wine dark red",
    "로즈골드 — 핑크빛 골드": "rose gold hair, pink golden shimmer",
    "오닉스 블루블랙 — 블루 광택 검정": "blue-black hair, onyx with blue sheen",
}

MODEL_COUNT = {
    "1명 — 싱글 모델 (기본)": {"count": 1, "prompt": "A stunning female model"},
    "2명 — 듀오, 두 모델 나란히": {"count": 2, "prompt": "Two stunning female models standing together side by side"},
    "2명 — 듀오, 대비되는 포즈": {"count": 2, "prompt": "Two stunning female models, contrasting poses, one in foreground one behind"},
    "3명 — 트리오, 세 모델": {"count": 3, "prompt": "Three stunning female models posing together, trio fashion editorial"},
    "그룹 — VS 런웨이 그룹샷": {"count": 4, "prompt": "Group of stunning female models on runway, Victoria's Secret fashion show group shot"},
}

ERA = {
    "없음": "",
    "현대 — 2020년대 트렌디": "contemporary 2020s fashion, modern trendy style",
    "레트로 80s — 네온, 빅헤어, 글램록": "retro 1980s fashion, neon colors, big hair, glam rock era",
    "레트로 90s — 슈퍼모델 황금시대": "1990s supermodel era, minimalist chic",
    "빅토리안 — 코르셋, 드라마틱": "Victorian era fashion, dramatic corset, ornate period costume",
    "1920s 플래퍼 — 재즈시대 글래머": "1920s flapper era, art deco glamour, jazz age fashion",
    "미래 2100년 — SF 하이테크": "year 2100 futuristic fashion, high-tech sci-fi costume",
    "고대 그리스 — 여신 드레이핑": "ancient Greek goddess, draped fabric, classical mythology aesthetic",
}

CONCEPT = {
    "없음": "",
    "CEO 글래머 — 파워수트, 강한 여성": "powerful CEO glamour, sharp power suit, dominant businesswoman",
    "악당 빌런 — 다크 글래머, 카리스마": "villain dark glamour, evil seductive charisma, dark queen energy",
    "여전사 — 갑옷+글래머 융합": "warrior goddess, glamorous armor, fierce battle-ready beauty",
    "팝스타 — 무대 의상, 공연 에너지": "pop star stage costume, performance energy, concert glamour",
    "비밀요원 — 스파이 글래머, 미스터리": "secret agent spy glamour, mysterious sleek operative",
    "여신 — 신화적 존재, 초월적 아름다움": "mythological goddess, ethereal divine beauty, supernatural aura",
    "천사 — 천상의 존재": "angel celestial beauty, ethereal divine wings, heavenly glamour",
    "인어 — 바다의 여신": "mermaid ocean goddess, aquatic beauty, sea creature glamour",
    "요정 — 숲의 정령, 에테리얼 판타지": "forest fairy, ethereal fantasy beauty, delicate nature spirit glamour",
    "님프 — 자연의 정령, 신비로운": "nature nymph, mystical forest spirit, ethereal natural beauty",
    "발키리 — 북유럽 전쟁 여신": "Valkyrie Norse warrior goddess, armored glamour, fierce Nordic beauty",
    "사이렌 — 바다 요정, 유혹적": "siren sea enchantress, mysterious oceanic allure, mythological beauty",
    "드래곤 퀸 — 판타지 여왕": "dragon queen, fantasy ruler, powerful mystical sovereignty, fierce glamour",
    "메두사 — 그리스 신화, 강렬한": "Medusa Greek mythology, serpentine beauty, intense powerful gaze",
    "다크 엘프 — 어둠의 정령": "dark elf fantasy beauty, mysterious shadow creature, edgy supernatural elegance",
    "아마조네스 — 전설의 여전사": "Amazon warrior queen, legendary female warrior, fierce battle glamour",
    "선녀 — 천상의 동양 미녀": "celestial Korean Chinese fairy, heavenly Eastern beauty, elegant divine draping",
    "항아 — 달의 여신": "Chang'e moon goddess, Chinese mythology, ethereal lunar beauty",
    "낙신 — 낙수의 여신": "Luoshen river goddess, classical Chinese beauty, elegant divine draping",
    "용녀 — 동양 용의 딸": "dragon princess Eastern mythology, mystical powerful beauty, divine dragon lineage",
    "구미호 — 요염한 여우 정령": "nine-tailed fox spirit, seductive Korean mythology, mysterious fox glamour",
    "백사 — 뱀 정령 글래머": "white snake spirit, Chinese mythology glamour, mystical serpentine beauty",
    "설녀 — 설원의 정령": "Yuki-onna snow spirit, Japanese mythology, icy ethereal winter beauty",
    "경국지색 — 절세 동양 미인": "legendary Eastern beauty, nation-toppling glamour, classical Asian magnificence",
    "클레오파트라 — 이집트 여왕": "Cleopatra Egyptian queen, ancient royal glamour, intense iconic beauty",
    "이슈타르 — 바빌론 사랑의 여신": "Ishtar Babylonian goddess of love, ancient Middle Eastern divine beauty",
    "셰헤라자데 — 천일야화의 신비": "Scheherazade Arabian nights, exotic Middle Eastern storyteller glamour",
    "오슌 — 황금빛 사랑의 여신": "Oshun Yoruba goddess of love, golden African divine beauty, river goddess",
    "예마야 — 바다의 어머니 여신": "Yemaya ocean mother goddess, African mythology, powerful divine femininity",
    "익스첼 — 마야 달의 여신": "Ixchel Mayan moon goddess, ancient Mesoamerican divine beauty",
    "뱀파이어 — 다크 불멸의 존재": "vampire dark immortal beauty, gothic supernatural elegance",
    "마녀 — 마법사 글래머": "witch magical glamour, mystical sorceress, dark magic beauty",
    "릴리스 — 다크 글래머 고대 존재": "Lilith dark ancient beauty, powerful feminine mystique, gothic supernatural allure",
}

SPECIAL_EFFECTS = {
    "없음": "",
    "불꽃 — 주변에 불이 타오르는": "surrounded by flames and fire, dramatic fire effects",
    "물 — 물에 젖거나 물속 장면": "water effects, soaking wet, underwater or water splashing",
    "연기 — 드라이아이스 안개": "dry ice smoke effects, mysterious fog surrounding model",
    "꽃비 — 꽃잎이 날리는": "flower petals raining down, blooming flowers surrounding",
    "번개 — 번개가 치는 배경": "lightning strike background, electric energy, storm effects",
    "우주 — 별빛, 은하수 배경": "galaxy and stars background, cosmic universe, nebula effects",
    "거울 파편 — 깨진 거울 조각": "broken mirror shards floating, glass fragments effect",
    "황금 — 황금 가루가 날리는": "golden dust particles floating, gilded shimmer effect",
    "얼음 — 얼음 결정, 냉기": "ice crystal effects, frozen breath, winter frost magic",
    "네온 빛줄기 — 네온 레이저 빛": "neon laser light beams, colorful light rays cutting through",
}

IMAGE_STYLE = {
    "없음": "",
    "하이퍼리얼 — 극사실주의 사진": "hyperrealistic photography, ultra-detailed photorealism",
    "오일페인팅 — 유화 회화 느낌": "oil painting style, painterly brushstrokes, fine art aesthetic",
    "필름누아르 — 1940s 흑백 시네마": "film noir style, 1940s black and white cinema, dramatic shadows",
    "팝아트 — 앤디워홀 스타일": "pop art style, Andy Warhol inspired, bold graphic colors",
    "수채화 — 부드러운 수채화": "watercolor painting style, soft translucent washes",
    "만화 — 코믹북 스타일": "comic book style, graphic novel illustration, bold outlines",
    "3D 렌더링 — CGI 퀄리티": "3D rendered CGI quality, Unreal Engine photorealistic render",
    "글리치 아트 — 디지털 왜곡": "glitch art effect, digital distortion, cyberpunk pixel corruption",
    "더블 익스포저 — 이중 노출": "double exposure photography, artistic silhouette overlay, fine art editorial",
    "타블로 — 르네상스 명화 스타일": "Renaissance painting tableau, classical masterpiece composition",
}

PROPS = {
    "없음": "",
    "스포츠카 — 페라리/람보르기니": "posing with Ferrari or Lamborghini sports car, luxury supercar",
    "오토바이 — 바이크 위에": "sitting on motorcycle, biker glamour, powerful motorbike",
    "말 — 승마 글래머": "with horse, equestrian glamour, majestic stallion",
    "의자 — 럭셔리 체어 포즈": "with luxury chair, seated or draped over elegant furniture",
    "우산 — 비 오는 날 우산": "holding umbrella in rain, elegant rainy day accessory",
    "꽃다발 — 화려한 꽃": "holding large flower bouquet, floral luxury arrangement",
    "검/칼 — 여전사 무기": "holding sword or blade, warrior weapon, powerful stance",
    "샴페인 — 럭셔리 파티": "holding champagne glass, luxury party celebration",
    "고양이 — 팜므파탈과 고양이": "with elegant cat, femme fatale and feline, mysterious companion",
    "거울 — 손거울 들고": "holding ornate mirror, self-reflection pose, vanity glamour",
    "골프채 — 골프 클럽 포즈": "holding golf club, golf course editorial, sporty glamour",
    "테니스 라켓 — 테니스 포즈": "holding tennis racket, tennis court editorial, athletic chic",
}

MAKEUP = {
    "없음": "",
    "스모키 아이 — 강렬한 눈매": "dramatic smoky eye makeup, dark eyeshadow, intense gaze",
    "누드 글램 — 자연스럽고 섹시한": "nude glam makeup, natural radiant look, glossy lips, subtle glow",
    "레드립 — 클래식 빨간 입술": "classic red lip makeup, bold red lipstick, timeless glamour",
    "글리터 글램 — 반짝이는 파티": "glitter glam makeup, sparkling eyeshadow, festival beauty",
    "노메이크업 — 청순 내추럴": "no-makeup natural look, fresh dewy skin, barely-there beauty",
    "고딕 다크 — 다크 립, 페일 스킨": "gothic dark makeup, black or deep plum lips, pale dramatic skin",
    "메탈릭 아이 — 금속빛 아이섀도우": "metallic eye makeup, chrome silver or gold eyeshadow, futuristic",
    "선번 글로우 — 여름 태양 느낌": "sun-kissed glow makeup, bronzed healthy skin, summer radiance",
    "코랄 핑크 — 발랄하고 귀여운": "coral pink makeup, fresh peachy tones, youthful glow",
    "오렌지 팝 — 트렌디한 컬러풀": "bold orange makeup, trendy color pop, fashion editorial look",
    "캣아이 — 날카로운 아이라인": "sharp cat eye liner, winged eyeliner, feline editorial look",
    "홀로그램 — 아방가르드 미래적": "holographic makeup, iridescent highlights, avant-garde editorial",
}

ACCESSORIES = {
    "없음": "",
    "골드 주얼리 — 목걸이+귀걸이": "gold jewelry set, gold necklace and earrings, luxury accessories",
    "다이아몬드 — 럭셔리 다이아 주얼리": "diamond jewelry, sparkling diamond necklace and earrings, ultra luxury",
    "초커 — 섹시한 목 초커": "choker necklace, edgy couture neck accessory",
    "바디체인 — 몸에 두르는 골드 체인": "gold body chain over clothing, layered over outfit, glamorous fashion jewelry",
    "레이어드 체인 — 여러 겹 목걸이": "layered chain necklaces, multiple gold chains, trendy stacked look",
    "진주 — 클래식 우아한 진주": "pearl jewelry, classic pearl necklace and earrings, timeless elegance",
    "크리스탈 — 반짝이는 크리스탈": "crystal jewelry, sparkling rhinestone accessories, glamorous",
    "귀걸이만 — 드라마틱한 드롭 귀걸이": "statement drop earrings only, dramatic dangling earrings",
    "럭셔리 워치 — 명품 시계": "luxury watch, designer timepiece on wrist, status accessory",
    "팔찌 스택 — 여러 겹 팔찌": "stacked bracelets, multiple bangles and cuffs on wrist",
    "선글라스 — 오버사이즈 명품 선글라스": "oversized designer sunglasses, luxury eyewear, glamorous shades",
    "캣아이 선글라스 — 고양이 눈 선글라스": "cat-eye sunglasses, vintage glamour eyewear, retro chic",
    "스포츠 선글라스 — 애슬레틱 선글라스": "sporty wraparound sunglasses, athletic eyewear, dynamic look",
    "밀짚 모자 — 여름 비치 햇": "straw sun hat, beach summer hat, boho glamour",
    "카우보이 햇 — 웨스턴 스타일": "cowboy hat, western style, bold fashion statement",
    "베레모 — 파리지앵 스타일": "beret hat, Parisian chic, classic French fashion",
    "페도라 — 클래식 페도라": "fedora hat, classic sophisticated hat, timeless glamour",
    "야구모자 — 스트릿 캐주얼": "baseball cap, streetwear casual, sporty chic editorial",
    "터번 — 이국적 헤드랩": "turban headwrap, exotic editorial, bold fashion statement",
    "크라운/왕관 — 여왕 글래머": "jeweled crown tiara, queen glamour, royal luxury editorial",
    "골프 바이저 — 스포티 골프 바이저": "golf visor, sporty sun visor, country club athletic chic",
}

SKIN_TONES = {
    "없음": "",
    "오일드 스킨 — 윤기있는 글로시": "luminous oiled skin, healthy glossy sheen, editorial glow",
    "태닝 — 브론즈 골든 태닝": "bronzed tan skin, golden sun-kissed tan, beach goddess",
    "딥 태닝 — 짙은 초콜릿 태닝": "deep dark tan, rich chocolate bronzed skin, intense tanning",
    "페일 — 창백하고 신비로운": "pale porcelain skin, ethereal fair complexion, mysterious allure",
    "글로우 — 발광하는 빛나는 피부": "luminous glowing skin, radiant inner glow, lit-from-within effect",
    "매트 — 무광 세련된 피부": "matte flawless skin, powdery smooth complexion, editorial finish",
    "듀이 — 촉촉하고 생기있는": "dewy fresh skin, hydrated plump complexion, youthful glow",
    "스웨티 — 운동 후 땀나는 느낌": "athletic glistening skin, post-workout healthy sheen, fitness editorial",
    "프로스티 — 차갑고 얼음같은": "frosty icy skin tone, cold ethereal complexion, winter goddess",
}

BODY_OIL = {
    "없음": "",
    "라이트 글로우 — 자연스러운 윤기": "light natural skin glow, subtle healthy sheen, barely-there luminosity",
    "새틴 글로우 — 새틴처럼 빛나는": "satin skin finish, smooth silky sheen, elegant glow",
    "미디엄 오일 — 적당한 오일감": "medium body oil, moderate skin glistening, healthy oiled appearance",
    "하이 글로스 — 강한 오일, 반짝이는": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
    "익스트림 웻룩 — 물에 젖은 듯한": "extreme wet-look skin, soaking wet glistening appearance, dripping oil effect",
    "선탄 오일 — 골든 태닝 오일": "tanning oil sheen, golden bronzed glistening skin, beach goddess oil",
    "메탈릭 글로스 — 금속빛 광택": "metallic body gloss, chrome-like skin sheen, futuristic metallic finish",
    "스웨티 글로스 — 땀+오일 믹스": "sweaty oiled skin, post-workout glistening, athletic perspiration mixed with oil",
}

# ── 피부 디테일 ──
SKIN_DETAILS = {
    "없음": "",
    # ── 탄 라인 ──
    "비키니 탄 라인 — 희미한 수영복 자국": "subtle bikini tan lines, sun-kissed skin contrast, beach goddess",
    "딥 탄 라인 — 선명한 탄 자국": "defined tan lines, strong swimsuit tan marks, bronzed skin contrast",
    "서퍼 탄 라인 — 자연스러운 서퍼 탄": "natural surfer tan lines, sun-kissed outdoor tanning, beach athletic",
    # ── 주근깨 ──
    "자연 주근깨 — 코+볼 주근깨": "natural freckles across nose and cheeks, sun-kissed freckled skin",
    "골든 주근깨 — 황금빛 주근깨": "golden sun freckles, warm scattered freckles, sun-kissed beauty marks",
    "연한 주근깨 — 희미한 주근깨": "light subtle freckles, barely-there freckles, natural skin texture",
    "짙은 주근깨 — 선명한 주근깨": "heavy freckles, bold freckled skin, strong freckle pattern",
    # ── 피부 결 ──
    "매끄러운 — 완벽하게 매끄러운": "porcelain smooth skin, flawless perfection, editorial finish",
    "자연 결 — 자연스러운 피부 결": "natural skin texture, visible pores, realistic skin detail",
    "보습 광채 — 촉촉한 광채": "hydrated dewy glow, plump moisturized skin, healthy luminosity",
    # ── 특별 마킹 ──
    "버스마크 — 자연스러운 점/마킹": "natural beauty marks, moles, authentic skin markings",
    "스트레치 마크 — 바디 포지티브": "natural stretch marks, body positive skin, authentic beauty",
}

# ── 네일 ──
NAILS = {
    "없음": "",
    # ── 기본 컬러 ──
    "레드 네일 — 클래식 레드": "classic red nail polish, bold red nails, timeless glamour",
    "누드 네일 — 자연스러운 누드": "nude nail polish, natural nail color, subtle elegance",
    "블랙 네일 — 엣지 블랙": "black nail polish, edgy dark nails, bold statement",
    "화이트 네일 — 깔끔한 화이트": "white nail polish, clean minimal nails, fresh editorial",
    "핑크 네일 — 소프트 핑크": "soft pink nail polish, feminine nails, delicate glamour",
    # ── 특별 스타일 ──
    "글리터 네일 — 반짝이는 글리터": "glitter nail polish, sparkly nails, glamorous shimmer",
    "홀로그램 네일 — 홀로그램 효과": "holographic nail polish, iridescent nails, futuristic shimmer",
    "프렌치 네일 — 클래식 프렌치": "French manicure, white tip nails, classic elegance",
    "옴브레 네일 — 그라데이션": "ombre gradient nails, color fade nail art, artistic nails",
    "네일 아트 — 정교한 네일 아트": "intricate nail art design, hand-painted nails, artistic manicure",
    # ── 길이/형태 ──
    "롱 스틸레토 — 길고 뾰족한": "long stiletto nails, sharp pointed tips, dramatic length",
    "롱 아몬드 — 길고 아몬드형": "long almond-shaped nails, elegant curved tips",
    "숏 스퀘어 — 짧은 네모형": "short square nails, clean squared tips, minimal style",
    "발레리나 — 관棺형 발레리나": "coffin-shaped nails, ballerina nails, dramatic length",
}

POSES = {
    "없음": "",
    "파워 스탠딩 — 손 허리, 당당한": "powerful standing pose, hands on hips, confident dominant stance",
    "런웨이 워킹 — 카메라를 향해": "walking confidently toward camera, runway catwalk stride",
    "걸어가는 뒷모습 — 카메라 등지고 걷기": "walking away from camera, back view, confident stride, looking over shoulder",
    "S커브 — 한쪽 다리 구부린 섹시": "S-curve pose, one leg bent, hip tilted, confident fashion stance",
    "크로스 암 — 팔짱 끼고 강렬한": "arms crossed, intense gaze, powerful commanding expression",
    "손 들어 — 머리 위로 손, 관능적": "arms raised above head, elongated elegant pose, arched back, fashion editorial",
    "기둥 포즈 — 기둥 감싸며 기댄": "leaning against pillar, arms resting on column, elegant architectural pose",
    "기댄 포즈 — 벽에 기댄 캐주얼": "leaning against wall, casual confident pose, relaxed editorial stance",
    "창문 기대기 — 창문에 손 짚고 빛 받으며": "leaning against window, hand pressed on glass, backlit silhouette, dreamy glow",
    "차 위 포즈 — 보닛에 기댄 글래머": "leaning on car hood, luxury supercar, confident glamour pose, fashion editorial",
    "앉은 포즈 — 바닥/의자에 우아하게": "seated elegantly, legs crossed, sophisticated sitting pose",
    "땅에 앉기 — 무릎 세우고 바닥에": "sitting on floor, knees drawn up, casual intimate pose",
    "계단 포즈 — 계단에 앉거나 기댄": "seated or leaning on staircase steps, architectural glamour",
    "누운 포즈 — 바닥/침대에 관능적": "lying down pose, reclined elegantly on floor or bed, fashion editorial",
    "엎드린 포즈 — 배를 깔고 관능적": "lying face down, propped on elbows, looking at camera, editorial pose",
    "백포즈 — 뒤돌아 어깨 너머 시선": "back to camera, elegant over-shoulder glance, confident editorial pose",
    "등 보이기 — 백뷰, 어깨 라인": "back view pose, shoulder blade emphasis, elegant fashion editorial",
    "역동적 — 머리카락 날리는 움직임": "dynamic pose, hair flowing in wind, motion blur effect",
    "스트레칭 — 몸을 길게 늘인 유연한": "full body stretch pose, elongated limbs, graceful flexibility, dancer energy",
    "점프 — 공중에 뜬 역동적": "mid-air jump pose, feet off ground, dynamic energy, motion captured",
    "수영장 입수 — 물가에서 다이빙": "standing at pool edge, about to dive, water reflection below",
    "수영장 물속 — 하반신 물에 잠긴": "standing waist-deep in pool, water surface at hips, cinematic pool editorial",
    "욕조 포즈 — 욕조 안 럭셔리": "reclining in luxury bathtub, bubbles or petals, spa glamour",
    "손으로 얼굴 감싸기 — 양손으로 얼굴": "hands framing face, fingers touching cheeks, intimate beauty pose",
    "턱 괴기 — 손으로 턱 받치고": "chin resting on hand, thoughtful editorial gaze, close-up ready",
    "거울 앞 — 거울 반영, 이중 시선": "standing before mirror, reflection visible, double perspective pose",
    # ── 귀여움/발랄 ──
    "브이 포즈 — 손가락 브이, 발랄한": "peace sign V pose, fingers up, playful cute gesture, kawaii editorial",
    "하트 손 — 손가락으로 하트": "finger heart gesture, Korean heart pose, cute playful editorial",
    "양손 볼 감싸기 — 귀엽고 청순한": "both hands cupping face, cute shy pose, adorable innocent editorial",
    "점프 하트 — 공중에서 발랄하게": "jumping with joy, arms spread wide, energetic playful pose, dynamic editorial",
    "머리 위 하트 — 팔로 하트 모양": "arms forming heart shape above head, cute playful pose, fun editorial",
    "등 뒤로 손 — 수줍은 포즈": "hands clasped behind back, shy innocent stance, cute editorial pose",
    # ── 신규 추가 ──
    "무릎 꿇기 — 의식적/신성한 포즈": "kneeling ceremonial pose, knees on floor, hands clasped or raised, sacred ritual energy",
    "측면 포즈 — 옆모습 실루엣": "profile side view, facing sideways, elegant side silhouette, fashion editorial",
    "발레 포즈 — 한 발로 균형 잡는": "ballet arabesque pose, one leg raised, graceful dancer balance, elegant extension",
    "기도 포즈 — 손 모아 위로 올린": "hands pressed together raised above head, devotional prayer pose, spiritual editorial",
    "왕좌 포즈 — 의자에 군림하듯 앉은": "seated on ornate throne chair, commanding regal pose, legs crossed, queen energy",
    "뒤로 기울기 — 아치형으로 몸을 젖힌": "backbend arch pose, spine arched backward, dramatic body curve, dance editorial",
    "앉아서 무릎 안기 — 바닥에 무릎 끌어안고": "sitting on floor, knees drawn to chest, intimate contemplative pose",
    "옆으로 누운 — 사이드뷰로 누운": "lying on side, elegant lateral pose, side profile reclined, fashion editorial",
    "스쿼트 포즈 — 낮게 앉은 역동적": "deep squat pose, low dynamic stance, powerful athletic energy, editorial",
    "기대어 앉기 — 한쪽으로 기울어 앉은": "sitting leaning to one side, relaxed asymmetric pose, casual glamour",
}

WEATHER = {
    "없음": "",
    "맑음 — 강한 햇살, 선명한 그림자": "bright sunny day, strong sunlight, sharp shadows, clear blue sky",
    "골든아워 — 석양 직전 황금빛": "golden hour just before sunset, warm amber light flooding the scene",
    "흐림 — 부드러운 확산광, 무드있는": "overcast sky, soft diffused light, moody atmospheric feel",
    "비 — 빗속, 젖은 바닥 반사": "raining, wet ground reflections, rain droplets, dramatic rain atmosphere",
    "폭우 — 거센 비, 극적인 분위기": "heavy downpour, intense rain, dramatic storm atmosphere",
    "안개 — 신비로운 안개, 몽환적": "dense fog, mysterious misty atmosphere, ethereal soft focus background",
    "눈 — 눈 내리는, 겨울 분위기": "snowfall, snowflakes falling, winter atmosphere, breath visible in cold air",
    "번개/폭풍 — 극적인 폭풍우": "lightning storm, dramatic storm clouds, electric atmosphere, intense weather",
    "바람 — 강한 바람, 옷과 머리 날림": "strong wind, clothes and hair dramatically blown, dynamic wind effect",
    "황사/모래폭풍 — 사막 먼지 분위기": "sandstorm dust haze, desert wind, warm orange dusty atmosphere",
    "무지개 — 비 온 뒤 무지개": "rainbow after rain, fresh air, vibrant colors in sky, hopeful atmosphere",
}

EXPRESSION = {
    "없음": "",
    "도발적 — 강렬하고 유혹적인 눈빛": "intense confident gaze, smoldering eyes, powerful editorial expression",
    "차가운 — 무표정, 냉한 카리스마": "cold expressionless face, icy stare, aloof powerful charisma, stone cold beauty",
    "당당한 — 자신감 넘치는 눈빛": "confident powerful expression, direct commanding gaze, dominant energy",
    "미소 — 부드러운 매혹적 미소": "soft alluring smile, gentle warm expression, approachable glamour",
    "활짝 웃음 — 환한 밝은 미소": "bright radiant smile, joyful expression, teeth showing, infectious happiness",
    "청순 — 순수하고 맑은 눈빛": "fresh youthful expression, wide bright eyes, natural clean beauty, editorial look",
    "신비로운 — 알 수 없는 표정": "mysterious enigmatic expression, knowing look, secretive allure",
    "관능적 — 반쯤 감은 눈, 육감적": "half-lidded eyes, heavy-lidded gaze, deeply expressive editorial look",
    "강렬한 — 눈을 부릅뜨고 압도하는": "intense piercing stare, powerful overwhelming gaze, magnetic eye contact",
    "우수 — 슬프고 몽환적인 눈빛": "melancholic dreamy expression, faraway gaze, wistful beauty",
    "화난 — 강렬한 분노, 악당 느낌": "fierce intense expression, villainous energy, dark powerful aura",
    "입술 벌림 — 입술 살짝 열린": "lips slightly parted, calm sophisticated editorial expression",
    # ── 귀여움/발랄 ──
    "윙크 — 장난스러운 윙크": "playful wink, one eye closed, mischievous cute expression",
    "혀 내밀기 — 발랄하고 귀여운": "tongue sticking out slightly, playful cheeky expression, cute editorial",
    "수줍은 미소 — 청순하고 귀여운": "shy sweet smile, bashful cute expression, innocent beauty",
    "볼 부풀리기 — 귀엽고 유쾌한": "puffed cheeks, playful pouty expression, adorable cute face",
    "깜짝 놀란 — 눈 크게 뜨고 귀여운": "wide-eyed surprised expression, cute shocked face, playful editorial",
}

TATTOO = {
    "없음": "",
    "슬리브 타투 — 한쪽 팔 전체 문신": "full sleeve tattoo on one arm, intricate detailed ink art",
    "목 타투 — 목 옆 작은 문신": "small delicate neck tattoo, side of neck ink",
    "가슴 타투 — 가슴 위 문신": "chest tattoo above collarbone, decorative upper chest ink, fashion editorial",
    "등 타투 — 등 전체 대형 문신": "large back tattoo, full back ink art, intricate spine tattoo",
    "허리 타투 — 허리 옆 타투": "hip waist tattoo, lower side tattoo, artistic placement",
    "손 타투 — 손등/손가락 문신": "hand and finger tattoos, knuckle ink, delicate hand art",
    "꽃 타투 — 플로럴 패턴": "floral tattoo pattern, rose and botanical ink, feminine tattoo art",
    "기하학 타투 — 선명한 기하학적": "geometric tattoo, clean line art, minimalist geometric ink",
    "뱀 타투 — 뱀 문양, 엣지있는": "snake tattoo, serpent ink art, edgy mystical tattoo",
    "천사/악마 타투 — 종교적 아트워크": "angel or demon tattoo, religious iconography ink, dramatic body art",
    "부족 타투 — 폴리네시안/마오리": "tribal tattoo, Polynesian Maori style ink, bold black patterns",
    "전신 바디페인팅 — 몸에 그림": "full body painting art, painted skin, artistic body art canvas",
    "전신 커버 타투 — 머리부터 발끝 빽빽한 타투": "full body tattoo coverage, head-to-toe intricate tattoo artwork, densely tattooed skin, tattoo collector aesthetic, heavily inked from neck to toe",
    "이레즈미 전신 — 일본 전통 전신 타투": "Japanese irezumi full body tattoo, traditional Japanese ink art, full body coverage, intricate cultural patterns",
}

BG_CROWD = {
    "없음": "",
    "완전 단독 — 배경에 아무도 없음": "completely alone, empty background, solitary subject, no other people",
    "흐릿한 군중 — 배경에 흐릿한 사람들": "blurred crowd in background, busy environment, bokeh people, social scene",
    "런웨이 관중 — 패션쇼 관중석": "fashion show audience in background, runway crowd, photographers flashing",
    "파티 군중 — 화려한 파티 배경": "glamorous party crowd in background, celebratory atmosphere, luxury event",
    "도시 행인 — 거리의 지나가는 사람들": "urban pedestrians blurred in background, busy city street life",
    "해변 군중 — 해변의 사람들": "beach crowd in background, summer beach scene, vacationers blurred",
    "두 명 — 다른 모델 한 명 배경에": "another model blurred in background, duo scene, second figure",
    "그림자 인물 — 배경에 실루엣만": "shadowy silhouette figures in background, mysterious dark outlines",
}

COLOR_GRADES = {
    "없음": "",
    "흑백 — 클래식 모노크롬": "black and white photography, classic monochrome, high contrast B&W",
    "시네마틱 틸 & 오렌지 — 영화적": "cinematic teal and orange color grade, Hollywood film look",
    "골든 — 따뜻한 황금빛 필름": "warm golden film grade, vintage golden hour tone",
    "다크 무드 — 어둡고 드라마틱": "dark moody color grade, deep shadows, dramatic contrast",
    "쿨 블루 — 차갑고 세련된": "cool blue color grade, cold steel tones, sleek editorial",
    "핑크 글램 — 핑크빛 글래머": "soft pink glamour grade, rose gold tones, feminine glow",
    "하이키 — 밝고 화사한 흰빛": "high key bright white tone, overexposed glamour, clean light",
    "빈티지 필름 — 필름 느낌": "vintage film grain, faded colors, analog photography look",
    "퍼플 무드 — 보라빛 신비로운": "purple moody color grade, violet atmospheric tones, mysterious glow",
    "에메랄드 — 초록빛 럭셔리": "emerald green color grade, rich jewel tones, luxury editorial",
    "세피아 — 따뜻한 앤티크": "sepia tone, warm antique finish, nostalgic editorial",
}

MOOD = {
    "없음": "",
    "다크 글래머 — 어둡고 강렬한": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
    "몽환적 — 꿈결같은 부드러운": "dreamy ethereal mood, soft romantic atmosphere, fantasy editorial",
    "하이패션 에디토리얼 — 차갑고 세련된": "high fashion editorial mood, cold sophisticated atmosphere, sharp luxury",
    "보헤미안 — 자유롭고 자연스러운": "bohemian free-spirited mood, natural earthy atmosphere, artistic editorial",
    "레트로 핀업 — 복고풍 글래머": "retro pin-up mood, vintage glamour atmosphere, classic playful editorial",
    "사이버펑크 글램 — 미래적 어두운": "cyberpunk glamour mood, futuristic neon atmosphere, dystopian editorial",
    "로맨틱 — 부드럽고 따뜻한": "romantic mood, soft warm atmosphere, tender feminine editorial",
    "파워풀 — 강렬하고 압도적인": "powerful commanding mood, intense dominant atmosphere, fierce editorial",
    "미스터리 — 신비롭고 매혹적": "mysterious alluring mood, enigmatic atmosphere, captivating editorial",
    "럭셔리 — 고급스럽고 우아한": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
    "플레이풀 — 발랄하고 생기있는": "playful vibrant mood, energetic joyful atmosphere, fresh editorial",
    "세레니티 — 평화롭고 고요한": "serene tranquil mood, peaceful calm atmosphere, meditative editorial",
}

TIME_OF_DAY = {
    "없음": "",
    "새벽 블루아워 — 해뜨기 직전 신비로운": "blue hour just before dawn, mystical pre-sunrise light, cool blue atmospheric glow",
    "골든아워 아침 — 이른 아침 햇살": "morning golden hour, soft warm early sunlight, fresh dewy atmosphere",
    "정오 — 강한 직사광선 선명한": "midday harsh sunlight, strong direct light, sharp shadows, high contrast",
    "오후 — 따뜻한 햇살 여유로운": "late afternoon warm sunlight, relaxed golden atmosphere, soft shadows",
    "황혼 — 해질 무렵 드라마틱": "dusk twilight, dramatic sunset colors, sky ablaze with color",
    "심야 — 완전한 어둠 신비로운": "deep midnight, complete darkness, mysterious nocturnal atmosphere",
    "오로라 — 북극광 신비로운 밤": "aurora borealis night, northern lights dancing, mystical arctic atmosphere",
}

LENS_EFFECT = {
    "없음": "",
    "얕은 심도 — 배경 극도 흐림": "extremely shallow depth of field, background heavily blurred, subject sharp",
    "렌즈플레어 — 빛 번짐 효과": "dramatic lens flare, light streaks and halos, cinematic sun flare effect",
    "소프트포커스 — 몽환적 흐림": "soft focus dreamy effect, gentle blur, ethereal soft glow",
    "틸트시프트 — 미니어처 효과": "tilt-shift effect, selective focus, miniature world aesthetic",
    "어안렌즈 — 왜곡된 광각": "fisheye lens distortion, ultra wide angle, dramatic perspective warp",
    "롱렌즈 압축 — 배경 압축 효과": "telephoto lens compression, background dramatically compressed, intimate portrait",
    "프리즘 효과 — 무지개 빛 분산": "prism glass effect, rainbow light dispersion, colorful light refraction",
    "빈티지 렌즈 — 필름카메라 감성": "vintage lens rendering, slight vignette, period-accurate optical character",
}