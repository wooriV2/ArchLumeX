"""
ArchLumeX core/builders.py
건축/인테리어 AI 이미지 프롬프트 빌더
플랫폼: Gemini / ChatGPT (DALL-E) / Midjourney
"""

from core.data import ASPECT_RATIOS, INDOOR_SPACES


def _is_indoor(space_type: str) -> bool:
    """실내 공간 여부 판별 (날씨 충돌 방지)"""
    for indoor_key in INDOOR_SPACES:
        if indoor_key in space_type:
            return True
    return False


def _build_exterior_line(data: dict) -> str:
    """실외 프롬프트 핵심 라인 조합"""
    parts = []

    building = data.get("building_type", "")
    style = data.get("arch_style", "")
    material = data.get("ext_material", "")
    roof = data.get("roof_style", "")
    landscape = data.get("landscaping", "")

    if building:
        parts.append(f"Building: {building}.")
    if style:
        parts.append(f"Architectural style: {style}.")
    if material:
        parts.append(f"Exterior material: {material}.")
    if roof:
        parts.append(f"Roof: {roof}.")
    if landscape:
        parts.append(f"Landscaping: {landscape}.")

    return " ".join(parts)


def _build_interior_line(data: dict) -> str:
    """실내 프롬프트 핵심 라인 조합"""
    parts = []

    space = data.get("space_type", "")
    style = data.get("int_style", "")
    material = data.get("int_material", "")
    furniture = data.get("furniture_style", "")
    palette = data.get("color_palette", "")
    features = data.get("special_features", "")

    if space:
        parts.append(f"Space: {space}.")
    if style:
        parts.append(f"Interior style: {style}.")
    if material:
        parts.append(f"Materials and finishes: {material}.")
    if furniture and furniture != "없음 — 빈 공간/건축 위주":
        parts.append(f"Furniture: {furniture}.")
    if palette:
        parts.append(f"Color palette: {palette}.")
    if features and features != "없음":
        parts.append(f"Special features: {features}.")

    return " ".join(parts)


def _build_common_line(data: dict, mode: str) -> str:
    """공통 요소 조합 (조명/날씨/시간대/무드/카메라)"""
    parts = []

    lighting = data.get("lighting", "")
    time_of_day = data.get("time_of_day", "")
    weather = data.get("weather", "")
    camera_angle = data.get("camera_angle", "")
    color_grade = data.get("color_grade", "")
    mood = data.get("mood", "")
    camera = data.get("camera", "")
    render_style = data.get("render_style", "")

    # 실내면 날씨 제외
    is_indoor = mode == "interior"
    space_type = data.get("space_type", "")
    if _is_indoor(space_type):
        is_indoor = True

    if lighting:
        parts.append(f"Lighting: {lighting}.")
    if time_of_day and time_of_day != "없음":
        parts.append(f"Time: {time_of_day}.")
    if weather and weather != "없음" and not is_indoor:
        parts.append(f"Weather: {weather}.")
    if camera_angle and camera_angle != "없음":
        parts.append(f"Camera angle: {camera_angle}.")
    if color_grade and color_grade != "없음":
        parts.append(f"Color grade: {color_grade}.")
    if mood and mood != "없음":
        parts.append(f"Mood: {mood}.")
    if camera:
        parts.append(f"Shot on {camera}.")
    if render_style:
        parts.append(f"Render style: {render_style}.")

    return " ".join(parts)


def build_gemini_prompt(data: dict, aspect_ratio: str, mode: str = "exterior") -> str:
    """
    Gemini용 자연어 서술형 프롬프트 빌더
    mode: 'exterior' | 'interior'
    """
    aspect_desc = ASPECT_RATIOS.get(aspect_ratio, "portrait 2:3 vertical")

    # 프리셋 기반 프롬프트가 있으면 우선 사용
    preset_prompt = data.get("preset_prompt", "")
    if preset_prompt:
        return f"{preset_prompt} {aspect_desc}."

    # 수동 조합
    if mode == "exterior":
        subject_line = "Professional architectural exterior photography."
        content_line = _build_exterior_line(data)
        viewpoint = data.get("ext_viewpoint", "")
    else:
        subject_line = "Professional architectural interior photography."
        content_line = _build_interior_line(data)
        viewpoint = data.get("int_viewpoint", "")

    common_line = _build_common_line(data, mode)

    if viewpoint:
        viewpoint_line = f"Viewpoint: {viewpoint}."
    else:
        viewpoint_line = ""

    quality_line = "Ultra-sharp photorealistic image, 8K resolution, award-winning architectural photography, highly detailed."

    parts = [p for p in [
        subject_line,
        content_line,
        viewpoint_line,
        common_line,
        quality_line,
        aspect_desc + "."
    ] if p.strip()]

    return " ".join(parts)


