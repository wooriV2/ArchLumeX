"""
LumineX core/builders.py
플랫폼별 프롬프트 빌더 함수
"""
from core.data import (
    MODEL_APPEARANCE, AGE_APPEARANCE, MODEL_TYPES, BODY_WEIGHT, BUST_SIZE, HIP_SIZE,
    OUTFIT_TYPES, MATERIALS, ENVIRONMENTS, STYLES, COVER_STYLES, LIGHTING, CAMERA_ANGLES, FRAMING,
    FOOTWEAR, CAMERAS, HAIR_STYLES, HAIR_COLORS, MODEL_COUNT, ERA, CONCEPT,
    SPECIAL_EFFECTS, IMAGE_STYLE, PROPS, MAKEUP, ACCESSORIES, SKIN_TONES,
    POSES, WEATHER, EXPRESSION, TATTOO, BODY_OIL, BG_CROWD, COLOR_GRADES, ASPECT_RATIOS,
    MOOD, TIME_OF_DAY, LENS_EFFECT,
    SKIN_DETAILS, NAILS,
    ART_IMAGE_STYLES, FULLBODY_ANGLES, CLOSEUP_ANGLES,
)

# ── 실사 suffix 키워드 ──
REALISM_SUFFIX = "photorealistic, RAW photo, hyperrealistic, natural skin texture, pore detail, film grain, professional photographer"
REALISM_KEYWORDS = ["photorealistic", "RAW photo", "hyperrealistic", "natural skin texture", "pore detail", "film grain"]


def _is_art_style(image_style: str) -> bool:
    """아트 스타일 여부 판단"""
    return image_style in ART_IMAGE_STYLES


# ── 바디페인팅 판별 (의상 오인식 방지용) ──
BODYPAINT_KEYWORDS = [
    "body paint", "painted on bare skin", "painted directly", "trompe",
    "no clothing", "no fabric", "painted illusion", "body art",
    "stencil", "expressionist patterns painted", "motifs painted",
    "painted across body", "patterns painted",
]

def _is_bodypaint(outfit_text: str, material_text: str = "") -> bool:
    """outfit/material 텍스트에 바디페인팅 신호가 있으면 True"""
    combined = f"{outfit_text} {material_text}".lower()
    return any(kw.lower() in combined for kw in BODYPAINT_KEYWORDS)


def _build_wearing_line(outfit_wearing: str, material_text: str, footwear: str) -> str:
    """
    바디페인팅이면 'Body fully painted with:' + 맨발 강제,
    일반 의상이면 기존 'Wearing:' 포맷 반환
    """
    if _is_bodypaint(outfit_wearing, material_text):
        return (
            f"Body fully painted with: {outfit_wearing}. "
            f"The entire design is body paint pigment applied directly on bare skin, "
            f"NOT clothing, NOT fabric, painted with {material_text}. Barefoot."
        )
    else:
        return f"Wearing: {outfit_wearing}, made of {material_text}{', ' + footwear if footwear else ''}."


def _build_wearing_phrase_chatgpt(outfit_wearing: str, material_text: str, footwear: str) -> str:
    """ChatGPT 빌더용 wearing 구문 (문장 중간 삽입형)"""
    if _is_bodypaint(outfit_wearing, material_text):
        return (
            f"Body fully painted with {outfit_wearing}, "
            f"the entire design is body paint pigment on bare skin, NOT clothing, NOT fabric, "
            f"painted with {material_text}, barefoot. "
        )
    else:
        return f"Wearing {outfit_wearing}, crafted from {material_text}{', ' + footwear if footwear else ''}. "


def _get_frame_suffix(framing: str, angle: str = "") -> str:
    """
    프레이밍에 따라 suffix 자동 조정
    - 전신샷: 'model fills the entire frame' 유지
    - 클로즈업: 'close-up portrait framing' 사용
    - 기타: 기본
    """
    if framing in FULLBODY_ANGLES:
        return "model fills the entire frame"
    elif framing in CLOSEUP_ANGLES:
        return "intimate close-up portrait framing"
    elif angle in FULLBODY_ANGLES:
        return "model fills the entire frame"
    elif angle in CLOSEUP_ANGLES:
        return "intimate close-up portrait framing"
    else:
        return "model fills the entire frame"


