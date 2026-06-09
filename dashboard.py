"""
LumineX Dashboard v4.4
실행: streamlit run dashboard.py

v4.4 변경사항 (2026-06-07):
1. 카테고리 재편 (B안) — 섹시/글래머 3분류
   - 💫 글래머 & 럭셔리 → 💫 럭셔리 글래머 (41개)
   - 💋 관능 & 에로틱 글래머 → 삭제
   - 🔥 핫 & 섹시 신설 (43개)
   - 💋 에로틱 & 페티쉬 신설 (26개)
2. 각 카테고리에서 섹시 계열 프리셋 이동 정리

v4.4.1 SS tier 엄격 재검토 (2026-06-07):
- SS 강등(S): burlesque, dominatrix_glam, corset_stockings,
  dark_fairy_erotic, tape_bondage, metal_bondage
- SS 제거: military_domme (나치 상징 생성 리스크 — 프리셋 정의 수정 필요)
- SS tier 128 → 121개
"""

import sys
import random
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from core.engine import list_presets, load_preset, build_prompt
from core.prompt_generator import generate_prompt_with_ai
from core.data import (
    ASPECT_RATIOS,
    MODEL_APPEARANCE, AGE_APPEARANCE, MODEL_TYPES,
    BODY_WEIGHT, BUST_SIZE, HIP_SIZE,
    OUTFIT_TYPES, MATERIALS, ENVIRONMENTS, STYLES,
    LIGHTING, CAMERA_ANGLES, FOOTWEAR, CAMERAS,
    HAIR_STYLES, HAIR_COLORS, MODEL_COUNT,
    ERA, CONCEPT, SPECIAL_EFFECTS, IMAGE_STYLE, PROPS,
    MAKEUP, ACCESSORIES, SKIN_TONES,
    POSES, WEATHER, EXPRESSION, TATTOO, BODY_OIL, BG_CROWD,
    COLOR_GRADES, MOOD, TIME_OF_DAY, LENS_EFFECT,
    TOP_TYPES, BOTTOM_TYPES,
    SKIN_DETAILS, NAILS,
    FRAMING,
    COVER_STYLES,
)
from core.combos import GOOD_COMBOS, CONFLICT_RULES, check_conflicts, get_combo_recommendations, auto_filter_check
from core.builders import build_gemini_prompt, build_chatgpt_prompt, build_midjourney_prompt, _build_wearing_line

