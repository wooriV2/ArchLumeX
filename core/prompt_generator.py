import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import anthropic
from core.engine import load_preset


def generate_prompt_with_ai(preset_name: str) -> str:
    preset = load_preset(preset_name)
    client = anthropic.Anthropic()

    instruction = f"""You are an expert AI image prompt engineer specializing in fashion photography.

Based on this preset data, generate a powerful, detailed image generation prompt:

Preset: {preset}

Requirements:
- Write in English
- Highly detailed, cinematic description
- Include camera settings, lighting, mood
- Optimized for Gemini image generation
- Maximum visual impact, glamorous and stunning female model
- Include specific fashion details, body language, atmosphere
- 150-200 words

Output ONLY the prompt, nothing else."""

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        messages=[{"role": "user", "content": instruction}]
    )

    return response.content[0].text.strip()