def build_chatgpt_prompt(data: dict, aspect_ratio: str, mode: str = "exterior") -> str:
    """
    ChatGPT (DALL-E)용 키워드 중심 간결 프롬프트
    """
    aspect_desc = ASPECT_RATIOS.get(aspect_ratio, "portrait 2:3 vertical")

    preset_prompt = data.get("preset_prompt", "")
    if preset_prompt:
        return f"{preset_prompt} Photorealistic, hyperrealistic, award-winning. {aspect_desc}."

    tags = []

    if mode == "exterior":
        building = data.get("building_type", "")
        style = data.get("arch_style", "")
        material = data.get("ext_material", "")
        roof = data.get("roof_style", "")
        viewpoint = data.get("ext_viewpoint", "")
        if building: tags.append(building.split(",")[0])
        if style: tags.append(style.split(",")[0])
        if material: tags.append(material.split(",")[0])
        if roof: tags.append(roof.split(",")[0])
        if viewpoint: tags.append(viewpoint.split(",")[0])
    else:
        space = data.get("space_type", "")
        style = data.get("int_style", "")
        material = data.get("int_material", "")
        palette = data.get("color_palette", "")
        viewpoint = data.get("int_viewpoint", "")
        if space: tags.append(space.split(",")[0])
        if style: tags.append(style.split(",")[0])
        if material: tags.append(material.split(",")[0])
        if palette: tags.append(palette.split(",")[0])
        if viewpoint: tags.append(viewpoint.split(",")[0])

    lighting = data.get("lighting", "")
    mood = data.get("mood", "")
    color_grade = data.get("color_grade", "")
    render_style = data.get("render_style", "")

    if lighting: tags.append(lighting.split(",")[0])
    if mood and mood != "없음": tags.append(mood.split(",")[0])
    if color_grade and color_grade != "없음": tags.append(color_grade.split(",")[0])
    if render_style: tags.append(render_style.split(",")[0])

    tags.append("photorealistic")
    tags.append("architectural photography")
    tags.append("8K ultra detail")

    return ", ".join(tags) + f". {aspect_desc}."


def build_midjourney_prompt(data: dict, aspect_ratio: str, mode: str = "exterior") -> str:
    """
    Midjourney용 태그 나열 + 파라미터 프롬프트
    """
    ar_map = {
        "세로 2:3 — 외관 기본 ★": "2:3",
        "정방형 1:1 — 인스타 피드": "1:1",
        "가로 16:9 — 와이드 전경": "16:9",
        "가로 4:3 — 화보/카탈로그": "4:3",
        "가로 3:2 — 클래식 가로": "3:2",
        "세로 9:16 — 모바일/릴스": "9:16",
    }
    ar = ar_map.get(aspect_ratio, "2:3")

    preset_prompt = data.get("preset_prompt", "")
    if preset_prompt:
        return f"{preset_prompt} --ar {ar} --style raw --q 2"

    tags = []

    if mode == "exterior":
        for key in ["building_type", "arch_style", "ext_material", "roof_style", "landscaping"]:
            val = data.get(key, "")
            if val:
                tags.append(val.split(",")[0].strip())
        viewpoint = data.get("ext_viewpoint", "")
        if viewpoint:
            tags.append(viewpoint.split(",")[0].strip())
    else:
        for key in ["space_type", "int_style", "int_material", "furniture_style", "color_palette"]:
            val = data.get(key, "")
            if val and val != "없음 — 빈 공간/건축 위주":
                tags.append(val.split(",")[0].strip())
        viewpoint = data.get("int_viewpoint", "")
        if viewpoint:
            tags.append(viewpoint.split(",")[0].strip())

    for key in ["lighting", "mood", "color_grade", "render_style"]:
        val = data.get(key, "")
        if val and val != "없음":
            tags.append(val.split(",")[0].strip())

    tags += ["architectural photography", "ultra detailed", "8K"]

    return ", ".join(tags) + f" --ar {ar} --style raw --q 2"