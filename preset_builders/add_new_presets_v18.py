"""
add_new_presets_v18.py
동물 바디페인팅 50개

🐆 대형 맹수 (6개): panther_black, cheetah_speed, lion_golden, cougar_tawny, snow_leopard, ocelot_wild
🐍 파충류 (7개): chameleon_skin, dragon_scales_red, komodo_dragon, gecko_pattern, crocodile_skin, boa_constrictor, king_cobra_hood
🦋 곤충 (7개): butterfly_monarch, butterfly_morpho, dragonfly_iridescent, scarab_beetle, praying_mantis, luna_moth, atlas_moth
🦅 조류 (9개): eagle_wings, flamingo_pink, owl_feather, parrot_tropical, hummingbird_iridescent, phoenix_rising, swan_white, macaw_scarlet, bird_of_paradise
🌊 해양 (9개): octopus_ink, koi_fish, jellyfish_glow, seahorse_fantasy, mantis_shrimp, anglerfish_deep, nudibranch_sea, lionfish_venomous, cuttlefish_chromo
🦌 포유류/야생 (7개): wolf_grey, zebra_stripes, giraffe_pattern, dalmatian_spots, arctic_fox, red_fox, hyena_spots
🦄 신화/판타지 (5개): koi_dragon, unicorn_opal, gryphon_feather, sphinx_cat, basilisk_scales

총 프리셋: 605 → 655개
"""

import json
from pathlib import Path

PRESETS_DIR = Path("presets")
PRESETS_DIR.mkdir(exist_ok=True)

