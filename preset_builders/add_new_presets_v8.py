import os
import json

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")

NEW_PRESETS_V7 = {

    # ─────────────────────────────────────────────
    # 🌫️ 빛/소재/컨셉 우회 전략 — 자연현상
    # ─────────────────────────────────────────────

    "mist_goddess": {
        "name": "안개 여신 — 수증기 속 실루엣",
        "outfit": "diaphanous white fabric dissolving into mist, ethereal veiling",
        "material": "water vapor, fine mist particles, soft translucent silk",
        "environment": "misty highland lake at dawn, fog rolling over still water",
        "lighting": "diffused dawn light through thick fog, soft luminous haze",
        "style": "fine art ethereal photography, dreamlike atmospheric editorial",
        "quality": "shot on Hasselblad medium format, mist diffusion filter, portrait 2:3"
    },

    "aurora_drape": {
        "name": "오로라 드레이프 — 북극광이 몸을 감싸는",
        "outfit": "aurora borealis light draped over figure like flowing silk, luminous curtain",
        "material": "atmospheric light phenomenon, ionized particles, iridescent color bands",
        "environment": "arctic tundra, vast dark sky, snow-covered landscape below",
        "lighting": "green and violet aurora illumination, cold starlight, dramatic sky glow",
        "style": "National Geographic fine art, surreal natural phenomenon photography",
        "quality": "long exposure astrophotography, cinematic color grade, portrait 2:3"
    },

    "sandstorm_veil": {
        "name": "모래바람 베일 — 사막 폭풍 속 실루엣",
        "outfit": "golden sand particles swirling around figure, desert wind draping",
        "material": "fine desert sand, golden dust particles, warm particulate veil",
        "environment": "Sahara desert at golden hour, sandstorm approaching horizon",
        "lighting": "warm amber sun filtered through dust, golden particle glow",
        "style": "dramatic desert editorial, cinematic sand storm fashion photography",
        "quality": "shot on Canon EOS R5, warm desert film grade, portrait 2:3"
    },

    "eclipse_body": {
        "name": "일식 역광 — 코로나 빛 테두리",
        "outfit": "total solar eclipse corona outlining silhouette, celestial light halo",
        "material": "solar corona plasma, atmospheric diffraction, celestial light",
        "environment": "open desert plain during total solar eclipse, darkened sky",
        "lighting": "solar corona rim lighting, diamond ring effect, dramatic eclipse shadow",
        "style": "astronomical fine art photography, once-in-lifetime light phenomenon",
        "quality": "ultra sharp silhouette, corona glow detail, portrait 2:3 vertical"
    },

    "bioluminescence": {
        "name": "생물발광 — 심해 빛으로 바디 라인",
        "outfit": "bioluminescent ocean light painting figure contours, glowing sea foam",
        "material": "dinoflagellate blue light, phosphorescent sea water, living light",
        "environment": "midnight beach with bioluminescent waves, dark tropical coast",
        "lighting": "electric blue bioluminescent glow, zero ambient light, pure bio-light",
        "style": "surreal nature fine art, scientific wonder photography",
        "quality": "long exposure night photography, cyan bioluminescent tone, portrait 2:3"
    },

    # ─────────────────────────────────────────────
    # 🪞 반사/굴절 — 초현실 효과
    # ─────────────────────────────────────────────

    "liquid_mirror": {
        "name": "액체 거울 — 수면 위 반사 실루엣",
        "outfit": "figure reflected and dissolved in perfectly still mercury-like water surface",
        "material": "mirror-perfect water surface, liquid reflection, inverted symmetry",
        "environment": "infinite flat salt lake, Uyuni-style mirror surface, cloudless sky",
        "lighting": "perfect sky reflection, horizon-less environment, pure mirror light",
        "style": "surreal reflective photography, Uyuni salt flat editorial",
        "quality": "shot on Phase One XT, perfect horizontal symmetry, portrait 2:3"
    },

    "ice_refraction": {
        "name": "빙하 굴절 — 얼음 속 형상",
        "outfit": "figure seen through thick glacial ice, prismatic refraction distorting form",
        "material": "ancient glacial ice, blue-white crystalline structure, deep ice clarity",
        "environment": "Icelandic glacier ice cave, blue ice tunnel, frozen stillness",
        "lighting": "refracted blue light through ice, cold crystal luminosity, deep cave glow",
        "style": "glacial fine art photography, frozen wonder editorial",
        "quality": "shot on Leica SL2, ice blue color grade, portrait 2:3 vertical"
    },

    "shattered_glass": {
        "name": "유리 파편 — 깨진 거울 속 분열된 형상",
        "outfit": "figure fragmented across hundreds of glass shards, kaleidoscopic reflection",
        "material": "shattered mirror fragments, glass shards, reflective splinter array",
        "environment": "black studio with suspended glass fragment installation",
        "lighting": "single dramatic spotlight fracturing through glass, prismatic scatter",
        "style": "conceptual fine art photography, broken mirror editorial",
        "quality": "ultra sharp glass detail, cinematic contrast, portrait 2:3"
    },

    "mercury_pool": {
        "name": "수은 풀 — 액체 금속 반영",
        "outfit": "figure emerging from or reflected in liquid silver mercury surface",
        "material": "liquid mercury silver, metallic fluid surface, mirror liquid",
        "environment": "dark industrial space, mercury pool floor, minimal backdrop",
        "lighting": "overhead silver light on mercury, reflective metallic ambiance",
        "style": "conceptual surrealist photography, liquid metal editorial",
        "quality": "shot on Sony A1, silver metallic grade, portrait 2:3 vertical"
    },

    # ─────────────────────────────────────────────
    # 🎨 예술/오브제 맥락화
    # ─────────────────────────────────────────────

    "living_sculpture": {
        "name": "살아있는 조각 — 대리석이 깨어나는",
        "outfit": "figure transitioning between white marble sculpture and living flesh",
        "material": "Carrara white marble, stone texture dissolving into skin, classical sculpture",
        "environment": "Renaissance museum hall, classical sculpture gallery, dramatic columns",
        "lighting": "museum spotlight, chiaroscuro contrast, sculpture illumination",
        "style": "fine art classical sculpture photography, Pygmalion concept editorial",
        "quality": "shot on Hasselblad H6D, marble-white tone, portrait 2:3"
    },

    "ink_wash_body": {
        "name": "수묵 바디 — 먹물이 번지듯",
        "outfit": "East Asian ink wash painting style, sumi-e brushwork forming figure",
        "material": "Japanese sumi ink, rice paper texture, flowing ink wash medium",
        "environment": "minimal white paper-like space, brushstroke environmental elements",
        "lighting": "soft diffused paper-white light, ink shadow depth",
        "style": "sumi-e fine art photography, East Asian ink painting aesthetic",
        "quality": "black and white with ink tones, artistic brush texture, portrait 2:3"
    },

    "fresco_awakening": {
        "name": "프레스코 각성 — 고대 벽화에서 깨어나는",
        "outfit": "figure emerging from Renaissance fresco painting, classical drapery",
        "material": "aged fresco plaster texture, ochre and earth pigments, painted fabric",
        "environment": "ancient Roman villa wall, crumbling fresco surface, archaeological site",
        "lighting": "warm amber ancient light, fresco pigment illumination, ochre glow",
        "style": "fine art archaeological editorial, living painting concept",
        "quality": "aged fresco color palette, classical composition, portrait 2:3"
    },

    # ─────────────────────────────────────────────
    # 🌊 소재/물성 — 우회 드레이핑
    # ─────────────────────────────────────────────

    "liquid_gold_pour": {
        "name": "액체 황금 — 몸 위로 흘러내리는",
        "outfit": "molten liquid gold flowing and draping over figure, gilded pour art",
        "material": "liquid 24k gold, molten metallic pour, gilded draping metal",
        "environment": "dark luxury studio, black velvet backdrop, minimal gold setting",
        "lighting": "warm gold reflective light, metallic sheen illumination, dramatic contrast",
        "style": "luxury fine art photography, liquid gold editorial, Klimt-inspired",
        "quality": "shot on Phase One, rich gold metallic grade, portrait 2:3 vertical"
    },

    "petal_storm": {
        "name": "꽃잎 폭풍 — 꽃잎이 몸을 휘감는",
        "outfit": "thousands of rose and peony petals swirling and draping around figure",
        "material": "fresh flower petals, organic floral confetti, botanical cascade",
        "environment": "garden or studio with petal storm, blooming floral installation",
        "lighting": "warm garden light filtering through petals, soft floral diffusion",
        "style": "romantic fine art photography, floral storm editorial",
        "quality": "shot on Canon EOS R5, warm bloom color grade, portrait 2:3"
    },

    "feather_cascade": {
        "name": "깃털 캐스케이드 — 깃털이 쏟아지며 가리는",
        "outfit": "thousands of white and black feathers cascading and draping over figure",
        "material": "luxury plume feathers, swan down, exotic bird plumage cascade",
        "environment": "dark studio with falling feather installation, feather floor",
        "lighting": "dramatic spotlight through feather shower, soft feather diffusion",
        "style": "high fashion feather editorial, luxury plume photography",
        "quality": "shot on Hasselblad, feather texture detail, portrait 2:3 vertical"
    },

    "smoke_veil": {
        "name": "연기 베일 — 연기가 드레이핑처럼",
        "outfit": "dramatic smoke tendrils wrapping and draping around figure like silk veil",
        "material": "white and grey smoke, atmospheric vapor, flowing smoke medium",
        "environment": "dark studio with controlled smoke machine, minimal backdrop",
        "lighting": "single backlight through smoke, volumetric light beams, smoke glow",
        "style": "cinematic smoke editorial, dramatic atmospheric photography",
        "quality": "shot on Sony A1, high contrast cinematic grade, portrait 2:3"
    },

    "cobweb_drape": {
        "name": "거미줄 레이스 — 전신을 감싸는",
        "outfit": "intricate spider web lace draping over entire figure, gothic organic veil",
        "material": "natural spider silk, gossamer web structure, organic lace medium",
        "environment": "dark forest at dawn, dew-covered spider webs, gothic natural setting",
        "lighting": "backlit morning dew on webs, gossamer light refraction, dramatic rim",
        "style": "dark nature fine art photography, gothic organic editorial",
        "quality": "macro spider silk detail, blue-grey morning tone, portrait 2:3"
    },

    # ─────────────────────────────────────────────
    # ⚡ 에너지/현상 — 추상화
    # ─────────────────────────────────────────────

    "plasma_aura": {
        "name": "플라즈마 오라 — 에너지가 감싸는",
        "outfit": "plasma energy aura enveloping figure, electric field visualization",
        "material": "ionized plasma light, electric field energy, luminous corona",
        "environment": "dark laboratory or void space, plasma containment aesthetic",
        "lighting": "plasma glow illumination, electric purple and blue light, energy aura",
        "style": "sci-fi fine art photography, energy field editorial",
        "quality": "plasma color grade, electric luminosity, portrait 2:3 vertical"
    },

    "lightning_body": {
        "name": "번개 바디 — 방전이 바디 라인을 그리는",
        "outfit": "Lichtenberg figure lightning tracing body contours, electric discharge art",
        "material": "electrical discharge patterns, plasma channels, fractal lightning",
        "environment": "dark void or storm environment, lightning storm backdrop",
        "lighting": "pure lightning illumination, electric flash, dramatic discharge glow",
        "style": "high voltage fine art, electric body photography",
        "quality": "ultra high speed capture, electric blue tone, portrait 2:3"
    },

    "void_emergence": {
        "name": "어둠 속 출현 — 빛이 형상을 조각하는",
        "outfit": "figure emerging from absolute darkness, light sculpting form from void",
        "material": "pure darkness, single light source, void and luminosity contrast",
        "environment": "completely dark studio, infinity black backdrop, zero ambient light",
        "lighting": "single sculpting light carving figure from darkness, Rembrandt extreme",
        "style": "fine art chiaroscuro photography, emergence from darkness editorial",
        "quality": "maximum contrast black, pure shadow and light, portrait 2:3"
    },

    "heat_shimmer": {
        "name": "아지랑이 — 열 굴절로 일렁이는 형상",
        "outfit": "figure distorted by heat shimmer and thermal refraction, mirage aesthetic",
        "material": "atmospheric thermal refraction, heat wave distortion, mirage medium",
        "environment": "desert highway or salt flat at peak midday heat",
        "lighting": "intense overhead midday sun, heat haze atmosphere, bleached light",
        "style": "mirage editorial, desert heat distortion fine art photography",
        "quality": "heat distortion effect, bleached desert tone, portrait 2:3"
    },

    # ─────────────────────────────────────────────
    # 🏛️ 신화/의식 맥락
    # ─────────────────────────────────────────────

    "ritual_ash": {
        "name": "의식 재 — 흰 재로 바디 페인팅",
        "outfit": "sacred white ash body paint covering figure in ritual ceremony markings",
        "material": "fine white ash, ceremonial pigment, sacred ritual medium",
        "environment": "ancient volcanic landscape, ritual fire ceremony, sacred site",
        "lighting": "ceremonial fire glow, warm amber flame light, sacred illumination",
        "style": "ethnographic fine art photography, sacred ritual editorial",
        "quality": "warm ritual fire tone, ash texture detail, portrait 2:3 vertical"
    },

    "oracle_smoke": {
        "name": "신탁 연기 — 델피 신탁의 예언자",
        "outfit": "white priestess robes dissolving into prophetic smoke, oracle aesthetic",
        "material": "sacred incense smoke, prophetic vapor, ceremonial white fabric",
        "environment": "ancient Greek temple ruins, oracle chamber, stone columns",
        "lighting": "sacred shaft of light through smoke, golden divine illumination",
        "style": "ancient Greek fine art photography, oracle myth editorial",
        "quality": "warm ancient golden grade, smoke diffusion, portrait 2:3"
    },

    "moonrise_ceremony": {
        "name": "달빛 의식 — 달이 실루엣을 비추는",
        "outfit": "figure in moonrise ceremony, silver moonlight creating luminous silhouette",
        "material": "silver moonlight, lunar illumination, celestial light medium",
        "environment": "stone circle or ancient sacred site under full moon rising",
        "lighting": "pure silver moonlight, blue-white lunar illumination, dramatic moon rise",
        "style": "lunar fine art photography, moon ceremony editorial",
        "quality": "silver moonlight color grade, lunar clarity, portrait 2:3"
    },

    # ─────────────────────────────────────────────
    # 💋 관능적 바디 페인팅 — 컨셉 우회 선별
    # ─────────────────────────────────────────────

    "klimt_gold_body": {
        "name": "클림트 황금 — 황금 모자이크 전신 장식",
        "outfit": "Gustav Klimt golden mosaic pattern painted across figure, Art Nouveau body art",
        "material": "gold leaf, Byzantine mosaic pattern, Art Nouveau decorative paint",
        "environment": "ornate gold Byzantine interior, Klimt-inspired golden backdrop",
        "lighting": "warm golden ambient glow, mosaic reflective light, Art Nouveau luminosity",
        "style": "Gustav Klimt fine art body painting editorial, Vienna Secession aesthetic",
        "quality": "rich gold leaf texture, Klimt color palette, portrait 2:3 vertical"
    },

    "oil_slick_body": {
        "name": "오일 슬릭 — 무지개빛 기름막 전신",
        "outfit": "iridescent oil slick paint covering figure, rainbow petroleum sheen body art",
        "material": "iridescent oil paint, petroleum rainbow film, holographic body paint",
        "environment": "dark wet urban surface, rain-slicked pavement, neon night city",
        "lighting": "neon city light refracting through oil paint, iridescent rainbow glow",
        "style": "cyberpunk body art photography, urban iridescent editorial",
        "quality": "oil slick iridescent grade, neon urban tone, portrait 2:3"
    },

    "bioluminescent_ink": {
        "name": "생물발광 잉크 — 발광 패턴 바디아트",
        "outfit": "bioluminescent deep sea creature patterns painted across figure, glowing marine art",
        "material": "UV-reactive bioluminescent paint, deep sea organism pattern, living light ink",
        "environment": "pure dark studio, UV black light environment, zero ambient light",
        "lighting": "UV black light only, pure bioluminescent glow, electric blue-green emission",
        "style": "deep sea bioluminescence body art, UV fine art photography",
        "quality": "pure UV glow, deep sea color palette, portrait 2:3 vertical"
    },

    "liquid_chrome_body": {
        "name": "크롬 바디 — 액체 금속이 흘러내리는",
        "outfit": "liquid chrome silver metallic paint poured and flowing over figure",
        "material": "liquid chrome body paint, metallic silver medium, molten metal aesthetic",
        "environment": "pure white or pure black studio, minimal chrome backdrop",
        "lighting": "high contrast studio light on chrome surface, metallic reflection",
        "style": "high fashion metallic body art, chrome editorial photography",
        "quality": "pure chrome reflection, high contrast metallic grade, portrait 2:3"
    },

    "henna_goddess_body": {
        "name": "헤나 여신 — 정교한 인도 레이스 패턴",
        "outfit": "full body intricate henna mehendi patterns, Indian bridal body art lace",
        "material": "traditional henna paste, mehendi ink, intricate botanical lace pattern",
        "environment": "Rajasthan palace courtyard, Indian luxury architectural setting",
        "lighting": "warm golden Indian light, palace courtyard ambiance, jewel tone illumination",
        "style": "Indian fine art body painting photography, maharani goddess editorial",
        "quality": "henna warm brown tone, intricate pattern detail, portrait 2:3"
    },

}


def main():
    print("\n  ✦ LumineX v7.0 프리셋 추가 시작...\n")
    created = 0
    skipped = 0

    for name, data in NEW_PRESETS_V7.items():
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
    print("  - 🌫️ 자연현상 우회 (mist/aurora/sandstorm/eclipse/bioluminescence) × 5")
    print("  - 🪞 반사/굴절   (liquid_mirror/ice_refraction/shattered_glass/mercury) × 4")
    print("  - 🎨 예술 맥락화 (living_sculpture/ink_wash/fresco_awakening)          × 3")
    print("  - 🌊 소재 드레이핑(liquid_gold/petal_storm/feather/smoke/cobweb)       × 5")
    print("  - ⚡ 에너지/현상  (plasma_aura/lightning_body/void_emergence/heat)     × 4")
    print("  - 🏛️ 신화/의식   (ritual_ash/oracle_smoke/moonrise_ceremony)          × 3")
    print("  - 💋 관능 바디페인팅(klimt/oil_slick/bioluminescent_ink/chrome/henna) × 5")
    print(f"  총 29개 신규 프리셋\n")


if __name__ == "__main__":
    main()