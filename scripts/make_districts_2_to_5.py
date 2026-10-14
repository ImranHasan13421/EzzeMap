# -*- coding: utf-8 -*-
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
os.makedirs('scripts/data_districts_17', exist_ok=True)

# 2. NARAIL
narail = {
    "slug": "narail",
    "en": "Narail",
    "bn": "নড়াইল",
    "hero_title_en": "Narail Artistic Legacy & Chitra Riverfront",
    "hero_title_bn": "নড়াইলের চিত্রানদী ও শিল্পী সুলতানের শিল্প-ঐতিহ্য",
    "hero_sub_en": "World-famous artworks of SM Sultan, historic zamindari heritage, and serene Chitra riverboat routes.",
    "hero_sub_bn": "বিশ্বখ্যাত চিত্রশিল্পী এস এম সুলতানের স্মৃতিবিজড়িত চিত্রাপাড় ও প্রাচীন জমিদারির গৌরবময় ইতিহাস।",
    "tagline_en": "The celebrated cultural sanctuary of southwestern Bengal, world-renowned as the birthplace of legendary painter SM Sultan, woven with picturesque riverways and colonial educational institutions.",
    "tagline_bn": "দক্ষিণ-পশ্চিম বাংলার এক বরেণ্য সাংস্কৃতিক জনপদ, যা কিংবদন্তি শিল্পী এস এম সুলতানের জন্মভূমি ও চিত্রা নদীর প্রাকৃতিক সৌন্দর্যের জন্য বিশ্বজুড়ে পরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/narail/carousel-1.webp",
            "titleEn": "SM Sultan Memorial Gallery & Studio",
            "titleBn": "এস এম সুলতান স্মৃতি সংগ্রহশালা ও স্টুডিও",
            "subtitleEn": "Riverside sanctuary in Machimdia preserving the iconic monumental canvases and personal artifacts of maestro SM Sultan",
            "subtitleBn": "মাছিমদিয়ায় চিত্রা নদীর তীরে অবস্থিত বিশ্বখ্যাত চিত্রশিল্পীর অমর শিল্পকর্ম ও ব্যক্তিগত স্মৃতি স্মারক"
        },
        {
            "id": 2,
            "image": "images/districts/narail/carousel-2.webp",
            "titleEn": "Chitra River Serene Waters & Boat Life",
            "titleBn": "চিত্রা নদীর রূপময় জলধারা ও নৌজীবন",
            "subtitleEn": "The poetic river that inspired generations of Bengali artists and writers flowing quietly through Narail",
            "subtitleBn": "নড়াইলের প্রাণস্বরূপ চিত্রা নদী, যার বুকে পালতোলা নৌকা ও শান্ত জলরাশি যুগ যুগ ধরে শিল্পীদের প্রেরণা জুগিয়েছে"
        },
        {
            "id": 3,
            "image": "images/districts/narail/carousel-3.webp",
            "titleEn": "Historic Narail Victoria College Architecture",
            "titleBn": "ঐতিহাসিক নড়াইল ভিক্টোরিয়া কলেজের স্থাপত্য",
            "subtitleEn": "Colonial-era educational institution established in 1886 with majestic arched red-brick facades",
            "subtitleBn": "১৮৮৬ সালে প্রতিষ্ঠিত শতবর্ষী এই বিদ্যাপীঠ নড়াইলের শিক্ষা ও বুদ্ধিবৃত্তিক জাগরণের এক ঐতিহাসিক প্রতীক"
        },
        {
            "id": 4,
            "image": "images/districts/narail/carousel-4.webp",
            "titleEn": "SM Sultan Shishu Swarga Floating Boat Studio",
            "titleBn": "এস এম সুলতান শিশু স্বর্গ ও নৌকা পাঠশালা",
            "subtitleEn": "Unique creative educational haven founded by Sultan for rural children along the tranquil riverbanks",
            "subtitleBn": "গ্রামীণ শিশুদের চিত্রাঙ্কন ও সৃজনশীল মেধা বিকাশের জন্য সুলতান প্রতিষ্ঠিত স্বপ্নময় শিশু স্বর্গ"
        },
        {
            "id": 5,
            "image": "images/districts/narail/carousel-5.webp",
            "titleEn": "Kalia Zamindari Heritage & Temples",
            "titleBn": "কালিয়ার প্রাচীন জমিদারি ও দেবালয়",
            "subtitleEn": "Aristocratic heritage mansions and ancient brick temples nestled amidst quiet village waterways in Kalia",
            "subtitleBn": "কালিয়ার সবুজ নিসর্গে ঢাকা প্রাচীন জমিদার বাড়ি ও মন্দিরের ঐতিহাসিক স্থাপত্যের স্মৃতিচিহ্ন"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "SM Sultan Memorial Gallery",
            "nameBn": "এস এম সুলতান স্মৃতি সংগ্রহশালা",
            "categoryEn": "Legendary Artist Memorial & Art Museum",
            "categoryBn": "বিশ্বখ্যাত শিল্পী স্মৃতি জাদুঘর ও সংগ্রহশালা",
            "descEn": "The SM Sultan Memorial Gallery at Machimdia, Narail Sadar, is the revered memorial complex and resting place of Bangladesh's legendary pioneer painter, Sheikh Mohammed Sultan. Overlooking the serene Chitra River, the museum complex houses an extensive permanent collection of Sultan's massive masterworks depicting heroic, muscular Bengali peasants tilling fertile soil and celebrating harvest abundance. Visitors can explore the artist's original studio rooms, rustic easel stands, personal brushes, and his beloved garden sanctuary where he cared for wildlife. The adjacent tomb of the maestro is surrounded by quiet flowering shrubs, creating an atmosphere of deep creative reverence. It remains an essential cultural pilgrimage site for art connoisseurs from around the globe.",
            "descBn": "মাছিমদিয়ায় চিত্রা নদীর তীরে অবস্থিত এস এম সুলতান স্মৃতি সংগ্রহশালা বাংলাদেশের শিল্পকলার ইতিহাসের এক পরম তীর্থস্থান। এই সংগ্রহশালায় সংরক্ষিত আছে বিশ্বখ্যাত চিত্রশিল্পী শেখ মোহাম্মদ সুলতানের বিশাল ক্যানভাসে আঁকা অমর চিত্রকর্ম, যেখানে বাংলার মেহনতি কৃষকদের পেশীবহুল ও বীরোচিত রূপে তুলে ধরা হয়েছে। শিল্পীর নিজস্ব স্টুডিও, রং-তুলি, এবং তাঁর জীবদ্দশায় ব্যবহৃত বিভিন্ন সামগ্রী এখানে অত্যন্ত যত্নের সাথে প্রদর্শিত। প্রাঙ্গণেই শায়িত আছেন এই মহান শিল্পী, যার সমাধি ঘিরে এক অপার্থিব স্নিগ্ধতা বিরাজ করে। দেশ-বিদেশের বহু শিল্পপ্রেমী প্রতিদিন এখানে এসে শিল্পীর অনন্য সৃষ্টি দর্শন ও শ্রদ্ধা নিবেদন করেন।",
            "locationEn": "Machimdia, Narail Sadar",
            "locationBn": "মাছিমদিয়া, নড়াইল সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=SM%20Sultan%20Memorial%20Gallery%2C%20Machimdia%2C%20Narail%20Sadar"
        },
        {
            "id": 2,
            "nameEn": "Victoria College building",
            "nameBn": "নড়াইল ভিক্টোরিয়া কলেজ ঐতিহাসিক ভবন",
            "categoryEn": "Nineteenth-Century Colonial Academic Monument",
            "categoryBn": "ঊনবিংশ শতাব্দীর ঔপনিবেশিক শিক্ষা স্থাপত্য",
            "descEn": "The historic Victoria College Building in Narail town is one of the oldest and most prestigious educational establishments in the Bengal delta. Founded in 1886 through the generous patronage of the philanthropic Narail Zamindar family, the grand brick edifice features British-Indian colonial architecture with sweeping verandas, classical brick columns, and high vaulted ceilings. The institution served as an intellectual crucible that educated generations of prominent lawyers, judges, freedom fighters, and cultural figures of Bengal. The mature rain trees and lush green lawns framing the academic structures provide an inspiring scholarly ambiance. The building stands as a majestic testament to Narail's enduring commitment to enlightened education and cultural progress.",
            "descBn": "১৮৮৬ সালে নড়াইলের জমিদার পরিবারের পৃষ্ঠপোষকতায় প্রতিষ্ঠিত নড়াইল ভিক্টোরিয়া কলেজ ভবনটি দক্ষিণ বাংলার অন্যতম প্রাচীন ও মর্যাদাপূর্ণ শিক্ষা প্রতিষ্ঠান। লাল ইটের সুদৃঢ় গাঁথুনি, সুবিশাল খিলানযুক্ত বারান্দা এবং ব্রিটিশ ঔপনিবেশিক স্থাপত্যশৈলী ভবনটিকে এক ঐতিহাসিক রাজকীয় রূপ দিয়েছে। এই কলেজটি অবিভক্ত বাংলা ও আধুনিক বাংলাদেশের বহু প্রথিতযশা বুদ্ধিজীবী, রাজনীতিবিদ ও গবেষক তৈরি করেছে। শতবর্ষী ছায়াঘন বৃক্ষরাজি বেষ্টিত এই ক্যাম্পাস নড়াইলের গৌরবোজ্জ্বল অতীতের এক অমলিন সাক্ষ্য বহন করছে। শিক্ষা ও স্থাপত্যের প্রতি অনুরাগী পর্যটকদের কাছে এটি এক অবিস্মরণীয় ঐতিহাসিক নিদর্শন।",
            "locationEn": "Narail town",
            "locationBn": "নড়াইল শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Victoria%20College%20building%2C%20Narail%20town"
        },
        {
            "id": 3,
            "nameEn": "Kalia historic zamindar sites",
            "nameBn": "কালিয়ার ঐতিহাসিক জমিদার বাড়ি",
            "categoryEn": "Colonial Aristocratic Estate & Temples",
            "categoryBn": "উপনিবেশিক জমিদারি প্রাসাদ ও মন্দির কমপ্লেক্স",
            "descEn": "The Kalia historic zamindar sites comprise an impressive cluster of eighteenth- and nineteenth-century feudal manors located in Kalia Upazila. During their zenith, the zamindars of Kalia commissioned monumental residential mansions, grand reception chambers, and terracotta-decorated family shrines along the riverbanks. Although time and monsoon moisture have weathered several structures, the surviving Corinthian pilasters, ornamental plaster cornices, and decorative brick water ghats exhibit aristocratic grandeur. Local historians emphasize the region's historical role as a vibrant center of cultural patronage and inland river commerce during the colonial era. The atmospheric ruins offer photographers and heritage travelers an evocative window into Bengal's bygone feudal chapter.",
            "descBn": "নড়াইলের কালিয়া উপজেলায় অবস্থিত ঐতিহাসিক জমিদার বাড়ির চত্বরটি অষ্টাদশ ও ঊনবিংশ শতাব্দীর জমিদারি আভিজাত্যের স্মৃতি বহন করে। নদীবেষ্টিত এই অঞ্চলে তৎকালীন প্রভাবশালী জমিদারগণ গড়ে তুলেছিলেন সুরম্য অট্টালিকা, নাচঘর, পূজামণ্ডপ ও সানবাঁধানো পুকুরঘাট। প্রাচীন দেওয়ালের কারুকার্যময় পলেস্তারা ও ইউরোপীয় ধারার স্তম্ভগুলো আজও দর্শনার্থীদের আকৃষ্ট করে। এই স্থানটি একসময় নদীকেন্দ্রিক ব্যবসা-বাণিজ্য ও সাংস্কৃতিক কর্মকাণ্ডের প্রাণকেন্দ্র ছিল। কালিয়ার প্রাচীন ধ্বংসাবশেষ ও গ্রামীণ নিসর্গ ইতিহাসের এক হারানো সোনালী অধ্যায়কে জীবন্ত করে তোলে।",
            "locationEn": "Kalia, Narail",
            "locationBn": "কালিয়া, নড়াইল",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kalia%20historic%20zamindar%20sites%2C%20Kalia%2C%20Narail"
        },
        {
            "id": 4,
            "nameEn": "Mohammadpur border heritage",
            "nameBn": "মোহাম্মদপুর সীমান্ত ঐতিহাসিক এলাকা",
            "categoryEn": "Historic River Borderland & Ruins",
            "categoryBn": "ঐতিহাসিক নদী সীমান্ত ও প্রত্নতাত্ত্বিক এলাকা",
            "descEn": "The Mohammadpur border heritage area in northern Narail marks the historic transitional frontier where ancient waterways connected Narail with the medieval kingdom of Raja Sitaram Ray. The landscape preserves ancient earthen flood control ramparts, neglected brick foundations, and forgotten brick kiln mounds that once supplied materials for regional forts and monasteries. Local oral traditions recount centuries of riverine boat skirmishes between regional chieftains and imperial naval flotillas cruising along the Madhumati basin. Today, the rural borderland offers peaceful pastoral vistas, tranquil bamboo groves, and winding canal crossings. It is valued by regional historians as a critical landscape for deciphering the geopolitical contours of medieval south-central Bengal.",
            "descBn": "নড়াইল ও পার্শ্ববর্তী মাগুরা সীমান্তের মধুমতী নদী অববাহিকায় অবস্থিত এই অঞ্চলটি প্রাচীন ইতিহাস ও প্রতিরক্ষামূলক যুদ্ধকৌশলের সাক্ষ্য বহন করে। সপ্তদশ শতকে রাজা সীতারাম রায়ের শাসনামলে এটি ছিল এক কৌশলগত সীমান্ত চৌকি ও জলপথের প্রধান পাহারা কেন্দ্র। এখানকার প্রাচীন মাটির ঢিবি ও ইটের ভগ্নাবশেষ তৎকালীন নদীকেন্দ্রিক যোগাযোগ ও সামরিক দুর্গব্যবস্থার ইঙ্গিত দেয়। বর্তমানে শান্ত-নিবিড় পল্লীপ্রকৃতি ও নদীবিধৌত সবুজ চরাঞ্চল এক স্নিগ্ধ রূপ ধারণ করেছে। ঐতিহাসিক অনুসন্ধিৎসু ভ্রমণকারীদের জন্য এই সীমান্তবর্তী ভূদৃশ্য অত্যন্ত কৌতূহলোদ্দীপক।",
            "locationEn": "Mohammadpur region",
            "locationBn": "মোহাম্মদপুর সীমান্ত এলাকা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Mohammadpur%20border%20heritage%2C%20Mohammadpur%20region"
        },
        {
            "id": 5,
            "nameEn": "Lohagara historic temple",
            "nameBn": "লোহাগড়ার ঐতিহাসিক মন্দির",
            "categoryEn": "Ancient Hindu Terracotta Shrine",
            "categoryBn": "প্রাচীন টেরাকোটা হিন্দু মন্দির ও দেবালয়",
            "descEn": "The historic temple of Lohagara is a centuries-old Hindu sanctuary celebrated for its authentic folk terracotta embellishments and elegant curving cornices. Dedicated to regional deities, the single-spire temple was built by master artisans using traditional sun-baked bricks bound by lime and molasses mortar. The sanctum exterior exhibits delicate floral panels, miniature deity figures, and geometric border bands that demonstrate the high artistry of medieval Bengali temple architecture. Surrounding village groves of jackfruit and mango trees shelter the sacred precinct, maintaining an aura of quiet contemplative peace. Devotees and cultural travelers cherish the temple as a preserved gemstone of community devotion.",
            "descBn": "নড়াইলের লোহাগড়ায় অবস্থিত এই প্রাচীন মন্দিরটি বাংলার ঐতিহ্যবাহী টেরাকোটা ও দোচালা স্থাপত্যশৈলীর এক চমৎকার নিদর্শন। চুন-সুরকি ও পোড়ামাটির সূক্ষ্ম কারুকাজে নির্মিত মন্দিরটির দেওয়ালে পৌরাণিক আখ্যান ও দেশীয় ফুল-লতার নকশা অত্যন্ত যত্নে খোদাই করা হয়েছে। মন্দিরের সুউচ্চ শিখরটি বহুদূর থেকে দৃষ্টিগোচর হয় এবং প্রাঙ্গণের স্নিগ্ধ পল্লী পরিবেশ এক স্বর্গীয় অনুভূতি এনে দেয়। যুগ যুগ ধরে এটি স্থানীয় ভক্তদের পূজা-অর্চনা ও ধর্মীয় পার্বণের পবিত্র কেন্দ্র হিসেবে সমাদৃত। স্থাপত্যকলা ও লোকঐতিহ্যের নিরিখে মন্দিরটি নড়াইলের এক পরম সম্পদ।",
            "locationEn": "Lohagara, Narail",
            "locationBn": "লোহাগড়া, নড়াইল",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Lohagara%20historic%20temple%2C%20Lohagara%2C%20Narail"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Chitra Riverbank",
            "nameBn": "চিত্রা নদীতীর",
            "categoryEn": "Iconic Riverfront Promenade & Boat Haven",
            "categoryBn": "মনোরম নদীতীর ওয়াকওয়ে ও নৌভ্রমণ কেন্দ্র",
            "descEn": "The Chitra Riverbank flowing gracefully through Narail town is the emotional and scenic heart of the entire district. Famous for inspiring the bold brushstrokes of maestro SM Sultan and lyrical Bengali poetry, the river's calm emerald waters create a mesmerizing panorama. Visitors can take relaxing wooden boat cruises along the shaded banks, watching local fishermen cast handmade cast-nets as water birds dive gracefully for fish. The paved riverfront promenade features shaded seating kiosks, ambient lighting, and panoramic sunset viewpoints where townsfolk unwind in the evenings. Experiencing the gentle breezes of Chitra River captures the pure essence of idyllic southern Bengal.",
            "descBn": "চিত্রা নদীর তীর নড়াইল জেলার সৌন্দর্য ও আত্মিক পরিচয়ের প্রধান কেন্দ্রবিন্দু। প্রখ্যাত চিত্রশিল্পী এস এম সুলতানের তুলির আঁচড়ে অমর হয়ে থাকা এই নদী তার শান্ত জলরাশি ও মনোরম দুই পাড়ের জন্য বিখ্যাত। দর্শনার্থীরা এখানে দেশীয় নৌকায় চড়ে নদীর স্নিগ্ধ রূপ উপভোগ করতে পারেন, যেখানে জেলেদের মাছ ধরার দৃশ্য ও তীরের সবুজ গাছপালা চোখ জুড়িয়ে দেয়। বিকেলে নদীর পাড়ে বাঁধাই করা ওয়াকওয়েতে হাঁটতে এবং মুক্ত হাওয়া উপভোগ করতে বহু পর্যটকের সমাগম হয়। চিত্রার নির্মল পরিবেশ ও শান্ত নদীপ্রকৃতি ভ্রমণপিপাসুদের এক অবিস্মরণীয় স্মৃতি উপহার দেয়।",
            "locationEn": "Narail town",
            "locationBn": "নড়াইল শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Chitra%20Riverbank%2C%20Narail%20town"
        },
        {
            "id": 2,
            "nameEn": "SM Sultan Shishu Swarga",
            "nameBn": "এস এম সুলতান শিশু স্বর্গ",
            "categoryEn": "Creative Children's Art Academy & Boat Studio",
            "categoryBn": "সৃজনশীল শিশু চিত্রাঙ্কন কেন্দ্র ও নৌকা পাঠশালা",
            "descEn": "SM Sultan Shishu Swarga in Machimdia is a visionary artistic institution founded by master painter SM Sultan to nurture the innate creative talents of rural children. The complex famously features the legendary floating studio—a massive multi-tiered wooden riverboat where Sultan conducted open-air drawing and painting classes along the Chitra River. Surrounded by sprawling gardens, animal enclosures, and open-air art pavilions, children learn freehand painting and sculpturing directly inspired by nature. Today, visitors and art students tour the colorful studios, viewing youthful artworks and original sketches created under the master's humanist philosophy. It represents one of the most heartwarming creative sanctuaries in Bangladesh.",
            "descBn": "মাছিমদিয়ায় অবস্থিত এস এম সুলতান শিশু স্বর্গ শিল্পী সুলতানের এক অনন্য মানবিক ও স্বপ্নদর্শী সৃষ্টি। সুবিধাবঞ্চিত গ্রামীণ শিশুদের অন্তরের সুপ্ত প্রতিভাকে জাগ্রত করতে তিনি এই প্রতিষ্ঠানটি গড়ে তোলেন। এখানে রয়েছে শিল্পীর স্বপ্নের সুবিশাল দ্বিতল নৌকা, যা একসময় নদীতে ভেসে ভেসে শিশুদের ছবি আঁকার ভ্রাম্যমাণ পাঠশালা হিসেবে ব্যবহৃত হতো। সবুজ মাঠ, ফুলবাগান ও পশুপাখির সান্নিধ্যে গড়ে ওঠা এই চত্বরে এখনো নিয়মিত শিশুদের আর্ট ক্লাস অনুষ্ঠিত হয়। শিল্প, শিক্ষা ও প্রকৃতির এমন অপূর্ব মিলনমেলা দর্শনার্থীদের মনে গভীর অনুপ্রেরণা ও আনন্দ সঞ্চার করে।",
            "locationEn": "Machimdia, Narail Sadar",
            "locationBn": "মাছিমদিয়া, নড়াইল সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=SM%20Sultan%20Shishu%20Swarga%2C%20Machimdia%2C%20Narail%20Sadar"
        },
        {
            "id": 3,
            "nameEn": "Narail Victoria College grounds",
            "nameBn": "ভিক্টোরিয়া কলেজ প্রাঙ্গণ ও উদ্যান",
            "categoryEn": "Historic Academic Parklands & Greenery",
            "categoryBn": "ঐতিহাসিক বিদ্যাপীঠ প্রাঙ্গণ ও সুদৃশ্য উদ্যান",
            "descEn": "The spacious grounds of Narail Victoria College offer visitors a tranquil park-like atmosphere enriched by over a century of academic heritage. Shaded by ancient banyan, mahogany, and mahogany trees, the open lawns host students, book lovers, and cultural societies engaged in lively intellectual discussions. The juxtaposition of nineteenth-century red-brick colonnades against expansive green turf provides marvelous opportunities for photography and quiet walks. During spring and winter, seasonal flowers bloom across landscaped garden beds, adding vibrant splashes of color to the historic quadrangle. It remains one of Narail's most cherished public sanctuaries for quiet contemplation.",
            "descBn": "নড়াইল ভিক্টোরিয়া কলেজের সুবিশাল প্রাঙ্গণ সবুজে ঘেরা এক চমৎকার উন্মুক্ত বিনোদন ও বিশ্রামের স্থান। শতবর্ষী বিশাল মেহগনি, রেইনট্রি ও দেবদারু গাছের শীতল ছায়ায় ঢাকা এই প্রাঙ্গণে এক পরম প্রশান্তিময় পরিবেশ বিরাজ করে। লাল ইটের প্রাচীন ভবনের সামনে বিস্তৃত খেলার মাঠ ও ফুলের বাগান প্রাঙ্গণটিকে অসাধারণ দৃষ্টিনন্দন রূপ দিয়েছে। শিক্ষার্থী ও স্থানীয় মানুষদের পাশাপাশি অনেক দূর-দূরান্তের পর্যটক এখানে এসে সময় কাটাতে ভালোবাসেন। ইতিহাস ও প্রকৃতির মেলবন্ধনে এই কলেজ ক্যাম্পাস নড়াইলের অন্যতম প্রধান দর্শনীয় স্থান।",
            "locationEn": "Narail town",
            "locationBn": "নড়াইল শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Narail%20Victoria%20College%20grounds%2C%20Narail%20town"
        },
        {
            "id": 4,
            "nameEn": "Lohagara countryside",
            "nameBn": "লোহাগড়া পল্লি নিসর্গ",
            "categoryEn": "Scenic Riverine Rural Countryside",
            "categoryBn": "নয়নাভিরাম গ্রামীণ মেঠোপথ ও নদীমাতৃক প্রকৃতি",
            "descEn": "The Lohagara countryside presents the timeless beauty of Bengal's rural heartland, adorned with verdant paddy expanses, meandering canals, and fertile river siltlands. Bounded by the Nabaganga and Madhumati waterways, the landscape features idyllic thatched homesteads shaded by clusters of betel nut palms and banana trees. Travelers exploring rural roads encounter traditional clay pottery workshops, bamboo craft artisans, and lively village haats bursting with organic seasonal fruits. Bicycle touring and walking along the canal embankments provide intimate glimpses into the peaceful rhythms of agricultural village life. It is an ideal escape for travelers seeking restorative pastoral stillness and genuine rural hospitality.",
            "descBn": "লোহাগড়ার পল্লী নিসর্গ বাংলার আবহমান গ্রাম্য রূপের এক জীবন্ত প্রতিচ্ছবি। মধুমতী ও নবগঙ্গার প্লাবনভূমিতে অবস্থিত এই অঞ্চলের সবুজ ধানক্ষেত, আঁকাবাঁকা মেঠোপথ ও নারকেল-সুপারির বাগান মনকে ছুঁয়ে যায়। এখানকার নিভৃত গ্রামগুলোতে রয়েছে ঐতিহ্যবাহী মৃৎশিল্প ও বাঁশ-বেতের কারিগরদের নিপুণ হাতের কাজ। বিকেলে গ্রামীণ হাট-বাজারের মুখরিত পরিবেশ ও নদীর বাঁকে সূর্যাস্তের অপরূপ দৃশ্য ভ্রমণকারীদের মুগ্ধ করে। শহুরে জীবনের ব্যস্ততা ছেড়ে বিশুদ্ধ গ্রামীণ বাতাবরণে প্রশান্তি পেতে লোহাগড়ার গ্রামগুলো অত্যন্ত চমৎকার।",
            "locationEn": "Lohagara, Narail",
            "locationBn": "লোহাগড়া, নড়াইল",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Lohagara%20countryside%2C%20Lohagara%2C%20Narail"
        },
        {
            "id": 5,
            "nameEn": "Narail municipal park",
            "nameBn": "নড়াইল পৌর পার্ক",
            "categoryEn": "Urban Recreation & Family Leisure Lake",
            "categoryBn": "পৌর বিনোদন পার্ক ও পারিবারিক পিকনিক স্পট",
            "descEn": "Narail Municipal Park is the primary urban recreational green space located conveniently within Narail town center. Featuring paved jogging walkways, a central ornamental lake, colorful children's play zones, and lush manicured flowerbeds, it is popular with families and fitness enthusiasts. Pedestrian bridges arching over the water allow visitors to feed schools of playful fish or admire reflecting evening lights across the surface. Shaded picnic gazebos and tidy refreshment stalls provide comfortable amenities for afternoon relaxation and social gatherings. The park serves as a lively civic oasis fostering community health, relaxation, and joyful family leisure.",
            "descBn": "নড়াইল শহরের কেন্দ্রস্থলে অবস্থিত নড়াইল পৌর পার্ক শহরবাসীর প্রধান বিনোদন ও পারিবারিক অবকাশ যাপনের কেন্দ্র। সুদৃশ্য লেক, লেকের ওপর নির্মিত নান্দনিক হাঁটার সেতু এবং চারপাশে রঙিন ফুলের বাগান পার্কটিকে আকর্ষণীয় করে তুলেছে। এখানে শিশুদের জন্য রয়েছে বিভিন্ন খেলার রাইড এবং বড়দের জন্য শান্ত-শীতল বসার জায়গা। পরিবার-পরিজন নিয়ে বিকেলে মুক্ত বাতাসে সময় কাটানো ও সান্ধ্যকালীন হাঁটার জন্য এটি অত্যন্ত জনপ্রিয়। শহরের কোলাহলমুক্ত ও সুশৃঙ্খল পরিবেশের কারণে নড়াইল পৌর পার্ক ভ্রমণকারীদের কাছে এক চমৎকার বিশ্রামস্থল।",
            "locationEn": "Narail town",
            "locationBn": "নড়াইল শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Narail%20municipal%20park%2C%20Narail%20town"
        }
    ]
}

