import os
import json

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")

NEW_PRESETS_V9 = {

    # ─────────────────────────────────────────────
    # 🎨 명화/아트 스타일 바디페인팅
    # ─────────────────────────────────────────────

    "vangogh_body": {
        "name": "반 고흐 바디 — 별이 빛나는 밤 소용돌이",
        "outfit": "Van Gogh Starry Night swirling brushstroke patterns painted across entire body",
        "material": "impasto oil paint texture, swirling cobalt blue and gold brushstrokes",
        "environment": "dark night sky with swirling stars, Provence village silhouette",
        "lighting": "moonlit night illumination, Van Gogh warm yellow glow, starlight",
        "style": "Post-Impressionist fine art body painting, World Body Painting Festival",
        "quality": "shot on Hasselblad H6D, Van Gogh color palette, portrait 2:3 vertical"
    },

    "monet_bloom": {
        "name": "모네 블룸 — 수련 연못이 피부에 번지는",
        "outfit": "Claude Monet water lily pond painted across figure, impressionist bloom pattern",
        "material": "soft impressionist brushwork, pastel water lily pigments, pond reflection",
        "environment": "Giverny garden pond, weeping willow reflections, morning mist",
        "lighting": "soft diffused morning light, impressionist haze, garden luminosity",
        "style": "Impressionist fine art body painting, Monet garden editorial",
        "quality": "shot on Leica SL2, soft pastel impressionist grade, portrait 2:3"
    },

    "pollock_splash": {
        "name": "폴록 스플래시 — 액션페인팅 드리핑",
        "outfit": "Jackson Pollock action painting drip art covering entire figure, chaotic paint splatter",
        "material": "dripped enamel paint, spontaneous action painting medium, layered paint drips",
        "environment": "artist studio, paint-splattered floor, raw creative space",
        "lighting": "dramatic studio spotlight, raw industrial illumination, artist light",
        "style": "Abstract Expressionist body painting, action painting editorial",
        "quality": "shot on Canon EOS R5, raw paint texture detail, portrait 2:3 vertical"
    },

    "broken_porcelain": {
        "name": "깨진 도자기 — 긴츠기 금 균열",
        "outfit": "kintsugi broken porcelain gold seam pattern across figure, golden crack repair art",
        "material": "white porcelain glaze with golden kintsugi repair lines, Japanese ceramic art",
        "environment": "minimalist Japanese tea ceremony space, white studio, zen aesthetic",
        "lighting": "soft diffused Japanese studio light, gold seam reflective glow",
        "style": "kintsugi philosophy fine art body painting, Japanese aesthetic editorial",
        "quality": "shot on Phase One XT, white and gold minimal grade, portrait 2:3"
    },

    "marble_veins": {
        "name": "대리석 결 — 대리석 결이 피부에 흐르는",
        "outfit": "Carrara marble veining pattern flowing across entire figure, stone texture body art",
        "material": "white marble with grey and gold veining, classical stone texture",
        "environment": "classical sculpture museum, white marble columns, Renaissance interior",
        "lighting": "museum sculpture lighting, marble surface reflectance, classical illumination",
        "style": "classical marble sculpture body art, museum fine art editorial",
        "quality": "shot on Hasselblad, cool marble white tone, portrait 2:3 vertical"
    },

    "munch_scream": {
        "name": "뭉크 절규 — 표현주의 소용돌이 패턴",
        "outfit": "Edvard Munch Scream expressionist swirling landscape painted across figure",
        "material": "expressionist oil paint, anxiety-swirl brushwork, Munch color palette",
        "environment": "fjord bridge at sunset, expressionist swirling sky, dramatic landscape",
        "lighting": "blood red expressionist sunset, dramatic anxiety-inducing sky glow",
        "style": "Expressionist fine art body painting, Munch aesthetic editorial",
        "quality": "shot on Sony A1, expressionist red-orange grade, portrait 2:3"
    },

    "dali_surreal": {
        "name": "달리 초현실 — 녹아내리는 시계 패턴",
        "outfit": "Salvador Dali surrealist melting clock and dreamscape painted across figure",
        "material": "surrealist oil paint, melting forms, Dali trompe-l'oeil medium",
        "environment": "Catalan landscape, infinite desert plain, surrealist dreamscape",
        "lighting": "harsh Mediterranean sun, surrealist theatrical lighting, dream light",
        "style": "Surrealist fine art body painting, Dali dreamscape editorial",
        "quality": "shot on Leica Q2, warm surrealist desert grade, portrait 2:3"
    },

    "mucha_nouveau": {
        "name": "무하 아르누보 — 장식적 선 전신",
        "outfit": "Alphonse Mucha Art Nouveau decorative botanical patterns covering entire figure",
        "material": "Art Nouveau line art, flowing botanical ornament, pastel decorative medium",
        "environment": "Belle Époque Parisian interior, ornate Art Nouveau architecture",
        "lighting": "warm Belle Époque gaslight, Art Nouveau decorative ambiance",
        "style": "Mucha Art Nouveau fine art body painting, decorative editorial",
        "quality": "shot on Hasselblad H6D, warm Art Nouveau pastel grade, portrait 2:3"
    },

    "hokusai_wave": {
        "name": "호쿠사이 파도 — 일본 목판화 파도 전신",
        "outfit": "Hokusai Great Wave woodblock print pattern covering entire figure, ukiyo-e body art",
        "material": "Japanese woodblock ink, ukiyo-e blue wave pattern, Edo period print medium",
        "environment": "Mount Fuji coastal view, dramatic ocean waves, Japanese landscape",
        "lighting": "dramatic Japanese coastal light, Fuji backdrop, ukiyo-e atmosphere",
        "style": "Hokusai ukiyo-e fine art body painting, Japanese woodblock editorial",
        "quality": "shot on Canon EOS R5, Prussian blue woodblock grade, portrait 2:3"
    },

    "kandinsky_abstract": {
        "name": "칸딘스키 추상 — 기하학 컬러 전신",
        "outfit": "Wassily Kandinsky abstract geometric composition painted across entire figure",
        "material": "primary color geometric shapes, Bauhaus abstract medium, bold color blocks",
        "environment": "Bauhaus school studio, geometric abstract backdrop, modernist space",
        "lighting": "clean Bauhaus studio light, primary color reflections, modernist illumination",
        "style": "Kandinsky abstract fine art body painting, Bauhaus editorial",
        "quality": "shot on Phase One, primary color Bauhaus grade, portrait 2:3 vertical"
    },

    # ─────────────────────────────────────────────
    # 🌿 자연물 패턴 바디페인팅
    # ─────────────────────────────────────────────

    "coral_reef": {
        "name": "산호초 — 컬러풀 산호 패턴 전신",
        "outfit": "vibrant coral reef ecosystem painted across entire figure, tropical marine body art",
        "material": "coral polyp texture, tropical fish pattern, reef organism pigments",
        "environment": "crystal clear tropical ocean, coral reef underwater, turquoise water",
        "lighting": "underwater caustic light, tropical ocean luminosity, reef color refraction",
        "style": "marine biology fine art body painting, coral reef editorial",
        "quality": "shot on Hasselblad, tropical turquoise grade, portrait 2:3"
    },

    "leopard_dissolve": {
        "name": "레오파드 디졸브 — 표범 무늬가 피부와 녹아드는",
        "outfit": "leopard spot pattern seamlessly dissolving into and merging with skin texture",
        "material": "natural leopard melanin pattern, skin-merging camouflage, organic spot medium",
        "environment": "African savanna golden grass, wild nature, big cat habitat",
        "lighting": "African golden hour, dappled savanna light, wild nature illumination",
        "style": "wildlife fine art body painting, nature camouflage editorial",
        "quality": "shot on Canon EOS R5, warm savanna golden grade, portrait 2:3"
    },

    "peacock_feather": {
        "name": "공작 깃털 — 아이리데슨트 깃털 전신",
        "outfit": "iridescent peacock feather eye patterns covering entire figure, avian body art",
        "material": "peacock feather iridescent pigment, eye pattern medium, teal and gold plumage",
        "environment": "lush garden with peacocks, ornate palace garden, exotic botanical setting",
        "lighting": "warm garden light on iridescent feather, color-shifting luminosity",
        "style": "peacock fine art body painting, exotic avian editorial",
        "quality": "shot on Leica SL2, iridescent teal-gold grade, portrait 2:3 vertical"
    },

    "snake_scale": {
        "name": "뱀 비늘 — 메탈릭 비늘 패턴 전신",
        "outfit": "metallic snake scale pattern covering entire figure, reptilian body art",
        "material": "iridescent reptile scale texture, metallic serpent skin medium, scale overlap pattern",
        "environment": "dark jungle or exotic reptile environment, mysterious forest",
        "lighting": "dramatic contrast light on metallic scales, reptilian sheen illumination",
        "style": "reptilian fine art body painting, serpentine editorial",
        "quality": "shot on Sony A1, dark metallic reptile grade, portrait 2:3"
    },

    "butterfly_wing": {
        "name": "나비 날개 — 나비 날개 패턴 전신",
        "outfit": "butterfly wing patterns from multiple species covering entire figure, lepidoptera body art",
        "material": "butterfly wing scale pigment, iridescent wing pattern, Morpho blue medium",
        "environment": "botanical garden, flower meadow, butterfly sanctuary",
        "lighting": "soft garden light on iridescent wing scales, nature luminosity",
        "style": "entomology fine art body painting, butterfly garden editorial",
        "quality": "shot on Hasselblad H6D, iridescent blue-orange grade, portrait 2:3"
    },

    "deep_ocean_map": {
        "name": "심해 지형도 — 해저 지형 등고선 전신",
        "outfit": "deep ocean floor topographic map contours covering entire figure, bathymetric body art",
        "material": "oceanographic map contour lines, deep blue bathymetric medium, ocean depth data",
        "environment": "dark deep sea environment, abyssal plain aesthetic, ocean darkness",
        "lighting": "deep sea pressure light, bioluminescent ambient glow, abyssal illumination",
        "style": "oceanographic fine art body painting, deep sea cartography editorial",
        "quality": "shot on Phase One, deep navy blue grade, portrait 2:3 vertical"
    },

    # ─────────────────────────────────────────────
    # ⚡ 과학/기술 패턴 바디페인팅
    # ─────────────────────────────────────────────

    "dna_helix": {
        "name": "DNA 나선 — 이중나선 전신",
        "outfit": "DNA double helix structure spiraling across entire figure, molecular biology body art",
        "material": "molecular biology illustration medium, phosphate backbone pattern, base pair color coding",
        "environment": "scientific laboratory, clean white research space, molecular aesthetic",
        "lighting": "clinical laboratory light, scientific precision illumination, clean white glow",
        "style": "molecular biology fine art body painting, science editorial",
        "quality": "shot on Leica SL2, clinical white and blue grade, portrait 2:3"
    },

    "star_map": {
        "name": "별자리 지도 — 별자리 전신",
        "outfit": "celestial star map constellation patterns covering entire figure, astronomical body art",
        "material": "gold and silver star point medium, constellation line art, nebula pigment",
        "environment": "dark observatory or open desert under night sky, astronomical setting",
        "lighting": "pure starlight illumination, Milky Way ambient glow, astronomical darkness",
        "style": "astronomical fine art body painting, celestial cartography editorial",
        "quality": "shot on Sony A1, deep space dark blue grade, portrait 2:3"
    },

    "neuron_network": {
        "name": "뉴런 네트워크 — 신경망 패턴 전신",
        "outfit": "neural network synapse firing patterns covering entire figure, neuroscience body art",
        "material": "bioluminescent neuron medium, synapse connection lines, electrical impulse pattern",
        "environment": "dark neuroscience laboratory, brain scan aesthetic, clinical dark space",
        "lighting": "electric synapse glow, neural impulse light, bioluminescent brain illumination",
        "style": "neuroscience fine art body painting, neural network editorial",
        "quality": "shot on Canon EOS R5, electric blue neural grade, portrait 2:3 vertical"
    },

    "topographic": {
        "name": "지형도 — 등고선 전신",
        "outfit": "topographic contour map lines covering entire figure, cartographic body art",
        "material": "survey map contour line medium, elevation gradient color, cartographic pigment",
        "environment": "mountain landscape or map room, geographic survey aesthetic",
        "lighting": "clean map room light, geographic survey illumination, contour shadow depth",
        "style": "cartographic fine art body painting, topographic editorial",
        "quality": "shot on Hasselblad, earth tone topographic grade, portrait 2:3"
    },

    "neon_circuit": {
        "name": "네온 회로 — 네온 회로기판 패턴",
        "outfit": "neon glowing circuit board traces covering entire figure, cyberpunk electronics body art",
        "material": "UV-reactive neon circuit trace medium, PCB pattern, electronic component art",
        "environment": "dark cyberpunk lab, electronic components backdrop, neon tech environment",
        "lighting": "UV black light on neon circuit traces, electric neon glow, cyberpunk illumination",
        "style": "cyberpunk electronics fine art body painting, circuit board editorial",
        "quality": "shot on Sony A1, neon circuit green-blue grade, portrait 2:3"
    },

    # ─────────────────────────────────────────────
    # 🏺 문명/부족 바디페인팅
    # ─────────────────────────────────────────────

    "maori_moko": {
        "name": "마오리 모코 — 전통 마오리 문신 전신",
        "outfit": "traditional Maori ta moko facial and body tattoo patterns covering entire figure",
        "material": "traditional Maori chisel-carved ink pattern, spiral koru medium, tribal identity art",
        "environment": "New Zealand volcanic landscape, Maori marae ceremonial space",
        "lighting": "dramatic Pacific island light, ceremonial fire glow, volcanic landscape",
        "style": "Maori cultural fine art body painting, indigenous identity editorial",
        "quality": "shot on Canon EOS R5, warm volcanic earth grade, portrait 2:3"
    },

    "aztec_warrior": {
        "name": "아즈텍 전사 — 기하학 전사 문양 전신",
        "outfit": "Aztec geometric warrior calendar and serpent god patterns covering entire figure",
        "material": "Aztec codex pigment, geometric sun calendar medium, warrior ceremonial paint",
        "environment": "Teotihuacan pyramid ruins, Mesoamerican ceremonial site, ancient Mexico",
        "lighting": "intense Mexican sun on pyramid, ancient ceremonial fire, Aztec gold glow",
        "style": "Aztec cultural fine art body painting, Mesoamerican warrior editorial",
        "quality": "shot on Phase One, warm terracotta Aztec grade, portrait 2:3 vertical"
    },

    "egypt_hieroglyph": {
        "name": "이집트 상형문자 — 황금 상형문자 전신",
        "outfit": "ancient Egyptian hieroglyphs and cartouche patterns covering entire figure in gold",
        "material": "Egyptian gold leaf hieroglyph medium, lapis lazuli accent, papyrus pattern",
        "environment": "Valley of the Kings tomb interior, Egyptian temple, ancient hieroglyph walls",
        "lighting": "warm torch light on gold hieroglyphs, ancient Egyptian temple glow",
        "style": "Egyptology fine art body painting, pharaonic editorial",
        "quality": "shot on Hasselblad H6D, warm Egyptian gold grade, portrait 2:3"
    },

    "celtic_knotwork": {
        "name": "켈틱 매듭 — 켈틱 매듭 문양 전신",
        "outfit": "intricate Celtic knotwork interlace patterns covering entire figure, endless knot body art",
        "material": "Celtic illuminated manuscript ink, interlace knot medium, Book of Kells pattern",
        "environment": "ancient Irish stone circle, Celtic monastery ruins, misty highland",
        "lighting": "misty Celtic morning light, ancient stone circle atmosphere, druid ambiance",
        "style": "Celtic cultural fine art body painting, illuminated manuscript editorial",
        "quality": "shot on Leica SL2, cool misty Celtic grade, portrait 2:3"
    },

    "polynesian_tribal": {
        "name": "폴리네시안 부족 — 폴리네시아 부족 문양 전신",
        "outfit": "Polynesian tribal tattoo patterns covering entire figure, Pacific island body art",
        "material": "traditional Polynesian tattoo ink, tapa cloth pattern medium, ocean wave motif",
        "environment": "Pacific island tropical beach, volcanic black sand, ocean horizon",
        "lighting": "tropical Pacific golden hour, ocean breeze atmosphere, island sunset glow",
        "style": "Polynesian cultural fine art body painting, Pacific island editorial",
        "quality": "shot on Canon EOS R5, warm tropical Pacific grade, portrait 2:3"
    },

    "viking_rune": {
        "name": "바이킹 룬 — 룬 문자 전신",
        "outfit": "ancient Viking runic alphabet and Norse knotwork covering entire figure",
        "material": "Norse runic inscription medium, Viking age ink, Elder Futhark pattern",
        "environment": "Norse fjord landscape, Viking longhouse, Scandinavian ancient site",
        "lighting": "dramatic Nordic light, Norse fire glow, fjord atmosphere",
        "style": "Norse cultural fine art body painting, Viking age editorial",
        "quality": "shot on Hasselblad, cold Nordic blue-grey grade, portrait 2:3 vertical"
    },

    "inca_geometric": {
        "name": "잉카 기하학 — 잉카 기하학 문양 전신",
        "outfit": "Inca geometric textile tokapu patterns covering entire figure, Andean body art",
        "material": "Andean geometric weave pattern medium, Inca gold and terracotta pigment",
        "environment": "Machu Picchu Andean ruins, mountain cloud forest, Inca citadel",
        "lighting": "high altitude Andean light, Machu Picchu sunrise, mountain golden glow",
        "style": "Inca cultural fine art body painting, Andean geometric editorial",
        "quality": "shot on Phase One, warm Andean terracotta grade, portrait 2:3"
    },

    "chinese_dragon": {
        "name": "중국 용 — 용 전신 문양",
        "outfit": "Imperial Chinese dragon winding across entire figure, traditional dragon body art",
        "material": "Chinese imperial lacquer red and gold dragon medium, cloud pattern, pearl motif",
        "environment": "Forbidden City imperial hall, Chinese palace architecture, dragon throne room",
        "lighting": "imperial red lantern light, Chinese palace gold glow, dragon ceremony",
        "style": "Chinese imperial fine art body painting, dragon editorial",
        "quality": "shot on Hasselblad H6D, imperial red-gold Chinese grade, portrait 2:3"
    },

    "aboriginal_dot": {
        "name": "호주 원주민 점묘 — 점묘 패턴 전신",
        "outfit": "Australian Aboriginal dot painting dreamtime patterns covering entire figure",
        "material": "ochre and white dot painting medium, dreamtime story pattern, sacred site map",
        "environment": "Australian red desert, Uluru landscape, ancient sacred site",
        "lighting": "harsh Australian desert sun, red earth glow, ancient land light",
        "style": "Aboriginal cultural fine art body painting, dreamtime editorial",
        "quality": "shot on Canon EOS R5, warm red ochre Australian grade, portrait 2:3"
    },

    # ─────────────────────────────────────────────
    # 🔮 판타지/신비 바디페인팅
    # ─────────────────────────────────────────────

    "galaxy_skin": {
        "name": "갤럭시 스킨 — 은하수가 피부에 투영된",
        "outfit": "Milky Way galaxy nebula and star field projected across entire figure, cosmic body art",
        "material": "cosmic nebula pigment, star field medium, galaxy dust and gas color",
        "environment": "dark desert under Milky Way, cosmic observatory, stargazing site",
        "lighting": "pure Milky Way starlight, nebula glow, cosmic darkness illumination",
        "style": "astrophotography fine art body painting, cosmic galaxy editorial",
        "quality": "shot on Sony A1, deep space cosmic grade, portrait 2:3 vertical"
    },

    "crystal_growth": {
        "name": "수정 성장 — 수정이 피부에서 자라는",
        "outfit": "crystalline mineral growth formations emerging from figure, geode body art",
        "material": "amethyst and quartz crystal growth medium, mineral formation texture",
        "environment": "crystal cave geode interior, mineral-rich cavern, crystal formation space",
        "lighting": "crystal refraction light, geode interior glow, mineral luminosity",
        "style": "mineralogy fine art body painting, crystal growth editorial",
        "quality": "shot on Phase One XT, crystal purple-clear grade, portrait 2:3"
    },

    "tree_of_life": {
        "name": "생명의 나무 — 뿌리가 전신에 뻗는",
        "outfit": "Tree of Life roots and branches spreading across entire figure, botanical body art",
        "material": "organic root and branch medium, bark texture, leaf and flower detail",
        "environment": "ancient forest, sacred tree grove, mystical woodland",
        "lighting": "dappled forest light through canopy, sacred grove atmosphere, earth glow",
        "style": "botanical mythology fine art body painting, tree of life editorial",
        "quality": "shot on Hasselblad, warm forest earth grade, portrait 2:3"
    },

    "moonphase_body": {
        "name": "달의 위상 — 달의 위상 변화 전신",
        "outfit": "lunar cycle moon phase progression mapped across entire figure, celestial body art",
        "material": "silver moonlight medium, lunar phase gradient, moon surface texture",
        "environment": "open landscape under full moon, lunar observatory, moonlit plain",
        "lighting": "pure silver moonlight, lunar phase illumination, celestial night glow",
        "style": "lunar cycle fine art body painting, moon phase editorial",
        "quality": "shot on Leica SL2, silver lunar grade, portrait 2:3 vertical"
    },

    "shadow_lace": {
        "name": "그림자 레이스 — 빛의 그림자가 레이스처럼",
        "outfit": "intricate shadow patterns from light through lace creating body art effect",
        "material": "projected shadow lace medium, light refraction through lacework, shadow pattern",
        "environment": "bright sunlit space with ornate lace screens, window light installation",
        "lighting": "strong directional light through intricate lace, shadow projection art",
        "style": "shadow projection fine art body painting, lace light editorial",
        "quality": "shot on Canon EOS R5, high contrast shadow-light grade, portrait 2:3"
    },

    "ash_phoenix": {
        "name": "불사조 재 — 재에서 불사조처럼",
        "outfit": "phoenix rising from ash pattern covering figure, fire bird rebirth body art",
        "material": "ash and ember medium, phoenix flame pattern, rebirth fire pigment",
        "environment": "volcanic landscape or dark studio with ash and ember atmosphere",
        "lighting": "phoenix fire glow, ember illumination, dramatic rebirth light",
        "style": "mythology fine art body painting, phoenix rebirth editorial",
        "quality": "shot on Sony A1, warm fire ember grade, portrait 2:3"
    },

    "half_statue": {
        "name": "절반 조각상 — 절반은 대리석 절반은 사람",
        "outfit": "figure transitioning from white marble sculpture on one side to living skin on other",
        "material": "Carrara marble texture on half, living skin on other half, boundary dissolution",
        "environment": "classical sculpture museum, Renaissance gallery, dramatic museum setting",
        "lighting": "dramatic museum spotlight emphasizing marble-to-skin transition",
        "style": "Pygmalion concept fine art photography, living sculpture editorial",
        "quality": "shot on Hasselblad H6D, marble-to-skin transition grade, portrait 2:3"
    },

}


def main():
    print("\n  ✦ LumineX v9.0 바디페인팅 확장 프리셋 추가 시작...\n")
    created = 0
    skipped = 0

    for name, data in NEW_PRESETS_V9.items():
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
    print("  - 🎨 명화/아트    (vangogh/monet/pollock/broken_porcelain/marble_veins/munch/dali/mucha/hokusai/kandinsky) × 10")
    print("  - 🌿 자연물 패턴  (coral_reef/leopard_dissolve/peacock_feather/snake_scale/butterfly_wing/deep_ocean_map)  × 6")
    print("  - ⚡ 과학/기술    (dna_helix/star_map/neuron_network/topographic/neon_circuit)                            × 5")
    print("  - 🏺 문명/부족    (maori_moko/aztec_warrior/egypt_hieroglyph/celtic_knotwork/polynesian/viking/inca/chinese/aboriginal) × 9")
    print("  - 🔮 판타지/신비  (galaxy_skin/crystal_growth/tree_of_life/moonphase/shadow_lace/ash_phoenix/half_statue)  × 7")
    print(f"  총 37개 신규 프리셋\n")
    print("  💡 기존 바디페인팅 5개 포함 총 42개 바디페인팅 계열 완성!")


if __name__ == "__main__":
    main()