def build_gemini_prompt(data: dict, aspect: str, realism: bool) -> str:
    aspect_desc   = ASPECT_RATIOS.get(aspect, "")
    image_style_key = data.get('image_style', '없음')
    is_art        = _is_art_style(image_style_key)

    # ── 2번: 아트 스타일이면 실사 suffix 제거 ──
    if realism and not is_art:
        realism_kw = REALISM_SUFFIX
    else:
        realism_kw = ""

    appearance    = MODEL_APPEARANCE.get(data.get('appearance', ''), '')
    age           = AGE_APPEARANCE.get(data.get('age', ''), '')
    outfit_data   = OUTFIT_TYPES[data['outfit']]
    outfit        = outfit_data["gemini"] if isinstance(outfit_data, dict) else outfit_data
    footwear      = FOOTWEAR.get(data.get('footwear', ''), '')
    pose          = POSES.get(data.get('pose', ''), '')
    color_grade   = COLOR_GRADES.get(data.get('color_grade', ''), '')
    hair_style    = HAIR_STYLES.get(data.get('hair_style', ''), '')
    hair_color    = HAIR_COLORS.get(data.get('hair_color', ''), '')
    hair_str      = " ".join(filter(None, [hair_color, hair_style]))
    makeup        = MAKEUP.get(data.get('makeup', ''), '')
    accessories   = ACCESSORIES.get(data.get('accessories', ''), '')
    skin_tone     = SKIN_TONES.get(data.get('skin_tone', ''), '')
    count_data    = MODEL_COUNT.get(data.get('model_count', '1명 — 싱글 모델 (기본)'), MODEL_COUNT['1명 — 싱글 모델 (기본)'])
    model_subject = count_data['prompt']
    era           = ERA.get(data.get('era', ''), '')
    concept       = CONCEPT.get(data.get('concept', ''), '')
    special_fx    = SPECIAL_EFFECTS.get(data.get('special_effects', ''), '')
    img_style     = IMAGE_STYLE.get(image_style_key, '')
    props         = PROPS.get(data.get('props', ''), '')
    body_weight   = BODY_WEIGHT.get(data.get('body_weight', ''), '')
    bust_size     = BUST_SIZE.get(data.get('bust_size', ''), '')
    hip_size      = HIP_SIZE.get(data.get('hip_size', ''), '')
    body_str      = ", ".join(filter(None, [body_weight, bust_size, hip_size]))
    weather       = WEATHER.get(data.get('weather', ''), '')
    expression    = EXPRESSION.get(data.get('expression', ''), '')
    tattoo        = TATTOO.get(data.get('tattoo', ''), '')
    body_oil      = BODY_OIL.get(data.get('body_oil', ''), '')
    bg_crowd      = BG_CROWD.get(data.get('bg_crowd', ''), '')
    mood          = MOOD.get(data.get('mood', ''), '')
    time_of_day   = TIME_OF_DAY.get(data.get('time_of_day', ''), '')
    lens_effect   = LENS_EFFECT.get(data.get('lens_effect', ''), '')
    skin_detail   = SKIN_DETAILS.get(data.get('skin_detail', ''), '')
    nails         = NAILS.get(data.get('nails', ''), '')

    # ── 4번: 앵글별 frame suffix ──
    angle_key    = data.get('angle', '없음')
    angle_val    = CAMERA_ANGLES.get(angle_key, '') if angle_key != '없음' else ''
    framing_key  = data.get('framing', '없음')
    framing_val  = FRAMING.get(framing_key, '') if framing_key != '없음' else ''
    frame_suffix = _get_frame_suffix(framing_key, angle_key)

    # ── 상하의 분리 조합 처리 ──
    top_val    = data.get('top_type', '')
    bottom_val = data.get('bottom_type', '')
    if top_val and bottom_val:
        from core.data import TOP_TYPES, BOTTOM_TYPES
        top_text    = TOP_TYPES.get(top_val, '')
        bottom_text = BOTTOM_TYPES.get(bottom_val, '')
        outfit_wearing = f"{top_text}, {bottom_text}" if top_text and bottom_text else outfit
    else:
        outfit_wearing = outfit

    # ── 바디페인팅이면 "Wearing:" 대신 "Body painted:" + 맨발 강제 ──
    material_text = MATERIALS[data['material']]
    wearing_line = _build_wearing_line(outfit_wearing, material_text, footwear)

    framing_prefix = f"{framing_val}, " if framing_val else ""
    angle_prefix   = f"{angle_val}, " if angle_val else ""

    parts = [
        f"Professional fashion photograph, {framing_prefix}{angle_prefix}{frame_suffix}.",
        f"{model_subject}: {MODEL_TYPES[data['model']]}{', ' + appearance if appearance else ''}.",
        f"Age: {age}." if age else "",
        f"Body adjustment: {body_str}." if body_str else "",
        f"Era: {era}." if era else "",
        f"Concept: {concept}." if concept else "",
        f"Mood: {mood}." if mood else "",
        f"Expression: {expression}." if expression else "",
        f"Skin: {skin_tone}." if skin_tone else "",
        f"Body oil: {body_oil}." if body_oil else "",
        f"Tattoo/Body art: {tattoo}." if tattoo else "",
        f"Skin detail: {skin_detail}." if skin_detail else "",
        f"Nails: {nails}." if nails else "",
        f"Hair: {hair_str}." if hair_str else "",
        f"Makeup: {makeup}." if makeup else "",
        f"Accessories: {accessories}." if accessories else "",
        f"Props: {props}." if props else "",
        f"Pose: {pose}." if pose else "",
        wearing_line,
        f"Environment: {ENVIRONMENTS[data['env']]}, background softly blurred bokeh.",
        f"Time of day: {time_of_day}." if time_of_day else "",
        f"Weather: {weather}." if weather else "",
        f"Background: {bg_crowd}." if bg_crowd else "",
        f"Special effects: {special_fx}." if special_fx else "",
        f"Lighting: {LIGHTING[data['light']]}.",
        f"Lens effect: {lens_effect}." if lens_effect else "",
        f"Style reference: {STYLES[data['style']]}.",
        f"Image style: {img_style}." if img_style else "",
        f"Camera: {CAMERAS[data['camera']]}, sharp focus on model.",
        f"Color grade: {color_grade}." if color_grade else "",
    ]
    suffix = []
    if realism_kw:
        suffix.append(realism_kw)
    if aspect_desc:
        suffix.append(aspect_desc)
    suffix.append("model is the primary subject, elegant editorial framing, background secondary")
    return " ".join(filter(None, parts)) + " " + ", ".join(suffix) + "."