# 3. NAOGAON
naogaon = {
    "slug": "naogaon",
    "en": "Naogaon",
    "bn": "নওগাঁ",
    "hero_title_en": "Naogaon UNESCO World Heritage & Medieval Grandeur",
    "hero_title_bn": "নওগাঁর বিশ্ব ঐতিহ্য পাহাড়পুর ও সুলতানি গৌরব",
    "hero_sub_en": "Monumental Buddhist monasteries of Somapura Mahavihara, ornate stone Kusumba Mosque, and serene wetlands.",
    "hero_sub_bn": "ইউনেস্কো স্বীকৃত সোমপুর মহাবিহার, অলংকৃত কুসুম্বা মসজিদ ও বরেন্দ্র অঞ্চলের ঐতিহাসিক রাজপ্রাসাদ।",
    "tagline_en": "The premier archaeological treasure-house of northern Bangladesh, celebrated for the colossal eighth-century Buddhist Somapura Mahavihara, medieval black basalt mosques, and the golden expanses of the Barind tract.",
    "tagline_bn": "উত্তরবঙ্গের প্রত্নতাত্ত্বিক ঐতিহ্যের রাজধানী, যা অষ্টম শতাব্দীর সুবিশাল সোমপুর বৌদ্ধ মহাবিহার, পাথরের কুসুম্বা মসজিদ এবং বরেন্দ্রভূমির সোনালী ঐতিহ্যের জন্য বিশ্বখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/naogaon/carousel-1.webp",
            "titleEn": "Somapura Mahavihara (Paharpur) UNESCO World Heritage",
            "titleBn": "সোমপুর মহাবিহার (পাহাড়পুর) বিশ্ব ঐতিহ্য",
            "subtitleEn": "Colossal eighth-century cruciform Buddhist monastery in Badalgachhi built during the Pala dynasty's golden epoch",
            "subtitleBn": "পাল আমলে নির্মিত এশিয়ার সর্ববৃহৎ ক্রুশাকার বৌদ্ধ বিহার, যা প্রাচীন জ্ঞান ও স্থাপত্যবিদ্যার এক অনন্য বিস্ময়"
        },
        {
            "id": 2,
            "image": "images/districts/naogaon/carousel-2.webp",
            "titleEn": "Kusumba Mosque Black Basalt Marvel",
            "titleBn": "কুসুম্বা মসজিদের কালো পাথরের স্থাপত্য",
            "subtitleEn": "Exquisite sixteenth-century Sultanate stone mosque in Manda famous as the 'Black Pearl of Bengal'",
            "subtitleBn": "মান্দায় অবস্থিত ষোড়শ শতকের কালো ব্যাসাল্ট পাথরে নির্মিত অপূর্ব সুলতানি মসজিদ, যা বাংলার কৃষ্ণরত্ন নামে খ্যাত"
        },
        {
            "id": 3,
            "image": "images/districts/naogaon/carousel-3.webp",
            "titleEn": "Dubalhati Rajbari Historic Palatial Façade",
            "titleBn": "দুবলহাটি রাজবাড়ির প্রাচীন রাজপ্রাসাদ",
            "subtitleEn": "Grand aristocratic palace featuring classical Greco-Roman colonnades, royal courtyards, and deep moats",
            "subtitleBn": "নওগাঁ সদরের সুবিশাল ঐতিহাসিক রাজপ্রাসাদ, যার গ্রিক-রোমান স্তম্ভ ও রাজকীয় আঙিনা শতবর্ষের গৌরব প্রকাশ করে"
        },
        {
            "id": 4,
            "image": "images/districts/naogaon/carousel-4.webp",
            "titleEn": "Altadighi National Park & Ancient Water Lake",
            "titleBn": "আলতাদীঘি জাতীয় উদ্যান ও বিশাল জলাধার",
            "subtitleEn": "Historic freshwater reservoir surrounded by dense Sal forests and wildlife sanctuaries in Dhamoirhat",
            "subtitleBn": "ধামইরহাটে শালবনের কোল ঘেঁষে অবস্থিত ঐতিহাসিক সুবিশাল দীঘি ও পরিযায়ী পাখির অভয়ারণ্য"
        },
        {
            "id": 5,
            "image": "images/districts/naogaon/carousel-5.webp",
            "titleEn": "Patisar Rabindra Memorial Palace",
            "titleBn": "পতিসর রবীন্দ্র স্মৃতি কাচারি বাড়ি",
            "subtitleEn": "Tranquil riverine estate of Nobel laureate Rabindranath Tagore along the gentle Nagor River in Atrai",
            "subtitleBn": "আত্রাইয়ে নাগর নদীর তীরে বিশ্বকবি রবীন্দ্রনাথ ঠাকুরের প্রিয় কাচারি বাড়ি ও ঐতিহাসিক কর্মক্ষেত্র"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Somapura Mahavihara",
            "nameBn": "সোমপুর মহাবিহার (পাহাড়পুর)",
            "categoryEn": "UNESCO World Heritage Buddhist Monastery",
            "categoryBn": "ইউনেস্কো বিশ্ব ঐতিহ্যবাহী প্রাচীন বৌদ্ধ বিহার",
            "descEn": "Somapura Mahavihara at Paharpur in Badalgachhi Upazila is the most monumental archaeological site in the Bengal delta and a UNESCO World Heritage Site since 1985. Commissioned in the late eighth century AD by the second Pala emperor Dharmapala, this colossal cruciform Buddhist monastic city served as one of the greatest intellectual universities of classical Asia. The colossal central tiered shrine rises dramatically above a vast quadrangular courtyard enclosed by 177 monk residential cells. Its lower terrace walls are embellished with thousands of exquisite terracotta plaque reliefs depicting animals, deities, dancers, and scenes of daily life. Scholars and monks traveled from Tibet, China, and across Southeast Asia to study philosophy, logic, and astronomy here. Today, it remains an awe-inspiring testimony to Bangladesh's ancient academic and artistic supremacy.",
            "descBn": "নওগাঁর বদলগাছীর পাহাড়পুরে অবস্থিত সোমপুর মহাবিহার ভারতীয় উপমহাদেশের অন্যতম বৃহত্তম ও সর্বশ্রেষ্ঠ বৌদ্ধ বিহার, যা ১৯৮৫ সালে ইউনেস্কো কর্তৃক বিশ্ব ঐতিহ্য হিসেবে ঘোষিত হয়। অষ্টম শতাব্দীর শেষভাগে পাল সম্রাট ধর্মপাল কর্তৃক প্রতিষ্ঠিত এই সুবিশাল জ্ঞানপীঠে সুদূর চীন, তিব্বত ও মালয়েশিয়া থেকে বৌদ্ধ পন্ডিত ও শিক্ষার্থীরা জ্ঞানচর্চায় আসতেন। মূল বিহারের চারপাশ ঘিরে ১৭৭টি ভিক্ষু কক্ষ এবং কেন্দ্রে সুউচ্চ ক্রুশাকার মন্দির রয়েছে, যার দেওয়ালে খোদাই করা হাজার হাজার পোড়ামাটির ফলক প্রাচীন বাংলার লোকজীবন ও শিল্পকলার চমৎকার পরিচয় বহন করে। এটি প্রাচীন স্থাপত্য ও প্রকৌশল বিদ্যার এক অবিস্মরণীয় কীর্তি।",
            "locationEn": "Paharpur, Badalgachhi",
            "locationBn": "পাহাড়পুর, বদলগাছী",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Somapura%20Mahavihara%2C%20Paharpur%2C%20Badalgachhi"
        },
        {
            "id": 2,
            "nameEn": "Kusumba Mosque",
            "nameBn": "কুসুম্বা মসজিদ",
            "categoryEn": "Sixteenth-Century Stone Sultanate Jewel",
            "categoryBn": "ষোড়শ শতকের কালো পাথরের ঐতিহাসিক মসজিদ",
            "descEn": "Kusumba Mosque, located at Manda on the western bank of the historic Atrai River, is revered as one of the finest surviving stone monuments of the late Sultanate period in Bengal. Constructed in 1558 AD during the reign of the Suri dynasty by the nobleman Sulaiman, the mosque is constructed entirely from finely carved dark black basalt stone imported from the Rajmahal hills. Its exterior displays delicately carved stone rosettes, floral bands, and protective battlements, while six ribbed domes crown the sturdy prayer hall. Inside, the elevated stone gallery, exquisitely carved stone mihrabs, and stone pillars display craftsmanship of peerless sophistication. Featured prominently on the Bangladesh five-taka currency note, Kusumba Mosque stands as the celebrated 'Black Pearl of Bengal'.",
            "descBn": "নওগাঁর মান্দা উপজেলায় আত্রাই নদীর পশ্চিম তীরে অবস্থিত কুসুম্বা মসজিদ বাংলার মধ্যযুগীয় পাথরের স্থাপত্যের এক অনন্য বিস্ময়। ১৫৫৮ খ্রিস্টাব্দে সুর সাম্রাজ্যের আমলে জনৈক সুলাইমান কর্তৃক নির্মিত এই মসজিদটি সম্পূর্ণ কালো ব্যাসাল্ট পাথরে তৈরি হওয়ায় এটিকে 'বাংলার কৃষ্ণরত্ন' বলা হয়। মসজিদের দেওয়ালে খোদাই করা পাথরের সূক্ষ্ম ফুল, লতাপাতা ও জ্যামিতিক নকশা কারিগরদের অসামান্য দক্ষতার সাক্ষ্য দেয়। ভেতরের খোদাই করা পাথরের মেহরাব ও রাজকীয় নামাজের উঁচু গ্যালারি অত্যন্ত দৃষ্টিনন্দন। বাংলাদেশের পাঁচ টাকার নোটে স্থান পাওয়া এই মসজিদটি প্রত্নতত্ত্বপ্রেমীদের কাছে এক অবশ্য দর্শনীয় স্থান।",
            "locationEn": "Manda, Naogaon",
            "locationBn": "মান্দা, নওগাঁ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kusumba%20Mosque%2C%20Manda%2C%20Naogaon"
        },
        {
            "id": 3,
            "nameEn": "Dubalhati Rajbari",
            "nameBn": "দুবলহাটি রাজবাড়ি",
            "categoryEn": "Grand Aristocratic Palace Complex",
            "categoryBn": "ঐতিহাসিক জমিদার প্রাসাদ ও নাটমন্দির",
            "descEn": "Dubalhati Rajbari in Naogaon Sadar is a sprawling feudal palace complex established by the influential Raja Krishna Sundar Roy and his successors. The architectural ensemble features expansive royal audience courts, Greek-inspired Corinthian colonnades, multi-tiered residential quarters, and ornate puja pavilions known as the Nachghar. The palace complex was strategically protected by wide perimeter moats known as 'Godi Dighi' and defensive watchtowers. Though weathered by centuries of seasonal monsoons, its grand arched entrances and stucco relief work still radiate imperial majesty. It remains one of northern Bengal's most photographed colonial-era aristocratic monuments.",
            "descBn": "নওগাঁ সদর উপজেলায় অবস্থিত দুবলহাটি রাজবাড়ি বরেন্দ্র অঞ্চলের এক সুবিশাল ও ঐতিহ্যবাহী সামন্তবাদী রাজপ্রাসাদ। রাজা কৃষ্ণসুন্দর রায় এবং তাঁর উত্তরসূরিদের প্রতিষ্ঠিত এই রাজবাড়িতে রয়েছে শত শত কক্ষ, সুবিশাল দরবার হল, ঝুলন্ত বারান্দা এবং রোমান স্থাপত্যের কারুকার্যময় স্তম্ভ। প্রাসাদের অভ্যন্তরীণ নাটমন্দির ও রাসমঞ্চের শৈল্পিক রূপ তৎকালীন আভিজাত্যের পরিচয় দেয়। দুর্গের মতো সুরক্ষিত এই রাজবাড়ির চারপাশ গভীর পরিখা দ্বারা বেষ্টিত ছিল। কালের সাক্ষী হয়ে দাঁড়িয়ে থাকা এই সুরম্য প্রাসাদ দর্শনার্থীদের বাংলার প্রাচীন জমিদারি ঐতিহ্যের এক সোনালী অধ্যায়ে ফিরিয়ে নিয়ে যায়।",
            "locationEn": "Naogaon Sadar",
            "locationBn": "নওগাঁ সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Dubalhati%20Rajbari%2C%20Naogaon%20Sadar"
        },
        {
            "id": 4,
            "nameEn": "Balihar Rajbari",
            "nameBn": "বলিহার রাজবাড়ি",
            "categoryEn": "Historic Royal Estate & Sacred Temples",
            "categoryBn": "ঐতিহাসিক বলিহার জমিদার বাড়ি ও মন্দির",
            "descEn": "Balihar Rajbari in Naogaon Sadar was the seat of the cultured Balihar royal family, renowned in northern Bengal for their patronage of classical music, learning, and temple architecture. The palace complex contains several impressive brick structures, a historic lion gateway, grand banquet courtyards, and numerous consecrated Hindu shrines dedicated to Lord Shiva and Radhamohan. The adjacent freshwater reservoirs, dug by the kings to relieve droughts, mirror the historic temple spires and surrounding palm groves. Visitors can explore the historic brick halls, admire antique carved stone doorways, and soak in the serene atmosphere of feudal antiquity. The site remains a cherished heritage destination for students of regional history.",
            "descBn": "নওগাঁর বলিহার রাজবাড়ি বরেন্দ্রভূমির শিক্ষা, সংস্কৃতি ও নাট্যকলার অন্যতম ঐতিহাসিক পৃষ্ঠপোষক রাজপরিবারের কেন্দ্র ছিল। সুরম্য সিংহদ্বার পেরিয়ে ভেতরে প্রবেশ করলে চোখে পড়ে সুবিশাল রাজদরবার, জলসাঘর এবং প্রাচীন শিব ও রাধাকান্ত জিউর মন্দির। রাজবাড়ির কারুকার্যময় খিলান, অলংকৃত কার্নিশ এবং সানবাঁধানো বিশাল রাজদীঘি এক রাজকীয় আবহ তৈরি করে। এই রাজপরিবারের রাজা কৃষ্ণেন্দ্র রায় ও শরৎচন্দ্র রায় বহু দাতব্য বিদ্যালয় ও পাঠাগার স্থাপন করে স্মরণীয় হয়ে আছেন। ঐতিহ্যের রূপ ও ইতিহাসের গভীরতা উপভোগ করতে বহু পর্যটক এখানে ছুটে আসেন।",
            "locationEn": "Naogaon Sadar",
            "locationBn": "নওগাঁ সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Balihar%20Rajbari%2C%20Naogaon%20Sadar"
        },
        {
            "id": 5,
            "nameEn": "Jagaddala Mahavihara ruins",
            "nameBn": "জগদ্দল মহাবিহারের ধ্বংসাবশেষ",
            "categoryEn": "Pala Dynasty Buddhist Monastery Ruins",
            "categoryBn": "পাল সাম্রাজ্যের প্রাচীন বৌদ্ধ মহাবিহার প্রত্নস্থল",
            "descEn": "Jagaddala Mahavihara at Dhamoirhat represents the archaeological excavations of the renowned Buddhist monastic university founded in the late eleventh century by King Ramapala. Historical manuscripts record that when ancient Nalanda and Vikramashila universities declined, Jagaddala flourished as a major center for Tantric Buddhist scholarship, Tibetan translations, and Sanskrit philosophy. Archaeological excavations have revealed solid brick monastic foundations, decorative terracotta plaques, stone Buddha sculptures, and monastic living cells. The peaceful, wind-swept rural setting provides a poignant backdrop for exploring one of the final great scholastic citadels of the Buddhist era in Bengal. It is recognized as a vital monument for understanding the intellectual history of South Asia.",
            "descBn": "ধামইরহাটে অবস্থিত জগদ্দল মহাবিহার পাল সাম্রাজ্যের শেষ শক্তিশালী রাজা রামপাল কর্তৃক একাদশ শতকের শেষভাগে প্রতিষ্ঠিত এক বিশ্বখ্যাত বৌদ্ধ বিশ্ববিদ্যালয়। নালন্দা ও বিক্রমশীলা বিহারের সমসাময়িক এই মহাবিহারটি তিব্বতি ভাষায় বহু সংস্কৃত পাণ্ডুলিপি অনুবাদের প্রধান কেন্দ্র হিসেবে সুপরিচিত ছিল। প্রত্নতাত্ত্বিক খননকাজের মাধ্যমে এখানে আবিষ্কৃত হয়েছে প্রাচীন বৌদ্ধ ভিক্ষু কক্ষ, সুদৃঢ় দেওয়াল, পোড়ামাটির ফলক এবং অপরূপ পাথরের মূর্তি। বরেন্দ্রভূমির এই নিভৃত প্রত্নস্থলটি প্রাচীন বাংলার বৌদ্ধ দর্শন, সাহিত্য ও উচ্চশিক্ষার এক অনন্য ঐতিহাসিক সাক্ষী।",
            "locationEn": "Dhamoirhat, Naogaon",
            "locationBn": "ধামইরহাট, নওগাঁ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Jagaddala%20Mahavihara%20ruins%2C%20Dhamoirhat%2C%20Naogaon"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Paharpur site museum and gardens",
            "nameBn": "পাহাড়পুর জাদুঘর ও প্রত্নতাত্ত্বিক উদ্যান",
            "categoryEn": "Archaeological Museum & Landscaped Grounds",
            "categoryBn": "আন্তর্জাতিক প্রত্নতাত্ত্বিক জাদুঘর ও উদ্যান",
            "descEn": "The Paharpur Site Museum and landscaped archaeological gardens stand adjacent to the magnificent Somapura Mahavihara, offering visitors profound historical context. The museum exhibits rare basalt statues of Buddha, Bodhisattvas, and Hindu deities excavated from the monastery, alongside ancient gold coins, inscribed clay seals, and ornamental pottery. Hundreds of the finest original eighth-century terracotta plaques are displayed behind protective glass, revealing intimate details of everyday life in classical Bengal. The expansive surrounding gardens feature manicured grassy lawns, fragrant flowerbeds, and shaded stone footpaths offering uninterrupted views of the central monument. It provides an indispensable cultural orientation for travelers exploring northern Bangladesh.",
            "descBn": "সোমপুর মহাবিহার প্রাঙ্গণে অবস্থিত পাহাড়পুর প্রত্নতাত্ত্বিক জাদুঘর ও উদ্যান প্রাচীন ইতিহাসের এক অমূল্য ভাণ্ডার। খননকালে প্রাপ্ত মহামূল্যবান বুদ্ধ ও বোধিসত্ত্বের পাথরের ভাস্কর্য, তাম্রশাসন, প্রাচীন মুদ্রা, টেরাকোটা ফলক ও কারুকার্যময় মাটির পাত্র এই জাদুঘরে সুন্দরভাবে সাজানো রয়েছে। জাদুঘরের বাইরে সুবিশাল সবুজ লন, ছায়াঘেরা বৃক্ষবীথি এবং পরিষ্কার হাঁটার পথ প্রাচীন মনুমেন্টের এক রাজকীয় দৃশ্য উপহার দেয়। ইতিহাস অনুরাগী শিক্ষার্থী ও আন্তর্জাতিক পর্যটকদের জন্য এই জাদুঘর ও উদ্যান এক অবিস্মরণীয় শিক্ষণীয় অভিজ্ঞতা প্রদান করে।",
            "locationEn": "Paharpur, Badalgachhi",
            "locationBn": "পাহাড়পুর, বদলগাছী",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Paharpur%20site%20museum%20and%20gardens%2C%20Paharpur%2C%20Badalgachhi"
        },
        {
            "id": 2,
            "nameEn": "Atrai Riverbank",
            "nameBn": "আত্রাই নদীতীর",
            "categoryEn": "Serene River Valley & Heritage Crossing",
            "categoryBn": "মনোরম আত্রাই নদীতীর ও নৌকা পারাপার",
            "descEn": "The Atrai Riverbank in Naogaon is a poetic freshwater corridor that has nourished human civilization and inland commerce in the Barind tract for millennia. Flowing gently past historic Sultanate mosques and rustic fishing villages, the river is dotted with traditional wooden dinghy boats casting shimmering ripples on the water. During monsoons, the river swells into a majestic water sheet, while winter brings golden sandbanks populated by flocks of migratory shorebirds. Paved embankments near town bridges provide peaceful vantage points for watching fishermen haul in indigenous freshwater catches against colorful evening skies. It is a tranquil sanctuary celebrating the timeless riverine rhythm of northern Bengal.",
            "descBn": "নওগাঁর বুক চিরে বয়ে চলা ঐতিহ্যবাহী আত্রাই নদীর তীর এক অপূর্ব প্রাকৃতিক ও রোমান্টিক দর্শনীয় স্থান। হাজার বছর ধরে এই নদী বরেন্দ্রভূমির বাণিজ্য, সংস্কৃতি ও কৃষিকাজের প্রধান উৎস হিসেবে ভূমিকা রেখে আসছে। নদীর শান্ত জলে ভেসে চলা ছোট ছোট ডিঙি নৌকা এবং তীরের সবুজ ফসলের ক্ষেত চোখ জুড়িয়ে দেয়। শীতকালে নদীর চরে বালি আর পরিযায়ী পাখির মেলা বসে, যা পাখিপ্রেমীদের খুব প্রিয়। নদীপাড়ে বসে মৃদুমন্দ বাতাসে সূর্যাস্ত দেখা এবং জেলেদের কর্মব্যস্ততা অবলোকন করা পর্যটকদের মনে পরম শান্তি এনে দেয়।",
            "locationEn": "Manda and surrounding areas",
            "locationBn": "মান্দা ও সন্নিহিত আত্রাই নদী",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Atrai%20Riverbank%2C%20Manda%20and%20surrounding%20areas"
        },
        {
            "id": 3,
            "nameEn": "Altadighi National Park",
            "nameBn": "আলতাদীঘি জাতীয় উদ্যান",
            "categoryEn": "Immense Heritage Lake & Wildlife Sanctuary",
            "categoryBn": "ঐতিহাসিক মহা দীঘি ও শালবনের জাতীয় উদ্যান",
            "descEn": "Altadighi National Park in Dhamoirhat Upazila is a breathtaking ecological and historical sanctuary centered on an enormous medieval freshwater lake. Legends recount that the lake was dug in the fourteenth century by King Viswarav in honor of his mother's thirst, stretching as far as her red-dyed feet could walk. The crystal-clear lake is framed by dense natural Sal (Shorea robusta) forests teeming with wild deer, golden jackals, monitors, and vibrant birdlife. In winter, thousands of migratory whistling ducks and teals blanket the water surface, creating a paradise for nature photographers. Shaded wooden pavilions and nature trails along the forested banks offer an unparalleled eco-tourism retreat.",
            "descBn": "ধামইরহাটে ভারত সীমান্তবর্তী শালবনের মাঝে অবস্থিত আলতাদীঘি জাতীয় উদ্যান নওগাঁর এক শ্রেষ্ঠ প্রাকৃতিক ও ঐতিহাসিক বিস্ময়। চতুর্দশ শতকে রাজা বিশ্বরাজ তাঁর মায়ের ইচ্ছা পূরণে এই সুবিশাল দীঘিটি খনন করেন বলে জনশ্রুতি রয়েছে। প্রায় এক কিলোমিটার দীর্ঘ এই স্বচ্ছ দীঘিকে ঘিরে রয়েছে সবুজে শ্যামল প্রাকৃতিক শালবন, যা বহু প্রজাতির বন্যপ্রাণী ও পাখির নিরাপদ আবাস। শীত মৌসুমে দীঘির বুকে হাজার হাজার পরিযায়ী পাখির কলকাকলি এক মায়াবী পরিবেশের সৃষ্টি করে। বনের ছায়ায় হাঁটা এবং বিশাল দীঘির সৌন্দর্য উপভোগ করা এক অনন্য রোমাঞ্চকর অভিজ্ঞতা।",
            "locationEn": "Dhamoirhat, Naogaon",
            "locationBn": "ধামইরহাট, নওগাঁ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Altadighi%20National%20Park%2C%20Dhamoirhat%2C%20Naogaon"
        },
        {
            "id": 4,
            "nameEn": "Patisar Rabindra Memorial",
            "nameBn": "পতিসর রবীন্দ্র স্মৃতি কাচারি বাড়ি",
            "categoryEn": "Tagore Literary Estate & Memorial Museum",
            "categoryBn": "বিশ্বকবি রবীন্দ্রনাথ ঠাকুরের স্মৃতি কাচারি বাড়ি",
            "descEn": "The Patisar Rabindra Memorial in Atrai Upazila is the hallowed estate where Nobel laureate Rabindranath Tagore spent deeply productive periods overseeing his ancestral zamindari. Situated on the bank of the winding Nagor River, the two-story brick mansion retains Tagore's study desk, personal bathtub, antique wooden sofa, and original photographs and handwritten letters. It was here that Tagore wrote several famous poems, short stories, and the seminal social welfare essay 'Swadeshi Samaj', while pioneering cooperative agricultural banks for impoverished tenants. The peaceful grounds feature blooming rose gardens, reading rooms, and a riverside pavilion where Tagore communed with nature. It stands as an essential literary sanctuary celebrating Bengal's immortal poetic genius.",
            "descBn": "নওগাঁর আত্রাইয়ে নাগর নদীর তীরে অবস্থিত পতিসর কাচারি বাড়ি বিশ্বকবি রবীন্দ্রনাথ ঠাকুরের সাহিত্য ও কর্মজীবনের স্মৃতিবিজড়িত এক পুণ্যভূমি। পতিসরে অবস্থানকালে কবিগুরু তাঁর বহু অমর কবিতা, ছোটগল্প এবং সমাজকল্যাণমূলক প্রবন্ধ রচনা করেন। এখানে কবির ব্যবহৃত লেখার টেবিল, আরামকেদারা, চিঠিপত্র এবং ঐতিহাসিক আসবাবপত্র অত্যন্ত সযত্নে সংরক্ষিত আছে। কৃষকদের কল্যাণে কবি এখানে একটি সমবায় কৃষি ব্যাংকও প্রতিষ্ঠা করেছিলেন। নাগর নদীর শান্ত হাওয়া এবং কাচারি বাড়ির স্নিগ্ধ পরিবেশ এখনো কবির পদচিহ্ন ও সাহিত্যের সুর যেন বয়ে নিয়ে চলেছে।",
            "locationEn": "Atrai, Naogaon",
            "locationBn": "আত্রাই, নওগাঁ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Patisar%20Rabindra%20Memorial%2C%20Atrai%2C%20Naogaon"
        },
        {
            "id": 5,
            "nameEn": "Naogaon town central park",
            "nameBn": "নওগাঁ শহর সেন্ট্রাল পার্ক (ডিসি পার্ক)",
            "categoryEn": "Civic Botanical Garden & Leisure Space",
            "categoryBn": "নাগরিক বিনোদন উদ্যান ও পরিবারিক লেক চত্বর",
            "descEn": "Naogaon Town Central Park, locally known as the DC Park, is the principal urban recreational haven nestled within Naogaon municipality. The park boasts paved jogging tracks, ornamental water fountains, a serene lake with paddleboat facilities, and lushly maintained flower beds. Families gather under broad shade trees while children enjoy colorful playground rides and open green lawns. In the evenings, decorative illumination transforms the lake perimeter into a charming setting for social walks and community gatherings. The park provides an essential green lung that combines refreshing recreation with family-friendly leisure in the district capital.",
            "descBn": "নওগাঁ জেলা শহরের কেন্দ্রস্থলে অবস্থিত নওগাঁ সেন্ট্রাল পার্ক (ডিসি পার্ক) স্থানীয় বাসিন্দাদের শরীরচর্চা ও বিনোদনের এক চমৎকার স্থান। সুসজ্জিত ফোয়ারা, মনোরম জলাশয় এবং চারপাশের বর্ণিল ফুলের বাগান পার্কটিকে দৃষ্টিনন্দন করে তুলেছে। এখানে লেকের বুকে প্যাডেল বোটিং এবং শিশুদের খেলাধুলার জন্য রয়েছে বিভিন্ন নিরাপদ রাইড। বিকেলে শান্ত পরিবেশে হাঁটার জন্য এবং পরিবার নিয়ে নির্ভেজাল আনন্দ উপভোগ করতে শহরের বহু মানুষ এখানে আসেন। নওগাঁর নাগরিক জীবনে এই উদ্যানটি সতেজতা ও প্রফুল্লতার এক আদর্শ কেন্দ্র।",
            "locationEn": "Naogaon town",
            "locationBn": "নওগাঁ শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Naogaon%20town%20central%20park%2C%20Naogaon%20town"
        }
    ]
}

