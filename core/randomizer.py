import random
from typing import Optional
from core.engine import load_preset, list_presets, build_prompt


# 랜덤 조합용 요소 풀
RANDOM_SUBJECTS = [
    "a professional fashion model",
    "a high-fashion editorial model",
    "a luxury brand campaign model",
    "a fitness and fashion model",
    "an avant-garde fashion model",
]

RANDOM_BODY = [
    "statuesque proportions, tall elegant figure",
    "athletic toned physique, powerful stance",
    "elongated legs, modelesque silhouette",
    "strong athletic build, dynamic presence",
    "graceful powerful figure, confident posture",
]

RANDOM_ENVIRONMENTS = [
    "minimalist white studio",
    "luxury penthouse rooftop",
    "industrial warehouse loft",
    "neon-lit city street at night",
    "desert dunes at golden hour",
    "ice cave interior",
    "modernist glass villa",
    "brutalist concrete architecture",
    "volcanic rock plateau at sunset",
    "luxury hotel suite",
]

RANDOM_LIGHTING = [
    "dramatic chiaroscuro lighting",
    "golden hour backlight",
    "cold blue ambient light",
    "multi-colored neon glow",
    "harsh direct strobe",
    "soft diffused skylight",
    "warm tungsten spotlight",
    "full moon moonlight",
    "volumetric fog light",
    "rim light silhouette",
]

RANDOM_STYLES = [
    "Vogue editorial photography",
    "Harper's Bazaar fashion spread",
    "Sports Illustrated editorial",
    "Dazed & Confused magazine",
    "W Magazine fashion editorial",
    "high-fashion campaign photography",
    "cinematic fashion film still",
]

RANDOM_QUALITY = [
    "shot on Hasselblad H6D, ultra-sharp, 8K resolution",
    "shot on Phase One XF IQ4, medium format, 8K",
    "shot on Canon EOS R5, professional grade, 8K",
    "shot on Sony A7R V, ultra-detailed, 8K",
    "shot on Nikon Z9, award-winning photography, 8K",
]


def build_random_prompt(seed: Optional[int] = None) -> str:
    """완전 랜덤 프롬프트 생성"""
    if seed is not None:
        random.seed(seed)

    subject = random.choice(RANDOM_SUBJECTS)
    body    = random.choice(RANDOM_BODY)
    env     = random.choice(RANDOM_ENVIRONMENTS)
    light   = random.choice(RANDOM_LIGHTING)
    style   = random.choice(RANDOM_STYLES)
    quality = random.choice(RANDOM_QUALITY)

    # 랜덤으로 프리셋 하나 믹스인
    available = list_presets()
    base_preset = load_preset(random.choice(available))
    outfit   = base_preset.get("outfit", "high-fashion designer ensemble")
    material = base_preset.get("material", "luxury fabric")

    prompt = (
        f"Professional fashion photograph of {subject}. "
        f"Body: {body}. "
        f"Wearing: {outfit} made of {material}. "
        f"Environment: {env}. "
        f"Lighting: {light}. "
        f"Style: {style}. "
        f"{quality}, professional fashion photography."
    )
    return prompt.strip()


def build_mixed_prompt(preset_name: str, seed: Optional[int] = None) -> str:
    """프리셋 기반 + 랜덤 요소 믹스"""
    if seed is not None:
        random.seed(seed)

    preset = load_preset(preset_name)

    # 환경과 조명만 랜덤으로 교체
    overrides = {
        "environment": random.choice(RANDOM_ENVIRONMENTS),
        "lighting":    random.choice(RANDOM_LIGHTING),
    }

    merged = {**preset, **overrides}

    from core.engine import build_prompt
    return build_prompt(merged)