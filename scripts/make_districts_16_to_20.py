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
# 16. JHENAIDAH
# ==========================================
jh_raw = all_data['jhenaidah']
jhenaidah_data = {
    "slug": "jhenaidah",
    "en": "Jhenaidah",
    "bn": "ঝিনাইদহ",
    "hero_title_en": "Jhenaidah Medieval Barobazar & Royal Naldanga Heritage",
    "hero_title_bn": "ঝিনাইদহের মধ্যযুগীয় বারোবাজার ও পুণ্যময় নলডাঙ্গা রাজবাড়ি",
    "hero_sub_en": "Fifteenth-century Sultanate mosques of Barobazar, historic Naldanga Temple Complex, and serene Nabaganga river corridors.",
    "hero_sub_bn": "বারোবাজারের পঞ্চদশ শতাব্দীর ঐতিহাসিক সুলতানি মসজিদ নগরী, প্রাচীন নলডাঙ্গা রাজবাড়ি ও নবগঙ্গা নদীর শান্ত প্রকৃতি।",
    "tagline_en": "The sacred archaeological capital of southwestern Bengal, celebrated for the medieval Sultanate mosque city at Barobazar, heroic folk legends of Pagla Kanai, and historic terracotta temples.",
    "tagline_bn": "দক্ষিণ-পশ্চিমাঞ্চলের এক গৌরবময় প্রত্নতাত্ত্বিক জেলা, যা বারোবাজারের সুলতানি আমলের ঐতিহাসিক মসজিদ নগরী, মরমি কবি পাগলা কানাইয়ের স্মৃতি, নলডাঙ্গা রাজবাড়ি ও ঢোল সমুদ্র দীঘির জন্য সুপরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/jhenaidah/carousel-1.webp",
            "titleEn": "Barobazar Archaeological Mosque City Heritage",
            "titleBn": "বারোবাজারের ঐতিহাসিক প্রত্নতাত্ত্বিক মসজিদ নগরী",
            "subtitleEn": "Cluster of 15th-century Sultanate brick mosques discovered across ancient trade routes in Kaliganj",
            "subtitleBn": "কালীগঞ্জের বারোবাজারে আবিষ্কৃত মধ্যযুগীয় বাংলার অপূর্ব সুলতানি আমলের পোড়ামাটির মসজিদ কমপ্লেক্স"
        },
        {
            "id": 2,
            "image": "images/districts/jhenaidah/carousel-2.webp",
            "titleEn": "Naldanga Temple Complex Royal Terracotta",
            "titleBn": "নলডাঙ্গা রাজবাড়ি মন্দির কমপ্লেক্স",
            "subtitleEn": "Centuries-old historic Hindu temple sanctuaries built by the Naldanga Rajas nestled in peaceful greenery",
            "subtitleBn": "নলডাঙ্গা রাজাদের পৃষ্ঠপোষকতায় নির্মিত শতাব্দীপ্রাচীন কারুকার্যময় সিদ্ধেশ্বরী ও তারা মন্দির"
        },
        {
            "id": 3,
            "image": "images/districts/jhenaidah/carousel-3.webp",
            "titleEn": "Dhol Samudra Dighi Vast Heritage Water Reservoir",
            "titleBn": "ঢোল সমুদ্র দীঘির সুবিশাল জলরাশি",
            "subtitleEn": "Legendary 52-bigha royal freshwater lake excavated by ancient Hindu rajas in Jhenaidah Sadar",
            "subtitleBn": "ঝিনাইদহ সদরে অবস্থিত ঐতিহাসিক ৫২ বিঘার সুবিশাল প্রাচীন দিঘি যা লোকগাথা ও শান্ত নিসর্গের প্রতীক"
        },
        {
            "id": 4,
            "image": "images/districts/jhenaidah/carousel-4.webp",
            "titleEn": "Shailkupa Shahi Mosque Sultanate Architecture",
            "titleBn": "শৈলকূপা শাহী মসজিদের লাল ইটের রূপ",
            "subtitleEn": "15th-century pre-Mughal Sultanate sanctuary built on the Kumar riverbank adorned with terracotta",
            "subtitleBn": "কুমার নদের তীরে অবস্থিত সুলতানি আমলের সুপ্রাচীন তিন গম্বুজ মসজিদ যা প্রাচীন শিল্পনৈপুণ্যে অনন্য"
        },
        {
            "id": 5,
            "image": "images/districts/jhenaidah/carousel-5.webp",
            "titleEn": "Nabaganga Riverbank Scenic Pastoral Promenade",
            "titleBn": "নবগঙ্গা নদীতীরের স্নিগ্ধ পল্লী নিসর্গ",
            "subtitleEn": "Meandering river flowing through the heart of Jhenaidah framed by date-palms and village tranquility",
            "subtitleBn": "ঝিনাইদহ শহরের পাশ দিয়ে বয়ে চলা শান্ত নদীপ্রবাহ যা ভ্রমণপ্রেমীদের দেয় নির্মল বাতাস ও মনোরম সূর্যাস্ত"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Naldanga Temple Complex",
            "nameBn": "নলডাঙ্গা রাজবাড়ি মন্দির কমপ্লেক্স",
            "categoryEn": "Royal Heritage Temple Sanctuary",
            "categoryBn": "ঐতিহাসিক রাজকীয় মন্দির কমপ্লেক্স ও দেবালয়",
            "descEn": "The Naldanga Temple Complex in Kaliganj Upazila is a magnificent cluster of seventeenth-century terracotta Hindu temples established under the patronage of the illustrious Naldanga royal dynasty. Built primarily by Raja Indranarayan and his successors between 1656 and 1788 AD, the complex features several individual sanctuaries, including the Siddheshwari Kali Temple, Gunjanath Shiva Temple, and Raj Rajeshwar Mandir. The architecture showcases classic Bengali At-Chala and Navaratna spire styles adorned with intricate terracotta plaques illustrating scenes from Hindu epics, floral rosettes, and royal processions. Surrounding the temples are ancient stepped dighis and mango groves that evoke the quiet grandeur of princely Bengal. It stands as a prized destination for architectural scholars, historians, and devotees.",
            "descBn": "কালীগঞ্জ উপজেলায় অবস্থিত নলডাঙ্গা মন্দির কমপ্লেক্স সপ্তদশ শতাব্দীর হিন্দু মন্দির স্থাপত্যের এক অনন্য ও ঐতিহাসিক রত্ন, যা নলডাঙ্গার রাজবংশের পৃষ্ঠপোষকতায় গড়ে উঠেছিল। ১৬৫৬ থেকে ১৭৮৮ খ্রিস্টাব্দের মধ্যে রাজা ইন্দ্রনারায়ণ ও তাঁর উত্তরসূরিদের দ্বারা নির্মিত এই কমপ্লেক্সে রয়েছে শ্রী শ্রী সিদ্ধেশ্বরী কালী মন্দির, গুঞ্জনাথ শিব মন্দির এবং রাজ রাজেশ্বর মন্দিরসহ বেশ কয়েকটি সুরম্য উপাসনালয়। ঐতিহ্যবাহী বাংলা আটচালা ও নবরত্ন স্থাপত্যরীতিতে নির্মিত এই মন্দিরগুলোর বহির্দেয়ালে পোড়ামাটির চমৎকার ফলকে রামায়ণ, মহাভারত ও পৌরাণিক কাহিনী খোদাই করা আছে। প্রাচীন দিঘি ও ছায়াঘেরা শান্ত পরিবেশে দাঁড়িয়ে থাকা এই রাজকীয় মন্দিরগুলো বাংলার প্রাচীন ভাস্কর্যকলার এক গৌরবময় স্মারক।",
            "locationEn": jh_raw['hist_spots'][0]['location'],
            "locationBn": "নলডাঙ্গা, কালীগঞ্জ, ঝিনাইদহ",
            "mapUrl": jh_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Shailkupa Shahi Mosque",
            "nameBn": "শৈলকূপা শাহী মসজিদ",
            "categoryEn": "Sultanate Architectural Masterpiece",
            "categoryBn": "সুলতানি আমলের ঐতিহাসিক শাহী মসজিদ",
            "descEn": "Constructed in 1519 AD during the reign of Sultan Alauddin Husain Shah by Ramat Khan, Shailkupa Shahi Mosque on the banks of the Kumar River is an architectural masterpiece of pre-Mughal Bengal. Built with seasoned terracotta bricks and lime mortar, the rectangular sanctuary features three ribbed hemispherical domes, six slender octagonal minarets, and three pointed-arch entrance portals decorated with delicate floral bands. The exterior walls display classic Sultanate curved cornices and recessed arched panels that reflect the golden age of Bengal Sultanate design. Inside, intricately carved black basalt stone mihrabs and arched niches provide an atmosphere of quiet reverence. Carefully preserved across five centuries, the mosque remains an active center of worship and an essential stop for cultural travelers.",
            "descBn": "১৫১৯ খ্রিস্টাব্দে সুলতান আলাউদ্দিন হোসেন শাহের আমলে নির্মিত শৈলকূপা শাহী মসজিদ কুমার নদের তীরে অবস্থিত প্রাক-মুঘল বাংলার এক অনিন্দ্যসুন্দর স্থাপত্যকীর্তি। আয়তাকার এই মসজিদে রয়েছে তিনটি সুষম গম্বুজ, ছয়টি অষ্টভুজাকৃতির মিনার এবং তিনটি খিলানযুক্ত প্রবেশপথ। পোড়ামাটির লাল ইট ও চুন-সুরকিতে নির্মিত এই মসজিদের বহির্দেয়ালে রয়েছে ঐতিহ্যবাহী বাঁকানো কার্নিশ এবং ভেতরের দেওয়ালে কালো ব্যাসল্ট পাথরের নিখুঁত মেহরাব। কুমার নদের শান্ত হাওয়া এবং ছায়াঘেরা প্রাঙ্গণ এই মসজিদটিকে এক গভীর আধ্যাত্মিক স্নিগ্ধতায় ভরিয়ে রেখেছে। পাঁচ শতাব্দীরও বেশি সময় ধরে কালের সাক্ষী হয়ে দাঁড়িয়ে থাকা এই প্রাচীন শাহী মসজিদ ঝিনাইদহের এক পরম অহংকার।",
            "locationEn": jh_raw['hist_spots'][1]['location'],
            "locationBn": "শৈলকূপা, ঝিনাইদহ",
            "mapUrl": jh_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Jor Bangla Mosque",
            "nameBn": "জোড় বাংলা মসজিদ (বারোবাজার)",
            "categoryEn": "15th-Century Sultanate Single-Dome Mosque",
            "categoryBn": "সুলতানি আমলের প্রাচীন এক গম্বুজ মসজিদ",
            "descEn": "Jor Bangla Mosque is a gem of fifteenth-century Sultanate brick architecture situated in the heart of the ancient Barobazar archaeological zone in Kaliganj. Excavated by the Department of Archaeology, the square sanctuary features a massive central dome resting atop thick burnt-clay walls, flanked by four octagonal corner minarets that taper gracefully toward the roof. The exterior facade displays delicate terracotta friezes, stepped brick cornices, and recessed arched niches that demonstrate the refined aesthetic of Khan Jahani architectural synthesis. Inside, a beautifully proportioned central mihrab is embellished with floral rosettes and geometric patterns that catch the soft natural light. Set amidst quiet village orchards, it offers visitors an authentic encounter with medieval Bengal's forgotten urban civilization.",
            "descBn": "কালীগঞ্জের প্রাচীন বারোবাজার প্রত্নতাত্ত্বিক এলাকার কেন্দ্রস্থলে অবস্থিত জোড় বাংলা মসজিদ পঞ্চদশ শতাব্দীর সুলতানি স্থাপত্যকলার এক অপূর্ব নিদর্শন। প্রত্নতাত্ত্বিক খননের মাধ্যমে উদ্ধার করা এই বর্গাকার মসজিদের ছাদে রয়েছে একটি সুবিশাল গম্বুজ এবং চার কোণে চারটি সুদৃশ্য অষ্টভুজাকৃতির মিনার। পোড়ামাটির লাল ইট, বাঁকানো কার্নিশ এবং দেওয়ালে খোদাই করা লতাপাতার সূক্ষ্ম নকশা খান জাহানী নির্মাণরীতির অনন্য আভিজাত্য প্রকাশ করে। মসজিদের ভেতরের মার্জিত মেহরাব ও শীতল পরিবেশ প্রাচীন আধ্যাত্মিক সাধনার কথা মনে করিয়ে দেয়। নিভৃত গ্রামীণ শান্ত পরিবেশে অবস্থিত এই প্রাচীন মসজিদটি মধ্যযুগীয় বাংলার সমৃদ্ধ নগর সংস্কৃতির এক জীবন্ত স্মারক।",
            "locationEn": jh_raw['hist_spots'][2]['location'],
            "locationBn": "বারোবাজার, কালীগঞ্জ, ঝিনাইদহ",
            "mapUrl": jh_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Gorar Mosque",
            "nameBn": "গোড়ার মসজিদ (বারোবাজার)",
            "categoryEn": "Historic Four-Corner Minaret Brick Mosque",
            "categoryBn": "ঐতিহাসিক সুলতানি পোড়ামাটির মসজিদ",
            "descEn": "Gorar Mosque is one of the most prominent excavated Sultanate sanctuaries in the Barobazar archaeological park, constructed in the late fifteenth century during the reign of the Ilyas Shahi or Husain Shahi rulers. The square brick building is crowned by a high central dome supported internally by squinches and heavy brick walls, with four octagonal corner towers that feature molded brick rings. The eastern entrance facade displays three arched openings flanked by terracotta pilasters decorated with hanging chain-and-bell motifs. An adjoining freshwater pond and landscaped archaeological lawn enhance the peaceful atmosphere of the site. Historians believe the mosque served as a prime congregational sanctuary for merchants traveling along medieval river-trade routes.",
            "descBn": "বারোবাজার প্রত্নতাত্ত্বিক কমপ্লেক্সের অন্যতম প্রধান ও চিত্তাকর্ষক প্রাচীন নিদর্শন হলো এই গোড়ার মসজিদ, যা পঞ্চদশ শতাব্দীর শেষভাগে ইলিয়াস শাহী বা হোসেন শাহী যুগে নির্মিত হয়েছিল। সুবিশাল বর্গাকার এই মসজিদের ছাদে একটি চমৎকার গম্বুজ এবং চার কোণে চক্রাকার নকশার মিনার রয়েছে। পূর্বমুখী তিনটি খিলানযুক্ত প্রবেশদ্বারের চারপাশে পোড়ামাটির সুদৃশ্য ঝুলন্ত শিকল ও ঘণ্টার মোটিফ অত্যন্ত চমৎকারভাবে সংরক্ষিত আছে। সংলগ্ন প্রাচীন জলাশয় ও সবুজ ঘাসের লন মসজিদটির ঐতিহাসিক পরিবেশকে আরও স্নিগ্ধ ও দৃষ্টিনন্দন করে তুলেছে। মধ্যযুগে এই অঞ্চলের সমৃদ্ধ বাণিজ্য ও আধ্যাত্মিক জীবনের এক অমূল্য প্রামাণ্য দলিল এই গোড়ার মসজিদ।",
            "locationEn": jh_raw['hist_spots'][3]['location'],
            "locationBn": "বারোবাজার, কালীগঞ্জ, ঝিনাইদহ",
            "mapUrl": jh_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Galakata Mosque",
            "nameBn": "গলাকাটা মসজিদ (বারোবাজার)",
            "categoryEn": "Historic Multi-Domed Sultanate Mosque",
            "categoryBn": "ঐতিহাসিক ছয় গম্বুজ সুলতানি মসজিদ",
            "descEn": "Galakata Mosque in Barobazar is an extraordinary six-domed Sultanate brick monument dating back to the fifteenth century, named after historical folklore associated with ancient saintly struggles in the region. Built on a raised rectangular plinth with seasoned terracotta bricks, the mosque features two parallel rows of three domes supported internally by sturdy stone pillars and groined brick arches. The western interior wall contains three beautifully arched mihrabs decorated with fine terracotta arabesques, rosettes, and miniature hanging lamp motifs. Outside, circular corner bastions and stepped brick mouldings emphasize the monument's defensive durability. Protected within the archaeological reserve, Galakata Mosque stands as a testament to the architectural sophistication of medieval Khalifatabad's northern frontier.",
            "descBn": "বারোবাজারের অন্যতম চমকপ্রদ প্রত্নতাত্ত্বিক নিদর্শন হলো ঐতিহাসিক গলাকাটা মসজিদ, যা পঞ্চদশ শতাব্দীতে সুলতানি আমলের লাল ইটের তৈরি এক সুরম্য ছয় গম্বুজ বিশিষ্ট মসজিদ। দুটি সারিতে তিনটি করে মোট ছয়টি গম্বুজযুক্ত এই মসজিদের ছাদটি ভেতরে পাথরের সুদৃঢ় স্তম্ভের ওপর স্থাপিত। মসজিদের পশ্চিম দেওয়ালে তিনটি অত্যন্ত সূক্ষ্ম ও কারুকার্যময় মেহরাব রয়েছে যাতে খোদাই করা আছে প্রাচীন লতাপাতা ও ঝুলন্ত প্রদীপের মোটিফ। চার কোণের বৃত্তাকার মিনার ও পুরু প্রাচীর তৎকালীন নির্মাণশিল্পীদের উচ্চ প্রকৌশল জ্ঞানের পরিচয় দেয়। লোকগাথা ও মধ্যযুগীয় ইতিহাসের অনন্য মিশ্রণ এই গলাকাটা মসজিদ প্রত্নতাত্ত্বিক ভ্রমণপিপাসুদের পরম প্রিয়।",
            "locationEn": jh_raw['hist_spots'][4]['location'],
            "locationBn": "বারোবাজার, কালীগঞ্জ, ঝিনাইদহ",
            "mapUrl": jh_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Barobazar Archaeological Area",
            "nameBn": "বারোবাজার প্রত্নতাত্ত্বিক এলাকা",
            "categoryEn": "Medieval Archaeological Park & Mosque City",
            "categoryBn": "ঐতিহাসিক প্রত্নতাত্ত্বিক পার্ক ও প্রাচীন মসজিদ নগরী",
            "descEn": "The Barobazar Archaeological Area in Kaliganj Upazila is one of the most concentrated medieval archaeological zones in South Asia, preserving nineteen excavated Sultanate-era mosques, royal mausoleums, and ancient dighis spread across an ancient riverfront city. Identified as the historic medieval city of Muhammadabad, the area flourished as a strategic trading metropolis along the Bhairab river corridor connecting Khulna to central Bengal. Well-maintained walking trails connect iconic monuments including the Gorar Mosque, Jor Bangla Mosque, Galakata Mosque, and Pir Pukur Mosque. Shaded by ancient mango orchards and date palms, the open-air archaeological park allows travelers to wander through five centuries of preserved Islamic architectural heritage. It is a world-class cultural destination for history enthusiasts.",
            "descBn": "কালীগঞ্জ উপজেলার বারোবাজার প্রত্নতাত্ত্বিক এলাকা বাংলাদেশের অন্যতম প্রাচীন ও সমৃদ্ধ মধ্যযুগীয় মসজিদ নগরী, যেখানে প্রায় ১৯টি সুলতানি আমলের মসজিদ, মাজার ও প্রাচীন দিঘির সমাহার রয়েছে। মধ্যযুগে এটি 'মুহাম্মাদাবাদ' নামে এক সমৃদ্ধ বাণিজ্যিক ও প্রশাসনিক রাজধানী হিসেবে পরিচিত ছিল যা ভৈরব নদের অববাহিকায় গড়ে উঠেছিল। সবুজ গাছগাছালি ও শান্ত গ্রামীণ পথের মাধ্যমে সংযুক্ত এই প্রত্নতাত্ত্বিক এলাকায় রয়েছে জোড় বাংলা, গোড়ার মসজিদ, গলাকাটা মসজিদ ও পীর পুকুর মসজিদের মতো অপূর্ব নিদর্শন। ইতিহাসপ্রেমী ও ভ্রমণপিপাসুদের জন্য উন্মুক্ত এই প্রাচীন মসজিদ নগরী ঘুরে দেখা এক স্বপ্নিল ও শিক্ষণীয় অভিজ্ঞতা।",
            "locationEn": jh_raw['tour_spots'][0]['location'],
            "locationBn": "বারোবাজার, কালীগঞ্জ, ঝিনাইদহ",
            "mapUrl": jh_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Dhol Samudra Dighi",
            "nameBn": "ঢোল সমুদ্র দীঘি",
            "categoryEn": "Colossal Royal Freshwater Dighi",
            "categoryBn": "ঐতিহাসিক ৫২ বিঘার সুবিশাল প্রাচীন দিঘি",
            "descEn": "Dhol Samudra Dighi in Jhenaidah Sadar is a legendary freshwater lake spanning over fifty-two bighas, excavated by ancient Hindu rajas to alleviate drinking water shortages across the surrounding region. Entwined with captivating local folklore, legend recounts that the lake remained stubbornly dry until royal drums (dhol) were beaten and a self-sacrificing queen stepped into its center, causing sweet water to gush forth to the drumbeats. Surrounded by ancient trees, date palms, and grassy meadows, the shimmering lake provides a serene sanctuary for morning walkers, anglers, and nature enthusiasts. During winter, flocks of migratory aquatic birds settle on its open waters, creating an idyllic setting for photography and relaxation. It is a cherished historical and recreational landmark of Jhenaidah.",
            "descBn": "ঝিনাইদহ সদর উপজেলায় অবস্থিত ঢোল সমুদ্র দীঘি প্রায় ৫২ বিঘা আয়তনের এক সুবিশাল ও প্রাচীন ঐতিহাসিক জলাশয়, যা শত শত বছর ধরে তার অপার সৌন্দর্য ও লোকগাথা নিয়ে টিকে আছে। কিংবদন্তি প্রচলিত আছে যে, প্রজাদের জলের কষ্ট দূর করতে খনন করা এই দিঘিতে পানি না ওঠায় রাজার আত্মত্যাগের পর ঢোলের শব্দে হঠাৎ জলরাশি উথলে উঠেছিল, যেখান থেকে এর নাম হয়েছে 'ঢোল সমুদ্র'। প্রাচীন গাছপালা ও স্নিগ্ধ বাতাসের স্পর্শে দীঘির পাড়ে সময় কাটানো অত্যন্ত আনন্দদায়ক। শীতের দিনে পরিযায়ী পাখির কলতানে মুখরিত থাকে এই সুবিশাল দিঘি। ইতিহাস ও নিসর্গের অপূর্ব সংমিশ্রণে ঢোল সমুদ্র দীঘি ঝিনাইদহের এক অন্যতম প্রধান পর্যটন আকর্ষণ।",
            "locationEn": jh_raw['tour_spots'][1]['location'],
            "locationBn": "ঝিনাইদহ সদর, ঝিনাইদহ",
            "mapUrl": jh_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Naldanga Rajbari and Temple Area",
            "nameBn": "নলডাঙ্গা রাজবাড়ি ও উদ্যান এলাকা",
            "categoryEn": "Royal Palace Grounds & Historic Eco Park",
            "categoryBn": "ঐতিহাসিক রাজবাড়ি উদ্যান ও প্রাচীন দিঘি প্রাঙ্গণ",
            "descEn": "The Naldanga Rajbari and Temple Area encompasses the historic grounds and lush parklands surrounding the centuries-old royal palaces of the Naldanga zamindars. Shaded by mature banyan, mahogany, and rain trees, the premises preserve antique stepped bathing ghats, tranquil lotus ponds, and ancient brick ruins that narrate centuries of feudal elegance. Visitors love strolling along the quiet village avenues, admiring the intricately carved terracotta temples, and resting on stone benches beside the water. The serene atmosphere, combined with the rich historical legacy of regional rulers who championed education and arts, creates a profoundly reflective environment. It is an indispensable stop for heritage travelers exploring the cultural roots of southwestern Bengal.",
            "descBn": "নলডাঙ্গা রাজবাড়ি ও উদ্যান এলাকা শতাব্দীপ্রাচীন সামন্তযুগীয় রাজপ্রাসাদ ও সুরম্য দেবালয় ঘিরে গড়ে ওঠা এক শান্ত ও নয়নাভিরাম পরিবেশ। সুপ্রাচীন বট-মেহগনির ছায়াতলে বিস্তৃত এই চত্বরে রয়েছে ঐতিহাসিক শানবাঁধানো দিঘি, পদ্মপুকুর এবং প্রাচীন রাজকীয় ভবনের অবশিষ্টাংশ। টেরাকোটা অলংকৃত মন্দিরগুলোর শৈল্পিক রূপ অবলোকন করতে এবং শান্ত গ্রামীণ বাতাসে হাঁটতে দেশ-বিদেশের বহু পর্যটক এখানে আসেন। তৎকালীন জমিদারদের প্রতিষ্ঠিত বিদ্যালয় ও দাতব্য চিকিৎসালয়ের স্মৃতি আজও এই এলাকার মানুষের মুখে মুখে ফেরে। ইতিহাস, ঐতিহ্য ও নিসর্গের শান্তিময় মেলবন্ধন দেখতে নলডাঙ্গা রাজবাড়ি প্রাঙ্গণ এক অতুলনীয় স্থান।",
            "locationEn": jh_raw['tour_spots'][2]['location'],
            "locationBn": "নলডাঙ্গা, কালীগঞ্জ, ঝিনাইদহ",
            "mapUrl": jh_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Nabaganga Riverbank",
            "nameBn": "নবগঙ্গা নদীতীর",
            "categoryEn": "Meandering River Promenade & Sunset Point",
            "categoryBn": "নয়নাভিরাম নদীতীর, স্নিগ্ধ বাঁধ ও সূর্যাস্ত ভিউপয়েন্ট",
            "descEn": "Flowing directly through the heart of Jhenaidah town and district, the Nabaganga Riverbank is the beloved scenic promenade and environmental lifeline of the region. Originating from the Mathabhanga River, the Nabaganga flows past lush date-palm orchards, green vegetable plains, and bustling municipal ghats. Paved pedestrian walkways and tree-shaded gazebos developed along the riverfront in Jhenaidah town offer residents and visitors a welcoming space for evening strolls and social gatherings. Traditional wooden rowboats drift gently across the water, offering peaceful rides while sunset paints the sky in glowing crimson tones. Waterfront tea stalls serve fresh tea and regional snacks, making it the premier civic leisure destination in Jhenaidah.",
            "descBn": "ঝিনাইদহ শহরের বুক চিরে প্রবাহিত নবগঙ্গা নদী এ অঞ্চলের এক অত্যন্ত মনোরম ও প্রাণবন্ত জলধারা। নদীর দুই তীর ঘেঁষে গড়ে ওঠা খেজুর বাগান, সবুজ খেত ও শহরের শানবাঁধানো ঘাট এক চমৎকার দৃশ্য তৈরি করেছে। নদীতীরে নির্মিত ওয়াকওয়ে ও বসার বেঞ্চগুলোতে বিকেলে প্রচুর মানুষ সমবেত হন নদীর শীতল বাতাস উপভোগ করতে। শান্ত নদীর বুকে কাঠের নৌকার মন্থর গতি এবং গোধূলির রক্তিম আভার ঝিলিক এক অপার্থিব প্রশান্তি এনে দেয়। নদীতীরের দোকানে গরম চা আর চটপটি-ফুচকা খাওয়ার আসর সান্ধ্যকালীন ভ্রমণকে আরও উপভোগ্য করে তোলে। শহরের বুকে প্রকৃতির নির্মল ছোঁয়া পেতে নবগঙ্গার পাড় এক দারুণ স্থান।",
            "locationEn": jh_raw['tour_spots'][3]['location'],
            "locationBn": "ঝিনাইদহ শহর ও জেলা নদীতীর, ঝিনাইদহ",
            "mapUrl": jh_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Kapotakkho River Corridor",
            "nameBn": "কপোতাক্ষ নদ করিডোর",
            "categoryEn": "Literary & Ecotourism River Landscape",
            "categoryBn": "ঐতিহাসিক নদী অববাহিকা ও গ্রামীণ নিসর্গ",
            "descEn": "The Kapotakkho River Corridor, meandering along the southern boundaries of Jhenaidah into Jashore and Khulna, is a poignantly scenic river landscape steeped in Bengali literary heritage. Celebrated in the immortal sonnets of epic poet Michael Madhusudan Dutt, the river flows past quiet pastoral hamlets, date-palm plantations, and blooming water lily ponds. Leisurely boat excursions along the river bends allow travelers to experience the timeless, undisturbed pace of rural deltaic life where fishermen cast nets from lightweight canoes. The tranquil river breezes and gentle ripples provide an ideal sanctuary for writers, photographers, and travelers seeking authentic peace. It represents the poetic natural soul of southwestern Bangladesh.",
            "descBn": "ঝিনাইদহের সীমানা ছুঁয়ে প্রবাহিত কপোতাক্ষ নদ বাংলা সাহিত্যের এক চিরন্তন ও অমর স্মারক, যা মহাকবি মাইকেল মধুসূদন দত্তের বিখ্যাত সনেটের মাধ্যমে বিশ্বজুড়ে পরিচিতি লাভ করেছে। নদীর দুই তীরে গড়ে ওঠা শান্ত পল্লী প্রকৃতি, খেজুর গাছের সারি এবং শাপলা ফোটা বিলের দৃশ্য চোখ জুড়িয়ে দেয়। কপোতাক্ষের বুকে ছোট কাঠের নৌকায় চড়ে ভেসে বেড়ানোর সময় কবির স্মৃতি ও নদীমাতৃক জীবনের মায়াবী রূপ গভীরভাবে উপলব্ধি করা যায়। শান্ত শীতল বাতাস আর নদীর কলতান শহুরে জীবনের সমস্ত ক্লান্তি দূর করে দেয়। সাহিত্য ও নদীপ্রকৃতির এক অপূর্ব মিলনমেলা এই কপোতাক্ষ নদ করিডোর।",
            "locationEn": jh_raw['tour_spots'][4]['location'],
            "locationBn": "ঝিনাইদহ জেলা অববাহিকা, ঝিনাইদহ",
            "mapUrl": jh_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('jhenaidah', jhenaidah_data)

# ==========================================
# 17. KHULNA
# ==========================================
kh_raw = all_data['khulna']
khulna_data = {
    "slug": "khulna",
    "en": "Khulna",
    "bn": "খুলনা",
    "hero_title_en": "Khulna Industrial Metropolis, Rupsha River & Sundarbans Gateway",
    "hero_title_bn": "খুলনার রূপসা নদীতীর, বিশ্ব ঐতিহ্য সুন্দরবন ও রবীন্দ্র স্মৃতিধাম",
    "hero_sub_en": "Colonial South Dihi Rabindra Memorial, iconic Khan Jahan Ali Rupsha Bridge, and wild mangrove gateway at Karamjal.",
    "hero_sub_bn": "দক্ষিণডিহির ঐতিহাসিক রবীন্দ্র স্মৃতিকেন্দ্র, রূপসা নদীর ওপর খান জাহান আলী সেতু ও করমজলের বন্যপ্রাণী অভয়ারণ্য।",
    "tagline_en": "The third-largest industrial and commercial metropolis of Bangladesh, gateway to the UNESCO Sundarbans mangrove forest, graced by the majestic Rupsha River and historic literary heritage.",
    "tagline_bn": "বাংলাদেশের তৃতীয় বৃহত্তম বিভাগীয় ও শিল্পনগরী, যা রূপসা নদীর উত্তাল রূপ, সুন্দরবনের প্রধান প্রবেশদ্বার করমজল, দক্ষিণডিহি রবীন্দ্র কমপ্লেক্স এবং রূপসা সেতুর জন্য আন্তর্জাতিকভাবে সুপরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/khulna/carousel-1.webp",
            "titleEn": "Khan Jahan Ali Rupsha Bridge Sunset Vista",
            "titleBn": "রূপসা সেতু (খান জাহান আলী সেতু) ও সূর্যাস্ত",
            "subtitleEn": "Monumental Japanese-engineered cable bridge spanning the Rupsha River connecting Khulna to Mongla port",
            "subtitleBn": "রূপসা নদীর ওপর নির্মিত আধুনিক দৃষ্টিনন্দন সেতু যেখান থেকে রূপসা ও ভৈরবের অপূর্ব মিলনমেলা দেখা যায়"
        },
        {
            "id": 2,
            "image": "images/districts/khulna/carousel-2.webp",
            "titleEn": "Sundarbans Gateway at Karamjal Eco Tourism Center",
            "titleBn": "করমজল সুন্দরবন ইকো ট্যুরিজম ও বন্যপ্রাণী প্রজনন কেন্দ্র",
            "subtitleEn": "Wild mangrove eco-reserve in the northern Sundarbans famous for saltwater crocodiles and spotted deer trails",
            "subtitleBn": "পশুর নদীর তীরে সুন্দরবনের প্রবেশমুখে অবস্থিত কুমির প্রজনন কেন্দ্র, কাঠের ট্রেইল ও হরিণ অভয়ারণ্য"
        },
        {
            "id": 3,
            "image": "images/districts/khulna/carousel-3.webp",
            "titleEn": "South Dihi Rabindra Memorial Complex Heritage",
            "titleBn": "দক্ষিণডিহি রবীন্দ্র স্মৃতি কমপ্লেক্স",
            "subtitleEn": "Historic ancestral home of Rabindranath Tagore's wife Mrinalini Devi in Fultala surrounded by ancient gardens",
            "subtitleBn": "ফুলতলায় অবস্থিত বিশ্বকবির শ্বশুরবাড়ি ও পৈতৃক ভিটা যা বর্তমানে একটি সমৃদ্ধ জাতীয় রবীন্দ্র জাদুঘর"
        },
        {
            "id": 4,
            "image": "images/districts/khulna/carousel-4.webp",
            "titleEn": "Rupsha Riverfront Historic Marine Boulevard",
            "titleBn": "রূপসা নদীতীর ও ঐতিহাসিক লঞ্চ ঘাট",
            "subtitleEn": "Bustling industrial riverfront where passenger steamers, cargo vessels, and fishing boats cruise daily",
            "subtitleBn": "খুলনা শহরের প্রাণকেন্দ্রে অবস্থিত রূপসা নদীর ব্যস্ত ঘাট ও নদীর বুকে ভেসে থাকা জাহাজের দৃশ্য"
        },
        {
            "id": 5,
            "image": "images/districts/khulna/carousel-5.webp",
            "titleEn": "Historic Jashore Road Centenary Tree Avenue",
            "titleBn": "ঐতিহাসিক যশোর রোড ও শতবর্ষী রেইনট্রি",
            "subtitleEn": "Iconic highway avenue shaded by colossal two-century-old rain trees immortalized in Allen Ginsberg's 1971 poem",
            "subtitleBn": "অ্যালেন গিন্সবার্গের বিখ্যাত কবিতায় অমর হওয়া শতবর্ষী বিশালাকার বৃক্ষশোভিত ঐতিহাসিক মহাসড়ক"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "South Dihi Rabindra Memorial Complex",
            "nameBn": "দক্ষিণডিহি রবীন্দ্র স্মৃতি কমপ্লেক্স",
            "categoryEn": "National Literary Heritage Palace & Museum",
            "categoryBn": "বিশ্বকবির স্মৃতিধন্য ঐতিহাসিক বাসভবন ও জাদুঘর",
            "descEn": "The South Dihi Rabindra Memorial Complex in Fultala Upazila is the hallowed ancestral estate of Mrinalini Devi (Bhabatarini Roy Chowdhury), the revered wife of Nobel laureate Rabindranath Tagore, as well as the maternal home of Tagore's mother Sarada Devi. Tagore visited this picturesque country mansion on multiple occasions during his youth and marriage, finding creative inspiration in the quiet village environment. The historic two-story brick residence has been conserved as a national museum housing rare photographs of the poet's family, vintage period furniture, original letters, and Tagore family genealogical archives. The surrounding brick courtyards feature ancient mango and olive trees alongside a life-sized bronze bust of Tagore. It stands as an essential pilgrimage site for literary enthusiasts exploring Tagore's intimate family connections to Bengal.",
            "descBn": "ফুলতলা উপজেলার দক্ষিণডিহিতে অবস্থিত রবীন্দ্র স্মৃতি কমপ্লেক্স বিশ্বকবি রবীন্দ্রনাথ ঠাকুরের স্ত্রী মৃণালিনী দেবী এবং কবির মাতা সারদা দেবীর পূর্বপুরুষদের এক পরম ঐতিহাসিক ও পুণ্যময় স্মৃতিধাম। যৌবনে ও বিবাহের পর কবিগুরু এই সুরম্য গ্রামীণ বাড়িতে একাধিকবার আগমন করেছিলেন এবং এখানকার শান্ত পরিবেশ তাঁর মনে গভীর প্রভাব ফেলেছিল। উপনিবেশিক স্থাপত্যের দোতলা প্রাচীন ভবনটিকে একটি সমৃদ্ধ জাদুঘরে রূপান্তর করা হয়েছে, যেখানে সংরক্ষিত আছে কবি ও তাঁর পরিবারের দুর্লভ আলোকচিত্র, প্রাচীন আসবাবপত্র এবং ঐতিহাসিক নথি। বাড়ির সবুজ চত্বরে রয়েছে রবীন্দ্রনাথ ও মৃণালিনী দেবীর সুন্দর আবক্ষ ভাস্কর্য এবং শতাব্দীপ্রাচীন বৃক্ষরাজি। রবীন্দ্র অনুরাগী ও সাহিত্যপ্রেমীদের কাছে এই দক্ষিণডিহি এক পরম আবেগময় তীর্থস্থান।",
            "locationEn": kh_raw['hist_spots'][0]['location'],
            "locationBn": "দক্ষিণডিহি, ফুলতলা, খুলনা",
            "mapUrl": kh_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Khulna Divisional Museum",
            "nameBn": "খুলনা বিভাগীয় জাদুঘর",
            "categoryEn": "Regional Archaeological & Antiquities Museum",
            "categoryBn": "বিভাগীয় প্রত্নতাত্ত্বিক জাদুঘর ও ইতিহাস প্রদর্শশালা",
            "descEn": "Situated in the central Shivbari area of Khulna city, the Khulna Divisional Museum is the second-largest archaeological museum in Bangladesh, curated by the Department of Archaeology. The sprawling two-story institution exhibits thousands of priceless antiquities spanning ancient, medieval, and colonial eras recovered from excavations across southern Bengal. Galleries showcase remarkable black stone sculptures of Buddhist and Hindu deities from the Gupta and Pala periods, terracotta plaques from Barobazar and Bharat Bhayna, ancient gold and punch-marked coins, and medieval brass cannons. A dedicated ethnographic section highlights indigenous cultural heritage, coastal boatbuilding models, and Sundarbans folklore artifacts. It provides an indispensable historical education for visitors exploring the ancient civilizational roots of Khulna division.",
            "descBn": "খুলনা শহরের শিববাড়ি এলাকায় অবস্থিত খুলনা বিভাগীয় জাদুঘর দেশের দ্বিতীয় বৃহত্তম ও অত্যন্ত সমৃদ্ধ প্রত্নতাত্ত্বিক জাদুঘর। প্রত্নতত্ত্ব অধিদপ্তর কর্তৃক পরিচালিত দ্বিতল এই আধুনিক জাদুঘরে সংরক্ষিত আছে দক্ষিণ বাংলার বিভিন্ন স্থান থেকে উদ্ধারকৃত হাজার হাজার বছরের প্রাচীন অমূল্য প্রত্নসম্পদ। এর গ্যালারিগুলোতে স্থান পেয়েছে গুপ্ত, পাল ও সেন যুগের কালো ব্যাসল্ট পাথরের মূর্তি, বারোবাজারের সুলতানি আমলের পোড়ামাটির ফলক, প্রাচীন রৌপ্যমুদ্রা ও মধ্যযুগীয় কামান। এছাড়া সুন্দরবনের ঐতিহ্যবাহী নৌকার মডেল ও উপকূলীয় মানুষের জীবনাচারের নানা নৃতাত্ত্বিক নিদর্শন এখানে প্রদর্শিত হয়েছে। দক্ষিণবঙ্গের ইতিহাস ও প্রাচীন সভ্যতা সম্পর্কে জানতে এই জাদুঘরটি এক অত্যন্ত গুরুত্বপূর্ণ শিক্ষণীয় স্থান।",
            "locationEn": kh_raw['hist_spots'][1]['location'],
            "locationBn": "খুলনা শহর, খুলনা",
            "mapUrl": kh_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Gollamari Liberation War Memorial Area",
            "nameBn": "গল্লামারী মুক্তিযুদ্ধ স্মৃতিসৌধ এলাকা",
            "categoryEn": "1971 National Liberation War Memorial Ground",
            "categoryBn": "১৯৭১ সালের মুক্তিযুদ্ধ স্মৃতিসৌধ ও বধ্যভূমি চত্বর",
            "descEn": "The Gollamari Liberation War Memorial Area, located along the Moyur River near Khulna University, is the most sacred and poignant historical monument in southwestern Bangladesh, commemorating the supreme sacrifices of the 1971 War of Independence. During the nine-month war, occupying Pakistani forces converted the former radio transmission complex here into an extermination camp, executing thousands of Bengali intellectuals, students, and freedom fighters before dumping their bodies into the river. Following liberation, a monumental memorial monument featuring a soaring central obelisk, sculpted murals of freedom fighters, and peaceful reflecting pools was erected on the sanctified soil. Every year on Independence Day and Victory Day, tens of thousands of citizens gather with floral wreaths to honor the martyrs. It stands as an essential, deeply moving monument of national memory.",
            "descBn": "খুলনা বিশ্ববিদ্যালয়ের সন্নিকটে ময়ূর নদীর তীরে অবস্থিত গল্লামারী মুক্তিযুদ্ধ স্মৃতিসৌধ ১৯৭১ সালের মহান মুক্তিযুদ্ধে শহীদ বীর মুক্তিযোদ্ধাদের আত্মত্যাগের এক পরম পবিত্র জাতীয় স্মারক। মুক্তিযুদ্ধের নয় মাস পাকিস্তানি হানাদার বাহিনী এখানকার রেডিও ট্রান্সমিশন ভবনে নির্বিচারে শত শত নিরীহ বাঙালি, বুদ্ধিজীবী ও মুক্তিযোদ্ধাদের হত্যা করে ময়ূর নদীতে ফেলে দিয়েছিল। বিজয়ের পর এই পুণ্যভূমিতে নির্মাণ করা হয় একটি দৃষ্টিনন্দন ও ভাবগাম্ভীর্যপূর্ণ স্মৃতিসৌধ, যাতে রয়েছে সুউচ্চ স্তম্ভ, মুক্তিযুদ্ধের ম্যুরাল এবং শান্ত জলাশয়। প্রতি বছর স্বাধীনতা ও বিজয় দিবসে সর্বস্তরের মানুষ এখানে শহীদদের স্মরণে পুষ্পস্তবক অর্পণ করেন। দেশের স্বাধীনতার রক্তঝরা ইতিহাস অনুধাবনে এটি এক অত্যন্ত তাৎপর্যপূর্ণ স্থান।",
            "locationEn": kh_raw['hist_spots'][2]['location'],
            "locationBn": "গল্লামারী, খুলনা",
            "mapUrl": kh_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Rupsha Bridge (Khan Jahan Ali Bridge)",
            "nameBn": "রূপসা সেতু (খান জাহান আলী সেতু)",
            "categoryEn": "Monumental River Gateway & Modern Engineering Marvel",
            "categoryBn": "প্রকৌশল বিস্ময় ও আধুনিক রূপসা সেতু",
            "descEn": "Formally named the Khan Jahan Ali Bridge and spanning 1.36 kilometers across the turbulent Rupsha River, the Rupsha Bridge is an engineering marvel constructed with Japanese technical assistance and opened in 2005. Engineered to handle heavy commercial cargo traffic between Khulna and the seaport of Mongla, the sleek concrete box-girder bridge features graceful curved ramps and elevated pedestrian promenades. The summit of the bridge deck provides a breathtaking panoramic viewpoint overlooking the convergence of the Rupsha and Bhairab rivers, where passenger launches, cargo ships, and fishing trawlers cruise below. Illuminated brightly at night with vibrant street lamps, the bridge has become the primary open-air civic landmark of Khulna city. It stands as a symbol of modern development and regional connectivity.",
            "descBn": "রূপসা নদীর ওপর নির্মিত ১.৩৬ কিলোমিটার দীর্ঘ খান জাহান আলী সেতু (রূপসা সেতু) আধুনিক প্রকৌশলবিদ্যার এক অনিন্দ্যসুন্দর নিদর্শন, যা জাপানি সহায়তায় ২০০৫ সালে উদ্বোধন করা হয়েছিল। খুলনা শহরের সাথে মোংলা সমুদ্র বন্দর ও দক্ষিণাঞ্চলের যোগাযোগে এই সেতু এক বৈপ্লবিক পরিবর্তন এনেছে। সেতুর ওপর দিয়ে হাঁটার পথ থেকে নিচে রূপসা ও ভৈরব নদের সুবিশাল সঙ্গমস্থল এবং নদীতে চলাচলকারী জাহাজের অপূর্ব দৃশ্য এক পলকে দেখা যায়। রাতের বেলা আধুনিক আলোকসজ্জায় পুরো সেতুটি রূপালী আলোর মালায় সেজে ওঠে যা দেখতে প্রতিদিন শত শত পর্যটক ভিড় জমান। মনোরম নদীপ্রকৃতি ও আধুনিক স্থাপত্যের চমৎকার নিদর্শন হিসেবে রূপসা সেতু খুলনার অন্যতম প্রধান গর্ব।",
            "locationEn": kh_raw['hist_spots'][3]['location'],
            "locationBn": "রূপসা নদী, খুলনা",
            "mapUrl": kh_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Historic Riverfront and Launch-Ghat Area",
            "nameBn": "ঐতিহাসিক নদী বন্দর ও লঞ্চ ঘাট এলাকা",
            "categoryEn": "Heritage Maritime Port & Riverfront Quarter",
            "categoryBn": "ঐতিহাসিক নদী বন্দর, প্রাচীন ঘাট ও নৌবাণিজ্য এলাকা",
            "descEn": "The Historic Riverfront and Launch-Ghat Area in central Khulna along the Bhairab and Rupsha rivers has operated for over a century as the bustling maritime nerve center of southwestern Bangladesh. Flanked by colonial-era brick custom houses, historic jute mills, and riverside godowns, the waterfront bustles constantly with long-distance passenger steamers (including the vintage Rocket Paddle Steamers), cargo barges, and wooden country dinghies. Merchants from across the Sundarbans coastal belt converge here to trade forest honey, dried fish, salt, and seasonal farm harvests. The aromatic blend of fresh river breezes, street tea stalls, and the distant blasts of steamship horns evokes the romantic golden era of Bengal river commerce. It remains a living historical museum of the nation's inland shipping culture.",
            "descBn": "ভৈরব ও রূপসা নদীর তীরে অবস্থিত খুলনার ঐতিহাসিক নদী বন্দর ও লঞ্চ ঘাট এলাকা এক শতাব্দীরও বেশি সময় ধরে দক্ষিণ বাংলার নৌবাণিজ্য ও যোগাযোগের প্রধান কেন্দ্র হিসেবে কাজ করে আসছে। ব্রিটিশ আমলের পুরোনো পাটের গুদাম, শানবাঁধানো ঘাট এবং ঐতিহ্যবাহী কাঠের আড়ত আজও এই নদীতীরের গৌরবময় অতীতের কথা মনে করিয়ে দেয়। ঐতিহাসিক রকেট প্যাডেল স্টিমার থেকে শুরু করে আধুনিক যাত্রীবাহী লঞ্চ ও পণ্যবাহী জাহাজের অবিরাম যাতায়াত এই ঘাটকে চব্বিশ ঘণ্টা প্রাণবন্ত রাখে। সুন্দরবনের খাঁটি মধু, গোলপাতা ও মাছের বিশাল পাইকারি বাণিজ্য এই ঘাটকে কেন্দ্র করেই পরিচালিত হয়। নদীমাতৃক বাংলার আসল স্পন্দন ও ইতিহাসের ছোঁয়া পেতে এই পুরোনো বন্দর এলাকা এক চমৎকার স্থান।",
            "locationEn": kh_raw['hist_spots'][4]['location'],
            "locationBn": "খুলনা শহর নদীতীর, খুলনা",
            "mapUrl": kh_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Rupsha Riverfront",
            "nameBn": "রূপসা নদীতীর",
            "categoryEn": "Scenic Urban Waterfront & Promenade",
            "categoryBn": "নয়নাভিরাম রূপসা নদীতীর ও বৈকালিক ওয়াকওয়ে",
            "descEn": "The Rupsha Riverfront is the beloved scenic promenade and environmental heart of Khulna city, where the powerful river flows gracefully under wide skies. The municipal waterfront features landscaped pedestrian walkways, decorative garden lamps, open-air seating terraces, and boat-boarding pontoons where residents and tourists gather to enjoy refreshing evening breezes. Traditional wooden motor launches offer scenic cruises across the river, providing close-up views of international cargo vessels and naval craft anchored in the stream. Sunset over the Rupsha River paints the water in shimmering crimson hues while riverside vendors serve hot tea, roasted peanuts, and local river fish snacks. It is the premier leisure and gathering ground for families and travelers visiting Khulna.",
            "descBn": "রূপসা নদীতীর খুলনা শহরের অন্যতম প্রধান প্রাকৃতিক ও বিনোদন কেন্দ্র, যেখানে প্রমত্তা রূপসা নদী তার রূপের ডালি সাজিয়ে বয়ে চলেছে। নদীর পাড়ে গড়ে তোলা সুন্দর ওয়াকওয়ে ও বসার স্থানে প্রতিদিন বিকেলে মুক্ত বাতাস উপভোগ করতে বহু মানুষ সমবেত হন। ইঞ্জিনচালিত কাঠের নৌকায় চড়ে নদীর বুক চিরে ঘুরে বেড়ানো এবং নদীতে নোঙর করে থাকা বিশালাকার জাহাজের পাশ দিয়ে যাওয়ার অভিজ্ঞতা অত্যন্ত আনন্দদায়ক। বিকেলের শান্ত আলোয় নদীর বুকে সূর্যাস্তের রঙের খেলা এক জাদুকরী মায়া তৈরি করে যা আলোকচিত্রীদের প্রিয় দৃশ্য। নদীর তাজা বাতাসে সময় কাটানো ও মুখরোচক খাবার উপভোগে রূপসা নদীতীর এক অনন্য স্থান।",
            "locationEn": kh_raw['tour_spots'][0]['location'],
            "locationBn": "খুলনা শহর, খুলনা",
            "mapUrl": kh_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Khan Jahan Ali Bridge Viewpoint",
            "nameBn": "খান জাহান আলী সেতু ভিউপয়েন্ট",
            "categoryEn": "Panoramic Bridge Observation Deck",
            "categoryBn": "রূপসা সেতুর চূড়া ও প্রাকৃতিক পর্যবেক্ষণ পয়েন্ট",
            "descEn": "The Khan Jahan Ali Bridge Viewpoint atop the pedestrian walkway of Rupsha Bridge is one of the most thrilling elevated vantage points in southwestern Bangladesh. Rising dozens of meters above the swirling water, the observation point offers a complete 360-degree aerial panorama encompassing the urban skyline of Khulna, expansive green mangrove fringes, and the convergence of two major river systems. Standing on the breezy bridge deck as evening falls, visitors can watch stars emerge while the rhythmic lights of passenger launches reflect on the waters below. Food vendors along the bridge approaches offer delicious street foods, spiced tea, and fresh local fruits. It is an unmissable sightseeing highlight for anyone touring Khulna.",
            "descBn": "রূপসা সেতুর ওপর অবস্থিত খান জাহান আলী সেতু ভিউপয়েন্ট খুলনার অন্যতম রোমাঞ্চকর ও জনপ্রিয় দর্শনীয় স্থান। সেতুর সুউচ্চ পদচারী পথ থেকে নিচে তাকালে দেখা যায় রূপসা ও ভৈরব নদের মিলনস্থলের বিশাল জলরাশি এবং দূরবর্তী সুন্দরবনের সবুজ প্রান্তরেখা। বিকেলের মিষ্টি রোদে দাঁড়িয়ে নদীর শীতল বাতাসের ছোঁয়া নেওয়ার অনুভূতি অত্যন্ত অসাধারণ। সন্ধ্যার পর যখন শহরের আলো নদীর বুকে জ্বলে ওঠে, তখন পুরো পরিবেশ এক রূপকথার মতো রূপ ধারণ করে। বন্ধুদের সাথে আড্ডা দেওয়া, ছবি তোলা এবং নদীর বিশালতা অবলোকন করতে এই ভিউপয়েন্টটিতে প্রতিদিন শত শত ভ্রমণপ্রেমী ভিড় জমান।",
            "locationEn": kh_raw['tour_spots'][1]['location'],
            "locationBn": "রূপসা নদী, খুলনা",
            "mapUrl": kh_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Sundarbans Gateway at Karamjal",
            "nameBn": "করমজল সুন্দরবন ইকো ট্যুরিজম কেন্দ্র",
            "categoryEn": "World Heritage Mangrove Gateway & Wildlife Sanctuary",
            "categoryBn": "সুন্দরবনের প্রবেশদ্বার, কুমির প্রজনন কেন্দ্র ও হরিণ অভয়ারণ্য",
            "descEn": "Karamjal Eco Tourism and Wildlife Breeding Center in the northern reaches of the Sundarbans is the most popular, accessible gateway to the world's largest mangrove forest. Located along the Pasur River, the eco-reserve features a famous saltwater crocodile breeding center, a sprawling spotted deer enclosure, and a half-kilometer elevated wooden canopy boardwalk winding deep through dense mangrove forest. Walking along the wooden boardwalk under the shady canopy of sundari, bain, and keora trees, visitors encounter playful rhesus macaques, colorful kingfishers, mudskippers, and fiddle crabs. The high observation watchtower provides stunning panoramic views of the untamed mangrove wilderness stretching toward the Bay of Bengal. It offers an unforgettable, family-friendly wildlife adventure into Bangladesh's wild soul.",
            "descBn": "সুন্দরবনের প্রবেশমুখে পশুর নদীর তীরে অবস্থিত করমজল ইকো ট্যুরিজম কেন্দ্র সুন্দরবন দেখার সবচেয়ে জনপ্রিয় ও সুবিধাজনক স্থান। এখানে রয়েছে বাংলাদেশের একমাত্র সরকারি নোনা পানির কুমির প্রজনন কেন্দ্র এবং শত শত মায়াবী চিত্রা হরিণের অভয়ারণ্য। বনের ভেতরে হেঁটে দেখার জন্য তৈরি করা হয়েছে প্রায় দেড় কিলোমিটার দীর্ঘ কাঠের ওয়াকওয়ে বা ট্রেইল, যা ধরে হাঁটলে সুন্দরবনের শ্বাসমূলযুক্ত সুন্দরী ও কেওড়া গাছের বনানী অত্যন্ত কাছ থেকে প্রত্যক্ষ করা যায়। বনের বানর, নানা প্রজাতির পাখি ও কাদায় খেলে বেড়ানো লাল কাঁকড়া পর্যটকদের মুগ্ধ করে। সুউচ্চ ওয়াচ টাওয়ার থেকে পুরো সুন্দরবনের বুনো রূপ অবলোকন করা যায়। সুন্দরবনের প্রথম রোমাঞ্চকর অভিজ্ঞতার জন্য করমজল অতুলনীয়।",
            "locationEn": kh_raw['tour_spots'][2]['location'],
            "locationBn": "করমজল, মোংলা নৌপথ, খুলনা অঞ্চল",
            "mapUrl": kh_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Jashore Road Tree Avenue",
            "nameBn": "ঐতিহাসিক যশোর রোড বৃক্ষবীথি",
            "categoryEn": "Historic Rain-Tree Heritage Highway",
            "categoryBn": "শতবর্ষী রেইনট্রি শোভিত ঐতিহাসিক মহাসড়ক",
            "descEn": "The Jashore Road Tree Avenue running between Khulna, Jashore, and the international border at Benapole is one of the most historically famous and picturesque highways in the subcontinent. Immortalized worldwide by American Beat poet Allen Ginsberg in his 1971 epic poem 'September on Jessore Road', which captured the refugee crisis during Bangladesh's Liberation War, the road is famous for its colossal, centuries-old rain trees. Planted originally during the mid-nineteenth century by local zamindars, the giant trees intertwine high overhead to form a living emerald canopy spanning miles of asphalt. Driving or cycling along this historic shaded corridor provides a breathtaking, poetic encounter with living historical memory and road geography. It remains a cherished natural and literary monument of Bangladesh.",
            "descBn": "খুলনা থেকে যশোর হয়ে বেনাপোল সীমান্ত পর্যন্ত চলে যাওয়া ঐতিহাসিক যশোর রোড উপমহাদেশের অন্যতম বিখ্যাত ও ছায়াঘেরা দৃষ্টিনন্দন মহাসড়ক। ১৯৭১ সালের মুক্তিযুদ্ধের সময় লাখ লাখ শরণার্থীর দুঃখ-দুর্দশা নিয়ে মার্কিন কবি অ্যালেন গিন্সবার্গের বিখ্যাত কবিতা 'সেপ্টেম্বর অন যশোর রোড'-এ এই রাস্তাটি বিশ্বজুড়ে অমর হয়ে আছে। উনিশ শতকে জমিদার কালী পোদ্দার কর্তৃক রোপিত শতবর্ষী বিশালাকার রেইনট্রি গাছগুলো রাস্তার ওপর এক সবুজ প্রাকৃতিক ছাদ তৈরি করে রেখেছে। এই ঐতিহাসিক ছায়াঘেরা পথ ধরে গাড়ি চালানো কিংবা হাঁটার সময় ইতিহাসের এক গভীর আবেগময় অনুভূতি সৃষ্টি হয়। প্রাকৃতিক সৌন্দর্য ও মুক্তিযুদ্ধের স্মৃতিবাহী এক চিরন্তন জীবন্ত স্মারক এই যশোর রোড।",
            "locationEn": kh_raw['tour_spots'][3]['location'],
            "locationBn": "খুলনা–যশোর মহাসড়ক, খুলনা",
            "mapUrl": kh_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Khulna Riverside Promenade Area",
            "nameBn": "খুলনা রিভারসাইড ওয়াকওয়ে ও পার্ক এলাকা",
            "categoryEn": "Civic Waterfront Promenade & Green Park",
            "categoryBn": "পৌর রিভারফ্রন্ট পার্ক ও নাগরিক বিনোদন কেন্দ্র",
            "descEn": "The Khulna Riverside Promenade Area along the revitalized waterfront of the Bhairab and Rupsha rivers serves as a major urban parkland and family recreational haven. Featuring paved jogging paths, open plazas, illuminated floral gazebos, and waterfront viewing terraces, the area attracts thousands of townspeople seeking relaxation and fresh coastal-river breezes. Children play in dedicated amusement areas while visitors enjoy refreshing lemon tea and spicy regional delicacies served by open-air cafeterias. The tranquil river horizon, combined with the passage of brightly illuminated passenger launches at night, creates a wonderfully serene urban ambiance. It stands as a vibrant testament to Khulna's modern transformation into an eco-friendly waterfront metropolis.",
            "descBn": "ভৈরব ও রূপসা নদীর কোল ঘেঁষে গড়ে তোলা খুলনা রিভারসাইড ওয়াকওয়ে ও পার্ক এলাকা স্থানীয় নাগরিক ও পর্যটকদের জন্য এক চমৎকার উন্মুক্ত বিনোদন কেন্দ্র। সুন্দর আলোকসজ্জা, শানবাঁধানো পথ, ফুলের বাগান এবং নদীর পাড়ে বসার জন্য আরামদায়ক বেঞ্চ এই স্থানটিকে অত্যন্ত পরিপাটি করেছে। বিকেলে নদীর মিষ্টি হাওয়া উপভোগ করতে এবং পরিবারের সদস্যদের সাথে সময় কাটাতে বহু মানুষ এখানে আসেন। শিশুদের জন্য খেলার সুন্দর জায়গা এবং নদীর পাড়ের ক্যাফেগুলোতে গরম চা ও স্ন্যাকসের সুব্যবস্থা রয়েছে। রাতের বেলা নদীর বুকে জাহাজের আলো আর শহরের আলো মিলেমিশে এক চমৎকার দৃশ্য তৈরি করে। খুলনার নাগরিক জীবনে স্বস্তির ছোঁয়া পেতে এই নদীতীর এক দারুণ আশ্রয়।",
            "locationEn": kh_raw['tour_spots'][4]['location'],
            "locationBn": "খুলনা শহর, খুলনা",
            "mapUrl": kh_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('khulna', khulna_data)

# ==========================================
# 18. CHUADANGA
# ==========================================
ch_raw = all_data['chuadanga']
chuadanga_data = {
    "slug": "chuadanga",
    "en": "Chuadanga",
    "bn": "চুয়াডাঙ্গা",
    "hero_title_en": "Chuadanga Historic Carew Distillery & Mathabhanga River",
    "hero_title_bn": "চুয়াডাঙ্গার ঐতিহাসিক কেরু অ্যান্ড কোম্পানি ও মাথাভাঙ্গা নদীতীর",
    "hero_sub_en": "1897 AD Carew & Company sugar and distillery heritage in Darshana, historic railway junction, and serene riverbanks.",
    "hero_sub_bn": "১৮৯৭ সালের প্রাচীন কেরু অ্যান্ড কোম্পানি চিনিকল ও ডিস্টিলারি, দর্শনা রেলওয়ে জংশন ও মাথাভাঙ্গা নদীর শান্ত প্রকৃতি।",
    "tagline_en": "The pioneering industrial and agricultural gateway of southwestern Bengal, celebrated for the century-old Carew & Company distillery, historic railway border crossings at Darshana, and sweet mango orchards.",
    "tagline_bn": "দক্ষিণ-পশ্চিমাঞ্চলের প্রথম মুক্ত মহকুমা ও শিল্প ঐতিহ্যের জেলা, যা দর্শনার শতবর্ষী কেরু অ্যান্ড কোম্পানি, আন্তর্জাতিক রেলওয়ে জংশন এবং মাথাভাঙ্গা নদীর রূপময় নিসর্গের জন্য সুপরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/chuadanga/carousel-1.webp",
            "titleEn": "Carew & Company Historic Industrial Distillery",
            "titleBn": "কেরু অ্যান্ড কোম্পানি ঐতিহাসিক ডিস্টিলারি ও চিনিকল",
            "subtitleEn": "1897 AD British-era sugar mill and distillery complex in Darshana preserving vintage steam machinery",
            "subtitleBn": "১৮৯৭ সালে প্রতিষ্ঠিত উপমহাদেশের প্রাচীনতম ও বিখ্যাত চিনিকল ও ডিস্টিলারির সুপ্রাচীন শিল্প স্থাপত্য"
        },
        {
            "id": 2,
            "image": "images/districts/chuadanga/carousel-2.webp",
            "titleEn": "Darshana Railway Junction Border Hub",
            "titleBn": "দর্শনা আন্তর্জাতিক রেলওয়ে জংশন ও বন্দর",
            "subtitleEn": "Historic broad-gauge railway crossing connecting Bangladesh with India across lush border landscapes",
            "subtitleBn": "ব্রিটিশ আমলের সুবিশাল রেলওয়ে প্ল্যাটফর্ম ও ভারত-বাংলাদেশ মৈত্রী এক্সপ্রেসের আন্তর্জাতিক রেল ট্রানজিট"
        },
        {
            "id": 3,
            "image": "images/districts/chuadanga/carousel-3.webp",
            "titleEn": "Mathabhanga Riverbank Scenic Green Waters",
            "titleBn": "মাথাভাঙ্গা নদীতীরের স্নিগ্ধ সবুজ নিসর্গ",
            "subtitleEn": "Meandering river flowing past Chuadanga town framed by bamboo groves and tranquil sandy shores",
            "subtitleBn": "চুয়াডাঙ্গা শহরের কোল ঘেঁষে বয়ে যাওয়া শান্ত নদীপ্রবাহ যা ভ্রমণপ্রেমীদের উপহার দেয় নির্মল বাতাস ও সূর্যাস্ত"
        },
        {
            "id": 4,
            "image": "images/districts/chuadanga/carousel-4.webp",
            "titleEn": "Taltala Park Civic Lake & Gardens",
            "titleBn": "তালতলা পার্কের মনোরম লেক ও উদ্যান",
            "subtitleEn": "Urban recreation oasis in Chuadanga town featuring pedal boating lakes and lush floral promenades",
            "subtitleBn": "পৌর এলাকার সুন্দর বিনোদন পার্ক যেখানে শান্ত লেকে বোটিং ও সবুজ বাগানে সময় কাটানোর চমৎকার ব্যবস্থা"
        },
        {
            "id": 5,
            "image": "images/districts/chuadanga/carousel-5.webp",
            "titleEn": "Alamdanga Historic Railway Heritage Town",
            "titleBn": "আলমডাঙ্গা ঐতিহাসিক রেলওয়ে জনপদ",
            "subtitleEn": "Vintage 19th-century railway town preserving colonial brick architecture, old trading markets, and river bridges",
            "subtitleBn": "উনিশ শতকের প্রাচীন রেলওয়ে স্টেশন, সুপ্রাচীন বাণিজ্যিক আড়ত ও ঐতিহ্যবাহী গ্রামীণ জনপদ"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Carew & Company Historic Distillery",
            "nameBn": "কেরু অ্যান্ড কোম্পানি ঐতিহাসিক ডিস্টিলারি",
            "categoryEn": "Centenary Industrial Heritage Complex",
            "categoryBn": "শতাব্দীপ্রাচীন শিল্প কারখানা ও ডিস্টিলারি কমপ্লেক্স",
            "descEn": "Established in 1897 by British entrepreneur John Carew, Carew & Company in Darshana, Damurhuda Upazila, is the oldest and only operational organic distillery and integrated sugar industrial complex in Bangladesh. Covering expansive acreage, the red-brick Victorian industrial compound features towering steam chimneys, heavy cast-iron boilers, historic sugarcane crushing mills, and massive copper distillation stills imported from Glasgow. The facility produces pharmaceutical-grade alcohol, organic vinegar, and celebrated confectionery byproducts derived from regional sugarcane harvests. Shaded by centenary rain trees and colonial-era staff quarters, the heritage factory preserves an extraordinary chapter of Bengal's late nineteenth-century industrial revolution. It stands as an iconic symbol of industrial resilience and engineering heritage.",
            "descBn": "১৮৯৭ সালে ব্রিটিশ উদ্যোক্তা জন কেরু কর্তৃক প্রতিষ্ঠিত দামুড়হুদা উপজেলার দর্শনায় অবস্থিত কেরু অ্যান্ড কোম্পানি বাংলাদেশের একমাত্র সরকারি ডিস্টিলারি ও প্রাচীনতম সমন্বিত চিনি শিল্প কমপ্লেক্স। লাল ইটের ভিক্টোরীয় স্থাপত্যে নির্মিত এই কারখানায় রয়েছে সুউচ্চ চিমনি, স্কটল্যান্ডের গ্লাসগো থেকে আনা প্রাচীন বাষ্পীয় বয়লার, সুবিশাল তামার পাতন পাত্র এবং আখ মাড়াই কল। এক শতাব্দীরও বেশি সময় ধরে এই প্রতিষ্ঠানটি উন্নতমানের চিনি, জৈব ভিনেগার এবং স্পিরিট উৎপাদন করে দেশের অর্থনীতিতে অনন্য অবদান রেখে আসছে। শতবর্ষী গাছের ছায়ায় ঘেরা ব্রিটিশ আমলের এই শিল্প কারখানাটি অবিভক্ত বাংলার শিল্প বিপ্লবের এক জীবন্ত স্মৃতি। শিল্প ইতিহাস ও প্রকৌশলবিদ্যার অনুরাগী ভ্রমণকারীদের জন্য এটি এক পরম দর্শনীয় স্থান।",
            "locationEn": ch_raw['hist_spots'][0]['location'],
            "locationBn": "দর্শনা, দামুড়হুদা, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Darshana Railway Junction",
            "nameBn": "দর্শনা রেলওয়ে জংশন",
            "categoryEn": "Historic International Railway Transit Hub",
            "categoryBn": "ঐতিহাসিক আন্তর্জাতিক রেলওয়ে জংশন ও সীমান্ত ট্রানজিট",
            "descEn": "Darshana Railway Junction in Chuadanga is one of the most historically significant broad-gauge railway border crossings in the subcontinent, inaugurated in 1862 under the Eastern Bengal Railway network. Situated right along the zero-point boundary with India opposite Gede in West Bengal, the junction historically facilitated massive passenger and commercial freight traffic connecting Kolkata with northern Bengal and Assam. Today, the station serves as the prestigious international customs and immigration terminal for the Maitree Express passenger train connecting Dhaka and Kolkata. The station features vintage covered iron-truss platforms, historic mechanical signal boxes, and colonial-era railway architecture. Strolling along the bustling platforms evokes the romance and diplomacy of cross-border railway travel.",
            "descBn": "১৮৬২ সালে ইস্টার্ন বেঙ্গল রেলওয়ের অধীনে প্রতিষ্ঠিত দর্শনা রেলওয়ে জংশন উপমহাদেশের অন্যতম প্রাচীন ও গুরুত্বপূর্ণ আন্তর্জাতিক ব্রডগেজ রেলওয়ে ট্রানজিট কেন্দ্র। ভারতের পশ্চিমবঙ্গের গেদে সীমান্তের ঠিক বিপরীত পাশে অবস্থিত এই স্টেশনটি অবিভক্ত বাংলায় কলকাতা থেকে ঢাকা, রাজশাহী ও আসামের যোগাযোগের মূল প্রবেশদ্বার ছিল। বর্তমানে এটি ঢাকা ও কলকাতার মধ্যে চলাচলকারী আন্তর্জাতিক 'মৈত্রী এক্সপ্রেস' ট্রেনের অন্যতম প্রধান কাস্টমস ও ইমিগ্রেশন স্টেশন হিসেবে ব্যবহৃত হচ্ছে। প্রাচীন লোহার ছাদযুক্ত প্ল্যাটফর্ম, ব্রিটিশ আমলের সিগন্যাল কেবিন এবং শতবর্ষী রেলওয়ে ভবনগুলো এর ঐতিহাসিক গুরুত্ব তুলে ধরে। আন্তর্জাতিক রেল যোগাযোগের গৌরবময় ইতিহাস প্রত্যক্ষ করতে দর্শনা জংশন অত্যন্ত আকর্ষণীয়।",
            "locationEn": ch_raw['hist_spots'][1]['location'],
            "locationBn": "দর্শনা, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Alamdanga Historic Rail Settlement",
            "nameBn": "আলমডাঙ্গা ঐতিহাসিক রেল জনপদ",
            "categoryEn": "Victorian Railway Town & Commercial Center",
            "categoryBn": "উপনিবেশিক রেলওয়ে জনপদ ও প্রাচীন বাণিজ্যিক আড়ত",
            "descEn": "Alamdanga is a venerable historic railway settlement that grew rapidly into a bustling commercial center following the opening of the Calcutta-Kushtia railway line in the late nineteenth century. Famous for handling massive regional trade in agricultural harvests, tobacco, jaggery, and handwoven textiles, the town preserves authentic colonial-era brick shophouses, wooden godowns, and vintage railway staff residences. The historic railway station features classical Victorian brickwork, high arched corridors, and cast-iron roof trusses. Flanked by the Mathabhanga and Kumar rivers, Alamdanga served as an essential multimodal transit hub where river barges met steam locomotives. Walking through its nostalgic bazaar streets reveals the enduring commercial vitality of southwestern Bengal.",
            "descBn": "উনিশ শতকের শেষভাগে কলকাতা-কুষ্টিয়া রেলপথ চালুর পর আলমডাঙ্গা দ্রুত এক অত্যন্ত গুরুত্বপূর্ণ রেলওয়ে জনপদ ও প্রধান বাণিজ্যিক কেন্দ্রে রূপান্তরিত হয়। তামাক, গুড়, ধান ও সুতি বস্ত্রের বিশাল পাইকারি আড়ত হিসেবে খ্যাত এই শহরে আজও ভিক্টোরীয় স্থাপত্যের লাল ইটের ভবন, প্রাচীন কাঠের গুদামঘর এবং রেলওয়ে বাংলো দেখা যায়। আলমডাঙ্গা স্টেশনের প্রাচীন প্ল্যাটফর্ম, খিলানযুক্ত বারান্দা এবং লোহার ছাদ তৎকালীন সময়ের চমৎকার নির্মাণরীতির পরিচয় দেয়। মাথাভাঙ্গা ও কুমার নদীর তীরে অবস্থিত হওয়ার কারণে এটি এককালে নদীবাণিজ্য ও রেল যোগাযোগের এক অনন্য মিলনস্থল ছিল। শতাব্দীর ঐতিহ্যবাহী বাণিজ্যিক আভিজাত্য প্রত্যক্ষ করতে আলমডাঙ্গার এই জনপদ অনন্য।",
            "locationEn": ch_raw['hist_spots'][2]['location'],
            "locationBn": "আলমডাঙ্গা, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Chuadanga Liberation War Memorial Sites",
            "nameBn": "চুয়াডাঙ্গা মুক্তিযুদ্ধ স্মৃতিসৌধ এলাকা",
            "categoryEn": "1971 National Liberation War Historic Memorials",
            "categoryBn": "১৯৭১ সালের মুক্তিযুদ্ধ স্মৃতিসৌধ ও প্রথম মুক্ত অঞ্চল",
            "descEn": "Chuadanga holds an immortal place in Bangladesh's independence history as the first subdivisional town to be liberated from occupying forces in late March 1971, briefly serving as the temporary administrative headquarters of the provisional Government of Bangladesh. The Liberation War Memorial Sites across Chuadanga town and surrounding battlegrounds commemorate the valiant resistance of Bengali freedom fighters and the sacrifices of martyrs. The central memorial monument features an imposing red brick cenotaph, inscribed rolls of honor, and landscaped surrounding gardens honoring fallen heroes. Historical plaques recount how patriotic citizens, police, and EPR soldiers united here to declare independence and raise the national flag. It represents a proud, deeply revered destination celebrating the birth of sovereign Bangladesh.",
            "descBn": "১৯৭১ সালের মহান মুক্তিযুদ্ধে চুয়াডাঙ্গা এক অবিস্মরণীয় ঐতিহাসিক গৌরবের অধিকারী, কারণ ২৬শে মার্চের পরপরই এটি পাকিস্তানি হানাদার মুক্ত হয়ে স্বাধীন বাংলাদেশের অস্থায়ী রাজধানী ও প্রশাসনিক কেন্দ্র হিসেবে কাজ করেছিল। চুয়াডাঙ্গা শহরের প্রাণকেন্দ্রে এবং বিভিন্ন যুদ্ধক্ষেত্রে নির্মিত মুক্তিযুদ্ধ স্মৃতিসৌধগুলো বীর মুক্তিযোদ্ধাদের অসীম সাহস ও আত্মত্যাগের স্মৃতি বহন করে। মার্বেল পাথরের তৈরি সুউচ্চ স্মৃতিস্তম্ভ, শহীদদের নামফলক এবং চারপাশের সবুজ উদ্যান এক গভীর ভাবগাম্ভীর্যপূর্ণ পরিবেশ সৃষ্টি করেছে। এখানে দাঁড়িয়ে মুক্তিকামী মানুষের প্রতিরোধ সংগ্রাম ও প্রথম স্বাধীনতার লাল-সবুজ পতাকা উত্তোলনের গৌরবময় ইতিহাস অনুধাবন করা যায়। জাতীয় স্বাধীনতার ইতিহাস জানতে চুয়াডাঙ্গার এই স্মৃতিকেন্দ্রগুলো অত্যন্ত মর্যাদাপূর্ণ।",
            "locationEn": ch_raw['hist_spots'][3]['location'],
            "locationBn": "চুয়াডাঙ্গা শহর ও জেলা, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Traditional Mosque Sites of Damurhuda",
            "nameBn": "দামুড়হুদা ঐতিহ্যবাহী মসজিদ এলাকা",
            "categoryEn": "Historic Architectural Sanctuaries",
            "categoryBn": "ঐতিহাসিক পোড়ামাটির মসজিদ ও প্রাচীন উপাসনালয়",
            "descEn": "The Traditional Mosque Sites of Damurhuda Upazila preserve centuries of Islamic spiritual heritage and traditional brick architecture across southwestern Chuadanga. Dating back to the late medieval and early colonial eras, the historic mosques feature lime-mortar brick construction, multi-tiered domes, curved cornices, and decorative terracotta relief plaques. Established by saintly scholars who traveled along the Mathabhanga River to promote community education and spiritual values, the sanctuaries are flanked by ancestral dighis and shaded courtyards. Devotees gather for daily and Friday congregational prayers in an atmosphere of profound serenity and community warmth. These sacred monuments stand as cherished guardians of Chuadanga's spiritual traditions and cultural endurance.",
            "descBn": "দামুড়হুদা উপজেলার বিভিন্ন প্রাচীন গ্রামে অবস্থিত ঐতিহ্যবাহী মসজিদগুলো দক্ষিণ-পশ্চিম বাংলার সুপ্রাচীন ইসলামিক স্থাপত্য ও সুফি সাধনার এক পরম নিদর্শন। মধ্যযুগ ও উপনিবেশিক আমলের শুরুতে নির্মিত এই মসজিদগুলোতে রয়েছে চুন-সুরকির সুদৃঢ় দেওয়াল, চমৎকার গম্বুজ, বাঁকানো কার্নিশ এবং পোড়ামাটির লতাপাতার কারুকাজ। মাথাভাঙ্গা নদীর অববাহিকায় ধর্মীয় শিক্ষা ও মানবসেবায় আত্মনিয়োগকারী সাধকদের হাত ধরে এই উপাসনালয়গুলো গড়ে উঠেছিল। প্রাচীন দীঘি ও ছায়াঘেরা শান্ত পরিবেশে অবস্থিত এই মসজিদগুলোতে আজও ধর্মপ্রাণ মানুষ প্রতিদিন সমবেত হন। চুয়াডাঙ্গার গ্রামীণ শান্ত প্রকৃতি ও ধর্মীয় ঐতিহ্যের জীবন্ত স্মারক হিসেবে এই মসজিদগুলো অত্যন্ত শ্রদ্ধেয়।",
            "locationEn": ch_raw['hist_spots'][4]['location'],
            "locationBn": "দামুড়হুদা, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Taltala Park",
            "nameBn": "তালতলা পার্ক",
            "categoryEn": "Civic Lake Promenade & Urban Recreation Park",
            "categoryBn": "পৌর লেক পার্ক ও পারিবারিক বিনোদন কেন্দ্র",
            "descEn": "Taltala Park in the center of Chuadanga municipality is the premier civic green recreational park and leisure haven for town residents and visiting tourists. Centered around a picturesque freshwater lake, the park features paved jogging boulevards, colorful seasonal flower beds, shaded gazebos, and illuminated night fountains. Children enjoy well-equipped playground equipment and pedal-boat rides across the calm waters, while families stroll along the lake under mature canopy trees. Street vendors outside the gates sell authentic local delicacies, including hot jilapis, roasted peanuts, and regional snacks. It provides a welcoming, family-friendly urban leisure oasis right within the city.",
            "descBn": "চুয়াডাঙ্গা পৌর শহরের কেন্দ্রস্থলে অবস্থিত তালতলা পার্ক স্থানীয় নাগরিক ও ভ্রমণকারীদের জন্য এক চমৎকার মুক্ত বিনোদন কেন্দ্র। সুন্দর একটি শান্ত লেক ঘিরে গড়ে ওঠা এই পার্কে রয়েছে পাকা হাঁটার পথ, ফুলের বাগান, ফোয়ারা এবং ছায়াঘেরা বসার বেঞ্চ। লেকের জলে প্যাডেল বোট চালানো এবং শিশুদের জন্য খেলার সুন্দর রাইডস পার্কটিকে মুখরিত রাখে। বিকেলে ও সন্ধ্যায় মুক্ত বাতাস উপভোগ করতে এবং পরিবার নিয়ে অবসর কাটাতে প্রচুর মানুষ এখানে সমবেত হন। পার্কের বাইরে পাওয়া যায় গরম গরম জিলাপি, চটপটি ও মুখরোচক খাবার। শহরের কোলাহল ছেড়ে স্বস্তিতে কিছুটা সময় কাটাতে এই পৌর পার্কটি অত্যন্ত চমৎকার।",
            "locationEn": ch_raw['tour_spots'][0]['location'],
            "locationBn": "চুয়াডাঙ্গা শহর, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Mathabhanga Riverbank",
            "nameBn": "মাথাভাঙ্গা নদীতীর",
            "categoryEn": "Scenic Riverfront Promenade & Sunset Point",
            "categoryBn": "নয়নাভিরাম নদীতীর, স্নিগ্ধ বাঁধ ও সূর্যাস্ত ভিউপয়েন্ট",
            "descEn": "The Mathabhanga Riverbank, curving gracefully alongside Chuadanga town and surrounding districts, is a poetic natural attraction that provides a tranquil countryside retreat. Originating as a distributary of the Padma River, the Mathabhanga flows with gentle currents between sandy banks and lush mango orchards. Paved riverside embankments in the town area serve as popular evening promenades where visitors enjoy refreshing breezes and sweeping views of wooden dinghies floating on water. During late afternoon, sunset transforms the river into a shimmering golden expanse while local tea vendors serve hot cardamom tea on the riverbanks. It represents the quintessential peaceful river landscape of southwestern Bengal.",
            "descBn": "চুয়াডাঙ্গা শহরের পাশ দিয়ে বয়ে চলা মাথাভাঙ্গা নদী এ অঞ্চলের প্রকৃতির এক অপরূপ সৌন্দর্যপীঠ। পদ্মা নদী থেকে উৎপন্ন হয়ে এই শান্ত নদীটি আমবাগান ও গ্রামীণ ফসলের মাঠের বুক চিরে এঁকেবেঁকে প্রবাহিত হয়েছে। নদীর পাড়ে গড়ে তোলা বাঁধ ও ওয়াকওয়ে ধরে হাঁটলে শরীর জুড়ানো দখিনা বাতাস মন প্রফুল্ল করে তোলে। বিকেলে শান্ত নদীর বুকে কাঠের নৌকার মন্থর গতি এবং পানিতে সূর্যের রক্তিম আভার ঝিলিক এক স্বর্গীয় অনুভূতি সৃষ্টি করে। নদীতীরের চায়ের দোকানগুলোতে বসে গরম চা খাওয়া ও স্থানীয় মুখরোচক খাবার উপভোগ করতে বহু মানুষ বিকেলে এখানে জড়ো হন। কোলাহলমুক্ত শান্ত পরিবেশে নদীর আসল রূপ উপভোগ করতে মাথাভাঙ্গা নদীতীর এক অসাধারণ স্থান।",
            "locationEn": ch_raw['tour_spots'][1]['location'],
            "locationBn": "চুয়াডাঙ্গা শহর ও জেলা নদীতীর, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Darshana Countryside",
            "nameBn": "দর্শনা গ্রামীণ নিসর্গ",
            "categoryEn": "Scenic Agricultural Borderland Landscapes",
            "categoryBn": "সীমান্তবর্তী গ্রামীণ নিসর্গ ও আখের ক্ষেত",
            "descEn": "The Darshana Countryside in Damurhuda Upazila offers an enchanting rural panorama of boundless sugarcane fields, mango orchards, and picturesque border villages nestled along the international frontier. Walking or cycling down shaded rural roads past waving sugarcane stalks, date palms, and blooming mustard fields provides a deeply peaceful connection to deltaic agrarian life. Local farmers are known for their warm hospitality, offering travelers freshly pressed sweet sugarcane juice and seasonal country fruits. Sunset across the open agricultural plains creates breathtaking photographic compositions of golden light filtering through palm canopies. It is an idyllic eco-tourism retreat celebrating the rural soul of Chuadanga.",
            "descBn": "দামুড়হুদা উপজেলার দর্শনা সংলগ্ন গ্রামীণ নিসর্গ দিগন্তজোড়া আখের ক্ষেত, আমবাগান ও সীমান্তঘেরা শান্ত পল্লিপ্রকৃতির এক অপূর্ব রূপ ধারণ করে আছে। কাঁচা-পাকা মাটির রাস্তা ধরে হাঁটলে বা সাইকেল চালালে চারপাশের সবুজ ফসলের মাঠ এবং তালগাছের সারি মন কেড়ে নেয়। এখানকার কৃষকদের আতিথেয়তা অত্যন্ত উষ্ণ, যারা ভ্রমণকারীদের তাজা আখের মিষ্টি রস ও মৌসুমি ফল দিয়ে আপ্যায়ন করেন। গোধূলিলগ্নে বিস্তীর্ণ ফসলের মাঠের ওপর রক্তিম সূর্যের আলো ছড়িয়ে পড়ার দৃশ্য আলোকচিত্রীদের জন্য এক পরম স্বর্গ। নির্মল গ্রামীণ বাতাস ও শান্তির খোঁজে দর্শনার এই পল্লি নিসর্গ এক চমৎকার আশ্রয়স্থল।",
            "locationEn": ch_raw['tour_spots'][2]['location'],
            "locationBn": "দর্শনা, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Alamdanga Railway Town",
            "nameBn": "আলমডাঙ্গা রেলওয়ে শহর ও বাজার",
            "categoryEn": "Vintage Railway Commerce & Colonial Bazaar",
            "categoryBn": "ঐতিহাসিক রেলওয়ে শহর, ঐতিহ্যবাহী বাজার ও নদীতীর",
            "descEn": "Alamdanga Railway Town is a charming, historic commercial hub where the nostalgia of Victorian steam railway travel blends seamlessly with the vibrant energy of a traditional rural market town. Centered around the historic broad-gauge station, the bustling town streets are lined with historic brick godowns, traditional copper and brassware shops, and famous regional sweetmeat makers producing authentic Chuadanga curd and sandesh. Crossing the historic railway bridges over the Kumar River provides sweeping viewpoints of rural river life and train crossings. Travelers love exploring the lively weekly bazaars and soaking in the timeless atmosphere of an authentic Bengal railway town. It offers an engaging cultural and historical experience.",
            "descBn": "আলমডাঙ্গা রেলওয়ে শহর এমন একটি চমৎকার ঐতিহ্যবাহী জনপদ যেখানে উনিশ শতকের রেলওয়ে নস্টালজিয়া এবং গ্রামীণ বাণিজ্যের প্রাণবন্ত রূপ পাশাপাশি অবস্থান করে। প্রাচীন স্টেশন ঘিরে গড়ে ওঠা এই শহরের অলিগলিতে রয়েছে শতবর্ষী পাটের আড়ত, কাঁসা-পিতলের দোকান এবং ঐতিহ্যবাহী মিষ্টির প্রস্তুতকারকদের দোকান যেখানে বিখ্যাত রসগোল্লা ও সন্দেশ পাওয়া যায়। কুমার নদের ওপর নির্মিত ঐতিহাসিক রেলসেতু থেকে নদী ও দূরবর্তী ট্রেনের দৃশ্য অত্যন্ত দৃষ্টিনন্দন দেখায়। সপ্তাহের হাটের দিনে দূর-দূরান্ত থেকে আসা মানুষের কর্মচাঞ্চল্য এই শহরকে দারুণভাবে মুখরিত করে তোলে। প্রাচীন রেলওয়ে সংস্কৃতি ও গ্রামীণ জীবনের চমৎকার অভিজ্ঞতা পেতে আলমডাঙ্গা অনন্য।",
            "locationEn": ch_raw['tour_spots'][3]['location'],
            "locationBn": "আলমডাঙ্গা, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Damurhuda Rural Landscape",
            "nameBn": "দামুড়হুদা পল্লি নিসর্গ",
            "categoryEn": "Pastoral Farmlands & Countryside Escape",
            "categoryBn": "শান্ত গ্রামীণ জনপদ, আমবাগান ও মেঠোপথ",
            "descEn": "The Damurhuda Rural Landscape in southern Chuadanga is an idyllic pastoral haven characterized by curving dirt tracks, shady bamboo groves, and expansive fertile fields producing rice, wheat, and seasonal vegetables. Intersected by tranquil freshwater canals and small lotus ponds, the landscape preserves the unhurried, authentic essence of traditional Bengali village life. Travelers can observe village artisans weaving bamboo baskets, farmers cultivating soil with traditional plows, and children playing under spreading banyan canopies. The unpolluted country breezes and serene silence provide deep mental peace away from noisy cities. It represents the timeless, poetic rural charm of southwestern Bangladesh.",
            "descBn": "দামুড়হুদার গ্রামীণ নিসর্গ প্রকৃতির এক অপার্থিব শান্তিময় বিস্তার, যেখানে মেঠোপথ, বাঁশঝাড় এবং উর্বর সবুজ ফসলের মাঠ এক চিরন্তন রূপ ধারণ করে আছে। ছোট ছোট মিষ্টি পানির খাল ও পদ্মপুকুরে ঘেরা এই জনপদ বাংলার চিরায়ত শান্ত গ্রামীণ জীবনের এক জীবন্ত প্রতিচ্ছবি। গ্রামের মানুষদের সহজ-সরল জীবনযাপন, হস্তশিল্পের কাজ এবং উন্মুক্ত মাঠে রাখাল বালকদের খেলাধুলার দৃশ্য ভ্রমণকারীদের শৈশবের স্মৃতি জাগিয়ে তোলে। দূষণমুক্ত নির্মল বাতাস এবং চারপাশের নিস্তব্ধতা শহুরে কোলাহল ভুলে মনের গভীর ক্লান্তি দূর করে দেয়। গ্রামবাংলার আসল মায়া ও শান্তি উপলব্ধি করতে দামুড়হুদার এই পল্লি নিসর্গ এক আদর্শ স্থান।",
            "locationEn": ch_raw['tour_spots'][4]['location'],
            "locationBn": "দামুড়হুদা, চুয়াডাঙ্গা",
            "mapUrl": ch_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('chuadanga', chuadanga_data)

# ==========================================
# 19. MEHERPUR
# ==========================================
me_raw = all_data['meherpur']
meherpur_data = {
    "slug": "meherpur",
    "en": "Meherpur",
    "bn": "মেহেরপুর",
    "hero_title_en": "Meherpur Sacred Mujibnagar & Historic Amjhupi Nilkuthi",
    "hero_title_bn": "মেহেরপুরের ঐতিহাসিক মুজিবনগর ও আমঝুপি নীলকুঠির স্মৃতি",
    "hero_sub_en": "Birthplace of sovereign Bangladesh governance at Mujibnagar, colonial Amjhupi indigo mansion, and the serene Bhairab river.",
    "hero_sub_bn": "স্বাধীন বাংলাদেশের প্রথম সরকারের শপথগ্রহণের পুণ্যভূমি মুজিবনগর, ঐতিহাসিক আমঝুপি নীলকুঠি ও ভৈরব নদের রূপ।",
    "tagline_en": "The sacred historic cradle where Bangladesh was formally born with the oath-taking of the provisional government on April 17, 1971, graced by the iconic Mujibnagar Monument and historic colonial Nilkuthis.",
    "tagline_bn": "স্বাধীন বাংলাদেশের প্রথম রাজধানী ও ঐতিহাসিক স্মৃতিপীঠ, যেখানে ১৯৭১ সালের ১৭ই এপ্রিল গঠিত হয়েছিল প্রথম সরকার, এবং যা মুজিবনগর স্মৃতিসৌধ ও আমঝুপি নীলকুঠির জন্য চিরস্মরণীয়।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/meherpur/carousel-1.webp",
            "titleEn": "Mujibnagar Memorial Complex Iconic Monument",
            "titleBn": "মুজিবনগর স্মৃতিসৌধ কমপ্লেক্সের নান্দনিক সৌধ",
            "subtitleEn": "Monumental architectural complex in Baidyanathtala commemorating the historic oath-taking of Bangladesh's first government",
            "subtitleBn": "ঐতিহাসিক বৈদ্যনাথতলায় ২৩টি স্তম্ভবিশিষ্ট সুবিশাল জাতীয় স্মৃতিসৌধ যা স্বাধীন বাংলাদেশের জন্মস্মারক"
        },
        {
            "id": 2,
            "image": "images/districts/meherpur/carousel-2.webp",
            "titleEn": "Amjhupi Nilkuthi Colonial Heritage Mansion",
            "titleBn": "আমঝুপি নীলকুঠির সুরম্য উপনিবেশিক প্রাসাদ",
            "subtitleEn": "19th-century British indigo planter's mansion in Meherpur Sadar surrounded by sprawling gardens on the Kazla riverbank",
            "subtitleBn": "কাজলা নদীর তীরে অবস্থিত ব্রিটিশ নীলকরদের শতাব্দীপ্রাচীন সুরম্য কুঠিবাড়ি ও ছায়াঘেরা বাগান"
        },
        {
            "id": 3,
            "image": "images/districts/meherpur/carousel-3.webp",
            "titleEn": "Mujibnagar Historic Mango Grove Sacred Grounds",
            "titleBn": "মুজিবনগরের ঐতিহাসিক আম্রকানন",
            "subtitleEn": "Venerable mango orchard where cabinet ministers, foreign correspondents, and freedom fighters stood on April 17, 1971",
            "subtitleBn": "১৯৭১ সালের ১৭ই এপ্রিল যে ছায়াঘেরা আম্রকাননে ঘোষিত হয়েছিল বাংলাদেশের স্বাধীনতার ঘোষণাপত্র"
        },
        {
            "id": 4,
            "image": "images/districts/meherpur/carousel-4.webp",
            "titleEn": "Bhairab Riverbank Scenic Sunset Waters",
            "titleBn": "ভৈরব নদীতীরের স্নিগ্ধ সূর্যাস্ত দৃশ্য",
            "subtitleEn": "Meandering historic river winding past Meherpur town bordered by bamboo groves and tranquil village ghats",
            "subtitleBn": "মেহেরপুর শহরের পাশ দিয়ে বয়ে চলা প্রাচীন ভৈরব নদের বুকজুড়ে শান্ত বাতাস ও গোধূলির আলো"
        },
        {
            "id": 5,
            "image": "images/districts/meherpur/carousel-5.webp",
            "titleEn": "Mujibnagar Liberation War Topographic Map Panorama",
            "titleBn": "মুজিবনগর মুক্তিযুদ্ধ স্মারক মানচিত্র কমপ্লেক্স",
            "subtitleEn": "Colossal walk-through relief map of Bangladesh illustrating major battlefronts and historical operations of 1971",
            "subtitleBn": "মুক্তিযুদ্ধের ঐতিহাসিক ১১টি সেক্টর ও প্রধান ঘটনাবলি ফুটিয়ে তোলা সুবিশাল ভূ-প্রাকৃতিক মানচিত্র"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Mujibnagar Memorial Complex",
            "nameBn": "মুজিবনগর স্মৃতিসৌধ কমপ্লেক্স",
            "categoryEn": "National Historical Memorial & Cradle of Sovereign Governance",
            "categoryBn": "জাতীয় ঐতিহাসিক স্মৃতিসৌধ ও প্রথম সরকারের শপথভূমি",
            "descEn": "The Mujibnagar Memorial Complex in Baidyanathtala is Bangladesh's most sacred constitutional and political birthplace, commemorating April 17, 1971, when the provisional Government of the People's Republic of Bangladesh took its historic oath of office under acting President Syed Nazrul Islam and Prime Minister Tajuddin Ahmad. Designed with extraordinary architectural symbolism, the monument features twenty-three ascending triangular brick pillars symbolizing the twenty-three years of Pakistani political and economic struggle (1948–1971). The monument complex spans over eighty acres, incorporating the historic mango grove where international journalists gathered, a world-class outdoor topographic relief map illustrating the 1971 war sectors, a museum, and research library. Millions of citizens and international dignitaries visit annually to pay homage to the visionary founding leadership of the nation. It stands as an indispensable, emotionally profound monument of national pride.",
            "descBn": "মেহেরপুরের বৈদ্যনাথতলায় অবস্থিত মুজিবনগর স্মৃতিসৌধ কমপ্লেক্স স্বাধীন বাংলাদেশের সবচেয়ে গৌরবময় সাংবিধানিক ও রাজনৈতিক তীর্থক্ষেত্র, যেখানে ১৯৭১ সালের ১৭ই এপ্রিল অস্থায়ী রাষ্ট্রপতি সৈয়দ নজরুল ইসলাম ও প্রধানমন্ত্রী তাজউদ্দীন আহমদের নেতৃত্বে প্রথম সরকারের ঐতিহাসিক শপথ অনুষ্ঠিত হয়েছিল। ২৩ বছরের পাকিস্তানি বৈষম্য ও মুক্তি সংগ্রামের প্রতীক হিসেবে এখানে ২৩টি সুউচ্চ ত্রিভুজাকৃতির স্তম্ভের ওপর দাঁড়িয়ে আছে জাতীয় স্মৃতিসৌধটি। প্রায় ৮০ একর এলাকা জুড়ে বিস্তৃত এই কমপ্লেক্সে রয়েছে ঐতিহাসিক আম্রকানন, মুক্তিযুদ্ধের ১১টি সেক্টর ও যুদ্ধের ইতিহাস ফুটিয়ে তোলা দেশের বৃহত্তম ভূ-প্রাকৃতিক মানচিত্র, মুক্তিযুদ্ধ জাদুঘর ও ডাকবাংলো। প্রতিদিন দেশের সর্বস্তরের মানুষ এখানে স্বাধীনতার পুণ্য ইতিহাসের মুখোমুখি হতে আসেন। জাতীয় অহংকার ও আত্মপরিচয়ের এক চিরন্তন প্রতীক এই মুজিবনগর।",
            "locationEn": me_raw['hist_spots'][0]['location'],
            "locationBn": "মুজিবনগর, মেহেরপুর",
            "mapUrl": me_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Amjhupi Nilkuthi",
            "nameBn": "আমঝুপি নীলকুঠি",
            "categoryEn": "Colonial Indigo Heritage Palace & Garden Estate",
            "categoryBn": "উপনিবেশিক নীলকুঠি প্রাসাদ ও ঐতিহাসিক চত্বর",
            "descEn": "Amjhupi Nilkuthi in Meherpur Sadar is an imposing colonial-era country mansion situated on the picturesque banks of the Kazla River, established in the early nineteenth century by European indigo planters. Infamous as the regional administrative headquarters where ruthless British indigo planters enforced oppressive cultivation quotas upon local Bengali peasants, the estate also preserves historical lore connected to the conspiratorial meetings preceding the fateful 1757 Battle of Plassey. The neoclassical two-story mansion features classical Corinthian columns, grand reception lounges, wooden shuttered verandas, and underground punishment cellars. Today, carefully preserved by the Department of Archaeology within tranquil manicured parklands, Amjhupi Nilkuthi stands as an evocative historical monument to the agrarian struggles and resistance of rural Bengal.",
            "descBn": "মেহেরপুর সদর উপজেলায় কাজলা নদীর তীরে অবস্থিত আমঝুপি নীলকুঠি উনিশ শতকের ব্রিটিশ ঔপনিবেশিক শোষণ ও নীল চাষের নির্মম ইতিহাসের এক জীবন্ত স্মারক। ইউরোপীয় নীলকরদের দ্বারা নির্মিত সুরম্য এই দোতলা প্রাসাদে রয়েছে ইউরোপীয় করিন্থিয়ান স্তম্ভ, সুপরিসর বারান্দা, রাজকীয় জলসাঘর এবং অন্ধকার বন্দিশালা। ইতিহাসবিদদের মতে, ১৭৫৭ সালের পলাশীর যুদ্ধের পূর্বে নবাব সিরাজউদ্দৌলাকে উৎখাত করার ষড়যন্ত্রের গোপন বৈঠকও এই কুঠিতে অনুষ্ঠিত হয়েছিল। বর্তমানে প্রত্নতত্ত্ব অধিদপ্তরের অধীনে মনোরম বাগান ও প্রাচীন বৃক্ষরাজির মাঝে সংরক্ষিত এই নীলকুঠিটি পর্যটকদের কাছে অত্যন্ত দর্শনীয়। ব্রিটিশদের বিরুদ্ধে বাংলার কৃষকদের ঐতিহাসিক নীল বিদ্রোহের স্মৃতি জানতে এই স্থানটি এক অনন্য শিক্ষণীয় স্মারক।",
            "locationEn": me_raw['hist_spots'][1]['location'],
            "locationBn": "আমঝুপি, মেহেরপুর সদর, মেহেরপুর",
            "mapUrl": me_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Mujibnagar Government Complex",
            "nameBn": "মুজিবনগর সরকারি কমপ্লেক্স",
            "categoryEn": "Historic Administrative Campus & State Archives",
            "categoryBn": "ঐতিহাসিক প্রশাসনিক কমপ্লেক্স ও জাতীয় সংগ্রহশালা",
            "descEn": "The Mujibnagar Government Complex forms the administrative and civic institutional zone within the historic sanctuary, housing commemorative government auditoriums, protocol offices, guest lodges, and public plazas. Developed to honor the solemn continuity of independent statehood, the brick campus was architecturally styled to blend seamlessly with the solemn red brick aesthetic of the main memorial. Within the complex, official ceremonial events and national cabinet meetings are held on historic anniversaries, drawing heads of state and freedom fighters. The surrounding courtyards feature paved avenues lined with indigenous flowering trees and stone plaques chronicling key milestones of the Proclamation of Independence. It serves as a dignified institutional monument celebrating constitutional democracy and sovereign rule.",
            "descBn": "মুজিবনগর সরকারি কমপ্লেক্স ঐতিহাসিক স্মৃতিপীঠের অন্তর্ভুক্ত এক গুরুত্বপূর্ণ প্রশাসনিক ও সম্মেলন কেন্দ্র, যা স্বাধীন রাষ্ট্র পরিচালনার ঐতিহ্যের স্মারক হিসেবে প্রতিষ্ঠিত হয়েছে। লাল ইটের গাম্ভীর্যপূর্ণ স্থাপত্যশৈলীতে নির্মিত এই চত্বরে রয়েছে আধুনিক সম্মেলন কক্ষ, ভিআইপি ডাকবাংলো, গবেষণা কেন্দ্র ও প্রশস্ত চত্বর। প্রতি বছর ১৭ই এপ্রিল ঐতিহাসিক মুজিবনগর দিবসে এখানে রাষ্ট্রীয় মর্যাদায় মন্ত্রিসভার বিশেষ বৈঠক, শোভাযাত্রা ও আলোচনা সভা অনুষ্ঠিত হয়। কমপ্লেক্সের ছায়াঘেরা পথগুলোতে রয়েছে স্বাধীনতার ঘোষণাপত্রের গুরুত্বপূর্ণ ধারাসমূহ খোদাই করা স্মৃতিফলক। গণতান্ত্রিক চেতনা ও জাতীয় সার্বভৌমত্বের প্রতীক হিসেবে এই প্রশাসনিক কমপ্লেক্সটি অত্যন্ত শ্রদ্ধার সাথে সংরক্ষিত।",
            "locationEn": me_raw['hist_spots'][2]['location'],
            "locationBn": "মুজিবনগর, মেহেরপুর",
            "mapUrl": me_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Baidyanath Tala Historic Site",
            "nameBn": "বৈদ্যনাথতলা ঐতিহাসিক স্থান (আম্রকানন)",
            "categoryEn": "Sacred Oath-Taking Ground of Sovereign Bangladesh",
            "categoryBn": "ঐতিহাসিক শপথস্থল ও স্মৃতিবিজড়িত আম্রকানন",
            "descEn": "Baidyanath Tala, famously christened 'Mujibnagar' by Tajuddin Ahmad in honor of Father of the Nation Bangabandhu Sheikh Mujibur Rahman, is the exact open-air mango orchard clearing where the Proclamation of Independence was read and Bangladesh's first government was sworn in on April 17, 1971. In this historic grove, surrounded by armed freedom fighters, police contingents, and international reporters from BBC and Reuters who slipped across the border, the acting President received a solemn guard of honor from the historic twelve-man police squad. The surviving mature mango trees stand as living, sacred witnesses to the momentous birth of the nation. A designated ceremonial dais marks the precise spot where the oath was administered. Walking through the quiet shadows of this sacred grove inspires profound emotional reverence.",
            "descBn": "ঐতিহাসিক বৈদ্যনাথতলা (যা পরবর্তীতে জাতির পিতা বঙ্গবন্ধু শেখ মুজিবুর রহমানের নামানুসারে 'মুজিবনগর' নামকরণ করা হয়) স্বাধীন বাংলাদেশের অভ্যুদয়ের সেই ঐতিহাসিক আম্রকানন যেখানে ১৯৭১ সালের ১৭ই এপ্রিল প্রথম সরকারের শপথ অনুষ্ঠিত হয়েছিল। এই আমবাগানেই বীর মুক্তিযোদ্ধা ও পুলিশ বাহিনীর ১২ জন সদস্য কর্তৃক ভারপ্রাপ্ত রাষ্ট্রপতিকে ঐতিহাসিক গার্ড অব অনার প্রদান করা হয়েছিল এবং দেশি-বিদেশি বহু সাংবাদিকের উপস্থিতিতে স্বাধীনতার ঐতিহাসিক ঘোষণাপত্র পাঠ করা হয়। শতবর্ষী আমগাছগুলো আজও বাংলাদেশের জন্মের সেই অবিস্মরণীয় মুহূর্তের জীবন্ত সাক্ষী হয়ে দাঁড়িয়ে আছে। যে নির্দিষ্ট স্থানে শপথ মঞ্চ তৈরি করা হয়েছিল, সেখানে নির্মিত স্মারক বেদি দর্শনার্থীদের শ্রদ্ধাবনত করে। স্বাধীনতা সংগ্রামের সবচেয়ে আবেগঘন স্থান এটি।",
            "locationEn": me_raw['hist_spots'][3]['location'],
            "locationBn": "মুজিবনগর, মেহেরপুর",
            "mapUrl": me_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Meherpur Liberation War Memorial Sites",
            "nameBn": "মেহেরপুর মুক্তিযুদ্ধ স্মৃতিসৌধ এলাকা",
            "categoryEn": "Frontier War Battleground & Mass Grave Memorials",
            "categoryBn": "মুক্তিযুদ্ধ স্মৃতিসৌধ, বধ্যভূমি ও শহীদ স্মৃতিস্তম্ভ",
            "descEn": "The Meherpur Liberation War Memorial Sites encompass multiple historic battlegrounds, mass grave memorials, and martyr cenotaphs distributed across the district, which served as the pivotal frontier gateway for the Mukti Bahini during 1971. Because of its direct border adjacency, Meherpur was the staging ground for crucial tactical operations, arms shipments, and refugee evacuations throughout the war. Memorials at places like Kazipur, Amjhupi, and Meherpur town honor the fearless sacrifices of local resistance fighters who repelled invading forces during brutal engagements. Beautifully landscaped memorial gardens with marble plaques preserve the names of fallen martyrs for posterity. These solemn sites serve as vital educational and reflective landmarks for future generations.",
            "descBn": "মেহেরপুর মুক্তিযুদ্ধ স্মৃতিসৌধ এলাকা ১৯৭১ সালের মহান মুক্তিযুদ্ধে সীমান্ত অঞ্চলের বীরত্বপূর্ণ যুদ্ধক্ষেত্র ও আত্মত্যাগের এক অনন্য স্মারক। ভারতীয় সীমান্ত সংলগ্ন হওয়ায় মেহেরপুর ছিল মুক্তিযোদ্ধাদের প্রশিক্ষণ, অস্ত্র সরবরাহ ও রণকৌশল পরিচালনার অত্যন্ত গুরুত্বপূর্ণ ঘাঁটি। কাজীপুর, আমঝুপি ও মেহেরপুর শহরের বিভিন্ন বধ্যভূমিতে হানাদার বাহিনীর হাতে শহীদ হওয়া মুক্তিকামী মানুষ ও বীর মুক্তিযোদ্ধাদের স্মরণে নির্মিত হয়েছে স্মৃতিসৌধ ও নামফলক। পরিপাটি উদ্যান ও স্মৃতিস্তম্ভে ঘেরা এই পবিত্র স্থানগুলো নতুন প্রজন্মকে স্বাধীনতার রক্তমূল্য ও বীরদের আত্মত্যাগের কথা স্মরণ করিয়ে দেয়। মুক্তিযুদ্ধের ঐতিহাসিক চেতনা হৃদয়ে ধারণ করতে এই স্মৃতিসৌধ এলাকা অত্যন্ত তাৎপর্যপূর্ণ।",
            "locationEn": me_raw['hist_spots'][4]['location'],
            "locationBn": "মেহেরপুর শহর ও জেলা, মেহেরপুর",
            "mapUrl": me_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Mujibnagar Memorial Garden",
            "nameBn": "মুজিবনগর স্মৃতি উদ্যান ও ফুলের বাগান",
            "categoryEn": "Landscaped Memorial Park & Botanical Promenade",
            "categoryBn": "সুবিন্যস্ত স্মৃতি উদ্যান, পদ্মপুকুর ও পরিপাটি বাগান",
            "descEn": "The Mujibnagar Memorial Garden is an impeccably designed and maintained botanical parkland surrounding the national monument, planned with lush green lawns, blooming seasonal flower beds, and tranquil lotus ponds. Broad brick-paved boulevards wind through shaded avenues of weeping willows, royal palms, and ornamental shrubs, providing visitors with a dignified setting for peaceful strolls. Sculpted marble fountains and shaded garden gazebos offer welcoming resting spots where families and tourists reflect upon the historical surroundings. The garden features life-sized bronze dioramas depicting key scenes of the 1971 struggle, including the historic oath-taking ceremony and refugees fleeing oppression. It represents one of the finest and most inspiring memorial gardens in South Asia.",
            "descBn": "মুজিবনগর স্মৃতিসৌধ ঘিরে গড়ে ওঠা সুবিশাল স্মৃতি উদ্যান অত্যন্ত নান্দনিক ও মনোরমভাবে সাজানো এক বোটানিক্যাল পার্ক। মখমলের মতো সবুজ ঘাসের লন, রঙ-বেরঙের ফুলের বাগান, সুদৃশ্য পদ্মপুকুর ও ছায়াঘেরা পথ এই চত্বরটিকে অপূর্ব স্নিগ্ধতায় ভরিয়ে রেখেছে। বাগানের বিভিন্ন প্রান্তে স্থাপিত জীবন্ত ব্রোঞ্জ ভাস্কর্যগুলোতে ১৯৭১ সালের ঐতিহাসিক শপথ গ্রহণ, পাকিস্তানি বাহিনীর আত্মসমর্পণ ও শরণার্থীদের জীবনযুদ্ধ জীবন্তভাবে ফুটিয়ে তোলা হয়েছে। পরিচ্ছন্ন ও ভাবগাম্ভীর্যপূর্ণ এই উদ্যানে হেঁটে বেড়ানো এবং পরিবারের সাথে সময় কাটানো যে কোনো দর্শনার্থীর জন্য এক দারুণ অনুভূতি। জাতীয় ইতিহাস ও রূপময় প্রকৃতির এক অসাধারণ মেলবন্ধন এই স্মৃতি উদ্যান।",
            "locationEn": me_raw['tour_spots'][0]['location'],
            "locationBn": "মুজিবনগর, মেহেরপুর",
            "mapUrl": me_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Amjhupi Countryside",
            "nameBn": "আমঝুপি গ্রামীণ নিসর্গ",
            "categoryEn": "Historic Riverside Countryside & Orchard Haven",
            "categoryBn": "কাজলা নদীতীরের গ্রামীণ নিসর্গ ও আমবাগান",
            "descEn": "The Amjhupi Countryside in Meherpur Sadar is a picturesque, tranquil rural haven cradled along the gentle meanders of the Kazla River. Famous for century-old mango orchards, lush litchi groves, and peaceful dirt pathways shaded by giant rain trees, the locality offers an authentic taste of pastoral Bengal. Strolling through the village paths, visitors encounter traditional mud-and-thatch homesteads, serene village ponds covered in water lilies, and hospitable farmers tending green vegetable fields. The peaceful breeze blowing off the river and the gentle rustle of fruit trees provide a rejuvenating escape from urban haste. It is an ideal eco-tourism spot for cycling, landscape photography, and quiet nature contemplation.",
            "descBn": "মেহেরপুর সদর উপজেলার আমঝুপি সংলগ্ন গ্রামীণ নিসর্গ কাজলা নদীর তীরে গড়ে ওঠা এক পরম শান্তিময় ও মনোমুগ্ধকর সবুজ আশ্রয়স্থল। শতবর্ষী আমবাগান, সুস্বাদু লিচুর বাগান এবং ছায়াঘেরা মেঠোপথ এই গ্রামের রূপকে এক অপূর্ব রূপ দিয়েছে। কাজলা নদীর শান্ত জলরাশির পাড় ঘেঁষে হাঁটলে গ্রামীণ মানুষের সরল জীবনযাপন ও মাটির ঘরের চিরায়ত রূপ চোখে পড়ে। মিষ্টি বাতাস আর পাখির কলকাকলি যে কোনো ভ্রমণপিপাসুর হৃদয়ে এক পরম প্রশান্তি এনে দেয়। সাইকেল চালানো, প্রকৃতির ছবি তোলা এবং কোলাহলমুক্ত নিস্তব্ধতায় কিছুটা সময় কাটানোর জন্য আমঝুপির এই গ্রামীণ প্রকৃতি এক অসাধারণ ঠিকানা।",
            "locationEn": me_raw['tour_spots'][1]['location'],
            "locationBn": "আমঝুপি, মেহেরপুর সদর, মেহেরপুর",
            "mapUrl": me_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Bhairab Riverbank",
            "nameBn": "ভৈরব নদীতীর",
            "categoryEn": "Meandering River Promenade & Sunset Vista",
            "categoryBn": "ঐতিহাসিক ভৈরব নদীতীর ও মনোরম সূর্যাস্ত ভিউপয়েন্ট",
            "descEn": "The Bhairab Riverbank, winding gracefully alongside Meherpur town and surrounding rural plains, is a historic riverfront that serves as the environmental soul of the district. Flanked by elevated protective embankments and lush bamboo groves, the river flows past old bathing ghats where local villagers wash and children dive into cool waters. Pedestrian pathways in the urban section provide residents and tourists with a popular scenic promenade for enjoying refreshing evening river winds. During twilight, the golden sunset casts glowing beams across the peaceful water while wooden dinghies float gently in the stream. It provides an authentic, accessible location to savor the beauty of deltaic river geography.",
            "descBn": "মেহেরপুর শহরের পাশ দিয়ে এঁকেবেঁকে বয়ে চলা ভৈরব নদীতীর এ অঞ্চলের এক অত্যন্ত মনোরম ও ঐতিহাসিক জলজ প্রকৃতি। নদীর দুই তীরে গড়ে ওঠা সবুজ গাছপালা, বাঁশঝাড় ও প্রাচীন শানবাঁধানো ঘাট এক শান্ত গ্রামীণ আবহ সৃষ্টি করে রেখেছে। নদীর পাড়ের বাঁধ দিয়ে হাঁটার সময় শীতল দখিনা বাতাস শরীর ও মনকে প্রফুল্ল করে তোলে। গোধূলিলগ্নে শান্ত নদীর বুকে রক্তিম সূর্যের প্রতিফলন এক অপার্থিব রূপ তৈরি করে যা সূর্যাস্তপ্রেমীদের জন্য এক দারুণ উপহার। নদীর পাড়ের ছোট ছোট চায়ের দোকানে বসে গরম চা খাওয়া ও শান্ত জলের সৌন্দর্য উপভোগ করতে বহু মানুষ বিকেলে এখানে সমবেত হন। প্রকৃতির অপার রূপ দেখতে ভৈরব নদীতীর এক চমৎকার স্থান।",
            "locationEn": me_raw['tour_spots'][2]['location'],
            "locationBn": "মেহেরপুর জেলা নদীতীর, মেহেরপুর",
            "mapUrl": me_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Meherpur Municipal Park",
            "nameBn": "মেহেরপুর পৌর পার্ক",
            "categoryEn": "Civic Lake Promenade & Urban Green Sanctuary",
            "categoryBn": "পৌর পার্ক, লেক ওয়াকওয়ে ও বিনোদন কেন্দ্র",
            "descEn": "Situated in the central urban area of Meherpur municipality, the Municipal Park serves as the premier green recreational oasis for residents and travelers. Centered around a tranquil heritage lake, the park features paved jogging boulevards, colorful seasonal flower beds, shaded gazebos, and illuminated night fountains. Children enjoy well-equipped playground equipment and pedal-boat rides on the calm lake waters, while families stroll along the water's edge under mature canopy trees. Street vendors outside the gates sell authentic local delicacies, including hot jilapi, roasted peanuts, and spicy street foods. It provides a welcoming, family-friendly urban leisure oasis right within the city.",
            "descBn": "মেহেরপুর জেলা শহরের কেন্দ্রস্থলে অবস্থিত পৌর পার্ক স্থানীয় নাগরিক ও ভ্রমণকারীদের জন্য এক চমৎকার মুক্ত বিনোদন কেন্দ্র। সুন্দর একটি শান্ত লেক ঘিরে গড়ে ওঠা এই পার্কে রয়েছে পাকা হাঁটার রাস্তা, ফুলের বাগান, ফোয়ারা এবং ছায়াঘেরা বসার বেঞ্চ। লেকের জলে প্যাডেল বোট চালানো এবং শিশুদের জন্য খেলার সুন্দর রাইডস পার্কটিকে মুখরিত রাখে। বিকেলে ও সন্ধ্যায় মুক্ত বাতাস উপভোগ করতে এবং পরিবার নিয়ে অবসর কাটাতে প্রচুর মানুষ এখানে সমবেত হন। পার্কের বাইরে পাওয়া যায় গরম গরম জিলাপি, চটপটি ও মুখরোচক খাবার। শহরের কোলাহল ছেড়ে স্বস্তিতে কিছুটা সময় কাটাতে এই পৌর পার্কটি অত্যন্ত চমৎকার।",
            "locationEn": me_raw['tour_spots'][3]['location'],
            "locationBn": "মেহেরপুর শহর, মেহেরপুর",
            "mapUrl": me_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Mujibnagar Rural Landscape",
            "nameBn": "মুজিবনগর পল্লি নিসর্গ",
            "categoryEn": "Pastoral Border Farmlands & Countryside Haven",
            "categoryBn": "সীমান্তবর্তী গ্রামীণ নিসর্গ, আম্রকানন ও মেঠোপথ",
            "descEn": "The Mujibnagar Rural Landscape surrounding the historic memorial complex is an enchanting pastoral haven characterized by sweeping green paddy fields, dense mango orchards, and picturesque border hamlets. Winding village roads lined with date palms and flowering gulmohar trees lead travelers through quiet agricultural communities that live peacefully along the international border. Travelers love walking down these quiet rural lanes, observing traditional threshing floors, and experiencing the warm hospitality of local farmers who offer sweet seasonal mangoes and fresh sugarcane juice. The serene silence, unpolluted air, and breathtaking sunsets make it an unforgettable countryside retreat. It captures the authentic, resilient soul of rural Bangladesh.",
            "descBn": "ঐতিহাসিক মুজিবনগর স্মৃতিসৌধের চারপাশের গ্রামীণ নিসর্গ দিগন্তজোড়া সবুজ ফসলের মাঠ, সুবিশাল আমবাগান ও শান্ত সীমান্তবর্তী জনপদের এক পরম স্নিগ্ধ বিস্তার। আন্তর্জাতিক সীমান্ত ঘেঁষে চলে যাওয়া শান্ত মাটির রাস্তা ধরে হাঁটলে চোখে পড়ে গ্রামীণ কৃষকদের কর্মব্যস্ত জীবন এবং মাটির সুন্দর বাড়িঘর। মেহেরপুরের বিখ্যাত সুস্বাদু আম এবং আখের মিষ্টি রস দিয়ে স্থানীয় মানুষ ভ্রমণকারীদের আন্তরিক আতিথেয়তায় বরণ করে নেন। দূষণমুক্ত নির্মল বাতাস, চারপাশের নিস্তব্ধতা এবং গোধূলির রক্তিম আভা ভ্রমণপ্রেমীদের হৃদয়ে এক চিরন্তন শান্তি এনে দেয়। বাংলার মাটির আসল রূপ ও গ্রামীণ সৌন্দর্য প্রত্যক্ষ করতে মুজিবনগরের এই পল্লি নিসর্গ এক অনুপম স্থান।",
            "locationEn": me_raw['tour_spots'][4]['location'],
            "locationBn": "মুজিবনগর, মেহেরপুর",
            "mapUrl": me_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('meherpur', meherpur_data)

# ==========================================
# 20. PATUAKHALI
# ==========================================
pa_raw = all_data['patuakhali']
patuakhali_data = {
    "slug": "patuakhali",
    "en": "Patuakhali",
    "bn": "পটুয়াখালী",
    "hero_title_en": "Patuakhali Daughter of the Sea, Kuakata Beach & Mangrove Trails",
    "hero_title_bn": "পটুয়াখালীর সাগরকন্যা কুয়াকাটা, বৌদ্ধ মন্দির ও ম্যানগ্রোভ নিসর্গ",
    "hero_sub_en": "Rare simultaneous sunrise and sunset from Kuakata Sea Beach, ancient Rakhine Buddhist shrines, and Fatrar Char mangroves.",
    "hero_sub_bn": "একই সৈকত থেকে সূর্যোদয় ও সূর্যাস্তের বিরল দৃশ্য, প্রাচীন রাখাইন বৌদ্ধ মন্দির ও ফাতরার চরের ম্যানগ্রোভ অরণ্য।",
    "tagline_en": "The iconic 'Daughter of the Sea' (Sagor Kanya) on the Bay of Bengal coast, globally celebrated for the panoramic sun-drenched beaches of Kuakata, centuries-old Rakhine culture, and Payra deep seaport.",
    "tagline_bn": "বঙ্গোপসাগরের কোল ঘেঁষে অবস্থিত রূপসী 'সাগরকন্যা' পটুয়াখালী, যা কুয়াকাটা সমুদ্র সৈকত, প্রাচীন মিশ্রিপাড়া বৌদ্ধ মন্দির, রাখাইন পল্লী, লেবুর চর ও পায়রা গভীর সমুদ্র বন্দরের জন্য বিশ্বখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/patuakhali/carousel-1.webp",
            "titleEn": "Kuakata Sea Beach Sunrise & Sunset Horizon",
            "titleBn": "কুয়াকাটা সমুদ্র সৈকত ও যুগল সূর্য দর্শন",
            "subtitleEn": "18-kilometer unbroken golden beach in Kalapara offering rare panoramic sunrise and sunset over the Bay of Bengal",
            "subtitleBn": "একই স্থান থেকে সমুদ্রের বুকে সূর্যোদয় ও সূর্যাস্তের বিরল স্বর্গীয় রূপ দর্শনের সুবিশাল সোনালী সৈকত"
        },
        {
            "id": 2,
            "image": "images/districts/patuakhali/carousel-2.webp",
            "titleEn": "Misripara Buddhist Temple Colossal Buddha Statue",
            "titleBn": "মিশ্রিপাড়া বৌদ্ধ মন্দির ও বিশালাকার বুদ্ধ মূর্তি",
            "subtitleEn": "Venerable Rakhine pagoda housing the largest seated stone Buddha statue in South Asia nestled in Kalapara",
            "subtitleBn": "দক্ষিণ এশিয়ার অন্যতম বৃহত্তম উপবিষ্ট পাথরের বুদ্ধ মূর্তি ধারণকারী প্রাচীন রাখাইন বৌদ্ধ উপাসনালয়"
        },
        {
            "id": 3,
            "image": "images/districts/patuakhali/carousel-3.webp",
            "titleEn": "Fatrar Char Sundarbans Mangrove Wilderness",
            "titleBn": "ফাতরার চরের গভীর ম্যানগ্রোভ অরণ্য",
            "subtitleEn": "Pristine western mangrove forest reached by sea boat featuring wild deer, monkeys, and tidal creeks",
            "subtitleBn": "কুয়াকাটার পশ্চিমে সাগরের বুকে সুন্দরবনের অংশ যা চিত্রা হরিণ, বানর ও শ্বাসমূলের বনের জন্য পরিচিত"
        },
        {
            "id": 4,
            "image": "images/districts/patuakhali/carousel-4.webp",
            "titleEn": "Lebu Char Red Crab Paradise & River Confluence",
            "titleBn": "লেবুর চর ও লাল কাঁকড়ার স্বর্গরাজ্য",
            "subtitleEn": "Scenic coastal estuary where millions of red fiddler crabs scuttle across sparkling sunset sandbars",
            "subtitleBn": "তিন নদীর মোহনায় অবস্থিত বালুচর যেখানে হাজার হাজার লাল কাঁকড়ার দল সৈকতকে রক্তিম রঙে সাজিয়ে তোলে"
        },
        {
            "id": 5,
            "image": "images/districts/patuakhali/carousel-5.webp",
            "titleEn": "Gangamati Reserved Forest Coastal Jungle",
            "titleBn": "গঙ্গামতি সংরক্ষিত বন ও উপকূলীয় নিসর্গ",
            "subtitleEn": "Dense evergreen coastal forest flanking eastern Kuakata framing breathtaking sunrises and sand dunes",
            "subtitleBn": "কুয়াকাটার পূর্ব প্রান্তে অবস্থিত নিঝুম বন ও বালিয়াড়ি যেখান থেকে সমুদ্রের বুক চিরে ভোরের সূর্যোদয় দেখা যায়"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Kuakata Buddhist Temple",
            "nameBn": "কুয়াকাটা বৌদ্ধ মন্দির (সীমা বৌদ্ধ বিহার)",
            "categoryEn": "Historic Rakhine Buddhist Temple & Ancient Well",
            "categoryBn": "ঐতিহাসিক রাখাইন বৌদ্ধ বিহার ও প্রাচীন কুয়া",
            "descEn": "The Kuakata Buddhist Temple (locally known as Seema Buddhist Vihara), situated near the main entrance to Kuakata Sea Beach, is a revered spiritual sanctuary established over two centuries ago by early Rakhine settlers. The monastery houses an extraordinary eight-metal alloy (Ashtadhatu) Buddha statue weighing nearly four hundred kilograms, celebrated for its serene classical craftsmanship and golden aura. Adjacent to the sanctuary stands the historic sacred well ('Kua') dug by the founding Rakhine community who migrated from Arakan in 1784, which gave the town of Kuakata its historic name. The traditional wooden temple features tiered Thai-Burmese pagodas, ornate woodcarvings, and shaded meditation courtyards. Devotees and tourists visit to pay homage, learn about Rakhine heritage, and experience deep spiritual peace.",
            "descBn": "কুয়াকাটা সমুদ্র সৈকতের সন্নিকটে অবস্থিত কুয়াকাটা সীমা বৌদ্ধ বিহার দুই শতাব্দীরও বেশি সময় পূর্বে আরাকান থেকে আগত আদি রাখাইন বসতি স্থাপনকারীদের দ্বারা প্রতিষ্ঠিত এক পরম পবিত্র তীর্থস্থান। এই মন্দিরে রয়েছে প্রায় চার শত কেজি ওজনের অষ্টধাতুর তৈরি এক বিশালাকার ও দৃষ্টিনন্দন বুদ্ধ মূর্তি, যার শান্ত অবয়ব ভক্তদের মুগ্ধ করে। মন্দিরের পাশেই অবস্থিত সেই ঐতিহাসিক প্রাচীন কুয়া (কূপ), যা ১৭৮৪ সালে রাখাইনরা সুপেয় পানির জন্য খনন করেছিলেন এবং যা থেকে এই পর্যটন শহরের নাম হয়েছে 'কুয়াকাটা'। ঐতিহ্যবাহী কাঠের কারুকার্যময় বার্মিজ স্থাপত্যের এই বিহারে প্রবেশ করলে এক নিবিড় আধ্যাত্মিক প্রশান্তি অনুভূত হয়। রাখাইনদের সমৃদ্ধ সংস্কৃতি ও প্রাচীন ঐতিহ্যের এক জীবন্ত স্মারক এই বৌদ্ধ মন্দির।",
            "locationEn": pa_raw['hist_spots'][0]['location'],
            "locationBn": "কুয়াকাটা, কলাপাড়া, পটুয়াখালী",
            "mapUrl": pa_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Misripara Buddhist Temple",
            "nameBn": "মিশ্রিপাড়া বৌদ্ধ মন্দির (সীমা বিহার)",
            "categoryEn": "Ancient Monastic Pagoda & Colossal Buddha Statue",
            "categoryBn": "প্রাচীন রাখাইন বৌদ্ধ বিহার ও বিশালাকার ধ্যানমগ্ন বুদ্ধ",
            "descEn": "Misripara Buddhist Temple, located in the traditional Rakhine village of Misripara in Kalapara Upazila, is renowned across South Asia for housing one of the largest seated stone Buddha statues in the subcontinent. Rising over thirty feet tall inside an elevated wooden prayer pagoda, the colossal Buddha statue depicts the Gautama Buddha in a meditative lotus posture, radiating profound serenity. The village of Misripara was founded during the late eighteenth century by displaced Rakhines who preserved their distinct language, Buddhist festivals, colorful handloom weaving, and pagodas. Visiting the quiet village courtyard allows travelers to observe traditional stilt architecture, tour active handloom workshops where women craft intricate silk lungis, and interact with welcoming Rakhine elders. It stands as an essential cultural and religious heritage destination in southern Bangladesh.",
            "descBn": "কলাপাড়া উপজেলার রাখাইন পল্লি মিশ্রিপাড়ায় অবস্থিত বৌদ্ধ মন্দিরটি উপমহাদেশের অন্যতম বৃহত্তম উপবিষ্ট ধ্যানমগ্ন বুদ্ধ মূর্তির জন্য আন্তর্জাতিকভাবে সুপরিচিত। কাঠের তৈরি সুউচ্চ বিহারের অভ্যন্তরে প্রতিষ্ঠিত এই বিশালাকার বুদ্ধ মূর্তিটি গভীর ধ্যানমগ্ন ভঙ্গিমায় নির্মিত, যা দেখলে মনে গভীর ভক্তি ও প্রশান্তি জাগে। অষ্টাদশ শতাব্দীর শেষভাগে আরাকান থেকে আসা রাখাইনদের দ্বারা প্রতিষ্ঠিত এই গ্রামটিতে আজও তাদের নিজস্ব ভাষা, সংস্কৃতি, ধর্মীয় উৎসব ও ঐতিহ্যবাহী তাঁতশিল্প জীবন্ত রয়েছে। গ্রামের মাচাং ঘর, শান্ত মন্দির প্রাঙ্গণ এবং রঙিন কাপড়ের তাঁত দেখার অভিজ্ঞতা পর্যটকদের কাছে অত্যন্ত আকর্ষণীয়। প্রাচীন রাখাইন ঐতিহ্য ও বৌদ্ধ সংস্কৃতির এক অনন্য মহাতীর্থ এই মিশ্রিপাড়া মন্দির।",
            "locationEn": pa_raw['hist_spots'][1]['location'],
            "locationBn": "মিশ্রিপাড়া, কুয়াকাটা, কলাপাড়া, পটুয়াখালী",
            "mapUrl": pa_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Karbala Dighi Area",
            "nameBn": "কারবালা দীঘি এলাকা",
            "categoryEn": "Historic Water Reservoir & Sacred Gathering Ground",
            "categoryBn": "ঐতিহাসিক জলাধার ও আধ্যাত্মিক স্মৃতি প্রাঙ্গণ",
            "descEn": "The Karbala Dighi Area in Patuakhali town is an ancient historical water reservoir and religious gathering landmark established over a century ago to serve the coastal community. Enclosed by massive embankments and shaded by mature rain trees and banyans, the dighi holds profound spiritual significance as the focal gathering point during annual Muharram commemorations and community fairs. The tranquil waters reflect the surrounding skyline, providing an urban green sanctuary where local residents and visitors take evening walks and find quiet respite. Surviving historical brick masonry, ancient steps, and commemorative markers narrate the cultural endurance of the district headquarters across cyclone-prone deltaic history. It remains an honored historical and civic anchor of Patuakhali.",
            "descBn": "পটুয়াখালী জেলা শহরের কেন্দ্রস্থলে অবস্থিত কারবালা দীঘি শতাব্দীর প্রাচীন এক ঐতিহাসিক জলাশয় ও ধর্মীয় ঐতিহ্যের স্মারক। সুবিশাল এই দীঘির চারপাশ সুদৃঢ় পাড় এবং প্রাচীন মেহগনি ও বটগাছের ছায়ায় ঘেরা, যা শহরে এক স্নিগ্ধ শান্তিময় পরিবেশ তৈরি করে রেখেছে। প্রতি বছর পবিত্র মহররম উপলক্ষে এখানে ঐতিহ্যবাহী তাশিয়া মিছিল ও ধর্মীয় সমাবেশ অনুষ্ঠিত হয়, যা এই স্থানকে গভীর আধ্যাত্মিক মর্যাদা দিয়েছে। দীঘির শান্ত জলরাশি এবং শানবাঁধানো ঘাট শহরের মানুষের সকাল ও সন্ধ্যার হাঁটার জন্য অত্যন্ত প্রিয়। উপকূলীয় ঝড়ের মধ্যেও শতাব্দীর পর শতাব্দী ধরে মিষ্টি জলের আধার হিসেবে টিকে থাকা এই কারবালা দীঘি পটুয়াখালীর এক ঐতিহ্যবাহী নিদর্শন।",
            "locationEn": pa_raw['hist_spots'][2]['location'],
            "locationBn": "পটুয়াখালী শহর এলাকা, পটুয়াখালী",
            "mapUrl": pa_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Patuakhali Historic Launch Terminal",
            "nameBn": "পটুয়াখালী ঐতিহাসিক লঞ্চ টার্মিনাল",
            "categoryEn": "Colonial Coastal Maritime Terminal",
            "categoryBn": "ঐতিহাসিক উপকূলীয় নদী বন্দর ও লঞ্চ ঘাট",
            "descEn": "Patuakhali Historic Launch Terminal along the deep waters of the Laukathi River has served for over a century as the primary maritime gateway connecting the coastal delta with Dhaka and the national interior. Prior to modern road bridges, this bustling riverfront was the only umbilical cord through which islanders, merchants, and colonial administrators traveled aboard legendary steam vessels and modern double-decker passenger launches. The terminal area bustles constantly with incoming launches sounding deep foghorns, fish vendors selling fresh coastal catches, and travelers embarking on night journeys under the stars. The wide riverfront promenade offers sweeping views of tidal currents, cargo coasters, and traditional country boats. It remains an indelible cultural symbol of southern maritime travel.",
            "descBn": "লাউকাঠী নদীর তীরে অবস্থিত পটুয়াখালী ঐতিহাসিক লঞ্চ টার্মিনাল এক শতাব্দীরও বেশি সময় ধরে এই উপকূলীয় জেলার সাথে রাজধানী ঢাকার নৌযোগাযোগের প্রধান লাইফলাইন হিসেবে কাজ করে আসছে। দক্ষিণাঞ্চলের নদীমাতৃক জীবনের প্রাণকেন্দ্র এই ঘাটে প্রতিদিন বিশালাকার আধুনিক দোতলা ও তিনতলা বিলাসবহুল লঞ্চের যাতায়াত এক চমৎকার দৃশ্যপট তৈরি করে। ভোর ও সন্ধ্যায় যাত্রীদের পদচারণা, কুলিদের হাঁকডাক এবং দূরপাল্লার লঞ্চের গম্ভীর সাইরেন এই বন্দরকে সবসময় মুখরিত রাখে। নদীর পাড়ে দাঁড়িয়ে প্রমত্তা নদীর বিশাল ঢেউ ও সূর্যাস্ত দেখা ভ্রমণপ্রেমীদের দারুণ আনন্দ দেয়। নদীমাতৃক বাংলার আসল স্পন্দন ও উপকূলীয় জীবনের গল্প প্রত্যক্ষ করতে এই পুরোনো লঞ্চ ঘাট এক অনন্য স্থান।",
            "locationEn": pa_raw['hist_spots'][3]['location'],
            "locationBn": "পটুয়াখালী শহর নদীতীর, পটুয়াখালী",
            "mapUrl": pa_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Kalapara Historic Settlement Area",
            "nameBn": "কলাপাড়া ঐতিহাসিক জনপদ এলাকা",
            "categoryEn": "Historic Coastal Frontier Town & Rakhine Settlement",
            "categoryBn": "ঐতিহাসিক উপকূলীয় শহর ও আদি রাখাইন জনপদ",
            "descEn": "The Kalapara Historic Settlement Area is a venerable frontier town nestled along the Andharmanik River, founded in the late eighteenth century when Arakanese Rakhine refugees cleared coastal mangrove jungles to build villages. The name 'Kalapara' commemorates early settlements established along coastal canals where traditional wooden boatbuilding, salt harvesting, and deep-sea fishing flourished. The historic quarters preserve authentic wooden-stilt architecture, century-old Buddhist pagodas, vibrant coastal markets, and ancient freshwater ponds. Flanked by tidal estuaries and lush coconut groves, the settlement played a pivotal role in opening the southern coast to agriculture and maritime commerce. Exploring its historic lanes offers travelers an intimate window into the pioneering coastal history of Patuakhali.",
            "descBn": "আন্ধারমানিক নদীর তীরে অবস্থিত কলাপাড়া ঐতিহাসিক জনপদ অষ্টাদশ শতাব্দীর শেষভাগে আরাকান থেকে আগত রাখাইনদের হাত ধরে গড়ে ওঠা এক প্রাচীন উপকূলীয় শহর। ঘন জঙ্গল আবাদ করে রাখাইন ও বাঙালিরা এখানে বসতি স্থাপন করেছিলেন এবং নদীকে কেন্দ্র করে নৌকা তৈরি, শুঁটকি ও উপকূলীয় কৃষির সমৃদ্ধ বাণিজ্য গড়ে তুলেছিলেন। শহরের পুরোনো অংশে আজও দেখা যায় প্রাচীন কাঠের দোতলা বাড়ি, রাখাইনদের বৌদ্ধ মন্দির এবং শতবর্ষী পুকুর। নদী ও খালের মাধ্যমে বঙ্গোপসাগরের সাথে সরাসরি যুক্ত এই জনপদটি উপকূলীয় জীবনের ইতিহাস ও সংস্কৃতির এক সমৃদ্ধ ভাণ্ডার। প্রাচীন উপকূলের মানুষের টিকে থাকার গল্প জানতে কলাপাড়া এক অত্যন্ত আকর্ষণীয় স্থান।",
            "locationEn": pa_raw['hist_spots'][4]['location'],
            "locationBn": "কলাপাড়া, পটুয়াখালী",
            "mapUrl": pa_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Kuakata Sea Beach",
            "nameBn": "কুয়াকাটা সমুদ্র সৈকত",
            "categoryEn": "World-Famous 'Daughter of the Sea' Panoramic Beach",
            "categoryBn": "আন্তর্জাতিক সাগরকন্যা সৈকত ও সূর্যোদয়-সূর্যাস্ত দর্শন",
            "descEn": "Kuakata Sea Beach, lovingly celebrated as the 'Daughter of the Sea' (Sagor Kanya), is one of the most magnificent natural coastal marvels in the world, spanning an unbroken eighteen kilometers of wide, gentle golden sand along the Bay of Bengal. Unique across South Asia, Kuakata is one of the extremely rare seashores on earth where travelers can witness both the dramatic fiery sunrise and the glowing oceanic sunset directly from the exact same beach location. Gentle rolling waves, fine sand ideal for motorcycling and jogging, and clean uncrowded stretches create an atmosphere of profound coastal peace. Traditional fishermen launching colorful wooden catamarans into the rolling surf provide unforgettable photographic compositions. Fresh seafood stalls along the shore grill fresh pomfret, red snapper, and tiger prawns directly on hot coal fires. It is an unmissable world-class holiday destination.",
            "descBn": "সবার প্রিয় 'সাগরকন্যা' নামে খ্যাত কুয়াকাটা সমুদ্র সৈকত বিশ্বের অন্যতম প্রধান ও দুর্লভ প্রাকৃতিক উপকূলীয় বিস্ময়, যা প্রায় ১৮ কিলোমিটার দীর্ঘ বিস্তীর্ণ সোনালী বালুকাবেলা নিয়ে বঙ্গোপসাগরের কোলে শুয়ে আছে। সমগ্র এশিয়ার মধ্যে কুয়াকাটা এমন এক বিরল সমুদ্র সৈকত যেখান থেকে একই স্থানে দাঁড়িয়ে সাগরের বুক চিরে উদিত হওয়া রক্তিম সূর্যোদয় এবং সাগরের বুকেই তলিয়ে যাওয়া মনোরম সূর্যাস্ত প্রত্যক্ষ করা যায়। সৈকতের শান্ত ঢেউ, বিস্তৃত বালুচর এবং সাগরের শীতল বাতাস ভ্রমণপিপাসুদের এক অপার্থিব স্বর্গীয় অনুভূতি উপহার দেয়। সকালে ও সন্ধ্যায় সমুদ্রের বুকে জেলেদের নৌকা বেয়ে চলার দৃশ্য এক মুগ্ধকর ক্যানভাস তৈরি করে। সৈকতে বসে গরম গরম তাজা রূপচাঁদা, কোরাল ও চিংড়ি মাছের বারবিকিউ উপভোগ করা প্রতিটি পর্যটকের প্রিয় অভিজ্ঞতা। জীবনের ক্লান্তি ভুলে প্রকৃতির অনন্ত রূপ দেখতে কুয়াকাটা এক অতুলনীয় স্বপ্নপুরী।",
            "locationEn": pa_raw['tour_spots'][0]['location'],
            "locationBn": "কুয়াকাটা, কলাপাড়া, পটুয়াখালী",
            "mapUrl": pa_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Fatrar Char",
            "nameBn": "ফাতরার চর (ম্যানগ্রোভ বন)",
            "categoryEn": "Coastal Mangrove Wilderness & Safari Island",
            "categoryBn": "সুন্দরবনের অংশ ম্যানগ্রোভ বন ও সাফারি চর",
            "descEn": "Fatrar Char is a wild, pristine mangrove island situated across the estuary west of Kuakata, serving as the easternmost natural extension of the UNESCO World Heritage Sundarbans forest. Accessible by a thrilling hour-long motorized trawler cruise across rolling coastal waves, the island features dense stands of breathing pneumatophore roots, towering sundari, keora, and golpata trees crisscrossed by tidal creeks. Guided ecotourists trek along safe forest trails where herds of wild spotted deer, playful rhesus monkeys, wild boars, and exotic monitor lizards are regularly sighted. Forest watchtowers provide panoramic views of untamed mangrove canopy melting into the blue ocean horizon. It is a thrilling, authentic wilderness safari excursion directly accessible from Kuakata.",
            "descBn": "কুয়াকাটার পশ্চিমে সাগরের মোহনা পেরিয়ে অবস্থিত ফাতরার চর সুন্দরবনের পূর্ব অংশের এক অক্ষত ও বুনো ম্যানগ্রোভ অরণ্য। কুয়াকাটা থেকে ইঞ্জিনচালিত ট্রলারে করে সাগরের ঢেউয়ের বুক চিরে প্রায় এক ঘণ্টা রোমাঞ্চকর নৌভ্রমণের পর এই দ্বীপে পৌঁছানো যায়। এই গভীর বনে রয়েছে শ্বাসমূলযুক্ত সুন্দরী, কেওড়া ও গোলপাতার সুবিশাল বনানী এবং জোয়ার-ভাটার সর্পিল খাল। বনের ভেতরের ট্রেইল ধরে হাঁটলে বুনো চিত্রা হরিণ, বানর, বুনো শুয়োর ও নানা প্রজাতির পাখির দেখা মেলে। বন বিভাগের ওয়াচ টাওয়ার থেকে পুরো ম্যানগ্রোভ বন ও সাগরের মিলনমেলা এক পলকে দেখা যায়। যারা সুন্দরবনের আসল বুনো রূপ খুব সহজে ও নিরাপদে উপভোগ করতে চান, তাদের জন্য ফাতরার চর এক সেরা রোমাঞ্চকর গন্তব্য।",
            "locationEn": pa_raw['tour_spots'][1]['location'],
            "locationBn": "কুয়াকাটা উপকূলীয় অঞ্চল, পটুয়াখালী",
            "mapUrl": pa_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Gangamati Reserved Forest",
            "nameBn": "গঙ্গামতি সংরক্ষিত বন ও সৈকত",
            "categoryEn": "Pristine Sunrise Forest & Coastal Dunes",
            "categoryBn": "সূর্যোদয়ের প্রধান সৈকত, বালিয়াড়ি ও ঝাউবন",
            "descEn": "Gangamati Reserved Forest, located at the eastern extreme of Kuakata Beach along the Gangamati canal, is an enchanting natural wilderness celebrated as the premier vantage point for catching the fiery morning sunrise over the Bay of Bengal. Blanketed in lush casuarina (jhau) trees, wild screw-pines, and natural sand dunes, the forest creates a fairy-tale coastal barrier between the sea and green farmland. In the early dawn hours, the red sun rises directly out of the ocean water, casting shimmering golden ribbons across wet tidal sands while flocks of sea gulls take flight. Red fiddler crabs emerge in their thousands to scuttle across the virgin shores, turning the sand into a carpet of brilliant scarlet. It is widely revered by photographers as the most poetic and unspoiled natural spot in Kuakata.",
            "descBn": "কুয়াকাটা সৈকতের পূর্ব প্রান্তে অবস্থিত গঙ্গামতি সংরক্ষিত বন ও সৈকত প্রকৃতির এক অপূর্ব কুমারী রূপ, যা সূর্যোদয় দেখার প্রধান ও সেরা কেন্দ্র হিসেবে খ্যাত। ঘন সবুজ ঝাউবন, গোলপাতা এবং বালিয়াড়িতে ঘেরা এই বনটি সমুদ্র ও সমতল ভূমির মাঝে এক প্রাকৃতিক প্রাচীর তৈরি করেছে। ভোরে যখন সাগরের বুক চিরে লাল টকটকে সূর্য উদিত হয়, তখন এখানকার বালুকাবেলায় তৈরি হয় এক স্বর্গীয় দৃশ্য যা আলোকচিত্রীদের পরম স্বপ্ন। সৈকতের নরম বালুতে হাজার হাজার লাল কাঁকড়ার অবাধ ছোটাছুটি সৈকতকে রক্তিম চাদরে ঢেকে দেয়। পর্যটকদের কোলাহলমুক্ত শান্ত পরিবেশে সমুদ্রের আসল নির্জনতা ও সকালের মিষ্টি আলো উপভোগ করতে গঙ্গামতি এক অবিস্মরণীয় স্থান।",
            "locationEn": pa_raw['tour_spots'][2]['location'],
            "locationBn": "কুয়াকাটা, পটুয়াখালী",
            "mapUrl": pa_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Lebu Char (Lebur Bon)",
            "nameBn": "লেবুর চর (লেবুর বন)",
            "categoryEn": "Scenic River Confluence & Fresh Seafood Haven",
            "categoryBn": "তিন নদীর মোহনা, লাল কাঁকড়ার দ্বীপ ও তাজা মাছের বাজার",
            "descEn": "Lebu Char (often called Lebur Bon) at the extreme western edge of Kuakata is an exhilarating coastal sandbar where the Bay of Bengal meets the confluence of the Khaprabhanga and Payra river systems. Characterized by expansive tidal mudflats, thriving young mangrove plantations, and thousands of scuttling red crabs, the char is famous for dramatic afternoon sunsets that fill the wide sky with brilliant hues. The area has become famous for open-air beachfront barbecue stalls where freshly caught pomfret, hilsha, cuttlefish, and king crabs landed directly from fishing boats are marinated in spicy herbs and grilled hot on coconut-shell embers. Tourists sit on wooden benches right on the sand with their feet in the tide while savoring mouth-watering seafood. It is an unforgettable culinary and coastal adventure.",
            "descBn": "কুয়াকাটা সৈকতের একেবারে পশ্চিম প্রান্তে অবস্থিত লেবুর চর (লেবুর বন) তিন নদীর মোহনা ও বঙ্গোপসাগরের মিলনস্থলে গড়ে ওঠা এক রোমাঞ্চকর পর্যটন কেন্দ্র। বিস্তীর্ণ বালুচর, ছোট ছোট ম্যানগ্রোভ বাগান এবং লাখ লাখ লাল কাঁকড়ার অবাধ বিচরণ এই স্থানটিকে দারুণ আকর্ষণীয় করেছে। এখান থেকে বিকেলের সূর্যাস্ত দেখা এক পরম তৃপ্তিদায়ক অনুভূতি। লেবুর চরের সবচেয়ে বড় আকর্ষণ হলো সৈকতের পাড়ে বসে তাজা সামুদ্রিক মাছের লাইভ বারবিকিউ উপভোগ করা। জেলেরা সরাসরি সাগর থেকে ধরে আনা রূপচাঁদা, কোরাল, টুনা ও কাঁকড়া পর্যটকদের চোখের সামনে কয়লার আগুনে ঝলসে পরিবেশন করেন। সাগরের ঢেউয়ের শব্দ আর সুস্বাদু খাবারের মেলবন্ধনে লেবুর চর এক স্বপ্নময় আনন্দের ঠিকানা।",
            "locationEn": pa_raw['tour_spots'][3]['location'],
            "locationBn": "কুয়াকাটা উপকূলীয় এলাকা, পটুয়াখালী",
            "mapUrl": pa_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Payra Port Viewpoint Area",
            "nameBn": "পায়রা গভীর সমুদ্র বন্দর ভিউপয়েন্ট",
            "categoryEn": "Deep Seaport Mega-Infrastructure & Maritime Vista",
            "categoryBn": "গভীর সমুদ্র বন্দর প্রকল্প ও সুবিশাল নৌ মোহনা",
            "descEn": "The Payra Port Viewpoint Area in the Kalapara/Rabnabad channel region is the strategic site of Bangladesh's monumental third deep-sea seaport mega-project. Designed to handle international container vessels and bulk coal carriers, the expanding port complex features massive dredging channels, deep-water jetties, and towering cargo cranes set against wide coastal estuaries. Viewing points near the port approaches allow travelers to witness the scale of modern maritime engineering transforming the southern delta alongside traditional fishing trawlers cruising the channel. Watching large cargo vessels glide into the harbor against sweeping sunset horizons provides an inspiring glimpse into the economic future of coastal Bangladesh. It stands as a proud symbol of twenty-first-century national maritime ambition.",
            "descBn": "কলাপাড়া উপজেলার রাবনাবাদ চ্যানেলে অবস্থিত পায়রা গভীর সমুদ্র বন্দর বাংলাদেশের তৃতীয় বৃহত্তম সমুদ্র বন্দর এবং জাতীয় অর্থনীতির অন্যতম প্রধান মেগা প্রকল্প। আন্তর্জাতিক কনটেইনার জাহাজ ও বিশালাকার কয়লাবাহী জাহাজ ভেড়ানোর জন্য নির্মিত এই গভীর সমুদ্র বন্দরে রয়েছে সুবিশাল জেটি, আধুনিক ক্রেন ও সুপ্রশস্ত নেভিগেশন চ্যানেল। বন্দরের প্রবেশমুখে দাঁড়িয়ে একদিকে আধুনিক প্রকৌশলবিদ্যার বিশাল কর্মযজ্ঞ এবং অন্যদিকে সুবিশাল নদীর মোহনায় সাগরের ঢেউয়ের খেলা প্রত্যক্ষ করা যায়। সন্ধ্যার আলোয় চ্যানেলের বুকে বিশাল জাহাজের আনাগোনা এবং মোহনার খোলা বাতাস দর্শনার্থীদের মনে এক গর্বিত অনুভূতি জাগায়। আধুনিক বাংলাদেশের সমুদ্রবাণিজ্যের নতুন দিগন্ত প্রত্যক্ষ করতে পায়রা বন্দর এলাকা এক দারুণ দর্শনীয় স্থান।",
            "locationEn": pa_raw['tour_spots'][4]['location'],
            "locationBn": "কলাপাড়া অঞ্চল, পটুয়াখালী",
            "mapUrl": pa_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('patuakhali', patuakhali_data)