# 4. SATKHIRA
satkhira = {
    "slug": "satkhira",
    "en": "Satkhira",
    "bn": "সাতক্ষীরা",
    "hero_title_en": "Satkhira Sundarbans Coastal Haven & Ancient Shrines",
    "hero_title_bn": "সাতক্ষীরার সুন্দরবন প্রবেশদ্বার ও প্রাচীন শক্তিপীঠ",
    "hero_sub_en": "Historic capital of Pratapaditya at Ishwaripur, royal hammamkhana, and wild mangrove estuaries.",
    "hero_sub_bn": "ঐতিহাসিক রাজা প্রতাপাদিত্যের রাজধানী ঈশ্বরীপুর, রাজকীয় হাম্মামখানা ও সুন্দরবনের শ্বাসমূলের নিসর্গ।",
    "tagline_en": "The southwestern coastal frontier of Bangladesh, celebrated as the historic seat of Raja Pratapaditya, home to sacred Shaktipeeth shrines, and the western gateway to the majestic Sundarbans mangrove wilderness.",
    "tagline_bn": "বাংলাদেশের দক্ষিণ-পশ্চিম উপকূলীয় জেলা, যা বারো ভূঁইয়ার প্রধান রাজা প্রতাপাদিত্যের রাজধানী, সুপ্রাচীন যশোরেশ্বরী কালী মন্দির ও বিশ্বখ্যাত সুন্দরবনের প্রবেশদ্বার হিসেবে পরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/satkhira/carousel-1.webp",
            "titleEn": "Jashoreeshwari Kali Temple Sacred Shaktipeeth",
            "titleBn": "যশোরেশ্বরী প্রাচীন শক্তিপীঠ মন্দির",
            "subtitleEn": "Revered medieval Hindu shrine in Ishwaripur founded by Raja Pratapaditya, listed among the 51 sacred Shaktipeeths",
            "subtitleBn": "ঈশ্বরীপুরে অবস্থিত ৫১ শক্তিপীঠের অন্যতম পবিত্র ধাম, যা রাজা প্রতাপাদিত্যের রাজধানী ও ভক্তির প্রতীক"
        },
        {
            "id": 2,
            "image": "images/districts/satkhira/carousel-2.webp",
            "titleEn": "Ishwaripur Royal Hammamkhana Architecture",
            "titleBn": "ঈশ্বরীপুরের রাজকীয় হাম্মামখানা",
            "subtitleEn": "Sixteenth-century royal bathhouse complex constructed with vaulted brick domes and sophisticated hot water conduits",
            "subtitleBn": "ষোড়শ শতকের মুঘল ও সুবেদারি আমলের অনন্য স্নানাগার, যার গম্বুজ ও জলাধার প্রকৌশলের বিস্ময়"
        },
        {
            "id": 3,
            "image": "images/districts/satkhira/carousel-3.webp",
            "titleEn": "Sundarbans Western Mangrove Waterways",
            "titleBn": "সুন্দরবনের পশ্চিম মোহনা ও শ্বাসমূলের বন",
            "subtitleEn": "The enchanting wilderness of tidal channels, Royal Bengal tiger tracks, and dense Sundari forests in Shyamnagar",
            "subtitleBn": "শ্যামনগর সীমান্ত ঘেঁষে সুবিশাল সুন্দরবনের শ্বাসমূল, রয়েল বেঙ্গল টাইগারের পদচিহ্ন ও নিবিড় ম্যানগ্রোভ"
        },
        {
            "id": 4,
            "image": "images/districts/satkhira/carousel-4.webp",
            "titleEn": "Mandarbaria Pristine Coastal Sea Beach",
            "titleBn": "মান্দারবাড়িয়া সমুদ্র সৈকত ও দ্বীপ নিসর্গ",
            "subtitleEn": "Remote coastal beach sanctuary facing the Bay of Bengal where mangrove forests merge directly into ocean surf",
            "subtitleBn": "বঙ্গোপসাগরের কোল ঘেঁষে জেগে ওঠা নির্জন বেলাভূমি, যেখানে বনের সবুজ সরাসরি সমুদ্রের ঢেউয়ে মেশে"
        },
        {
            "id": 5,
            "image": "images/districts/satkhira/carousel-5.webp",
            "titleEn": "Sonabaria Medieval Navaratna Temple Complex",
            "titleBn": "সোনাবাড়িয়ার নবরত্ন মন্দির প্রাঙ্গণ",
            "subtitleEn": "Stunning eighteenth-century terracotta temple group in Kalaroa showcasing nine pinnacles and delicate brickwork",
            "subtitleBn": "কলারোয়ায় অবস্থিত অষ্টাদশ শতকের নবরত্ন মন্দির, যার নয়টি রত্নশিখর ও টেরাকোটা কারুকাজ অপূর্ব"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Ishwaripur Hammamkhana and Chanda Bhairab Temple",
            "nameBn": "ঈশ্বরীপুর হাম্মামখানা ও চণ্ড ভৈরব মন্দির",
            "categoryEn": "Sixteenth-Century Royal Bath & Medieval Temple",
            "categoryBn": "ষোড়শ শতকের রাজকীয় স্নানাগার ও ঐতিহাসিক মন্দির",
            "descEn": "The Ishwaripur Hammamkhana and Chanda Bhairab Temple at Shyamnagar represent extraordinary monuments from the capital of Raja Pratapaditya, the legendary chieftain of Bengal's Baro-Bhuiyans. Constructed around 1590 AD with the assistance of skilled Persian masons, the Hammamkhana is a four-domed brick bathhouse equipped with subterranean conduits for circulating hot and cold water. Adjacent to the bathhouse stands the ancient Chanda Bhairab Temple, an elevated brick shrine crowned by an ornate conical sikhara. The precinct preserves the regal aura of Pratapaditya's naval citadel that boldly challenged Mughal imperial hegemony. Walking among these weathered brick vaults offers a vivid encounter with the maritime and military pride of southwestern Bengal.",
            "descBn": "সাতক্ষীরার শ্যামনগরে অবস্থিত ঈশ্বরীপুর হাম্মামখানা ও চণ্ড ভৈরব মন্দির বারো ভূঁইয়ার শ্রেষ্ঠ প্রতাপশালী বীর রাজা প্রতাপাদিত্যের রাজধানী যশোহর-ঈশ্বরীপুরের অনন্য ঐতিহাসিক স্মৃতিচিহ্ন। আনুমানিক ১৫৯০ খ্রিস্টাব্দে নির্মিত চার গম্বুজ বিশিষ্ট এই হাম্মামখানাটিতে ছিল ভূগর্ভস্থ নলের মাধ্যমে ঠান্ডা ও গরম পানির আধুনিক সঞ্চালন ব্যবস্থা। পাশে থাকা প্রাচীন চণ্ড ভৈরব মন্দিরটির লাল ইটের সুউচ্চ শিখর অত্যন্ত নজরকাড়া। মুঘল নৌবহর প্রতিহত করার শক্তিশালী ঘাঁটি হিসেবে ঈশ্বরীপুরের সামরিক গুরুত্ব ছিল অপরিসীম। বাংলার স্বাধীনতা ও আত্মমর্যাদার প্রতীক হিসেবে এই স্থানটি আজও স্বগৌরবে বিরাজমান।",
            "locationEn": "Ishwaripur, Shyamnagar",
            "locationBn": "ঈশ্বরীপুর, শ্যামনগর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Ishwaripur%20Hammamkhana%20and%20Chanda%20Bhairab%20Temple%2C%20Ishwaripur%2C%20Shyamnagar"
        },
        {
            "id": 2,
            "nameEn": "Jashoreeshwari Kali Temple",
            "nameBn": "যশোরেশ্বরী কালী মন্দির",
            "categoryEn": "Sacred Fifty-One Shaktipeeth Hindu Shrine",
            "categoryBn": "৫১ শক্তিপীঠের অন্যতম মহাপবিত্র সনাতন তীর্থ",
            "descEn": "Jashoreeshwari Kali Temple in Ishwaripur is one of the most famous and sacred Hindu pilgrimage sites in the Indian subcontinent, consecrated as one of the 51 Shaktipeeths. Hindu scriptures chronicle that the palms of Goddess Sati's hands fell here, making it a spot of intense divine energy. The shrine was patronized by Raja Pratapaditya in the sixteenth century, featuring an expansive Natmandir with a triangular brick layout and one hundred stone pillars originally supporting the roof. The temple sanctum houses an ancient stone murti of Goddess Kali, attracting hundreds of thousands of pilgrims, especially during annual Kali Puja and Navaratri rituals. It stands as an internationally renowned symbol of deep spiritual devotion and enduring inter-faith heritage.",
            "descBn": "শ্যামনগরের ঈশ্বরীপুরে অবস্থিত শ্রী শ্রী যশোরেশ্বরী কালী মন্দির সমগ্র উপমহাদেশের সনাতন ধর্মাবলম্বীদের কাছে অত্যন্ত পবিত্র ও শ্রদ্ধেয় এক তীর্থস্থান। পৌরাণিক বিশ্বাস অনুসারে এটি সতীর একান্ন শক্তিপীঠের অন্যতম, যেখানে দেবীর করপদ্ম বা হাতের তালু পতিত হয়েছিল। রাজা প্রতাপাদিত্য এই মন্দিরের প্রধান পৃষ্ঠপোষক ছিলেন এবং তিনি এখানে একশত স্তম্ভ বিশিষ্ট সুবিশাল নাটমন্দির নির্মাণ করেন। মন্দিরের গর্ভগৃহে দেবীর অপরূপ বিগ্রহ প্রতিষ্ঠিত রয়েছে। প্রতি বছর কালীপূজা ও বিভিন্ন তিথিতে দেশ-বিদেশের লক্ষ লক্ষ ভক্ত এখানে পূজা দিতে আসেন। এই ঐতিহাসিক তীর্থটি সাতক্ষীরার সাংস্কৃতিক ও আধ্যাত্মিক অহংকার।",
            "locationEn": "Ishwaripur, Shyamnagar",
            "locationBn": "ঈশ্বরীপুর, শ্যামনগর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Jashoreeshwari%20Kali%20Temple%2C%20Ishwaripur%2C%20Shyamnagar"
        },
        {
            "id": 3,
            "nameEn": "Moyna Mosque",
            "nameBn": "ময়না মসজিদ",
            "categoryEn": "Historic Pre-Mughal Brick Mosque",
            "categoryBn": "প্রাক-মুঘল যুগের ঐতিহাসিক এক গম্বুজ মসজিদ",
            "descEn": "Moyna Mosque, located in Kalaroa Upazila, is a treasured pre-Mughal brick monument showcasing early Islamic architecture in southwestern Bengal. The square single-domed sanctuary is built with finely fired red terracotta bricks using lime and clay mortar. Its exterior features curved Bengali cornices, delicate terracotta rosettes, and recessed arched niches that facilitate continuous air circulation. The tranquil setting amidst green village ponds and palm groves enhances the mosque's contemplative dignity. It remains a precious historic gem reflecting the early spread of Islamic architectural traditions into the coastal hinterlands.",
            "descBn": "সাতক্ষীরার কলারোয়া উপজেলায় অবস্থিত ময়না মসজিদ প্রাক-মুঘল মুসলিম স্থাপত্যরীতির এক অনন্য ঐতিহাসিক নিদর্শন। এক গম্বুজ বিশিষ্ট এই প্রাচীন মসজিদটি লাল ইটের নিপুণ গাঁথুনি ও বাঁকানো কার্নিশের জন্য অত্যন্ত দৃষ্টিনন্দন। এর বাইরের দেওয়াল ও মেহরাবে পোড়ামাটির সূক্ষ্ম ফুল ও নকশা অঙ্কিত রয়েছে, যা তৎকালীন শিল্পীদের রুচির পরিচয় দেয়। শান্ত গ্রামীণ পরিবেশ ও পাশের প্রাচীন পুকুর মসজিদটির আধ্যাত্মিক গাম্ভীর্যকে বহুগুণ বাড়িয়ে দিয়েছে। সাতক্ষীরায় ইসলামি ঐতিহ্যের প্রাচীনতম নিদর্শনগুলোর অন্যতম হিসেবে এটি পর্যটকদের মুগ্ধ করে।",
            "locationEn": "Kalaroa, Satkhira",
            "locationBn": "কলারোয়া, সাতক্ষীরা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Moyna%20Mosque%2C%20Kalaroa%2C%20Satkhira"
        },
        {
            "id": 4,
            "nameEn": "Sonabaria historic temple complex",
            "nameBn": "সোনাবাড়িয়া ঐতিহাসিক নবরত্ন মন্দির",
            "categoryEn": "Eighteenth-Century Navaratna Terracotta Complex",
            "categoryBn": "অষ্টাদশ শতকের নবরত্ন মন্দির ও শ্যামসুন্দর দেবালয়",
            "descEn": "The Sonabaria historic temple complex in Kalaroa is an awe-inspiring architectural wonder featuring three interrelated Hindu temples, headlined by the majestic three-tiered Navaratna (nine-jeweled) shrine. Built in 1767 AD by the pious zamindar Hariram Das, the 60-foot-tall central temple boasts nine gracefully tapered spires perched upon three diminishing roof tiers. The outer facades are completely encrusted with thousands of terracotta tiles depicting episodes from the Ramayana, battle scenes, and regional flora and fauna. Adjacent shrines dedicated to Lord Shiva and Radhamohan, alongside a massive bathing tank called 'Durga Sarobar', complete this royal holy precinct. It is celebrated as one of the absolute masterpieces of terracotta architecture in Bengal.",
            "descBn": "কলারোয়ার সোনাবাড়িয়ায় অবস্থিত এই মন্দির প্রাঙ্গণটি অবিভক্ত বাংলার টেরাকোটা স্থাপত্যের এক পরম বিস্ময়কর কীর্তি। ১৭৬৭ খ্রিস্টাব্দে জমিদার হরিরাম দাশ কর্তৃক প্রতিষ্ঠিত এই চত্বরের প্রধান আকর্ষণ হলো ৬০ ফুট উঁচু তিনতলা বিশিষ্ট সুরম্য 'নবরত্ন মন্দির', যার ছাদে নয়টি রত্নশিখর বিদ্যমান। মন্দিরের গায়ে খোদাই করা হাজার হাজার পোড়ামাটির ফলকে রামায়ণের কাহিনী, রাজকীয় শোভাযাত্রা ও দেশীয় জীববৈচিত্র্যের রূপ ফুটে উঠেছে। প্রাঙ্গণে অবস্থিত প্রাচীন শিব মন্দির ও 'দুর্গা সরোবর' দীঘি পুরো কমপ্লেক্সটিকে এক স্বর্গীয় রূপ দিয়েছে। স্থাপত্যের নিপুণতা ও প্রাচীন সৌন্দর্যের কারণে এটি পর্যটকদের কাছে অত্যন্ত প্রিয়।",
            "locationEn": "Kalaroa, Satkhira",
            "locationBn": "কলারোয়া, সাতক্ষীরা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Sonabaria%20historic%20temple%20complex%2C%20Kalaroa%2C%20Satkhira"
        },
        {
            "id": 5,
            "nameEn": "Prannath Roy Zamindar Bari",
            "nameBn": "প্রাণনাথ রায় জমিদার বাড়ি",
            "categoryEn": "Colonial Riverfront Aristocratic Palace",
            "categoryBn": "ঐতিহাসিক নদী বন্দর ও জমিদার প্রাসাদ",
            "descEn": "Prannath Roy Zamindar Bari at Debhata is an imposing nineteenth-century colonial estate constructed along the bustling Ichamati River corridor. The palace exhibits neoclassical colonnaded facades, decorative ironwork balconies, grand reception halls, and subterranean escape tunnels designed for security during regional unrest. The zamindars played an influential role in developing Debhata as a flourishing municipal port and river trading entrepot linking southwestern Bengal with Kolkata. Today, the majestic weathered columns, sprawling banquet courtyards, and riverfront steps provide an evocative glimpse into the wealth and sophistication of late colonial zamindari culture. It is an essential stop for heritage enthusiasts touring the Ichamati basin.",
            "descBn": "সাতক্ষীরার দেবহাটায় ইছামতী নদীর তীরে অবস্থিত প্রাণনাথ রায়ের জমিদার বাড়ি একসময় দক্ষিণ বাংলার অন্যতম ঐশ্বর্যশালী প্রাসাদ ছিল। ঊনবিংশ শতাব্দীর মাঝামাঝি সময়ে নির্মিত এই সুরম্য প্রাসাদে রয়েছে ইউরোপীয় ধাঁচের করিন্থিয়ান স্তম্ভ, সুবিশাল নাচঘর, খিলানযুক্ত বারান্দা এবং গোপন সুড়ঙ্গপথ। তৎকালীন সময়ে দেবহাটাকে এক আধুনিক পৌরসভা ও প্রধান নদী বন্দর হিসেবে গড়ে তোলায় এই জমিদারদের অবদান ছিল অপরিসীম। নদীর হাওয়া ও প্রাচীন অট্টালিকার জাঁকজমকপূর্ণ ধ্বংসাবশেষ আজও দর্শকদের রোমাঞ্চিত করে। নদীকেন্দ্রিক জমিদারির ইতিহাস জানতে এটি এক চমৎকার গন্তব্য।",
            "locationEn": "Debhata, Satkhira",
            "locationBn": "দেবহাটা, সাতক্ষীরা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Prannath%20Roy%20Zamindar%20Bari%2C%20Debhata%2C%20Satkhira"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Sundarbans gateway at Kaliganj and Shyamnagar",
            "nameBn": "শ্যামনগর সুন্দরবন পশ্চিম প্রবেশদ্বার",
            "categoryEn": "UNESCO World Heritage Mangrove Gateway",
            "categoryBn": "সুন্দরবনের আন্তর্জাতিক ম্যানগ্রোভ ও বাঘের বন প্রবেশদ্বার",
            "descEn": "The Sundarbans gateway at Shyamnagar and Kaliganj is the premier ecotourism entry portal to the world's largest mangrove forest on its western boundary. Here, travelers embark on motor-powered river cruisers and wooden boats into tidal estuaries lined with breathing pneumatophores of Sundari and Golpata trees. The region is home to the majestic Royal Bengal tiger, spotted deer herds, saltwater crocodiles, and playful Gangetic river dolphins. Forest department watchtowers at Munshiganj and Burigoalini offer breathtaking views across unbroken horizons of green wilderness meeting emerald waters. It provides an authentic, thrilling immersion into Bangladesh's untamed natural wonder.",
            "descBn": "সাতক্ষীরার শ্যামনগর ও মুন্সীগঞ্জ সুন্দরবনের পশ্চিম অংশের প্রধান ও রোমাঞ্চকর প্রবেশদ্বার। এখান থেকেই শুরু হয় বিশ্বের বৃহত্তম অবিভক্ত ম্যানগ্রোভ অরণ্যের রহস্যময় জলপথ। পর্যটকরা ট্রলার ও জাহাজে চড়ে গোলপাতা, সুন্দরী ও কেওড়া বনের মাঝ দিয়ে এঁকেবেঁকে চলা নদী-খালে ভ্রমণ করতে পারেন। এই অঞ্চলে রয়েছে রয়েল বেঙ্গল টাইগারের পদচারণা, চিত্রা হরিণের পাল, লবণাক্ত পানির কুমির ও ডলফিনের অবাধ বিচরণ। বুড়িগোয়ালিনী ও কলাগাছিয়ার সুউচ্চ ওয়াচটাওয়ার থেকে সবুজে ঢাকা সুন্দরবনের অপার দিগন্ত অবলোকন করা যায়, যা ভ্রমণপিপাসুদের এক অনন্য জীবনভর স্মৃতি উপহার দেয়।",
            "locationEn": "Shyamnagar, Satkhira",
            "locationBn": "শ্যামনগর, সাতক্ষীরা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Sundarbans%20gateway%20at%20Kaliganj%20and%20Shyamnagar%2C%20Shyamnagar%2C%20Satkhira"
        },
        {
            "id": 2,
            "nameEn": "Mandarbaria Sea Beach",
            "nameBn": "মান্দারবাড়িয়া সমুদ্র সৈকত",
            "categoryEn": "Pristine Offshore Mangrove Beach Sanctuary",
            "categoryBn": "সুন্দরবনের নির্জন সমুদ্র সৈকত ও সাগর মোহনা",
            "descEn": "Mandarbaria Sea Beach is an extraordinary, unspoiled coastal beach sanctuary situated in the deep southwest corner of the Sundarbans where mangrove forest directly meets the Bay of Bengal. Accessible only by boat through tidal rivers, this pristine strand of white sand remains completely untouched by urban commercialism. Travelers can witness spectacular sunrises and sunsets painting the oceanic horizons, with tiger paw prints and sea turtle tracks frequently visible along the wet shore. Flocks of white egrets, sandpipers, and seagulls circle overhead while wild deer graze near the forest margins. It is celebrated by intrepid adventurers as one of the wildest and most pristine coastal frontiers in South Asia.",
            "descBn": "মান্দারবাড়িয়া সমুদ্র সৈকত সুন্দরবনের গভীর দক্ষিণে বঙ্গোপসাগরের কোল ঘেঁষে অবস্থিত এক অপরূপ ও নির্জন বেলাভূমি। নদীপথে ট্রলারে চড়ে পৌঁছানো এই সৈকতে ম্যানগ্রোভ বন সরাসরি সমুদ্রের আছড়ে পড়া ঢেউয়ের সাথে আলিঙ্গন করে। মানুষের কোলাহলমুক্ত এই সৈকতে প্রায়ই বাঘের তাজা পায়ের ছাপ এবং লাল কাঁকড়ার অবাধ বিচরণ দেখা যায়। দিগন্তজোড়া নীল জলরাশির ওপর সূর্যোদয় ও সূর্যাস্তের দৃশ্য যেন কোনো দক্ষ শিল্পীর আঁকা ক্যানভাস। প্রকৃতির আদিম ও নিঃশব্দ রূপ যারা ভালোবাসেন, তাদের কাছে মান্দারবাড়িয়া এক চরম রোমাঞ্চকর স্বর্গরাজ্য।",
            "locationEn": "Mandarbaria island",
            "locationBn": "মান্দারবাড়িয়া দ্বীপ, সাতক্ষীরা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Mandarbaria%20Sea%20Beach%2C%20Mandarbaria%20island"
        },
        {
            "id": 3,
            "nameEn": "Kholpetua Riverbank",
            "nameBn": "খোলপেটুয়া নদীতীর",
            "categoryEn": "Majestic Tidal Riverway & Rural Embankment",
            "categoryBn": "জোয়ার-ভাটার উত্তাল খোলপেটুয়া নদী ও উপকূলীয় নিসর্গ",
            "descEn": "The Kholpetua Riverbank in Assasuni and Shyamnagar is a dynamic tidal river expanse celebrated for its sweeping coastal beauty and vibrant fishermen communities. The river carries the powerful ebb and flow of the tides from the Bay of Bengal, creating dramatic water level changes that shape local livelihood and culture. From the elevated flood protection embankments, visitors can enjoy refreshing saline breezes, watching fleets of motorized fishing trawlers depart toward deep-sea grounds. In the evenings, sky colors mirror across the vast river waves, while riverside crab fattening farms and shrimp ghers showcase southwestern coastal agro-heritage. It offers a captivating window into the resilient riverine spirit of Satkhira.",
            "descBn": "সাতক্ষীরার আশাশুনি ও শ্যামনগর উপজেলার কোল ঘেঁষে বয়ে যাওয়া খোলপেটুয়া নদী উপকূলীয় জীবন ও প্রকৃতির এক জীবন্ত প্রতীক। বঙ্গোপসাগরের তীব্র জোয়ার-ভাটার সাথে তাল মিলিয়ে চলা এই নদীর সুবিশাল রূপ যে কাউকে মুগ্ধ করে। নদীর পাড়ের ওয়াপদা বাঁধে দাঁড়িয়ে দিগন্তবিস্তৃত জলরাশি ও দূরবর্তী জেলে ট্রলারের আনাগোনা উপভোগ করা যায়। নদীর শান্ত বাতাসে গোধূলিবেলায় সূর্যাস্তের লাল আভা যখন জলে প্রতিফলিত হয়, তখন এক অপার্থিব দৃশ্যের অবতারণা ঘটে। উপকূলীয় মানুষের জীবনযুদ্ধ ও নদীমাতৃক সৌন্দর্য এক অনন্য রূপ ধারণ করেছে খোলপেটুয়ার তীরে।",
            "locationEn": "Assasuni and Shyamnagar",
            "locationBn": "আশাশুনি ও শ্যামনগর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kholpetua%20Riverbank%2C%20Assasuni%20and%20Shyamnagar"
        },
        {
            "id": 4,
            "nameEn": "Mozaffar Garden",
            "nameBn": "মোজাফফর গার্ডেন অ্যান্ড রিসোর্ট",
            "categoryEn": "Eco-Amusement Park & Botanical Retreat",
            "categoryBn": "ইকো অ্যামিউজমেন্ট পার্ক ও পরিবারিক বিনোদন কেন্দ্র",
            "descEn": "Mozaffar Garden and Resort on the outskirts of Satkhira town is the largest private eco-amusement park and family leisure center in the southwestern region. Spanning extensive landscaped grounds, the retreat features interconnected lakes with paddle boats, lush botanical gardens, a mini zoo with indigenous fauna, and colorful children's amusement rides. Walkways bordered by royal palms and flowering hedges lead to comfortable picnic sheds and waterside dining cottages. Families and tour groups visit year-round for weekend picnics, recreational fishing, and peaceful open-air relaxation. It stands as Satkhira's most popular contemporary family entertainment destination.",
            "descBn": "সাতক্ষীরা শহরের অদূরে অবস্থিত মোজাফফর গার্ডেন অ্যান্ড রিসোর্ট দক্ষিণ-পশ্চিমাঞ্চলের অন্যতম বৃহৎ ও সুসজ্জিত বিনোদন কেন্দ্র। সুবিশাল এলাকা জুড়ে বিস্তৃত এই পার্কে রয়েছে নয়নাভিরাম লেক, প্যাডেল বোটিং, মিনি চিড়িয়াখানা এবং শিশুদের জন্য বিভিন্ন রোমাঞ্চকর রাইড। চারপাশের সুদৃশ্য বাগান, দেশি-বিদেশি ফুলের সমাহার এবং শান্ত পরিবেশ পারিবারিক পিকনিকের জন্য অত্যন্ত উপযুক্ত। অবকাশ যাপনের পাশাপাশি এখানে বিভিন্ন সামাজিক অনুষ্ঠান আয়োজনের সুব্যবস্থা রয়েছে। সবুজের সান্নিধ্যে একদিন আনন্দময় সময় কাটাতে এটি ভ্রমণকারীদের প্রথম পছন্দ।",
            "locationEn": "Satkhira town outskirts",
            "locationBn": "সাতক্ষীরা শহরতলী",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Mozaffar%20Garden%2C%20Satkhira%20town%20outskirts"
        },
        {
            "id": 5,
            "nameEn": "Satkhira municipal park",
            "nameBn": "সাতক্ষীরা শহীদ আব্দুর রাজ্জাক পৌর পার্ক",
            "categoryEn": "Civic Botanical Garden & Promenade",
            "categoryBn": "শহীদ আব্দুর রাজ্জাক পৌর পার্ক ও লেক চত্বর",
            "descEn": "Satkhira Municipal Park, famously dedicated to liberation war hero Shaheed Abdur Razzak, is the vibrant central green lung of Satkhira city. Encircling a historic freshwater lake, the park features paved jogging avenues, shaded flower-covered pavilions, and open-air recreational plazas. Residents gather daily for brisk morning fitness walks, lively intellectual discussions under rain trees, and refreshing evening breezes. Children enjoy safe dedicated playground zones while colorful ambient lighting illuminates the water walkways at night. The park serves as the welcoming heart of civic community life and social recreation in the district capital.",
            "descBn": "সাতক্ষীরা শহরের প্রাণকেন্দ্রে অবস্থিত শহীদ আব্দুর রাজ্জাক পৌর পার্ক শহরবাসীর প্রিয় প্রাতঃভ্রমণ ও পারিবারিক বিনোদনের উন্মুক্ত চত্বর। বিশাল দীঘিকে ঘিরে গড়ে ওঠা এই পার্কে রয়েছে পাকা ওয়াকওয়ে, সুশোভিত বৃক্ষরাজি এবং মুক্তমঞ্চ। প্রতিদিন বিকেলে সব বয়সী মানুষ এখানে মুক্ত হাওয়া উপভোগ করতে এবং বন্ধুদের সাথে আড্ডা দিতে আসেন। শিশুদের খেলাধুলার জন্য মনোরম পরিবেশ ও রাতে লেকপাড়ের চমৎকার আলোকসজ্জা পার্কটিকে আনন্দময় করে তোলে। সাতক্ষীরা শহরের সামাজিক মিলনমেলা হিসেবে এই পার্কটি অত্যন্ত পরিচিত।",
            "locationEn": "Satkhira town",
            "locationBn": "সাতক্ষীরা শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Satkhira%20municipal%20park%2C%20Satkhira%20town"
        }
    ]
}

