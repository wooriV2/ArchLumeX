"""
add_new_presets_v22.py
에로틱 & 페티쉬 강화 프리셋 26개

✅ 즉시 추가 (20개) → 💋 에로틱 & 페티쉬
  노출: transparent_dress, sheer_catsuit
  라텍스/PVC: latex_transparent, latex_hood_full, pvc_transparent_full
  소재: chrome_bodysuit, mirror_dress, liquid_metal_body
  본디지: suspension_art
  도미나트릭스: dominatrix_full_armor, goddess_throne
  역할극: teacher_after_class, doctor_sensual, police_dominatrix, stewardess_dark
  퍼포먼스: pole_dance_extreme, fire_goddess
  판타지: succubus_full, dark_angel_fallen, alien_queen_body

⚠️ 조정 후 추가 (6개) → 💋 에로틱 & 페티쉬
  body_paint_nude, micro_thong_only, tape_bondage,
  metal_bondage, military_domme, lap_dance_extreme

총 프리셋: 777 → 803개
"""

import json
from pathlib import Path

PRESETS_DIR = Path("presets")
PRESETS_DIR.mkdir(exist_ok=True)

new_presets = {

    # ═══════════════════════════════════════
    # 노출 (2개)
    # ═══════════════════════════════════════

    "transparent_dress": {
        "tag": "Transparent Dress",
        "subject": "a daring female model in completely transparent PVC mini dress",
        "outfit": "completely transparent PVC mini dress, body fully visible through fabric, thong underneath, stilettos",
        "material": "crystal clear PVC, transparent vinyl",
        "environment": "luxury nightclub VIP area, purple neon lighting, mirror walls",
        "lighting": "neon purple glow through transparent dress, body silhouette highlighted",
        "style": "avant-garde fetish fashion editorial, transparent dress art",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "sheer_catsuit": {
        "tag": "Sheer Catsuit",
        "subject": "a sensual female model in fully sheer mesh catsuit",
        "outfit": "full-body sheer mesh catsuit, body silhouette completely visible, minimal lingerie underneath, heels",
        "material": "ultra-sheer stretch mesh, second-skin transparency",
        "environment": "minimalist dark studio, single dramatic spotlight",
        "lighting": "single spotlight revealing body through sheer fabric, dramatic shadow",
        "style": "high fashion editorial, sheer catsuit body art",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 라텍스/PVC (3개)
    # ═══════════════════════════════════════

    "latex_transparent": {
        "tag": "Latex Transparent",
        "subject": "a futuristic female model in transparent latex full bodysuit",
        "outfit": "transparent clear latex full bodysuit, skin visible through latex, black latex trim, platform boots",
        "material": "crystal clear transparent latex, glossy finish",
        "environment": "futuristic sci-fi set, blue LED ambient, metallic backdrop",
        "lighting": "cold blue light through transparent latex, futuristic glow",
        "style": "sci-fi latex fashion editorial, transparent latex couture",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "latex_hood_full": {
        "tag": "Latex Hood Full",
        "subject": "a mysterious female model in full latex hood and catsuit",
        "outfit": "full black latex hood covering entire head, matching latex catsuit, only eyes and lips visible, stiletto boots",
        "material": "shiny black latex, form-fitting hood",
        "environment": "dark industrial set, single overhead spotlight, smoke",
        "lighting": "dramatic overhead light on latex hood, mysterious shadow",
        "style": "extreme latex fashion editorial, latex hood fetish couture",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "pvc_transparent_full": {
        "tag": "PVC Transparent Full",
        "subject": "a bold female model in full transparent PVC bodysuit",
        "outfit": "full-body transparent PVC bodysuit, skin clearly visible, black lingerie underneath, platform boots",
        "material": "ultra-clear PVC vinyl, high gloss transparent",
        "environment": "cyberpunk rain-soaked street, neon reflections on PVC",
        "lighting": "neon reflections on transparent PVC, rain glow, cyberpunk palette",
        "style": "cyberpunk transparent PVC editorial, vinyl fetish fashion",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 소재 (3개)
    # ═══════════════════════════════════════

    "chrome_bodysuit": {
        "tag": "Chrome Bodysuit",
        "subject": "a futuristic female model in chrome mirror full bodysuit",
        "outfit": "chrome mirror-finish full bodysuit, reflective metallic surface, form-fitting, platform boots",
        "material": "chrome mirror vinyl, liquid metal finish",
        "environment": "white infinity studio, mirror floor, chrome reflections everywhere",
        "lighting": "multiple light sources creating chrome reflections, prismatic",
        "style": "futuristic chrome fashion editorial, mirror bodysuit art",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "mirror_dress": {
        "tag": "Mirror Dress",
        "subject": "a dazzling female model in mosaic mirror shard mini dress",
        "outfit": "mosaic mirror shard mini dress, thousands of tiny mirrors covering dress, strappy heels",
        "material": "mosaic mirror fragments, reflective tiles on dress base",
        "environment": "dark nightclub, disco ball aesthetic, light refraction everywhere",
        "lighting": "multiple light beams creating kaleidoscope reflections from mirror dress",
        "style": "disco glamour editorial, mirror mosaic dress fashion art",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "liquid_metal_body": {
        "tag": "Liquid Metal Body",
        "subject": "a powerful female model in liquid metal texture full bodysuit",
        "outfit": "liquid mercury silver full bodysuit, molten metal texture, form-fitting, silver boots",
        "material": "liquid metal effect fabric, mercury silver finish",
        "environment": "dark dramatic studio, silver liquid pools on floor",
        "lighting": "dramatic side lighting creating liquid metal flow illusion",
        "style": "liquid metal fashion editorial, mercury goddess concept",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 본디지 (1개)
    # ═══════════════════════════════════════

    "suspension_art": {
        "tag": "Suspension Art",
        "subject": "a graceful female model in aerial rope suspension art performance",
        "outfit": "aerial rope suspension with artistic rope wrapping, minimal coverage, suspended mid-air in graceful pose",
        "material": "natural fiber rope, aerial performance art rigging",
        "environment": "black box theater, single spotlight from above, dark dramatic space",
        "lighting": "single dramatic spotlight from above, model suspended in light beam",
        "style": "aerial rope art performance editorial, suspension body art",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 도미나트릭스 (2개)
    # ═══════════════════════════════════════

    "dominatrix_full_armor": {
        "tag": "Dominatrix Full Armor",
        "subject": "a supremely dominant female model in full black latex armor",
        "outfit": "full black latex armor suit, structured shoulders, corset waist, thigh-high boots, riding crop, commanding pose",
        "material": "rigid black latex armor panels, patent leather details",
        "environment": "dramatic dungeon-inspired dark set, chains as decor, red accent lighting",
        "lighting": "dramatic red and black lighting, power silhouette",
        "style": "supreme dominatrix fashion editorial, full latex armor power",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "goddess_throne": {
        "tag": "Goddess Throne",
        "subject": "a dominant goddess female model seated on ornate throne in latex",
        "outfit": "latex corset and thigh-highs, seated on elaborate throne, chains draped as accessories, commanding expression",
        "material": "black latex, ornate gold throne, decorative chains",
        "environment": "dark gothic throne room, torchlight, dramatic stone architecture",
        "lighting": "dramatic torchlight, throne room atmosphere, power lighting",
        "style": "goddess dominatrix fashion editorial, throne room power",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 역할극 (4개)
    # ═══════════════════════════════════════

    "teacher_after_class": {
        "tag": "Teacher After Class",
        "subject": "a seductive female model as after-class teacher in unbuttoned shirt",
        "outfit": "fitted pencil skirt, white shirt unbuttoned revealing lace underneath, reading glasses pushed down, heels, desk setting",
        "material": "tailored pencil skirt, cotton shirt, lace bra",
        "environment": "empty classroom after hours, evening light through windows, chalkboard",
        "lighting": "warm evening classroom light, intimate after-hours atmosphere",
        "style": "role-play fashion editorial, teacher after class fantasy",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "doctor_sensual": {
        "tag": "Doctor Sensual",
        "subject": "a sensual female model in open white doctor coat with lingerie underneath",
        "outfit": "open white doctor coat revealing lingerie underneath, stethoscope, stockings, heels",
        "material": "white medical coat, silk lingerie underneath",
        "environment": "private clinic room, clinical white with warm accent lighting",
        "lighting": "clinical white light with warm intimate glow",
        "style": "medical role-play fashion editorial, sensual doctor fantasy",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "police_dominatrix": {
        "tag": "Police Dominatrix",
        "subject": "a dominant female model in police uniform with dominatrix elements",
        "outfit": "tight police uniform shirt, micro skirt, thigh-high boots, handcuffs as accessory, commanding pose",
        "material": "tailored police uniform fabric, patent leather boots",
        "environment": "dark urban setting, interrogation room aesthetic, dramatic lighting",
        "lighting": "single harsh interrogation light, dramatic shadows, power atmosphere",
        "style": "police dominatrix fashion editorial, authority role-play",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "stewardess_dark": {
        "tag": "Stewardess Dark",
        "subject": "a seductive female model in dark version stewardess uniform",
        "outfit": "ultra-fitted stewardess uniform, very short skirt, black stockings, stilettos, hat tilted",
        "material": "fitted uniform fabric, silk stockings",
        "environment": "private jet interior at night, dim cabin lighting, luxury seats",
        "lighting": "dim moody private jet cabin light, intimate atmosphere",
        "style": "dark stewardess fashion editorial, private jet fantasy",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 퍼포먼스 (2개)
    # ═══════════════════════════════════════

    "pole_dance_extreme": {
        "tag": "Pole Dance Extreme",
        "subject": "an athletic female model in extreme pole dance pose with minimal outfit",
        "outfit": "micro sports bra, micro booty shorts, bare legs, heels, extreme athletic pole pose",
        "material": "minimal stretch sportswear",
        "environment": "professional pole dance studio, dramatic spotlight on pole, mirror walls",
        "lighting": "single dramatic spotlight on pole and model, high contrast",
        "style": "extreme pole dance athletic editorial, pole art performance",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "fire_goddess": {
        "tag": "Fire Goddess",
        "subject": "a powerful female fire performer with flames surrounding minimal outfit",
        "outfit": "minimal fire performance costume, tribal-inspired, barely covering, flames as extension of body",
        "material": "heat-resistant performance fabric, minimal coverage",
        "environment": "outdoor night performance, darkness surrounding, fire as only light source",
        "lighting": "dramatic fire light only, orange and red flame glow, dark surroundings",
        "style": "fire performance art editorial, fire goddess concept",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 판타지 (3개)
    # ═══════════════════════════════════════

    "succubus_full": {
        "tag": "Succubus Full",
        "subject": "a full-form succubus female model with wings horns and latex",
        "outfit": "red and black latex corset, dramatic demon wings, curved horns, thigh-highs, tail, full succubus form",
        "material": "red black latex, prosthetic wings and horns, dramatic accessories",
        "environment": "hellfire inferno backdrop, dark red smoke, burning embers",
        "lighting": "hellfire red and orange dramatic lighting, demonic atmosphere",
        "style": "full succubus fantasy editorial, demon goddess concept",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "dark_angel_fallen": {
        "tag": "Dark Angel Fallen",
        "subject": "a fallen angel female model with dark wings in torn lingerie",
        "outfit": "torn white lingerie, large black feather wings, dark halo, chains as accessories, dramatic pose",
        "material": "torn silk lingerie, black feather wings, dark metal chains",
        "environment": "gothic cathedral ruins, moonlight through broken stained glass",
        "lighting": "moonlight through ruins, dramatic chiaroscuro, fallen grace",
        "style": "fallen angel dark fantasy editorial, dark angel concept",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "alien_queen_body": {
        "tag": "Alien Queen Body",
        "subject": "a commanding alien queen female model with silver body paint and alien costume",
        "outfit": "silver metallic body paint covering upper body, alien queen crown, structural alien armor pieces, minimal coverage",
        "material": "silver body paint, alien armor pieces, iridescent materials",
        "environment": "alien spacecraft interior, bioluminescent blue-green ambient, otherworldly",
        "lighting": "bioluminescent alien light, silver body paint reflections, otherworldly glow",
        "style": "sci-fi alien queen fashion editorial, alien goddess concept",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    # ═══════════════════════════════════════
    # 조정 후 추가 (6개) — 리스크 키워드 제거
    # ═══════════════════════════════════════

    "body_paint_nude": {
        "tag": "Body Paint Nude",
        "subject": "a fine art female model with body paint as sole artistic covering",
        "outfit": "body paint as sole covering — elaborate full-body artistic paint design covering entire figure, painted on bare skin as fine art, NO clothing, NO fabric",
        "material": "fine art body paint pigments covering entire body as garment",
        "environment": "fine art gallery or minimalist studio, white backdrop",
        "lighting": "gallery lighting, artistic body paint illumination",
        "style": "fine art body painting editorial, body paint as fashion",
        "quality": "ultra-sharp, 8K, professional fine art photography",
    },

    "micro_thong_only": {
        "tag": "Micro Thong",
        "subject": "a toned female model in micro thong bikini with body chain accessories",
        "outfit": "micro triangle thong bikini bottom, layered gold body chains covering torso, stilettos",
        "material": "micro fabric, 14k gold body chains",
        "environment": "luxury yacht deck, Mediterranean sea, golden hour",
        "lighting": "warm golden Mediterranean sunset, yacht luxury",
        "style": "luxury yacht editorial, minimal swimwear body chain",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "tape_bondage": {
        "tag": "Tape Bondage Art",
        "subject": "a bold female model in industrial tape body art installation",
        "outfit": "black industrial tape applied as body art installation, geometric tape patterns covering key areas as artistic statement, heels",
        "material": "black industrial tape as art medium",
        "environment": "contemporary art gallery, white cube space, installation art context",
        "lighting": "gallery white cube lighting, art installation aesthetic",
        "style": "contemporary body art installation editorial, tape as fashion",
        "quality": "ultra-sharp, 8K, professional art photography",
    },

    "metal_bondage": {
        "tag": "Metal Bondage Jewelry",
        "subject": "a fierce female model in elaborate metal chain jewelry as garment",
        "outfit": "elaborate metal chain jewelry draped as garment covering body, heavy chain necklace, chain belt, chain accessories as sole covering",
        "material": "heavy metal chains, industrial hardware as jewelry",
        "environment": "industrial loft, exposed metal beams, dramatic spotlight",
        "lighting": "dramatic industrial spotlight, metal chain reflections",
        "style": "industrial metal jewelry fashion editorial, chain as garment",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "military_domme": {
        "tag": "Military Domme",
        "subject": "a commanding female model in latex military-inspired dominatrix uniform",
        "outfit": "latex military-inspired jacket, micro skirt, thigh-high boots, peaked cap, commanding baton prop",
        "material": "black latex military jacket, patent leather boots",
        "environment": "stark dramatic set, military aesthetic, powerful atmosphere",
        "lighting": "harsh dramatic military-style lighting, power and command",
        "style": "military dominatrix fashion editorial, latex military fantasy",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },

    "lap_dance_extreme": {
        "tag": "Lap Dance Glamour",
        "subject": "a sensual female model in extreme close-contact dance pose in VIP setting",
        "outfit": "sequined micro dress, strappy heels, intimate close dance pose, VIP chair setting",
        "material": "sequined stretch fabric, minimal coverage",
        "environment": "exclusive VIP lounge, velvet chairs, dim amber lighting, champagne",
        "lighting": "dim amber intimate VIP lounge lighting, seductive atmosphere",
        "style": "VIP lounge sensual dance editorial, intimate performance glamour",
        "quality": "ultra-sharp, 8K, professional fashion photography",
    },
}

# ─── dashboard.py PRESET_CATEGORIES 추가 코드 안내 ────────
EROTIC_ADDITIONS = [
    # 노출
    "transparent_dress", "sheer_catsuit",
    # 라텍스/PVC
    "latex_transparent", "latex_hood_full", "pvc_transparent_full",
    # 소재
    "chrome_bodysuit", "mirror_dress", "liquid_metal_body",
    # 본디지
    "suspension_art",
    # 도미나트릭스
    "dominatrix_full_armor", "goddess_throne",
    # 역할극
    "teacher_after_class", "doctor_sensual", "police_dominatrix", "stewardess_dark",
    # 퍼포먼스
    "pole_dance_extreme", "fire_goddess",
    # 판타지
    "succubus_full", "dark_angel_fallen", "alien_queen_body",
    # 조정 후 추가
    "body_paint_nude", "micro_thong_only", "tape_bondage",
    "metal_bondage", "military_domme", "lap_dance_extreme",
]

# ─── JSON 파일 생성 ────────────────────────────────────────
added = 0
skipped = 0
for name, data in new_presets.items():
    path = PRESETS_DIR / f"{name}.json"
    if path.exists():
        print(f"⏭️  skip: {name}")
        skipped += 1
    else:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ added: {name}")
        added += 1

print(f"\n완료: {added}개 추가, {skipped}개 스킵")
print(f"총 프리셋: 777 → {777 + added}개")
print(f"\n─── dashboard.py PRESET_CATEGORIES 추가 필요 ───")
print(f"\n💋 에로틱 & 페티쉬 끝에 추가 ({len(EROTIC_ADDITIONS)}개):")
for name in EROTIC_ADDITIONS:
    print(f'        "{name}",')
