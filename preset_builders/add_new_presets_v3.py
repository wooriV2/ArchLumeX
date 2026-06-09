"""
LumineX - 전통 복장 글래머 프리셋 추가 스크립트 v3.6
실행: python add_new_presets_v3.py
전통 복장 + 글래머/섹시 컨셉 10개
"""

import json
import os

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")
os.makedirs(PRESETS_DIR, exist_ok=True)

NEW_PRESETS_V36 = {

    "hanbok_glamour": {
        "tag": "Hanbok Glamour",
        "subject": "a stunning Korean goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "modern hanbok fusion, low-cut jeogori top, high-slit skirt, sexy Korean traditional reinterpretation",
        "material": "liquid satin silk, iridescent traditional fabric, jewel-tone colors",
        "environment": "Korean palace courtyard, Gyeongbokgung at night, lantern light",
        "lighting": "golden lantern light, warm amber glow, traditional Korean atmosphere",
        "style": "Harper's Bazaar Korea sensual editorial, luxury traditional Korean fashion",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },

    "qipao_noir": {
        "tag": "Qipao Noir",
        "subject": "a mysterious seductive Chinese female model",
        "body": "super glamour model, tiny waist, very wide round hips, maximum hourglass silhouette",
        "outfit": "ultra-high slit qipao cheongsam, extreme leg reveal, plunging neckline, figure-hugging Chinese dress",
        "material": "liquid satin, body-hugging stretch silk, shimmering embroidered fabric",
        "environment": "Shanghai art deco interior, 1930s opium den glamour, red lanterns",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights, film noir atmosphere",
        "style": "Shanghai noir editorial, dark Chinese glamour photography",
        "quality": "shot on Sony A7R V, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },

    "sari_goddess": {
        "tag": "Sari Goddess",
        "subject": "a divine Indian goddess female model",
        "body": "glamour curvy model, dramatic waist-to-hip ratio, very wide round hips, voluptuous",
        "outfit": "draped sari with midriff-baring crop blouse, jeweled belt, low-back choli, sensual traditional Indian",
        "material": "gold embroidered silk sari, jewel-encrusted fabric, shimmering Indian textile",
        "environment": "Rajasthan palace at sunset, ornate Mughal architecture, rose petals",
        "lighting": "golden hour warm backlight, skin luminosity, magical Indian sunset",
        "style": "Vogue India sensual editorial, luxury Indian fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, portrait 2:3 vertical"
    },

    "odalisque": {
        "tag": "Odalisque",
        "subject": "a exotic Ottoman harem beauty female model",
        "body": "soft curvy model, wide round hips, full soft thighs, voluptuous feminine curves",
        "outfit": "Ottoman harem costume, sheer silk pants, jeweled bra top, translucent veil, exotic Middle Eastern glamour",
        "material": "sheer silk chiffon, gold embroidered fabric, jeweled accessories",
        "environment": "Ottoman palace harem, opulent cushions, silk drapes, incense smoke",
        "lighting": "warm candlelight, golden amber glow, mysterious harem atmosphere",
        "style": "Orientalist painting inspired editorial, exotic luxury fashion photography",
        "quality": "shot on Phase One XF IQ4, warm golden film grade, portrait 2:3 vertical"
    },

    "geisha_red": {
        "tag": "Geisha Red",
        "subject": "a seductive crimson geisha female model",
        "body": "hot glamour model, narrow cinched waist, elegant curves, refined Japanese beauty",
        "outfit": "scarlet red open kimono, deep plunging neckline, obi belt cinching waist, dramatic red geisha",
        "material": "crimson silk kimono, gold embroidery, luxurious Japanese textile",
        "environment": "Kyoto red lantern district, Gion at night, cherry blossoms",
        "lighting": "red lantern glow, dramatic crimson atmosphere, mysterious night",
        "style": "dark Japanese glamour editorial, seductive geisha fashion photography",
        "quality": "shot on Fujifilm GFX 100S, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },

    "maiko_glamour": {
        "tag": "Maiko Glamour",
        "subject": "a youthful seductive maiko female model",
        "body": "slim toned model, lean elegant figure, graceful delicate presence",
        "outfit": "elaborate maiko furisode kimono, dangling kanzashi hair ornaments, modern seductive reinterpretation",
        "material": "elaborate silk kimono fabric, colorful embroidered textile, traditional Japanese material",
        "environment": "Kyoto teahouse garden, bamboo forest, golden hour",
        "lighting": "soft golden hour light, dappled bamboo shadows, ethereal atmosphere",
        "style": "Vogue Japan editorial, luxury Japanese fashion photography",
        "quality": "shot on Hasselblad H6D, soft pink glamour grade, rose gold tones, portrait 2:3 vertical"
    },

    "belly_dancer": {
        "tag": "Belly Dancer",
        "subject": "a exotic seductive belly dancer female model",
        "body": "glamour curvy model, dramatic waist-to-hip ratio, very wide round hips, toned midriff",
        "outfit": "jeweled belly dance costume, coin-adorned bra top, hip scarf, exposed midriff, Arabian glamour",
        "material": "gold coin chain fabric, jeweled sequin material, sheer chiffon layers",
        "environment": "Arabian palace courtyard, mosaic tiles, candles, desert night",
        "lighting": "warm candlelight, golden amber glow, mysterious Arabian atmosphere",
        "style": "Arabian nights editorial, exotic dance glamour photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },

    "flamenco_queen": {
        "tag": "Flamenco Queen",
        "subject": "a fierce passionate flamenco female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "dramatic flamenco dress, ruffled high-slit skirt, off-shoulder bodice, deep plunging neckline, Spanish passion",
        "material": "dramatic ruffled fabric, polka dot silk, bold Spanish textile",
        "environment": "Seville flamenco stage, dramatic spotlight, roses on floor",
        "lighting": "dramatic stage spotlight, deep red atmosphere, passionate shadows",
        "style": "Spanish glamour editorial, flamenco fashion photography",
        "quality": "shot on Sony A7R V, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },

    "harem_goddess": {
        "tag": "Harem Goddess",
        "subject": "a powerful Arabian harem goddess female model",
        "body": "super glamour model, tiny waist, very wide round hips, maximum hourglass silhouette, pinup glamour",
        "outfit": "Arabian harem goddess costume, jeweled crop top, sheer palazzo pants, golden body chains, exotic goddess",
        "material": "sheer gold silk, jewel-encrusted fabric, Arabian luxury textile",
        "environment": "Arabian palace throne room, gold and jewels, desert stars visible",
        "lighting": "golden chandelier light, jewel reflections, opulent Arabian atmosphere",
        "style": "Arabian luxury editorial, harem goddess fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },

    "pharaoh_queen": {
        "tag": "Pharaoh Queen",
        "subject": "a powerful Egyptian pharaoh queen female model",
        "body": "luxury glamour model, defined waist, wide round hips, sophisticated voluptuous elegance",
        "outfit": "Egyptian pharaoh queen costume, jeweled collar, pleated linen skirt, bare midriff, ancient Egyptian glamour",
        "material": "gold hammered fabric, Egyptian linen, royal jeweled textile",
        "environment": "ancient Egyptian temple, hieroglyph walls, torch light, Nile at night",
        "lighting": "torch fire light, golden amber glow, ancient Egyptian atmosphere",
        "style": "ancient Egypt glamour editorial, pharaoh fashion photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },
}


def main():
    print("\n  ✦ LumineX v3.6 전통 복장 글래머 프리셋 추가 시작...\n")
    created = 0
    skipped = 0

    for name, data in NEW_PRESETS_V36.items():
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
    print("  📋 추가된 프리셋:")
    print("  - 한복 글래머 (hanbok_glamour)")
    print("  - 치파오 느아르 (qipao_noir)")
    print("  - 사리 여신 (sari_goddess)")
    print("  - 오달리스크 (odalisque)")
    print("  - 붉은 게이샤 (geisha_red)")
    print("  - 마이코 글래머 (maiko_glamour)")
    print("  - 벨리댄서 (belly_dancer)")
    print("  - 플라멩코 여왕 (flamenco_queen)")
    print("  - 하렘 여신 (harem_goddess)")
    print("  - 파라오 여왕 (pharaoh_queen)")
    print(f"  총 10개 신규 프리셋\n")


if __name__ == "__main__":
    main()
