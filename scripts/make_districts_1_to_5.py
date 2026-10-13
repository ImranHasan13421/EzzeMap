# -*- coding: utf-8 -*-
import json
import os

with open('scripts/all_200_extracted.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

def write_module(slug, data_dict):
    out_path = os.path.join('scripts', 'data_districts_20', f'{slug}.py')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('DISTRICT_DATA = ' + json.dumps(data_dict, ensure_ascii=False, indent=4) + '\n')
    print(f"Wrote {out_path}")

# ==========================================
# 1. LAKSHMIPUR
# ==========================================
l_raw = all_data['lakshmipur']
lakshmipur_data = {
    "slug": "lakshmipur",
    "en": "Lakshmipur",
    "bn": "লক্ষ্মীপুর",
    "hero_title_en": "Lakshmipur Coastal Estuaries & Zamindari Heritage",
    "hero_title_bn": "লক্ষ্মীপুরের উপকূলীয় মোহনা ও ঐতিহাসিক জমিদারি ঐতিহ্য",
    "hero_sub_en": "Historic colonial zamindar estates, sacred Sufi shrines, and vast Meghna river estuary landscapes.",
    "hero_sub_bn": "উপনিবেশিক যুগের প্রাচীন জমিদার বাড়ি, আধ্যাত্মিক সুফি দরবার ও মেঘনা নদীর সুবিশাল মোহনার রূপময় প্রকৃতি।",
    "tagline_en": "A historic coastal district flanking the mighty Lower Meghna, celebrated for rich river traditions, legendary zamindari estates at Dalal Bazar, and serene riverside horizons.",
    "tagline_bn": "লোয়ার মেঘনার উপকূলে অবস্থিত এক ঐতিহ্যবাহী উপকূলীয় জেলা, যা দালাল বাজারের প্রাচীন জমিদারি স্থাপত্য, পুণ্যময় দরবার ও নদীর উত্তাল রূপের জন্য পরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/lakshmipur/carousel-1.webp",
            "titleEn": "Dalal Bazar Zamindar Bari Historic Facade",
            "titleBn": "দালাল বাজার জমিদার বাড়ির প্রাচীন প্রাসাদ",
            "subtitleEn": "Centuries-old aristocratic mansion in Lakshmipur Sadar showcasing neoclassical colonnades and antique courtyards",
            "subtitleBn": "লক্ষ্মীপুর সদরের শতাব্দীপ্রাচীন অভিজাত প্রাসাদ, যার স্তম্ভ ও উন্মুক্ত আঙিনায় সোনালী অতীত স্পষ্ট"
        },
        {
            "id": 2,
            "image": "images/districts/lakshmipur/carousel-2.webp",
            "titleEn": "Tita Khan Jame Mosque (Jinn Mosque) Architectural Spire",
            "titleBn": "টিটা খাঁ জামে মসজিদ (জ্বীন মসজিদ) স্থাপত্য শৈলী",
            "subtitleEn": "Intricately crafted historic religious sanctuary in Raipur surrounded by fascinating folklore and delicate masonry",
            "subtitleBn": "রায়পুরের প্রাচীন ঐতিহাসিক মসজিদ যা অনন্য লোককথা ও মনোমুগ্ধকর চুন-সুরকির গাঁথুনির জন্য বিখ্যাত"
        },
        {
            "id": 3,
            "image": "images/districts/lakshmipur/carousel-3.webp",
            "titleEn": "Ramgati Meghna Riverfront Estuary Vista",
            "titleBn": "রামগতি মেঘনা নদীতীরের মোহনা দৃশ্য",
            "subtitleEn": "Endless river horizons and whispering breezes where the Lower Meghna meets the Bay of Bengal waters",
            "subtitleBn": "মেঘনার উত্তাল জলরাশি ও দিগন্তজোড়া মোহনা, যা ভ্রমণপিপাসুদের উপহার দেয় মুক্ত হাওয়া ও অপূর্ব সূর্যাস্ত"
        },
        {
            "id": 4,
            "image": "images/districts/lakshmipur/carousel-4.webp",
            "titleEn": "Khowasagar Dighi Historic Water Reservoir",
            "titleBn": "ঐতিহাসিক খোয়াসাগর দীঘি ও পাড়ের নিসর্গ",
            "subtitleEn": "Sprawling heritage dighi dug centuries ago to supply clean freshwater, enveloped by tranquil village greenery",
            "subtitleBn": "দালাল বাজার এলাকায় শতাব্দীপ্রাচীন বিশাল জলাধার, যার পাড়ে স্নিগ্ধ শান্ত পল্লী পরিবেশ বিরাজমান"
        },
        {
            "id": 5,
            "image": "images/districts/lakshmipur/carousel-5.webp",
            "titleEn": "Char Alexander Scenic Coastal Riverbank",
            "titleBn": "চর আলেকজান্ডার উপকূলীয় নদীতীর",
            "subtitleEn": "Panoramic coastal char landscapes and fishing boat fleets cruising along the active river corridor",
            "subtitleBn": "উপকূলীয় চরাঞ্চলের নয়নাভিরাম দৃশ্য ও জেলে নৌকার অবাধ বিচরণে মুখরিত নদীপ্রকৃতি"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Dalal Bazar Zamindar Bari",
            "nameBn": "দালাল বাজার জমিদার বাড়ি",
            "categoryEn": "Colonial Aristocratic Estate",
            "categoryBn": "উপনিবেশিক জমিদারি প্রাসাদ",
            "descEn": "Dalal Bazar Zamindar Bari is one of the most prominent eighteenth-century feudal estates in Lakshmipur Sadar, established by prominent merchant-zamindars during the British colonial era. Spread across several acres, the compound features ornamental entrance gates, grand residential quarters, inner Zenana courtyards, and fortified treasuries. Classical Greco-Roman pilasters, arched verandas, and decorative brick cornices demonstrate the opulence of regional landlords who handled salt and maritime commerce. The surrounding premises house expansive bathing ponds, paved ghats, and surviving family temples reflecting a blend of traditional Bengali and European architecture. Today, visitors and heritage enthusiasts wander through its nostalgic corridors to experience the vanished elegance of Lakshmipur's aristocratic past.",
            "descBn": "দালাল বাজার জমিদার বাড়ি লক্ষ্মীপুর সদর উপজেলার অন্যতম প্রাচীন ও দৃষ্টিনন্দন সামন্তযুগীয় প্রাসাদ, যা অষ্টাদশ শতাব্দীতে স্থানীয় প্রভাবশালী বণিক ও জমিদার পরিবার কর্তৃক প্রতিষ্ঠিত হয়েছিল। সুবিশাল এলাকা জুড়ে বিস্তৃত এই জমিদার বাড়িতে রয়েছে সুসজ্জিত সিংহদ্বার, রাজকীয় অন্দরমহল, নাচঘর ও প্রশাসনিক ভবন। ইউরোপীয় ও স্থানীয় স্থাপত্যের মেলবন্ধনে তৈরি এই ভবনের খিলানযুক্ত বারান্দা এবং কারুকার্যময় স্তম্ভ তৎকালীন জমিদারদের প্রভাব-প্রতিপত্তির পরিচয় দেয়। প্রাসাদ প্রাঙ্গণে রয়েছে সুপ্রাচীন পুকুর, শানবাঁধানো ঘাট ও দেবালয়, যা নিস্তব্ধ পরিবেশে অতীতের স্মৃতি জাগিয়ে তোলে। ইতিহাসপ্রেমীদের জন্য এই প্রাসাদটি লক্ষ্মীপুরের গৌরবময় ইতিহাসের অন্যতম শ্রেষ্ঠ স্মারক।",
            "locationEn": l_raw['hist_spots'][0]['location'],
            "locationBn": "দালাল বাজার, লক্ষ্মীপুর সদর, লক্ষ্মীপুর",
            "mapUrl": l_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Tita Khan Jame Mosque (Jinn Mosque)",
            "nameBn": "টিটা খাঁ জামে মসজিদ (জ্বীন মসজিদ)",
            "categoryEn": "Historic Architectural Mosque",
            "categoryBn": "ঐতিহাসিক স্থাপত্যিক মসজিদ",
            "descEn": "Tita Khan Jame Mosque, popular throughout the region as the 'Jinn Mosque', is an extraordinary nineteenth-century sanctuary situated in Raipur Upazila. Commissioned by revered local personality Moulvi Tita Khan, the mosque is celebrated for its deep subterranean foundations, thick lime-surki brick walls, and graceful vaulted domes. Local folklore claims that unseen supernatural forces assisted in its rapid overnight construction, drawing curious travellers and spiritual pilgrims from across the nation. The sanctuary exhibits exquisite floral plaster reliefs, graceful arched entryways, and traditional terracotta jaali ventilation panels. Maintaining an aura of profound sacred serenity, the mosque remains an active center of community prayers and a prized monument of Lakshmipur's spiritual architecture.",
            "descBn": "টিটা খাঁ জামে মসজিদ, যা স্থানীয়ভাবে 'জ্বীন মসজিদ' নামে সমধিক পরিচিত, রায়পুর উপজেলার এক অনন্য স্থাপত্যকীর্তি ও আধ্যাত্মিক নিদর্শন। উনিশ শতকে ধর্মপ্রাণ ব্যক্তিত্ব মৌলভী টিটা খাঁ কর্তৃক প্রতিষ্ঠিত এই মসজিদটি এর সুদৃঢ় ভিত্তিপ্রস্তর, চুন-সুরকির পুরু দেয়াল এবং চমৎকার গম্বুজ নির্মাণের জন্য প্রশংসিত। লোকমুখে প্রচলিত রহস্যময় বিশ্বাস যে এটি অলৌকিক শক্তিবলে অত্যন্ত দ্রুত নির্মিত হয়েছিল, দেশজুড়ে দর্শনার্থী ও ইতিহাসানুরাগীদের কৌতূহলী করে তোলে। মসজিদের দেওয়ালে রয়েছে দৃষ্টিনন্দন লতাপাতার নকশা, খিলানযুক্ত প্রবেশপথ এবং ঐতিহ্যবাহী অলংকরণ। নিবিড় প্রশান্তিময় পরিবেশে প্রতিদিন বহু মুসল্লি এখানে নামাজ আদায় করেন এবং পর্যটকরা এর অপূর্ব নির্মাণশৈলী উপভোগ করতে আসেন।",
            "locationEn": l_raw['hist_spots'][1]['location'],
            "locationBn": "রায়পুর, লক্ষ্মীপুর",
            "mapUrl": l_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Kanchanpur Zamindar Bari Jame Mosque",
            "nameBn": "কাঞ্চনপুর জমিদার বাড়ি জামে মসজিদ",
            "categoryEn": "Heritage Estate Mosque",
            "categoryBn": "জমিদারি আমলের ঐতিহাসিক মসজিদ",
            "descEn": "Nestled in the historic locality of Kanchanpur, this heritage estate mosque stands as a timeless testament to Islamic religious patronage by regional zamindars. Constructed with seasoned terracotta bricks and indigenous lime mortar, the building features three central ribbed domes and ornate corner turrets that rise above the tranquil countryside. Its western facade displays deeply recessed prayer niches decorated with refined stucco geometric patterns and classical calligraphy bands. The mosque stands adjacent to the historic residential ruins of the Kanchanpur landlords, flanked by ancestral dighis and shade-giving mango groves. Visitors appreciate the sanctuary for its peaceful atmosphere, undisturbed historic brickwork, and deep spiritual legacy.",
            "descBn": "ঐতিহাসিক কাঞ্চনপুর গ্রামে অবস্থিত জমিদার বাড়ি জামে মসজিদটি স্থানীয় জমিদার পরিবারের ধর্মীয় পৃষ্ঠপোষকতা ও শিল্পরুচির এক চমৎকার নিদর্শন। প্রাচীন পোড়ামাটির ইট ও চুন-সুরকির সমন্বয়ে নির্মিত এই মসজিদের ছাদে রয়েছে তিনটি সুদৃশ্য গম্বুজ এবং চার কোণে শোভা পাওয়া কারুকার্যময় মিনার। মসজিদের পশ্চিম দেওয়ালে নির্মিত মেহরাবগুলোতে অত্যন্ত সূক্ষ্ম জ্যামিতিক নকশা ও আরবেস্ক অলংকরণ চোখে পড়ে। সংলগ্ন জমিদার বাড়ির ধ্বংসাবশেষ ও প্রাচীন দীঘির পাড়ে অবস্থিত এই মসজিদটি গ্রামীণ নিসর্গের সাথে অপূর্ব সামঞ্জস্য তৈরি করেছে। শতাব্দীর স্মৃতি বিজড়িত এই শান্তিময় উপাসনালয়টি ইতিহাসসন্ধানীদের জন্য অত্যন্ত আকর্ষণীয় একটি স্থান।",
            "locationEn": l_raw['hist_spots'][2]['location'],
            "locationBn": "কাঞ্চনপুর, লক্ষ্মীপুর",
            "mapUrl": l_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Shyampur Daira Sharif",
            "nameBn": "শ্যামপুর দায়রা শরীফ",
            "categoryEn": "Historic Sufi Shrine & Monastery",
            "categoryBn": "ঐতিহাসিক সুফি দরবার ও খানকাহ",
            "descEn": "Shyampur Daira Sharif in Ramganj Upazila is a venerated spiritual sanctuary that has served as a beacon of Islamic learning, Sufi contemplation, and humanitarian service for over two centuries. Founded by saintly scholars who migrated to Bengal to spread spiritual wisdom, the complex includes sacred tombs, a historic prayer hall, madrasa quarters, and a communal dining hall. The architecture emphasizes tranquility, with expansive colonnaded verandas, shaded gardens, and reflective pools that create an atmosphere of contemplation. Tens of thousands of devotees gather here during annual commemorative Urs gatherings to seek blessings and participate in traditional devotional sessions. It stands as a centerpiece of Lakshmipur's living spiritual heritage and communal harmony.",
            "descBn": "রামগঞ্জ উপজেলার শ্যামপুর দায়রা শরীফ লক্ষ্মীপুরের এক ঐতিহ্যবাহী আধ্যাত্মিক প্রতিষ্ঠান, যা দুই শতাব্দীরও বেশি সময় ধরে সুফি দর্শন, ধর্মীয় শিক্ষা ও মানবসেবায় গুরুত্বপূর্ণ ভূমিকা পালন করে আসছে। আধ্যাত্মিক সুফি সাধকগণের দ্বারা প্রতিষ্ঠিত এই দরবার প্রাঙ্গণে রয়েছে পুণ্যময় মাজার, প্রাচীন জামে মসজিদ, খানকাহ এবং ধর্মপ্রাণ মানুষের জন্য উন্মুক্ত লঙ্গরখানা। সবুজ গাছগাছালি ও শান্ত প্রাঙ্গণে ঘেরা এই দরবারে প্রবেশ করলে এক অপার্থিব প্রশান্তি অনুভূত হয়। প্রতি বছর বার্ষিক ওরস ও ধর্মীয় সম্মেলনে দূর-দূরান্ত থেকে হাজার হাজার ভক্ত এখানে পুণ্য অর্জনে সমবেত হন। সর্বজনীন সৌহার্দ্য ও আধ্যাত্মিকতার প্রতীক হিসেবে শ্যামপুর দায়রা শরীফের খ্যাতি অঞ্চলজুড়ে সমাদৃত।",
            "locationEn": l_raw['hist_spots'][3]['location'],
            "locationBn": "শ্যামপুর, রামগঞ্জ, লক্ষ্মীপুর",
            "mapUrl": l_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Miran Shah Shrine",
            "nameBn": "মীরান শাহ মাজার শরীফ",
            "categoryEn": "Sacred Historical Mazar",
            "categoryBn": "পবিত্র ঐতিহাসিক মাজার",
            "descEn": "Miran Shah Shrine in Kanchanpur commemorates the sacred resting place of Hazrat Miran Shah, an early Sufi missionary who played a foundational role in propagating ethical teachings across coastal Bengal. The shrine complex features an authentic domed mausoleum constructed in traditional Sultanate-Mughal synthesis style, surrounded by old brick boundary enclosures and protective banyan trees. Devotees of diverse faiths visit the sanctuary throughout the year to offer prayers, light oil lamps, and recite verses in remembrance of the saint's benevolence. The surrounding grounds preserve antique water reservoirs and stone inscriptions that highlight the long cultural history of the settlement. Visiting the shrine provides a profound connection to the historical currents of syncretic spirituality that define Lakshmipur.",
            "descBn": "কাঞ্চনপুরে অবস্থিত হযরত মীরান শাহ মাজার শরীফ উপকূলীয় বাংলায় ইসলাম প্রচার ও মানবিক মূল্যবোধ প্রতিষ্ঠায় আত্মনিয়োগকারী সুফি সাধকের এক পবিত্র সমাধিস্থল। সুদৃশ্য গম্বুজযুক্ত এই সমাধি সৌধটি মুঘল ও স্থানীয় নির্মাণরীতির ছোঁয়ায় প্রতিষ্ঠিত, যার চারপাশ ঘিরে রয়েছে প্রাচীন বৃক্ষরাজি ও সুরম্য সীমানা প্রাচীর। যুগ যুগ ধরে বিভিন্ন সম্প্রদায়ের ধর্মপ্রাণ মানুষ মানসিক শান্তি ও মানত পূরণের উদ্দেশ্যে এখানে উপস্থিত হন। মাজার প্রাঙ্গণে থাকা প্রাচীন জলাশয় ও পরিবেশ দর্শনার্থীদের মনে এক নিবিড় ভক্তিভাব সৃষ্টি করে। লক্ষ্মীপুরের শতাব্দীপ্রাচীন সুফি ঐতিহ্যের প্রামাণ্য স্মারক হিসেবে মীরান শাহের মাজার অত্যন্ত শ্রদ্ধার সাথে সংরক্ষিত।",
            "locationEn": l_raw['hist_spots'][4]['location'],
            "locationBn": "কাঞ্চনপুর, লক্ষ্মীপুর",
            "mapUrl": l_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Ramgati Meghna Riverfront",
            "nameBn": "রামগতি মেঘনা নদীতীর",
            "categoryEn": "Coastal Riverfront Panorama",
            "categoryBn": "উপকূলীয় নদীতীর ও মোহনা দৃশ্য",
            "descEn": "Ramgati Meghna Riverfront offers an awe-inspiring natural escape where the wide Lower Meghna river surges forward into the coastal estuary. Visitors strolling along the protective embankments are greeted by refreshing maritime breezes, soaring river terns, and panoramic views of endless water stretching to the distant horizon. The riverbank comes alive during late afternoons as sunset paints the rippling waves in shades of gold and crimson, while traditional wooden fishing boats glide smoothly towards the harbor. Fresh Hilsa fish markets set up directly on the riverfront allow travelers to witness active coastal trades and savor authentic regional seafood. It represents one of the premier open-air eco-tourism and relaxation hubs in Lakshmipur.",
            "descBn": "রামগতি মেঘনা নদীতীর লক্ষ্মীপুরের অন্যতম সেরা প্রাকৃতিক আকর্ষণ, যেখানে প্রমত্তা মেঘনা নদী সমুদ্রের মোহনায় মিলিত হয়ে এক অনন্ত জলরাশির বিস্তার সৃষ্টি করেছে। বেড়িবাঁধের ওপর দিয়ে হাঁটলে শরীর জুড়ানো দখিনা বাতাস ও জলতরঙ্গের গর্জন ভ্রমণপিপাসুদের এক অদ্ভুত মুগ্ধতায় আচ্ছন্ন করে। গোধূলিলগ্নে যখন অস্তগামী সূর্যের রক্তিম আভা নদীর বুকে ছড়িয়ে পড়ে, তখন এখানে সৃষ্টি হয় এক অপরূপ স্বর্গীয় দৃশ্য। নদীতে সারি সারি পালতোলা মাছ ধরার ট্রলার ও নৌকা এই উপকূলীয় জীবনের বাস্তব চিত্র তুলে ধরে। নদীতীরবর্তী বাজার থেকে রূপালী ইলিশের তাজা স্বাদ নেওয়া ও মুক্ত বাতাসে ঘুরে বেড়ানোর জন্য রামগতি এক আদর্শ গন্তব্য।",
            "locationEn": l_raw['tour_spots'][0]['location'],
            "locationBn": "রামগতি, লক্ষ্মীপুর",
            "mapUrl": l_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Khowasagar Dighi",
            "nameBn": "খোয়াসাগর দীঘি",
            "categoryEn": "Historic Water Reservoir & Eco Spot",
            "categoryBn": "ঐতিহাসিক দীঘি ও পরিবেশবান্ধব পর্যটন স্থান",
            "descEn": "Khowasagar Dighi is an immense historical water reservoir located in the Dalal Bazar area, excavated centuries ago by the benevolent zamindars to resolve drinking water scarcity. Spanning several dozen bighas, the shimmering body of water is encircled by tall mahogany, palm, and rain trees that cast soothing shadows across grassy banks. During the winter months, migratory birds from northern climes flock to the tranquil waters, creating a haven for birdwatchers and nature photographers. Local residents and tourists gather here for morning walks, peaceful angling sessions, and leisurely picnics by the water's edge. The harmony of historical engineering and scenic natural beauty makes it an indispensable attraction.",
            "descBn": "দালাল বাজার এলাকায় অবস্থিত ঐতিহাসিক খোয়াসাগর দীঘি লক্ষ্মীপুরের এক সুবিশাল ও প্রাচীন মিষ্টি জলের জলাশয়, যা বহু শতাব্দী পূর্বে স্থানীয় প্রজাদের পানীয় জলের কষ্ট দূর করতে খনন করা হয়েছিল। বিস্তৃত এই দীঘির চারপাশ সবুজ তাল, নারকেল ও মেহগনি গাছের স্নিগ্ধ ছায়ায় ঘেরা, যা এক মনোরম পরিবেশ উপহার দেয়। শীত মৌসুমে দূরদেশী অতিথি পাখির কলকাকলিতে মুখরিত হয়ে ওঠে দীঘির শান্ত জলরাশি, ফলে পক্ষীপ্রেমী ও আলোকচিত্রীদের কাছে এটি অত্যন্ত প্রিয়। স্থানীয় মানুষ ও পর্যটকরা এখানে হাঁটাহাঁটি, ছিপ ফেলে মাছ ধরা কিংবা অবসর সময় কাটাতে ভিড় জমান। ইতিহাস ও প্রকৃতির এক অপূর্ব মেলবন্ধন এই খোয়াসাগর দীঘি।",
            "locationEn": l_raw['tour_spots'][1]['location'],
            "locationBn": "দালাল বাজার এলাকা, লক্ষ্মীপুর সদর, লক্ষ্মীপুর",
            "mapUrl": l_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Sree Sree Anandamoyee Kali Bari",
            "nameBn": "শ্রী শ্রী আনন্দময়ী কালী বাড়ি",
            "categoryEn": "Traditional Hindu Sanctuary & Cultural Site",
            "categoryBn": "ঐতিহ্যবাহী হিন্দু দেবালয় ও সাংস্কৃতিক স্থান",
            "descEn": "Situated near the Government Girls' High School in Lakshmipur Sadar, Sree Sree Anandamoyee Kali Bari is a venerable Hindu sanctuary deeply intertwined with the town's cultural life. Renowned for its artistic terracotta-embellished sanctum and sacred peepal trees, the temple provides a peaceful oasis in the heart of urban Lakshmipur. The sanctuary becomes the focal point of joyous celebrations during annual Kali Puja and Deepavali, illuminated by thousands of clay oil lamps and attended by devotees from all walks of life. Its welcoming courtyard houses shrines dedicated to various deities, reflecting centuries of devotion and religious architecture. Visitors admire the spiritual ambiance, intricate temple rituals, and warm communal environment.",
            "descBn": "লক্ষ্মীপুর সদর পৌর এলাকার সরকারি বালিকা উচ্চ বিদ্যালয়ের সন্নিকটে অবস্থিত শ্রী শ্রী আনন্দময়ী কালী বাড়ি শহরের এক সুপ্রাচীন ও ঐতিহ্যবাহী ধর্মীয় মিলনক্ষেত্র। কারুকার্যময় মন্দির শিখর এবং শতাব্দীপ্রাচীন বটবৃক্ষবেষ্টিত এই মন্দির প্রাঙ্গণে এক শান্ত ও পবিত্র পরিবেশ বিরাজ করে। প্রতি বছর কালীপূজা ও দীপাবলি উৎসবে প্রদীপের আলোকচ্ছটায় মন্দিরটি অপরূপ রূপ ধারণ করে এবং ধর্ম-বর্ণ নির্বিশেষে দর্শনার্থীদের সমাগম ঘটে। মন্দিরের অভ্যন্তরে রয়েছে দেব-দেবীর সুন্দর প্রতিমা এবং সনাতন ঐতিহ্যের নানা কারুকাজ। শহরের কেন্দ্রস্থলে অবস্থিত হলেও এর ভেতরের স্নিগ্ধ পরিবেশ যে কাউকে ক্ষণিকের জন্য শহরের কোলাহল ভুলিয়ে আধ্যাত্মিক প্রশান্তি এনে দেয়।",
            "locationEn": l_raw['tour_spots'][2]['location'],
            "locationBn": "সরকারি বালিকা উচ্চ বিদ্যালয়ের নিকটে, লক্ষ্মীপুর সদর, লক্ষ্মীপুর",
            "mapUrl": l_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Char Alexander Riverbank",
            "nameBn": "চর আলেকজান্ডার নদীতীর",
            "categoryEn": "Coastal Char & Sunset Viewpoint",
            "categoryBn": "উপকূলীয় চরাঞ্চল ও সূর্যাস্ত ভিউপয়েন্ট",
            "descEn": "Char Alexander Riverbank in Ramganj-Ramgati coastal belt is an expansive alluvial wonderland shaped by the relentless dynamic flows of the Lower Meghna River. The riverbank features dramatic sandbars, verdant grazing pastures, and an unobstructed panoramic vista across the vast river channel. Travel enthusiasts visit this serene haven to observe traditional coastal fishing methods, witness migratory birds skimming across tidal marshes, and watch spectacular red sunsets over open waters. The gentle lap of water against coastal dykes and the fresh marine wind provide a rejuvenating retreat from city bustle. It stands as an iconic destination for travelers seeking pristine deltaic nature in southern Bangladesh.",
            "descBn": "রামগতি উপজেলার চর আলেকজান্ডার নদীতীর মেঘনা নদীর প্রবল স্রোত ও পলি জমার ফলে গঠিত এক মনোমুগ্ধকর উপকূলীয় চরাঞ্চল। দিগন্তবিস্তৃত সবুজ তৃণভূমি, বালুকাবেলা এবং নদীর বিশাল জলরাশি এই স্থানটিকে প্রকৃতির এক স্বর্গরাজ্যে পরিণত করেছে। ভ্রমণপিপাসুরা এখানে নদীর শান্ত হাওয়া উপভোগ করতে, স্থানীয় জেলেদের মাছ ধরার দৃশ্য দেখতে এবং নদীর বুকে লাল টুকটুকে সূর্যের অস্তাচলে যাওয়ার দৃশ্য দেখতে আসেন। শীতের সকালে চরাঞ্চলের ওপর কুয়াশার চাদর এবং মুক্ত বাতাসে পাখির ওড়াউড়ি যে কারও মনকে প্রফুল্ল করে তোলে। কোলাহলমুক্ত গ্রামীণ নদীর আসল রূপ আবিষ্কারে চর আলেকজান্ডার ভ্রমণপ্রেমীদের কাছে এক অনন্য তীর্থস্থান।",
            "locationEn": l_raw['tour_spots'][3]['location'],
            "locationBn": "চর আলেকজান্ডার, রামগতি, লক্ষ্মীপুর",
            "mapUrl": l_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Meghna River Estuary Viewpoint",
            "nameBn": "মেঘনা নদী মোহনা ভিউপয়েন্ট",
            "categoryEn": "River Confluence Observation Deck",
            "categoryBn": "নদী সঙ্গম ও প্রাকৃতিক পর্যবেক্ষণ কেন্দ্র",
            "descEn": "The Meghna River Estuary Viewpoint at the extreme southern edge of Ramgati presents an awe-inspiring vantage point where river and ocean waters converge in sweeping tidal rhythms. Standing at this prominent observation point, observers behold an oceanic scale of water where the horizon dissolves into sky and distant green char formations float like emeralds. Powerful marine breezes, dancing waves, and the ceaseless movement of seafaring cargo vessels and mechanized trawlers deliver an exhilarating sensation of coastal vastness. Sunrise and twilight hours here offer extraordinary photographic compositions of dramatic lighting against water. It is an unforgettable ecological highlight of any travel itinerary across Lakshmipur.",
            "descBn": "রামগতির দক্ষিণাংশে অবস্থিত মেঘনা নদী মোহনা ভিউপয়েন্ট এমন একটি দর্শনীয় স্থান যেখানে মেঘনা নদী বঙ্গোপসাগরের সাথে মিলিত হওয়ার বিশালতা স্পষ্ট প্রতীয়মান হয়। এই ভিউপয়েন্টে দাঁড়ালে মনে হয় যেন নদীর কোনো শেষ নেই, জল আর আকাশ মিলেমিশে একাকার হয়ে গেছে। দূরবর্তী সবুজ চরাঞ্চল ও নদীর বুক চিরে ছুটে চলা বিশালাকার ট্রলার ও জাহাজের দৃশ্য এক রোমাঞ্চকর অনুভূতি তৈরি করে। নদীর তীব্র বাতাস ও ঢেউয়ের গর্জন শহরের সমস্ত ক্লান্তি দূর করে দেয়। বিশেষ করে ভোর ও সন্ধ্যার আলোয় মোহনার দৃশ্য এতটাই মোহময় যে আলোকচিত্রী ও ভ্রমণপ্রেমীরা বারবার এখানে ছুটে আসেন।",
            "locationEn": l_raw['tour_spots'][4]['location'],
            "locationBn": "রামগতি, লক্ষ্মীপুর",
            "mapUrl": l_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('lakshmipur', lakshmipur_data)

# ==========================================
# 2. GOPALGANJ
# ==========================================
g_raw = all_data['gopalganj']
gopalganj_data = {
    "slug": "gopalganj",
    "en": "Gopalganj",
    "bn": "গোপালগঞ্জ",
    "hero_title_en": "Gopalganj Historic Tungipara & Riverside Wetlands",
    "hero_title_bn": "গোপালগঞ্জের ঐতিহাসিক টুঙ্গিপাড়া ও মধুমতীর কোল",
    "hero_sub_en": "Father of the Nation's sacred mausoleum, Matua spiritual heritage at Orakandi, and peaceful Madhumati riverfronts.",
    "hero_sub_bn": "জাতির পিতার পবিত্র সমাধি সৌধ, ওড়াকান্দির মতুয়া তীর্থ ও মধুমতী নদীর স্নিগ্ধ রূপমাধুর্য।",
    "tagline_en": "The sacred birthplace of Bangabandhu Sheikh Mujibur Rahman, enriched by centuries of deltaic heritage, grand zamindari mansions at Ulpur, and meandering river canals.",
    "tagline_bn": "স্বাধীন বাংলাদেশের স্থপতি বঙ্গবন্ধু শেখ মুজিবুর রহমানের পুণ্য জন্মভূমি, যা উলপুরের প্রাচীন জমিদারি প্রাসাদ, ওড়াকান্দির ধর্মীয় তীর্থ ও মধুমতীর রূপলাবণ্যে মহিমান্বিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/gopalganj/carousel-1.webp",
            "titleEn": "Bangabandhu Mausoleum Complex Monument",
            "titleBn": "বঙ্গবন্ধু সমাধি সৌধ কমপ্লেক্সের নান্দনিক সৌধ",
            "subtitleEn": "Architectural marvel of red ceramic brick and marble honoring the Father of the Nation in Tungipara",
            "subtitleBn": "টুঙ্গিপাড়ায় জাতির পিতা বঙ্গবন্ধু শেখ মুজিবুর রহমানের স্মরণে লাল সিরামিক ইট ও মার্বেল পাথরে নির্মিত জাতীয় সৌধ"
        },
        {
            "id": 2,
            "image": "images/districts/gopalganj/carousel-2.webp",
            "titleEn": "Orakandi Thakur Bari Sacred Pilgrimage Shrine",
            "titleBn": "ওড়াকান্দি ঠাকুর বাড়ির পবিত্র মতুয়া মহাতীর্থ",
            "subtitleEn": "Venerable birthplace of Harichand Thakur drawing millions of Matua devotees to the holy Kamana Sagar lake",
            "subtitleBn": "শ্রীশ্রী হরিচাঁদ ঠাকুরের স্মৃতিবিজড়িত পুণ্যধাম ও কামনা সাগরের শান্তিময় প্রাঙ্গণ"
        },
        {
            "id": 3,
            "image": "images/districts/gopalganj/carousel-3.webp",
            "titleEn": "Ulpur Zamindar Bari Colonial Mansions",
            "titleBn": "উলপুর জমিদার বাড়ির প্রাচীন রাজপ্রাসাদ",
            "subtitleEn": "Cluster of historic neo-classical brick estates built by wealthy zamindars along rural waterways",
            "subtitleBn": "গোপালগঞ্জ সদরের উলপুরে শতাব্দীপ্রাচীন ইউরোপীয় স্থাপত্যশৈলীর অভিজাত জমিদারি ভবন"
        },
        {
            "id": 4,
            "image": "images/districts/gopalganj/carousel-4.webp",
            "titleEn": "Madhumati Riverbank Scenic Sunset Promenade",
            "titleBn": "মধুমতী নদীতীরের স্নিগ্ধ সূর্যাস্ত দৃশ্য",
            "subtitleEn": "Meandering river waters flowing past lush countryside and whispering village groves",
            "subtitleBn": "মধুমতীর বুক চিরে বয়ে চলা শান্ত বাতাস ও গোধূলির রক্তিম আভার অপূর্ব দৃশ্যপট"
        },
        {
            "id": 5,
            "image": "images/districts/gopalganj/carousel-5.webp",
            "titleEn": "Tungipara Mausoleum Landscaped Botanical Gardens",
            "titleBn": "টুঙ্গিপাড়া সমাধি সৌধের সুবিন্যস্ত বাগান ও দিঘি",
            "subtitleEn": "Lush manicured lawns, lotus-filled water bodies, and quiet promenades surrounding the memorial",
            "subtitleBn": "সমাধি সৌধ কমপ্লেক্সের চারিদিকে মনোরম সবুজ লন, পদ্মপুকুর ও শান্ত পদচারণ পথ"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Bangabandhu Sheikh Mujibur Rahman Mausoleum Complex",
            "nameBn": "বঙ্গবন্ধু শেখ মুজিবুর রহমান সমাধি সৌধ কমপ্লেক্স",
            "categoryEn": "National Historical Memorial",
            "categoryBn": "জাতীয় ঐতিহাসিক সমাধি কমপ্লেক্স",
            "descEn": "The Bangabandhu Sheikh Mujibur Rahman Mausoleum Complex in Tungipara is one of Bangladesh's most sacred national monuments, preserving the final resting place of the Father of the Nation. Designed with soaring red ceramic brick walls, pure white marble finishes, and graceful domed skylights, the architectural sanctuary evokes profound solemnity. The surrounding complex spans over thirty-eight acres, incorporating ancestral home exhibits, a dedicated research library, a museum documenting the Liberation War, and landscaped lotus ponds. Millions of citizens, international dignitaries, and students make pilgrimages here annually to pay tribute to the architect of Bangladesh's independence. It is an indispensable landmark that combines national history, modern architecture, and deep emotional resonance.",
            "descBn": "টুঙ্গিপাড়ায় অবস্থিত বঙ্গবন্ধু শেখ মুজিবুর রহমান সমাধি সৌধ কমপ্লেক্স বাংলাদেশের অন্যতম প্রধান জাতীয় তীর্থ ও ঐতিহাসিক স্মারক, যেখানে সমাহিত আছেন স্বাধীন বাংলাদেশের স্থপতি জাতির পিতা বঙ্গবন্ধু শেখ মুজিবুর রহমান। লাল সিরামিক ইট, শুভ্র মার্বেল পাথর এবং কাঁচের নান্দনিক গম্বুজের সমন্বয়ে নির্মিত এই সমাধি সৌধটি গভীর ভাবগাম্ভীর্য ও আধুনিক স্থাপত্যের প্রতীক। প্রায় ৩৮ একর এলাকা জুড়ে বিস্তৃত এই কমপ্লেক্সে রয়েছে বঙ্গবন্ধুর পৈতৃক ভিটা, সমৃদ্ধ জাদুঘর, মুক্তিযুদ্ধ কর্নার, গবেষণাগার ও পদ্মপুকুরবেষ্টিত নয়নাভিরাম বাগান। প্রতি বছর দেশের সর্বস্তরের জনগণ এবং বিদেশি অতিথিরা এখানে শ্রদ্ধা নিবেদন করতে আসেন। বাংলাদেশের স্বাধীনতা ও আত্মপরিচয়ের ইতিহাস জানতে এটি এক অনন্য স্থান।",
            "locationEn": g_raw['hist_spots'][0]['location'],
            "locationBn": "টুঙ্গিপাড়া, গোপালগঞ্জ",
            "mapUrl": g_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Orakandi Thakur Bari",
            "nameBn": "ওড়াকান্দি ঠাকুর বাড়ি",
            "categoryEn": "Sacred Religious Pilgrimage Site",
            "categoryBn": "পবিত্র ধর্মীয় তীর্থধাম",
            "descEn": "Orakandi Thakur Bari in Kashiani Upazila is the revered spiritual capital of the worldwide Matua community, founded by Harichand Thakur in the early nineteenth century. Preaching equality, human dignity, and devotion beyond social caste barriers, the holy site preserves ancestral shrines, prayer mandirs, and the sacred 'Kamana Sagar' holy pond. During the annual Baruni Snan and fair in spring, hundreds of thousands of Matua devotees congregate to take ritual holy dips in the waters and sing heartfelt spiritual hymns. The peaceful rural setting, flanked by age-old banyans and historic temples, radiates profound spiritual devotion and social history. The site stands as a monument to progressive spiritual reform and communal brotherhood in Bengal.",
            "descBn": "কাশিয়ানী উপজেলার ওড়াকান্দি ঠাকুর বাড়ি বিশ্বব্যাপী মতুয়া সম্প্রদায়ের এক পরম পবিত্র মহাতীর্থ, যা উনিশ শতকে সমাজসংস্কারক ও ধর্মগুরু শ্রীশ্রী হরিচাঁদ ঠাকুর কর্তৃক প্রতিষ্ঠিত হয়েছিল। জাতপাতহীন সাম্য ও মানবতার বাণী প্রচারকারী এই পুণ্যভূমিতে রয়েছে শতাব্দীপ্রাচীন নাটমন্দির, সমাধি মন্দির এবং পবিত্র 'কামনা সাগর' দীঘি। প্রতি বছর চৈত্র মাসে বারুণী স্নান ও মহামেলা উপলক্ষে ভারত ও বাংলাদেশের লাখ লাখ মতুয়া ভক্ত এখানে পুণ্যস্নান ও কীর্তনে অংশ নিতে সমবেত হন। সুপ্রাচীন বৃক্ষরাজি ও ভক্তিপূর্ণ পরিবেশে ঘেরা ওড়াকান্দি ঠাকুর বাড়ি সমাজ সংস্কার ও আধ্যাত্মিক পুনর্জাগরণের এক ঐতিহাসিক স্মারক হিসেবে সমাদৃত।",
            "locationEn": g_raw['hist_spots'][1]['location'],
            "locationBn": "ওড়াকান্দি, কাশিয়ানী, গোপালগঞ্জ",
            "mapUrl": g_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Ulpur Zamindar Bari",
            "nameBn": "উলপুর জমিদার বাড়ি",
            "categoryEn": "Colonial Palatial Estate",
            "categoryBn": "উপনিবেশিক জমিদারি রাজপ্রাসাদ",
            "descEn": "Ulpur Zamindar Bari in Gopalganj Sadar is an extensive eighteenth-century aristocratic palace complex constructed by the prominent Basu Roy Chowdhury zamindar dynasty. Originally encompassing over a dozen individual multi-storied palaces, courtyards, and administrative offices, several majestic brick mansions still survive today amidst serene rural surroundings. The surviving structures exhibit classical European neoclassical elements, including fluted Corinthian columns, arched windows, and decorative lime-mortar parapets. Adjoining the palaces are ancient stepped bathing tanks, family temples, and paved avenues that once echoed with horse-drawn carriages and musical soirees. Walking through the quiet paths of Ulpur offers an evocative glimpse into the feudal splendor of old Bengal.",
            "descBn": "গোপালগঞ্জ সদর উপজেলার উলপুর গ্রামে অবস্থিত উলপুর জমিদার বাড়ি অষ্টাদশ শতাব্দীর এক সুবিশাল ও ঐতিহাসিক সামন্তযুগীয় প্রাসাদ কমপ্লেক্স, যা বসু রায় চৌধুরী জমিদার বংশ কর্তৃক নির্মিত হয়েছিল। তৎকালীন সময়ে এক ডজনেরও বেশি সুরম্য দোতলা ও তেতলা ভবন নিয়ে গঠিত এই জমিদারি এলাকার বেশ কয়েকটি প্রাসাদ আজও কালের সাক্ষী হয়ে দাঁড়িয়ে আছে। ইউরোপীয় নিও-ক্লাসিক্যাল স্থাপত্যশৈলীতে নির্মিত এই ভবনগুলোর খিলানযুক্ত প্রবেশপথ, অলংকৃত স্তম্ভ ও কারুকার্যময় ছাদ নজরকাড়া। প্রাসাদের সন্নিকটে রয়েছে প্রাচীন শানবাঁধানো দীঘি ও পূজামণ্ডপ, যা জমিদারদের সমৃদ্ধ অতীতের সাক্ষ্য বহন করে। ইতিহাসপ্রেমীদের কাছে উলপুরের এই প্রাচীন প্রাসাদগুলো অত্যন্ত আকর্ষণীয়।",
            "locationEn": g_raw['hist_spots'][2]['location'],
            "locationBn": "উলপুর, গোপালগঞ্জ সদর, গোপালগঞ্জ",
            "mapUrl": g_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Kotalipara Archaeological Area",
            "nameBn": "কোটালীপাড়া প্রত্নতাত্ত্বিক এলাকা",
            "categoryEn": "Ancient Fortified Settlement & Archaeological Site",
            "categoryBn": "প্রাচীন দুর্গ ও প্রত্নতাত্ত্বিক এলাকা",
            "descEn": "The Kotalipara Archaeological Area is an ancient fortified settlement dating back to the sixth to eighth centuries AD during the independent Vanga Kingdom and Chandra dynastic periods. Historical excavations revealed defensive earthen ramparts, ancient brick fortifications, and rare copperplate inscriptions that documented ancient trade and administrative boundaries. The area once served as a prominent inland river port and political capital protected by intricate canal networks and water fortresses. While many earthen ramparts have merged into surrounding greenery and lotus beels, the archaeological landscape holds immense value for scholars exploring early medieval Bengal. Exploring the undulating terrain connects visitors with the earliest urban roots of the southern delta.",
            "descBn": "কোটালীপাড়া প্রত্নতাত্ত্বিক এলাকা গোপালগঞ্জের এক সুপ্রাচীন ঐতিহাসিক ও দুর্গনগরী এলাকা, যার ইতিহাস ষষ্ঠ থেকে অষ্টম শতাব্দীর স্বাধীন বঙ্গ রাজ্য এবং চন্দ্র রাজবংশের গৌরবময় যুগের সাথে জড়িত। বিভিন্ন গবেষণায় এখানে প্রাচীন মাটির তৈরি প্রতিরক্ষা দুর্গপ্রাচীর, প্রাচীন ইটের নিদর্শন ও তাম্রশাসনের সন্ধান মিলেছে, যা তৎকালীন সমৃদ্ধ শাসনব্যবস্থার প্রমাণ দেয়। নদী ও খালের প্রাকৃতিক প্রতিরক্ষায় ঘেরা এই এলাকাটি সে যুগে এক গুরুত্বপূর্ণ নৌঘাঁটি ও বাণিজ্য কেন্দ্র হিসেবে ব্যবহৃত হতো। যদিও প্রাচীন দুর্গের বহু অংশ আজ বিলুপ্ত, তবুও এর ঐতিহাসিক গুরুত্ব ও প্রত্নতাত্ত্বিক অবশিষ্টাংশ ইতিহাসসন্ধানীদের কাছে অত্যন্ত মূল্যবান। প্রাচীন বাংলার শিকড় খুঁজতে কোটালীপাড়া এক পরম বিস্ময়।",
            "locationEn": g_raw['hist_spots'][3]['location'],
            "locationBn": "কোটালীপাড়া, গোপালগঞ্জ",
            "mapUrl": g_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Madhumati River Historic Settlements",
            "nameBn": "মধুমতী নদীর ঐতিহাসিক জনপদ",
            "categoryEn": "Historic Riverside Heritage Corridor",
            "categoryBn": "ঐতিহাসিক নদীমাতৃক জনপদ ও নৌ ঐতিহ্য",
            "descEn": "The historic riverside settlements flanking the Madhumati River in Gopalganj represent centuries of continuous riverine commerce, boatbuilding traditions, and folk settlements. Originating as strategic trade routes connecting central Bengal to the coastal Sundarbans, the riverbanks feature old brick trading posts, traditional ghats, and fishing communities. Folk literature and songs from this basin celebrate the timeless rhythm of boatmen singing Bhatiali tunes under wide delta skies. Ancient trees line the water's edge alongside colonial-era wooden bazaars where fresh river catches and local sweets are traded daily. Traveling along these riverside settlements reveals the living cultural artery that shaped the identity and history of Gopalganj.",
            "descBn": "গোপালগঞ্জের বুক চিরে প্রবাহিত মধুমতী নদীর দুই তীরের ঐতিহাসিক জনপদ শতাব্দীর পর শতাব্দী ধরে নদীভিত্তিক বাণিজ্য, ঐতিহ্যবাহী নৌকা নির্মাণ ও গ্রামীণ সংস্কৃতির কেন্দ্র হিসেবে গড়ে উঠেছে। প্রাচীনকালে মধুমতী নদী মধ্য বাংলার সাথে সুন্দরবন উপকূলীয় অঞ্চলের অন্যতম প্রধান বাণিজ্যপথ হিসেবে ব্যবহৃত হতো। নদীর তীরবর্তী প্রাচীন ঘাট, পুরোনো বাজার ও জেলে পল্লীগুলো আজও নদীমাতৃক জীবনের ঐতিহ্য ধরে রেখেছে। ভাটিয়ালি গানের সুর আর মাঝি-মাল্লাদের জীবনসংগ্রাম এই জনপদের সাহিত্য ও সংস্কৃতিতে অমর হয়ে আছে। মধুমতীর কোল ঘেঁষে গড়ে ওঠা এই ঐতিহাসিক বসতিগুলো ভ্রমণ করলে বাংলার চিরন্তন রূপ ও ঐতিহ্যের সান্নিধ্য পাওয়া যায়।",
            "locationEn": g_raw['hist_spots'][4]['location'],
            "locationBn": "মধুমতী নদীর তীরবর্তী অঞ্চল, গোপালগঞ্জ",
            "mapUrl": g_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Savana Eco Park and Resort",
            "nameBn": "সাভানা ইকো পার্ক অ্যান্ড রিসোর্ট",
            "categoryEn": "Modern Eco Resort & Recreation Park",
            "categoryBn": "আধুনিক ইকো পার্ক ও বিনোদন কেন্দ্র",
            "descEn": "Savana Eco Park and Resort in Sahapur Union of Gopalganj Sadar is an expansive recreation and ecological retreat designed for family outings and nature relaxation. Spread over sprawling acreage, the park features ornamental lakes, pedal boating facilities, lush botanical gardens, and shaded walking avenues. Visitors enjoy birdwatching along water reservoirs, relaxing in private lakeside gazebos, and taking in fresh rural air. The facility includes children's amusement zones, dining restaurants serving local delicacies, and modern resort accommodations surrounded by tropical greenery. It has rapidly grown into one of the most popular leisure and recreation landmarks in Gopalganj district.",
            "descBn": "গোপালগঞ্জ সদর উপজেলার সাহাপুর ইউনিয়নে অবস্থিত সাভানা ইকো পার্ক অ্যান্ড রিসোর্ট একটি সুবিশাল ও আধুনিক বিনোদন কেন্দ্র, যা পরিবার-পরিজন নিয়ে অবকাশ যাপনের জন্য অত্যন্ত জনপ্রিয়। বিশাল আয়তনের এই পার্কে রয়েছে দৃষ্টিনন্দন কৃত্রিম লেক, প্যাডেল বোটিং সুবিধা, সুসজ্জিত বোটানিক্যাল গার্ডেন ও ছায়াঘেরা হাঁটার পথ। লেকের জলে জলজ পাখির ওড়াউড়ি এবং শান্ত গ্রামীণ পরিবেশ দর্শনার্থীদের মনকে প্রশান্ত করে তোলে। শিশুদের জন্য আকর্ষণীয় রাইড, সুস্বাদু খাবারের রেস্তোরাঁ এবং আধুনিক রিসোর্ট সুবিধার কারণে ছুটির দিনে এখানে প্রচুর পর্যটক ভিড় জমান। প্রকৃতি ও আধুনিক বিনোদনের সমন্বয়ে এটি গোপালগঞ্জের এক চমৎকার পর্যটন কেন্দ্র।",
            "locationEn": g_raw['tour_spots'][0]['location'],
            "locationBn": "সাহাপুর ইউনিয়ন, গোপালগঞ্জ সদর, গোপালগঞ্জ",
            "mapUrl": g_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Madhumati Riverbank",
            "nameBn": "মধুমতী নদীতীর",
            "categoryEn": "Scenic Riverside Promenade",
            "categoryBn": "নয়নাভিরাম নদীতীর ও সূর্যাস্ত ভিউপয়েন্ট",
            "descEn": "The Madhumati Riverbank provides an enchanting natural haven where clear river waters flow serenely past palm-fringed villages and lush mustard fields. Riverfront walkways developed along the urban and rural sections allow tourists to enjoy peaceful evening strolls, gentle breezes, and picturesque views of wooden country boats. During late afternoons, the river surface shimmers with golden hues as the sun descends behind the tree lines across the opposite bank. Local waterfront stalls offer steaming tea, fresh village snacks, and local river fish dishes right beside the water. It represents the quintessential natural landscape of Gopalganj, offering timeless peace and refreshing open spaces.",
            "descBn": "মধুমতী নদীতীর গোপালগঞ্জের প্রকৃতির এক অপার সৌন্দর্যপীঠ, যেখানে শান্ত নদীপ্রবাহ গ্রামীণ সবুজ ও তালগাছের সারির বুক চিরে এঁকেবেঁকে বয়ে চলেছে। নদীর পাড়ে তৈরি করা বাঁধ ও ওয়াকওয়ে দিয়ে হাঁটার সময় দখিনা হাওয়া দর্শনার্থীদের মন জুড়িয়ে দেয়। বিকেলে নদীর বুকে কাঠের নৌকার মন্থর গতি এবং পানিতে সূর্যের রক্তিম আভার ঝিলিক এক স্বর্গীয় অনুভূতি সৃষ্টি করে। নদীতীরের চায়ের দোকানগুলোতে বসে গরম চা ও স্থানীয় মুখরোচক খাবার উপভোগ করতে বহু মানুষ বিকেলে এখানে জড়ো হন। কোলাহলমুক্ত শান্ত পরিবেশে নদীর আসল রূপ উপভোগ করতে মধুমতীর পাড় ভ্রমণকারীদের প্রিয় একটি স্থান।",
            "locationEn": g_raw['tour_spots'][1]['location'],
            "locationBn": "গোপালগঞ্জ নদীতীরবর্তী এলাকা, গোপালগঞ্জ",
            "mapUrl": g_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Ulpur Dighi",
            "nameBn": "উলপুর দীঘি",
            "categoryEn": "Historic Water Reservoir & Birdwatching Lake",
            "categoryBn": "ঐতিহাসিক জলাধার ও প্রাকৃতিক দীঘি",
            "descEn": "Ulpur Dighi is a magnificent historical lake excavated alongside the zamindari palace complex in Ulpur to supply fresh water to the royal estate and local villagers. Flanked by ancient coconut palms and banyan canopies, the crystal-clear water reflects the surrounding historic architecture and open sky. In the winter season, flocks of migratory aquatic birds settle on its serene waters, creating a delightful scene for nature enthusiasts. Anglers frequently cast their lines along the grassy shores, while visitors find quiet solace sitting on the stone steps of the old ghats. Its combination of historic heritage and serene natural tranquility makes it a beloved local escape.",
            "descBn": "ঐতিহাসিক উলপুর জমিদার বাড়ি সংলগ্ন উলপুর দীঘি গোপালগঞ্জের এক দৃষ্টিনন্দন ও সুবিশাল প্রাচীন জলাধার, যা শত শত বছর ধরে তার স্নিগ্ধ রূপ নিয়ে বেঁচে আছে। দীঘির স্বচ্ছ জলরাশি এবং পাড়ঘেরা নারকেল ও বটের ছায়া এক অপার্থিব শান্তিময় পরিবেশ তৈরি করে। শীতকালে এই দীঘিতে অতিথি পাখির আগমন ঘটে, যা দেখতে পাখিপ্রেমীরা ভিড় জমান। দীঘির প্রাচীন শানবাঁধানো ঘাটে বসে অলস সময় কাটানো কিংবা শান্ত জলের দিকে তাকিয়ে থাকা যে কোনো ভ্রমণপিপাসুকে মানসিক প্রশান্তি এনে দেয়। জমিদার বাড়ির ইতিহাস ঘুরে দেখার পাশাপাশি এই দীঘির পাড়ে বিশ্রাম নেওয়া পর্যটকদের জন্য এক দারুণ অভিজ্ঞতা।",
            "locationEn": g_raw['tour_spots'][2]['location'],
            "locationBn": "উলপুর, গোপালগঞ্জ সদর, গোপালগঞ্জ",
            "mapUrl": g_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Tungipara Mausoleum Gardens",
            "nameBn": "টুঙ্গিপাড়া সমাধি সৌধ উদ্যান",
            "categoryEn": "Landscaped Memorial Park & Botanical Grounds",
            "categoryBn": "সুবিন্যস্ত স্মৃতি উদ্যান ও বোটানিক্যাল চত্বর",
            "descEn": "The Tungipara Mausoleum Gardens encompass the beautifully landscaped surrounding grounds of the Bangabandhu Memorial Complex, planned with meticulous ecological care. The gardens feature velvet-like green lawns, ornamental flower beds with seasonal blossoms, weeping willows, and serene lotus ponds traversed by paved walkways. Visitors enjoy tranquil walks along wide tree-lined boulevards where birds sing amid tranquil surroundings. The gardens provide a soothing, reverent setting that complements the emotional gravity of the mausoleum while offering green open spaces for quiet reflection. It is considered one of the finest maintained public landscaped gardens in Bangladesh.",
            "descBn": "বঙ্গবন্ধু সমাধি সৌধ কমপ্লেক্সের অন্তর্ভুক্ত টুঙ্গিপাড়া সমাধি সৌধ উদ্যান অত্যন্ত পরিপাটি ও নান্দনিকভাবে সাজানো এক সুবিশাল বোটানিক্যাল পার্ক। মখমলের মতো সবুজ ঘাসের লন, বর্ণিল ফুলের বাগান, সুদৃশ্য পদ্মপুকুর ও ছায়াঘেরা পথ এই চত্বরটিকে অপূর্ব স্নিগ্ধতায় ভরিয়ে রেখেছে। সমাধি সৌধ দর্শনের পর দর্শনার্থীরা এই সুবিন্যস্ত উদ্যানে শান্ত পদচারণা করে মানসিক প্রশান্তি লাভ করেন। পাখির কলকাকলি এবং পরিচ্ছন্ন শান্তিময় পরিবেশ এটিকে বাংলাদেশের অন্যতম সেরা ও সুসংরক্ষিত পাবলিক উদ্যানে পরিণত করেছে। জাতীয় শ্রদ্ধাবোধ ও প্রকৃতির চমৎকার সমন্বয় এই বাগানে ফুটে উঠেছে।",
            "locationEn": g_raw['tour_spots'][3]['location'],
            "locationBn": "টুঙ্গিপাড়া, গোপালগঞ্জ",
            "mapUrl": g_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Gopalganj Town Lake and Park Area",
            "nameBn": "গোপালগঞ্জ শহর লেক ও পার্ক এলাকা",
            "categoryEn": "Urban Lake Promenade & Civic Park",
            "categoryBn": "পৌর লেক ওয়াকওয়ে ও বিনোদন পার্ক",
            "descEn": "Located in the heart of Gopalganj district headquarters, the Town Lake and Park Area serves as the urban green sanctuary and recreational hub of the municipality. The scenic lake is encircled by paved jogging tracks, illuminated lamp posts, garden benches, and colorful flower beds that attract families and fitness enthusiasts. In the evenings, gentle breezes ripple across the water as fountains play under decorative lighting, creating an inviting public ambiance. Boating facilities on the lake provide fun for children and youth, while nearby cafeterias offer refreshing snacks. It is an essential urban recreational spot offering leisure and relaxation for visitors and town residents alike.",
            "descBn": "গোপালগঞ্জ জেলা শহরের কেন্দ্রস্থলে অবস্থিত শহর লেক ও পার্ক এলাকা স্থানীয় নাগরিক ও পর্যটকদের জন্য এক প্রধান মুক্ত বিনোদন কেন্দ্র। মনোরম এই লেকের চারপাশে রয়েছে শানবাঁধানো হাঁটার রাস্তা, বসার বেঞ্চ, রঙিন ফুলের বাগান ও সন্ধ্যার মনোরম আলোকসজ্জা। বিকেলে ও সন্ধ্যায় লেকের মিষ্টি হাওয়া উপভোগ করতে এবং পরিবারের সদস্যদের নিয়ে সময় কাটাতে প্রচুর মানুষ এখানে সমবেত হন। লেকের জলে বোটিং করার সুযোগ এবং শিশুদের জন্য খেলার জায়গা এই পার্কটিকে আরও প্রাণবন্ত করে তুলেছে। শহরের কোলাহল থেকে মুক্ত হয়ে সুন্দর কিছুটা সময় কাটানোর জন্য এটি এক দারুণ স্থান।",
            "locationEn": g_raw['tour_spots'][4]['location'],
            "locationBn": "গোপালগঞ্জ পৌর এলাকা, গোপালগঞ্জ",
            "mapUrl": g_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('gopalganj', gopalganj_data)

# ==========================================
# 3. HABIGANJ
# ==========================================
h_raw = all_data['habiganj']
habiganj_data = {
    "slug": "habiganj",
    "en": "Habiganj",
    "bn": "হবিগঞ্জ",
    "hero_title_en": "Habiganj Tea Valleys & Pristine Wildlife Sanctuaries",
    "hero_title_bn": "হবিগঞ্জের চাবাগান, বনাঞ্চল ও হাওর প্রকৃতি",
    "hero_sub_en": "Verdant rainforests at Satchari and Rema-Kalenga, historic Sultanate mosques, and the world's largest village at Baniachong.",
    "hero_sub_bn": "সাতছড়ি ও রেমা-কালেঙ্গার ঘন সবুজ রেইনফরেস্ট, সুলতানি আমলের শঙ্করপাশা মসজিদ ও বানিয়াচংয়ের সুবিশাল হাওর।",
    "tagline_en": "A lush borderland district in northeastern Sylhet division, renowned for dense tropical wildlife sanctuaries, rolling green tea estates, and immense haor wetlands.",
    "tagline_bn": "সিলেট বিভাগের চা ও বনাঞ্চলসমৃদ্ধ এক রূপময় জেলা, যা সাতছড়ি ও রেমা-কালেঙ্গা জাতীয় উদ্যান, শঙ্করপাশা শাহী মসজিদ ও বানিয়াচংয়ের হাওর সংস্কৃতির জন্য খ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/habiganj/carousel-1.webp",
            "titleEn": "Satchari National Park Dense Canopy",
            "titleBn": "সাতছড়ি জাতীয় উদ্যানের সবুজ বনাঞ্চল",
            "subtitleEn": "Pristine mixed evergreen rainforest famous for rare wildlife trails and hanging tree canopy walkways",
            "subtitleBn": "চুনারুঘাটের চিরসবুজ সংরক্ষিত বন যা দুর্লভ উল্লুক, চশমা পরা হনুমান ও বুনো পাখির স্বর্গরাজ্য"
        },
        {
            "id": 2,
            "image": "images/districts/habiganj/carousel-2.webp",
            "titleEn": "Rema-Kalenga Wildlife Sanctuary Wilderness",
            "titleBn": "রেমা-কালেঙ্গা বন্যপ্রাণী অভয়ারণ্য",
            "subtitleEn": "Tarap Hill Reserve forest harboring diverse flora, fauna, and indigenous Tipra tribal heritage",
            "subtitleBn": "ভারতের ত্রিপুরা সীমান্তবর্তী গভীর অরণ্য যেখানে জীববৈচিত্র্য ও আদিবাসী সংস্কৃতি জীবন্ত"
        },
        {
            "id": 3,
            "image": "images/districts/habiganj/carousel-3.webp",
            "titleEn": "Shankarpasha Shahi Mosque Red Brick Heritage",
            "titleBn": "শঙ্করপাশা শাহী মসজিদের লাল ইটের রূপ",
            "subtitleEn": "15th-century Sultanate brick architecture embellished with delicate terracotta floral patterns",
            "subtitleBn": "পঞ্চদশ শতাব্দীর সুলতানি আমলের চার গম্বুজ বিশিষ্ট অনন্য মসজিদ যা মনোমুগ্ধকর টেরাকোটায় সাজানো"
        },
        {
            "id": 4,
            "image": "images/districts/habiganj/carousel-4.webp",
            "titleEn": "Chunarughat Rolling Green Tea Estates",
            "titleBn": "চুনারুঘাটের দিগন্তজোড়া চা বাগান",
            "subtitleEn": "Endless undulating carpets of emerald tea bushes framed by shade-giving rain trees",
            "subtitleBn": "সবুজ পাহাড়ের খাঁজে খাঁজে বিছানো সতেজ চা পাতার মায়াবী সমারোহ ও শান্ত পাহাড়ি পথ"
        },
        {
            "id": 5,
            "image": "images/districts/habiganj/carousel-5.webp",
            "titleEn": "Baniachong Haor Boundless Water Horizon",
            "titleBn": "বানিয়াচং হাওরের দিগন্তবিস্তৃত জলরাশি",
            "subtitleEn": "Vast monsoon inland sea supporting traditional wetland fisheries and dramatic sky reflections",
            "subtitleBn": "বর্ষায় সাগরের মতো উত্তাল হাওরের বিস্তার ও জেলেদের ঐতিহ্যবাহী জীবনচিত্র"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Baniachong Zamindar Bari Area",
            "nameBn": "বানিয়াচং জমিদার বাড়ি এলাকা",
            "categoryEn": "Historic Medieval Estate & Settlement",
            "categoryBn": "ঐতিহাসিক জমিদারি জনপদ ও ধ্বংসাবশেষ",
            "descEn": "Baniachong is celebrated globally as one of the largest villages on earth, and its historic Zamindar Bari area was once the fortified political hub of Raja Gobinda Dev and prominent medieval feudal rulers. Established during the pre-Mughal era amidst the sprawling haor wetlands, the estate featured moated defensive waterways, brick courtyards, and palatial living chambers. The rulers governed a flourishing semi-autonomous territory known for rich fisheries, paddy cultivation, and regional self-defense. Today, surviving brick foundations, historic dighis like Kamalranir Dighi, and local oral legends provide rich historical texture to the village landscape. Visiting Baniachong offers an extraordinary look into how medieval Bengali settlements engineered life in seasonal wetland environments.",
            "descBn": "বানিয়াচং এশিয়ার তথা বিশ্বের বৃহত্তম গ্রাম হিসেবে সুপরিচিত, এবং এখানকার ঐতিহাসিক জমিদার বাড়ি এলাকা এককালে রাজা গোবিন্দ দেব ও মধ্যযুগীয় শাসকদের ক্ষমতাশালী দুর্গনগরী ছিল। হাওরাঞ্চলের বুকে সুরক্ষিত এই জমিদারি বসতিতে ছিল পরিখা বেষ্টিত জলদুর্গ, সুদৃঢ় ইটের প্রাসাদ ও বিচারালয়। মধ্যযুগে এই স্বাধীন জমিদাররা সুবিশাল অঞ্চল শাসন করতেন যা মাছ, ধান ও জলপথ বাণিজ্যে সমৃদ্ধ ছিল। বর্তমানে প্রাসাদের প্রাচীন ধ্বংসাবশেষ, কমলা রানীর ঐতিহাসিক দীঘি ও লোকগাথা এই এলাকার গৌরবময় স্মৃতি বহন করে। বিশাল এই গ্রামের প্রাচীন জমিদারি জনপদ ঘুরে দেখা ইতিহাসপ্রেমীদের জন্য এক রোমাঞ্চকর অভিজ্ঞতা।",
            "locationEn": h_raw['hist_spots'][0]['location'],
            "locationBn": "বানিয়াচং, হবিগঞ্জ",
            "mapUrl": h_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Murari Chand College Historic Campus (Historic Heritage Site)",
            "nameBn": "ঐতিহাসিক বিদ্যাপীঠ ও প্রাচীন ঐতিহ্য চত্বর",
            "categoryEn": "Colonial-Era Educational Landmark",
            "categoryBn": "উপনিবেশিক শিক্ষাঙ্গন ও স্থাপত্যিক ঐতিহ্য",
            "descEn": "Associated with the historic intellectual awakening of the Surma-Kushiyara basin, this heritage educational campus in Habiganj town represents over a century of academic prominence. Founded during the late colonial period to provide modern collegiate instruction to regional students, the compound features classical brick administrative halls, colonnaded corridors, and tranquil green courtyards. Prominent scholars, freedom fighters, and cultural figures of Bengal walked through these classrooms, cementing its status as an intellectual cradle. The enduring brick architecture with graceful wooden eaves and vaulted windows reflects high colonial design tailored to subtropical weather. It remains a deeply respected institutional landmark that anchors Habiganj's cultural identity.",
            "descBn": "সুরমা ও কুশিয়ারা অববাহিকার শিক্ষা ও নবজাগরণের স্মারক হিসেবে হবিগঞ্জ শহরের এই ঐতিহ্যবাহী বিদ্যাপীঠ চত্বর শতাব্দীপ্রাচীন স্মৃতি বহন করে। উনিশ শতকের শেষভাগে প্রতিষ্ঠিত এই শিক্ষাপ্রতিষ্ঠানটি এ অঞ্চলের আধুনিক জ্ঞানচর্চার প্রধান বাতিঘর হিসেবে কাজ করেছে। লাল ইটের উপনিবেশিক স্থাপত্য, সুউচ্চ খিলানযুক্ত বারান্দা এবং বিশাল সবুজ মাঠ একে এক বিশেষ আভিজাত্য দান করেছে। বাংলার বহু খ্যাতনামা পণ্ডিত, রাজনীতিবিদ ও সংস্কৃতিকর্মী এই প্রাঙ্গণ থেকে শিক্ষা লাভ করেছেন। প্রাচীন বৃক্ষরাজি ও সুনিবিড় পরিবেশে ঘেরা এই ঐতিহাসিক শিক্ষাঙ্গনটি হবিগঞ্জের শিক্ষা-সংস্কৃতির অন্যতম গর্ব।",
            "locationEn": h_raw['hist_spots'][1]['location'],
            "locationBn": "হবিগঞ্জ শহর, হবিগঞ্জ",
            "mapUrl": h_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Shankarpasha Shahi Mosque",
            "nameBn": "শঙ্করপাশা শাহী মসজিদ",
            "categoryEn": "Sultanate Architectural Masterpiece",
            "categoryBn": "সুলতানি আমলের স্থাপত্যিক শাহী মসজিদ",
            "descEn": "Erected in the late fifteenth century during the Sultanate era of Bengal, Shankarpasha Shahi Mosque in Lakhai Upazila is a dazzling gem of pre-Mughal terracotta brick architecture. The monument features a grand central dome flanked by three smaller companion domes resting atop thick, seasoned red-brick masonry. The entire exterior surface is adorned with exquisite floral rosettes, hanging chain motifs, and geometric terracotta reliefs reflecting the artistic zenith of Sultan Alauddin Husain Shah's reign. Inside, a beautifully carved stone mihrab directs the prayers, surrounded by arched niches and serene natural acoustics. Preserved carefully amid quiet rural groves, it represents one of the finest surviving architectural monuments in northeastern Bangladesh.",
            "descBn": "লাখাই উপজেলার শঙ্করপাশা গ্রামে অবস্থিত শঙ্করপাশা শাহী মসজিদটি প্রাক-মুঘল সুলতানি আমলের লাল ইটের তৈরি এক অনিন্দ্যসুন্দর স্থাপত্যকীর্তি। পঞ্চদশ শতাব্দীর শেষভাগে সুলতান আলাউদ্দিন হোসেন শাহের আমলে নির্মিত এই মসজিদে রয়েছে একটি মূল বৃহৎ গম্বুজ ও তিনটি ক্ষুদ্রতর গম্বুজ। মসজিদের বহির্দেয়ালে পোড়ামাটির অপূর্ব লতাপাতা, ঝুলন্ত শিকল ও ফুলের নকশা খোদাই করা রয়েছে যা মধ্যযুগীয় বাংলার কারুশিল্পের শ্রেষ্ঠত্ব প্রমাণ করে। ভেতরের মার্জিত মেহরাব ও শীতল পরিবেশ মুসল্লি ও দর্শনার্থীদের গভীর প্রশান্তি এনে দেয়। সবুজ প্রকৃতির মাঝে লাল ইটের এই প্রাচীন মসজিদটি বাংলার সুলতানি ঐতিহ্যের এক অমূল্য সম্পদ।",
            "locationEn": h_raw['hist_spots'][2]['location'],
            "locationBn": "শঙ্করপাশা, লাখাই, হবিগঞ্জ",
            "mapUrl": h_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Nabiganj Historic Zamindar-House Area",
            "nameBn": "নবীগঞ্জ ঐতিহাসিক জমিদার বাড়ি এলাকা",
            "categoryEn": "Feudal Heritage Estate",
            "categoryBn": "ঐতিহাসিক জমিদারি আবাস ও প্রত্নস্থল",
            "descEn": "The Nabiganj Historic Zamindar-House Area encompasses the surviving residential estates and administrative centers of prominent landlords who held sway across the northern reaches of Habiganj. Dating primarily to the late eighteenth and nineteenth centuries, these compounds feature imposing entrance gateways, classical reception halls, and secluded inner zenana quarters. The architecture demonstrates traditional lime-mortar craftsmanship mixed with colonial porticos, decorated wrought-iron railings, and large stepped dighis. Though parts of the mansions now stand in melancholic ruins overgrown with climbing ivy, they narrate fascinating chapters of regional agrarian commerce and tax governance. Heritage travelers find these quiet ruins an evocative window into the rural feudal past.",
            "descBn": "নবীগঞ্জ উপজেলার ঐতিহাসিক জমিদার বাড়ি এলাকা হবিগঞ্জের উত্তরাঞ্চলের একসময়ের প্রভাবশালী জমিদারদের স্মৃতিবাহী এক প্রাচীন জনপদ। অষ্টাদশ ও উনিশ শতকে নির্মিত এই জমিদারি ভবনগুলোতে ছিল সুরম্য সিংহদ্বার, জলসাঘর, কাচারিবাড়ি ও অন্দরমহল। চুন-সুরকির মজবুত গাঁথুনি, অলংকৃত লোহার রেলিং ও বিশাল শানবাঁধানো দীঘি তৎকালীন জমিদারদের আড়ম্বরপূর্ণ জীবনযাত্রার কথা স্মরণ করিয়ে দেয়। কালের পরিক্রমায় প্রাসাদের অনেক অংশ আজ ধ্বংসাবশেষে পরিণত হলেও এর কারুকার্যময় দেয়াল ও স্তম্ভ পর্যটকদের নস্টালজিক করে তোলে। প্রাচীন স্থাপত্য ও গ্রামীণ ইতিহাসের সন্ধানে নবীগঞ্জের এই স্থানটি অত্যন্ত তাৎপর্যপূর্ণ।",
            "locationEn": h_raw['hist_spots'][3]['location'],
            "locationBn": "নবীগঞ্জ, হবিগঞ্জ",
            "mapUrl": h_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Lakhai Historic Mosque and Shrine Sites",
            "nameBn": "লাখাই ঐতিহাসিক মসজিদ ও দরবার এলাকা",
            "categoryEn": "Sacred Historical Sanctuary",
            "categoryBn": "ঐতিহাসিক ধর্মীয় স্থান ও দরগাহ",
            "descEn": "Situated along the historic waterways of Lakhai Upazila, these centuries-old mosques and Sufi shrine sites bear witness to the early propagation of spiritual teachings and community life in Habiganj. Built originally during the medieval era near river junctions, the sanctuaries feature ancient brick domes, decorative arched gateways, and shaded courtyards shaded by venerable tamarind trees. Pilgrims and seekers have visited these peaceful shrines across generations to pray for healing, guidance, and peace amid life's trials. The complex preserves antique calligraphic inscriptions, water reservoirs, and centuries-old burial grounds of revered Sufi darweshes. Visiting Lakhai provides a deeply reflective encounter with the syncretic spiritual roots of the Sylhet basin.",
            "descBn": "লাখাই উপজেলার নদীবিধৌত অঞ্চলে অবস্থিত ঐতিহাসিক মসজিদ ও মাজার প্রাঙ্গণ হবিগঞ্জের প্রাচীন সুফি ঐতিহ্য ও ধর্মীয় সংস্কৃতির অন্যতম প্রাণকেন্দ্র। মধ্যযুগে বিভিন্ন সুফি সাধক ও আউলিয়াদের হাত ধরে গড়ে ওঠা এই উপাসনালয়গুলোতে রয়েছে প্রাচীন গম্বুজ, খিলানযুক্ত প্রবেশপথ এবং ছায়াঘেরা শান্ত পরিবেশ। যুগ যুগ ধরে ধর্মপ্রাণ মানুষ আধ্যাত্মিক প্রশান্তি ও দোয়ার উদ্দেশ্যে এই পবিত্র স্থানগুলোতে আগমন করেন। মাজার প্রাঙ্গণে থাকা প্রাচীন শিলালিপি ও জলাশয়গুলো অতীতের আধ্যাত্মিক চেতনার নীরব সাক্ষী হয়ে রয়েছে। গ্রামীণ শান্তিময় পরিবেশে সুফি দর্শনের গভীর অনুভূতি পেতে লাখাইয়ের এই ঐতিহাসিক স্থানটি অনন্য।",
            "locationEn": h_raw['hist_spots'][4]['location'],
            "locationBn": "লাখাই, হবিগঞ্জ",
            "mapUrl": h_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Rema-Kalenga Wildlife Sanctuary",
            "nameBn": "রেমা-কালেঙ্গা বন্যপ্রাণী অভয়ারণ্য",
            "categoryEn": "Dense Tropical Rainforest Sanctuary",
            "categoryBn": "গভীর রেইনফরেস্ট ও বন্যপ্রাণী অভয়ারণ্য",
            "descEn": "Rema-Kalenga Wildlife Sanctuary in Chunarughat is the second-largest natural reserve forest in Bangladesh, protecting an astonishing expanse of pristine mixed evergreen hill forest along the Indian border. Home to endangered hoolock gibbons, slow lorises, capped langurs, barking deer, and over 160 species of tropical birds, the sanctuary is a world-class ecotourism destination. Trekking along shaded forest trails brings visitors past giant chapalish and teak trees draped in wild lianas, with natural streams babbling through valleys. Canopy observation towers provide breathtaking treetop vistas over miles of emerald wilderness. For adventurous wildlife enthusiasts and hikers, Rema-Kalenga delivers an untamed, authentic jungle experience.",
            "descBn": "চুনারুঘাট উপজেলায় ভারত সীমান্ত ঘেঁষে অবস্থিত রেমা-কালেঙ্গা বন্যপ্রাণী অভয়ারণ্য বাংলাদেশের দ্বিতীয় বৃহত্তম প্রাকৃতিক রেইনফরেস্ট ও বন্যপ্রাণীদের নিরাপদ স্বর্গরাজ্য। প্রায় ১,৭৯৫ হেক্টর আয়তনের এই গভীর চিরসবুজ বনে বাস করে বিলুপ্তপ্রায় সাদা ভ্রু উল্লুক, মুখপোড়া হনুমান, মায়া হরিণ, বুনো শুয়োর এবং শত শত প্রজাতির রঙ-বেরঙের পাখি। বিশালাকার চাপালিশ, গর্জন ও সেগুন গাছের ছায়াঘেরা ট্রেইল ধরে হাঁটার অভিজ্ঞতা প্রকৃতিপ্রেমীদের রোমাঞ্চিত করে। জঙ্গলের মাঝে নির্মিত ওয়াচ টাওয়ার থেকে পুরো অরণ্যের দিগন্তজোড়া রূপ এক পলকে দেখা যায়। রোমাঞ্চকর ট্র্যাকিং ও বন্যপ্রাণী দেখার জন্য এটি বাংলাদেশের অন্যতম সেরা বন।",
            "locationEn": h_raw['tour_spots'][0]['location'],
            "locationBn": "চুনারুঘাট, হবিগঞ্জ",
            "mapUrl": h_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Satchari National Park",
            "nameBn": "সাতছড়ি জাতীয় উদ্যান",
            "categoryEn": "National Wildlife Park & Nature Trail",
            "categoryBn": "জাতীয় উদ্যান ও ইকো ট্র্যাকিং জোন",
            "descEn": "Satchari National Park in Chunarughat is a celebrated biodiversity hotspot nestled within the southern hills of Habiganj, named after the seven pristine freshwater streams that wind through its undulating terrain. The park features well-marked hiking trails ranging from short half-hour walks to rigorous three-hour deep-forest expeditions. Travelers frequently spot playful capped langurs, giant squirrels, and rare hornbills while wandering beneath towering forest canopies. An exhilarating tree canopy walkway and children's eco-learning park add to its appeal for nature-loving families. Satchari stands as one of the most accessible and richly rewarding wildlife exploration destinations in eastern Bangladesh.",
            "descBn": "চুনারুঘাট উপজেলার রঘুনন্দন পাহাড়ে অবস্থিত সাতছড়ি জাতীয় উদ্যান হবিগঞ্জের সবচেয়ে জনপ্রিয় ও সমৃদ্ধ জীববৈচিত্র্যপূর্ণ বন। সাতটি পাহাড়ি ছড়া বা ঝিরি এই বনের বুক চিরে প্রবাহিত হওয়ায় এর নাম হয়েছে 'সাতছড়ি'। এখানে রয়েছে আধা ঘণ্টা, এক ঘণ্টা ও তিন ঘণ্টার চমৎকার ট্র্যাকিং ট্রেইল, যা ধরে হাঁটলে বুনো বানর, চশমা পরা হনুমান, মায়া হরিণ ও ধনেশ পাখির দেখা মেলে। বনের উঁচুতে নির্মিত ক্যানোপি ওয়াকওয়ে ধরে হাঁটার রোমাঞ্চকর অভিজ্ঞতা দর্শনার্থীদের মুগ্ধ করে। পরিবার নিয়ে বনের নির্মল বাতাস ও বন্যপ্রাণীদের সান্নিধ্য পেতে সাতছড়ি এক আদর্শ পরিবেশবান্ধব পর্যটন কেন্দ্র।",
            "locationEn": h_raw['tour_spots'][1]['location'],
            "locationBn": "চুনারুঘাট, হবিগঞ্জ",
            "mapUrl": h_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Chunarughat Tea Gardens",
            "nameBn": "চুনারুঘাটের চা বাগান",
            "categoryEn": "Undulating Tea Valleys & Scenic Estates",
            "categoryBn": "সবুজ চা বাগান ও পাহাড়ি উপত্যকা",
            "descEn": "The Chunarughat Tea Gardens present an endless rolling carpet of emerald-green tea shrubs sweeping across low hill slopes beneath protective rubber and albizia shade trees. Winding paved roads lead travelers through picturesque estates like Chandpore, Amo, and Nalua, where cool fragrant breezes accompany every turn. Visitors can observe skilled tea pluckers carrying woven baskets on their backs while deftly harvesting tender tea leaves during harvest hours. Quiet tea estate bungalows and scenic view-points offer ideal spots for photography, cycling, and unwinding amidst peaceful nature. The verdant slopes create a tranquil visual poetry that epitomizes the romance of Bangladesh's tea country.",
            "descBn": "চুনারুঘাটের পাহাড়ি ঢালে অবস্থিত চা বাগানগুলো সবুজের এক অনন্ত গালিচা বিছিয়ে রেখেছে, যা চোখ জুড়িয়ে দেয়। চান্দপুর, আমু ও নালুয়া চা বাগানের মধ্য দিয়ে চলে যাওয়া সর্পিল পিচঢালা পথ ধরে হাঁটলে বা গাড়ি চালালে স্নিগ্ধ সুবাসিত পাহাড়ি বাতাস মন ভরিয়ে দেয়। নারী চা শ্রমিকদের মাথায় ঝুড়ি বেঁধে নিপুণ হাতে দুটি পাতা একটি কুঁড়ি তোলার দৃশ্য অত্যন্ত মোহনীয়। উঁচু-নিচু টিলার মাঝে ব্রিটিশ আমলের সুরম্য বাংলো এবং শান্ত পরিবেশ আলোকচিত্রীদের জন্য এক পরম স্বর্গ। দৈনন্দিন জীবনের ব্যস্ততা ভুলে সবুজের মাঝে হারিয়ে যেতে চুনারুঘাটের চা বাগান এক অতুলনীয় স্থান।",
            "locationEn": h_raw['tour_spots'][2]['location'],
            "locationBn": "চুনারুঘাট, হবিগঞ্জ",
            "mapUrl": h_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Baniachong Haor",
            "nameBn": "বানিয়াচং হাওর",
            "categoryEn": "Vast Wetland & Monsoon Inland Sea",
            "categoryBn": "বিশাল হাওর জলাভূমি ও বর্ষাকালীন জলপ্রকৃতি",
            "descEn": "Baniachong Haor transforms with the seasons, morphing from vast golden paddy fields in the dry winter months into a breathtaking inland sea during the monsoon. Wooden country boats ferry passengers across wide open waters that mirror cloud-swept skies all the way to distant horizon edges. Travelers love embarking on traditional boat journeys across the gentle waves, savoring fresh fish curries cooked on wooden stoves by local boatmen. In winter, hundreds of thousands of migratory waterfowl feed in the shrinking lagoons, creating an avian paradise for birdwatchers. The sheer scale of water and sky provides an unforgettable taste of Bengal's authentic wetland soul.",
            "descBn": "বানিয়াচং হাওর প্রকৃতির এক অদ্ভুত রূপবদলকারী জলাভূমি, যা শুষ্ক মৌসুমে সবুজ-সোনালী ধানের প্রান্তর এবং বর্ষাকালে এক কূলহীন মহাসমুদ্রে পরিণত হয়। বর্ষায় হাওরের দিগন্তজোড়া উত্তাল জলরাশি আর মেঘভাঙ্গা রোদের খেলা যেন এক জীবন্ত ক্যানভাস তৈরি করে। ইঞ্জিনচালিত কাঠের নৌকায় চড়ে হাওরের বুকে ভেসে বেড়ানো এবং স্থানীয় তাজা মাছের স্বাদ নেওয়া পর্যটকদের এক অভূতপূর্ব রোমাঞ্চ উপহার দেয়। শীতকালে হাওরের বিভিন্ন বিলে হাজার হাজার পরিযায়ী পাখির কলকাকলিতে মুখরিত হয়ে ওঠে পরিবেশ। নদীমাতৃক বাংলার আসল সৌন্দর্য ও হাওর জীবনের রূপ দেখতে বানিয়াচং হাওর এক জাদুকরী গন্তব্য।",
            "locationEn": h_raw['tour_spots'][3]['location'],
            "locationBn": "বানিয়াচং, হবিগঞ্জ",
            "mapUrl": h_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Khowai Riverbank",
            "nameBn": "খোয়াই নদীতীর",
            "categoryEn": "Meandering River Promenade",
            "categoryBn": "নয়নাভিরাম নদীতীর ও কাশফুলের বন",
            "descEn": "The Khowai Riverbank flows gracefully alongside Habiganj town, originating in the Tripura hills and meandering through fertile plains to meet the mighty Kushiyara River. The riverside embankments serve as popular gathering promenades where townspeople and tourists enjoy cooling river breezes and watch twilight reflect upon smooth waters. During autumn, extensive sandbars on the riverbed bloom with wild white kashful reeds that sway gently under clear azure skies. Small wooden canoes glide softly past the ghats, offering short river rides and tranquil photography opportunities. It provides a peaceful, accessible waterfront setting in harmonious companionship with Habiganj's urban life.",
            "descBn": "ভারতের ত্রিপুরা রাজ্য থেকে উৎপন্ন হয়ে হবিগঞ্জ শহরের পাশ দিয়ে বয়ে চলা খোয়াই নদী এ অঞ্চলের এক অত্যন্ত গুরুত্বপূর্ণ ও রূপময় জলধারা। নদীর বাঁধ ঘেঁষে গড়ে ওঠা হাঁটার পথগুলো বিকেলে ভ্রমণপিপাসু ও স্থানীয়দের প্রিয় আড্ডাস্থলে পরিণত হয়। শরৎকালে খোয়াই নদীর চরে ফোটা ধবধবে সাদা কাশফুলের বন এবং নীল আকাশের মেলবন্ধন এক অপরূপ রূপ ধারণ করে। শান্ত নদীর জলে স্থানীয় মাঝিদের নৌকা বেয়ে চলা এবং গোধূলির আলোয় নদীর রূপ যে কাউকে মুগ্ধ করে। শহরের কাছেই নির্মল হাওয়া ও নদীপ্রকৃতি উপভোগ করতে খোয়াই নদীতীর অত্যন্ত জনপ্রিয় একটি স্থান।",
            "locationEn": h_raw['tour_spots'][4]['location'],
            "locationBn": "হবিগঞ্জ শহর সংলগ্ন নদীতীর, হবিগঞ্জ",
            "mapUrl": h_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('habiganj', habiganj_data)

# ==========================================
# 4. PABNA
# ==========================================
p_raw = all_data['pabna']
pabna_data = {
    "slug": "pabna",
    "en": "Pabna",
    "bn": "পাবনা",
    "hero_title_en": "Pabna Historic River Confluences & Engineering Marvels",
    "hero_title_bn": "পাবনার ঐতিহাসিক হার্ডিঞ্জ ব্রিজ ও পদ্মাপাড়ের ঐতিহ্য",
    "hero_sub_en": "Centenary Hardinge Bridge steel trusses, terracotta Jor Bangla Temple, and sweeping Padma riverside vistas.",
    "hero_sub_bn": "শতাব্দীপ্রাচীন হার্ডিঞ্জ ব্রিজের ইস্পাত স্থাপত্য, জোড় বাংলা মন্দির ও পদ্মা নদীর স্নিগ্ধ নদীতীর।",
    "tagline_en": "The industrial and cultural powerhouse of northern Bengal, guarded by monumental railway bridges spanning the Padma and enriched by deep literary traditions.",
    "tagline_bn": "উত্তরবঙ্গের সমৃদ্ধ শিল্প ও সংস্কৃতির জনপদ, যা শতবর্ষী হার্ডিঞ্জ ব্রিজ, লালন শাহ সেতু, জোড় বাংলা মন্দির ও চলনবিলের বিস্তীর্ণ রূপলাবণ্যে মহিমান্বিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/pabna/carousel-1.webp",
            "titleEn": "Hardinge Bridge Centenary Steel Trusses",
            "titleBn": "হার্ডিঞ্জ ব্রিজের শতবর্ষী ইস্পাত কাঠামো",
            "subtitleEn": "1915 AD engineering masterpiece spanning the Padma River between Pakshi and Bheramara",
            "subtitleBn": "১৯১৫ সালে নির্মিত পদ্মার বুকে ব্রিটিশ ভারতের অন্যতম শ্রেষ্ঠ ইস্পাত রেলসেতু স্থাপত্য"
        },
        {
            "id": 2,
            "image": "images/districts/pabna/carousel-2.webp",
            "titleEn": "Lalon Shah Bridge Modern Highway Span",
            "titleBn": "লালন শাহ সেতুর আধুনিক সড়ক বিস্তার",
            "subtitleEn": "Monumental road bridge running parallel to Hardinge Bridge, framing dramatic sunset panoramas",
            "subtitleBn": "হার্ডিঞ্জ ব্রিজের সমান্তরালে নির্মিত সুবিশাল সড়ক সেতু যা উত্তর-দক্ষিণের যোগাযোগের সেতুবন্ধন"
        },
        {
            "id": 3,
            "image": "images/districts/pabna/carousel-3.webp",
            "titleEn": "Jor Bangla Temple Exquisite Terracotta",
            "titleBn": "জোড় বাংলা মন্দিরের সূক্ষ্ম পোড়ামাটির কারুকাজ",
            "subtitleEn": "18th-century dual-roofed Hindu brick temple adorned with Ramayana terracotta reliefs",
            "subtitleBn": "অষ্টাদশ শতাব্দীর ঐতিহ্যবাহী দোচালা স্থাপত্যের মন্দির যা রামায়ণের পোড়ামাটির ফলকে সুশোভিত"
        },
        {
            "id": 4,
            "image": "images/districts/pabna/carousel-4.webp",
            "titleEn": "Pakshi Railway Colony Heritage Avenues",
            "titleBn": "পাকশী রেলওয়ে কলোনির ছায়াঘেরা পথ ও নিসর্গ",
            "subtitleEn": "Vintage colonial bungalows, rain-tree canopies, and historic steam-engine railway memories",
            "subtitleBn": "ব্রিটিশ আমলের রেলওয়ে বাংলো, শতবর্ষী কড়ই গাছের ছায়া ও পদ্মাপাড়ের শান্ত পরিবেশ"
        },
        {
            "id": 5,
            "image": "images/districts/pabna/carousel-5.webp",
            "titleEn": "Chatmohar Shahi Mosque Sultanate Heritage",
            "titleBn": "চাটমোহর শাহী মসজিদের সুপ্রাচীন স্থাপত্য",
            "subtitleEn": "1581 AD pre-Mughal brick sanctuary preserving historic stone pillars and serene courtyards",
            "subtitleBn": "১৫৮১ খ্রিস্টাব্দে নির্মিত ঐতিহাসিক তিন গম্বুজ মসজিদ যা প্রাচীন বাংলার শাহি ঐতিহ্যের স্মারক"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Hardinge Bridge",
            "nameBn": "হার্ডিঞ্জ ব্রিজ",
            "categoryEn": "Historic Engineering Masterpiece",
            "categoryBn": "শতবর্ষী প্রকৌশল ও ঐতিহাসিক রেলসেতু",
            "descEn": "Inaugurated in March 1915 and named after Viceroy Lord Hardinge, the Hardinge Bridge in Pakshi is one of the world's most iconic railway engineering marvels. Spanning over 1.8 kilometers across the powerful Padma River, this monumental steel truss bridge rests on deep caisson foundations sunk dozens of meters beneath the riverbed. Designed by chief engineer Sir Robert Gales, its intricate riveted steel girder spans withstood massive floods and wartime bombardments during the 1971 Liberation War. Trains thundering across its rhythmic steel lattice against the sunset create a breathtaking spectacle cherished by generations of travelers. The bridge stands as a towering monument to early twentieth-century industrial brilliance and national connectivity.",
            "descBn": "১৯১৫ সালের মার্চ মাসে উদ্বোধন হওয়া শতবর্ষী হার্ডিঞ্জ ব্রিজ ব্রিটিশ ভারতের অন্যতম শ্রেষ্ঠ প্রকৌশল বিস্ময় ও ঐতিহ্যবাহী ইস্পাত রেলসেতু। ঈশ্বরদীর পাকশীতে প্রমত্তা পদ্মার বুকে ১.৮ কিলোমিটারেরও বেশি দীর্ঘ এই সেতুটি মাটির গভীর পর্যন্ত প্রোথিত সুবিশাল ক্যাসন পিলারের ওপর দাঁড়িয়ে আছে। চিফ ইঞ্জিনিয়ার স্যার রবার্ট গ্যালসের নকশায় তৈরি এই সেতুটির রিভেটেড স্টিল ট্রাস ১৯৭১ সালের মুক্তিযুদ্ধের বোমা হামলা ও শত বছরের বন্যার মধ্যেও অটুট রয়েছে। গোধূলিলগ্নে সেতুর ওপর দিয়ে ট্রেনের ঝকঝক শব্দে ছুটে চলার দৃশ্য এক রোমাঞ্চকর অনুভূতি উপহার দেয়। প্রযুক্তি, ইতিহাস ও প্রকৃতির এক অনন্য মেলবন্ধন এই হার্ডিঞ্জ ব্রিজ।",
            "locationEn": p_raw['hist_spots'][0]['location'],
            "locationBn": "পাকশী, ঈশ্বরদী, পাবনা",
            "mapUrl": p_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Lalon Shah Bridge",
            "nameBn": "লালন শাহ সেতু",
            "categoryEn": "Monumental Roadway Bridge",
            "categoryBn": "আধুনিক মেগা সড়ক সেতু ও নদীতীর",
            "descEn": "Opened in 2004 and named in honor of the revered mystic philosopher Fakir Lalon Shah, this monumental highway bridge spans the Padma River parallel to the historic Hardinge Bridge. Stretching nearly 1.8 kilometers with contemporary pre-stressed concrete box-girder engineering, it provides crucial seamless vehicular connectivity between northern Bengal and the southwest regions. The wide pedestrian walkways along the bridge deck offer tourists extraordinary aerial perspectives of the Padma River flowing below and the historic railway trusses nearby. Sunset visits here are immensely popular as cool river winds blow across the water and golden light reflects from the river's active sandbars. It perfectly unites modern transport efficiency with breathtaking river tourism.",
            "descBn": "বাউল সম্রাট ফকির লালন শাহের স্মরণে ২০০৪ সালে উদ্বোধন করা লালন শাহ সেতু উত্তরবঙ্গের সাথে দক্ষিণাঞ্চলের সড়ক যোগাযোগের অন্যতম প্রধান লাইফলাইন। হার্ডিঞ্জ ব্রিজের ঠিক পাশেই পদ্মার ওপর নির্মিত প্রায় ১.৮ কিলোমিটার দীর্ঘ এই আধুনিক কংক্রিট বক্স-গার্ডার সেতুটি প্রকৌশলবিদ্যার এক আধুনিক নিদর্শন। সেতুর ওপর দিয়ে হাঁটার পথ থেকে নিচে পদ্মার দিগন্তজোড়া জলরাশি এবং পাশের ঐতিহাসিক হার্ডিঞ্জ ব্রিজের সমান্তরাল দৃশ্য অসাধারণ দেখায়। বিকেলের শান্ত বাতাস ও সূর্যাস্তের রঙে রাঙানো নদী দেখতে প্রতিদিন বহু পর্যটক এখানে আসেন। আধুনিক যোগাযোগ ও প্রাকৃতিক সৌন্দর্যের অপূর্ব এক প্রতীক এই লালন শাহ সেতু।",
            "locationEn": p_raw['hist_spots'][1]['location'],
            "locationBn": "পাকশী–ভেড়ামারা সংযোগ, পাবনা অংশ",
            "mapUrl": p_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Jor Bangla Temple",
            "nameBn": "জোড় বাংলা মন্দির",
            "categoryEn": "Terracotta Brick Heritage Temple",
            "categoryBn": "টেরাকোটা সমৃদ্ধ প্রাচীন জোড় বাংলা মন্দির",
            "descEn": "Jor Bangla Temple in Pabna town is an architectural jewel of eighteenth-century Bengal, constructed by Brajamohan Krori, an influential tahsildar under the Nawab of Bengal. Built in the classic indigenous 'Jor-Bangla' style, the structure features two adjoining conjoined thatched-roof hut replicas topped by a central miniature spire. The entire brick exterior facade is embellished with remarkably detailed terracotta plaques depicting scenes from the Ramayana, Mahabharata, royal hunts, and contemporary village life. The delicate curved cornices and arched portals demonstrate the remarkable heights achieved by Bengal's traditional brick masons. Carefully protected by archaeological authorities, the temple remains an essential stop for devotees of art and architecture.",
            "descBn": "পাবনা শহরের রাঘবপুর এলাকায় অবস্থিত জোড় বাংলা মন্দির অষ্টাদশ শতাব্দীর বাংলার পোড়ামাটির অলংকরণসমৃদ্ধ এক অনন্য স্থাপত্য নিদর্শন। তৎকালীন নবাবের তহশিলদার ব্রজমোহন ক্রোড়ী কর্তৃক নির্মিত এই মন্দিরটি বাংলার ঐতিহ্যবাহী দুটি দোচালা ঘরের জোড়া কাঠামোর ওপর প্রতিষ্ঠিত, যার শীর্ষে রয়েছে একটি ক্ষুদ্রাকার চূড়া। মন্দিরের সম্মুখভাগ জুড়ে রামায়ণ, মহাভারত, পৌরাণিক যুদ্ধ ও তৎকালীন গ্রামীণ জীবনের চমৎকার দৃশ্য খোদাই করা পোড়ামাটির ফলকে সুশোভিত। নিপুণ বাঁকানো কার্নিশ ও খিলানযুক্ত প্রবেশপথ প্রাচীন বাংলার রাজমিস্ত্রিদের অসাধারণ দক্ষতার সাক্ষ্য দেয়। প্রত্নতাত্ত্বিক গুরুত্ব ও শৈল্পিক সৌন্দর্যের কারণে এটি পাবনার এক অমূল্য ঐতিহাসিক কীর্তি।",
            "locationEn": p_raw['hist_spots'][2]['location'],
            "locationBn": "পাবনা শহর, পাবনা",
            "mapUrl": p_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Taratia Zamindar Bari Area",
            "nameBn": "তারাটিয়া জমিদার বাড়ি এলাকা",
            "categoryEn": "Historic Feudal Estate Ruins",
            "categoryBn": "ঐতিহাসিক জমিদারি প্রাসাদ ও কাচারি এলাকা",
            "descEn": "The Taratia Zamindar Bari area in Pabna preserves the historic residential remnants and courtyards of a prominent landed estate that flourished during the late colonial period. Characterized by neoclassical entrance archways, brick colonnaded verandas, and ornamental water reservoirs, the complex served as an important center of revenue collection and judicial administration. The zamindars patronized traditional cultural performances, community festivals, and educational institutions across the surrounding countryside. Although natural weathering has left portions in romantic ruin, the sturdy brickwork and surviving decorative pilasters evoke an era of feudal grandeur. Visiting Taratia allows travelers to explore authentic regional history away from typical tourist routes.",
            "descBn": "পাবনার তারাটিয়া জমিদার বাড়ি এলাকা উনিশ শতকের সামন্তযুগীয় ঐতিহ্যবাহী শাসন ও সাংস্কৃতিক জীবনের স্মৃতিবাহী এক প্রাচীন প্রাসাদ প্রাঙ্গণ। উপনিবেশিক স্থাপত্যের ছোঁয়ায় নির্মিত এই জমিদার বাড়িতে ছিল সুবিশাল কাচারি ঘর, নাচঘর, সুসজ্জিত অন্দরমহল এবং শানবাঁধানো দীঘি। তৎকালীন জমিদাররা এই অঞ্চলে শিক্ষা বিস্তার, পূজা-পার্বণ ও সমাজসেবামূলক কাজে বিশেষ ভূমিকা রেখেছিলেন। যদিও সময়ের বিবর্তনে ভবনের কিছু অংশ আজ জরাজীর্ণ, তবুও এর সুদৃঢ় ইটের গাঁথুনি ও শৈল্পিক স্তম্ভগুলো অতীতের আভিজাত্যের সাক্ষ্য বহন করে। গ্রামীণ শান্ত পরিবেশে অতীতের জমিদারি স্মৃতি প্রত্যক্ষ করতে এটি এক চমৎকার স্থান।",
            "locationEn": p_raw['hist_spots'][3]['location'],
            "locationBn": "তারাটিয়া এলাকা, পাবনা",
            "mapUrl": p_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Pabna Mental Hospital Historic Campus",
            "nameBn": "পাবনা মানসিক হাসপাতাল ঐতিহাসিক ক্যাম্পাস",
            "categoryEn": "Colonial Medical Heritage Landmark",
            "categoryBn": "ঐতিহাসিক চিকিৎসা প্রতিষ্ঠান ও ঐতিহ্য চত্বর",
            "descEn": "Established in 1957 in Hemayetpur near the revered Satsang ashram of Thakur Anukulchandra, the Pabna Mental Hospital is the premier and oldest specialized psychiatric medical institution in Bangladesh. Spread across over one hundred acres of verdant landscaped grounds, the hospital campus features colonial-style red brick wards, shaded walking paths, and peaceful agricultural therapy zones. The institution pioneered compassionate modern psychiatric healthcare, occupational therapy, and rehabilitation in the subcontinent. Tall mahogany and banyan trees shade the historic avenues, fostering a tranquil therapeutic environment far removed from urban congestion. It stands as a significant landmark in the history of medical science and social welfare in Bengal.",
            "descBn": "১৯৫৭ সালে শ্রীশ্রী ঠাকুর অনুকূলচন্দ্রের সৎসঙ্গ আশ্রমের সন্নিকটে হেমায়েতপুরে প্রতিষ্ঠিত পাবনা মানসিক হাসপাতাল বাংলাদেশের প্রাচীনতম ও প্রধান বিশেষায়িত মানসিক স্বাস্থ্যসেবা প্রতিষ্ঠান। প্রায় ১১১ একর আয়তনের সুবিশাল সবুজ ছায়াঘেরা ক্যাম্পাসে রয়েছে লাল ইটের প্রাচীন চিকিৎসালয়, উন্মুক্ত মাঠ ও কর্মচিকিৎসার সুন্দর ব্যবস্থা। উপমহাদেশে বৈজ্ঞানিক ও মানবিক মানসিক স্বাস্থ্যসেবার পথিকৃৎ হিসেবে এই প্রতিষ্ঠানটি অত্যন্ত মর্যাদাপূর্ণ। প্রাচীন মেহগনি ও কড়ই গাছের ছায়ায় ঘেরা শান্ত পরিবেশ রোগীদের মানসিক প্রশান্তির জন্য বিশেষভাবে উপযোগী। চিকিৎসা বিজ্ঞানের ইতিহাস ও সামাজিক সেবামূলক ঐতিহ্যের দিক থেকে পাবনার এই ক্যাম্পাসটি অত্যন্ত তাৎপর্যপূর্ণ।",
            "locationEn": p_raw['hist_spots'][4]['location'],
            "locationBn": "হেমায়েতপুর, পাবনা",
            "mapUrl": p_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Pakshi Railway Colony and Riverside",
            "nameBn": "পাকশী রেলওয়ে কলোনি ও নদীতীর",
            "categoryEn": "Colonial Heritage Colony & Riverside Park",
            "categoryBn": "উপনিবেশিক রেলওয়ে কলোনি ও মনোরম নদীতীর",
            "descEn": "Pakshi Railway Colony is a picturesque colonial-era settlement established over a century ago to house British railway engineers who constructed the Hardinge Bridge. Nestled on high ground overlooking the Padma River, the colony features charming wooden-trussed brick bungalows, wide tree-canopied avenues, and sprawling lawns. Giant centenary rain trees and flowering gulmohar trees provide continuous shade, creating a microclimate of cooling tranquility. Visitors love walking down the historic winding paths, relaxing in riverside tea gazebos, and taking in sweeping views of the twin Padma bridges. It remains one of northern Bangladesh's most serene and atmospheric colonial eco-tourism spots.",
            "descBn": "হার্ডিঞ্জ ব্রিজ নির্মাণের সময় ব্রিটিশ প্রকৌশলী ও কর্মকর্তাদের জন্য ঈশ্বরদীর পাকশীতে গড়ে তোলা শতাব্দীপ্রাচীন রেলওয়ে কলোনি প্রকৃতির এক অপরূপ সবুজ আশ্রয়স্থল। পদ্মার কোল ঘেঁষে অবস্থিত এই কলোনিতে রয়েছে শতবর্ষী রেইনট্রি ও দেবদারু গাছের ছায়াঘেরা পিচঢালা পথ, ব্রিটিশ আমলের বাংলো এবং সুপরিসর সবুজ চত্বর। কলোনির ভেতরে হাঁটলে মনে হয় যেন ইতিহাসের এক শান্ত অধ্যায়ে প্রবেশ করা হয়েছে। নদীতীরের ক্যাফে ও বসার স্থান থেকে হার্ডিঞ্জ ও লালন শাহ সেতুর নয়নাভিরাম দৃশ্য অবলোকন করা যায়। নির্মল বাতাস, ইতিহাস ও প্রকৃতির মেলবন্ধনে সময় কাটাতে পাকশী কলোনি এক অসাধারণ গন্তব্য।",
            "locationEn": p_raw['tour_spots'][0]['location'],
            "locationBn": "পাকশী, ঈশ্বরদী, পাবনা",
            "mapUrl": p_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Ishwardi Railway Junction",
            "nameBn": "ঈশ্বরদী রেলওয়ে জংশন",
            "categoryEn": "Historic Railway Hub & Steam-Era Legacy",
            "categoryBn": "ঐতিহাসিক রেলওয়ে জংশন ও ঐতিহ্যবাহী লোকোশেড",
            "descEn": "Ishwardi Railway Junction is one of the oldest, largest, and most bustling railway transit hubs in the subcontinent, operating as the nerve center for rail traffic traversing northern and southern Bangladesh. Developed alongside the opening of the Sara-Sirajganj and Broad Gauge railway lines over a century ago, the station retains vintage mechanical signal cabins, high covered iron-truss platforms, and expansive marshaling yards. Enthusiasts can view vintage locomotive turntables and historic railway infrastructure that supported Bengal's industrialization. The station bustles day and night with passenger trains, fragrant street food vendors selling regional sweets, and travelers connecting across the nation. It represents a vibrant living monument to Bengal's railway romance.",
            "descBn": "ঈশ্বরদী রেলওয়ে জংশন উপমহাদেশের অন্যতম প্রাচীন ও সর্ববৃহৎ রেল ট্রানজিট কেন্দ্র, যা উত্তর ও দক্ষিণাঞ্চলের রেলপথ যোগাযোগের হৃদপিণ্ড হিসেবে কাজ করে। এক শতাব্দীরও বেশি সময় পূর্বে নির্মিত এই জংশনে আজও ব্রিটিশ আমলের বিশালাকার লোহার ছাদ, প্রাচীন সিগন্যাল কেবিন ও সুবিশাল লোকোমোটিভ ইয়ার্ড সংরক্ষিত রয়েছে। দিনরাত শত শত ট্রেনের আনাগোনা এবং যাত্রীদের প্রাণবন্ত কোলাহলে মুখরিত থাকে এই স্টেশনটি। স্টেশন চত্বরে পাওয়া যায় ঈশ্বরদীর বিখ্যাত চা ও স্থানীয় মিষ্টি। প্রাচীন রেল ঐতিহ্যের অনুভূতি পেতে এবং ট্রেনপ্রেমীদের জন্য ঈশ্বরদী জংশন এক অত্যন্ত রোমাঞ্চকর দর্শনীয় স্থান।",
            "locationEn": p_raw['tour_spots'][1]['location'],
            "locationBn": "ঈশ্বরদী, পাবনা",
            "mapUrl": p_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Chatmohar Shahi Mosque",
            "nameBn": "চাটমোহর শাহী মসজিদ",
            "categoryEn": "Pre-Mughal Sultanate Mosque",
            "categoryBn": "সুলতানি আমলের ঐতিহাসিক শাহী মসজিদ",
            "descEn": "Constructed in 1581 AD by Masum Khan Kabuli during the pre-Mughal transitional era, Chatmohar Shahi Mosque is a grand triple-domed sanctuary situated in Chatmohar Upazila. Built with seasoned terracotta bricks and sturdy basalt stone pillars, the mosque displays a harmonious blend of Sultanate architectural curves and early Mughal spatial grandeur. The central high dome is flanked by two smaller domes, resting over three pointed arched entrances ornamented with delicate floral terracotta bands. The peaceful courtyard features a deep historic pond and ancient trees that enhance its spiritual serenity. It stands as a prized destination for architectural historians and cultural pilgrims visiting the region.",
            "descBn": "১৫৮১ খ্রিস্টাব্দে প্রাক-মুঘল যুগে মসনদে আলা ঈসা খাঁর সেনাপতি মাছুম খাঁ কাবুলী কর্তৃক নির্মিত চাটমোহর শাহী মসজিদ পাবনার এক অনন্য ঐতিহাসিক গৌরব। তিন গম্বুজ বিশিষ্ট এই প্রাচীন মসজিদটি সুলতানি ও মুঘল স্থাপত্যরীতির অপূর্ব মিশ্রণে পোড়ামাটির ইট ও পাথরের স্তম্ভের ওপর প্রতিষ্ঠিত। এর তিনটি খিলানযুক্ত প্রবেশপথের ওপরে রয়েছে মনোরম লতাপাতা ও জ্যামিতিক নকশার টেরাকোটা কাজ। মসজিদ প্রাঙ্গণের প্রাচীন পুকুর ও ছায়াঘেরা শান্ত পরিবেশ এক গভীর আধ্যাত্মিক অনুভূতির জন্ম দেয়। উত্তরবঙ্গের প্রাচীন মুসলিম স্থাপত্যকলার অন্যতম শ্রেষ্ঠ নিদর্শন হিসেবে চাটমোহর শাহী মসজিদ ইতিহাসপ্রেমীদের মুগ্ধ করে।",
            "locationEn": p_raw['tour_spots'][2]['location'],
            "locationBn": "চাটমোহর, পাবনা",
            "mapUrl": p_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Padma Riverbank at Pakshi",
            "nameBn": "পাকশীতে পদ্মা নদীতীর",
            "categoryEn": "Scenic Riverfront Beach & Sunset Point",
            "categoryBn": "নয়নাভিরাম পদ্মাপাড় ও সূর্যাস্ত ভিউপয়েন্ট",
            "descEn": "The Padma Riverbank at Pakshi is an exhilarating natural recreational zone where the mighty Padma spreads out wide before flowing beneath the iconic twin bridges. Extensive seasonal sandbars emerge during low water periods, providing sandy beaches where tourists enjoy walking, camel rides, and traditional boat tours on wooden rowboats. The view of the evening sun casting crimson beams between the towering steel girders of Hardinge Bridge is widely recognized as one of the finest sunset spectacles in Bangladesh. Waterfront food stalls serve piping hot fried Padma river fish, traditional street snacks, and masala tea right on the riverbank. It offers an unforgettable outdoor experience celebrating river life and scenic beauty.",
            "descBn": "পাকশীতে পদ্মা নদীর তীর উত্তরবঙ্গের অন্যতম জনপ্রিয় ও দৃষ্টিনন্দন পর্যটন কেন্দ্র, যেখানে প্রমত্তা পদ্মা তার বিশাল রূপ নিয়ে দুই ঐতিহাসিক সেতুর নিচে বয়ে গেছে। শীত ও বসন্তে নদীর বুকে জেগে ওঠা বালুচরে পর্যটকরা ঘুরে বেড়ান, স্পিডবোট ও কাঠের নৌকায় চড়ে নদীতে ভেসে বেড়ান। হার্ডিঞ্জ ব্রিজের ইস্পাত কাঠামোর ফাঁক দিয়ে রক্তিম সূর্যের অস্ত যাওয়ার দৃশ্য এক অদ্ভুত জাদুকরী মায়া তৈরি করে যা আলোকচিত্রীদের পরম প্রিয়। নদীতীরের দোকানগুলোতে পদ্মার তাজা ভাজা মাছ, ইলিশের টুকরো ও গরম চায়ের আসর ভ্রমণকে আরও উপভোগ্য করে তোলে। প্রকৃতির অপার সৌন্দর্য উপভোগে এই নদীতীর এক স্বর্গীয় স্থান।",
            "locationEn": p_raw['tour_spots'][3]['location'],
            "locationBn": "পাকশী, ঈশ্বরদী, পাবনা",
            "mapUrl": p_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Gajnar Beel",
            "nameBn": "গাজনার বিল",
            "categoryEn": "Expansive Wetland Ecosystem & Aquatic Paradise",
            "categoryBn": "বিশাল প্রাকৃতিক বিল ও জলজ জীববৈচিত্র্য",
            "descEn": "Gajnar Beel in Sujanagar Upazila is a sprawling natural wetland depression that forms an ecologically rich aquatic haven covering dozens of interconnected villages. In the monsoon season, the beel fills with clean floodwaters, creating an endless shimmering aquatic expanse studded with blooming water lilies and lotus flowers. Local fishermen skillfully navigate light wooden dinghies across the waters, casting their nets in timeless rhythms to catch delicious freshwater indigenous fish. During winter, thousands of migratory whistling ducks and egrets arrive from Siberia, transforming the shallow marshes into a birdwatcher's paradise. A boat ride across Gajnar Beel reveals the untamed natural soul of rural Bengal.",
            "descBn": "সুজানগর উপজেলায় অবস্থিত গাজনার বিল পাবনার এক সুবিশাল ও প্রাকৃতিক সম্পদে ভরপুর মিষ্টি জলের জলাভূমি। বর্ষাকালে এই বিল পানিতে টইটম্বুর হয়ে ওঠে এবং এর বুকজুড়ে ফুটে থাকে হাজার হাজার রক্তকমল ও সাদা শাপলা ফুল, যা দেখতে চোখ জুড়িয়ে যায়। জেলেরা ছোট ছোট ডিঙি নৌকায় জাল ফেলে ঐতিহ্যবাহী পদ্ধতিতে মাছ ধরেন, যা গ্রামীণ জীবনের এক জীবন্ত ছবি। শীতের দিনে সুদূর সাইবেরিয়া থেকে আসা অতিথি পাখির কলকাকলিতে মুখরিত হয়ে ওঠে পুরো বিল এলাকা। বিলের শান্ত জলের ওপর দিয়ে নৌকা ভ্রমণের অভিজ্ঞতা ভ্রমণপ্রেমীদের মনে আজীবন এক মধুর স্মৃতি হয়ে থাকে।",
            "locationEn": p_raw['tour_spots'][4]['location'],
            "locationBn": "সুজানগর এলাকা, পাবনা",
            "mapUrl": p_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('pabna', pabna_data)

# ==========================================
# 5. NETROKONA
# ==========================================
n_raw = all_data['netrokona']
netrokona_data = {
    "slug": "netrokona",
    "en": "Netrokona",
    "bn": "নেত্রকোণা",
    "hero_title_en": "Netrokona Turquoise Lakes, Garo Hills & Susang Heritage",
    "hero_title_bn": "নেত্রকোণার বিরিশিরি, চিনামাটির পাহাড় ও সুসং দুর্গাপুর",
    "hero_sub_en": "Crystal-clear Someshwari river, turquoise China Clay hills at Bijoypur, and rich Garo-Hajong indigenous culture.",
    "hero_sub_bn": "স্বচ্ছতোয়া সোমেশ্বরী নদী, বিজয়পুরের নীল চিনামাটির পাহাড় ও গারো-হাজং আদিবাসী সংস্কৃতির রূপময় মেলবন্ধন।",
    "tagline_en": "The enchanting frontier district nestled against the Meghalaya Garo hills, globally celebrated for emerald china-clay waters, Susang Durgapur palaces, and vibrant indigenous traditions.",
    "tagline_bn": "মেঘালয়ের গারো পাহাড়ের পাদদেশে অবস্থিত এক রূপসী সীমান্ত জেলা, যা বিরিশিরির চিনামাটির নীল লেক, সোমেশ্বরী নদীর স্বচ্ছ জল ও সুসং দুর্গাপুরের সমৃদ্ধ ঐতিহ্যের জন্য বিখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/netrokona/carousel-1.webp",
            "titleEn": "Bijoypur China Clay Hills Turquoise Lake",
            "titleBn": "বিজয়পুর চিনামাটির পাহাড় ও নীল জলের লেক",
            "subtitleEn": "Vibrant turquoise waters reflecting white porcelain clay hillocks in Durgapur near the Meghalaya border",
            "subtitleBn": "মেঘালয় সীমান্ত সংলগ্ন দুর্গাপুরের সাদা চিনামাটির পাহাড় ও তার কোলে জমে থাকা অপরূপ নীল জলরাশি"
        },
        {
            "id": 2,
            "image": "images/districts/netrokona/carousel-2.webp",
            "titleEn": "Someshwari River Shimmering Sands",
            "titleBn": "স্বচ্ছতোয়া সোমেশ্বরী নদী ও বালুকাবেলা",
            "subtitleEn": "Crystal clear mountain river waters flowing down from Garo hills past coal-extracting wooden boats",
            "subtitleBn": "গারো পাহাড় থেকে নেমে আসা স্বচ্ছ শীতল নদীপ্রবাহ ও বালুর বুক চিরে ছুটে চলা ডিঙি নৌকা"
        },
        {
            "id": 3,
            "image": "images/districts/netrokona/carousel-3.webp",
            "titleEn": "Susang Durgapur Historic Zamindar Estate",
            "titleBn": "সুসং দুর্গাপুরের ঐতিহাসিক রাজবাড়ি",
            "subtitleEn": "Ancient palatial seat of the Susang Rajas guarding border territories and patronizing local arts",
            "subtitleBn": "মধ্যযুগীয় সুসং রাজাদের প্রাচীন রাজধানী ও ইতিহাসসমৃদ্ধ রাজকীয় ঐতিহ্যের স্মারক"
        },
        {
            "id": 4,
            "image": "images/districts/netrokona/carousel-4.webp",
            "titleEn": "Birishiri Cultural Academy & Landscape",
            "titleBn": "বিরিশিরি ক্ষুদ্র নৃ-গোষ্ঠী কালচারাল একাডেমি",
            "subtitleEn": "Cultural center preserving vibrant traditions, woven textiles, and folklore of the Garo and Hajong peoples",
            "subtitleBn": "গারো ও হাজং জনগোষ্ঠীর সমৃদ্ধ লোকসংস্কৃতি, পোশাক ও ঐতিহ্য সংরক্ষণের প্রধান সাংস্কৃতিক কেন্দ্র"
        },
        {
            "id": 5,
            "image": "images/districts/netrokona/carousel-5.webp",
            "titleEn": "Ranikhong Mission Historic Hilltop Church",
            "titleBn": "রানীখং ঐতিহাসিক ক্যাথলিক মিশন ও টিলা",
            "subtitleEn": "Centenary church perched atop a high hillock offering breathtaking panoramic vistas of the Someshwari",
            "subtitleBn": "উঁচু টিলার চূড়ায় প্রতিষ্ঠিত শতবর্ষী গির্জা যেখান থেকে সোমেশ্বরী নদী ও ভারতীয় পাহাড়ের নয়নাভিরাম দৃশ্য দেখা যায়"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Susang Durgapur Historic Estate Area",
            "nameBn": "সুসং দুর্গাপুর ঐতিহাসিক রাজবাড়ি এলাকা",
            "categoryEn": "Ancient Royal Seat & Feudal Estate",
            "categoryBn": "ঐতিহাসিক সুসং রাজবাড়ি ও রাজকীয় জনপদ",
            "descEn": "The Susang Durgapur Historic Estate Area preserves the legendary royal seat of the Susang dynasty, founded in the late thirteenth century by Someshwar Pathak. Nestled near the scenic banks of the Someshwari River, the estate commanded vast forested hills and plains populated by diverse indigenous communities. The rajas built fortified brick residences, elephant stables, treasury buildings, and the famous Dashabhuja Temple. They played an active role in regional border governance and cultural patronage, supporting classical literature and folk arts. Today, the surviving architectural gateways, ancestral dighis, and time-worn brickwork narrate centuries of regal prestige, indigenous rebellions, and cultural assimilation along Bengal's northern frontier.",
            "descBn": "সুসং দুর্গাপুর ঐতিহাসিক রাজবাড়ি এলাকা ত্রয়োদশ শতাব্দীর শেষভাগে সোমেশ্বর পাঠক কর্তৃক প্রতিষ্ঠিত সুসং রাজবংশের প্রাচীন ও গৌরবময় রাজধানী। সোমেশ্বরী নদীর কোল ঘেঁষে পাহাড়ের পাদদেশে অবস্থিত এই রাজবাড়ির শাসকরা বিশাল পাহাড়ি ও সমতল অঞ্চলের শাসনভার পরিচালনা করতেন। রাজবাড়ি প্রাঙ্গণে ছিল সুদৃঢ় ইটের প্রাসাদ, হাতিশালা, প্রাচীন দশভূজা মন্দির এবং রাজকীয় কাচারি। গারো পাহাড়ের সীমান্ত প্রতিরক্ষা এবং স্থানীয় সংস্কৃতি ও সাহিত্যের পৃষ্ঠপোষকতায় সুসং রাজারা অবিস্মরণীয় অবদান রেখেছিলেন। বর্তমানে রাজবাড়ির প্রবেশদ্বার, প্রাচীন পরিখা ও ধ্বংসাবশেষ পর্যটকদের এক সমৃদ্ধ ইতিহাসের মুখোমুখি করে।",
            "locationEn": n_raw['hist_spots'][0]['location'],
            "locationBn": "দুর্গাপুর, নেত্রকোণা",
            "mapUrl": n_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Birishiri Cultural Heritage Area",
            "nameBn": "বিরিশিরি সাংস্কৃতিক ঐতিহ্য চত্বর",
            "categoryEn": "Indigenous Cultural Heritage Center",
            "categoryBn": "ক্ষুদ্র নৃ-গোষ্ঠী সাংস্কৃতিক ঐতিহ্য এলাকা",
            "descEn": "The Birishiri Cultural Heritage Area in Durgapur is the intellectual and artistic epicentre of northern Bangladesh's indigenous communities, most prominently the Garo and Hajong peoples. Centered around the Tribal Cultural Academy established in 1977, the complex features a specialized ethnographic museum exhibiting traditional woven dakmanda textiles, musical instruments, war shields, and ancient farming tools. Cultural performances, folk dance recitals, and Wangala harvest festivals celebrated here showcase a deep harmony between native communities and nature. Visiting the compound provides deep insight into matrilineal Garo social structures and centuries of rich folkloric heritage. It is an indispensable cultural immersion landmark in Netrokona.",
            "descBn": "দুর্গাপুরের বিরিশিরি সাংস্কৃতিক ঐতিহ্য চত্বর নেত্রকোণার ক্ষুদ্র নৃ-গোষ্ঠী, বিশেষ করে গারো ও হাজং সম্প্রদায়ের শিল্প, সংস্কৃতি ও জীবনধারার প্রধান কেন্দ্র। ১৯৭৭ সালে প্রতিষ্ঠিত কালচারাল একাডেমিকে ঘিরে গড়ে ওঠা এই চত্বরে রয়েছে সমৃদ্ধ নৃতাত্ত্বিক জাদুঘর, যেখানে ঐতিহ্যবাহী দকবান্দা পোশাক, বাদ্যযন্ত্র, যুদ্ধাস্ত্র ও গৃহস্থালি সামগ্রী সংরক্ষিত আছে। প্রতি বছর এখানে আয়োজিত ওয়ানগালা নবান্ন উৎসব ও লোকনৃত্যের পরিবেশনা পর্যটকদের মুগ্ধ করে। মাতৃতান্ত্রিক গারো সমাজ ও আদিবাসী জীবনের বৈচিত্র্যময় ইতিহাস জানতে এই সাংস্কৃতিক চত্বরটি অত্যন্ত গুরুত্বপূর্ণ। সংস্কৃতির মেলবন্ধনে গড়ে ওঠা বিরিশিরি সত্যিই এক অনন্য দর্শনীয় স্থান।",
            "locationEn": n_raw['hist_spots'][1]['location'],
            "locationBn": "বিরিশিরি, দুর্গাপুর, নেত্রকোণা",
            "mapUrl": n_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Durgapur Zamindar Bari Remains",
            "nameBn": "দুর্গাপুর জমিদার বাড়ির ধ্বংসাবশেষ",
            "categoryEn": "Historic Architectural Ruins",
            "categoryBn": "প্রাচীন জমিদার বাড়ির স্থাপত্যিক ধ্বংসাবশেষ",
            "descEn": "The Durgapur Zamindar Bari Remains stand as evocative architectural fragments of the grand brick residences constructed during the height of late nineteenth-century zamindari affluence. Featuring soaring Greco-Roman columns, ornate plaster friezes, and thick lime-mortar walls, the surviving palace structures showcase the fusion of Victorian architectural trends with Bengali layout preferences. The compound includes ancient ceremonial courtyards, subterranean cellars, and stepped ponds that served domestic and religious needs. Surrounded by ancient trees and overgrown bamboo groves, the ruins possess an atmospheric melancholic charm that captivates photographers and history enthusiasts alike. It remains a silent witness to the social and agrarian history of northern Mymensingh-Netrokona.",
            "descBn": "দুর্গাপুর জমিদার বাড়ির ধ্বংসাবশেষ উনিশ শতকের শেষভাগে নির্মিত একসময়ের প্রতাপশালী জমিদারদের সুরম্য প্রাসাদের স্মৃতিচিহ্ন। ইউরোপীয় ভিক্টোরীয় ও স্থানীয় নির্মাণরীতির ছোঁয়ায় তৈরি এই ভবনের ধ্বংসাবশেষে আজও দেখা যায় দৃষ্টিনন্দন করিন্থিয়ান স্তম্ভ, খিলানযুক্ত প্রবেশপথ ও চুন-সুরকির মজবুত গাঁথুনি। প্রাসাদের ভেতরের নাটমন্দির, শানবাঁধানো দীঘি ও গোপন কুঠুরি তৎকালীন আড়ম্বরপূর্ণ জীবনের সাক্ষ্য দেয়। লতাগুল্মে ঘেরা শান্ত পরিবেশে প্রাচীন এই ধ্বংসাবশেষ আলোকচিত্রী ও ইতিহাসসন্ধানীদের মনে গভীর ভাবনার উদ্রেক করে। অতীতের জমিদারদের শাসন ও গ্রামীণ সমাজব্যবস্থা অনুধাবনে এই স্থানটি অত্যন্ত তাৎপর্যপূর্ণ।",
            "locationEn": n_raw['hist_spots'][2]['location'],
            "locationBn": "দুর্গাপুর, নেত্রকোণা",
            "mapUrl": n_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Ranikhong Mission",
            "nameBn": "রানীখং ক্যাথলিক মিশন",
            "categoryEn": "Historic Hilltop Mission Church",
            "categoryBn": "শতবর্ষী পাহাড়ি মিশন ও গির্জা",
            "descEn": "Founded in 1912 atop a picturesque hillock overlooking the Someshwari River, the Ranikhong Mission is a centenary Roman Catholic sanctuary and humanitarian complex. Established by European missionaries to serve indigenous Garo communities, the complex features a distinctive church building with high brick arches, stained glass accents, and a skyward cross. From the elevated hilltop courtyards, visitors can gaze across a spectacular panoramic vista encompassing the sparkling river below and the purple peaks of the Meghalaya hills beyond. The mission has played a transformative role in indigenous education, healthcare, and community welfare for over a century. Its serene spiritual atmosphere and unmatched natural setting make it a highlight of any trip to Durgapur.",
            "descBn": "১৯১২ সালে সোমেশ্বরী নদীর তীরে উঁচু টিলার চূড়ায় প্রতিষ্ঠিত রানীখং ক্যাথলিক মিশন নেত্রকোণার এক শতবর্ষী আধ্যাত্মিক ও ঐতিহাসিক প্রতিষ্ঠান। স্থানীয় গারো জনগোষ্ঠীর মধ্যে শিক্ষা ও সমাজসেবা প্রসারের লক্ষ্যে প্রতিষ্ঠিত এই মিশন চত্বরে রয়েছে সুদৃশ্য লাল ইটের গির্জা ও শিক্ষাপ্রতিষ্ঠান। টিলার ওপর দাঁড়িয়ে নিচে তাকালে দেখা যায় সোমেশ্বরী নদীর অপূর্ব রূপালী প্রবাহ এবং ওপারে ভারতের মেঘালয় রাজ্যের দিগন্তবিস্তৃত নীল পাহাড়ের সারি। শতাব্দীরও বেশি সময় ধরে এই মিশনটি এ অঞ্চলের পশ্চাৎপদ মানুষের কল্যাণে কাজ করে যাচ্ছে। এর শান্তিময় পরিবেশ এবং টিলার ওপর থেকে প্রকৃতির দৃশ্যপট দর্শনার্থীদের এক স্বর্গীয় আনন্দ উপহার দেয়।",
            "locationEn": n_raw['hist_spots'][3]['location'],
            "locationBn": "রানীখং, দুর্গাপুর, নেত্রকোণা",
            "mapUrl": n_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Kendua Historic Settlement Sites",
            "nameBn": "কেন্দুয়া ঐতিহাসিক জনপদ ও প্রত্নস্থল",
            "categoryEn": "Ancient Rural Settlement & Heritage Site",
            "categoryBn": "ঐতিহাসিক জনপদ ও প্রাচীন লোকঐতিহ্য",
            "descEn": "Kendua Upazila in southern Netrokona is deeply steeped in medieval literary and archaeological heritage, renowned as the cradle of Mymensingh Gitika folklore and rural ballad culture. The historic settlement sites in Kendua preserve antique brick mosques, terracotta shrine foundations, and ancestral dighis that date back to the Sultanate and Mughal eras. Prominent folk poets and rural scholars flourished in this basin, creating enduring poetic ballads such as Mahua and Malua that celebrated rural love and courage. The landscape features peaceful village clearings, old market ghats, and archaeological mounds that hold undiscovered layers of pre-modern history. Visiting Kendua connects travelers with the living literary soul and ancient rural civilization of Bengal.",
            "descBn": "নেত্রকোণার দক্ষিণাঞ্চলে অবস্থিত কেন্দুয়া এক প্রাচীন জনপদ, যা বিশ্বখ্যাত 'ময়মনসিংহ গীতিকা' এবং লোকসাহিত্যের উর্বর ভূমি হিসেবে ইতিহাসে চিহ্নিত। কেন্দুয়ার বিভিন্ন ঐতিহাসিক স্থানে রয়েছে সুলতানি ও মুঘল আমলের প্রাচীন মসজিদ, সুফি সাধকদের মাজার এবং শতাব্দীপ্রাচীন দীঘি। এই অঞ্চলে মহুয়া ও মলুয়ার মতো কালজয়ী লোকগাথা রচিত হয়েছিল যা বাংলার লোকসংস্কৃতিকে বিশ্বদরবারে পৌঁছে দিয়েছে। শান্ত পল্লী প্রকৃতির মাঝে ছড়িয়ে থাকা প্রাচীন মাটির ঢিবি ও প্রত্নতাত্ত্বিক অবশিষ্টাংশ এই জনপদের গভীর ঐতিহাসিক শিকড়কে তুলে ধরে। লোকসাহিত্য ও গ্রামীণ ঐতিহ্যের গভীরে প্রবেশ করতে কেন্দুয়ার এই ঐতিহাসিক স্থানগুলো অত্যন্ত সমৃদ্ধ।",
            "locationEn": n_raw['hist_spots'][4]['location'],
            "locationBn": "কেন্দুয়া, নেত্রকোণা",
            "mapUrl": n_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Bijoypur China Clay Hills",
            "nameBn": "বিজয়পুর চিনামাটির পাহাড়",
            "categoryEn": "Turquoise Lake & White Ceramic Hills",
            "categoryBn": "চিনামাটির পাহাড় ও নীল জলের হ্রদ",
            "descEn": "Bijoypur China Clay Hills in Durgapur is one of the most stunning geological attractions in Bangladesh, renowned for its dazzling turquoise-blue lake cradled between sculpted porcelain clay bluffs. The exposed hillocks display layers of pinkish-white, lilac, and cream-colored kaolin clay, creating an ethereal landscape unlike anywhere else in the nation. Rainwater collecting in the deep clay quarries turns a brilliant crystalline cyan due to mineral reflection, providing a breathtaking backdrop for photography. Visitors climb along safe ridgelines to marvel at the contrast between white cliffs, blue waters, and surrounding green forest groves. It represents an unmissable crown jewel of ecotourism in northern Bangladesh.",
            "descBn": "দুর্গাপুরের বিজয়পুরে অবস্থিত চিনামাটির পাহাড় বাংলাদেশের অন্যতম প্রধান ও নয়নাভিরাম ভূতাত্ত্বিক প্রাকৃতিক আকর্ষণ। সাদা, হালকা গোলাপি ও বেগুনি রঙের চিনামাটির খাড়া পাহাড়ের খাঁজে খাঁজে জমে থাকা স্ফটিকস্বচ্ছ নীল জলের লেক এক স্বপ্নের মতো দৃশ্য তৈরি করেছে। খনিজ পদার্থের উপস্থিতির কারণে এখানকার পানির রঙ উজ্জ্বল ফিরোজা-নীল দেখায়, যা আলোকচিত্রীদের জন্য এক পরম স্বর্গ। পাহাড়ের চূড়ায় উঠে দাঁড়ালে একদিকে নীল লেক এবং অন্যদিকে মেঘালয়ের সুউচ্চ সবুজ পাহাড়ের দৃশ্য দেখা যায়। প্রকৃতির এই দুর্লভ ও জাদুকরী রূপ দেখতে সারা দেশ থেকে হাজার হাজার পর্যটক প্রতিদিন বিজয়পুরে ছুটে আসেন।",
            "locationEn": n_raw['tour_spots'][0]['location'],
            "locationBn": "বিজয়পুর, দুর্গাপুর, নেত্রকোণা",
            "mapUrl": n_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Someshwari River",
            "nameBn": "সোমেশ্বরী নদী",
            "categoryEn": "Crystal Mountain River & Sandy Shores",
            "categoryBn": "পাহাড়ি স্বচ্ছ নদী ও বালুকাবেলা",
            "descEn": "Flowing down directly from the Meghalaya Garo hills across the international border, the Someshwari River is celebrated for its crystalline waters and sparkling silvery riverbed sands. The river continuously changes its channels and colors across the seasons, turning azure blue in the dry winter months while carrying rich coal fragments washed down from upstream mountain seams. Tourists love taking gentle boat rides in wooden dinghies, wading into the refreshingly cool shallows, and watching local coal-miners dive into the waters with woven baskets. The river offers breathtaking views of the blue mountain ridges rising right beyond the border fence. It is the life-giving, poetic centerpiece of travel in Netrokona.",
            "descBn": "মেঘালয়ের পাহাড় থেকে নেমে আসা স্বচ্ছতোয়া সোমেশ্বরী নদী নেত্রকোণার রূপের রাণী হিসেবে খ্যাত। শীত ও বসন্তে এই নদীর পানি কাঁচের মতো স্বচ্ছ ও নীল রূপ ধারণ করে, যার নিচে চকচকে রূপালী বালুকাবেলা স্পষ্ট দেখা যায়। স্থানীয় শ্রমিকদের পানিতে ডুব দিয়ে কয়লা ও পাথর তোলার অনন্য জীবনযুদ্ধ এই নদীর বুকে প্রত্যক্ষ করা যায়। কাঠের ছোট ডিঙি নৌকায় চড়ে নদীর বুক চিরে ঘুরে বেড়ানো এবং ওপারে পাহাড়ের বিশালতা দেখা যে কোনো মানুষকে মুগ্ধ করে। নদীর ঠান্ডা জলে পা ডুবিয়ে বসে থাকা কিংবা বালুচরে হাঁটার অভিজ্ঞতা এক গভীর প্রশান্তি এনে দেয়। নেত্রকোণা ভ্রমণের মূল আকর্ষণই হলো এই মায়াবী সোমেশ্বরী নদী।",
            "locationEn": n_raw['tour_spots'][1]['location'],
            "locationBn": "দুর্গাপুর, নেত্রকোণা",
            "mapUrl": n_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Garo Hills Viewpoint Area",
            "nameBn": "গারো পাহাড় ভিউপয়েন্ট এলাকা",
            "categoryEn": "Mountain Borderland Vista",
            "categoryBn": "গারো পাহাড় সীমান্ত ও প্রাকৃতিক পর্যবেক্ষণ পয়েন্ট",
            "descEn": "The Garo Hills Viewpoint Area along the northern border of Durgapur provides a stunning panoramic vantage point where the flat alluvial plains of Bangladesh dramatically meet the rising green ramparts of Meghalaya. Looking across the frontier, travelers behold layers of undulating misty mountain ridges cloaked in thick tropical forest and occasional cascading waterfalls. The fresh mountain winds and sweeping horizons provide a cool and invigorating retreat from urban heat. Shaded border roads wind through quiet tribal settlements, betel-leaf gardens, and citrus orchards, offering a peaceful glimpse into borderland nature. It is an extraordinary spot for watching sunsets and absorbing the grandeur of mountain geography.",
            "descBn": "দুর্গাপুরের উত্তর সীমান্তে অবস্থিত গারো পাহাড় ভিউপয়েন্ট এমন একটি স্থান যেখানে বাংলাদেশের সমতল ভূমি মেঘালয়ের সুউচ্চ সবুজ পাহাড়মালার সাথে এসে মিশেছে। সীমান্তরেখার ওপারে তাকালে ঘন কুয়াশা ও মেঘে ঢাকা পাহাড়ের ভাঁজে ভাঁজে সবুজের অনন্ত সমারোহ দেখা যায়। পাহাড়ি মুক্ত বাতাস এবং দিগন্তজোড়া দৃশ্যপট ভ্রমণকারীদের দেহ ও মনে এক সতেজ অনুভূতি এনে দেয়। সীমান্তের শান্ত পথ ধরে হাঁটলে চোখে পড়ে ক্ষুদ্র নৃ-গোষ্ঠীদের শান্ত গ্রাম, সুপারি বাগান ও পাহাড়ি ঝিরি। গোধূলিলগ্নে পাহাড়ের বুকে রঙের খেলা দেখার জন্য এই ভিউপয়েন্টটি অত্যন্ত জনপ্রিয়।",
            "locationEn": n_raw['tour_spots'][2]['location'],
            "locationBn": "দুর্গাপুর সীমান্ত অঞ্চল, নেত্রকোণা",
            "mapUrl": n_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Ubal Khashia Mandi Cultural Area",
            "nameBn": "উবাল খাসিয়া মান্দি সাংস্কৃতিক এলাকা",
            "categoryEn": "Indigenous Eco Village & Heritage Corridor",
            "categoryBn": "আদিবাসী পল্লি ও পরিবেশবান্ধব সাংস্কৃতিক এলাকা",
            "descEn": "The Ubal Khashia Mandi Cultural Area is an authentic indigenous village cluster nestled in the hills of Durgapur where traditional Garo (Mandi) and Khasi lifestyles thrive in harmony with the natural environment. Village paths are lined with traditional bamboo stilt homes, lush betel leaf groves, pineapple plantations, and sacred community meeting courtyards. Travelers can interact with warm and welcoming indigenous villagers, observe intricate handloom weaving of traditional fabrics, and learn about herbal medicinal traditions. The pristine, clean surroundings and serene eco-conscious village lifestyle provide an eye-opening cultural journey. It is a wonderful community-based tourism stop that celebrates indigenous resilience and heritage.",
            "descBn": "দুর্গাপুরের পাহাড়ি অঞ্চলে অবস্থিত উবাল খাসিয়া মান্দি সাংস্কৃতিক এলাকা গারো (মান্দি) ও খাসিয়া জনগোষ্ঠীর ঐতিহ্যবাহী জীবনযাত্রার এক চমৎকার ও জীবন্ত উদাহরণ। এই আদিবাসী পল্লিগুলোতে বাঁশ ও কাঠের তৈরি মাচাং ঘর, পান বরজ ও আনারস বাগানের মনোমুগ্ধকর দৃশ্য চোখে পড়ে। পর্যটকরা এখানে এসে স্থানীয় অধিবাসীদের সরল জীবনযাপন প্রত্যক্ষ করতে পারেন, তাদের ঐতিহ্যবাহী তাঁতে বোনা রঙিন পোশাক দেখা এবং পাহাড়ি সংস্কৃতির সাথে পরিচিত হতে পারেন। প্রকৃতির ক্ষতি না করে মাটির সাথে মিশে থাকা এই জনগোষ্ঠীর জীবনদর্শন অত্যন্ত অনুপ্রেরণাদায়ী। গ্রামীণ আতিথেয়তা ও আদিবাসী সংস্কৃতি অনুভবে এটি এক অপূর্ব স্থান।",
            "locationEn": n_raw['tour_spots'][3]['location'],
            "locationBn": "দুর্গাপুর, নেত্রকোণা",
            "mapUrl": n_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Birishiri Riverside Landscape",
            "nameBn": "বিরিশিরি নদীতীরবর্তী নিসর্গ",
            "categoryEn": "Serene Riverside Eco Haven",
            "categoryBn": "নয়নাভিরাম নদীতীর ও প্রাকৃতিক বিনোদন চত্বর",
            "descEn": "The Birishiri Riverside Landscape encompasses the tranquil waterfront along the bends of the Someshwari River near the historic Birishiri bridge crossing. Characterized by wide sandy banks, gently nodding kashful reeds, and panoramic views of distant blue hill contours, it is the favored gathering ground for travelers at twilight. Bamboo tea stalls and open-air seating areas set up along the high embankment offer steaming lemon tea and hot pakoras while the evening breeze rustles through the river reeds. Visitors sit for hours taking in the peaceful sound of gentle waves and watching stars emerge in the dark borderland sky. It encapsulates the romantic, serene essence of traveling through Netrokona.",
            "descBn": "বিরিশিরি ব্রিজ সংলগ্ন সোমেশ্বরী নদীর তীরবর্তী এলাকা প্রকৃতির এক শান্ত ও অপূর্ব আশ্রয়স্থল, যেখানে নদীর আঁকাবাঁকা গতিপথ ও বালুচরের দৃশ্য মন কেড়ে নেয়। নদীর পাড়ে বসে দূরের গারো পাহাড়ের দিকে তাকালে জীবনের সব ক্লান্তি যেন মিলিয়ে যায়। বিকেলে নদীতীরের বাঁশের চায়ের দোকানে বসে ধোঁয়া ওঠা লেবু চা আর চপ-সিঙাড়া খাওয়ার আনন্দই আলাদা। নদীর বুকে সূর্যাস্তের রঙের প্রতিফলন এবং সন্ধ্যার বাতাসে কাশফুলের দোলা এক রোমান্টিক আবহ তৈরি করে। বিরিশিরির এই নদীতীরে কিছুটা সময় কাটানো প্রতিটি ভ্রমণপিপাসুর হৃদয়ে এক চিরন্তন ভালোলাগা তৈরি করে।",
            "locationEn": n_raw['tour_spots'][4]['location'],
            "locationBn": "বিরিশিরি, দুর্গাপুর, নেত্রকোণা",
            "mapUrl": n_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('netrokona', netrokona_data)
