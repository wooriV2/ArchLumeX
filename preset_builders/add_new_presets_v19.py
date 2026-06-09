"""
add_new_presets_v19.py
한국 테마 프리셋 43개

🎨 한국 바디아트 (10개)
  dancheong_body, najeonchilgi_body, goryeo_celadon_body, minhwa_body,
  korean_tiger_body, pojagi_body, taegeuk_body, silla_crown_body,
  dansaekhwa_body, najeon_abalone

🏯 역사/왕조/전통 (13개)
  joseon_queen, joseon_consort, gisaeng_glamour, gisaeng_noir,
  mudang_shaman, haenyeo_goddess, silla_empress, goguryeo_warrior,
  goryeo_empress, joseon_painter, korean_shaman_fire, baekje_lotus, silla_gold_crown

🐯 한국 동물/신수 (9개)
  haetae_guardian, dokkaebi_spirit, baekhak_crane, korean_dragon_body,
  phoenix_jujakk, baekho_white_tiger, hyeonmu_turtle, cheongnyong_dragon, korean_tiger_spirit

🌸 한국 자연/식물/장소 (5개)
  mugunghwa_body, korean_lotus_body, korean_plum_body, korean_bamboo_body, gyeongbokgung_night

🎭 K-컬처/뷰티/패션 (6개)
  kpop_girl_crush, hallyu_goddess, kbeauty_glass_skin,
  kdrama_villain_queen, kdrama_chaebol_heir, gangnam_luxury_glam

총 프리셋: 655 → 698개
"""

import json
from pathlib import Path

PRESETS_DIR = Path("presets")
PRESETS_DIR.mkdir(exist_ok=True)

