"""
LumineX - 유니폼 글래머 프리셋 추가 스크립트 v3.7
실행: python add_new_presets_v4.py
유니폼 직업 글래머 컨셉 18개
"""

import json
import os

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")
os.makedirs(PRESETS_DIR, exist_ok=True)

NEW_PRESETS_V37 = {

    # ── 럭셔리/서비스 계열 ──────────────────────────────────
    "flight_attendant": {
        "tag": "Flight Attendant",
        "subject": "a glamorous airline flight attendant female model",
        "body": "slim toned model, lean elegant figure, refined fashion presence",
        "outfit": "luxury airline uniform, fitted blazer, pencil skirt, silk neck scarf, elegant cabin crew styling",
        "material": "structured tailored fabric, luxury airline uniform textile",
        "environment": "first class cabin interior, private jet luxury, airplane window view",
        "lighting": "soft cabin lighting, warm golden glow, luxury aviation atmosphere",
        "style": "luxury airline editorial, Singapore Airlines glamour photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },

    "hotel_concierge": {
        "tag": "Hotel Concierge",
        "subject": "a sophisticated luxury hotel concierge female model",
        "body": "slender elegant model, slim narrow frame, graceful refined fashion presence",
        "outfit": "luxury hotel concierge uniform, fitted blazer, pencil skirt, gold name badge, white gloves",
        "material": "structured luxury wool fabric, high-end hotel uniform textile",
        "environment": "grand luxury hotel lobby, marble columns, crystal chandeliers",
        "lighting": "warm chandelier light, luxury hotel atmosphere, golden glow",
        "style": "luxury hotel editorial, Ritz Carlton glamour photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },

    "casino_dealer": {
        "tag": "Casino Dealer",
        "subject": "a mysterious glamorous casino dealer female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "casino dealer uniform, sleek black vest, white shirt, bow tie, fitted trousers, playing card props",
        "material": "structured matte fabric, casino uniform textile, silk bow tie",
        "environment": "luxury casino interior, green felt tables, warm casino lighting",
        "lighting": "warm casino lights, dramatic shadows, glamorous gaming atmosphere",
        "style": "casino glamour editorial, Las Vegas luxury photography",
        "quality": "shot on Sony A7R V, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },

    "cruise_hostess": {
        "tag": "Cruise Hostess",
        "subject": "a radiant cruise ship hostess female model",
        "body": "VS 앤젤 — 완벽한 VS 글래머",
        "outfit": "cruise ship hostess uniform, fitted white dress, gold accents, maritime elegance",
        "material": "crisp white luxury fabric, nautical gold detail textile",
        "environment": "luxury cruise ship deck, Mediterranean sea, golden sunset",
        "lighting": "golden hour warm backlight, ocean reflection, tropical glamour",
        "style": "luxury cruise editorial, Mediterranean glamour photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },

    "yacht_captain": {
        "tag": "Yacht Captain",
        "subject": "a commanding glamorous yacht captain female model",
        "body": "slim toned model, lean athletic build, confident commanding presence",
        "outfit": "yacht captain uniform, fitted white naval blazer, gold epaulettes, captain hat, tailored shorts",
        "material": "crisp white naval fabric, gold braided trim, luxury maritime textile",
        "environment": "luxury superyacht deck, Monaco harbor, Mediterranean blue",
        "lighting": "bright Mediterranean sun, ocean reflection, clean glamour light",
        "style": "luxury yacht editorial, captain glamour photography",
        "quality": "shot on Canon EOS R5, high key bright white tone, portrait 2:3 vertical"
    },

    "sommelier": {
        "tag": "Sommelier",
        "subject": "a sophisticated wine sommelier female model",
        "body": "slender elegant model, slim narrow frame, graceful refined presence",
        "outfit": "sommelier uniform, fitted black apron, white shirt, tastevin necklace, holding wine glass",
        "material": "structured black fabric, crisp white linen, luxury restaurant textile",
        "environment": "luxury wine cellar, vintage bottles, candlelight, Bordeaux estate",
        "lighting": "warm candlelight, wine cellar amber glow, intimate luxury atmosphere",
        "style": "luxury wine editorial, Michelin restaurant glamour photography",
        "quality": "shot on Leica SL2, warm golden film grade, portrait 2:3 vertical"
    },

    # ── 스포츠 계열 ─────────────────────────────────────────
    "cheerleader": {
        "tag": "Cheerleader",
        "subject": "a vibrant glamorous cheerleader female model",
        "body": "athletic fitness model, defined abs, toned muscular legs, round athletic hips",
        "outfit": "luxury cheerleader uniform, fitted crop top, short pleated skirt, pompoms, high boots",
        "material": "stretch performance fabric, vibrant color athletic textile",
        "environment": "stadium field, bright stadium lights, crowd energy",
        "lighting": "dramatic stadium lighting, high energy atmosphere, bright performance light",
        "style": "sports glamour editorial, NFL cheerleader luxury photography",
        "quality": "shot on Canon EOS R5, high key bright white tone, portrait 2:3 vertical"
    },

    "golf_caddie": {
        "tag": "Golf Caddie",
        "subject": "a sporty glamorous golf caddie female model",
        "body": "slim toned model, lean athletic build, flat stomach, slim toned silhouette",
        "outfit": "luxury golf caddie uniform, fitted polo shirt, tailored shorts, golf cap, white gloves",
        "material": "luxury performance fabric, tailored country club textile",
        "environment": "championship golf course, manicured green, blue sky",
        "lighting": "golden hour warm sunlight, country club glamour",
        "style": "luxury golf editorial, country club glamour photography",
        "quality": "shot on Sony A7R V, high key bright white tone, portrait 2:3 vertical"
    },

    "tennis_referee": {
        "tag": "Tennis Referee",
        "subject": "a elegant tennis referee female model",
        "body": "slim fitness model, lean defined muscles, athletic slim silhouette",
        "outfit": "tennis referee uniform, fitted polo dress, official badge, whistle, athletic elegance",
        "material": "luxury performance fabric, official tennis uniform textile",
        "environment": "Wimbledon grass court, pristine white surroundings, summer glamour",
        "lighting": "bright natural daylight, clean tennis court light",
        "style": "Wimbledon editorial, tennis glamour photography",
        "quality": "shot on Canon EOS R5, high key bright white tone, portrait 2:3 vertical"
    },

    "f1_grid_girl": {
        "tag": "F1 Grid Girl",
        "subject": "a fierce glamorous F1 grid girl female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "F1 racing team uniform, fitted racing suit, team colors, holding racing sign, motorsport glamour",
        "material": "racing performance fabric, team branded athletic textile",
        "environment": "Formula 1 racing circuit, pit lane, race cars, dramatic motorsport",
        "lighting": "dramatic race day lighting, motion blur background, motorsport atmosphere",
        "style": "F1 motorsport editorial, racing glamour photography",
        "quality": "shot on Sony A7R V, cinematic teal and orange color grade, portrait 2:3 vertical"
    },

    "martial_arts": {
        "tag": "Martial Arts",
        "subject": "a powerful martial arts female model",
        "body": "power fitness model, very muscular defined body, strong arms and legs, athletic powerful build",
        "outfit": "martial arts uniform, fitted white taekwondo dobok, black belt, dynamic fighting pose",
        "material": "crisp white martial arts fabric, structured dobok textile",
        "environment": "traditional dojo, Japanese architecture, tatami floor, dramatic lighting",
        "lighting": "dramatic dojo lighting, sharp shadows, martial arts atmosphere",
        "style": "martial arts editorial, action glamour photography",
        "quality": "shot on Canon EOS R5, dark moody color grade, portrait 2:3 vertical"
    },

    # ── 전문직 계열 ─────────────────────────────────────────
    "nurse_glamour": {
        "tag": "Nurse Glamour",
        "subject": "a elegant medical nurse female model",
        "body": "slim toned model, lean athletic build, refined elegant presence",
        "outfit": "luxury nurse uniform, fitted white medical dress, nurse cap, stethoscope, editorial medical fashion",
        "material": "crisp white medical fabric, structured luxury uniform textile",
        "environment": "luxury private hospital room, clean modern medical interior",
        "lighting": "clean bright medical lighting, pure white atmosphere",
        "style": "medical fashion editorial, luxury healthcare photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, portrait 2:3 vertical"
    },

    "pilot_glamour": {
        "tag": "Pilot Glamour",
        "subject": "a commanding glamorous pilot female model",
        "body": "slim toned model, confident commanding presence, elegant refined figure",
        "outfit": "airline captain uniform, fitted dark blazer, gold epaulettes, captain hat, aviator sunglasses",
        "material": "structured dark navy fabric, gold braided trim, luxury aviation textile",
        "environment": "aircraft cockpit, runway at sunset, aviation glamour",
        "lighting": "golden sunset through cockpit window, dramatic aviation atmosphere",
        "style": "aviation glamour editorial, captain luxury photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },

    "lawyer_power": {
        "tag": "Lawyer Power",
        "subject": "a powerful glamorous lawyer female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, confident dominant presence",
        "outfit": "power lawyer suit, ultra-fitted blazer, pencil skirt, silk blouse, briefcase, dominant glamour",
        "material": "luxury structured wool, power suit fabric, silk blouse",
        "environment": "luxury law office, mahogany desk, city view, high-rise building",
        "lighting": "dramatic office lighting, power ambiance, city skyline glow",
        "style": "corporate power editorial, Suits TV show glamour photography",
        "quality": "shot on Sony A7R V, dark moody color grade, portrait 2:3 vertical"
    },

    "architect_chic": {
        "tag": "Architect Chic",
        "subject": "a sophisticated architect female model",
        "body": "slender elegant model, slim narrow frame, intellectual refined presence",
        "outfit": "architect chic outfit, minimal structured blazer, tailored trousers, blueprint props, minimal luxury",
        "material": "structured minimal fabric, architectural clean-line textile",
        "environment": "modern architectural space, glass and steel building, dramatic structure",
        "lighting": "clean architectural lighting, sharp geometric shadows",
        "style": "architectural editorial, Zaha Hadid inspired glamour photography",
        "quality": "shot on Hasselblad H6D, cool blue color grade, portrait 2:3 vertical"
    },

    # ── 엔터테인먼트 계열 ───────────────────────────────────
    "burlesque": {
        "tag": "Burlesque",
        "subject": "a glamorous burlesque performer female model",
        "body": "glamour curvy model, dramatic waist-to-hip ratio, very wide round hips, voluptuous pinup",
        "outfit": "burlesque costume, corset bustier, feather boa, fishnet stockings, vintage glamour performance",
        "material": "satin corset fabric, luxury feathers, vintage burlesque textile",
        "environment": "vintage burlesque theater, red velvet curtains, spotlight stage",
        "lighting": "dramatic stage spotlight, vintage theater atmosphere, warm amber glow",
        "style": "burlesque editorial, vintage pinup glamour photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, portrait 2:3 vertical"
    },

    "showgirl": {
        "tag": "Showgirl",
        "subject": "a spectacular Las Vegas showgirl female model",
        "body": "VS 앤젤 — 완벽한 VS 글래머",
        "outfit": "Las Vegas showgirl costume, elaborate feather headdress, sequin bodysuit, long feather tail",
        "material": "iridescent sequin fabric, luxury feathers, Las Vegas showgirl textile",
        "environment": "Las Vegas showroom stage, bright stage lights, casino glamour",
        "lighting": "bright showroom spotlight, Las Vegas glamour lighting, sequin reflections",
        "style": "Las Vegas showgirl editorial, Moulin Rouge glamour photography",
        "quality": "shot on Sony A7R V, high key bright white tone, portrait 2:3 vertical"
    },

    "circus_performer": {
        "tag": "Circus Performer",
        "subject": "a spectacular circus performer female model",
        "body": "athletic fitness model, defined abs, toned muscular legs, acrobatic powerful physique",
        "outfit": "circus performer costume, sequin leotard, dramatic cape, acrobatic glamour styling",
        "material": "iridescent sequin fabric, dramatic performance textile, circus luxury material",
        "environment": "grand circus tent, dramatic big top, aerial performance space",
        "lighting": "dramatic circus spotlight, aerial performance lighting, magical atmosphere",
        "style": "Cirque du Soleil editorial, circus glamour photography",
        "quality": "shot on Canon EOS R5, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },
}


def main():
    print("\n  ✦ LumineX v3.7 유니폼 글래머 프리셋 추가 시작...\n")
    created = 0
    skipped = 0

    for name, data in NEW_PRESETS_V37.items():
        path = os.path.join(PRESETS_DIR, f"{name}.json")
        if os.path.exists(path):
            print(f"  ⏭️  건너뜀: {name}.json")
            skipped += 1
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  ✅ 생성: {name}.json")
            created += 1

    print(f"\n  완료: 생성 {created}개 / 건너뜀 {skipped}개")
    total = len([f for f in os.listdir(PRESETS_DIR) if f.endswith('.json')])
    print(f"  총 프리셋: {total}개\n")
    print("  📋 추가된 카테고리:")
    print("  - 럭셔리/서비스 (승무원/컨시어지/딜러/크루즈/요트/소믈리에) × 6")
    print("  - 스포츠 (치어리더/캐디/심판/F1/무술) × 5")
    print("  - 전문직 (간호사/파일럿/변호사/건축가) × 4")
    print("  - 엔터테인먼트 (버레스크/쇼걸/서커스) × 3")
    print(f"  총 18개 신규 프리셋\n")


if __name__ == "__main__":
    main()
