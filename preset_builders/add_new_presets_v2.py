"""
LumineX - 신규 프리셋 추가 스크립트 v3.5
실행: python add_new_presets_v2.py
다양성/개성/신선함 중심 30개 신규 프리셋
"""

import json
import os

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")
os.makedirs(PRESETS_DIR, exist_ok=True)

NEW_PRESETS_V35 = {

    # ── 귀엽고 발랄 🌸 ────────────────────────────────────
    "harajuku_doll": {
        "tag": "Harajuku Doll",
        "subject": "a playful kawaii female model",
        "body": "petite slender figure, doll-like proportions, youthful energy",
        "outfit": "harajuku street fashion, layered colorful mini dress, oversized accessories, kawaii styling",
        "material": "mixed pastel fabrics, tulle layers, shiny vinyl accents",
        "environment": "Tokyo Harajuku street, colorful storefronts, Takeshita Street",
        "lighting": "bright daylight, vivid colors, playful atmosphere",
        "style": "Harajuku Fruits magazine editorial, kawaii street fashion photography",
        "quality": "shot on Canon EOS R5, high key bright white tone, vivid saturated colors, portrait 2:3 vertical"
    },
    "candy_rave": {
        "tag": "Candy Rave",
        "subject": "a vibrant rave female model",
        "body": "athletic toned figure, energetic presence, festival ready",
        "outfit": "candy-colored rave outfit, neon crop top, holographic mini skirt, glow accessories",
        "material": "holographic iridescent fabric, neon stretch material",
        "environment": "outdoor music festival, stage lights, crowd energy",
        "lighting": "neon UV light, colorful stage lighting, electric atmosphere",
        "style": "festival fashion editorial, EDM rave culture photography",
        "quality": "shot on Sony A7R V, neon color grade, vibrant saturated tones, portrait 2:3 vertical"
    },
    "pastel_fairy": {
        "tag": "Pastel Fairy",
        "subject": "a ethereal pastel fairy female model",
        "body": "slender delicate figure, graceful ethereal presence, fairy-like proportions",
        "outfit": "pastel fairy dress, soft tulle layers, floral crown, delicate wing accessories",
        "material": "soft chiffon tulle, pastel organza, sheer layered fabric",
        "environment": "enchanted flower meadow, cherry blossom forest, magical garden",
        "lighting": "soft diffused golden light, magical bokeh, dreamy atmosphere",
        "style": "fairy tale fashion editorial, ethereal fantasy photography",
        "quality": "shot on Hasselblad H6D, soft pink glamour grade, rose gold tones, portrait 2:3 vertical"
    },
    "bubble_tea": {
        "tag": "Bubble Tea",
        "subject": "a cute aesthetic female model",
        "body": "petite feminine figure, soft curves, cute youthful energy",
        "outfit": "Taiwanese street style, cute co-ord set, pastel colors, playful accessories",
        "material": "soft cotton fabric, pastel knit, cute printed textile",
        "environment": "Taipei night market, bubble tea shop, neon signs, Asian street",
        "lighting": "warm neon glow, cozy night market atmosphere, soft ambient light",
        "style": "Taiwanese aesthetic editorial, Asian cute fashion photography",
        "quality": "shot on Fujifilm GFX 100S, soft pink glamour grade, warm tones, portrait 2:3 vertical"
    },
    "doll_house": {
        "tag": "Doll House",
        "subject": "a Barbie-inspired glamorous female model",
        "body": "ultra-slim hourglass figure, long legs, doll-perfect proportions",
        "outfit": "hot pink Barbie-inspired mini dress, plastic glamour, maximalist pink styling",
        "material": "shiny pink satin, glossy pink vinyl accents",
        "environment": "pink Barbie dreamhouse interior, pink everything, maximalist pink world",
        "lighting": "bright pink-tinted studio light, glamorous doll lighting",
        "style": "Barbie movie inspired editorial, maximalist pink fashion photography",
        "quality": "shot on Canon EOS R5, high key bright white tone, pink color grade, portrait 2:3 vertical"
    },

    # ── 독특/신선 🌈 ──────────────────────────────────────
    "bioluminescent": {
        "tag": "Bioluminescent",
        "subject": "a glowing deep sea goddess female model",
        "body": "ethereal slender figure, otherworldly presence, luminous skin",
        "outfit": "bioluminescent deep sea creature inspired gown, glowing patterns, organic flowing shapes",
        "material": "light-reactive glowing fabric, bioluminescent textile",
        "environment": "deep ocean environment, bioluminescent sea creatures, underwater darkness",
        "lighting": "bioluminescent blue-green glow, deep sea light, magical underwater illumination",
        "style": "deep sea fantasy editorial, bioluminescent fashion photography",
        "quality": "shot on Sony A7R V, cool blue color grade, cold steel tones, portrait 2:3 vertical"
    },
    "living_statue": {
        "tag": "Living Statue",
        "subject": "a marble goddess female model",
        "body": "statuesque figure, classical proportions, marble-smooth skin texture",
        "outfit": "Greco-Roman draped marble texture dress, classical goddess robes, sculptural fashion",
        "material": "marble-texture fabric, white stone-like material, classical draping",
        "environment": "ancient Greek museum, classical sculpture hall, white marble columns",
        "lighting": "cold marble light, museum spotlight, classical sculpture lighting",
        "style": "living sculpture editorial, classical art meets fashion photography",
        "quality": "shot on Phase One XF IQ4, black and white photography, classic monochrome, portrait 2:3 vertical"
    },
    "hologram_ghost": {
        "tag": "Hologram Ghost",
        "subject": "a holographic ethereal female model",
        "body": "translucent ethereal figure, ghost-like presence, digital phantom",
        "outfit": "holographic translucent outfit, digital glitch patterns, futuristic ghost fashion",
        "material": "holographic translucent fabric, digital iridescent material",
        "environment": "dark digital void, floating data streams, cyber space",
        "lighting": "holographic blue-purple light, digital glow, translucent illumination",
        "style": "digital phantom editorial, holographic fashion photography",
        "quality": "shot on Nikon Z9, purple moody color grade, violet atmospheric tones, portrait 2:3 vertical"
    },
    "origami_couture": {
        "tag": "Origami Couture",
        "subject": "a structural avant-garde female model",
        "body": "tall slender figure, geometric posture, architectural presence",
        "outfit": "origami-inspired paper couture, geometric folded structure, architectural fashion",
        "material": "paper-like structured fabric, geometric folded textile, architectural material",
        "environment": "minimalist Japanese architecture, white geometric space, zen garden",
        "lighting": "clean directional light, sharp geometric shadows, minimal studio",
        "style": "Issey Miyake origami editorial, structural fashion photography",
        "quality": "shot on Hasselblad H6D, high key bright white tone, clean light, portrait 2:3 vertical"
    },
    "glitch_beauty": {
        "tag": "Glitch Beauty",
        "subject": "a digital glitch female model",
        "body": "sleek powerful figure, digital distortion, fragmented presence",
        "outfit": "glitch art fashion, digitally distorted patterns, cyberpunk editorial styling",
        "material": "glitch-print fabric, digital distortion textile, pixel pattern material",
        "environment": "corrupted digital space, glitch art environment, broken screen aesthetic",
        "lighting": "glitch light artifacts, corrupted neon, digital error atmosphere",
        "style": "glitch art editorial, digital corruption fashion photography",
        "quality": "shot on Sony A7R V, glitch art effect, digital distortion, portrait 2:3 vertical"
    },

    # ── Y2K/레트로 💿 ────────────────────────────────────
    "y2k_chrome": {
        "tag": "Y2K Chrome",
        "subject": "a Y2K era glamorous female model",
        "body": "slim toned figure, early 2000s energy, confident Y2K presence",
        "outfit": "Y2K chrome metallic outfit, low-rise pants, butterfly accessories, 2000s fashion",
        "material": "chrome metallic fabric, silver vinyl, Y2K iridescent material",
        "environment": "early 2000s aesthetic space, chrome furniture, futuristic Y2K interior",
        "lighting": "Y2K silver chrome light, metallic reflections, early 2000s glamour",
        "style": "Y2K fashion editorial, early 2000s nostalgia photography",
        "quality": "shot on Canon EOS R5, cool blue color grade, chrome tones, portrait 2:3 vertical"
    },
    "vaporwave_dream": {
        "tag": "Vaporwave Dream",
        "subject": "a vaporwave aesthetic female model",
        "body": "slender dreamy figure, retro-future presence, aesthetic energy",
        "outfit": "vaporwave inspired outfit, pastel purple and pink, retro-future fashion",
        "material": "pastel gradient fabric, retro synthetic material",
        "environment": "vaporwave digital sunset, Greek columns, palm trees, retro-future landscape",
        "lighting": "purple and pink gradient light, sunset neon, vaporwave atmosphere",
        "style": "vaporwave aesthetic editorial, retro-future fashion photography",
        "quality": "shot on Sony A7R V, purple moody color grade, violet atmospheric tones, portrait 2:3 vertical"
    },
    "disco_goddess": {
        "tag": "Disco Goddess",
        "subject": "a 1970s disco goddess female model",
        "body": "glamorous curves, 70s goddess energy, long legs, disco ready",
        "outfit": "1970s disco sequin jumpsuit, bell bottoms, platform shoes, glitter everywhere",
        "material": "mirror-ball sequins, silver metallic disco fabric",
        "environment": "Studio 54 disco era nightclub, mirror ball, dance floor lights",
        "lighting": "disco ball light patterns, warm amber club lighting, mirror reflections",
        "style": "1970s disco editorial, Studio 54 fashion photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },
    "80s_power": {
        "tag": "80s Power",
        "subject": "a 1980s power woman female model",
        "body": "tall powerful figure, 80s power silhouette, strong presence",
        "outfit": "1980s power shoulder blazer, neon colors, big hair energy, bold accessories",
        "material": "structured power fabric, 80s bold textile, neon synthetic material",
        "environment": "1980s corporate power aesthetic, glass tower, city power view",
        "lighting": "dramatic 80s lighting, bold shadows, power ambiance",
        "style": "1980s power fashion editorial, retro corporate glamour photography",
        "quality": "shot on Nikon Z9, cinematic teal and orange color grade, Hollywood film look, portrait 2:3 vertical"
    },

    # ── 자연/보태니컬 🌿 ──────────────────────────────────
    "forest_witch": {
        "tag": "Forest Witch",
        "subject": "a mysterious forest witch female model",
        "body": "ethereal slender figure, mysterious dark presence, witchy energy",
        "outfit": "dark botanical witch dress, forest herbs and flowers, mystical accessories",
        "material": "dark velvet, botanical fabric with pressed flowers, mystical textile",
        "environment": "ancient dark forest, twisted trees, magical mushroom circle, moonlit woods",
        "lighting": "moonlight filtering through trees, magical forest glow, mysterious shadows",
        "style": "dark botanical editorial, forest witch fashion photography",
        "quality": "shot on Canon EOS R5, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },
    "coral_reef": {
        "tag": "Coral Reef",
        "subject": "a underwater coral goddess female model",
        "body": "flowing ethereal figure, underwater goddess presence",
        "outfit": "coral reef inspired gown, ocean creature details, flowing underwater fashion",
        "material": "iridescent sea-inspired fabric, coral texture material, ocean colors",
        "environment": "vibrant coral reef, tropical underwater world, colorful sea life",
        "lighting": "underwater caustic light, turquoise ocean glow, tropical underwater illumination",
        "style": "underwater coral editorial, ocean fashion photography",
        "quality": "shot on Hasselblad H6D, emerald green color grade, rich jewel tones, portrait 2:3 vertical"
    },
    "aurora_spirit": {
        "tag": "Aurora Spirit",
        "subject": "a northern lights spirit female model",
        "body": "ethereal tall figure, luminous presence, spirit-like grace",
        "outfit": "aurora-inspired flowing gown, northern lights colors, magical spirit fashion",
        "material": "color-shifting iridescent fabric, aurora-inspired textile",
        "environment": "Arctic tundra, dramatic northern lights, snow covered landscape",
        "lighting": "aurora borealis green and purple light, arctic glow, magical sky illumination",
        "style": "aurora spirit editorial, northern lights fashion photography",
        "quality": "shot on Phase One XF IQ4, cool blue color grade, cold steel tones, portrait 2:3 vertical"
    },
    "desert_oracle": {
        "tag": "Desert Oracle",
        "subject": "a mysterious desert oracle female model",
        "body": "tall commanding figure, ancient wisdom presence, oracle energy",
        "outfit": "ancient desert oracle robes, mystical symbols, layered desert fashion",
        "material": "sand-colored layered linen, mystical embroidered fabric",
        "environment": "ancient desert ruins, sand dunes at sunset, mysterious stone structures",
        "lighting": "harsh desert sun, golden sand glow, mystical sunset atmosphere",
        "style": "ancient oracle editorial, mystical desert fashion photography",
        "quality": "shot on Sony A7R V, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },

    # ── 역사/문명 🏺 ──────────────────────────────────────
    "cleopatra_gold": {
        "tag": "Cleopatra Gold",
        "subject": "a Cleopatra-inspired Egyptian queen female model",
        "body": "statuesque powerful figure, Egyptian queen proportions, commanding royal presence",
        "outfit": "ancient Egyptian gold couture, Cleopatra headdress, pharaoh jewelry, golden robes",
        "material": "hammered gold fabric, Egyptian linen, royal golden textile",
        "environment": "ancient Egyptian palace, golden columns, Nile river backdrop",
        "lighting": "Egyptian golden sun, warm amber light, ancient royal illumination",
        "style": "Cleopatra editorial, ancient Egyptian fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },
    "geisha_noir": {
        "tag": "Geisha Noir",
        "subject": "a modern dark geisha female model",
        "body": "graceful slender figure, Japanese aesthetic presence, dark glamour energy",
        "outfit": "modern dark geisha kimono, black and gold, contemporary Japanese fashion fusion",
        "material": "dark silk kimono fabric, gold embroidered textile, modern Japanese material",
        "environment": "modern Tokyo meets traditional Japan, dark Japanese garden, neon and lanterns",
        "lighting": "dramatic Japanese lantern light, dark atmospheric glow, noir shadows",
        "style": "modern geisha editorial, dark Japanese fashion photography",
        "quality": "shot on Fujifilm GFX 100S, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },
    "aztec_warrior": {
        "tag": "Aztec Warrior",
        "subject": "a fierce Aztec warrior goddess female model",
        "body": "powerful athletic figure, warrior goddess presence, fierce strength",
        "outfit": "Aztec warrior fashion, feather headdress, gold armor details, tribal couture",
        "material": "feather-trimmed fabric, gold hammered material, tribal textile",
        "environment": "ancient Aztec pyramid, Mexican jungle, dramatic sky",
        "lighting": "dramatic tropical sun, golden ancient light, warrior atmosphere",
        "style": "Aztec warrior editorial, ancient civilization fashion photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },
    "byzantine_empress": {
        "tag": "Byzantine Empress",
        "subject": "a Byzantine empress female model",
        "body": "regal statuesque figure, imperial presence, empress proportions",
        "outfit": "Byzantine gold mosaic gown, jewel encrusted crown, imperial purple and gold",
        "material": "Byzantine mosaic-inspired fabric, gold and purple imperial textile",
        "environment": "Byzantine palace interior, gold mosaic walls, Constantinople grandeur",
        "lighting": "Byzantine gold candlelight, mosaic reflection, imperial glow",
        "style": "Byzantine empress editorial, ancient imperial fashion photography",
        "quality": "shot on Phase One XF IQ4, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },
    "viking_queen": {
        "tag": "Viking Queen",
        "subject": "a fierce Viking queen female model",
        "body": "powerful tall figure, Norse warrior presence, fierce Nordic beauty",
        "outfit": "Viking queen armor and furs, Norse runes, warrior crown, battle-ready fashion",
        "material": "leather and fur, hammered metal fabric, Norse textile",
        "environment": "dramatic Norwegian fjord, Viking longship, stormy Nordic sky",
        "lighting": "dramatic Nordic storm light, fierce warrior atmosphere, Nordic glow",
        "style": "Viking queen editorial, Norse warrior fashion photography",
        "quality": "shot on Nikon Z9, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },

    # ── 다크/고딕 🦇 ──────────────────────────────────────
    "dark_academia": {
        "tag": "Dark Academia",
        "subject": "a dark academia aesthetic female model",
        "body": "slender intellectual figure, brooding presence, academic elegance",
        "outfit": "dark academia outfit, tweed blazer, plaid skirt, Oxford shoes, vintage books",
        "material": "tweed wool, plaid fabric, vintage academic textile",
        "environment": "Oxford university library, dark wood bookshelves, candlelit study",
        "lighting": "warm candlelight, dark academia atmosphere, moody library glow",
        "style": "dark academia editorial, intellectual aesthetic fashion photography",
        "quality": "shot on Leica SL2, vintage film grain, faded colors, analog photography look, portrait 2:3 vertical"
    },
    "gothic_romance": {
        "tag": "Gothic Romance",
        "subject": "a gothic romance female model",
        "body": "pale ethereal figure, gothic elegance, romantic darkness",
        "outfit": "gothic Victorian romance dress, black lace, corset, dramatic silhouette",
        "material": "black lace fabric, gothic velvet, romantic dark textile",
        "environment": "Victorian gothic mansion, rose garden at night, moonlit cemetery",
        "lighting": "moonlight through stained glass, gothic candle glow, romantic darkness",
        "style": "gothic romance editorial, Victorian dark fashion photography",
        "quality": "shot on Sony A7R V, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },
    "shadow_queen": {
        "tag": "Shadow Queen",
        "subject": "a powerful shadow queen female model",
        "body": "commanding powerful figure, shadow queen presence, dark dominance",
        "outfit": "shadow queen dramatic gown, dark sculptural couture, shadow-inspired fashion",
        "material": "ultra-matte black fabric, shadow-absorbing textile, void-like material",
        "environment": "dark dramatic throne room, shadow kingdom, dramatic void space",
        "lighting": "single rim light only, deep shadow atmosphere, dramatic darkness",
        "style": "shadow queen editorial, dark power fashion photography",
        "quality": "shot on Phase One XF IQ4, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },

    # ── 스포츠/액티브 🏊 ──────────────────────────────────
    "surfer_goddess": {
        "tag": "Surfer Goddess",
        "subject": "a surf goddess female model",
        "body": "athletic toned figure, sun-kissed surfer body, wave-ready fitness",
        "outfit": "luxury surf fashion, high-cut one-piece swimsuit, surf accessories, beach goddess",
        "material": "performance surf fabric, ocean-resistant material",
        "environment": "Bali surf beach, dramatic ocean waves, tropical paradise",
        "lighting": "golden surf sunset, ocean reflection, tropical golden hour",
        "style": "surf goddess editorial, luxury beach fashion photography",
        "quality": "shot on Canon EOS R5, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },
    "equestrian_glam": {
        "tag": "Equestrian Glam",
        "subject": "a luxury equestrian female model",
        "body": "tall elegant figure, equestrian posture, refined athletic presence",
        "outfit": "luxury equestrian fashion, riding boots, tailored jodhpurs, equestrian jacket",
        "material": "fine leather, tailored equestrian fabric, luxury riding textile",
        "environment": "English countryside estate, horse stable, polo field, green meadow",
        "lighting": "golden English countryside light, aristocratic atmosphere",
        "style": "equestrian luxury editorial, polo fashion photography",
        "quality": "shot on Hasselblad H6D, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },
    "fencer_noir": {
        "tag": "Fencer Noir",
        "subject": "a dark glamorous fencer female model",
        "body": "sleek athletic figure, fencer's precision, dark athletic elegance",
        "outfit": "dark glamour fencing fashion, sleek protective mask, noir athletic couture",
        "material": "dark matte performance fabric, noir athletic textile",
        "environment": "dramatic dark fencing hall, single spotlight, noir atmosphere",
        "lighting": "dramatic single spotlight, dark fencing atmosphere, noir shadows",
        "style": "fencer noir editorial, dark athletic fashion photography",
        "quality": "shot on Sony A7R V, dark moody color grade, deep shadows, portrait 2:3 vertical"
    },
}


def main():
    print("\n  ✦ LumineX v3.5 신규 프리셋 추가 시작...\n")
    created = 0
    skipped = 0

    for name, data in NEW_PRESETS_V35.items():
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
    print("  📋 카테고리:")
    print("  - 귀엽고 발랄 (harajuku/candy/pastel/bubble_tea/doll_house) × 5")
    print("  - 독특/신선 (bioluminescent/hologram/origami/glitch 등)       × 5")
    print("  - Y2K/레트로 (y2k_chrome/vaporwave/disco/80s)                 × 4")
    print("  - 자연/보태니컬 (forest_witch/coral/aurora/desert)             × 4")
    print("  - 역사/문명 (cleopatra/geisha/aztec/byzantine/viking)          × 5")
    print("  - 다크/고딕 (dark_academia/gothic_romance/shadow_queen)        × 3")
    print("  - 스포츠/액티브 (surfer/equestrian/fencer)                     × 3")
    print(f"  총 29개 신규 프리셋\n")


if __name__ == "__main__":
    main()