def build_chatgpt_prompt(data: dict, aspect: str) -> str:
    aspect_map    = {
        "세로 2:3 — 인물 기본 ★": "vertical portrait 2:3",
        "세로 9:16 — 모바일/릴스": "vertical portrait 9:16, mobile format",
        "세로 3:4 — 전신샷": "vertical portrait 3:4",
        "세로 4:5 — 인스타 세로": "vertical portrait 4:5",
        "정방형 1:1 — 인스타 피드": "square format 1:1",
        "가로 16:9 — 시네마틱 와이드": "wide cinematic 16:9",
        "가로 4:3 — 화보/매거진": "wide editorial 4:3",
        "가로 3:2 — 클래식 가로": "wide classic 3:2",
        "가로 2:1 — 파노라마": "wide panoramic 2:1",
        "가로 21:9 — 울트라와이드": "ultrawide cinematic 21:9",
    }
    aspect_desc   = aspect_map.get(aspect, "vertical portrait 2:3")
    image_style_key = data.get('image_style', '없음')
    is_art        = _is_art_style(image_style_key)

    appearance    = MODEL_APPEARANCE.get(data.get('appearance', ''), '')
    age           = AGE_APPEARANCE.get(data.get('age', ''), '')
    model         = MODEL_TYPES[data['model']]
    outfit_data   = OUTFIT_TYPES[data['outfit']]
    outfit        = outfit_data["chatgpt"] if isinstance(outfit_data, dict) else outfit_data
    material      = MATERIALS[data['material']]
    env           = ENVIRONMENTS[data['env']]
    light         = LIGHTING[data['light']]
    style         = STYLES[data['style']]
    camera        = CAMERAS[data['camera']]
    angle_key     = data.get('angle', '없음')
    angle         = CAMERA_ANGLES.get(angle_key, '') if angle_key != '없음' else ''
    framing_key   = data.get('framing', '없음')
    framing_val   = FRAMING.get(framing_key, '') if framing_key != '없음' else ''
    footwear      = FOOTWEAR.get(data.get('footwear', ''), '')
    pose          = POSES.get(data.get('pose', ''), '')
    color_grade   = COLOR_GRADES.get(data.get('color_grade', ''), '')
    hair_style    = HAIR_STYLES.get(data.get('hair_style', ''), '')
    hair_color    = HAIR_COLORS.get(data.get('hair_color', ''), '')
    hair_str      = " ".join(filter(None, [hair_color, hair_style]))
    makeup        = MAKEUP.get(data.get('makeup', ''), '')
    accessories   = ACCESSORIES.get(data.get('accessories', ''), '')
    skin_tone     = SKIN_TONES.get(data.get('skin_tone', ''), '')
    count_data    = MODEL_COUNT.get(data.get('model_count', '1명 — 싱글 모델 (기본)'), MODEL_COUNT['1명 — 싱글 모델 (기본)'])
    model_subject = count_data['prompt']
    era           = ERA.get(data.get('era', ''), '')
    concept       = CONCEPT.get(data.get('concept', ''), '')
    special_fx    = SPECIAL_EFFECTS.get(data.get('special_effects', ''), '')
    img_style     = IMAGE_STYLE.get(image_style_key, '')
    props         = PROPS.get(data.get('props', ''), '')
    body_weight   = BODY_WEIGHT.get(data.get('body_weight', ''), '')
    bust_size     = BUST_SIZE.get(data.get('bust_size', ''), '')
    hip_size      = HIP_SIZE.get(data.get('hip_size', ''), '')
    body_str      = ", ".join(filter(None, [body_weight, bust_size, hip_size]))
    weather       = WEATHER.get(data.get('weather', ''), '')
    expression    = EXPRESSION.get(data.get('expression', ''), '')
    tattoo        = TATTOO.get(data.get('tattoo', ''), '')
    body_oil      = BODY_OIL.get(data.get('body_oil', ''), '')
    bg_crowd      = BG_CROWD.get(data.get('bg_crowd', ''), '')
    mood          = MOOD.get(data.get('mood', ''), '')
    time_of_day   = TIME_OF_DAY.get(data.get('time_of_day', ''), '')
    lens_effect   = LENS_EFFECT.get(data.get('lens_effect', ''), '')
    skin_detail   = SKIN_DETAILS.get(data.get('skin_detail', ''), '')
    nails         = NAILS.get(data.get('nails', ''), '')
    appearance_desc = f"with {appearance}" if appearance else ""

    # ── 4번: 앵글별 frame suffix ──
    frame_suffix = _get_frame_suffix(framing_key, angle_key)

    # ── 상하의 분리 조합 처리 ──
    top_val    = data.get('top_type', '')
    bottom_val = data.get('bottom_type', '')
    if top_val and bottom_val:
        from core.data import TOP_TYPES, BOTTOM_TYPES
        top_text    = TOP_TYPES.get(top_val, '')
        bottom_text = BOTTOM_TYPES.get(bottom_val, '')
        outfit_wearing = f"{top_text}, {bottom_text}" if top_text and bottom_text else outfit
    else:
        outfit_wearing = outfit

    # ── 바디페인팅이면 "Wearing" 대신 "Body painted" + 맨발 강제 ──
    wearing_phrase = _build_wearing_phrase_chatgpt(outfit_wearing, material, footwear)

    # ── 2번: 아트 스타일이면 실사 suffix 제거 ──
    if is_art:
        realism_suffix = img_style  # 아트 스타일 설명만
        quality_suffix = "award-winning fashion photography."
    else:
        realism_suffix = "Photorealistic, hyperrealistic skin texture, cinematic realism, award-winning fashion photography."
        quality_suffix = ""

    framing_prefix = f"{framing_val}, " if framing_val else ""
    angle_prefix   = f"{angle}, " if angle else ""

    return (
        f"Professional luxury fashion editorial photograph, {aspect_desc}, {framing_prefix}{angle_prefix}{frame_suffix}. "
        f"{model_subject} {appearance_desc}, {model}, elegant couture presence. "
        f"{'Age: ' + age + '. ' if age else ''}"
        f"{'Body: ' + body_str + '. ' if body_str else ''}"
        f"{'Era: ' + era + '. ' if era else ''}"
        f"{'Concept: ' + concept + '. ' if concept else ''}"
        f"{'Mood: ' + mood + '. ' if mood else ''}"
        f"{'Expression: ' + expression + '. ' if expression else ''}"
        f"{'Skin: ' + skin_tone + '. ' if skin_tone else ''}"
        f"{'Body oil: ' + body_oil + '. ' if body_oil else ''}"
        f"{'Tattoo: ' + tattoo + '. ' if tattoo else ''}"
        f"{'Hair: ' + hair_str + '. ' if hair_str else ''}"
        f"{'Makeup: ' + makeup + '. ' if makeup else ''}"
        f"{'Accessories: ' + accessories + '. ' if accessories else ''}"
        f"{'Props: ' + props + '. ' if props else ''}"
        f"{'Pose: ' + pose + '. ' if pose else ''}"
        f"{wearing_phrase}"
        f"Scene at {env}, {'Time: ' + time_of_day + '. ' if time_of_day else ''}"
        f"{'Weather: ' + weather + '. ' if weather else ''}"
        f"{'Background: ' + bg_crowd + '. ' if bg_crowd else ''}"
        f"{'Special effects: ' + special_fx + '. ' if special_fx else ''}"
        f"bathed in {light}. "
        f"{'Lens effect: ' + lens_effect + '. ' if lens_effect else ''}"
        f"{'Image style: ' + img_style + '. ' if img_style else ''}"
        f"Style of {style}, captured on {camera}. "
        f"{'Color grade: ' + color_grade + '. ' if color_grade else ''}"
        f"{realism_suffix}"
    )