# 5. KHAGRACHHARI
khagrachhari = {
    "slug": "khagrachhari",
    "en": "Khagrachhari",
    "bn": "খাগড়াছড়ি",
    "hero_title_en": "Khagrachhari Mystical Hills & Indigenous Heritage",
    "hero_title_bn": "খাগড়াছড়ির রহস্যময় আলুটিলা গুহা ও পাহাড়ি ঝরনা",
    "hero_sub_en": "Subterranean Alutila mystery caves, gushing Richhang waterfalls, and vibrant Hill Tracts tribal cultures.",
    "hero_sub_bn": "ভূগর্ভস্থ আলুটিলা রহস্যময় সুড়ঙ্গ, রিছাং জলপ্রপাত ও পার্বত্য পাহাড়ি সংস্কৃতির বৈচিত্র্যময় রূপ।",
    "tagline_en": "The captivating hill-forest frontier of the Chittagong Hill Tracts, renowned for the subterranean mystery of Alutila cave, tumbling mountain cascades, and the rich traditions of the Chakma, Marma, and Tripura peoples.",
    "tagline_bn": "পার্বত্য চট্টগ্রামের এক অপরূপ পাহাড়ি জনপদ, যা আলুটিলার রহস্যময় সুরঙ্গ, পাহাড়ি ঝরনার গর্জন এবং চাকমা, মারমা ও ত্রিপুরা জনগোষ্ঠীর বর্ণাঢ্য সংস্কৃতির জন্য বিখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/khagrachhari/carousel-1.webp",
            "titleEn": "Alutila Mysterious Subterranean Cave",
            "titleBn": "আলুটিলার রহস্যময় প্রাকৃতিক সুড়ঙ্গ গুহা",
            "subtitleEn": "Thrilling 100-meter dark stone cave tunnel embedded within ancient limestone hills, navigated by flaming bamboo torches",
            "subtitleBn": "চুনাপাথরের পাহাড়ের তলদেশ দিয়ে বয়ে চলা শীতল জলের প্রাচীন গুহা, যা মশাল জ্বালিয়ে অতিক্রম করতে হয়"
        },
        {
            "id": 2,
            "image": "images/districts/khagrachhari/carousel-2.webp",
            "titleEn": "Richhang Tumbling Mountain Waterfall",
            "titleBn": "রিছাং পাহাড়ি জলপ্রপাত ও প্রাকৃতিক স্লাইড",
            "subtitleEn": "Cascading mountain waterfall in Matiranga dropping over polished natural stone slopes amidst lush rainforest greenery",
            "subtitleBn": "সবুজ পাহাড়ের খাঁদ বেয়ে নেমে আসা চোখজুড়ানো ঝরনা, যার মসৃণ পাথুরে ঢালে জলকেলিতে মেতে ওঠে পর্যটকরা"
        },
        {
            "id": 3,
            "image": "images/districts/khagrachhari/carousel-3.webp",
            "titleEn": "Tareng Panoramic Hilltop Viewpoint",
            "titleBn": "তারেং পাহাড়ের চূড়া ও মেঘের ভেলা",
            "subtitleEn": "High-altitude observation point offering breathtaking 360-degree vistas of rolling hill ranges and misty cloud seas",
            "subtitleBn": "মেঘের ছোঁয়া পাওয়া সুউচ্চ পাহাড়ি ভিউপয়েন্ট, যেখান থেকে দূর-দিগন্তের সবুজ পাহাড়ের ঢেউ অবলোকন করা যায়"
        },
        {
            "id": 4,
            "image": "images/districts/khagrachhari/carousel-4.webp",
            "titleEn": "Dighinala Sacred Buddhist Temple & Giant Buddha",
            "titleBn": "দীঘিনালা শান্তিনিকেতন বৌদ্ধ বিহার",
            "subtitleEn": "Spiritual Buddhist monastery sanctuary in Dighinala set amidst rolling orchards and tranquil prayer bells",
            "subtitleBn": "দীঘিনালার সবুজ পাহাড়ের বুকে প্রতিষ্ঠিত পরম শ্রদ্ধেয় বৌদ্ধ বিহার ও ধ্যানকেন্দ্র"
        },
        {
            "id": 5,
            "image": "images/districts/khagrachhari/carousel-5.webp",
            "titleEn": "Chengi River Valley & Hanging Bridges",
            "titleBn": "চেঙ্গী নদী উপত্যকা ও ঝুলন্ত সেতু",
            "subtitleEn": "Scenic mountain river flowing gently across the green valley floor under traditional footbridges in Khagrachhari",
            "subtitleBn": "পাহাড়ের কোল বেয়ে ছুটে চলা খরস্রোতা চেঙ্গী নদী ও স্থানীয় পাহাড়ি জনপদের সংযোগকারী ঝুলন্ত সেতু"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Alutila Cave",
            "nameBn": "আলুটিলা রহস্যময় গুহা",
            "categoryEn": "Primeval Subterranean Cave Geological Wonder",
            "categoryBn": "প্রাকৃতিক ভূগর্ভস্থ সুড়ঙ্গ ও ভূতাত্ত্বিক বিস্ময়",
            "descEn": "Alutila Cave (Matiranga) is a breathtaking geological wonder and one of the most mysterious natural caves in South Asia. Embedded deep inside a dense limestone and shale mountain ridge at an elevation of nearly 1,000 feet, this dark subterranean tunnel spans approximately 100 meters from entrance to exit. Travelers descend steep concrete stairs into the jungle to ignite flaming bamboo torches before wading through ankle-deep subterranean crystal streams flowing over slippery stone floors. Inside, the echoing sound of dripping water, natural vaulted stone ceilings, and complete darkness create an unforgettable thrill of exploration. The cave is held in sacred awe by local indigenous communities and draws adventurous travelers from across the nation.",
            "descBn": "খাগড়াছড়ির মাটিরাঙ্গায় অবস্থিত আলুটিলা গুহা বাংলাদেশের সবচেয়ে রোমাঞ্চকর ও রহস্যময় প্রাকৃতিক সুড়ঙ্গ। পাহাড়ের প্রায় ১০০০ ফুট উঁচুতে অবস্থিত এই প্রাকৃতিক গুহাটি লম্বায় প্রায় ১০০ মিটার। বাঁশের তৈরি জ্বলন্ত মশাল হাতে নিয়ে পর্যটকরা এই অন্ধকার সুরঙ্গের ভেতরে প্রবেশ করেন, যেখানে পায়ের নিচে অবিরাম বয়ে চলে শীতল পাহাড়ি ঝিরির জল। সুড়ঙ্গের ভেতরের রহস্যময় নিস্তব্ধতা, পাথুরে ছাদ থেকে চুইয়ে পড়া জলের শব্দ এবং গা ছমছমে অন্ধকার এক পরম রোমাঞ্চকর অনুভূতির জন্ম দেয়। প্রকৃতির আদিম রূপ ও সাহসিকতার স্বাদ পেতে আলুটিলা গুহা ভ্রমণ এক অনন্য অভিজ্ঞতা।",
            "locationEn": "Matiranga, Khagrachhari",
            "locationBn": "মাটিরাঙ্গা, খাগড়াছড়ি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Alutila%20Cave%2C%20Matiranga%2C%20Khagrachhari"
        },
        {
            "id": 2,
            "nameEn": "Richhang Waterfall",
            "nameBn": "রিছাং জলপ্রপাত",
            "categoryEn": "Cascading Natural Mountain Cascade",
            "categoryBn": "প্রাকৃতিক পাহাড়ি জলপ্রপাত ও জলস্লাইড",
            "descEn": "Richhang Waterfall, located in the deep mountain folds of Matiranga, is a magnificent natural waterfall that tumbles continuously over sheer terraced rock formations. Falling from a height of approximately one hundred feet, the crystal-clear mountain stream flows over smooth, sloped natural stone chutes before forming a refreshing pool below. The unique natural water slide formed by polished rocks allows visitors to slide joyfully into cool mountain water amidst dense rainforest vegetation. Wooden footbridges and elevated jungle pathways offer spectacular panoramic viewpoints of the cascade surrounded by wild ferns, bamboo groves, and native orchids. It stands as an iconic wilderness adventure destination in the Chittagong Hill Tracts.",
            "descBn": "মাটিরাঙ্গার নিবিড় পাহাড়ি অরণ্যের গভীরে অবস্থিত রিছাং ঝরনা খাগড়াছড়ির অন্যতম আকর্ষণীয় ও জনপ্রিয় জলপ্রপাত। প্রায় একশত ফুট উঁচু পাহাড়ের চূড়া থেকে অনবরত আছড়ে পড়া স্বচ্ছ জলরাশি এক সম্মোহনী শব্দের সৃষ্টি করে। ঝরনার নিচের মসৃণ ও ঢালু পাথুরে অংশে পানির প্রবাহ এক অপূর্ব প্রাকৃতিক স্লাইড তৈরি করেছে, যেখানে পর্যটকরা পরম আনন্দে জলকেলিতে মেতে ওঠেন। চারপাশের বুনো গাছপালা, ফার্ন ও অর্কিডের সমাহার স্থানটিকে অপার্থিব সৌন্দর্য দান করেছে। পাহাড়ি পথের ক্লান্তি ভুলে প্রকৃতির শীতল পরশ পেতে রিছাং ঝরনার কোনো বিকল্প নেই।",
            "locationEn": "Matiranga, Khagrachhari",
            "locationBn": "মাটিরাঙ্গা, খাগড়াছড়ি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Richhang%20Waterfall%2C%20Matiranga%2C%20Khagrachhari"
        },
        {
            "id": 3,
            "nameEn": "Dighinala Buddhist Temple",
            "nameBn": "দীঘিনালা বনবিহার ও বৌদ্ধ মন্দির",
            "categoryEn": "Sacred Hill Tracts Monastic Sanctuary",
            "categoryBn": "পাহাড়ের পবিত্র বৌদ্ধ বিহার ও শান্তিনিকেতন",
            "descEn": "Dighinala Buddhist Temple is a revered monastic sanctuary that anchors the spiritual and cultural heritage of the Buddhist communities in northern Khagrachhari. Set atop a tranquil forested knoll, the temple complex features traditional multi-tiered pagodas, gleaming golden stupas, and a colossal statue of Gautama Buddha depicted in serene meditation. Saffron-robed monks chant sacred Pali sutras in open-air prayer halls, their bells echoing peacefully across the surrounding valleys. The complex serves as an important center of spiritual study, meditation retreats, and preservation of indigenous Chakma and Marma religious manuscripts. Travelers are welcomed with peaceful grace into this haven of mindfulness and ancient devotion.",
            "descBn": "দীঘিনালার মনোরম পাহাড়ি উপত্যকায় প্রতিষ্ঠিত এই বৌদ্ধ মন্দিরটি পার্বত্য অঞ্চলের ধর্মীয় ও সাংস্কৃতিক ঐতিহ্যের এক পরম পবিত্র কেন্দ্র। পাহাড়ের ধাপে ধাপে গড়ে ওঠা এই কমপ্লেক্সে রয়েছে নান্দনিক প্যাগোডা, স্বর্ণালি স্তূপ এবং ধ্যানমগ্ন বুদ্ধের সুবিশাল অপরূপ মূর্তি। মন্দিরের ভেতরে সংরক্ষিত রয়েছে প্রাচীন পালি পাণ্ডুলিপি ও ধর্মীয় সামগ্রী। সকাল ও সন্ধ্যায় ঘণ্টার ধ্বনি এবং ভিক্ষুদের শান্তিময় মন্ত্রোচ্চারণ পুরো পাহাড়ে এক স্বর্গীয় আবহ সৃষ্টি করে। আধ্যাত্মিক প্রশান্তি ও পাহাড়ি জনপদের নিবিড় জীবনাচার দর্শনে এই বিহারটি অত্যন্ত মর্যাদাপূর্ণ।",
            "locationEn": "Dighinala, Khagrachhari",
            "locationBn": "দীঘিনালা, খাগড়াছড়ি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Dighinala%20Buddhist%20Temple%2C%20Dighinala%2C%20Khagrachhari"
        },
        {
            "id": 4,
            "nameEn": "Khagrachhari royal palace",
            "nameBn": "খাগড়াছড়ি মং রাজবাড়ি",
            "categoryEn": "Traditional Mong Royal Palace & Heritage Seat",
            "categoryBn": "ঐতিহাসিক মং রাজার রাজপ্রাসাদ ও ঐতিহ্য",
            "descEn": "The Khagrachhari Royal Palace is the ancestral seat of the Mong Circle Chief, one of the three traditional royal circles governing the Chittagong Hill Tracts. Located in Khagrachhari town, the compound includes royal audience chambers, traditional wooden council halls, and ceremonial courtyards where ancestral customs and tribal judicial disputes are resolved according to customary law. The architecture fuses traditional indigenous wooden craftsmanship with colonial-era planning, housing antique cannons, royal royal swords, and heirloom textiles. The annual Rajpunyah festival gathers hundreds of village headmen and subjects in vibrant traditional attire to pay homage to the King. The palace stands as an enduring living monument to indigenous self-governance and monarchical heritage.",
            "descBn": "খাগড়াছড়ি শহরে অবস্থিত মং রাজবাড়ি পার্বত্য চট্টগ্রামের তিনটি ঐতিহ্যবাহী প্রশাসনিক সার্কেলের অন্যতম প্রধান মং রাজার রাজকীয় বাসভবন। শতবর্ষের ঐতিহ্যবাহী এই রাজপ্রাসাদটিতে এখনো নিজস্ব প্রথা ও রীতিনীতি অনুযায়ী পাহাড়ি বিচার ও সামাজিক শাসন ব্যবস্থা পরিচালিত হয়। কাঠের নিপুণ কারুকাজে তৈরি রাজপ্রাসাদে সংরক্ষিত আছে প্রাচীন কামান, রাজকীয় তরবারি, প্রাচীন পোশাক ও ঐতিহ্যবাহী স্মারক। প্রতি বছর অনুষ্ঠিত ঐতিহাসিক 'রাজপুণ্যাহ' উৎসবে রাজা ও পাহাড়ি প্রজাদের মেলবন্ধন দেখার মতো এক রাজকীয় দৃশ্য। পাহাড়ি জাতিগোষ্ঠীর আত্মপরিচয় ও ঐতিহ্যের স্মারক হিসেবে এই রাজবাড়ি অত্যন্ত গুরুত্বপূর্ণ।",
            "locationEn": "Khagrachhari town",
            "locationBn": "খাগড়াছড়ি শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Khagrachhari%20royal%20palace%2C%20Khagrachhari%20town"
        },
        {
            "id": 5,
            "nameEn": "Hill Tracts indigenous cultural centers",
            "nameBn": "ক্ষুদ্র নৃগোষ্ঠীর সাংস্কৃতিক ইনস্টিটিউট",
            "categoryEn": "Tribal Ethnic Cultural Institute & Museum",
            "categoryBn": "পাহাড়ি নৃগোষ্ঠীর সাংস্কৃতিক জাদুঘর ও সংগ্রহশালা",
            "descEn": "The Hill Tracts Indigenous Cultural Center and Museum in Khagrachhari is an indispensable cultural institution dedicated to documenting and celebrating the diverse ethnic groups of the hill districts. The museum galleries display authentic ethnic costumes, intricately woven textiles from Chakma, Marma, and Tripura looms, hunting implements, musical instruments, and antique jewelry. Interactive displays and diorama exhibits depict the traditional festivals of Bizu, Sangrai, and Baisu, capturing the rich animist and Buddhist traditions of the communities. The center hosts regular live traditional dance performances, linguistic research archives, and handicraft training workshops. It offers visitors a profound and respectful appreciation of the rich human tapestry of the Chittagong Hill Tracts.",
            "descBn": "খাগড়াছড়ি শহরে অবস্থিত ক্ষুদ্র নৃগোষ্ঠীর সাংস্কৃতিক ইনস্টিটিউট ও জাদুঘর পার্বত্য অঞ্চলের চাকমা, মারমা, ত্রিপুরাসহ বিভিন্ন আদিবাসী সম্প্রদায়ের বর্ণাঢ্য সংস্কৃতি সংরক্ষণের প্রধান প্রতিষ্ঠান। জাদুঘরের গ্যালারিগুলোতে অত্যন্ত সুন্দরভাবে প্রদর্শিত রয়েছে পাহাড়ি জনগোষ্ঠীর ঐতিহ্যবাহী কোমর তাঁতের পোশাক, অলংকার, বাঁশ ও মাটির পাত্র, শিকারের অস্ত্র এবং প্রাচীন বাদ্যযন্ত্র। বিজু, সাংগ্রাই ও বৈসু উৎসবের আনন্দঘন চিত্র এবং পাহাড়ি জীবনের বিভিন্ন দিক এখানে জীবন্ত হয়ে উঠেছে। পার্বত্য সংস্কৃতির বৈচিত্র্য ও সমৃদ্ধি উপলব্ধি করার জন্য এই সাংস্কৃতিক কেন্দ্রটি এক অনন্য পাঠশালা।",
            "locationEn": "Khagrachhari town",
            "locationBn": "খাগড়াছড়ি শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Hill%20Tracts%20indigenous%20cultural%20centers%2C%20Khagrachhari%20town"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Alutila Tourist Center",
            "nameBn": "আলুটিলা পর্যটন কেন্দ্র ও ভিউপয়েন্ট",
            "categoryEn": "Panoramic Mountain Park & Cloud Observation",
            "categoryBn": "সুউচ্চ পাহাড়ি পর্যটন কেন্দ্র ও মেঘ দর্শন কেন্দ্র",
            "descEn": "The Alutila Tourist Center sits atop the highest ridge overlooking Khagrachhari town, providing a world-class eco-tourism haven for travelers. The landscaped park complex features paved walkways hanging over steep emerald ravines, scenic wooden gazebos, an amphitheater, and multi-level observation towers. On clear mornings, visitors are treated to an astonishing phenomenon as thick seas of white clouds fill the valleys below while the golden sunrise illuminates distant mountain peaks. The cool mountain air, flowering gardens, and panoramic views stretching into neighboring Tripura make it a must-visit highland retreat. It is the premier destination for sunset watching and mountain photography in Khagrachhari.",
            "descBn": "আলুটিলা পর্যটন কেন্দ্র খাগড়াছড়ি শহরের কোল ঘেঁষে পাহাড়ের চূড়ায় গড়ে ওঠা এক নয়নকাড়া ইকোপার্ক। খাড়া পাহাড়ের ঢালে নির্মিত দৃষ্টিনন্দন ওয়াকওয়ে, বিশ্রামের শেড এবং সুউচ্চ ওয়াচটাওয়ার পর্যটকদের মুগ্ধ করে। সকালে এখান থেকে দেখা যায় উপত্যকা জুড়ে জমে থাকা মেঘের শুভ্র সমুদ্র, যার ওপর সূর্যের প্রথম আলো পড়লে এক অপার্থিব রূপ ধারণ করে। পাহাড়ের গা বেয়ে চলা শীতল বাতাস ও দূর-দিগন্তের সবুজ পাহাড়ের দৃশ্য মনকে প্রশান্তিতে ভরিয়ে দেয়। বিকেলে সূর্যাস্ত দেখা এবং পাহাড়ি প্রকৃতির রূপ ক্যামেরাবন্দি করার জন্য আলুটিলা পর্যটন কেন্দ্র এক অনবদ্য গন্তব্য।",
            "locationEn": "Matiranga, Khagrachhari",
            "locationBn": "মাটিরাঙ্গা, খাগড়াছড়ি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Alutila%20Tourist%20Center%2C%20Matiranga%2C%20Khagrachhari"
        },
        {
            "id": 2,
            "nameEn": "Tareng viewpoint",
            "nameBn": "তারেং হিলটপ ভিউপয়েন্ট",
            "categoryEn": "Highland Observation Peak & Sunset Deck",
            "categoryBn": "সুউচ্চ পাহাড়ি চূড়া ও সূর্যাস্ত দর্শন ডেক",
            "descEn": "Tareng Viewpoint in Khagrachhari Sadar is an awe-inspiring scenic viewpoint perched atop a steep peak overlooking the surrounding valleys. Celebrated for offering an uninterrupted 360-degree vista of undulating mountain ranges, the viewpoint allows travelers to watch clouds sweep rapidly across forested summits. Dedicated wooden viewing decks, cozy open-air coffee kiosks, and camping zones make Tareng a favorite hangout for younger travelers and nature photographers. Sunset at Tareng is nothing short of magical, with deep oranges, purples, and crimsons washing over the distant horizons. It is renowned as one of the most romantic and visually stunning hill points in southeastern Bangladesh.",
            "descBn": "খাগড়াছড়ি সদর উপজেলার মায়াবী তারেং পাহাড়ের চূড়া পর্যটকদের কাছে অত্যন্ত জনপ্রিয় এক রোমাঞ্চকর ভিউপয়েন্ট। এখান থেকে চারপাশের ৩৬০ ডিগ্রি কোণে সবুজ পাহাড়ের অনন্ত ঢেউ এবং মেঘের উড়ে চলা অবলোকন করা যায়। পাহাড়ের শীর্ষে স্থাপিত আধুনিক কাঠের ডেক ও কফি কর্নারে বসে শীতল হাওয়া উপভোগ করা এক স্বর্গীয় অনুভূতি এনে দেয়। বিশেষ করে গোধূলিবেলায় যখন পাহাড়ের ওপারে সূর্য অস্ত যায়, তখন পুরো আকাশ রঙিন আলোর খেলায় মেতে ওঠে। মুক্ত বাতাস, মেঘের ছোঁয়া এবং নীরব প্রকৃতির মাঝে সময় কাটাতে তারেং এক অপূর্ব পাহাড়ি ঠিকানা।",
            "locationEn": "Khagrachhari Sadar",
            "locationBn": "খাগড়াছড়ি সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Tareng%20viewpoint%2C%20Khagrachhari%20Sadar"
        },
        {
            "id": 3,
            "nameEn": "Dighinala countryside",
            "nameBn": "দীঘিনালা পাহাড়ি উপত্যকা",
            "categoryEn": "Pristine Mountain Valleys & Tribal Hamlets",
            "categoryBn": "মনোরম পাহাড়ি উপত্যকা ও ঐতিহ্যবাহী গ্রাম",
            "descEn": "The Dighinala countryside offers travelers a tranquil journey through the peaceful agricultural rhythm of highland indigenous life. Winding roads wind past vibrant green step-farming paddy terraces, lush rubber plantations, and crystal-clear mountain streams crossed by swaying bamboo bridges. Traditional stilt houses (machang) constructed from seasoned bamboo and thatch dot the hillsides, home to hospitable Chakma and Tripura farming families. Visitors can purchase sweet hill pineapples, wild honey, and hand-woven tribal textiles at bustling local rural bazaars. Exploring Dighinala captures the untamed soul and serene lifestyle of the Chittagong Hill Tracts.",
            "descBn": "দীঘিনালার গ্রামীণ ভূদৃশ্য পাহাড়ি প্রকৃতি ও আদিবাসী সরল জীবনের এক অপূর্ব রূপ তুলে ধরে। পাহাড়ের ঢালে ধাপে ধাপে চাষ করা সবুজ জুম ক্ষেত, রবার বাগান এবং পাহাড়ি ছড়ার স্বচ্ছ জলপ্রবাহ চোখ জুড়িয়ে দেয়। পাহাড়ের ওপর বাঁশ ও ছনে নির্মিত ঐতিহ্যবাহী 'মাচাং ঘর' এবং আদিবাসী জনগোষ্ঠীর সহজ-সরল জীবনযাত্রা পর্যটকদের মুগ্ধ করে। স্থানীয় পাহাড়ি হাটে মিলবে পাহাড়ি আনারস, কলা, বুনো মধু এবং হাতে বোনা বর্ণিল থামি ও চাদর। শহরের কোলাহল ছেড়ে প্রকৃতির নিবিড় সান্নিধ্য পেতে দীঘিনালার পাহাড়ি পথ এক অনবদ্য ভ্রমণ অভিজ্ঞতা।",
            "locationEn": "Dighinala, Khagrachhari",
            "locationBn": "দীঘিনালা, খাগড়াছড়ি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Dighinala%20countryside%2C%20Dighinala%2C%20Khagrachhari"
        },
        {
            "id": 4,
            "nameEn": "Chengi Riverbank",
            "nameBn": "চেঙ্গী নদীতীর ও উপত্যকা",
            "categoryEn": "Scenic Mountain River & Valley Corridor",
            "categoryBn": "পাহাড়ি খরস্রোতা চেঙ্গী নদী ও বালুকাবেলা",
            "descEn": "The Chengi Riverbank is the lifeline waterway of Khagrachhari, carving a scenic, fertile valley between towering mountain ranges. Flowing south toward Kaptai Lake, the river's clear waters rush gently over gravel beds, shaded by weeping willows and bamboo groves. Local indigenous fishermen navigate the shallow rapids in slim dugout wooden canoes, while colorful hanging footbridges provide scenic river-crossing viewpoints. During dry seasons, wide pebble sandbars invite visitors for riverside walks and serene photography against dramatic mountain silhouettes. The river corridor epitomizes the natural poetry and life-giving energy of the hill terrain.",
            "descBn": "খাগড়াছড়ির প্রধান নদী চেঙ্গীর তীর পাহাড়ের কোল ঘেঁষে বয়ে যাওয়া এক নয়নাভিরাম প্রাকৃতিক সৌন্দর্যভূমি। দুই পাশে সবুজ পাহাড়ের সারি এবং মাঝখান দিয়ে বয়ে চলা চেঙ্গী নদীর স্বচ্ছ জলধারা ভ্রমণকারীদের মুগ্ধ করে। নদীর ওপর টানানো দীর্ঘ ঝুলন্ত সেতুগুলো থেকে চারপাশের দৃশ্য দেখার মতো সুন্দর। শীতকালে নদীর দুই পাড়ে জেগে ওঠে সাদা বালুর চর ও নুড়িপাথরের মেলা, যেখানে বসে পাহাড়ি নদীর কলতান শোনা এক অনাবিল প্রশান্তি দেয়। স্থানীয় পাহাড়ি শিশুদের জলকেলি ও নৌকার চলাচল এই নদীর সৌন্দর্যকে আরও জীবন্ত করে তোলে।",
            "locationEn": "Khagrachhari Sadar",
            "locationBn": "খাগড়াছড়ি সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Chengi%20Riverbank%2C%20Khagrachhari%20Sadar"
        },
        {
            "id": 5,
            "nameEn": "Horticulture Heritage Park",
            "nameBn": "হর্টিকালচার হেরিটেজ পার্ক",
            "categoryEn": "Highland Botanical Garden & Family Lake Park",
            "categoryBn": "পাহাড়ি উদ্ভিদ উদ্যান ও বিনোদন পার্ক",
            "descEn": "The Horticulture Heritage Park, established by the district administration in Khagrachhari town, is a premier botanical garden and family recreational destination. Spread over 22 acres of undulating hillocks, the park features fruit orchards, indigenous timber tree sanctuaries, a large central lake with pedalo boat rentals, and scenic hanging pedestrian bridges. Well-maintained stone footpaths, hill observation pavilions, children's amusement zones, and waterside dining cottages provide delightful amenities for visitors of all ages. Seasonal flower blooms carpet the slopes in winter, creating a paradise for nature walks and family photography. It is the premier green sanctuary for leisurely relaxation within Khagrachhari town.",
            "descBn": "খাগড়াছড়ি জেলা শহরের কেন্দ্রস্থলে প্রায় ২২ একর উঁচু-নিচু পাহাড়ি টিলা জুড়ে গড়ে উঠেছে নয়নাভিরাম হর্টিকালচার হেরিটেজ পার্ক। এই পার্কে রয়েছে বিভিন্ন প্রজাতির পাহাড়ি ফলদ ও বনজ উদ্ভিদের বাগান, ঝুলন্ত সেতু, সুদৃশ্য কৃত্রিম লেক এবং প্যাডেল বোটিংয়ের ব্যবস্থা। পাহাড়ের ঢালে সুন্দরভাবে সাজানো ফুলের বাগান ও হাঁটার পথ পরিবারের সবাইকে নিয়ে আনন্দময় সময় কাটানোর জন্য আদর্শ। শিশুদের খেলার জন্য বিভিন্ন রাইড এবং লেকের পাড়ে বিশ্রামের জন্য রয়েছে নান্দনিক কটেজ। পাহাড়ি পরিবেশে নিরিবিলি বিনোদনের জন্য এই পার্কটি অত্যন্ত চমৎকার।",
            "locationEn": "Khagrachhari town",
            "locationBn": "খাগড়াছড়ি শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Horticulture%20Heritage%20Park%2C%20Khagrachhari%20town"
        }
    ]
}

data_dict = {
    "narail": narail,
    "naogaon": naogaon,
    "satkhira": satkhira,
    "khagrachhari": khagrachhari
}

for slug, data in data_dict.items():
    fp = f"scripts/data_districts_17/{slug}.py"
    with open(fp, "w", encoding="utf-8") as f:
        f.write(f"# -*- coding: utf-8 -*-\nDISTRICT_DATA = {json.dumps(data, ensure_ascii=False, indent=4)}\n")
    print(f"Wrote {fp}")

print("Batch 2 to 5 complete!")