new_presets = {
    "anglerfish_deep": {
        "tag": "Anglerfish Deep",
        "subject": "a abyssal anglerfish body art female model",
        "body": "slim elegance model, dark abyssal figure, anglerfish goddess deep sea presence",
        "outfit": "anglerfish bioluminescent lure and pattern painted directly on bare skin, NOT wearing fabric, abyssal predator body art",
        "material": "anglerfish dark body bioluminescent lure paint on bare skin, abyssal predator body art",
        "environment": "absolute deep ocean darkness, anglerfish realm, abyssal predator atmosphere",
        "lighting": "single bioluminescent lure glow, absolute darkness atmosphere, abyssal predator light",
        "style": "anglerfish deep body art editorial, abyssal predator glamour photography",
        "quality": "shot on Sony A7R V, maximum dark abyssal grade, portrait 2:3 vertical"
    },
    "arctic_fox": {
        "tag": "Arctic Fox",
        "subject": "a ethereal arctic fox body art female model",
        "body": "slim elegance model, pure white ethereal figure, arctic fox goddess winter presence",
        "outfit": "arctic fox pure white winter fur patterns painted directly on bare skin, NOT wearing fabric, winter white body art",
        "material": "arctic fox pure white winter fur paint on bare skin, winter ethereal body art",
        "environment": "arctic tundra snow, arctic fox winter realm, pure white atmosphere",
        "lighting": "soft arctic snow light, pure white winter atmosphere, arctic fox ethereal glow",
        "style": "arctic fox body art editorial, winter white glamour photography",
        "quality": "shot on Hasselblad H6D, pure white cold grade, portrait 2:3 vertical"
    },
    "atlas_moth": {
        "tag": "Atlas Moth",
        "subject": "a magnificent atlas moth body art female model",
        "body": "slim elegance model, large wingspan figure, atlas moth goddess presence",
        "outfit": "atlas moth complex burgundy brown eyespot patterns painted directly on bare skin, NOT wearing fabric, largest moth body art",
        "material": "atlas moth burgundy brown complex eyespot paint on bare skin, magnificent wing body art",
        "environment": "Southeast Asian forest, atlas moth realm, largest moth atmosphere",
        "lighting": "warm forest dusk light, atlas moth complex atmosphere, magnificent wing glow",
        "style": "atlas moth body art editorial, magnificent wing glamour photography",
        "quality": "shot on Phase One XF IQ4, warm burgundy grade, portrait 2:3 vertical"
    },
    "basilisk_scales": {
        "tag": "Basilisk Scales",
        "subject": "a deadly basilisk scales body art female model",
        "body": "slim elegance model, deadly gaze figure, basilisk goddess petrifying presence",
        "outfit": "basilisk emerald green deadly scale patterns painted directly on bare skin, NOT wearing fabric, king of serpents body art",
        "material": "basilisk emerald green scale paint on bare skin, deadly gaze pattern body art",
        "environment": "dark cave, basilisk realm, deadly emerald atmosphere",
        "lighting": "dramatic emerald cave light, basilisk deadly atmosphere, petrifying gaze glow",
        "style": "basilisk scales body art editorial, deadly serpent glamour photography",
        "quality": "shot on Sony A7R V, deep emerald grade, portrait 2:3 vertical"
    },
    "bird_of_paradise": {
        "tag": "Bird of Paradise",
        "subject": "a spectacular bird of paradise body art female model",
        "body": "slim elegance model, spectacular display figure, bird of paradise goddess presence",
        "outfit": "bird of paradise spectacular plume patterns painted directly on bare skin, NOT wearing fabric, mating display body art",
        "material": "bird of paradise iridescent plume paint on bare skin, spectacular display body art",
        "environment": "Papua New Guinea forest, bird of paradise display realm, spectacular atmosphere",
        "lighting": "spectacular display light, iridescent plume atmosphere, bird of paradise glow",
        "style": "bird of paradise body art editorial, spectacular display glamour photography",
        "quality": "shot on Phase One XF IQ4, spectacular iridescent grade, portrait 2:3 vertical"
    },
    "boa_constrictor": {
        "tag": "Boa Constrictor",
        "subject": "a hypnotic boa constrictor body art female model",
        "body": "slim elegance model, sinuous serpentine figure, boa goddess hypnotic presence",
        "outfit": "boa constrictor saddle pattern painted directly on bare skin, NOT wearing fabric, hypnotic brown black pattern body art",
        "material": "boa saddle pattern brown black paint on bare skin, hypnotic serpentine body art",
        "environment": "tropical rainforest canopy, boa territory, serpentine realm",
        "lighting": "dappled canopy light, hypnotic serpentine atmosphere, boa constrictor glow",
        "style": "boa constrictor body art editorial, hypnotic serpent glamour photography",
        "quality": "shot on Leica SL2, warm tropical grade, portrait 2:3 vertical"
    },
    "butterfly_monarch": {
        "tag": "Butterfly Monarch",
        "subject": "a magnificent monarch butterfly body art female model",
        "body": "slim elegance model, butterfly figure, monarch goddess presence",
        "outfit": "monarch butterfly orange black white patterns painted directly on bare skin, NOT wearing fabric, monarch wing body art",
        "material": "monarch butterfly orange black white paint on bare skin, wing pattern body art",
        "environment": "monarch butterfly migration, milkweed meadow, butterfly realm",
        "lighting": "warm golden butterfly migration light, monarch orange atmosphere, butterfly glow",
        "style": "monarch butterfly body art editorial, butterfly migration glamour photography",
        "quality": "shot on Hasselblad H6D, warm monarch orange grade, portrait 2:3 vertical"
    },
    "butterfly_morpho": {
        "tag": "Butterfly Morpho",
        "subject": "a iridescent morpho butterfly body art female model",
        "body": "slim elegance model, metallic blue figure, morpho goddess presence",
        "outfit": "morpho butterfly metallic electric blue patterns painted directly on bare skin, NOT wearing fabric, iridescent blue wing body art",
        "material": "morpho metallic electric blue iridescent paint on bare skin, structural color body art",
        "environment": "Amazon rainforest, morpho butterfly realm, iridescent blue atmosphere",
        "lighting": "iridescent blue light, structural color atmosphere, morpho electric glow",
        "style": "morpho butterfly body art editorial, iridescent blue glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum iridescent blue grade, portrait 2:3 vertical"
    },
    "chameleon_skin": {
        "tag": "Chameleon Skin",
        "subject": "a magical chameleon skin body art female model",
        "body": "slim elegance model, color-shifting figure, chameleon goddess presence",
        "outfit": "chameleon rainbow color-shifting patterns painted directly on bare skin, NOT wearing fabric, iridescent color gradient body art",
        "material": "chameleon iridescent rainbow paint on bare skin, color-shift gradient, magical body art",
        "environment": "lush rainforest, shifting light atmosphere, chameleon magical realm",
        "lighting": "rainbow spectrum light, color-shifting atmosphere, iridescent chameleon glow",
        "style": "chameleon skin body art editorial, color-shift glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum iridescent grade, portrait 2:3 vertical"
    },
    "cheetah_speed": {
        "tag": "Cheetah Speed",
        "subject": "a lightning cheetah body art female model",
        "body": "athletic fitness model, lean defined body, cheetah speed goddess presence",
        "outfit": "cheetah spots and speed lines painted directly on bare skin, NOT wearing fabric, golden yellow black spot body art",
        "material": "cheetah golden yellow paint with black spots on bare skin, speed line accents, cheetah body art",
        "environment": "African savanna golden grass, speed blur atmosphere, cheetah hunting ground",
        "lighting": "golden savanna light, speed motion atmosphere, cheetah golden glow",
        "style": "cheetah speed body art editorial, African savanna glamour photography",
        "quality": "shot on Sony A7R V, golden savanna grade, portrait 2:3 vertical"
    },
    "cougar_tawny": {
        "tag": "Cougar Tawny",
        "subject": "a sleek cougar tawny body art female model",
        "body": "athletic fitness model, mountain lion physique, cougar predator goddess presence",
        "outfit": "cougar tawny mountain lion patterns painted directly on bare skin, NOT wearing fabric, warm brown tawny body art",
        "material": "tawny warm brown cougar paint on bare skin, mountain lion texture, predator body art",
        "environment": "mountain rocky outcrop, cougar territory, wild mountain atmosphere",
        "lighting": "dramatic mountain light, tawny cougar atmosphere, wild predator glow",
        "style": "cougar tawny body art editorial, mountain predator glamour photography",
        "quality": "shot on Canon EOS R5, warm tawny mountain grade, portrait 2:3 vertical"
    },
    "crocodile_skin": {
        "tag": "Crocodile Skin",
        "subject": "a armored crocodile skin body art female model",
        "body": "athletic fitness model, ancient armored figure, crocodile goddess presence",
        "outfit": "crocodile armored scale patterns painted directly on bare skin, NOT wearing fabric, ancient reptile armor body art",
        "material": "dark green grey crocodile armor scale paint on bare skin, ancient reptile texture body art",
        "environment": "African river bank, ancient predator atmosphere, crocodile realm",
        "lighting": "dramatic river light, ancient armored atmosphere, crocodile primordial glow",
        "style": "crocodile skin body art editorial, armored reptile glamour photography",
        "quality": "shot on Phase One XF IQ4, dark river grade, portrait 2:3 vertical"
    },
    "cuttlefish_chromo": {
        "tag": "Cuttlefish Chromo",
        "subject": "a shape-shifting cuttlefish body art female model",
        "body": "slim elegance model, color-shifting figure, cuttlefish goddess chromatophore presence",
        "outfit": "cuttlefish chromatophore color-shifting patterns painted directly on bare skin, NOT wearing fabric, rapid color change body art",
        "material": "cuttlefish chromatophore rapid color-shift paint on bare skin, intelligent color body art",
        "environment": "coastal ocean, cuttlefish realm, color-shifting atmosphere",
        "lighting": "shifting color light, cuttlefish chromatophore atmosphere, intelligent color glow",
        "style": "cuttlefish chromo body art editorial, color-shifting glamour photography",
        "quality": "shot on Phase One XF IQ4, color-shift grade, portrait 2:3 vertical"
    },
    "dalmatian_spots": {
        "tag": "Dalmatian Spots",
        "subject": "a playful dalmatian spots body art female model",
        "body": "slim elegance model, playful spotted figure, dalmatian goddess playful presence",
        "outfit": "dalmatian black white spot patterns painted directly on bare skin, NOT wearing fabric, playful spot body art",
        "material": "dalmatian black spot on white paint on bare skin, playful spot body art",
        "environment": "clean white studio, dalmatian playful realm, spot pattern atmosphere",
        "lighting": "clean bright studio light, playful spot atmosphere, dalmatian fun glow",
        "style": "dalmatian spots body art editorial, playful spot glamour photography",
        "quality": "shot on Canon EOS R5, clean bright grade, portrait 2:3 vertical"
    },
    "dragon_scales_red": {
        "tag": "Dragon Scales Red",
        "subject": "a fierce red dragon scales body art female model",
        "body": "power fitness model, dragon goddess powerful curves, crimson dragon presence",
        "outfit": "crimson red dragon scales painted directly on bare skin, NOT wearing fabric, fire dragon body art covering full body",
        "material": "deep crimson red dragon scale paint on bare skin, fire dragon texture, mythical body art",
        "environment": "dragon lair, volcanic fire atmosphere, dragon realm",
        "lighting": "volcanic fire glow, crimson red dragon atmosphere, fire goddess light",
        "style": "red dragon scales body art editorial, fire dragon glamour photography",
        "quality": "shot on Sony A7R V, deep crimson fire grade, portrait 2:3 vertical"
    },
    "dragonfly_iridescent": {
        "tag": "Dragonfly Iridescent",
        "subject": "a shimmering dragonfly body art female model",
        "body": "slim elegance model, delicate iridescent figure, dragonfly goddess presence",
        "outfit": "dragonfly iridescent wing patterns painted directly on bare skin, NOT wearing fabric, gossamer wing body art",
        "material": "dragonfly iridescent rainbow wing paint on bare skin, gossamer transparent wing body art",
        "environment": "still pond surface, dragonfly realm, iridescent wing atmosphere",
        "lighting": "pond reflection light, iridescent wing shimmer, dragonfly glow",
        "style": "dragonfly iridescent body art editorial, gossamer wing glamour photography",
        "quality": "shot on Hasselblad H6D, iridescent shimmer grade, portrait 2:3 vertical"
    },
    "eagle_wings": {
        "tag": "Eagle Wings",
        "subject": "a majestic eagle wings body art female model",
        "body": "athletic fitness model, powerful wingspan figure, eagle goddess sovereign presence",
        "outfit": "bald eagle wing spread patterns painted directly on bare skin, NOT wearing fabric, massive wing spread full back body art",
        "material": "eagle brown white wing pattern paint on bare skin, full wingspan body art",
        "environment": "mountain peak, eagle realm, sovereign sky atmosphere",
        "lighting": "dramatic mountain peak light, eagle sovereign atmosphere, wing spread glow",
        "style": "eagle wings body art editorial, sovereign sky glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic mountain grade, portrait 2:3 vertical"
    },
    "flamingo_pink": {
        "tag": "Flamingo Pink",
        "subject": "a elegant flamingo pink body art female model",
        "body": "slim elegance model, long-legged flamingo figure, flamingo goddess elegant presence",
        "outfit": "flamingo pink feather patterns painted directly on bare skin, NOT wearing fabric, elegant pink flamingo body art",
        "material": "flamingo hot pink feather paint on bare skin, elegant bird body art",
        "environment": "pink salt lake, flamingo colony, elegant bird realm",
        "lighting": "pink salt lake reflection light, flamingo elegant atmosphere, pink goddess glow",
        "style": "flamingo pink body art editorial, elegant bird glamour photography",
        "quality": "shot on Hasselblad H6D, hot pink flamingo grade, portrait 2:3 vertical"
    },
    "gecko_pattern": {
        "tag": "Gecko Pattern",
        "subject": "a delicate gecko pattern body art female model",
        "body": "slim elegance model, delicate adhesive figure, gecko goddess presence",
        "outfit": "gecko adhesive toe pad and scale patterns painted directly on bare skin, NOT wearing fabric, tropical gecko body art",
        "material": "gecko bright green tropical scale paint on bare skin, adhesive pad pattern, tropical body art",
        "environment": "tropical leaf surface, gecko night atmosphere, tropical creature realm",
        "lighting": "tropical night light, gecko adhesive atmosphere, tropical creature glow",
        "style": "gecko pattern body art editorial, tropical creature glamour photography",
        "quality": "shot on Hasselblad H6D, bright tropical grade, portrait 2:3 vertical"
    },
    "giraffe_pattern": {
        "tag": "Giraffe Pattern",
        "subject": "a elegant giraffe pattern body art female model",
        "body": "slim elegance model, tall graceful figure, giraffe goddess elegant presence",
        "outfit": "giraffe reticulated patch patterns painted directly on bare skin, NOT wearing fabric, savanna patchwork body art",
        "material": "giraffe warm brown tan reticulated paint on bare skin, savanna patchwork body art",
        "environment": "African savanna acacia tree, giraffe realm, warm patch atmosphere",
        "lighting": "warm golden savanna light, giraffe patch atmosphere, elegant tall glow",
        "style": "giraffe pattern body art editorial, elegant savanna glamour photography",
        "quality": "shot on Hasselblad H6D, warm savanna grade, portrait 2:3 vertical"
    },
    "gryphon_feather": {
        "tag": "Gryphon Feather",
        "subject": "a powerful gryphon body art female model",
        "body": "athletic fitness model, combined eagle-lion figure, gryphon goddess guardian presence",
        "outfit": "gryphon eagle feather and lion scale patterns painted directly on bare skin, NOT wearing fabric, guardian beast body art",
        "material": "gryphon golden eagle feather lion scale paint on bare skin, guardian beast body art",
        "environment": "medieval castle, gryphon guardian realm, heraldic atmosphere",
        "lighting": "dramatic heraldic light, guardian beast atmosphere, gryphon golden glow",
        "style": "gryphon feather body art editorial, guardian beast glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic heraldic grade, portrait 2:3 vertical"
    },
    "hummingbird_iridescent": {
        "tag": "Hummingbird Iridescent",
        "subject": "a jewel hummingbird iridescent body art female model",
        "body": "slim elegance model, jewel-like delicate figure, hummingbird goddess iridescent presence",
        "outfit": "hummingbird jewel iridescent green ruby throat patterns painted directly on bare skin, NOT wearing fabric, living jewel body art",
        "material": "hummingbird iridescent green ruby throat paint on bare skin, living jewel body art",
        "environment": "tropical flower garden, hummingbird realm, jewel bird atmosphere",
        "lighting": "iridescent jewel light, hummingbird shimmer atmosphere, living jewel glow",
        "style": "hummingbird iridescent body art editorial, living jewel glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum jewel iridescent grade, portrait 2:3 vertical"
    },
    "hyena_spots": {
        "tag": "Hyena Spots",
        "subject": "a powerful hyena spots body art female model",
        "body": "athletic fitness model, powerful scavenger figure, hyena goddess complex presence",
        "outfit": "hyena complex spot and stripe patterns painted directly on bare skin, NOT wearing fabric, complex predator body art",
        "material": "hyena tawny brown complex spot paint on bare skin, predator body art",
        "environment": "African savanna twilight, hyena clan realm, complex predator atmosphere",
        "lighting": "dramatic twilight savanna light, hyena complex atmosphere, predator clan glow",
        "style": "hyena spots body art editorial, complex predator glamour photography",
        "quality": "shot on Sony A7R V, warm twilight grade, portrait 2:3 vertical"
    },
    "jellyfish_glow": {
        "tag": "Jellyfish Glow",
        "subject": "a ethereal jellyfish glow body art female model",
        "body": "slim elegance model, translucent flowing figure, jellyfish goddess ethereal presence",
        "outfit": "jellyfish bioluminescent glow patterns painted directly on bare skin, NOT wearing fabric, translucent tentacle body art",
        "material": "jellyfish bioluminescent blue purple paint on bare skin, translucent glow body art",
        "environment": "dark deep ocean, jellyfish bioluminescent realm, ethereal glow atmosphere",
        "lighting": "pure bioluminescent jellyfish glow, dark ocean atmosphere, ethereal translucent light",
        "style": "jellyfish glow body art editorial, bioluminescent ethereal glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum bioluminescent grade, portrait 2:3 vertical"
    },
    "king_cobra_hood": {
        "tag": "King Cobra Hood",
        "subject": "a deadly king cobra body art female model",
        "body": "slim elegance model, regal serpent queen figure, king cobra goddess presence",
        "outfit": "king cobra hood spread pattern painted directly on bare skin, NOT wearing fabric, regal serpent body art with hood detail",
        "material": "king cobra golden brown hood pattern paint on bare skin, regal serpent body art",
        "environment": "Indian jungle, cobra charmer atmosphere, serpent queen realm",
        "lighting": "dramatic cobra hood light, regal serpent atmosphere, king cobra goddess glow",
        "style": "king cobra body art editorial, regal serpent glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic warm grade, portrait 2:3 vertical"
    },
    "koi_dragon": {
        "tag": "Koi Dragon",
        "subject": "a transforming koi dragon body art female model",
        "body": "slim elegance model, transforming fish-to-dragon figure, koi dragon goddess transcendence presence",
        "outfit": "koi fish transforming into dragon patterns painted directly on bare skin, NOT wearing fabric, transcendence transformation body art",
        "material": "koi fish scales transforming into dragon scales paint on bare skin, Japanese transformation body art",
        "environment": "Dragon Gate waterfall, koi-to-dragon transformation realm, Japanese mythology",
        "lighting": "dramatic waterfall light, transformation atmosphere, koi dragon transcendence glow",
        "style": "koi dragon body art editorial, Japanese mythology glamour photography",
        "quality": "shot on Phase One XF IQ4, dramatic transformation grade, portrait 2:3 vertical"
    },
    "koi_fish": {
        "tag": "Koi Fish",
        "subject": "a serene koi fish body art female model",
        "body": "slim elegance model, flowing koi figure, koi goddess Japanese beauty presence",
        "outfit": "Japanese koi fish flowing patterns painted directly on bare skin, NOT wearing fabric, Ukiyo-e koi body art",
        "material": "koi fish red orange white black paint on bare skin, Japanese Ukiyo-e style body art",
        "environment": "Japanese koi pond, cherry blossom backdrop, serene Japanese atmosphere",
        "lighting": "soft Japanese garden light, koi reflection atmosphere, serene koi glow",
        "style": "koi fish body art editorial, Japanese Ukiyo-e glamour photography",
        "quality": "shot on Hasselblad H6D, soft Japanese grade, portrait 2:3 vertical"
    },
    "komodo_dragon": {
        "tag": "Komodo Dragon",
        "subject": "a primal komodo dragon body art female model",
        "body": "athletic fitness model, ancient reptile power figure, komodo dragon goddess presence",
        "outfit": "komodo dragon grey green textured scales painted directly on bare skin, NOT wearing fabric, ancient reptile body art",
        "material": "grey green komodo scale texture paint on bare skin, ancient reptile body art",
        "environment": "Komodo island volcanic landscape, ancient reptile atmosphere",
        "lighting": "harsh tropical sun, ancient reptile atmosphere, komodo primordial glow",
        "style": "komodo dragon body art editorial, ancient reptile glamour photography",
        "quality": "shot on Canon EOS R5, warm volcanic grade, portrait 2:3 vertical"
    },
    "lion_golden": {
        "tag": "Lion Golden",
        "subject": "a majestic lion body art female model",
        "body": "luxury glamour model, powerful curves, lion queen goddess presence",
        "outfit": "golden lion mane patterns and fur texture painted directly on bare skin, NOT wearing fabric, lion goddess body art",
        "material": "golden lion fur paint on bare skin, mane pattern, savanna gold body art",
        "environment": "African sunset savanna, Pride Rock backdrop, lion queen realm",
        "lighting": "golden African sunset, lion golden atmosphere, pride goddess glow",
        "style": "lion golden body art editorial, African queen glamour photography",
        "quality": "shot on Phase One XF IQ4, warm golden African grade, portrait 2:3 vertical"
    },
    "lionfish_venomous": {
        "tag": "Lionfish Venomous",
        "subject": "a dangerous lionfish body art female model",
        "body": "slim elegance model, dangerous beautiful figure, lionfish goddess venomous presence",
        "outfit": "lionfish striped venomous spine patterns painted directly on bare skin, NOT wearing fabric, dangerous beauty body art",
        "material": "lionfish red white stripe venomous spine paint on bare skin, dangerous beauty body art",
        "environment": "coral reef, lionfish territory, dangerous beauty atmosphere",
        "lighting": "dramatic coral reef light, venomous beauty atmosphere, lionfish dangerous glow",
        "style": "lionfish venomous body art editorial, dangerous beauty glamour photography",
        "quality": "shot on Hasselblad H6D, dramatic coral grade, portrait 2:3 vertical"
    },
    "luna_moth": {
        "tag": "Lunar Moth",
        "subject": "a ethereal luna moth body art female model",
        "body": "slim elegance model, pale ethereal figure, luna moth goddess presence",
        "outfit": "luna moth pale green eyespot wing patterns painted directly on bare skin, NOT wearing fabric, ethereal night moth body art",
        "material": "luna moth pale green eyespot paint on bare skin, ethereal night wing body art",
        "environment": "moonlit forest, luna moth night realm, ethereal moth atmosphere",
        "lighting": "soft moonlight, ethereal pale green moth atmosphere, luna moth glow",
        "style": "luna moth body art editorial, ethereal night glamour photography",
        "quality": "shot on Hasselblad H6D, soft pale moonlight grade, portrait 2:3 vertical"
    },
    "macaw_scarlet": {
        "tag": "Macaw Scarlet",
        "subject": "a vivid scarlet macaw body art female model",
        "body": "slim elegance model, vivid tropical figure, macaw goddess explosive color presence",
        "outfit": "scarlet macaw vivid red yellow blue patterns painted directly on bare skin, NOT wearing fabric, explosive tropical bird body art",
        "material": "scarlet macaw red yellow blue vivid paint on bare skin, explosive tropical body art",
        "environment": "Amazon rainforest canopy, scarlet macaw realm, explosive color atmosphere",
        "lighting": "bright Amazon light, explosive macaw color atmosphere, scarlet tropical glow",
        "style": "scarlet macaw body art editorial, explosive tropical glamour photography",
        "quality": "shot on Canon EOS R5, maximum scarlet grade, portrait 2:3 vertical"
    },
    "mantis_shrimp": {
        "tag": "Mantis Shrimp",
        "subject": "a spectacular mantis shrimp body art female model",
        "body": "slim elegance model, powerful compact figure, mantis shrimp goddess spectacular presence",
        "outfit": "mantis shrimp spectacular rainbow patterns painted directly on bare skin, NOT wearing fabric, most colorful creature body art",
        "material": "mantis shrimp rainbow spectrum paint on bare skin, maximum color body art",
        "environment": "tropical reef, mantis shrimp realm, spectacular color atmosphere",
        "lighting": "tropical reef rainbow light, mantis shrimp spectacular atmosphere, rainbow creature glow",
        "style": "mantis shrimp body art editorial, spectacular rainbow glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum rainbow grade, portrait 2:3 vertical"
    },
    "nudibranch_sea": {
        "tag": "Nudibranch Sea",
        "subject": "a spectacular nudibranch sea body art female model",
        "body": "slim elegance model, toxic beautiful figure, nudibranch goddess warning color presence",
        "outfit": "nudibranch sea slug spectacular warning color patterns painted directly on bare skin, NOT wearing fabric, most colorful sea creature body art",
        "material": "nudibranch neon warning color paint on bare skin, toxic beauty body art",
        "environment": "coral reef, nudibranch territory, toxic beautiful atmosphere",
        "lighting": "coral reef bright light, toxic beauty atmosphere, neon warning glow",
        "style": "nudibranch sea body art editorial, toxic beauty glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum neon warning grade, portrait 2:3 vertical"
    },
    "ocelot_wild": {
        "tag": "Ocelot Wild",
        "subject": "a wild ocelot body art female model",
        "body": "slim elegance model, small wild cat physique, ocelot jungle goddess presence",
        "outfit": "ocelot complex golden brown black pattern painted directly on bare skin, NOT wearing fabric, intricate wild cat body art",
        "material": "ocelot golden brown complex pattern paint on bare skin, intricate rosette chain body art",
        "environment": "Central American jungle, ocelot territory, wild cat realm",
        "lighting": "dappled jungle light, complex pattern atmosphere, wild ocelot glow",
        "style": "ocelot wild body art editorial, jungle cat glamour photography",
        "quality": "shot on Leica SL2, warm jungle grade, portrait 2:3 vertical"
    },
    "octopus_ink": {
        "tag": "Octopus Ink",
        "subject": "a mysterious octopus ink body art female model",
        "body": "slim elegance model, tentacle-wrapped figure, octopus goddess dark presence",
        "outfit": "octopus tentacle and chromatophore patterns painted directly on bare skin, NOT wearing fabric, deep sea tentacle body art",
        "material": "octopus dark ink tentacle paint on bare skin, chromatophore pattern body art",
        "environment": "dark deep ocean, octopus realm, ink cloud atmosphere",
        "lighting": "bioluminescent deep sea light, octopus dark atmosphere, ink cloud glow",
        "style": "octopus ink body art editorial, deep sea dark glamour photography",
        "quality": "shot on Sony A7R V, dark deep sea grade, portrait 2:3 vertical"
    },
    "owl_feather": {
        "tag": "Owl Feather",
        "subject": "a wise owl feather body art female model",
        "body": "slim elegance model, mysterious wise figure, owl goddess nocturnal presence",
        "outfit": "owl feather disc pattern painted directly on bare skin, NOT wearing fabric, nocturnal wisdom body art",
        "material": "owl brown grey feather disc pattern paint on bare skin, nocturnal wisdom body art",
        "environment": "ancient forest night, owl realm, nocturnal wisdom atmosphere",
        "lighting": "moonlit forest, nocturnal wisdom atmosphere, owl mysterious glow",
        "style": "owl feather body art editorial, nocturnal wisdom glamour photography",
        "quality": "shot on Leica SL2, dark moonlit grade, portrait 2:3 vertical"
    },
    "panther_black": {
        "tag": "Panther Black",
        "subject": "a sleek black panther body art female model",
        "body": "slim elegance model, perfectly defined curves, black panther goddess predator presence",
        "outfit": "black panther patterns painted directly on bare skin, NOT wearing fabric, glossy black panther coat body art, subtle rosette patterns on black",
        "material": "glossy black panther paint on bare skin, subtle dark rosette pattern, predator body art",
        "environment": "dark jungle night, black panther realm, mysterious predator atmosphere",
        "lighting": "dramatic side light on black panther skin, subtle gloss highlight, predator dark atmosphere",
        "style": "black panther body art editorial, apex predator glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum black contrast grade, portrait 2:3 vertical"
    },
    "parrot_tropical": {
        "tag": "Parrot Tropical",
        "subject": "a vivid parrot tropical body art female model",
        "body": "slim elegance model, vivid tropical figure, parrot goddess colorful presence",
        "outfit": "tropical parrot vivid red green blue yellow patterns painted directly on bare skin, NOT wearing fabric, tropical bird body art",
        "material": "parrot vivid rainbow tropical paint on bare skin, maximum color bird body art",
        "environment": "tropical rainforest, parrot canopy, vivid tropical atmosphere",
        "lighting": "bright tropical light, vivid parrot color atmosphere, tropical rainbow glow",
        "style": "parrot tropical body art editorial, vivid tropical glamour photography",
        "quality": "shot on Canon EOS R5, maximum vivid tropical grade, portrait 2:3 vertical"
    },
    "phoenix_rising": {
        "tag": "Phoenix Rising",
        "subject": "a reborn phoenix rising body art female model",
        "body": "power fitness model, rising from ashes figure, phoenix goddess rebirth presence",
        "outfit": "phoenix fire feather rebirth patterns painted directly on bare skin, NOT wearing fabric, fire bird rebirth body art",
        "material": "phoenix orange red gold fire feather paint on bare skin, rebirth fire body art",
        "environment": "rising from ashes, phoenix rebirth realm, fire and light atmosphere",
        "lighting": "dramatic fire rebirth light, phoenix rising atmosphere, rebirth fire glow",
        "style": "phoenix rising body art editorial, rebirth fire glamour photography",
        "quality": "shot on Sony A7R V, dramatic fire grade, portrait 2:3 vertical"
    },
    "praying_mantis": {
        "tag": "Praying Mantis",
        "subject": "a predatory praying mantis body art female model",
        "body": "slim elegance model, angular predator figure, mantis goddess deadly presence",
        "outfit": "praying mantis green angular patterns painted directly on bare skin, NOT wearing fabric, camouflage predator body art",
        "material": "praying mantis leaf green angular paint on bare skin, predator camouflage body art",
        "environment": "tropical leaf camouflage, mantis ambush atmosphere, predator realm",
        "lighting": "soft green leaf light, camouflage atmosphere, mantis predator glow",
        "style": "praying mantis body art editorial, predator camouflage glamour photography",
        "quality": "shot on Sony A7R V, natural green grade, portrait 2:3 vertical"
    },
    "red_fox": {
        "tag": "Red Fox",
        "subject": "a vivid red fox body art female model",
        "body": "slim elegance model, vivid orange figure, red fox goddess clever presence",
        "outfit": "red fox vivid orange red patterns painted directly on bare skin, NOT wearing fabric, clever fox body art",
        "material": "red fox vivid orange fur paint on bare skin, white muzzle black legs body art",
        "environment": "autumn forest, red fox realm, warm orange atmosphere",
        "lighting": "warm autumn forest light, fox orange atmosphere, clever fox glow",
        "style": "red fox body art editorial, clever fox glamour photography",
        "quality": "shot on Leica SL2, warm autumn orange grade, portrait 2:3 vertical"
    },
    "scarab_beetle": {
        "tag": "Scarab Beetle",
        "subject": "a sacred scarab beetle body art female model",
        "body": "slim elegance model, Egyptian sacred figure, scarab goddess divine presence",
        "outfit": "Egyptian scarab beetle golden iridescent patterns painted directly on bare skin, NOT wearing fabric, sacred scarab body art",
        "material": "golden iridescent scarab beetle paint on bare skin, Egyptian sacred pattern body art",
        "environment": "ancient Egyptian tomb, sacred scarab atmosphere, divine Egyptian realm",
        "lighting": "golden Egyptian divine light, scarab iridescent atmosphere, sacred beetle glow",
        "style": "scarab beetle body art editorial, Egyptian sacred glamour photography",
        "quality": "shot on Phase One XF IQ4, golden Egyptian grade, portrait 2:3 vertical"
    },
    "seahorse_fantasy": {
        "tag": "Seahorse Fantasy",
        "subject": "a delicate seahorse fantasy body art female model",
        "body": "slim elegance model, delicate upright figure, seahorse goddess fantasy presence",
        "outfit": "seahorse bony plate and fin patterns painted directly on bare skin, NOT wearing fabric, fantasy sea creature body art",
        "material": "seahorse golden brown bony plate paint on bare skin, fantasy creature body art",
        "environment": "coral reef fantasy, seahorse realm, magical ocean atmosphere",
        "lighting": "magical coral reef light, seahorse fantasy atmosphere, golden sea creature glow",
        "style": "seahorse fantasy body art editorial, magical ocean glamour photography",
        "quality": "shot on Hasselblad H6D, warm coral grade, portrait 2:3 vertical"
    },
    "snow_leopard": {
        "tag": "Snow Leopard",
        "subject": "a ethereal snow leopard body art female model",
        "body": "slim elegance model, graceful mountain figure, snow leopard ghost cat goddess presence",
        "outfit": "snow leopard pale grey white patterns with dark rosettes painted directly on bare skin, NOT wearing fabric, ghost cat body art",
        "material": "pale grey white snow leopard paint with dark rosettes on bare skin, mountain ghost body art",
        "environment": "Himalayan snow peak, misty mountain atmosphere, snow leopard realm",
        "lighting": "cold mountain snow light, pale ghost cat atmosphere, ethereal snow leopard glow",
        "style": "snow leopard body art editorial, Himalayan ghost cat glamour photography",
        "quality": "shot on Hasselblad H6D, cold pale mountain grade, portrait 2:3 vertical"
    },
    "sphinx_cat": {
        "tag": "Sphinx Cat",
        "subject": "a enigmatic sphinx cat body art female model",
        "body": "slim elegance model, mysterious cat goddess figure, sphinx cat enigmatic presence",
        "outfit": "Egyptian sphinx cat sacred patterns painted directly on bare skin, NOT wearing fabric, sacred cat goddess body art",
        "material": "sphinx cat golden sacred pattern paint on bare skin, Egyptian cat goddess body art",
        "environment": "ancient Egyptian temple, sacred cat realm, sphinx enigmatic atmosphere",
        "lighting": "golden Egyptian temple light, sacred cat atmosphere, sphinx enigmatic glow",
        "style": "sphinx cat body art editorial, Egyptian cat goddess glamour photography",
        "quality": "shot on Hasselblad H6D, golden Egyptian grade, portrait 2:3 vertical"
    },
    "swan_white": {
        "tag": "Swan White",
        "subject": "a graceful swan white body art female model",
        "body": "slim elegance model, graceful long neck figure, swan goddess elegant presence",
        "outfit": "swan pure white feather patterns painted directly on bare skin, NOT wearing fabric, elegant swan body art",
        "material": "swan pure white feather paint on bare skin, elegant lake bird body art",
        "environment": "misty lake at dawn, swan realm, elegant white atmosphere",
        "lighting": "soft dawn lake mist light, swan pure white atmosphere, elegant grace glow",
        "style": "swan white body art editorial, elegant lake glamour photography",
        "quality": "shot on Hasselblad H6D, pure white soft grade, portrait 2:3 vertical"
    },
    "unicorn_opal": {
        "tag": "Unicorn Opal",
        "subject": "a magical unicorn opal body art female model",
        "body": "slim elegance model, magical opal figure, unicorn goddess rainbow presence",
        "outfit": "unicorn opal rainbow iridescent patterns painted directly on bare skin, NOT wearing fabric, magical horn and opal body art",
        "material": "unicorn opal rainbow iridescent paint on bare skin, magical creature body art",
        "environment": "enchanted meadow, unicorn magical realm, opal rainbow atmosphere",
        "lighting": "magical rainbow opal light, unicorn iridescent atmosphere, magical creature glow",
        "style": "unicorn opal body art editorial, magical creature glamour photography",
        "quality": "shot on Hasselblad H6D, maximum opal iridescent grade, portrait 2:3 vertical"
    },
    "wolf_grey": {
        "tag": "Wolf Grey",
        "subject": "a wild wolf grey body art female model",
        "body": "athletic fitness model, wild pack figure, wolf goddess pack leader presence",
        "outfit": "wolf grey fur patterns painted directly on bare skin, NOT wearing fabric, wild pack body art",
        "material": "wolf grey fur pattern paint on bare skin, wild pack body art",
        "environment": "northern forest, wolf pack realm, wild grey atmosphere",
        "lighting": "cold northern forest light, wolf pack atmosphere, wild grey glow",
        "style": "wolf grey body art editorial, wild pack glamour photography",
        "quality": "shot on Sony A7R V, cold grey forest grade, portrait 2:3 vertical"
    },
    "zebra_stripes": {
        "tag": "Zebra Stripes",
        "subject": "a striking zebra stripes body art female model",
        "body": "slim elegance model, bold stripe figure, zebra goddess striking presence",
        "outfit": "zebra bold black white stripe patterns painted directly on bare skin, NOT wearing fabric, maximum contrast stripe body art",
        "material": "zebra bold black white stripe paint on bare skin, maximum contrast body art",
        "environment": "African savanna, zebra herd, bold stripe atmosphere",
        "lighting": "harsh African sun, maximum contrast stripe atmosphere, zebra bold glow",
        "style": "zebra stripes body art editorial, maximum contrast glamour photography",
        "quality": "shot on Phase One XF IQ4, maximum black white contrast grade, portrait 2:3 vertical"
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
print(f"총 프리셋: 605 → {605 + added}개")
