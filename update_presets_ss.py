"""
SS tier 업데이트 + constellation_body/melting_chocolate 프롬프트 수정
"""
import json
from pathlib import Path

PRESETS_DIR = Path("presets")

# constellation_body 프롬프트 수정
constellation = {
    "tag": "Constellation Body",
    "subject": "a celestial constellation body art female model",
    "body": "slim elegance model, cosmic figure, star map goddess presence",
    "outfit": "zodiac constellation patterns painted directly on bare skin, NOT wearing any fabric, gold star dots and connecting lines painted on body, trompe l'oeil body art not clothing",
    "material": "gold constellation paint on bare skin, star pattern body art only, zero fabric no clothing",
    "environment": "dark space void, milky way backdrop, cosmic atmosphere",
    "lighting": "starlight glow on painted skin, cosmic atmosphere, constellation body art light",
    "style": "constellation body art editorial, celestial glamour photography",
    "quality": "shot on Hasselblad H6D, deep space grade, portrait 2:3 vertical"
}

# melting_chocolate 프롬프트 수정
melting_chocolate = {
    "tag": "Melting Chocolate",
    "subject": "a decadent melting chocolate body art female model",
    "body": "slim elegance model, bare skin dripping with chocolate, sensual chocolate goddess presence",
    "outfit": "NOT wearing any clothing, liquid chocolate poured directly on bare skin, melting chocolate drip body art, chocolate covering bare body only",
    "material": "liquid dark chocolate dripping on bare skin only, NOT fabric or clothing, chocolate body art",
    "environment": "dark luxury chocolate atelier, copper pots, artisan atmosphere",
    "lighting": "warm amber chocolate atelier light, drip shadow, sensual chocolate glow",
    "style": "melting chocolate body art editorial, sensual food glamour photography",
    "quality": "shot on Phase One XF IQ4, warm chocolate grade, portrait 2:3 vertical"
}

updates = {
    "constellation_body": constellation,
    "melting_chocolate": melting_chocolate,
}

for name, data in updates.items():
    path = PRESETS_DIR / f"{name}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ updated: {name}")

print("\n완료!")