new_presets = {
    "baekhak_crane": {
        "tag": "Baekhak Crane",
        "subject": "a graceful Korean white crane goddess female model",
        "body": "slim elegance model, graceful long-necked figure, baekhak crane goddess elegant presence",
        "outfit": "Korean white crane feather patterns painted directly on bare skin, NOT wearing fabric, crane wing body art",
        "material": "white crane feather paint on bare skin, elegant Korean bird body art",
        "environment": "Korean pine forest mist, white crane realm, elegant Korean atmosphere",
        "lighting": "soft Korean pine mist light, crane elegant atmosphere, baekhak white glow",
        "style": "baekhak crane body art editorial, Korean elegant bird glamour photography",
        "quality": "shot on Hasselblad H6D, soft white misty grade, portrait 2:3 vertical"
    },
    "baekho_white_tiger": {
        "tag": "Baekho White Tiger",
        "subject": "a divine Baekho white tiger goddess female model",
        "body": "slim elegance model, divine white tiger figure, Baekho western guardian presence",
        "outfit": "Korean Baekho white tiger stripe patterns painted directly on bare skin, NOT wearing fabric, divine white tiger body art",
        "material": "Baekho pure white tiger stripe paint on bare skin, Korean divine guardian body art",
        "environment": "Korean western heavenly realm, divine white tiger atmosphere",
        "lighting": "cold divine western light, Baekho white tiger atmosphere, divine guardian glow",
        "style": "Baekho white tiger body art editorial, Korean divine guardian glamour photography",
        "quality": "shot on Phase One XF IQ4, pure white divine grade, portrait 2:3 vertical"
    },
    "baekje_lotus": {
        "tag": "Baekje Lotus",
        "subject": "a graceful Baekje dynasty lotus female model",
        "body": "slim elegance model, Baekje elegant figure, Baekje lotus goddess presence",
        "outfit": "Baekje dynasty lotus pattern ceremonial dress, elegant Baekje court costume",
        "material": "Baekje silk lotus embroidery dress, Baekje dynasty accessories",
        "environment": "Baekje ancient palace, lotus pond, Korean ancient dynasty atmosphere",
        "lighting": "soft lotus pond light, Baekje elegant atmosphere, ancient Korean lotus glow",
        "style": "Baekje lotus editorial, ancient Korean glamour photography",
        "quality": "shot on Hasselblad H6D, soft lotus grade, portrait 2:3 vertical"
    },
    "cheongnyong_dragon": {
        "tag": "Cheongnyong Dragon",
        "subject": "a divine Cheongnyong blue dragon goddess female model",
        "body": "slim elegance model, divine blue eastern dragon figure, Cheongnyong eastern guardian presence",
        "outfit": "Korean Cheongnyong blue eastern dragon scale patterns painted directly on bare skin, NOT wearing fabric, divine blue dragon body art",
        "material": "Cheongnyong electric blue dragon scale paint on bare skin, Korean eastern guardian body art",
        "environment": "Korean eastern heavenly spring realm, divine blue dragon atmosphere",
        "lighting": "electric blue divine eastern light, Cheongnyong dragon atmosphere, Korean divine blue glow",
        "style": "Cheongnyong dragon body art editorial, Korean divine eastern glamour photography",
        "quality": "shot on Phase One XF IQ4, electric blue divine grade, portrait 2:3 vertical"
    },
    "dancheong_body": {
        "tag": "Dancheong Body",
        "subject": "a Korean dancheong five color body art female model",
        "body": "slim elegance model, Korean traditional figure, dancheong five color goddess presence",
        "outfit": "Korean traditional dancheong obangsaek five color patterns painted directly on bare skin, NOT wearing fabric, blue red yellow black white sacred pattern body art",
        "material": "dancheong obangsaek five sacred colors paint on bare skin, traditional Korean palace pattern body art",
        "environment": "Korean traditional palace hall, dancheong ceiling, Joseon dynasty atmosphere",
        "lighting": "warm palace hall light, obangsaek five color glow, traditional Korean atmosphere",
        "style": "dancheong body art editorial, Korean traditional palace glamour photography",
        "quality": "shot on Phase One XF IQ4, vibrant obangsaek grade, portrait 2:3 vertical"
    },
    "dansaekhwa_body": {
        "tag": "Dansaekhwa Body",
        "subject": "a minimal Korean dansaekhwa monochrome body art female model",
        "body": "slim elegance model, minimal meditative figure, dansaekhwa goddess zen presence",
        "outfit": "Korean dansaekhwa monochrome repetitive line patterns painted directly on bare skin, NOT wearing fabric, meditative repetition body art",
        "material": "dansaekhwa monochrome repetitive line paint on bare skin, Korean contemporary art body art",
        "environment": "minimal white gallery, Korean contemporary art atmosphere",
        "lighting": "clean minimal gallery light, meditative atmosphere, dansaekhwa zen glow",
        "style": "dansaekhwa body art editorial, Korean contemporary art glamour photography",
        "quality": "shot on Hasselblad H6D, minimal monochrome grade, portrait 2:3 vertical"
    },
    "dokkaebi_spirit": {
        "tag": "Dokkaebi Spirit",
        "subject": "a mischievous dokkaebi spirit goddess female model",
        "body": "slim elegance model, playful spirit figure, Korean dokkaebi goddess presence",
        "outfit": "Korean dokkaebi goblin spirit costume, horn accessories, club, playful spirit styling",
        "material": "dokkaebi costume, spirit horn accessories, Korean goblin club element",
        "environment": "Korean mountain forest night, dokkaebi spirit realm, Korean folklore",
        "lighting": "mysterious spirit night light, dokkaebi mischief atmosphere, Korean goblin glow",
        "style": "dokkaebi spirit editorial, Korean folklore glamour photography",
        "quality": "shot on Canon EOS R5, mysterious Korean grade, portrait 2:3 vertical"
    },
    "gangnam_luxury_glam": {
        "tag": "Gangnam Luxury Glam",
        "subject": "a ultra-chic Gangnam luxury glamour female model",
        "body": "slim elegance model, Gangnam ultra-chic figure, Korean luxury district goddess presence",
        "outfit": "Gangnam district ultra-luxury fashion, Korean designer outfit, Gangnam style accessories",
        "material": "Korean luxury designer fabric, Gangnam accessories, ultra-chic Korean elements",
        "environment": "Gangnam luxury boutique, COEX mall, Korean luxury district atmosphere",
        "lighting": "Gangnam luxury boutique light, ultra-chic atmosphere, Korean luxury district glow",
        "style": "Gangnam luxury editorial, Korean district glamour photography",
        "quality": "shot on Hasselblad H6D, ultra-chic Korean grade, portrait 2:3 vertical"
    },
    "gisaeng_glamour": {
        "tag": "Gisaeng Glamour",
        "subject": "a alluring Korean gisaeng glamour female model",
        "body": "slim elegance model, gisaeng graceful sensual figure, Korean courtesan goddess presence",
        "outfit": "Korean gisaeng glamour dress, colorful chima jeogori, elaborate hair accessories, sensual Korean courtesan styling",
        "material": "colorful silk chima jeogori, elaborate binyeo hair accessories, gisaeng accessories",
        "environment": "Joseon dynasty gisaeng house, lantern light, Korean courtesan atmosphere",
        "lighting": "warm lantern gisaeng atmosphere, Korean courtesan sensual light, gisaeng glow",
        "style": "gisaeng glamour editorial, Korean courtesan glamour photography",
        "quality": "shot on Leica SL2, warm lantern Korean grade, portrait 2:3 vertical"
    },
    "gisaeng_noir": {
        "tag": "Gisaeng Noir",
        "subject": "a mysterious gisaeng noir female model",
        "body": "slim elegance model, dark mysterious gisaeng figure, Korean noir courtesan presence",
        "outfit": "dark gisaeng noir costume, black silk chima, mysterious Korean courtesan dark styling",
        "material": "black silk dark chima jeogori, mysterious accessories, noir Korean courtesan",
        "environment": "dark Joseon night, gisaeng noir atmosphere, mysterious Korean night",
        "lighting": "low candle noir light, mysterious Korean night atmosphere, gisaeng dark glow",
        "style": "gisaeng noir editorial, Korean dark courtesan photography",
        "quality": "shot on Leica SL2, dark noir Korean grade, portrait 2:3 vertical"
    },
    "goguryeo_warrior": {
        "tag": "Goguryeo Warrior",
        "subject": "a fierce Goguryeo warrior goddess female model",
        "body": "athletic fitness model, ancient Korean warrior figure, Goguryeo warrior queen presence",
        "outfit": "Goguryeo mural painting warrior goddess costume, ancient Korean warrior armor styling",
        "material": "Goguryeo ancient warrior costume, mural painting style, ancient Korean armor elements",
        "environment": "Goguryeo tomb mural setting, ancient Korean warrior atmosphere",
        "lighting": "dramatic ancient tomb light, warrior goddess atmosphere, Goguryeo mural glow",
        "style": "Goguryeo warrior editorial, ancient Korean warrior glamour photography",
        "quality": "shot on Sony A7R V, dramatic ancient grade, portrait 2:3 vertical"
    },
    "goryeo_celadon_body": {
        "tag": "Goryeo Celadon Body",
        "subject": "a ethereal Goryeo celadon jade body art female model",
        "body": "slim elegance model, jade celadon figure, Goryeo celadon goddess ethereal presence",
        "outfit": "Goryeo celadon jade green cloud crane patterns painted directly on bare skin, NOT wearing fabric, jade celadon body art",
        "material": "Goryeo celadon jade green paint with crane cloud inlay on bare skin, Korean celadon body art",
        "environment": "Goryeo dynasty pottery chamber, celadon jade atmosphere, Korean heritage",
        "lighting": "soft jade celadon light, crane cloud atmosphere, Goryeo ethereal glow",
        "style": "Goryeo celadon body art editorial, Korean jade glamour photography",
        "quality": "shot on Hasselblad H6D, soft jade celadon grade, portrait 2:3 vertical"
    },
    "goryeo_empress": {
        "tag": "Goryeo Empress",
        "subject": "a magnificent Goryeo dynasty empress female model",
        "body": "luxury glamour model, Goryeo empress regal figure, Korean empress divine presence",
        "outfit": "Goryeo dynasty empress ceremonial robe, lotus pattern embroidery, empress crown",
        "material": "Goryeo silk empress robe, lotus embroidery, Goryeo dynasty accessories",
        "environment": "Goryeo dynasty palace, celadon pottery atmosphere, Korean dynasty",
        "lighting": "warm Goryeo palace light, lotus embroidery atmosphere, Goryeo empress glow",
        "style": "Goryeo empress editorial, Korean dynasty glamour photography",
        "quality": "shot on Hasselblad H6D, Goryeo jade grade, portrait 2:3 vertical"
    },
    "gyeongbokgung_night": {
        "tag": "Gyeongbokgung Night",
        "subject": "a majestic Gyeongbokgung palace night glamour female model",
        "body": "luxury glamour model, Korean palace night figure, Gyeongbokgung night goddess presence",
        "outfit": "elegant Korean palace night glamour costume, modern hanbok fusion, palace night styling",
        "material": "silk modern hanbok fusion dress, Korean palace night accessories",
        "environment": "Gyeongbokgung palace at night, lantern reflection, Korean royal night atmosphere",
        "lighting": "Gyeongbokgung palace lantern night light, royal Korean night atmosphere, palace night glow",
        "style": "Gyeongbokgung night editorial, Korean royal night glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic Korean night grade, portrait 2:3 vertical"
    },
    "haenyeo_goddess": {
        "tag": "Haenyeo Goddess",
        "subject": "a powerful Jeju haenyeo diving goddess female model",
        "body": "athletic fitness model, powerful Jeju diver figure, haenyeo sea goddess presence",
        "outfit": "traditional haenyeo diving suit, Jeju sea goddess styling, diving accessories",
        "material": "haenyeo wetsuit, Jeju traditional diving accessories, sea goddess elements",
        "environment": "Jeju volcanic coast, haenyeo diving realm, Korean sea goddess atmosphere",
        "lighting": "Jeju coastal golden light, sea goddess atmosphere, haenyeo powerful glow",
        "style": "haenyeo goddess editorial, Jeju sea glamour photography",
        "quality": "shot on Canon EOS R5, Jeju coastal grade, portrait 2:3 vertical"
    },
    "haetae_guardian": {
        "tag": "Haetae Guardian",
        "subject": "a powerful haetae guardian beast body art female model",
        "body": "athletic fitness model, guardian beast figure, haetae Korean guardian goddess presence",
        "outfit": "Korean haetae guardian beast scales and flame patterns painted directly on bare skin, NOT wearing fabric, guardian beast body art",
        "material": "haetae guardian beast scale flame paint on bare skin, Korean guardian body art",
        "environment": "Korean palace gate, haetae guardian realm, Korean guardian atmosphere",
        "lighting": "dramatic palace gate light, guardian beast atmosphere, haetae Korean glow",
        "style": "haetae guardian body art editorial, Korean guardian beast glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic guardian grade, portrait 2:3 vertical"
    },
    "hallyu_goddess": {
        "tag": "Hallyu Goddess",
        "subject": "a global Hallyu Korean wave goddess female model",
        "body": "slim elegance model, global Korean wave figure, Hallyu goddess international presence",
        "outfit": "Hallyu Korean wave glamour, modern Korean luxury fashion, global K-culture styling",
        "material": "modern Korean luxury fabric, Hallyu wave accessories, global K-culture elements",
        "environment": "Seoul luxury rooftop, Han River night, Korean wave global atmosphere",
        "lighting": "Seoul night skyline light, global Hallyu atmosphere, Korean wave goddess glow",
        "style": "Hallyu goddess editorial, global Korean wave glamour photography",
        "quality": "shot on Phase One XF IQ4, Seoul night grade, portrait 2:3 vertical"
    },
    "hyeonmu_turtle": {
        "tag": "Hyeonmu Turtle",
        "subject": "a mysterious Hyeonmu turtle snake goddess female model",
        "body": "slim elegance model, dark northern guardian figure, Hyeonmu divine presence",
        "outfit": "Korean Hyeonmu turtle shell and snake pattern painted directly on bare skin, NOT wearing fabric, northern guardian body art",
        "material": "Hyeonmu dark turtle shell snake paint on bare skin, Korean northern guardian body art",
        "environment": "Korean northern heavenly realm, dark water turtle atmosphere",
        "lighting": "dark divine northern light, Hyeonmu mysterious atmosphere, Korean dark guardian glow",
        "style": "Hyeonmu guardian body art editorial, Korean dark divine glamour photography",
        "quality": "shot on Hasselblad H6D, dark divine grade, portrait 2:3 vertical"
    },
    "joseon_consort": {
        "tag": "Joseon Consort",
        "subject": "a elegant Joseon royal consort female model",
        "body": "slim elegance model, Joseon consort graceful figure, royal consort sensual presence",
        "outfit": "Joseon dynasty royal consort ceremonial dress, elegant court costume, royal accessories",
        "material": "silk court dress, elegant Korean embroidery, royal consort jewelry",
        "environment": "Joseon palace inner court, royal consort atmosphere, Korean dynasty",
        "lighting": "soft palace inner court light, elegant consort atmosphere, royal Korean glow",
        "style": "Joseon consort editorial, Korean dynasty glamour photography",
        "quality": "shot on Hasselblad H6D, soft royal Korean grade, portrait 2:3 vertical"
    },
    "joseon_painter": {
        "tag": "Joseon Painter",
        "subject": "a Shin Yunbok style Korean beauty painting female model",
        "body": "slim elegance model, Joseon classical beauty figure, Hyewon beauty painting presence",
        "outfit": "Joseon dynasty beauty in Shin Yunbok Hyewon painting style, classical Korean beauty dress",
        "material": "Joseon classical beauty dress, Korean traditional cosmetics, beauty painting style",
        "environment": "Joseon dynasty courtyard, beauty painting atmosphere, classical Korean setting",
        "lighting": "soft Joseon courtyard light, classical beauty atmosphere, Hyewon painting glow",
        "style": "Joseon Hyewon painter editorial, classical Korean beauty photography",
        "quality": "shot on Hasselblad H6D, soft classical Korean grade, portrait 2:3 vertical"
    },
    "joseon_queen": {
        "tag": "Joseon Queen",
        "subject": "a majestic Joseon dynasty queen female model",
        "body": "luxury glamour model, Joseon queen regal figure, Korean queen divine presence",
        "outfit": "Joseon dynasty queen daeraeryebok ceremonial robe, dragon phoenix embroidery, royal crown, full royal regalia",
        "material": "crimson silk queen robe, dragon phoenix gold embroidery, royal Korean jewelry",
        "environment": "Gyeongbokgung palace throne room, Joseon dynasty royal atmosphere",
        "lighting": "warm royal palace light, dragon phoenix ceremony atmosphere, Joseon queen divine glow",
        "style": "Joseon queen editorial, Korean royal glamour photography",
        "quality": "shot on Phase One XF IQ4, royal Korean grade, portrait 2:3 vertical"
    },
    "kbeauty_glass_skin": {
        "tag": "Kbeauty Glass Skin",
        "subject": "a luminous K-beauty glass skin goddess female model",
        "body": "slim elegance model, luminous translucent skin figure, K-beauty glass skin goddess presence",
        "outfit": "K-beauty glass skin editorial look, minimal clean beauty styling, luminous skin focus",
        "material": "minimal clean beauty outfit, glass skin luminous accessories",
        "environment": "clean minimal white studio, K-beauty atmosphere, luminous skin realm",
        "lighting": "clean ring light, K-beauty glass skin luminous atmosphere, translucent skin glow",
        "style": "K-beauty glass skin editorial, luminous skin glamour photography",
        "quality": "shot on Hasselblad H6D, maximum luminous skin grade, portrait 2:3 vertical"
    },
    "kdrama_chaebol_heir": {
        "tag": "Kdrama Chaebol Heir",
        "subject": "a ultra-luxury K-drama chaebol heiress female model",
        "body": "slim elegance model, ultra-luxury heiress figure, Korean chaebol goddess presence",
        "outfit": "K-drama chaebol heiress ultra-luxury outfit, designer Korean fashion, chaebol heir accessories",
        "material": "ultra-luxury designer fabric, chaebol heir jewelry, Korean luxury accessories",
        "environment": "Korean luxury chaebol mansion, Han River penthouse, ultra-luxury atmosphere",
        "lighting": "ultra-luxury penthouse light, chaebol heir luxury atmosphere, Korean luxury glow",
        "style": "K-drama chaebol heiress editorial, Korean luxury glamour photography",
        "quality": "shot on Phase One XF IQ4, ultra-luxury Korean grade, portrait 2:3 vertical"
    },
    "kdrama_villain_queen": {
        "tag": "Kdrama Villain Queen",
        "subject": "a commanding K-drama villain queen female model",
        "body": "luxury glamour model, commanding villain figure, K-drama villain queen dark presence",
        "outfit": "K-drama villain queen power outfit, dark luxury Korean fashion, commanding villain accessories",
        "material": "dark luxury Korean fabric, villain queen accessories, commanding power elements",
        "environment": "dark Korean drama villain mansion, power atmosphere",
        "lighting": "dramatic dark power light, villain queen atmosphere, commanding Korean drama glow",
        "style": "K-drama villain queen editorial, dark power glamour photography",
        "quality": "shot on Leica SL2, dark power Korean grade, portrait 2:3 vertical"
    },
    "korean_bamboo_body": {
        "tag": "Korean Bamboo Body",
        "subject": "a noble Korean bamboo body art female model",
        "body": "slim elegance model, upright noble figure, Korean bamboo goddess noble presence",
        "outfit": "Korean bamboo grove pattern painted directly on bare skin, NOT wearing fabric, noble scholar bamboo body art",
        "material": "Korean bamboo green noble paint on bare skin, scholar integrity body art",
        "environment": "Korean bamboo forest, noble scholar atmosphere, Korean bamboo realm",
        "lighting": "green bamboo filtered light, noble scholar atmosphere, Korean bamboo glow",
        "style": "Korean bamboo body art editorial, Korean noble scholar glamour photography",
        "quality": "shot on Hasselblad H6D, green bamboo grade, portrait 2:3 vertical"
    },
    "korean_dragon_body": {
        "tag": "Korean Dragon Body",
        "subject": "a divine Korean dragon body art female model",
        "body": "power fitness model, Korean dragon goddess figure, imugi divine presence",
        "outfit": "Korean dragon imugi scale and cloud patterns painted directly on bare skin, NOT wearing fabric, Korean divine dragon body art",
        "material": "Korean dragon blue gold scale cloud paint on bare skin, Korean divine body art",
        "environment": "Korean mountain cloud peak, Korean dragon realm, divine Korean atmosphere",
        "lighting": "dramatic Korean mountain cloud light, divine dragon atmosphere, Korean dragon glow",
        "style": "Korean dragon body art editorial, Korean divine glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic divine Korean grade, portrait 2:3 vertical"
    },
    "korean_lotus_body": {
        "tag": "Korean Lotus Body",
        "subject": "a serene Korean lotus body art female model",
        "body": "slim elegance model, Buddhist lotus figure, Korean lotus goddess serene presence",
        "outfit": "Korean Buddhist lotus flower patterns painted directly on bare skin, NOT wearing fabric, lotus enlightenment body art",
        "material": "Korean lotus pink gold paint on bare skin, Buddhist enlightenment body art",
        "environment": "Korean Buddhist temple pond, lotus bloom, serene Korean atmosphere",
        "lighting": "soft Buddhist temple light, lotus bloom atmosphere, Korean serene glow",
        "style": "Korean lotus body art editorial, Buddhist glamour photography",
        "quality": "shot on Hasselblad H6D, soft lotus grade, portrait 2:3 vertical"
    },
    "korean_plum_body": {
        "tag": "Korean Plum Body",
        "subject": "a elegant Korean plum blossom body art female model",
        "body": "slim elegance model, plum blossom scholar figure, Korean plum goddess elegant presence",
        "outfit": "Korean plum blossom branch patterns painted directly on bare skin, NOT wearing fabric, scholar flower body art",
        "material": "Korean plum blossom pink white branch paint on bare skin, scholar flower body art",
        "environment": "Korean winter garden, plum blossom season, scholar flower atmosphere",
        "lighting": "cold winter Korean light, plum blossom delicate atmosphere, Korean scholar flower glow",
        "style": "Korean plum body art editorial, Korean scholar flower glamour photography",
        "quality": "shot on Leica SL2, cool delicate grade, portrait 2:3 vertical"
    },
    "korean_shaman_fire": {
        "tag": "Korean Shaman Fire",
        "subject": "a ecstatic Korean shaman fire ritual female model",
        "body": "power fitness model, fire ritual shaman figure, Korean shaman fire goddess presence",
        "outfit": "Korean shaman fire ritual costume, burning spirit flags, fire ceremony accessories",
        "material": "shaman fire costume, burning ritual flags, fire ceremony elements",
        "environment": "Korean open air shaman fire ceremony, burning spirit atmosphere",
        "lighting": "dramatic fire ritual light, burning spirit atmosphere, Korean shaman fire glow",
        "style": "Korean shaman fire editorial, ritual fire glamour photography",
        "quality": "shot on Sony A7R V, dramatic fire grade, portrait 2:3 vertical"
    },
    "korean_tiger_body": {
        "tag": "Korean Tiger Body",
        "subject": "a sacred Korean folk tiger body art female model",
        "body": "slim elegance model, Korean tiger guardian figure, minhwa tiger goddess presence",
        "outfit": "Korean minhwa folk tiger patterns painted directly on bare skin, NOT wearing fabric, sacred guardian tiger body art",
        "material": "Korean folk tiger orange black white paint on bare skin, minhwa guardian body art",
        "environment": "Korean mountain, sacred tiger guardian realm, minhwa folk atmosphere",
        "lighting": "dramatic mountain light, Korean tiger guardian atmosphere, sacred folk glow",
        "style": "Korean tiger body art editorial, minhwa folk glamour photography",
        "quality": "shot on Phase One XF IQ4, warm Korean tiger grade, portrait 2:3 vertical"
    },
    "korean_tiger_spirit": {
        "tag": "Korean Tiger Spirit",
        "subject": "a sacred Korean mountain tiger spirit female model",
        "body": "power fitness model, Korean mountain guardian tiger figure, sacred Sanshin tiger goddess presence",
        "outfit": "Korean sacred Sanshin mountain tiger spirit costume, tiger fur elements, mountain guardian styling",
        "material": "Korean mountain tiger spirit costume, sacred tiger elements, Sanshin guardian accessories",
        "environment": "Korean sacred mountain, Sanshin tiger spirit realm, mountain guardian atmosphere",
        "lighting": "dramatic sacred mountain light, tiger spirit atmosphere, Korean mountain guardian glow",
        "style": "Korean tiger spirit editorial, sacred mountain glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic sacred Korean grade, portrait 2:3 vertical"
    },
    "kpop_girl_crush": {
        "tag": "Kpop Girl Crush",
        "subject": "a powerful K-POP girl crush female model",
        "body": "athletic fitness model, K-POP powerful girl crush figure, idol girl crush presence",
        "outfit": "K-POP girl crush power stage costume, edgy dark idol outfit, girl crush accessories",
        "material": "edgy K-POP stage fabric, girl crush dark accessories, powerful idol styling",
        "environment": "K-POP concert stage, dramatic lighting, girl crush atmosphere",
        "lighting": "dramatic K-POP stage light, girl crush power atmosphere, idol stage glow",
        "style": "K-POP girl crush editorial, idol stage glamour photography",
        "quality": "shot on Sony A7R V, dramatic stage grade, portrait 2:3 vertical"
    },
    "minhwa_body": {
        "tag": "Minhwa Body",
        "subject": "a vibrant Korean minhwa folk painting body art female model",
        "body": "slim elegance model, folk art goddess figure, Korean minhwa vibrant presence",
        "outfit": "Korean minhwa folk painting tiger lotus magpie patterns painted directly on bare skin, NOT wearing fabric, Korean folk art body art",
        "material": "minhwa vibrant folk painting colors on bare skin, Korean folk tiger lotus magpie body art",
        "environment": "Korean traditional folk painting atmosphere, minhwa colorful realm",
        "lighting": "warm folk painting light, minhwa vibrant atmosphere, Korean folk art glow",
        "style": "minhwa body art editorial, Korean folk painting glamour photography",
        "quality": "shot on Canon EOS R5, vibrant folk art grade, portrait 2:3 vertical"
    },
    "mudang_shaman": {
        "tag": "Mudang Shaman",
        "subject": "a powerful Korean mudang shaman female model",
        "body": "power fitness model, shaman spirit-possessed figure, mudang goddess divine possession presence",
        "outfit": "Korean mudang shaman ceremony costume, colorful shaman flags, spirit possession accessories",
        "material": "colorful mudang ceremony robe, shaman spirit flags, Korean ritual accessories",
        "environment": "Korean mudang gut ceremony, spirit possession ritual, shaman divine atmosphere",
        "lighting": "dramatic shaman ceremony light, spirit possession atmosphere, mudang divine glow",
        "style": "mudang shaman editorial, Korean spirit glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic shaman grade, portrait 2:3 vertical"
    },
    "mugunghwa_body": {
        "tag": "Mugunghwa Body",
        "subject": "a national flower mugunghwa body art female model",
        "body": "slim elegance model, Korean national flower figure, mugunghwa hibiscus goddess presence",
        "outfit": "Korean mugunghwa Rose of Sharon hibiscus patterns painted directly on bare skin, NOT wearing fabric, national flower body art",
        "material": "mugunghwa pink purple hibiscus paint on bare skin, Korean national flower body art",
        "environment": "Korean garden, mugunghwa bloom season, national flower atmosphere",
        "lighting": "soft Korean garden light, mugunghwa bloom atmosphere, national flower glow",
        "style": "mugunghwa body art editorial, Korean national flower glamour photography",
        "quality": "shot on Hasselblad H6D, soft pink purple grade, portrait 2:3 vertical"
    },
    "najeon_abalone": {
        "tag": "Najeon Abalone",
        "subject": "a shimmering abalone shell Korean body art female model",
        "body": "slim elegance model, abalone iridescent figure, Korean abalone goddess presence",
        "outfit": "Korean abalone shell swirling iridescent patterns painted directly on bare skin, NOT wearing fabric, abalone shimmer body art",
        "material": "abalone green purple blue iridescent swirl paint on bare skin, Korean shell body art",
        "environment": "Korean coastal setting, abalone shell atmosphere",
        "lighting": "abalone iridescent coastal light, shell shimmer atmosphere, Korean coastal glow",
        "style": "abalone Korean body art editorial, coastal shimmer glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum abalone iridescent grade, portrait 2:3 vertical"
    },
    "najeonchilgi_body": {
        "tag": "Najeonchilgi Body",
        "subject": "a iridescent mother-of-pearl Korean lacquerware body art female model",
        "body": "slim elegance model, iridescent lustrous figure, najeonchilgi goddess rainbow presence",
        "outfit": "Korean najeonchilgi mother-of-pearl lacquerware iridescent patterns painted directly on bare skin, NOT wearing fabric, rainbow nacre body art",
        "material": "najeonchilgi mother-of-pearl iridescent rainbow paint on bare skin, Korean lacquerware body art",
        "environment": "dark lacquerware studio, Korean craft atmosphere, mother-of-pearl shimmer",
        "lighting": "iridescent mother-of-pearl light, rainbow nacre atmosphere, najeonchilgi shimmer glow",
        "style": "najeonchilgi body art editorial, Korean lacquerware glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum iridescent nacre grade, portrait 2:3 vertical"
    },
    "phoenix_jujakk": {
        "tag": "Phoenix Jujakk",
        "subject": "a divine Jujakk southern phoenix goddess female model",
        "body": "slim elegance model, divine southern bird figure, Jujakk phoenix goddess presence",
        "outfit": "Korean Jujakk southern divine phoenix fire feather patterns painted directly on bare skin, NOT wearing fabric, divine phoenix body art",
        "material": "Jujakk southern phoenix red fire feather paint on bare skin, Korean divine body art",
        "environment": "Korean southern heavenly realm, divine phoenix fire atmosphere",
        "lighting": "divine southern fire light, Jujakk phoenix atmosphere, Korean divine bird glow",
        "style": "Jujakk phoenix body art editorial, Korean divine bird glamour photography",
        "quality": "shot on Sony A7R V, divine fire grade, portrait 2:3 vertical"
    },
    "pojagi_body": {
        "tag": "Pojagi Body",
        "subject": "a colorful pojagi patchwork body art female model",
        "body": "slim elegance model, patchwork mosaic figure, pojagi goddess colorful presence",
        "outfit": "Korean pojagi silk patchwork geometric patterns painted directly on bare skin, NOT wearing fabric, patchwork mosaic body art",
        "material": "pojagi silk patchwork multicolor geometric paint on bare skin, Korean textile body art",
        "environment": "Korean traditional room, pojagi window light, patchwork color atmosphere",
        "lighting": "pojagi silk window light through patchwork colors, mosaic atmosphere, Korean craft glow",
        "style": "pojagi body art editorial, Korean patchwork glamour photography",
        "quality": "shot on Hasselblad H6D, vibrant patchwork grade, portrait 2:3 vertical"
    },
    "silla_crown_body": {
        "tag": "Silla Crown Body",
        "subject": "a golden Silla gold crown body art female model",
        "body": "slim elegance model, ancient gold crown figure, Silla gold goddess divine presence",
        "outfit": "Silla kingdom gold crown tree branch patterns painted directly on bare skin, NOT wearing fabric, ancient Korean gold body art",
        "material": "Silla gold crown tree branch gold paint on bare skin, ancient Korean gold body art",
        "environment": "Silla ancient tomb, gold crown divine atmosphere, Korean ancient kingdom",
        "lighting": "golden ancient Silla light, gold crown divine atmosphere, ancient Korean goddess glow",
        "style": "Silla crown body art editorial, ancient Korean gold glamour photography",
        "quality": "shot on Phase One XF IQ4, ancient gold grade, portrait 2:3 vertical"
    },
    "silla_empress": {
        "tag": "Silla Empress",
        "subject": "a divine Silla dynasty empress female model",
        "body": "luxury glamour model, ancient Korean empress figure, Silla divine queen presence",
        "outfit": "Silla dynasty empress costume, gold crown accessories, ancient Korean royal regalia",
        "material": "Silla ancient silk, gold crown accessories, ancient Korean royal jewelry",
        "environment": "Silla ancient capital Gyeongju, gold tomb atmosphere, ancient Korean kingdom",
        "lighting": "golden ancient Silla light, divine empress atmosphere, ancient Korean kingdom glow",
        "style": "Silla empress editorial, ancient Korean dynasty glamour photography",
        "quality": "shot on Phase One XF IQ4, ancient gold Korean grade, portrait 2:3 vertical"
    },
    "silla_gold_crown": {
        "tag": "Silla Gold Crown",
        "subject": "a divine Silla gold crown goddess female model",
        "body": "slim elegance model, gold crown divine figure, Silla gold goddess presence",
        "outfit": "Silla kingdom spectacular gold crown full regalia, ancient Korean gold divine costume",
        "material": "Silla gold crown full regalia, ancient Korean gold accessories, divine gold elements",
        "environment": "Silla Cheonmachong gold tomb, ancient gold divine atmosphere",
        "lighting": "golden ancient Silla divine light, gold crown spectacular atmosphere, ancient goddess glow",
        "style": "Silla gold crown editorial, ancient Korean divine glamour photography",
        "quality": "shot on Phase One XF IQ4, spectacular gold grade, portrait 2:3 vertical"
    },
    "taegeuk_body": {
        "tag": "Taegeuk Body",
        "subject": "a powerful taegeuk symbol body art female model",
        "body": "athletic fitness model, yin yang balance figure, taegeuk goddess cosmic presence",
        "outfit": "Korean taegeuk yin yang and trigram patterns painted directly on bare skin, NOT wearing fabric, cosmic balance body art",
        "material": "taegeuk red blue cosmic yin yang paint on bare skin, Korean cosmic symbol body art",
        "environment": "Korean mountain peak, cosmic balance atmosphere, taegeuk realm",
        "lighting": "cosmic balance light, red blue yin yang atmosphere, taegeuk goddess glow",
        "style": "taegeuk body art editorial, Korean cosmic glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic cosmic grade, portrait 2:3 vertical"
    }
}

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
print(f"총 프리셋: 655 → {655 + added}개")