st.set_page_config(
    page_title="LumineX Dashboard",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── 카테고리별 프리셋 매핑 ─────────────────────────────────
PRESET_CATEGORIES = {
    "🖌️ 바디페인팅 & 스킨 트랜스폼": [
        # 기존
        "bioluminescent_ink","klimt_gold_body","vangogh_body","dali_surreal","munch_scream",
        "monet_bloom","mucha_nouveau","hokusai_wave","kandinsky_abstract","pollock_splash",
        "broken_porcelain","marble_veins","henna_goddess_body","oil_slick_body","liquid_chrome_body",
        "ink_wash_body","body_paint_art","watercolor_goddess","fresco_goddess","fresco_awakening",
        "tableau_vivant","coral_reef","leopard_dissolve","peacock_feather","snake_scale",
        "butterfly_wing","deep_ocean_map","dna_helix","star_map","neuron_network","neon_circuit",
        "topographic","maori_moko","aztec_warrior","egypt_hieroglyph","celtic_knotwork",
        "polynesian_tribal","viking_rune","inca_geometric","chinese_dragon","aboriginal_dot",
        "galaxy_skin","crystal_growth","tree_of_life","moonphase_body","shadow_lace",
        "ash_phoenix","half_statue",
        # v12
        "rembrandt_chiaroscuro","klimt_silver","matisse_cutout","mondrian_body","basquiat_street",
        "warhol_pop","lichtenstein_dot","huli_wigman","nuba_body","wodaabe_beauty","mehndi_full",
        "mayan_ritual","haida_totem","aurora_skin","crystal_mineral","tide_pool","magnetic_field",
        "cell_division",
        # v14 — 관능적 바디페인팅 35개
        "melting_chocolate","liquid_gold_drip","silver_mercury_body","ink_pour_body",
        "paint_splash_body","milk_bath_body",
        "rose_petal_body","orchid_body","vine_wrap_body","lotus_body","poison_flower",
        "fire_skin","water_ripple_body","frost_crystallize","storm_static_body","smoke_body_art",
        "lace_body_paint","fishnet_paint","chain_body_paint","jewelry_trompe_loeil","mandala_body",
        "body_calligraphy","zentangle_body","constellation_body","circuit_erotic","tarot_body",
        "moon_tattoo_body","rune_body_art","alchemy_body","henna_erotic",
        "python_scales","jaguar_spots","mermaid_scales","raven_feathers","tiger_stripes_body",
        # v15 — 명화/작가 퍼블릭 도메인 14개
        "cezanne_body","gauguin_tropics","toulouse_lautrec","schiele_body","degas_dancer",
        "renoir_soft","botticelli_venus","titian_goddess","rubens_baroque","ingres_odalisque",
        "waterhouse_nymph","rossetti_dante","alma_tadema","vigee_lebrun",
        # v15 — 생존/최근 작가 5개
        "keith_haring_body","yayoi_kusama","takashi_murakami",
        "jean_dubuffet","jean_cocteau",
        # v15 — 부족/문화 10개
        "bodi_clay","ndebele_pattern","tuareg_indigo","mursi_lip",
        "surma_body","asaro_mudmen","kayapo_brasil","nuba_scarification","kayan_neck",
        # v15 — 과학/자연 10개
        "thermal_scan","bioluminescent_deep","microscope_pollen","xray_body","mri_scan_body",
        "neural_map","geologic_strata","crystal_lattice","solar_system_body","dna_double_helix",
        # v18 — 동물 바디페인팅 50개
        "panther_black","cheetah_speed","snow_leopard","ocelot_wild",
        "chameleon_skin","dragon_scales_red","komodo_dragon","gecko_pattern","crocodile_skin",
        "boa_constrictor","king_cobra_hood",
        "butterfly_monarch","butterfly_morpho","dragonfly_iridescent","scarab_beetle",
        "praying_mantis","luna_moth","atlas_moth",
        "eagle_wings","flamingo_pink","owl_feather","parrot_tropical","hummingbird_iridescent",
        "phoenix_rising","swan_white","macaw_scarlet","bird_of_paradise",
        "octopus_ink","koi_fish","jellyfish_glow","seahorse_fantasy","mantis_shrimp",
        "anglerfish_deep","nudibranch_sea","cuttlefish_chromo",
        "wolf_grey","zebra_stripes","giraffe_pattern","dalmatian_spots","arctic_fox",
        "red_fox","hyena_spots",
        "koi_dragon","unicorn_opal","gryphon_feather","sphinx_cat","basilisk_scales",
        # v19 — 한국 바디아트 10개
        "dancheong_body","najeonchilgi_body","goryeo_celadon_body","minhwa_body",
        "korean_tiger_body","pojagi_body","taegeuk_body","silla_crown_body",
        "dansaekhwa_body","najeon_abalone",
        # v19 — 한국 동물/신수 (바디아트)
        "baekhak_crane","korean_dragon_body","phoenix_jujakk",
        "baekho_white_tiger","hyeonmu_turtle","cheongnyong_dragon",
        # v19 — 한국 자연/식물 바디아트
        "mugunghwa_body","korean_lotus_body","korean_plum_body","korean_bamboo_body",
        # v20 — 지도 계열 13개
        "world_map_body","topographic_body","ocean_depth_body","thermal_map_body",
        "weather_map_body","subway_map_body","europe_political_body","africa_tribes_body",
        "japan_prefecture_body","ancient_map_body","star_map_body",
        "usa_county_map_body",
        # v20 — 과학/자연현상 5개
        "thermal_scan_body","circuit_board_body","galaxy_nebula_body",
        "crystal_geode_body",
        # v20 — 문명/문자 6개
        "hieroglyph_body","aztec_calendar_body","celtic_knot_body",
        "arabic_calligraphy_body","islamic_geometric_body","greek_mosaic_body",
        # v20 — 식물/자연 3개
        "autumn_leaves_body","coral_reef_body","mushroom_forest_body",
        # v20 — 건축/패턴 2개
        "stained_glass_body","bauhaus_body",
        # v20 — 환경융합 2개
        "urban_decay_body","forest_stone_body",
        # 2026-06-08 카테고리 누락 복구
        "banksy_stencil","shadow_art_nude",
        # v23 — 개방형 바디페인팅 20개 (주제 비움, 매번 다르게 생성)
        "body_paint_watercolor_free","body_paint_metallic_free","body_paint_impasto",
        "body_paint_airbrush","body_paint_ink_splatter","body_paint_drip_free",
        "body_paint_monochrome","body_paint_pastel_dream","body_paint_neon_glow",
        "body_paint_earth_tones","body_paint_jewel_tones","body_paint_iridescent_free",
        "body_paint_abstract_expressionist","body_paint_geometric_free","body_paint_organic_flow",
        "body_paint_surreal_free","body_paint_minimalist_free",
        "body_paint_blacklight","body_paint_glitter_free","body_paint_uv_reactive",
    ],
    "💫 럭셔리 글래머": [
        "runway_power","red_carpet","editorial_glam","golden_hour_editorial","elite_motion",
        "noir_opulence","platinum_elite","ivory_silk","ivory_tower",
        "pearl_essence","velvet_gold","velvet_darkness","all_black_goddess","black_mirror",
        "onyx_tension","phantom_gloss","champagne_mist","couture_heat","silk_wrap","goddess_draped",
        "feather_cascade","feather_touch","golden_oil","golden_nude","gold_temptress","red_temptress",
        "veil_goddess","petal_goddess","cobweb_drape",
        # v11
        "casino_royale","black_tie_gala","champagne_tower","fur_coat_only",
        # v16
        "plunge_gown","slit_maxi","cutout_bodysuit","sheer_overlay",
        "jeweled_bikini_top","golden_drape_goddess","crystal_gown","feather_trim_mini",
        # v21 — 럭셔리 글래머 13개
        "luxury_noir","diamond_couture","velvet_serpent","opera_glam","silver_screen",
        "lace_noir","white_silk_goddess","crystal_bodycon","penthouse_glam",
        "midnight_couture","crimson_gown","serpentine_dress","baroque_glam",
    ],
    "🔥 핫 & 섹시": [
        # 기존 관능 & 에로틱 글래머
        "lingerie_goddess","silk_robe_only","corset_queen","bodycon_power","sheer_negligee","boudoir_noir",
        "wet_silk_gown","oil_goddess_gold","pool_wet_glam","rain_soaked_dress","sweat_glam",
        "micro_dress_only","barely_covered","deep_plunge_gown","backless_extreme","one_strap_gown",
        "pinup_classic","vargas_girl","bombshell_retro","bunny_suit","playboy_glam",
        # 럭셔리에서 이동
        "elite_lingerie","lingerie_noir",
        # 비치에서 이동
        "barely_there","wet_look_goddess","thong_bikini","micro_bikini_gold",
        "sarong_goddess","wet_bikini_pool","topless_editorial","nude_beach_art",
        "aqua_bikini","golden_summer","riviera_heat",
        # 계절에서 이동
        "snow_queen_erotic","autumn_gold_sensual","christmas_boudoir","summer_solstice_glam",
        # 란제리/페티쉬 경계
        "latex_queen","pvc_goddess","leather_mistress","crystal_mesh_goddess","chain_mail_glam",
        # v21 — 핫 & 섹시 19개
        "fishnet_goddess","see_through_gown","wet_tshirt","string_bikini","lace_bodysuit",
        "satin_slip","velvet_corset","body_chain_only","strappy_dress","cut_out_swimsuit",
        "monokini_goddess","champagne_drip","neon_bodysuit","bikini_top_only",
        "white_linen_sheer","oil_drip_body","yoga_pants_glam","micro_skirt","halter_glam",
        # 2026-06-08 누락 복구
        "wet_editorial",
    ],
    "💋 에로틱 & 페티쉬": [
        # 파워&엣지에서 이동
        "latex_venom","chrome_vixen","chain_goddess",
        "dominatrix_glam","bondage_fashion","strappy_harness","mesh_bodysuit","latex_catsuit",
        "oil_goddess","savage_leather",
        # 퍼포먼스에서 이동
        "burlesque","showgirl","cabaret_star","pole_art","candy_rave",
        "lap_dance_glam","striptease_art","pole_dance_power","midnight_bath","belly_dance_glam",
        # 판타지에서 이동
        "dark_succubus","vampire_seduction","witch_sensual","dark_fairy_erotic","shadow_seductress",
        # v21 — 에로틱 & 페티쉬 16개
        "latex_catsuit_red","rubber_goddess","harness_only","rope_bondage_art",
        "vinyl_goddess","corset_stockings","catsuit_zipper","bodystocking",
        "secretary_after_hours","nurse_sensual","maid_sensual","leather_bodysuit",
        "wet_latex","fetish_boots_only","dominatrix_red","fishnet_bodysuit",
        # v22 — 에로틱 & 페티쉬 강화 26개
        "transparent_dress","sheer_catsuit",
        "latex_transparent","latex_hood_full","pvc_transparent_full",
        "chrome_bodysuit","mirror_dress","liquid_metal_body",
        "suspension_art",
        "dominatrix_full_armor","goddess_throne",
        "teacher_after_class","doctor_sensual","police_dominatrix","stewardess_dark",
        "pole_dance_extreme","fire_goddess",
        "succubus_full","dark_angel_fallen","alien_queen_body",
        "body_paint_nude","micro_thong_only","tape_bondage",
        "metal_bondage","lap_dance_extreme",
    ],
    "🌿 자연 & 원소": [
        "lava_flow","ocean_surge","ice_palace","ice_refraction","frozen_latex","blizzard_queen","sandstorm_veil",
        "storm_couture","heat_shimmer","water_reflection","waterfall_goddess","rain_soaked",
        "mist_goddess","mist_vanguard","winter_forest","desert_mirage","desert_oracle",
        "desert_sand_glam","cliff_edge","arctic_minimal","dawn_awakening","aurora_drape",
        "aurora_spirit","lightning_body","solar_flare","tropical_storm","santorini_lightning",
        "smoke_veil","liquid_gold_pour","liquid_mirror","prism_light","shattered_glass","zero_gravity",
        # v11
        "volcanic_goddess","storm_lightning","deep_cave","tidal_wave",
    ],
    "🌃 도시 & 나이트": [
        "neon_noir","neon_dystopia","neon_rain_goddess","holographic_city","vaporwave_dream",
        "rooftop_midnight","rooftop_party","midnight_goddess","midnight_monolith","nightclub_vip",
        "monaco_nights","miami_afterglow","azure_nights","blue_hour_goddess","candlelight_noir",
        "jazz_club","jazz_age","noir_ballet","urban_vanguard","brutalist_glam","after_dark_minimal",
        "disco_goddess","music_festival","new_year_countdown","cyber_fire","cyber_silk","emerald_city",
        # v11
        "tokyo_shibuya","paris_midnight","subway_editorial","penthouse_view",
    ],
    "🎬 에디토리얼 & 무드": [
        "silhouette_only","back_beauty","collarbone_focus","neck_elegance","long_legs_focus",
        "light_driven","backlit_silk","mirror_goddess","mirror_room","eclipse_body","chrome_skin",
        "neon_body","plasma_aura","molten_chrome","mercury_rising","mercury_pool","titanium_body",
        "snowflake_skin","80s_power","y2k_chrome","bohemian_paris","origami_couture",
        # v11
        "wet_glass","smoke_studio","infrared_beauty","grain_film",
        # 2026-06-08 누락 복구
        "dreamy_soft_focus","film_noir_glam","noir_femme_fatale",
    ],
    "🏺 문명 & 신화": [
        "cleopatra_gold","pharaoh_queen","byzantine_empress","maasai_warrior","nine_tails",
        "moonrise_ceremony","oracle_smoke","ritual_ash","ruins_goddess","renaissance_fantasy",
        "renaissance_nude","cathedral_light","baroque_punk","art_gallery","museum_glamour",
        "library_secret","living_sculpture","living_statue","sculpture_goddess","marble_goddess",
        "marble_minimal","viking_queen",
        # v11
        "sumerian_queen","ming_empress","aztec_sun_goddess","celtic_warrior_queen",
        # v17 보강
        "aphrodite_glam","artemis_huntress","freya_norse","kali_goddess",
        "isis_egypt","lakshmi_goddess","oshun_yoruba","morgan_le_fay",
        # v19 — 한국 신수/정령
        "haetae_guardian","dokkaebi_spirit","korean_tiger_spirit","gyeongbokgung_night",
        # v20 — 국기 8개
        "union_jack_body","brazil_flag_body","usa_stars_stripes_body",
        "japan_rising_sun_body","south_africa_flag_body","india_flag_body",
        "mexico_flag_body","ukraine_flag_body",
    ],
    "✈️ 직업 & 라이프스타일": [
        "flight_attendant","pilot_glamour","nurse_glamour","lawyer_power","hotel_concierge",
        "cruise_hostess","yacht_captain","yacht_club","sommelier","wine_tasting","casino_dealer",
        "private_jet","helipad","luxury_shopping","golf_glam","golf_caddie","tennis_luxe",
        "tennis_referee","f1_grid_girl","equestrian_glam","cheerleader","architect_chic",
        "fitness_power","yoga_goddess",
        # v11
        "barista_chic","gallery_curator","horse_racing","scuba_instructor",
        # v13 스포츠
        "ballet_prima","gymnastics_editorial","figure_skater","tennis_champion",
        "archery_goddess","carnival_rio",
    ],
    "🔮 판타지 & 다크": [
        "dark_mermaid","vampire_queen","angel_fallen","moon_goddess","demon_goddess","forest_witch",
        "pastel_fairy","medusa_queen","halloween_queen","hologram_ghost","glitch_beauty",
        "void_emergence","void_glamour","void_secret","crystal_goddess","toxic_bloom",
        "zombie_apocalypse","dark_academia","gothic_romance","double_exposure_dark",
        "double_exposure_ethereal","oil_slick_noir",
        # v11
        "witch_ritual","fae_queen","cursed_beauty","shadow_realm",
    ],
    "⚔️ 파워 & 엣지": [
        "valkyrie_storm","biker_glam","shadow_play",
        "fencer_noir","martial_arts","boxing_glamour","power_curve",
        "power_suit","sculpted_power","shadow_queen","bioluminescence","bioluminescent",
        # v11
        "riot_goddess","punk_queen","steel_warrior","cage_fighter",
    ],
    "🏖️ 비치 & 리조트": [
        "summer_beach","surfer_goddess","pool_goddess",
        "poolside_noir","infinity_pool","beach_bonfire",
        "scuba_goddess","glass_floor","glass_house","ski_chalet","vineyard_harvest","spa_noir",
        "balcony_goddess",
        # v11
        "sunset_cruise","coral_diving","beach_bonfire_night","hammock_resort",
    ],
    "🎭 퍼포먼스 & 댄스": [
        "flamenco_queen","tango_passion","circus_performer",
        "ribbon_dance","aerial_silk","fire_dancer","masquerade_ball",
        "opera_night","christmas_glamour","pop_art_glamour","ribbon_goddess","petal_storm",
        # v11
        "ballet_noir","broadway_diva","street_dance","drag_glamour",
        # v17
        "samba_carnival","hula_goddess","jazz_dance_glam","kathak_dance",
    ],
    "👘 전통 & 문화의상": [
        "geisha_noir","geisha_red","maiko_glamour","hanbok_glamour","qipao_noir","sari_goddess",
        "harem_goddess","belly_dancer","odalisque","imperial_silk",
        # v10
        "kimono_silk","ao_dai_sheer","thai_temple","indian_bridal","moroccan_kaftan",
        "persian_court","yoruba_glamour","balinese_goddess","chinese_qipao_slit","scottish_corset",
        # v17 보강
        "hanfu_goddess","cheongsam_slit","kebaya_java","dashiki_glam","kaftan_sheer",
        "flamenco_dress","dirndl_glam","hanbok_modern","ao_dai_glamour","saree_draped_sensual",
        # v19 — 한국 역사/전통
        "joseon_queen","joseon_consort","gisaeng_glamour","gisaeng_noir","mudang_shaman",
        "haenyeo_goddess","silla_empress","goguryeo_warrior","goryeo_empress","joseon_painter",
        "korean_shaman_fire","baekje_lotus","silla_gold_crown",
    ],
    "🌸 계절 & 테마": [
        "cherry_blossom","lavender_field","spring_rain","tulip_field","autumn_forest",
        "sunflower_field","greenhouse_eden","tropical_night",
        # v10
        "first_snow","golden_autumn","midsummer_heat","rainy_season","harvest_moon",
        "winter_solstice","cherry_blossom_night","tropical_monsoon",
        # v17
        "halloween_glam","new_year_glam","sakura_night_glam","monsoon_goddess",
    ],
    "🍬 팝 & 카와이": [
        # v10
        "y2k_fairy","pink_champagne","cotton_candy","angel_baby","idol_stage","kitty_glam",
        "strawberry_milk","cherry_pop","neon_kawaii","fairy_kei",
        # v13
        "gyaru_glam","kogal_style","hime_gyaru","decora_kei","maid_glamour","visual_kei",
        "lolita_gothic","disco_barbie","space_babe","bubblegum_pop","rainbow_rave","glitter_bomb",
        "arcade_queen","virtual_idol","tokimeki_pop","kpop_idol","korean_ulzzang","kbeauty_goddess",
        "kdrama_heroine","manga_girl",
        # v19 — K-컬처/뷰티
        "kpop_girl_crush","hallyu_goddess","kbeauty_glass_skin",
        "kdrama_villain_queen","kdrama_chaebol_heir","gangnam_luxury_glam",
        # 2026-06-08 누락 복구
        "bubble_tea","doll_house","harajuku_doll",
    ],

    "🎌 애니 & 글래머": [
        # v13 일본 계열
        "zero_suit","battle_bikini","succubus_anime","catgirl_luxe","dark_magical_girl",
        "witch_apprentice","fallen_angel_anime","kunoichi_glam","oni_warrior","samurai_bride",
        "dragon_princess","android_girl","pilot_suit","neon_android","vampire_seductress",
        # v13 글로벌 계열
        "cosmic_warrior_glam","dark_jester_glam","poison_ivy_vines","storm_goddess",
        "dark_sorceress_glam","jessica_rabbit_glam","webtoon_heroine","manhwa_villainess",
        "barbarella_retro","vampirella_dark","ghost_shell","android_2b","street_fighter_chun",
        "dark_elsa","sailor_moon_dark",
        # v24 — A형 실사 컨셉 7개 (특정 IP 회피, 일반 아키타입)
        "anime_swordmistress","anime_mecha_pilot","anime_shrine_maiden","anime_demon_slayer",
        "anime_galaxy_idol","anime_battle_angel","anime_cyber_ninja",
        # v24 — B형 2D 그림체 파일럿 2개 (실사 엔진 그림체 테스트 — 검증 필요)
        "anime_cel_shaded","anime_webtoon_style",
    ],

    # ── 🎨 애니 아트스타일 (2026-06-09 신설, 그림체 32종) ──
    "🎨 애니 아트스타일": [
        'anime_jp_90s_retro',
        'anime_jp_80s_citypop',
        'anime_jp_modern_glossy',
        'anime_jp_shoujo_soft',
        'anime_jp_shounen_action',
        'anime_jp_seinen_gritty',
        'anime_jp_makoto_watercolor',
        'anime_jp_ghibli_soft',
        'anime_jp_ecchi_glossy',
        'anime_jp_gekiga_noir',
        'anime_jp_pinup_retro',
        'anime_kr_webtoon_glossy',
        'anime_kr_romance_soft',
        'anime_kr_action_manhwa',
        'anime_kr_lezhin_mature',
        'anime_kr_pastel_dream',
        'anime_kr_lofi_chill',
        'anime_kr_noir_mature',
        'anime_cn_donghua_xianxia',
        'anime_cn_guofeng_ink',
        'anime_cn_modern_donghua',
        'anime_cn_palace_drama',
        'anime_us_cartoon_bold',
        'anime_us_comic_ink',
        'anime_us_pixar_stylized',
        'anime_us_disney_classic',
        'anime_us_pinup_classic',
        'anime_us_badgirl_comic',
        'anime_eu_ligne_claire',
        'anime_eu_graphic_novel',
        'anime_eu_erotic_bd',
        'anime_noir_silhouette',
    ],
}

# SS tier
SS_TIER = {
    # 기존 명화/예술 계열
    "bioluminescent_ink","galaxy_skin","klimt_gold_body","half_statue","vangogh_body",
    "dali_surreal","munch_scream","cherry_blossom_night","kitty_glam","yoruba_glamour",
    "ash_phoenix","lichtenstein_dot","warhol_pop","mondrian_body",
    # v14
    "lace_body_paint","jewelry_trompe_loeil",
    # v15 명화
    "klimt_silver","botticelli_venus","liquid_gold_drip","mermaid_scales","tiger_stripes_body",
    # v16 관능
    "latex_queen",
    # v18 동물 1차 테스트
    # v18 동물 SS — 엄격 재검토 후 확정 (2026-06-07)
    "mantis_shrimp","phoenix_rising","jellyfish_glow","panther_black",
    "octopus_ink","snow_leopard","scarab_beetle",
    "atlas_moth","eagle_wings","butterfly_monarch",
    "arctic_fox",  # SS 확정 (2026-06-08 설원 페이스페인팅+모피결 2장 검증 완료)
    # 2026-06-06 명화/작가 테스트 확정
    "degas_dancer","toulouse_lautrec","waterhouse_nymph",
    "takashi_murakami","yayoi_kusama","keith_haring_body",
    # 2026-06-06 한국테마 테스트 확정
    "dancheong_body","najeonchilgi_body","goryeo_celadon_body",
    "minhwa_body","korean_tiger_body","silla_crown_body",
    # 2026-06-06 동물/자연 테스트 확정
    "najeon_abalone","giraffe_pattern","zebra_stripes","dragon_scales_red",
    # 2026-06-06 추가 테스트 확정
    "alma_tadema","gauguin_tropics","melting_chocolate",
    # 2026-06-06 동물/조류/재테스트 확정 7개
    "parrot_tropical","boa_constrictor","king_cobra_hood","cheetah_speed",
    "bird_of_paradise","owl_feather","crocodile_skin",
    # 2026-06-07 한국 신수 4개
    "phoenix_jujakk","cheongnyong_dragon","korean_dragon_body","haetae_guardian",
    # 2026-06-07 v20 SS 6개
    "coral_reef_body","galaxy_nebula_body","islamic_geometric_body",
    "aztec_calendar_body","stained_glass_body","mushroom_forest_body",
    # 2026-06-07 문명/동물/부족 (국기 4개는 2026-06-08 강등)
    "hieroglyph_body","mexico_flag_body",
    "ocelot_wild","ndebele_pattern",
    # 2026-06-08 국기 계열 SS 재검토 — 강등 S 4개
    #   (union_jack_body, usa_stars_stripes_body, south_africa_flag_body, brazil_flag_body)
    #   사유: 원색 면분할=피부톤 근접도 낮음, 구상 모티프 없음 → SS 회화성 미달
    #   mexico_flag_body만 SS 유지 (중앙 국장=독수리+뱀 구상화, 명화/문명 계열에 닿음)
    # 2026-06-07 문명/자연/동물 6개
    "celtic_knot_body","greek_mosaic_body","ocean_depth_body",
    "weather_map_body","bauhaus_body","wolf_grey",
    # 2026-06-07 v22 에로틱&페티쉬 SS — 엄격 재검토 후 확정
    #   (강등 S: burlesque, dominatrix_glam, corset_stockings,
    #    dark_fairy_erotic, tape_bondage, metal_bondage)
    #   (제거: military_domme — 나치 상징 생성 리스크, 프리셋 수정 필요)
    # 2026-06-08 라텍스/광택소재 재검토: 강등 pvc_transparent_full/chrome_vixen/liquid_metal_body,
    #   승격 vampire_seduction/witch_sensual/latex_venom (±0)
    # 2026-06-08 서큐버스 재검토: dark_succubus 강등(succubus_full과 중복) → SS 105개
    "transparent_dress","sheer_catsuit","latex_transparent",
    "chrome_bodysuit","mirror_dress","suspension_art",
    "dominatrix_full_armor","goddess_throne",
    "doctor_sensual","police_dominatrix",
    "pole_dance_extreme","fire_goddess",
    "succubus_full","dark_angel_fallen","alien_queen_body",
    "body_paint_nude",
    "cabaret_star",
    # 2026-06-08 라텍스/광택소재 SS 재검토 — 승격 3개
    #   (강등 S: pvc_transparent_full, chrome_vixen, liquid_metal_body)
    #   (보류: latex_catsuit_red — 컬러 라텍스 중복, 재검토 대상)
    "vampire_seduction","witch_sensual","latex_venom",
    # 2026-06-09 애니 아트스타일 SS 10종 확정 (JP4/KR3/CN2/EU1)
    "anime_jp_80s_citypop","anime_jp_shoujo_soft","anime_jp_seinen_gritty","anime_jp_makoto_watercolor",
    "anime_kr_webtoon_glossy","anime_kr_action_manhwa","anime_kr_lofi_chill",
    "anime_cn_donghua_xianxia","anime_cn_palace_drama",
    "anime_eu_ligne_claire",
}

# ─── 다크 테마 CSS ────────────────────────────────────────
BG       = "#1e1e1e"
BG_SIDE  = "#252526"
BG_INPUT = "#2d2d2d"
BG_CARD  = "#2a2a2a"
GOLD     = "#c9a84c"
GOLD_DIM = "#8a6f30"
BORDER   = "#3a3a3a"
TEXT     = "#d4d4d4"
TEXT_DIM = "#888"

st.markdown(f"""
<style>
.stApp, [data-testid="stAppViewContainer"] {{ background-color: {BG} !important; }}
[data-testid="stHeader"] {{ background-color: {BG} !important; }}
[data-testid="stSidebar"] {{ background-color: {BG_SIDE} !important; border-right: 1px solid {BORDER} !important; }}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] label {{ color: {TEXT_DIM} !important; font-size: 0.78rem !important; }}
[data-testid="stSidebar"] h3 {{ color: {GOLD_DIM} !important; font-size: 0.65rem !important; letter-spacing: 2.5px !important; text-transform: uppercase !important; }}
h1, h2, h3, h4, h5 {{ color: {GOLD} !important; letter-spacing: 1.5px !important; }}
.stTabs [data-baseweb="tab-list"] {{ background-color: transparent !important; border-bottom: 1px solid {BORDER} !important; gap: 0 !important; }}
.stTabs [data-baseweb="tab"] {{ background-color: transparent !important; color: {TEXT_DIM} !important; font-size: 0.78rem !important; padding: 10px 20px !important; border-bottom: 2px solid transparent !important; }}
.stTabs [aria-selected="true"] {{ color: {GOLD} !important; border-bottom: 2px solid {GOLD} !important; background-color: transparent !important; }}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] {{ display: none !important; }}
.stSelectbox > div > div {{ background-color: {BG_INPUT} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; color: {TEXT} !important; font-size: 0.8rem !important; }}
.stSelectbox > div > div:hover {{ border-color: rgba(201,168,76,0.4) !important; }}
.stSelectbox > div > div:focus-within {{ border-color: rgba(201,168,76,0.7) !important; box-shadow: 0 0 0 1px rgba(201,168,76,0.2) !important; }}
.stSelectbox label {{ color: {GOLD} !important; font-size: 0.68rem !important; letter-spacing: 1.2px !important; text-transform: uppercase !important; font-weight: 600 !important; }}
.stSelectbox [data-baseweb="select"] span,
.stSelectbox [data-baseweb="select"] div,
.stSelectbox [data-baseweb="select"] input {{ color: {TEXT} !important; }}
[data-baseweb="popover"] [data-baseweb="menu"] {{ background-color: {BG_INPUT} !important; border: 1px solid {BORDER} !important; }}
[data-baseweb="popover"] li {{ background-color: {BG_INPUT} !important; color: {TEXT} !important; font-size: 0.8rem !important; }}
[data-baseweb="popover"] li:hover {{ background-color: rgba(201,168,76,0.1) !important; color: {GOLD} !important; }}
.stButton > button {{ border-radius: 6px !important; font-size: 0.75rem !important; letter-spacing: 1.5px !important; text-transform: uppercase !important; font-weight: 700 !important; transition: all 0.2s !important; height: 42px !important; }}
.stButton > button[kind="primary"] {{ background: linear-gradient(135deg, {GOLD}, {GOLD_DIM}) !important; border: none !important; color: #111 !important; }}
.stButton > button[kind="primary"]:hover {{ background: linear-gradient(135deg, #e8c96a, {GOLD}) !important; transform: translateY(-1px) !important; }}
.stButton > button[kind="secondary"] {{ background: transparent !important; border: 1px solid rgba(201,168,76,0.4) !important; color: {GOLD} !important; }}
.stButton > button[kind="secondary"]:hover {{ background: rgba(201,168,76,0.08) !important; border-color: rgba(201,168,76,0.7) !important; }}
.stRadio > div {{ gap: 6px !important; }}
.stRadio label {{ background: {BG_CARD} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; padding: 7px 12px !important; font-size: 0.78rem !important; color: {TEXT_DIM} !important; cursor: pointer !important; transition: all 0.2s !important; }}
.stRadio label:has(input:checked) {{ background: rgba(201,168,76,0.12) !important; border-color: rgba(201,168,76,0.5) !important; color: {GOLD} !important; }}
.stTextArea textarea {{ background-color: {BG_INPUT} !important; color: {TEXT} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; font-size: 0.78rem !important; line-height: 1.8 !important; }}
.stTextArea textarea:focus {{ border-color: rgba(201,168,76,0.5) !important; box-shadow: 0 0 0 1px rgba(201,168,76,0.15) !important; }}
.stCode {{ background-color: {BG_INPUT} !important; border: 1px solid rgba(201,168,76,0.25) !important; border-radius: 6px !important; }}
.stCode code {{ color: #ce9178 !important; font-size: 0.75rem !important; line-height: 1.8 !important; }}
.stCode button {{ background: rgba(201,168,76,0.1) !important; border: 1px solid rgba(201,168,76,0.3) !important; color: {GOLD} !important; border-radius: 4px !important; }}
[data-testid="stToggle"] > div {{ background-color: {GOLD} !important; }}
.stAlert {{ background-color: {BG_CARD} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; color: {TEXT_DIM} !important; font-size: 0.78rem !important; }}
hr {{ border-color: {BORDER} !important; margin: 12px 0 !important; }}
.stCaption {{ color: {TEXT_DIM} !important; font-size: 0.7rem !important; }}
p, li, .stMarkdown {{ color: {TEXT} !important; font-size: 0.82rem !important; }}
::-webkit-scrollbar {{ width: 4px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: {BORDER}; border-radius: 2px; }}
::-webkit-scrollbar-thumb:hover {{ background: {GOLD_DIM}; }}
</style>
""", unsafe_allow_html=True)

# ─── 헤더 ─────────────────────────────────────────────────
st.markdown('''
<div style="padding:8px 0 20px;">
  <div style="font-size:1.6rem;font-weight:700;letter-spacing:8px;color:#c9a84c;">✦ LumineX</div>
  <div style="font-size:0.65rem;letter-spacing:3px;color:#555;margin-top:4px;text-transform:uppercase;">AI Fashion Image Engine · v4.4</div>
</div>
''', unsafe_allow_html=True)

# ─── 사이드바 ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ 전역 설정")
    st.markdown("---")
    global_platform = st.radio("🖥️ 출력 플랫폼", options=["Gemini", "ChatGPT (DALL-E)", "Midjourney"], index=0)
    global_aspect   = st.selectbox("📐 이미지 비율", options=list(ASPECT_RATIOS.keys()), index=0, help="★ = 기본값 권장")
    global_realism      = st.toggle("📷 실사 모드", value=True)
    global_art_fallback = st.toggle("🎨 위험 시 아트 스타일", value=False, help="HIGH 위험 감지 시 수채화/흑백 자동 적용")
    st.markdown("---")
    st.markdown("### 🎬 영상 플랫폼")
    global_video_platform = st.radio("영상 생성 플랫폼", options=["Veo 3 (Gemini)", "Kling AI", "Runway", "Hailuo"], index=0)
    st.markdown("---")
    platform_colors = {"Gemini": "🔵", "ChatGPT (DALL-E)": "🟢", "Midjourney": "🟣"}
    st.markdown(f"**플랫폼:** {platform_colors[global_platform]} `{global_platform}`")
    st.markdown(f"**비율:** `{global_aspect.split('—')[0].strip()}`")
    if global_platform == "Gemini":
        st.markdown(f"**실사:** `{'ON ✅' if global_realism else 'OFF'}`")
    st.markdown("---")
    st.markdown("### 📌 사용법")
    st.markdown("1. 플랫폼 선택\n2. 탭 선택\n3. 요소 선택\n4. **프롬프트 조합** 클릭\n5. 코드박스 클릭 → 복사\n6. 해당 플랫폼에 붙여넣기")
    st.markdown("---")
    st.markdown("### 💡 플랫폼 팁")
    if global_platform == "Gemini":
        st.info("자연어 서술형. 길고 상세할수록 좋아요.")
    elif global_platform == "ChatGPT (DALL-E)":
        st.success("키워드 중심. 짧고 강렬하게!")
    else:
        st.warning("태그 나열 + --파라미터 방식.")
    if global_platform == "Gemini":
        st.markdown("---")
        st.markdown("### 🔄 Gemini 세션")
        if st.button("🆕 Gemini 새 창 열기", use_container_width=True, help="누적 맥락 초기화"):
            import webbrowser
            webbrowser.open("https://gemini.google.com/app")
        st.caption("💡 같은 창 반복 생성 시 타투/헤어 오염 주의")
    st.markdown("---")
    st.markdown("### 📊 프리셋 현황")
    total = sum(len(v) for v in PRESET_CATEGORIES.values())
    st.markdown(f"**총 프리셋:** `{total}개`")
    st.markdown(f"**SS tier:** `{len(SS_TIER)}개`")
    st.markdown(f"**카테고리:** `{len(PRESET_CATEGORIES)}개`")


def get_prompt(data: dict) -> str:
    if global_platform == "Gemini":
        return build_gemini_prompt(data, global_aspect, global_realism)
    elif global_platform == "ChatGPT (DALL-E)":
        return build_chatgpt_prompt(data, global_aspect)
    else:
        return build_midjourney_prompt(data, global_aspect)


tab1, tab2, tab3, tab4 = st.tabs(["🎨 프리셋 모드", "🛠️ 수동 조합", "🎲 랜덤 모드", "🎬 영상 프롬프트"])

# ══════════════════════════════════════════════════════════
# 탭 1: 프리셋 모드
# ══════════════════════════════════════════════════════════
with tab1:
    st.markdown("### 프리셋으로 프롬프트 생성")

    col_cat, col_search = st.columns([2, 1])
    with col_cat:
        all_cats = ["🌟 전체"] + list(PRESET_CATEGORIES.keys())
        selected_cat = st.selectbox("📂 카테고리 필터", options=all_cats, index=0, key="preset_cat_filter")
    with col_search:
        search_query = st.text_input("🔍 프리셋 검색", placeholder="이름 검색...", key="preset_search")

    all_presets = list_presets()
    if selected_cat == "🌟 전체":
        filtered_presets = all_presets
    else:
        cat_list = PRESET_CATEGORIES.get(selected_cat, [])
        filtered_presets = [p for p in all_presets if p in cat_list]

    if search_query:
        filtered_presets = [p for p in filtered_presets if search_query.lower() in p.lower()]

    def format_preset(name):
        if name in SS_TIER:
            return f"⭐ {name} [SS]"
        return f"• {name}"

    col1, col2 = st.columns([2, 1])
    with col1:
        if filtered_presets:
            selected_preset = st.selectbox(
                f"🎨 프리셋 선택 ({len(filtered_presets)}개)",
                options=filtered_presets,
                format_func=format_preset
            )
        else:
            st.warning("해당 카테고리에 프리셋이 없어요.")
            selected_preset = None
    with col2:
        if selected_cat != "🌟 전체":
            ss_count = sum(1 for p in filtered_presets if p in SS_TIER)
            st.markdown(f"""
<div style="background:{BG_CARD};border:1px solid {BORDER};border-radius:8px;padding:10px 14px;margin-top:28px;">
  <div style="font-size:0.65rem;color:{TEXT_DIM};letter-spacing:1px;">카테고리 현황</div>
  <div style="font-size:1.1rem;font-weight:700;color:{GOLD};margin-top:4px;">{len(filtered_presets)}개</div>
  <div style="font-size:0.7rem;color:{TEXT_DIM};">⭐ SS tier {ss_count}개</div>
</div>
""", unsafe_allow_html=True)

    if not selected_preset:
        st.stop()

    NONE = "None — 프리셋 기본값 사용"
    col1, col2, col3 = st.columns(3)
    with col1:
        preset_appearance  = st.selectbox("👩 인종/국적",       [NONE] + list(MODEL_APPEARANCE.keys()), key="preset_appearance")
        preset_age         = st.selectbox("🎂 연령대",          [NONE] + list(AGE_APPEARANCE.keys()),   key="preset_age")
        preset_body        = st.selectbox("👤 체형",            [NONE] + list(MODEL_TYPES.keys()),      key="preset_body")
        preset_outfit      = st.selectbox("👗 의상",            [NONE] + list(OUTFIT_TYPES.keys()),     key="preset_outfit")
        preset_material    = st.selectbox("🧵 소재",            [NONE] + list(MATERIALS.keys()),        key="preset_material")
        preset_footwear    = st.selectbox("👠 신발",            [NONE] + list(FOOTWEAR.keys()),         key="preset_footwear")
        preset_nails       = st.selectbox("💅 네일",            [NONE] + list(NAILS.keys()),            key="preset_nails")
        preset_skin_detail = st.selectbox("🌿 피부 디테일",     [NONE] + list(SKIN_DETAILS.keys()),     key="preset_skin_detail")
        preset_body_oil    = st.selectbox("✨ 바디 오일",        [NONE] + list(BODY_OIL.keys()),         key="preset_body_oil")
    with col2:
        preset_hair_style  = st.selectbox("💇 헤어스타일",      [NONE] + list(HAIR_STYLES.keys()),      key="preset_hair_style")
        preset_pose        = st.selectbox("💃 포즈",            [NONE] + list(POSES.keys()),            key="preset_pose")
        preset_framing     = st.selectbox("🖼️ 프레이밍",        [NONE] + list(FRAMING.keys()),          key="preset_framing")
        preset_angle       = st.selectbox("📸 카메라 앵글",     [NONE] + list(CAMERA_ANGLES.keys()),    key="preset_angle")
        preset_lighting    = st.selectbox("💡 조명",            [NONE] + list(LIGHTING.keys()),         key="preset_lighting")
        preset_color_grade = st.selectbox("🎨 색감",            [NONE] + list(COLOR_GRADES.keys()),     key="preset_color_grade")
        preset_style       = st.selectbox("🎬 스타일",          [NONE] + list(STYLES.keys()),           key="preset_style")
        preset_cover_style = st.selectbox("📰 커버 스타일",     [NONE] + list(COVER_STYLES.keys()),     key="preset_cover_style")
    with col3:
        preset_environment = st.selectbox("🏙️ 환경",            [NONE] + list(ENVIRONMENTS.keys()),     key="preset_environment")
        preset_weather     = st.selectbox("🌦️ 날씨",            [NONE] + list(WEATHER.keys()),          key="preset_weather")
        preset_image_style = st.selectbox("📐 이미지 스타일",   [NONE] + list(IMAGE_STYLE.keys()),      key="preset_image_style")
        preset_special_fx  = st.selectbox("🌈 특수 효과",       [NONE] + list(SPECIAL_EFFECTS.keys()),  key="preset_special_fx")
        preset_mood        = st.selectbox("🎭 무드",            [NONE] + list(MOOD.keys()),             key="preset_mood")

    col_a, col_b, _ = st.columns([1, 1, 2])
    with col_a:
        btn_ai    = st.button("🤖 AI 생성",   use_container_width=True, type="primary", key="preset_btn_ai")
    with col_b:
        btn_quick = st.button("⚡ 빠른 생성", use_container_width=True, key="preset_btn_quick")

    if "preset_prompt"   not in st.session_state: st.session_state.preset_prompt   = ""
    if "preset_selected" not in st.session_state: st.session_state.preset_selected = ""
    if selected_preset != st.session_state.preset_selected:
        st.session_state.preset_selected = selected_preset
        st.session_state.preset_prompt   = ""

    def build_preset_overrides() -> dict:
        overrides = {}
        if preset_appearance  != NONE: overrides['appearance']  = MODEL_APPEARANCE[preset_appearance]
        if preset_age         != NONE: overrides['age']         = AGE_APPEARANCE[preset_age]
        if preset_body        != NONE: overrides['body']        = MODEL_TYPES[preset_body]
        if preset_outfit      != NONE:
            od = OUTFIT_TYPES[preset_outfit]
            overrides['outfit'] = od["gemini"] if isinstance(od, dict) else od
        if preset_material    != NONE: overrides['material']    = MATERIALS[preset_material]
        if preset_pose        != NONE: overrides['pose']        = POSES[preset_pose]
        if preset_framing     != NONE: overrides['framing']     = FRAMING[preset_framing]
        if preset_angle       != NONE: overrides['angle']       = CAMERA_ANGLES[preset_angle]
        if preset_footwear    != NONE: overrides['footwear']    = FOOTWEAR[preset_footwear]
        if preset_nails       != NONE: overrides['nails']       = NAILS[preset_nails]
        if preset_skin_detail != NONE: overrides['skin_detail'] = SKIN_DETAILS[preset_skin_detail]
        if preset_body_oil    != NONE: overrides['body_oil']    = BODY_OIL[preset_body_oil]
        if preset_hair_style  != NONE: overrides['hair_style']  = HAIR_STYLES[preset_hair_style]
        if preset_color_grade != NONE: overrides['color_grade'] = COLOR_GRADES[preset_color_grade]
        if preset_lighting    != NONE: overrides['lighting']    = LIGHTING[preset_lighting]
        if preset_style       != NONE: overrides['style']       = STYLES[preset_style]
        if preset_cover_style != NONE: overrides['cover_style'] = COVER_STYLES[preset_cover_style]
        if preset_environment != NONE: overrides['environment'] = ENVIRONMENTS[preset_environment]
        if preset_weather     != NONE: overrides['weather']     = WEATHER[preset_weather]
        if preset_image_style != NONE: overrides['image_style'] = IMAGE_STYLE[preset_image_style]
        if preset_special_fx  != NONE: overrides['special_fx']  = SPECIAL_EFFECTS[preset_special_fx]
        if preset_mood        != NONE: overrides['mood']        = MOOD[preset_mood]
        return overrides

    def apply_overrides_to_prompt(preset: dict, overrides: dict) -> str:
        p = {**preset, **overrides}
        outfit_text   = p.get('outfit', '')
        material_text = p.get('material', '')
        footwear_text = overrides.get('footwear', '')
        wearing_line  = _build_wearing_line(outfit_text, material_text, footwear_text)
        return (
            f"Professional fashion photograph, {overrides.get('framing', 'full body shot')}. "
            f"{'Model appearance: ' + overrides['appearance'] + '. ' if 'appearance' in overrides else ''}"
            f"Model: {p.get('subject', 'a stunning female model')}. Body: {p.get('body', '')}. "
            f"{'Pose: ' + overrides['pose'] + '. ' if 'pose' in overrides else ''}"
            f"{wearing_line} "
            f"Environment: {p.get('environment', '')}. Lighting: {p.get('lighting', '')}. Style: {p.get('style', '')}. "
            f"{'Color grade: ' + overrides['color_grade'] + '. ' if 'color_grade' in overrides else ''}"
            f"{p.get('quality', 'ultra-sharp, 8K, professional photography')}."
        ).strip()

    if btn_ai and selected_preset:
        st.session_state.preset_prompt = ""
        with st.spinner("Claude가 프롬프트 생성 중..."):
            try:
                raw       = generate_prompt_with_ai(selected_preset)
                overrides = build_preset_overrides()
                prefix    = []
                if 'appearance' in overrides: prefix.append(overrides['appearance'].split(',')[0])
                if 'body'       in overrides: prefix.append(overrides['body'].split(',')[0])
                if prefix: raw = f"Model: {', '.join(prefix)}. " + raw
                aspect_desc = ASPECT_RATIOS.get(global_aspect, "")
                if aspect_desc: raw += f" {aspect_desc}."
                st.session_state.preset_prompt = raw
            except Exception as e:
                st.error(f"오류: {str(e)}")

    if btn_quick and selected_preset:
        st.session_state.preset_prompt = ""
        raw = apply_overrides_to_prompt(load_preset(selected_preset), build_preset_overrides())
        aspect_desc = ASPECT_RATIOS.get(global_aspect, "portrait 2:3 vertical")
        if global_platform == "Gemini":
            raw += f" {aspect_desc}."
        elif global_platform == "ChatGPT (DALL-E)":
            raw += f" {aspect_desc}. Photorealistic, hyperrealistic skin texture, award-winning fashion photography."
        else:
            ar = {"세로 2:3 — 인물 기본":"2:3","세로 3:4 — 전신샷":"3:4","가로 16:9 — 시네마틱":"16:9","가로 4:3 — 화보":"4:3","정방형 1:1 — 인스타":"1:1"}.get(global_aspect, "2:3")
            raw += f" --ar {ar} --style raw --q 2"
        st.session_state.preset_prompt = raw

    if st.session_state.preset_prompt:
        st.text_area("생성된 프롬프트", value=st.session_state.preset_prompt, height=160)
        st.code(st.session_state.preset_prompt, language=None)
        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")

# ══════════════════════════════════════════════════════════
# 탭 2: 수동 조합
# ══════════════════════════════════════════════════════════
with tab2:
    st.markdown("### 요소별 수동 조합")
    st.caption("💡 핵심 요소(외모/체형/의상/환경)만 선택해도 좋은 프롬프트가 나와요.")

    if st.button("🎲 전체 랜덤으로 채우기"):
        def rnd(d):
            keys = [k for k in d.keys() if k != "없음"]
            return random.choice(keys) if keys else "없음"
        st.session_state.r_appearance  = rnd(MODEL_APPEARANCE)
        st.session_state.r_model       = rnd(MODEL_TYPES)
        st.session_state.r_outfit      = rnd(OUTFIT_TYPES)
        st.session_state.r_material    = rnd(MATERIALS)
        st.session_state.r_env         = rnd(ENVIRONMENTS)
        st.session_state.r_light       = rnd(LIGHTING)
        st.session_state.r_framing     = rnd(FRAMING)
        st.session_state.r_angle       = rnd(CAMERA_ANGLES)
        st.session_state.r_style       = rnd(STYLES)
        st.session_state.r_cover_style = "없음"
        st.session_state.r_camera      = rnd(CAMERAS)
        st.session_state.r_pose        = rnd(POSES)
        st.session_state.r_expression  = rnd(EXPRESSION)
        st.session_state.r_skin_tone   = rnd(SKIN_TONES)
        st.session_state.r_hair_style  = rnd(HAIR_STYLES)
        st.session_state.r_hair_color  = rnd(HAIR_COLORS)
        st.session_state.r_makeup      = rnd(MAKEUP)
        def rnd_maybe(d, prob=0.5):
            return rnd(d) if random.random() < prob else "없음"
        st.session_state.r_footwear        = rnd_maybe(FOOTWEAR,       0.50)
        st.session_state.r_color_grade     = rnd_maybe(COLOR_GRADES,   0.50)
        st.session_state.r_accessories     = rnd_maybe(ACCESSORIES,    0.40)
        st.session_state.r_body_oil        = rnd_maybe(BODY_OIL,       0.30)
        st.session_state.r_weather         = rnd_maybe(WEATHER,        0.30)
        st.session_state.r_bg_crowd        = rnd_maybe(BG_CROWD,       0.30)
        st.session_state.r_mood            = rnd_maybe(MOOD,           0.30)
        st.session_state.r_time_of_day     = rnd_maybe(TIME_OF_DAY,   0.30)
        st.session_state.r_tattoo          = rnd_maybe(TATTOO,         0.15)
        st.session_state.r_special_effects = rnd_maybe(SPECIAL_EFFECTS,0.15)
        st.session_state.r_props           = rnd_maybe(PROPS,          0.15)
        st.session_state.r_image_style     = rnd_maybe(IMAGE_STYLE,    0.15)
        st.session_state.r_era             = rnd_maybe(ERA,            0.15)
        st.session_state.r_concept         = rnd_maybe(CONCEPT,        0.15)
        st.session_state.r_lens_effect     = rnd_maybe(LENS_EFFECT,    0.15)
        st.session_state.r_skin_detail     = rnd_maybe(SKIN_DETAILS,   0.20)
        st.session_state.r_nails           = rnd_maybe(NAILS,          0.30)
        st.session_state.r_cover_style     = rnd_maybe(COVER_STYLES,   0.20)
        st.session_state.r_age         = "없음"
        st.session_state.r_model_count = "1명 — 싱글 모델 (기본)"
        st.session_state.r_body_weight = "없음"
        st.session_state.r_bust_size   = "없음"
        st.session_state.r_hip_size    = "없음"
        st.session_state["use_separate_outfit"] = st.session_state.get("use_separate_outfit", False)
        if st.session_state.get("use_separate_outfit", False):
            top_keys = [k for k in TOP_TYPES.keys() if k != "없음 (의상 타입 사용)"]
            bot_keys = [k for k in BOTTOM_TYPES.keys() if k != "없음 (의상 타입 사용)"]
            if top_keys: st.session_state["r_top_type"] = random.choice(top_keys)
            if bot_keys: st.session_state["r_bottom_type"] = random.choice(bot_keys)
        st.rerun()

    def idx(d, key, default=0):
        keys = list(d.keys())
        val  = st.session_state.get(key, keys[default])
        return keys.index(val) if val in keys else default

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("##### 👤 모델")
        appearance  = st.selectbox("👩 외모 — 인종/국적",          list(MODEL_APPEARANCE.keys()), index=idx(MODEL_APPEARANCE, "r_appearance"))
        age         = st.selectbox("🎂 연령대",                     list(AGE_APPEARANCE.keys()),   index=idx(AGE_APPEARANCE,   "r_age"))
        model_type  = st.selectbox("👤 체형과 비율",               list(MODEL_TYPES.keys()),       index=idx(MODEL_TYPES,      "r_model"))
        body_weight = st.selectbox("⚖️ 체형 보정",                 list(BODY_WEIGHT.keys()),       index=idx(BODY_WEIGHT,      "r_body_weight"))
        bust_size   = st.selectbox("👙 가슴 보정",                  list(BUST_SIZE.keys()),         index=idx(BUST_SIZE,        "r_bust_size"))
        hip_size    = st.selectbox("🍑 힙 보정",                   list(HIP_SIZE.keys()),          index=idx(HIP_SIZE,         "r_hip_size"))
        skin_tone   = st.selectbox("🌊 피부 톤/질감",              list(SKIN_TONES.keys()),        index=idx(SKIN_TONES,       "r_skin_tone"))
        body_oil    = st.selectbox("✨ 바디 오일/글로스",           list(BODY_OIL.keys()),          index=idx(BODY_OIL,         "r_body_oil"))
        expression  = st.selectbox("😏 표정/눈빛",                 list(EXPRESSION.keys()),        index=idx(EXPRESSION,       "r_expression"))
        tattoo      = st.selectbox("🎨 문신/바디아트",              list(TATTOO.keys()),            index=idx(TATTOO,           "r_tattoo"))
        skin_detail = st.selectbox("🌿 피부 디테일",               list(SKIN_DETAILS.keys()),      index=idx(SKIN_DETAILS,     "r_skin_detail"))
        nails       = st.selectbox("💅 네일",                      list(NAILS.keys()),             index=idx(NAILS,            "r_nails"))
        model_count = st.selectbox("👥 모델 수",                   list(MODEL_COUNT.keys()),       index=idx(MODEL_COUNT,      "r_model_count"))
    with col2:
        st.markdown("##### 👗 스타일")
        use_separate = st.checkbox("✂️ 상하의 분리 선택", value=False, key="use_separate_outfit", help="상의+하의를 각각 선택해 조합")
        if use_separate:
            top_type    = st.selectbox("👕 상의",  list(TOP_TYPES.keys()),    index=0, key="r_top_type")
            bottom_type = st.selectbox("👖 하의",  list(BOTTOM_TYPES.keys()), index=0, key="r_bottom_type")
            top_label    = top_type.split("—")[0].strip()    if top_type    != "없음 (의상 타입 사용)" else "없음"
            bottom_label = bottom_type.split("—")[0].strip() if bottom_type != "없음 (의상 타입 사용)" else "없음"
            st.markdown(f"""
<div style="background:#2a2a2a;border:1px solid #c9a84c33;border-radius:8px;padding:8px 12px;margin:4px 0;">
  <span style="font-size:0.7rem;color:#888;letter-spacing:1px;">선택된 조합</span><br>
  <span style="background:#c9a84c22;border:1px solid #c9a84c55;border-radius:4px;padding:2px 8px;font-size:0.78rem;color:#c9a84c;margin-right:4px;">👕 {top_label}</span>
  <span style="color:#555;margin-right:4px;">+</span>
  <span style="background:#c9a84c22;border:1px solid #c9a84c55;border-radius:4px;padding:2px 8px;font-size:0.78rem;color:#c9a84c;">👖 {bottom_label}</span>
</div>
""", unsafe_allow_html=True)
            outfit = list(OUTFIT_TYPES.keys())[0]
        else:
            outfit      = st.selectbox("👗 의상 타입",  list(OUTFIT_TYPES.keys()), index=idx(OUTFIT_TYPES, "r_outfit"))
            top_type    = "없음 (의상 타입 사용)"
            bottom_type = "없음 (의상 타입 사용)"
        material    = st.selectbox("🧵 소재 — 옷감 질감",          list(MATERIALS.keys()),         index=idx(MATERIALS,        "r_material"))
        footwear    = st.selectbox("👠 신발",                      list(FOOTWEAR.keys()),          index=idx(FOOTWEAR,         "r_footwear"))
        pose        = st.selectbox("💃 포즈 — 자세와 동작",        list(POSES.keys()),             index=idx(POSES,            "r_pose"))
        hair_style  = st.selectbox("💇 헤어스타일",                list(HAIR_STYLES.keys()),       index=idx(HAIR_STYLES,      "r_hair_style"))
        hair_color  = st.selectbox("🎨 헤어컬러",                 list(HAIR_COLORS.keys()),       index=idx(HAIR_COLORS,      "r_hair_color"))
        makeup      = st.selectbox("💄 메이크업",                  list(MAKEUP.keys()),            index=idx(MAKEUP,           "r_makeup"))
        accessories = st.selectbox("💍 액세서리",                  list(ACCESSORIES.keys()),       index=idx(ACCESSORIES,      "r_accessories"))
        props       = st.selectbox("🎪 특별 소품",                 list(PROPS.keys()),             index=idx(PROPS,            "r_props"))
        era         = st.selectbox("🌍 시대/시간대",                list(ERA.keys()),               index=idx(ERA,              "r_era"))
        concept     = st.selectbox("🎭 컨셉/페르소나",              list(CONCEPT.keys()),           index=idx(CONCEPT,          "r_concept"))
    with col3:
        st.markdown("##### 🏙️ 환경")
        environment = st.selectbox("🏙️ 촬영 장소",                list(ENVIRONMENTS.keys()),      index=idx(ENVIRONMENTS,     "r_env"))
        weather     = st.selectbox("🌦️ 날씨/기상",                 list(WEATHER.keys()),           index=idx(WEATHER,          "r_weather"))
        time_of_day = st.selectbox("🕐 촬영 시간대",               list(TIME_OF_DAY.keys()),       index=idx(TIME_OF_DAY,      "r_time_of_day"))
        lighting    = st.selectbox("💡 조명 — 빛의 분위기",        list(LIGHTING.keys()),          index=idx(LIGHTING,         "r_light"))
        framing     = st.selectbox("🖼️ 프레이밍 — 구도/크기",      list(FRAMING.keys()),           index=idx(FRAMING,          "r_framing"))
        angle       = st.selectbox("📸 카메라 앵글",               list(CAMERA_ANGLES.keys()),     index=idx(CAMERA_ANGLES,    "r_angle"))
        camera      = st.selectbox("📷 카메라 — 장비",             list(CAMERAS.keys()),           index=idx(CAMERAS,          "r_camera"))
        lens_effect = st.selectbox("🔭 렌즈/초점 효과",            list(LENS_EFFECT.keys()),       index=idx(LENS_EFFECT,      "r_lens_effect"))
        style       = st.selectbox("🎬 스타일 — 화보 레퍼런스",    list(STYLES.keys()),            index=idx(STYLES,           "r_style"))
        cover_style = st.selectbox("📰 커버 스타일 — 잡지/화보",    list(COVER_STYLES.keys()),      index=idx(COVER_STYLES,     "r_cover_style"))
        color_grade = st.selectbox("🖼️ 색감 — 컬러 그레이딩",     list(COLOR_GRADES.keys()),      index=idx(COLOR_GRADES,     "r_color_grade"))
        mood        = st.selectbox("🎭 무드/분위기",               list(MOOD.keys()),              index=idx(MOOD,             "r_mood"))
        special_fx  = st.selectbox("🌈 특수 효과",                 list(SPECIAL_EFFECTS.keys()),   index=idx(SPECIAL_EFFECTS,  "r_special_effects"))
        img_style   = st.selectbox("📐 이미지 스타일",             list(IMAGE_STYLE.keys()),       index=idx(IMAGE_STYLE,      "r_image_style"))
        bg_crowd    = st.selectbox("👥 배경 인물",                 list(BG_CROWD.keys()),          index=idx(BG_CROWD,         "r_bg_crowd"))

    rec = get_combo_recommendations(model_type)
    if rec:
        with st.expander("✅ 이 체형에 잘 맞는 조합 추천", expanded=False):
            rc1, rc2, rc3 = st.columns(3)
            with rc1:
                st.markdown("**👗 의상**")
                for o in rec.get("outfit", []): st.markdown(f"{'🟡 ' if outfit == o else '• '}{o.split('—')[0].strip()}")
                st.markdown("**🧵 소재**")
                for m in rec.get("material", []): st.markdown(f"{'🟡 ' if material == m else '• '}{m.split('—')[0].strip()}")
            with rc2:
                st.markdown("**📸 앵글**")
                for a in rec.get("angle", []): st.markdown(f"{'🟡 ' if angle == a else '• '}{a.split('—')[0].strip()}")
                st.markdown("**💃 포즈**")
                for p in rec.get("pose", []): st.markdown(f"{'🟡 ' if pose == p else '• '}{p.split('—')[0].strip()}")
            with rc3:
                st.markdown("**🎬 스타일**")
                for s in rec.get("style", []): st.markdown(f"{'🟡 ' if style == s else '• '}{s.split('—')[0].strip()}")
                st.markdown("**🏙️ 환경**")
                for e in rec.get("env", []): st.markdown(f"{'🟡 ' if environment == e else '• '}{e.split('—')[0].strip()}")
            st.caption("🟡 = 현재 선택됨  •  = 추천 항목")

    conflicts = check_conflicts(angle, pose, style, environment, model_type, material, weather)
    if conflicts:
        for c in conflicts: st.warning(f"⚠️ {c}")

    col_x, col_y, col_z, _ = st.columns([1, 1, 1, 1])
    with col_x: btn_build      = st.button("✨ 프롬프트 조합", type="primary", use_container_width=True)
    with col_y: btn_ai_enhance = st.button("🤖 AI로 강화", use_container_width=True)
    with col_z: btn_ai_review  = st.button("🔍 AI 검수", use_container_width=True)

    if "manual_prompt" not in st.session_state: st.session_state.manual_prompt = ""
    if "review_result" not in st.session_state: st.session_state.review_result = ""

    if btn_ai_review:
        st.session_state.review_result = ""
        with st.spinner("Claude가 조합 검수 + 자동 수정 중..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                current_combo = {"model": model_type, "outfit": outfit, "material": material, "angle": angle, "pose": pose, "skin_tone": skin_tone, "body_oil": body_oil, "weather": weather, "style": style, "lighting": lighting, "expression": expression, "bg_crowd": bg_crowd, "img_style": img_style, "color_grade": color_grade}
                safe_options = {
                    "outfit":    [k for k in OUTFIT_TYPES.keys() if k not in ["코트 only — 롱코트만 입은 미니멀 글래머","란제리 에디토리얼 — VS 스타일, 실크 레이스","시스루 바디수트 — 메쉬, 아방가르드","브라탑+하이슬릿 — 브라탑, 롱 하이슬릿","마이크로 비키니 — 끈 비키니, SI 수영복 화보","모노키니 — 원피스 수영복 변형, 대담한 컷아웃"]],
                    "material":  [k for k in MATERIALS.keys() if k not in ["라텍스 — 피부 밀착, 세컨드스킨","시스루 오간자 — 반투명, 살이 비치는","PVC — 투명 비닐, 미래적","골드 체인 메쉬 — 금속 체인 망사"]],
                    "angle":     [k for k in CAMERA_ANGLES.keys() if k not in ["오버헤드 — 위에서 내려다보기","로우앵글 — 다리 강조, 아래서 위로"]],
                    "pose":      [k for k in POSES.keys() if k not in ["없음","수영장 물속 — 하반신 물에 잠긴","엎드린 포즈 — 배를 깔고 관능적","백포즈 — 뒤돌아 어깨 너머 시선","등 보이기 — 백뷰, 어깨 라인"]],
                    "skin_tone": [k for k in SKIN_TONES.keys() if k not in ["스웨티 — 운동 후 땀나는 느낌","오일드 스킨 — 윤기있는 글로시"]],
                    "body_oil":  ["없음", "라이트 글로우 — 자연스러운 윤기", "새틴 글로우 — 새틴처럼 빛나는"],
                    "weather":   [k for k in WEATHER.keys() if k not in ["폭우 — 거센 비, 극적인 분위기"]],
                    "style":     [k for k in STYLES.keys() if k not in ["빅토리아 시크릿 패션쇼","스포츠 일러스트레이티드 수영복"]],
                    "lighting":  list(LIGHTING.keys()),
                    "img_style": [k for k in IMAGE_STYLE.keys() if k not in ["더블 익스포저 — 이중 노출"]],
                }
                response = client.messages.create(
                    model="claude-sonnet-4-5", max_tokens=1200,
                    messages=[{"role": "user", "content": f"""You are an expert AI image generation filter analyst.
Analyze this combination for risks:
{chr(10).join([f"- {k}: {v}" for k, v in current_combo.items()])}
SAFE: body paint art, cultural costume, artistic context → high pass rate
Risk: 3+ risky elements = HIGH
Respond ONLY in JSON:
{{"risk_level": "HIGH/MEDIUM/LOW","issues": ["issue1"],"replacements": {{"outfit": "key or null","material": "key or null","angle": "key or null","pose": "key or null","skin_tone": "key or null","body_oil": "key or null","weather": "key or null","style": "key or null","img_style": "key or null"}},"summary": "한국어 2-3줄"}}"""}]
                )
                raw = response.content[0].text.strip()
                import json, re
                json_match = re.search(r'\{.*\}', raw, re.DOTALL)
                if json_match:
                    result = json.loads(json_match.group())
                    risk = result.get("risk_level", "UNKNOWN")
                    issues = result.get("issues", [])
                    repls = result.get("replacements", {})
                    summary = result.get("summary", "")
                    KEY_MAP = {"outfit":"r_outfit","material":"r_material","angle":"r_angle","pose":"r_pose","skin_tone":"r_skin_tone","body_oil":"r_body_oil","weather":"r_weather","style":"r_style","img_style":"r_image_style"}
                    replaced = {}
                    for field, new_val in repls.items():
                        if new_val and new_val != "null":
                            ss_key = KEY_MAP.get(field)
                            if ss_key:
                                st.session_state[ss_key] = new_val
                                replaced[field] = new_val
                    risk_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(risk, "⚪")
                    msg = f"{risk_emoji} **리스크: {risk}**\n\n"
                    if issues: msg += "**⚠️ 감지된 문제:**\n" + "\n".join([f"- {i}" for i in issues]) + "\n\n"
                    if replaced: msg += "**🔄 자동 교체:**\n" + "\n".join([f"- {k} → `{v.split('—')[0].strip()}`" for k, v in replaced.items()]) + "\n\n"
                    msg += f"**💬 요약:** {summary}"
                    st.session_state.review_result = msg
                    if replaced:
                        st.session_state._trigger_build = True
                        st.rerun()
            except Exception as e:
                st.session_state.review_result = f"오류: {str(e)}"

    if st.session_state.get("review_result"):
        st.markdown("---")
        st.markdown("#### 🔍 AI 검수 결과")
        st.markdown(st.session_state.review_result)
        st.markdown("---")

    if btn_build:
        def smart_update(key, d, prob):
            cur = st.session_state.get(key, "없음")
            if cur == "없음":
                keys = [k for k in d.keys() if k != "없음"]
                if keys and random.random() < prob:
                    st.session_state[key] = random.choice(keys)
        smart_update("r_pose",        POSES,          0.80)
        smart_update("r_expression",  EXPRESSION,     0.80)
        smart_update("r_skin_tone",   SKIN_TONES,     0.80)
        smart_update("r_hair_style",  HAIR_STYLES,    0.50)
        smart_update("r_hair_color",  HAIR_COLORS,    0.50)
        smart_update("r_makeup",      MAKEUP,         0.50)
        smart_update("r_footwear",    FOOTWEAR,       0.50)
        smart_update("r_color_grade", COLOR_GRADES,   0.50)
        smart_update("r_accessories", ACCESSORIES,    0.30)
        smart_update("r_body_oil",    BODY_OIL,       0.30)
        smart_update("r_weather",     WEATHER,        0.30)
        smart_update("r_bg_crowd",    BG_CROWD,       0.30)
        smart_update("r_tattoo",      TATTOO,         0.15)
        smart_update("r_special_effects", SPECIAL_EFFECTS, 0.15)
        smart_update("r_props",       PROPS,          0.15)
        smart_update("r_image_style", IMAGE_STYLE,    0.15)
        smart_update("r_era",         ERA,            0.15)
        smart_update("r_concept",     CONCEPT,        0.15)
        st.session_state._trigger_build = True
        st.session_state.r_outfit      = outfit
        st.session_state.r_material    = material
        st.session_state.r_angle       = angle
        st.session_state.r_model       = model_type
        st.session_state.r_age         = age
        st.session_state.r_model_count = model_count
        st.session_state.r_style       = style
        st.session_state.r_skin_tone   = skin_tone
        st.session_state.r_body_oil    = body_oil
        st.session_state.r_weather     = weather
        st.session_state.r_expression  = expression
        st.session_state.r_env         = environment
        st.session_state.r_light       = lighting
        st.session_state.r_camera      = camera
        st.session_state.r_mood        = mood
        st.session_state.r_time_of_day = time_of_day
        st.session_state.r_lens_effect = lens_effect
        manual_sel = set()
        if outfit != list(OUTFIT_TYPES.keys())[0]: manual_sel.add("r_outfit")
        if use_separate: manual_sel.add("r_outfit")
        filter_result = auto_filter_check(dict(st.session_state), platform=global_platform, manual_selections=manual_sel, art_fallback=global_art_fallback)
        if filter_result["replacements"]:
            for ss_key, new_val in filter_result["replacements"].items():
                st.session_state[ss_key] = new_val
            risk_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(filter_result["risk_level"], "⚪")
            replaced_labels = {"r_angle":"앵글","r_pose":"포즈","r_outfit":"의상","r_material":"소재","r_skin_tone":"피부","r_body_oil":"바디오일","r_style":"스타일","r_expression":"표정","r_model":"체형","r_image_style":"이미지스타일"}
            changed = "  |  ".join([f"{replaced_labels.get(k, k)} → **{v.split('—')[0].strip()}**" for k, v in filter_result["replacements"].items()])
            st.session_state._auto_filter_msg = f"{risk_emoji} 필터 자동 조정: {changed}"
        else:
            risk_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(filter_result["risk_level"], "⚪")
            st.session_state._auto_filter_msg = f"{risk_emoji} 필터 검수 통과 (점수: {filter_result['total_score']})"
        st.rerun()

    if st.session_state.get("_trigger_build", False):
        st.session_state._trigger_build = False
        def ss(key, d, default=None):
            keys = list(d.keys())
            val = st.session_state.get(key, keys[0] if keys else "없음")
            return val if val in d else (keys[0] if keys else "없음")
        _prev = {k: st.session_state.get(f"_prev_{k}", "없음") for k in ["r_pose","r_expression","r_skin_tone","r_hair_style","r_hair_color","r_makeup","r_footwear","r_color_grade","r_accessories","r_body_oil","r_weather","r_bg_crowd","r_tattoo","r_special_effects","r_props","r_image_style","r_era","r_concept"]}
        auto_labels = {"r_pose":"💃 포즈","r_expression":"😏 표정","r_skin_tone":"🌊 피부","r_hair_style":"💇 헤어","r_hair_color":"🎨 헤어컬러","r_makeup":"💄 메이크업","r_footwear":"👠 신발","r_color_grade":"🖼️ 색감","r_accessories":"💍 액세서리","r_body_oil":"✨ 바디오일","r_weather":"🌦️ 날씨","r_bg_crowd":"👥 배경","r_tattoo":"🎨 문신","r_special_effects":"🌈 특수효과","r_props":"🎪 소품","r_image_style":"📐 이미지스타일","r_era":"🌍 시대","r_concept":"🎭 컨셉"}
        picked_items = {}
        for key, label in auto_labels.items():
            cur = st.session_state.get(key, "없음")
            if _prev[key] == "없음" and cur != "없음":
                picked_items[label] = cur.split("—")[0].strip()
            st.session_state[f"_prev_{key}"] = cur
        if picked_items:
            st.session_state._auto_picked_msg = f"🎲 자동 선택: {'  |  '.join([f'{k} → **{v}**' for k, v in picked_items.items()])}"
        else:
            st.session_state._auto_picked_msg = ""
        data = {
            "appearance": ss("r_appearance", MODEL_APPEARANCE), "age": ss("r_age", AGE_APPEARANCE),
            "model": ss("r_model", MODEL_TYPES), "outfit": ss("r_outfit", OUTFIT_TYPES),
            "material": ss("r_material", MATERIALS), "footwear": ss("r_footwear", FOOTWEAR),
            "pose": ss("r_pose", POSES), "color_grade": ss("r_color_grade", COLOR_GRADES),
            "hair_style": ss("r_hair_style", HAIR_STYLES), "hair_color": ss("r_hair_color", HAIR_COLORS),
            "makeup": ss("r_makeup", MAKEUP), "accessories": ss("r_accessories", ACCESSORIES),
            "skin_tone": ss("r_skin_tone", SKIN_TONES), "model_count": ss("r_model_count", MODEL_COUNT),
            "era": ss("r_era", ERA), "concept": ss("r_concept", CONCEPT),
            "special_effects": ss("r_special_effects", SPECIAL_EFFECTS),
            "image_style": ss("r_image_style", IMAGE_STYLE), "props": ss("r_props", PROPS),
            "body_weight": ss("r_body_weight", BODY_WEIGHT), "bust_size": ss("r_bust_size", BUST_SIZE),
            "hip_size": ss("r_hip_size", HIP_SIZE), "weather": ss("r_weather", WEATHER),
            "expression": ss("r_expression", EXPRESSION), "tattoo": ss("r_tattoo", TATTOO),
            "skin_detail": ss("r_skin_detail", SKIN_DETAILS), "nails": ss("r_nails", NAILS),
            "body_oil": ss("r_body_oil", BODY_OIL), "bg_crowd": ss("r_bg_crowd", BG_CROWD),
            "mood": ss("r_mood", MOOD), "time_of_day": ss("r_time_of_day", TIME_OF_DAY),
            "lens_effect": ss("r_lens_effect", LENS_EFFECT), "env": ss("r_env", ENVIRONMENTS),
            "light": ss("r_light", LIGHTING), "framing": ss("r_framing", FRAMING),
            "angle": ss("r_angle", CAMERA_ANGLES), "style": ss("r_style", STYLES),
            "cover_style": ss("r_cover_style", COVER_STYLES), "camera": ss("r_camera", CAMERAS),
            "top_type": st.session_state.get("r_top_type", "없음 (의상 타입 사용)"),
            "bottom_type": st.session_state.get("r_bottom_type", "없음 (의상 타입 사용)"),
        }
        st.session_state.manual_prompt = get_prompt(data)

    if st.session_state.get("_auto_picked_msg"): st.info(st.session_state._auto_picked_msg)
    if st.session_state.get("_auto_filter_msg"):
        msg = st.session_state._auto_filter_msg
        if "🔴" in msg: st.warning(msg)
        elif "🟡" in msg: st.info(msg)
        else: st.success(msg)

    if btn_ai_enhance and st.session_state.manual_prompt:
        with st.spinner("Claude가 프롬프트 강화 중..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                platform_instruction = {"Gemini": "Make it detailed and descriptive (150-200 words), natural language style.", "ChatGPT (DALL-E)": "Make it concise and keyword-focused (under 80 words), punchy style.", "Midjourney": "Convert to comma-separated tags with --ar 2:3 --style raw --q 2 at the end."}
                response = client.messages.create(model="claude-sonnet-4-5", max_tokens=500,
                    messages=[{"role": "user", "content": f"Enhance this fashion photography prompt for {global_platform}.\nRules: model fills frame, photorealistic skin.\n{platform_instruction[global_platform]}\nOutput ONLY the prompt:\n\n{st.session_state.manual_prompt}"}])
                st.session_state.manual_prompt = response.content[0].text.strip()
            except Exception as e:
                st.error(f"오류: {str(e)}")

    if st.session_state.manual_prompt:
        st.text_area("조합된 프롬프트", value=st.session_state.manual_prompt, height=160)
        st.code(st.session_state.manual_prompt, language=None)
        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")

# ══════════════════════════════════════════════════════════
# 탭 3: 랜덤 모드
# ══════════════════════════════════════════════════════════
with tab3:
    st.markdown("### 완전 랜덤 프롬프트 생성")
    st.caption("핵심 요소만 랜덤 조합 — 프롬프트 최적 길이 유지")
    col1, col2, _ = st.columns([1, 1, 2])
    with col1: btn_rand    = st.button("🎲 랜덤 생성", type="primary", use_container_width=True)
    with col2: btn_rand_ai = st.button("🤖 AI 랜덤", use_container_width=True)
    if "random_prompt" not in st.session_state: st.session_state.random_prompt = ""
    if btn_rand:
        data = {"appearance": random.choice(list(MODEL_APPEARANCE.keys())), "age": "없음", "model": random.choice(list(MODEL_TYPES.keys())), "outfit": random.choice(list(OUTFIT_TYPES.keys())), "material": random.choice(list(MATERIALS.keys())), "footwear": "없음", "pose": random.choice(list(POSES.keys())), "color_grade": "없음", "hair_style": "없음", "hair_color": "없음", "makeup": "없음", "accessories": "없음", "skin_tone": "없음", "model_count": "1명 — 싱글 모델 (기본)", "era": "없음", "concept": "없음", "special_effects": "없음", "image_style": "없음", "props": "없음", "body_weight": "없음", "bust_size": "없음", "hip_size": "없음", "env": random.choice(list(ENVIRONMENTS.keys())), "light": random.choice(list(LIGHTING.keys())), "angle": random.choice(list(CAMERA_ANGLES.keys())), "style": random.choice(list(STYLES.keys())), "camera": random.choice(list(CAMERAS.keys())), "top_type": "없음 (의상 타입 사용)", "bottom_type": "없음 (의상 타입 사용)"}
        st.session_state.random_prompt = get_prompt(data)
    if btn_rand_ai:
        preset_name = random.choice(list_presets())
        with st.spinner(f"Claude가 [{preset_name}] 기반으로 생성 중..."):
            try:
                st.session_state.random_prompt = generate_prompt_with_ai(preset_name)
            except Exception as e:
                st.error(f"오류: {str(e)}")
    if st.session_state.random_prompt:
        st.text_area("랜덤 프롬프트", value=st.session_state.random_prompt, height=160)
        st.code(st.session_state.random_prompt, language=None)
        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#444;font-size:0.75rem;">✦ LumineX v4.4 — AI Fashion Image Engine</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# 탭 4: 영상 프롬프트
# ══════════════════════════════════════════════════════════
with tab4:
    st.markdown(f"### 🎬 영상 프롬프트 생성 — {global_video_platform}")
    VIDEO_PLATFORM_TIPS = {"Veo 3 (Gemini)": ("🔵", "gemini.google.com", "Gemini Advanced 구독 필요. 좌측 메뉴에서 Veo 3 선택."), "Kling AI": ("🟡", "klingai.com", "무료 티어 사용 가능. 매일 크레딧 지급."), "Runway": ("🟢", "runwayml.com", "무료 크레딧 제공. Gen-3 Alpha 사용."), "Hailuo": ("🟠", "hailuoai.video", "완전 무료. 중국 서비스.")}
    color, url, tip = VIDEO_PLATFORM_TIPS[global_video_platform]
    st.info(f"{color} **{global_video_platform}** — {tip} → [{url}](https://{url})")
    VIDEO_DURATIONS  = {"5초 — 짧고 임팩트 있는": "5 seconds", "8초 — 표준 클립": "8 seconds", "10초 — 긴 클립": "10 seconds"}
    VIDEO_MOTIONS    = {"워킹 — 런웨이 워크, 카메라 정면": "walking towards camera, confident runway walk, slow motion", "턴 — 360도 회전, 의상 전체 공개": "slow 360 degree turn, revealing full outfit", "포즈 — 정적 포즈, 바람에 머리 날림": "standing pose, hair flowing in wind, subtle movement", "댄스 — 섹시한 느낌의 부드러운 움직임": "slow sensual dance movement, fluid motion", "워킹+턴 — 걷다가 카메라 보며 턴": "walking then turning to camera, fashion editorial motion", "등장 — 안개/빛 속에서 천천히 등장": "emerging slowly from mist and light, dramatic entrance"}
    VIDEO_CAMERAS    = {"시네마틱 — 느린 달리샷": "slow cinematic dolly shot, smooth camera movement", "오빗 — 모델 주위를 도는 카메라": "slow orbit around subject, 360 camera movement", "줌인 — 전신에서 얼굴로 천천히 줌": "slow zoom from full body to face, intimate close-up", "로우앵글 — 아래서 위로 올려다보기": "low angle upward camera, powerful perspective", "하이앵글 — 위에서 내려다보기": "high angle downward camera, elegant perspective", "핸드헬드 — 약간의 흔들림, 현장감": "slight handheld camera movement, documentary feel"}
    VIDEO_ATMOSPHERES = {"럭셔리 글래머 — 화려하고 고급스러운": "luxury glamour atmosphere, high-end fashion film", "다크 시네마틱 — 어둡고 영화적인": "dark cinematic atmosphere, noir fashion film", "골든아워 — 따뜻한 황금빛": "golden hour warm light, dreamy fashion film", "네온 사이버펑크 — 미래적 네온 분위기": "neon cyberpunk atmosphere, futuristic fashion film", "미니멀 클린 — 깔끔하고 모던한": "minimal clean white atmosphere, modern fashion film", "에디토리얼 — 잡지 화보 느낌": "editorial fashion film, Vogue video style"}
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**📝 기존 프롬프트 기반으로 변환**")
        source_prompt  = st.text_area("이미지 프롬프트 붙여넣기 (선택사항)", placeholder="기존 이미지 프롬프트를 여기에 붙여넣으면 영상용으로 변환해줘요...", height=120, key="video_source")
        video_duration = st.selectbox("⏱️ 영상 길이", list(VIDEO_DURATIONS.keys()))
        video_motion   = st.selectbox("🏃 모션 타입", list(VIDEO_MOTIONS.keys()))
    with col2:
        video_camera     = st.selectbox("📷 카메라 무브먼트", list(VIDEO_CAMERAS.keys()))
        video_atmosphere = st.selectbox("🌟 분위기", list(VIDEO_ATMOSPHERES.keys()))
        video_appearance = st.selectbox("👩 모델 외모", ["None — 프롬프트 기반"] + list(MODEL_APPEARANCE.keys()), key="video_appearance")
        video_outfit     = st.selectbox("👗 의상", ["None — 프롬프트 기반"] + list(OUTFIT_TYPES.keys()), key="video_outfit")
    st.markdown("")
    col_x, col_y, _ = st.columns([1, 1, 2])
    with col_x: btn_video_build = st.button("🎬 영상 프롬프트 생성", type="primary", use_container_width=True)
    with col_y: btn_video_ai    = st.button("🤖 AI로 강화", use_container_width=True, key="btn_video_ai")
    if "video_prompt" not in st.session_state: st.session_state.video_prompt = ""
    if btn_video_build:
        st.session_state.video_prompt = ""
        appearance_str = f"Model: {MODEL_APPEARANCE[video_appearance].split(',')[0]}. " if video_appearance != "None — 프롬프트 기반" else ""
        outfit_str = ""
        if video_outfit != "None — 프롬프트 기반":
            od = OUTFIT_TYPES[video_outfit]
            outfit_str = f"Wearing: {(od['gemini'] if isinstance(od, dict) else od).split(',')[0]}. "
        base = f"Based on: {source_prompt[:200]}. " if source_prompt else ""
        st.session_state.video_prompt = (f"Cinematic fashion video, {VIDEO_DURATIONS[video_duration]}. {base}{appearance_str}{outfit_str}Motion: {VIDEO_MOTIONS[video_motion]}. Camera: {VIDEO_CAMERAS[video_camera]}. Atmosphere: {VIDEO_ATMOSPHERES[video_atmosphere]}. Photorealistic, hyperrealistic, 4K cinematic quality, professional fashion film, no text, no watermark.")
    if btn_video_ai and (source_prompt or st.session_state.video_prompt):
        with st.spinner("Claude가 영상 프롬프트 강화 중..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                base = source_prompt or st.session_state.video_prompt
                response = client.messages.create(model="claude-sonnet-4-5", max_tokens=500,
                    messages=[{"role": "user", "content": f"You are an expert video prompt engineer.\nCreate a powerful cinematic fashion video prompt based on this: {base}\nSettings: Duration: {VIDEO_DURATIONS[video_duration]}, Motion: {VIDEO_MOTIONS[video_motion]}, Camera: {VIDEO_CAMERAS[video_camera]}, Atmosphere: {VIDEO_ATMOSPHERES[video_atmosphere]}\nRules: Cinematic, photorealistic, 4K. No text overlays. Output ONLY the prompt, 100-150 words."}])
                st.session_state.video_prompt = response.content[0].text.strip()
            except Exception as e:
                st.error(f"오류: {str(e)}")
    if st.session_state.video_prompt:
        st.text_area("생성된 영상 프롬프트", value=st.session_state.video_prompt, height=180)
        st.code(st.session_state.video_prompt, language=None)
        st.caption("👆 복사 후 해당 플랫폼에 붙여넣으세요!")
        st.markdown("---")
        st.markdown(f"### 💡 {global_video_platform} 사용 방법")
        if global_video_platform == "Veo 3 (Gemini)":
            st.markdown("1. [gemini.google.com](https://gemini.google.com) 접속\n2. 좌측 **Veo 3** 선택\n3. 위 프롬프트 붙여넣기\n4. 생성 클릭!")
        elif global_video_platform == "Kling AI":
            st.markdown("1. [klingai.com](https://klingai.com) 접속\n2. **Text to Video** 선택\n3. 위 프롬프트 붙여넣기\n4. 생성 클릭!")
        elif global_video_platform == "Runway":
            st.markdown("1. [runwayml.com](https://runwayml.com) 접속\n2. **Gen-3 Alpha** 선택\n3. 위 프롬프트 붙여넣기\n4. 생성 클릭!")
        else:
            st.markdown("1. [hailuoai.video](https://hailuoai.video) 접속\n2. **Text to Video** 선택\n3. 위 프롬프트 붙여넣기\n4. 생성 클릭!")