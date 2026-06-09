"""
LumineX - AI Fashion Image Generation Engine
Usage:
  python main.py --preset editorial_glam
  python main.py --random
  python main.py --batch 4 --preset runway_power
  python main.py --mixed runway_power
  python main.py --list
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import OUTPUT_DIR, BATCH_SIZE, ACTIVE_PROVIDER
from core.engine import build_prompt_from_name, list_presets
from core.randomizer import build_random_prompt, build_mixed_prompt
from providers import get_provider


def make_output_path(preset_name: str, index: int = 0) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{preset_name}_{ts}_{index:02d}.png"
    return os.path.join(OUTPUT_DIR, filename)


def run_generation(prompt: str, label: str, index: int = 0):
    provider = get_provider(ACTIVE_PROVIDER)

    if not provider.is_available():
        print(f"  ❌ {provider.name} API 키가 설정되지 않았습니다.")
        print(f"     .env 파일에 GEMINI_API_KEY=your_key_here 를 추가하세요.")
        sys.exit(1)

    output_path = make_output_path(label, index)
    print(f"  ⚡ 생성 중: [{label}] #{index+1}")
    print(f"  📝 프롬프트: {prompt[:120]}...")

    result = provider.generate(prompt, output_path)

    if result.success:
        print(f"  ✅ 성공: {result.image_path}")
    else:
        print(f"  ❌ 실패: {result.error}")

    return result


def main():
    parser = argparse.ArgumentParser(
        description="LumineX - AI Fashion Image Generation Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--preset",  type=str, help="프리셋 이름으로 생성")
    parser.add_argument("--random",  action="store_true", help="완전 랜덤 생성")
    parser.add_argument("--mixed",   type=str, help="프리셋 기반 랜덤 믹스 생성")
    parser.add_argument("--batch",   type=int, default=1, help="배치 생성 수량 (기본 1)")
    parser.add_argument("--list",    action="store_true", help="사용 가능한 프리셋 목록 출력")
    parser.add_argument("--prompt",  type=str, help="직접 프롬프트 입력")
    parser.add_argument("--prompt-only", action="store_true", help="프롬프트만 생성 (이미지 생성 안 함)")

    args = parser.parse_args()

    if args.prompt_only and args.preset:
        from core.prompt_generator import generate_prompt_with_ai
        print(f"\n  🤖 AI 프롬프트 생성 중: [{args.preset}]\n")
        prompt = generate_prompt_with_ai(args.preset)
        print("─" * 55)
        print(prompt)
        print("─" * 55)
        print("\n  👆 위 프롬프트를 Gemini 창에 복붙하세요!\n")
        return

    print("\n" + "═" * 55)
    print("  ✦  LumineX Image Engine")
    print("═" * 55)

    # 프리셋 목록 출력
    if args.list:
        presets = list_presets()
        print(f"\n  사용 가능한 프리셋 ({len(presets)}개):\n")
        for p in presets:
            print(f"    • {p}")
        print()
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = max(1, args.batch)
    results = []

    for i in range(count):
        print()
        if args.preset:
            prompt = build_prompt_from_name(args.preset)
            result = run_generation(prompt, args.preset, i)

        elif args.random:
            prompt = build_random_prompt()
            result = run_generation(prompt, "random", i)

        elif args.mixed:
            prompt = build_mixed_prompt(args.mixed)
            result = run_generation(prompt, f"mixed_{args.mixed}", i)

        elif args.prompt:
            result = run_generation(args.prompt, "custom", i)

        else:
            parser.print_help()
            return

        results.append(result)

    # 최종 요약
    success = sum(1 for r in results if r.success)
    fail    = len(results) - success

    print("\n" + "─" * 55)
    print(f"  완료: ✅ 성공 {success}개  ❌ 실패 {fail}개")
    print("─" * 55 + "\n")


if __name__ == "__main__":
    main()