def build_midjourney_prompt(data: dict, aspect: str) -> str:
    ar_map        = {
        "세로 2:3 — 인물 기본 ★": "2:3",
        "세로 9:16 — 모바일/릴스": "9:16",
        "세로 3:4 — 전신샷": "3:4",
        "세로 4:5 — 인스타 세로": "4:5",
        "정방형 1:1 — 인스타 피드": "1:1",
        "가로 16:9 — 시네마틱 와이드": "16:9",
        "가로 4:3 — 화보/매거진": "4:3",
        "가로 3:2 — 클래식 가로": "3:2",
        "가로 2:1 — 파노라마": "2:1",
        "가로 21:9 — 울트라와이드": "21:9",
    }
    ar            = ar_map.get(aspect, "2:3")
    appearance    = MODEL_APPEARANCE.get(data.get('appearance', ''), '').split(',')[0]
    model_short   = MODEL_TYPES[data['model']].split(',')[0]
    outfit_data   = OUTFIT_TYPES[data['outfit']]
    outfit_full   = (outfit_data["chatgpt"] if isinstance(outfit_data, dict) else outfit_data)
    outfit_short  = outfit_full.split(',')[0]
    material_short = MATERIALS[data['material']].split(',')[0]
    env_short     = ENVIRONMENTS[data['env']].split(',')[0]
    light_short   = LIGHTING[data['light']].split(',')[0]
    style_short   = STYLES[data['style']].split(',')[0]
    footwear_short = FOOTWEAR.get(data.get('footwear', ''), '').split(',')[0]
    image_style_key = data.get('image_style', '없음')
    is_art        = _is_art_style(image_style_key)

    # ── 바디페인팅이면 의상 태그를 body paint로 치환 + footwear 제거 ──
    if _is_bodypaint(outfit_full, MATERIALS[data['material']]):
        outfit_short = f"full body paint, {outfit_short}, painted on bare skin not clothing"
        footwear_short = "barefoot"

    tags = [t for t in [
        appearance, model_short, outfit_short, material_short, footwear_short,
        env_short, light_short, style_short,
    ] if t]

    if is_art:
        img_style_short = IMAGE_STYLE.get(image_style_key, '').split(',')[0]
        if img_style_short:
            tags.append(img_style_short)
    else:
        tags.extend(["photorealistic", "hyperrealistic", "fashion editorial", "sharp focus", "8K"])

    return f"{', '.join(tags)} --ar {ar} --style raw --q 2"