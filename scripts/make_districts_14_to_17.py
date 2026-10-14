# -*- coding: utf-8 -*-
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
os.makedirs('scripts/data_districts_17', exist_ok=True)

# 14. LALMONIRHAT
lalmonirhat = {
    "slug": "lalmonirhat",
    "en": "Lalmonirhat",
    "bn": "লালমনিরহাট",
    "hero_title_en": "Lalmonirhat The Teesta Barrage & Tin Bigha Heritage",
    "hero_title_bn": "লালমনিরহাটের তিস্তা ব্যারেজ ও তিন বিঘা করিডোর",
    "hero_sub_en": "Mighty Teesta River vistas, ancient Harano Mosque, and historic Kakina heritage.",
    "hero_sub_bn": "প্রমত্তা তিস্তার জলধারা, সপ্তম শতকের প্রাচীন হারানো মসজিদ ও কাকিনার ঐতিহাসিক ঐতিহ্য।",
    "tagline_en": "A northern frontier district steeped in railway history and borderland heritage, celebrated for the colossal Teesta Barrage, the historic enclave corridor of Tin Bigha, and the ancient Islamic monument of Harano Mosque.",
    "tagline_bn": "উত্তরবঙ্গের তিস্তা বিধৌত সীমান্ত জেলা, যা তিস্তা ব্যারেজের অপার জলরাশি, ঐতিহাসিক তিন বিঘা করিডোর এবং প্রাচীন হারানো মসজিদের অমূল্য ঐতিহ্যের জন্য প্রসিদ্ধ।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/lalmonirhat/carousel-1.webp",
            "titleEn": "Teesta Barrage Massive River Irrigation Project",
            "titleBn": "তিস্তা ব্যারেজ সুবিশাল জলকপাট ও বাঁধ",
            "subtitleEn": "Bangladesh's largest river barrage controlling the swift northern currents of the Teesta River",
            "subtitleBn": "তিস্তা নদীর বুকে নির্মিত দেশের সর্ববৃহৎ সেচ প্রকল্প ও পর্যটকদের অন্যতম প্রিয় দর্শনীয় স্থান"
        },
        {
            "id": 2,
            "image": "images/districts/lalmonirhat/carousel-2.webp",
            "titleEn": "Tin Bigha Corridor Historical Border Gateway",
            "titleBn": "তিন বিঘা করিডোর ঐতিহাসিক ছিটমহল সংযোগ",
            "subtitleEn": "Historic sovereign land corridor connecting Dahagram-Angarpota enclave with mainland Bangladesh",
            "subtitleBn": "দহগ্রাম-আঙ্গরপোতার মানুষকে মূল ভূখণ্ডের সাথে যুক্তকারী ঐতিহাসিক সীমান্ত করিডোর"
        },
        {
            "id": 3,
            "image": "images/districts/lalmonirhat/carousel-3.webp",
            "titleEn": "Kakina Zamindar Bari Ancient Feudal Estate",
            "titleBn": "কাকিনা জমিদার বাড়ি ও রাজকীয় ধ্বংসাবশেষ",
            "subtitleEn": "Historic palace estate in Kaliganj showcasing royal gateways, ponds, and literary lore",
            "subtitleBn": "কালীগঞ্জের কাকিনায় অবস্থিত ব্রিটিশ আমলের প্রভাবশালী জমিদারদের স্মৃতিবিজড়িত প্রাসাদ"
        },
        {
            "id": 4,
            "image": "images/districts/lalmonirhat/carousel-4.webp",
            "titleEn": "Harano Mosque Ancient Hijri Relic",
            "titleBn": "হারানো মসজিদ প্রাচীন ঐতিহাসিক নিদর্শন",
            "subtitleEn": "One of the oldest Islamic archaeological ruins in South Asia dating back to early Hijri centuries",
            "subtitleBn": "দক্ষিণ এশিয়ার অন্যতম প্রাচীন ইসলামিক পুরাকীর্তি যা ৬৯ হিজরি সালের বলে ইতিহাসবিদদের মত"
        },
        {
            "id": 5,
            "image": "images/districts/lalmonirhat/carousel-5.webp",
            "titleEn": "Burimari Land Port International Frontier",
            "titleBn": "বুড়িমারী স্থলবন্দর আন্তর্জাতিক সীমান্ত কেন্দ্র",
            "subtitleEn": "Bustling international land crossing facilitating transit to Bhutan, Nepal, and northern India",
            "subtitleBn": "ভারত ও ভুটানের সাথে আন্তর্জাতিক বাণিজ্য ও যাত্রী যাতায়াতের ব্যস্ততম স্থলবন্দর"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Kakina Zamindar Bari",
            "nameBn": "কাকিনা জমিদার বাড়ি",
            "categoryEn": "Historic Feudal Palace & Cultural Estate",
            "categoryBn": "ঐতিহাসিক জমিদার প্রাসাদ ও সাংস্কৃতিক কেন্দ্র",
            "descEn": "Kakina Zamindar Bari, situated in Kaliganj Upazila of Lalmonirhat, was the seat of the influential Kakina zamindars whose lineage dates back to the reign of Mughal Emperor Jahangir. During the British colonial era, Zamindar Raja Mahima Ranjan Roy Chowdhuri modernized the estate, establishing a renowned printing press, an extensive library, and premier educational institutions. Today, the expansive estate retains its majestic entrance gate, remnants of royal residential quarters, classical columns, and sprawling palace tanks. The complex stands as a powerful testament to the literary patronage, aristocratic architectural grandeur, and socio-economic influence of northern Bengal's zamindars.",
            "descBn": "লালমনিরহাটের কালীগঞ্জ উপজেলায় অবস্থিত কাকিনা জমিদার বাড়ি মোঘল ও ব্রিটিশ আমলের এক সুবিখ্যাত ঐতিহাসিক রাজপ্রাসাদ। রাজা মহিমারঞ্জন রায় চৌধুরীর সময়ে এই জমিদারির ব্যাপক সমৃদ্ধি ঘটে এবং তিনি এখানে সমৃদ্ধ লাইব্রেরি, ছাপাখানা ও শিক্ষা প্রতিষ্ঠান প্রতিষ্ঠা করেছিলেন। বর্তমানে প্রাসাদের রাজকীয় সিংহদ্বার, নাটমন্দির, প্রাচীন দিঘি ও ইট-সুরকির অলংকৃত দেয়াল অতীত সমৃদ্ধির সাক্ষ্য বহন করে। উত্তরবঙ্গের সাহিত্যচর্চা ও জমিদারি ঐতিহ্যের অন্যতম গুরুত্বপূর্ণ প্রত্নতাত্ত্বিক নিদর্শন হিসেবে এটি সুপরিচিত।",
            "locationEn": "Kakina, Kaliganj",
            "locationBn": "কাকিনা, কালীগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kakina%20Zamindar%20Bari%2C%20Kakina%2C%20Kaliganj"
        },
        {
            "id": 2,
            "nameEn": "Nidaria Mosque",
            "nameBn": "নিদারিয়া মসজিদ",
            "categoryEn": "Historic Mughal Era Single-Dome Mosque",
            "categoryBn": "মোঘল আমলের ঐতিহাসিক এক গম্বুজ মসজিদ",
            "descEn": "Nidaria Mosque, located in Panchgram under Lalmonirhat Sadar Upazila, is a celebrated historical mosque erected during the late Mughal period around 1176 Bengal Era (circa 1769 CE) by Subedar Mansur Khan. Built on an elevated plinth with thick terracotta walls, massive octagonal corner minarets, and a large hemispherical central dome, the mosque is renowned for its acoustic perfection and structural elegance. Folk legend holds that the mosque received its name ('Nidaria') because prayers here are traditionally answered without denial. The historic sanctuary continues to serve as an active center of worship and remains a treasured landmark of regional medieval architecture.",
            "descBn": "লালমনিরহাট সদর উপজেলার পঞ্চগ্রাম ইউনিয়নে অবস্থিত নিদারিয়া মসজিদ মোঘল স্থাপত্যের একটি মনোহর নিদর্শন। আনুমানিক ১১৭৬ বঙ্গাব্দে (১৭৬৯ খ্রিষ্টাব্দ) সুবেদার মনসুর খান এই ঐতিহাসিক এক গম্বুজবিশিষ্ট মসজিদটি নির্মাণ করেন। পুরু চুন-সুরকির প্রাচীর, চার কোণে অষ্টভুজাকৃতির মিনার এবং বিশালাকার গম্বুজ বিশিষ্ট মসজিদটির চারপাশের পরিবেশ অত্যন্ত শান্ত ও সুনিবিড়। জনশ্রুতি রয়েছে, এখানে নিষ্ঠাভরে মানত করলে তা বিফল হয় না বলেই এর নাম নিদারিয়া মসজিদ। স্থানীয় ধর্মপ্রাণ মানুষ ও ভ্রমণপিপাসুদের কাছে এটি এক ঐতিহাসিক পুণ্যভূমি।",
            "locationEn": "Panchgram, Lalmonirhat Sadar",
            "locationBn": "পঞ্চগ্রাম, লালমনিরহাট সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Nidaria%20Mosque%2C%20Panchgram%2C%20Lalmonirhat%20Sadar"
        },
        {
            "id": 3,
            "nameEn": "Harano Mosque",
            "nameBn": "হারানো মসজিদ (৬৯ হিজরির মসজিদ)",
            "categoryEn": "Ancient Archaeological Islamic Ruins",
            "categoryBn": "প্রাচীনতম ইসলামিক প্রত্নতাত্ত্বিক নিদর্শন",
            "descEn": "Harano Mosque (literally 'The Lost Mosque'), also known as the 69 Hijri Mosque of Ramdas village, is one of the most astonishing archaeological discoveries in South Asia. Excavated in 1986 beneath an overgrown earthen mound locally known as Majher Bhita, the site revealed an ancient stone inscription bearing the date 69 Hijri (circa 688 CE), suggesting maritime Arab trade routes reached northern Bengal during the era of the Prophet's companions. The excavated foundations feature hand-molded bricks, floral terracotta motifs, and early Islamic architectural planning. The discovery has attracted global archaeological attention, cementing Lalmonirhat's place on early Islamic historical maps.",
            "descBn": "লালমনিরহাট সদর উপজেলার রামদাস গ্রামে ১৯৮৬ সালে স্থানীয় মাটির ঢিবি খননের সময় আবিষ্কৃত হয় সুপ্রাচীন হারানো মসজিদ। সেখানে প্রাপ্ত প্রাচীন পাথরের শিলালিপিতে আরবিতে '৬৯ হিজরি' (আনুমানিক ৬৮৮ খ্রিষ্টাব্দ) উৎকীর্ণ পাওয়া যায়, যা নির্দেশ করে সাহাবিদের যুগেই হয়তো এই অঞ্চলে ইসলামের আলোকবর্তিকা পৌঁছেছিল। পোড়ামাটির কারুকাজময় ইট ও প্রাচীন ভিত্তিভূমি সমন্বিত এই প্রত্নতাত্ত্বিক আবিষ্কার দক্ষিণ এশিয়ার প্রাচীনতম মুসলিম ঐতিহ্যের এক অবিশ্বাস্য বিস্ময় হিসেবে আন্তর্জাতিকভাবে স্বীকৃতি লাভ করেছে।",
            "locationEn": "Lalmonirhat district; verify locality",
            "locationBn": "রামদাস, লালমনিরহাট",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Harano%20Mosque%2C%20Lalmonirhat%20district%3B%20verify%20locality"
        },
        {
            "id": 4,
            "nameEn": "Sheikh Fazlul Karim's house and grave",
            "nameBn": "কবি শেখ ফজলল করিমের বাড়ি ও মাজার",
            "categoryEn": "Literary Memorial & Heritage Homestead",
            "categoryBn": "সাহিত্যিকের স্মৃতিবিজড়িত বাস্তুভিটা ও সমাধিসৌধ",
            "descEn": "The homestead and final resting place of celebrated poet and philosopher Sheikh Fazlul Karim (1882–1936) is located in Kakina under Kaliganj Upazila. Fazlul Karim was a pioneering progressive Bengali poet whose verses, notably 'Kothai shorgo, kothai norok' ('Where is heaven, where is hell, who says it is far away?'), are etched into the moral conscience of Bengali literature. His peaceful homestead retains the preserved family cemetery, memorial plaques, and lush fruit orchards where the poet penned literary treatises, magazines, and moral poetry. Visitors and literature lovers from across Bangladesh visit the sanctuary to pay homage to this humanist intellectual icon.",
            "descBn": "কালীগঞ্জ উপজেলার কাকিনায় অবস্থিত মানবতাবাদী অমর কবি শেখ ফজলল করিমের (১৮৮২-১৯৩৬) স্মৃতিবিজড়িত বসতভিটা ও সমাধিসৌধ। 'কোথায় স্বর্গ কোথায় নরক, কে বলে তা বহুদূর? মানুষের মাঝে স্বর্গ নরক মানুষেতে সুরাসুর'— তাঁর এই কালজয়ী নীতি কবিতার চরণ বাঙালির মুখে মুখে ফেরে। শ্যামল বৃক্ষরাজিশোভিত শান্ত এই প্রাঙ্গণে কবির সমাধি, স্মৃতিফলক এবং তাঁর রচিত সাহিত্যকর্মের নিদর্শন সংরক্ষিত রয়েছে। বাংলা সাহিত্যের এই মহান মনীষীর প্রতি শ্রদ্ধা জানাতে দেশ-বিদেশের বহু সাহিত্যপ্রেমী এখানে আগমন করেন।",
            "locationEn": "Kakina area, Kaliganj",
            "locationBn": "কাকিনা এলাকা, কালীগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Sheikh%20Fazlul%20Karim%27s%20house%20and%20grave%2C%20Kakina%20area%2C%20Kaliganj"
        },
        {
            "id": 5,
            "nameEn": "World War II airfield site",
            "nameBn": "দ্বিতীয় বিশ্বযুদ্ধের বিমানঘাঁটি সাইট",
            "categoryEn": "WWII Military Aviation Heritage Site",
            "categoryBn": "দ্বিতীয় বিশ্বযুদ্ধের ঐতিহাসিক সামরিক বিমানঘাঁটি",
            "descEn": "The Lalmonirhat World War II Airfield is an enormous historical aviation site established in the early 1940s by the British Royal Air Force and the United States Army Air Forces. Covering over 1,100 acres, it served as a vital Allied strategic air hub during the Burma Campaign, dispatching long-range bombers and transport planes over the Himalayan 'Hump' into China. The site still features massive concrete runways, underground fuel depots, aircraft parking aprons, and taxiways. In recent years, the Government of Bangladesh has designated part of this sprawling historic airfield for the Bangabandhu Sheikh Mujibur Rahman Aviation and Aerospace University (BSMRAAU), breathing futuristic academic life into wartime history.",
            "descBn": "১৯৪০-এর দশকে দ্বিতীয় বিশ্বযুদ্ধের সময় মিত্রবাহিনী (ব্রিটিশ রাজকীয় বিমানবাহিনী ও মার্কিন বিমানবাহিনী) লালমনিরহাটে এশিয়ার অন্যতম বৃহত্তম এই সামরিক বিমানঘাঁটি নির্মাণ করে। বার্মা ফ্রন্ট ও চীনে রসদ ও বোমারু বিমান প্রেরণের অন্যতম প্রধান কৌশলগত কেন্দ্র ছিল এটি। সুবিশাল রানওয়ে, বিমানের হ্যাঙ্গার ও যোগাযোগ ব্যবস্থার ঐতিহাসিক চিহ্ন এখনও এখানে দৃশ্যমান। বর্তমানে এই ঐতিহাসিক বিমানঘাঁটির প্রাঙ্গণেই প্রতিষ্ঠিত হয়েছে বঙ্গবন্ধু শেখ মুজিবুর রহমান এভিয়েশন অ্যান্ড অ্যারোস্পেস বিশ্ববিদ্যালয়, যা অতীত ও আধুনিক প্রযুক্তির এক অনন্য মিলনস্থল।",
            "locationEn": "Lalmonirhat town area",
            "locationBn": "লালমনিরহাট শহর এলাকা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=World%20War%20II%20airfield%20site%2C%20Lalmonirhat%20town%20area"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Teesta Barrage",
            "nameBn": "তিস্তা ব্যারেজ প্রকল্প",
            "categoryEn": "Mega Hydraulic Engineering Landmark",
            "categoryBn": "দেশের বৃহত্তম জলসেচ ও বাঁধ প্রকল্প",
            "descEn": "The Teesta Barrage, located at Dalia in Hatibandha Upazila of Lalmonirhat, is Bangladesh's largest river water management and irrigation project. Inaugurated in 1990 on the transboundary Teesta River, the 615-meter-long barrage features 44 massive sluice gates and 8 silt excluder bays designed to irrigate hundreds of thousands of hectares across northern agricultural districts. The bridge across the barrage offers spectacular panoramic views of raging turquoise river currents, vast sandbars, and distant mountain foothills. The scenic water reservoir, landscaped embankments, and cool river breeze make it the premier tourist destination in the northern division.",
            "descBn": "লালমনিরহাটের হাতিবান্ধা উপজেলার ডালিয়ায় তিস্তা নদীর বুকে নির্মিত তিস্তা ব্যারেজ বাংলাদেশের সর্ববৃহৎ নদী নিয়ন্ত্রণ ও সেচ প্রকল্প। ১৯৯০ সালে উদ্বোধন হওয়া ৬১৫ মিটার দীর্ঘ এই ব্যারেজে রয়েছে ৪৪টি জলকপাট ও বিশাল সেচ খাল। ব্যারেজের ওপর দাঁড়ালে একদিকে তিস্তার জলরাশির গর্জন এবং অন্যদিকে দিগন্তবিস্তৃত বালুচর ও নদীর শান্ত রূপ চোখ জুড়িয়ে দেয়। ব্যারেজ সংলগ্ন বাঁধ, মনোরম বাগান ও নদীর হিমশীতল বাতাস পর্যটকদের জন্য এক অনাবিল আনন্দ ও প্রশান্তি বয়ে আনে।",
            "locationEn": "Dalia, Hatibandha, Lalmonirhat",
            "locationBn": "ডালিয়া, হাতিবান্ধা, লালমনিরহাট",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Teesta%20Barrage%2C%20Dalia%2C%20Hatibandha%2C%20Lalmonirhat"
        },
        {
            "id": 2,
            "nameEn": "Teesta Riverbank",
            "nameBn": "তিস্তা নদী তীর ও চরভূমি",
            "categoryEn": "Scenic Riverine Landscape & Sandbars",
            "categoryBn": "মনোরম নদী তীরবর্তী বালুচর ও সূর্যাস্ত",
            "descEn": "The riverbanks and wide alluvial char islands of the Teesta River spanning Hatibandha, Kaliganj, and Sadar offer some of Bangladesh's most dramatic open-sky landscapes. In the dry season, the braided river flows in shimmering azure channels across vast golden sandbanks carpeted in wild white kashful blooms. Visitors take wooden country boat cruises along the tranquil river stretches, watch migratory river terns and waterfowl, and experience golden sunsets reflecting across the water surface. The peaceful riverside ambiance offers a tranquil escape into pure rural serenity and riverine charm.",
            "descBn": "হাতিবান্ধা ও সংলগ্ন অঞ্চলে তিস্তা নদীর তীরবর্তী বিস্তৃত বালুচর ও চরাঞ্চল প্রকৃতির এক অপরূপ দৃশ্য উপহার দেয়। হেমন্ত ও শীতের মৌসুমে তিস্তার জলধারা শান্ত হয়ে নীল স্ফটিকের মতো রূপ নেয় এবং নদীর তীরে ফোটে সাদা কাশফুল। স্থানীয় নৌকায় করে চরে ঘুরে বেড়ানো, অতিথি পাখির কলকাকলি শোনা এবং সূর্যাস্তের রক্তিম আভা নদীর জলে প্রতিফলিত হতে দেখা পর্যটকদের বিমোহিত করে। নদীর মৃদুমন্দ হাওয়া ও শান্ত গ্রামীণ পরিবেশ মনকে করে তোলে স্নিগ্ধ ও সতেজ।",
            "locationEn": "Hatibandha and surrounding areas",
            "locationBn": "হাতিবান্ধা ও সংলগ্ন নদী তীর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Teesta%20Riverbank%2C%20Hatibandha%20and%20surrounding%20areas"
        },
        {
            "id": 3,
            "nameEn": "Burimari Land Port",
            "nameBn": "বুড়িমারী স্থলবন্দর",
            "categoryEn": "International Trade Gateway & Border Port",
            "categoryBn": "আন্তর্জাতিক সীমান্ত বন্দর ও বাণিজ্য কেন্দ্র",
            "descEn": "Burimari Land Port, situated at the northern border extremity in Patgram Upazila, is one of Bangladesh's most vital international land transit hubs. Bordering Changrabandha in Cooch Behar (West Bengal, India), this lively port handles extensive cargo traffic, notably importing crushed boulder stones from Bhutan and transporting agricultural and consumer goods across South Asia. The port compound buzzes with colorful multi-axle freight trucks, customs terminals, and international immigration desks. Travelers passing through on trips to Bhutan and the Himalayas find Burimari an intriguing focal point of cross-border commerce.",
            "descBn": "লালমনিরহাটের পাটগ্রাম উপজেলার সীমান্তে অবস্থিত বুড়িমারী স্থলবন্দর বাংলাদেশের অন্যতম গুরুত্বপূর্ণ আন্তর্জাতিক বাণিজ্য পথ। ভারতের কোচবিহারের চ্যাংড়াবান্ধা সীমান্তের মুখোমুখি এই বন্দরটি দিয়ে ভুটান থেকে উচ্চমানের বোল্ডার পাথর এবং ভারত থেকে বিভিন্ন পণ্য আমদানি করা হয়। শত শত মালবাহী ট্রাক, কাস্টমস কার্যালয় এবং ইমিগ্রেশন টার্মিনালের ব্যস্ত কর্মচাঞ্চল্য একে একটি গতিশীল বন্দরে রূপ দিয়েছে। ভারত ও ভুটান ভ্রমণকারী পর্যটকদের জন্য এটি এক অত্যন্ত সুবিধাজনক ও দৃষ্টিনন্দন প্রবেশদ্বার।",
            "locationEn": "Patgram, Lalmonirhat",
            "locationBn": "পাটগ্রাম, লালমনিরহাট",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Burimari%20Land%20Port%2C%20Patgram%2C%20Lalmonirhat"
        },
        {
            "id": 4,
            "nameEn": "Dahagram–Angarpota and Tin Bigha Corridor",
            "nameBn": "দহগ্রাম-আঙ্গরপোতা ও তিন বিঘা করিডোর",
            "categoryEn": "Historic Sovereign Enclave & Border Corridor",
            "categoryBn": "সার্বভৌম ছিটমহল ও ঐতিহাসিক করিডোর",
            "descEn": "The Dahagram–Angarpota enclave and the connecting Tin Bigha Corridor in Patgram represent a profound chapter in the geopolitical and human history of the Indian subcontinent. Once isolated enclaves surrounded entirely by Indian territory, Dahagram and Angarpota were permanently connected to Bangladesh via the Tin Bigha Corridor, leased in perpetuity following historic bilateral treaties. Today, the corridor is open 24 hours a day under the surveillance of the Border Guard Bangladesh (BGB) and India's BSF. Visitors can traverse this symbolic corridor, visit the thriving sovereign community of Dahagram, and witness the enduring triumph of cross-border diplomacy.",
            "descBn": "পাটগ্রাম উপজেলার দহগ্রাম-আঙ্গরপোতা ছিটমহল এবং সংযোগকারী 'তিন বিঘা করিডোর' উপমহাদেশের ভূ-রাজনৈতিক ইতিহাসের এক অনন্য দলিল। চারদিকে ভারতীয় ভূখণ্ড দিয়ে ঘেরা থাকলেও ২০১১ সালে স্থায়ীভাবে ২৪ ঘণ্টা করিডোর উন্মুক্ত করার পর এই ছিটমহলবাসী মুক্ত জীবনের স্বাদ লাভ করেন। বিজিবি ও বিএসএফের পাহারাধীন এই ঐতিহাসিক করিডোর অতিক্রম করে দহগ্রামের গ্রামীণ জীবনযাত্রা, হাসপাতাল ও বিদ্যালয় প্রত্যক্ষ করা যে কোনো দেশপ্রেমিক পর্যটকের জন্য এক অবিস্মরণীয় অনুভূতি।",
            "locationEn": "Patgram; check entry rules",
            "locationBn": "পাটগ্রাম সীমান্ত এলাকা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Dahagram%E2%80%93Angarpota%20and%20Tin%20Bigha%20Corridor%2C%20Patgram%3B%20check%20entry%20rules"
        },
        {
            "id": 5,
            "nameEn": "Kakina countryside",
            "nameBn": "কাকিনার মনোরম গ্রামীণ নিসর্গ",
            "categoryEn": "Rural Pastoral Landscapes & Waterbodies",
            "categoryBn": "সবুজ ধানক্ষেত, দীঘি ও শান্ত গ্রাম",
            "descEn": "The countryside surrounding Kakina in Kaliganj Upazila encapsulates the timeless pastoral elegance of northern Bangladesh. Characterized by expansive green paddy terraces, ancient royal ponds, winding canopy roads flanked by towering mahogany trees, and tranquil rural hamlets, this area offers a refreshing breath of fresh air. Visitors enjoy leisurely country walks, cycling through scenic farm lanes, sampling fresh seasonal fruits, and experiencing the warm hospitality of local farming communities who have lived in harmony with the historic land for generations.",
            "descBn": "কালীগঞ্জ উপজেলার কাকিনা ও আশপাশের গ্রামীণ অঞ্চল যেন শান্ত নিসর্গের এক জীবন্ত ক্যানভাস। সুপ্রাচীন জমিদারদের খনন করা বিশালাকার দীঘি, ছায়াঘেরা মেঠোপথ, দুপাশে সারিবদ্ধ সবুজ মেহগনি ও তালগাছ এবং বিস্তীর্ণ ফসলের মাঠ মনকে জুড়িয়ে দেয়। গ্রামীণ জীবনের শান্ত কোলাহলমুক্ত আবহ, বিশুদ্ধ বাতাস এবং স্থানীয় মানুষের অমায়িক আতিথেয়তা শহুরে জীবনের ক্লান্তি দূর করে এক অপরূপ স্বস্তি এনে দেয়।",
            "locationEn": "Kaliganj, Lalmonirhat",
            "locationBn": "কালীগঞ্জ, লালমনিরহাট",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kakina%20countryside%2C%20Kaliganj%2C%20Lalmonirhat"
        }
    ]
}

# 15. NILPHAMARI
nilphamari = {
    "slug": "nilphamari",
    "en": "Nilphamari",
    "bn": "নীলফামারী",
    "hero_title_en": "Nilphamari The Nilsagar Lake & Saidpur Heritage",
    "hero_title_bn": "নীলফামারীর নীলসাগর দীঘি ও সৈয়দপুরের ঐতিহ্য",
    "hero_sub_en": "Ancient Nilsagar sanctuary, Chini Mosque tiles, and railway workshop heritage.",
    "hero_sub_bn": "ঐতিহাসিক নীলসাগর দিঘি, অপূর্ব কারুকার্যময় চিনি মসজিদ ও রেলওয়ের সমৃদ্ধ ঐতিহ্য।",
    "tagline_en": "A historic northern district famed for the majestic migrant-bird haven of Nilsagar Dighi, the ceramic splendor of Chini Mosque, and Saidpur's legendary British railway engineering heritage.",
    "tagline_bn": "উত্তরবঙ্গের ঐতিহ্যবাহী জেলা, যা অতিথি পাখির অভয়ারণ্য ঐতিহাসিক নীলসাগর, চীনা মাটির টুকরায় খচিত চিনি মসজিদ এবং সৈয়দপুরের সুবিশাল ব্রিটিশ রেলওয়ে কারখানার জন্য খ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/nilphamari/carousel-1.webp",
            "titleEn": "Nilsagar Dighi Legendary Ancient Lake Sanctuary",
            "titleBn": "নীলসাগর দীঘি ঐতিহাসিক হ্রদ ও পাখির অভয়ারণ্য",
            "subtitleEn": "Historic 54-acre freshwater reservoir shaded by towering trees and home to winter migratory birds",
            "subtitleBn": "বিশাল জলরাশি ও সবুজ বনায়ন পরিবেষ্টিত ঐতিহাসিক দিঘি যেখানে শীতকালে হাজারো অতিথি পাখি নামে"
        },
        {
            "id": 2,
            "image": "images/districts/nilphamari/carousel-2.webp",
            "titleEn": "Chini Mosque Exquisite Porcelain Mosaic Architecture",
            "titleBn": "চিনি মসজিদ চীনা মাটির অপরূপ মোজাইক শিল্প",
            "subtitleEn": "Masterpiece of Islamic architecture adorned with thousands of imported porcelain china shards",
            "subtitleBn": "সৈয়দপুরে অবস্থিত রঙিন চীনা মাটির প্লেট ও কাঁচের টুকরোয় খচিত বিশ্ববিখ্যাত স্থাপত্য"
        },
        {
            "id": 3,
            "image": "images/districts/nilphamari/carousel-3.webp",
            "titleEn": "Saidpur Railway Workshop Historic Locomotive Works",
            "titleBn": "সৈয়দপুর রেলওয়ে কারখানা ঐতিহাসিক কারখানা",
            "subtitleEn": "British colonial 1870 railway hub spanning over 110 acres with vintage machinery",
            "subtitleBn": "১৮৭০ সালে ব্রিটিশদের নির্মিত দেশের সর্ববৃহৎ ও প্রাচীনতম রেলওয়ে মেরামত কারখানা"
        },
        {
            "id": 4,
            "image": "images/districts/nilphamari/carousel-4.webp",
            "titleEn": "Nilkuthi Natkhana Historic Indigo Factory Ruins",
            "titleBn": "নীলকুঠি নটখানা ঐতিহাসিক ব্রিটিশ নীল কারখানা",
            "subtitleEn": "Colonial-era indigo processing house ruins echoing the historical peasant struggles",
            "subtitleBn": "ব্রিটিশ নীলকরদের নির্যাতন ও নীলচাষের ইতিহাসের নীরব সাক্ষী নীলফামারীর নটখানা নীলকুঠি"
        },
        {
            "id": 5,
            "image": "images/districts/nilphamari/carousel-5.webp",
            "titleEn": "Teesta Riverbank Dimla Northern Waterways",
            "titleBn": "তিস্তা নদী তীর ডিমলা মনোরম নদীচর",
            "subtitleEn": "Spectacular northern river sweeps and lush alluvial islands near Dimla Upazila",
            "subtitleBn": "ডিমলা উপজেলা সংলগ্ন তিস্তা নদীর অপার জলরাশি ও চরাঞ্চলের নয়নাভিরাম নৈসর্গিক রূপ"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Nilkuthi (Natkhana)",
            "nameBn": "নীলকুঠি (নটখানা)",
            "categoryEn": "British Colonial Indigo Factory Heritage",
            "categoryBn": "ব্রিটিশ আমলের ঐতিহাসিক নীলকুঠি",
            "descEn": "The Nilkuthi at Natkhana in Nilphamari Sadar is an evocative colonial relic from which the district derives its name (originally 'Nil-khamar', meaning indigo farm). Built in the early 19th century by British indigo planters, the fortified brick building served as an administrative quarters, indigo processing facility, and judicial court where farmers were coerced into cultivating indigo over food crops. Although partly weathered by time, the sturdy brick arches, deep foundation walls, and high ceilings remain standing. The monument preserves the memory of the brave peasant uprisings during the historic Nil Bidroha (Indigo Rebellion) that shook British colonial rule.",
            "descBn": "নীলফামারী সদর উপজেলার নটখানায় অবস্থিত প্রাচীন নীলকুঠি ব্রিটিশ উপনিবেশিক শোষণের এক জলজ্যান্ত ঐতিহাসিক সাক্ষী। এই 'নীল-খামার' থেকেই কালক্রমে জেলাটির নাম 'নীলফামারী' হয়েছে। উনবিংশ শতাব্দীর শুরুর দিকে ব্রিটিশ নীলকররা কৃষকদের নীল চাষে বাধ্য করার জন্য এই কুঠি নির্মাণ করেছিল। এর সুদৃঢ় ইটের খিলান, উঁচু ছাদ ও প্রাঙ্গণ সেই সময়ের নীল বিদ্রোহ ও কৃষকদের রক্তক্ষয়ী সংগ্রামের স্মৃতি বহন করে। ইতিহাসপ্রেমী ও গবেষকদের কাছে এটি অত্যন্ত শিক্ষণীয় ও গুরুত্বপূর্ণ একটি ঐতিহাসিক নিদর্শন।",
            "locationEn": "Nilphamari Sadar; verify entrance",
            "locationBn": "নটখানা, নীলফামারী সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Nilkuthi%20%28Natkhana%29%2C%20Nilphamari%20Sadar%3B%20verify%20entrance"
        },
        {
            "id": 2,
            "nameEn": "Binnadighi (King Birat's Dighi)",
            "nameBn": "বিন্নাদীঘি (রাজা বিরাটের দীঘি)",
            "categoryEn": "Ancient Legendary Royal Reservoir",
            "categoryBn": "পৌরাণিক রাজা বিরাটের ঐতিহাসিক দীঘি",
            "descEn": "Binnadighi, also known as the historic Dighi of King Birat, is an enormous freshwater reservoir dating back to the epic mythological period of Mahabharata. According to local archaeological traditions, Raja Birat of the Matsya Kingdom maintained vast herds of royal dairy cattle here and excavated this colossal dighi to water tens of thousands of cows. The waterbody covers over 200 bighas of land and is bounded by towering earthen dykes lined with mature banyan and palm trees. Coins and pottery fragments unearthed around the reservoir attest to deep antiquity, making it an enthralling destination for history and mythology enthusiasts.",
            "descBn": "নীলফামারী জেলায় অবস্থিত বিন্নাদীঘি যা মহাভারতের পৌরাণিক রাজা বিরাটের দীঘি হিসেবে লোকমুখে পরিচিত। জনশ্রুতি মতে, মৎস্য দেশের অধিপতি রাজা বিরাট তাঁর অসংখ্য গাভীকে জলপান করানোর জন্য এই বিশালাকার জলাশয় খনন করেছিলেন। প্রায় ২০০ বিঘা এলাকা জুড়ে বিস্তৃত এই দীঘির চারপাশের সুউচ্চ পাড় ও বিশাল বটবৃক্ষগুলো যেন সুপ্রাচীন কালের সাক্ষ্য দেয়। এই প্রাচীন দীঘি ও এর আশপাশে প্রাপ্ত বিভিন্ন প্রত্নতাত্ত্বিক সামগ্রী ইতিহাসের গবেষক ও পর্যটকদের দারুণভাবে আকর্ষণ করে।",
            "locationEn": "Nilphamari district; verify precise locality",
            "locationBn": "নীলফামারী জেলা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Binnadighi%20%28King%20Birat%27s%20Dighi%29%2C%20Nilphamari%20district%3B%20verify%20precise%20locality"
        },
        {
            "id": 3,
            "nameEn": "Dharmapal Garh ruins",
            "nameBn": "ধর্মপাল গড়ের ধ্বংসাবশেষ",
            "categoryEn": "Ancient Pala Dynasty Fortified Citadel Ruins",
            "categoryBn": "পাল রাজবংশের ঐতিহাসিক দুর্গের ধ্বংসাবশেষ",
            "descEn": "Dharmapal Garh, situated near Jaldhaka Upazila, is the fortified historical citadel of Dharmapala, the great emperor of the imperial Pala Dynasty who ruled Bengal and Bihar during the 8th to 9th centuries CE. Archaeological remains at the site reveal the defensive earthen ramparts, a deep surrounding moat, foundations of palatial royal buildings, and ancient brick structures buried beneath rolling green mounds. Pottery shards, ornamental terracotta fragments, and historical artifacts recovered from the locality demonstrate the urban sophistication of early medieval Bengal. The serene forested ruins offer visitors a tangible connection to Bengal's golden Pala era.",
            "descBn": "জলঢাকা উপজেলার সন্নিকটে অবস্থিত ধর্মপাল গড় পাল রাজবংশের দ্বিতীয় ও সর্বশ্রেষ্ঠ শাসক ধর্মপালের স্মৃতিবিজড়িত এক প্রাচীন দুর্গনগরী। অষ্টম-নবম শতাব্দীতে নির্মিত এই দুর্গের বিশাল মাটির পরিখা, প্রতিরক্ষা প্রাচীর এবং সুপ্রাচীন ইটের ভিত্তিপ্রস্তর এখনও মাটির নিচে ও স্তূপে দৃশ্যমান। খননকালে প্রাপ্ত প্রাচীন পোড়ামাটির ফলক ও মৃৎপাত্র এই অঞ্চলের প্রাচীন সমৃদ্ধ নগরায়নের পরিচয় দেয়। ইতিহাস অনুসন্ধানকারী পর্যটকদের জন্য ধর্মপাল গড়ের এই নিরিবিলি প্রত্নস্থল অত্যন্ত রোমাঞ্চকর।",
            "locationEn": "Nilphamari district; local guidance advised",
            "locationBn": "ধর্মপাল, জলঢাকা, নীলফামারী",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Dharmapal%20Garh%20ruins%2C%20Nilphamari%20district%3B%20local%20guidance%20advised"
        },
        {
            "id": 4,
            "nameEn": "Harishchandra Path",
            "nameBn": "হরিশচন্দ্রের পাঠ",
            "categoryEn": "Historic Mound & Mythological Relic",
            "categoryBn": "পৌরাণিক হরিশচন্দ্রের ঐতিহাসিক পাঠ ও ঢিবি",
            "descEn": "Harishchandra Path is a celebrated ancient archaeological mound and mythological memorial site in Nilphamari district, tied to the benevolent legendary King Harishchandra of Indian epic lore. The elevated mound contains buried brick foundations, antique structural pillars, and historical water tanks that date back over a millennium. Local folklore reveres the place as the scholarly seat and court of justice where King Harishchandra governed with peerless truth and justice. Surrounded by verdant rural orchards, the heritage mound continues to intrigue archaeologists and heritage seekers investigating the pre-Islamic antiquities of northern Bengal.",
            "descBn": "নীলফামারী জেলায় অবস্থিত হরিশচন্দ্রের পাঠ এক সুপ্রাচীন প্রত্নতাত্ত্বিক ঢিবি যা পৌরাণিক সত্যবাদী রাজা হরিশচন্দ্রের নামের সাথে জড়িত। এই ঐতিহাসিক ঢিবির নিচে প্রাচীন যুগের পোড়ামাটির ইট, স্তম্ভের অবশিষ্টাংশ এবং প্রাচীন কূপের সন্ধান পাওয়া যায়। লোকবিশ্বাস অনুসারে এটি ছিল রাজা হরিশচন্দ্রের রাজসভা ও সাধনার পবিত্র পাঠস্থল। সবুজ শ্যামল গ্রামীণ পরিবেশে অবস্থিত এই প্রাচীন প্রত্নস্থল উত্তরবঙ্গের প্রাক-ইসলামিক ইতিহাস ও ঐতিহ্যের এক রহস্যময় ও আকর্ষণীয় কেন্দ্র।",
            "locationEn": "Nilphamari district; verify exact site",
            "locationBn": "নীলফামারী জেলা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Harishchandra%20Path%2C%20Nilphamari%20district%3B%20verify%20exact%20site"
        },
        {
            "id": 5,
            "nameEn": "Nilsagar Dighi",
            "nameBn": "নীলসাগর দীঘি (ঐতিহাসিক বিরাট দীঘি)",
            "categoryEn": "Historic 54-Acre Royal Waterbody",
            "categoryBn": "ঐতিহাসিক ৫৪ একরের বিশালাকার দীঘি",
            "descEn": "Nilsagar Dighi, originally excavated by King Birat in ancient times and formerly known as Birat Dighi, is a sprawling 54-acre freshwater reservoir located at Gorgram under Nilphamari Sadar. In 1979, the historic dighi was revitalized and renamed 'Nilsagar' by the administration, beautifying its perimeter with groves of teak, mahogany, coconut palms, and flowering trees. The crystal-clear lake water reflects the towering canopy and provides an internationally renowned haven for tens of thousands of migratory birds during winter. Its broad paved pathways, historical temples, and tranquil stone ghats make it the premier historical and leisure destination in Nilphamari.",
            "descBn": "নীলফামারী সদর উপজেলার গোড়গ্রাম ইউনিয়নে অবস্থিত নীলসাগর বাংলাদেশের অন্যতম বিখ্যাত ও ঐতিহাসিক বিশাল দিঘি। প্রাচীনকালে রাজা বিরাট কর্তৃক খননকৃত এই দিঘিটি একসময় 'বিরাট দিঘি' নামে পরিচিত ছিল। প্রায় ৫৪ একর এলাকা জুড়ে বিস্তৃত এই জলাশয় ১৯৭৯ সালে সংস্কার করে 'নীলসাগর' নাম দেওয়া হয়। দিঘির চারপাশ ঘিরে গড়ে তোলা হয়েছে মেহগনি, শাল ও নারিকেল গাছের মনোরম অরণ্য। শান্ত স্নিগ্ধ জলরাশি ও মনোরম প্রাকৃতিক পরিবেশের জন্য এটি জেলার প্রধান ঐতিহাসিক আকর্ষণ হিসেবে পর্যটকদের মুগ্ধ করে।",
            "locationEn": "Gorgram, Nilphamari Sadar",
            "locationBn": "গোড়গ্রাম, নীলফামারী সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Nilsagar%20Dighi%2C%20Gorgram%2C%20Nilphamari%20Sadar"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Nilsagar",
            "nameBn": "নীলসাগর পর্যটন কেন্দ্র ও অতিথি পাখির অভয়ারণ্য",
            "categoryEn": "Ecotourism Park & Migratory Bird Sanctuary",
            "categoryBn": "ইকোট্যুরিজম পার্ক ও শীতকালীন পাখির স্বর্গরাজ্য",
            "descEn": "Nilsagar Tourist Park at Gorgram is a pristine ecotourism haven and wildlife sanctuary. During the winter months from November to March, the vast 54-acre lake transforms into an enchanting paradise as thousands of migratory whistling ducks, teals, and waterbirds arrive from Siberia and the Himalayan regions. The district administration has developed comfortable walking promenades, shaded benches, rest houses, and viewing piers along the lake embankment. Families, nature photographers, and picnickers flock here to savor the tranquil lakeside breeze, boat across the calm waters, and witness the golden sunset illuminating the bird-filled lake.",
            "descBn": "গোড়গ্রামের নীলসাগর বর্তমানে একটি আধুনিক ইকোট্যুরিজম ও বিনোদন কেন্দ্র হিসেবে সুপরিচিত। শীত মৌসুমে সুদূর সাইবেরিয়া ও হিমালয় অঞ্চল থেকে হাজার হাজার পরিযায়ী পাখি এসে নীলসাগরের স্বচ্ছ জলে জলকেলি করে, যা এক স্বর্গীয় দৃশ্যের অবতারণা করে। পর্যটকদের সুবিধার জন্য দিঘির পাড়ে পাকা ওয়াকওয়ে, বিশ্রামের শেড, পিকনিক স্পট ও ওয়াচ টাওয়ার তৈরি করা হয়েছে। পরিবারের সদস্যদের নিয়ে নৌভ্রমণ, পাখির কলতান উপভোগ এবং সূর্যাস্তের মনোরম দৃশ্য দেখার জন্য এটি উত্তরবঙ্গের অন্যতম সেরা পর্যটন কেন্দ্র।",
            "locationEn": "Gorgram, Nilphamari Sadar",
            "locationBn": "গোড়গ্রাম, নীলফামারী সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Nilsagar%2C%20Gorgram%2C%20Nilphamari%20Sadar"
        },
        {
            "id": 2,
            "nameEn": "Teesta Riverbank",
            "nameBn": "তিস্তা নদী তীর (ডিমলা)",
            "categoryEn": "Scenic Northern River Landscapes",
            "categoryBn": "ডিমলার নয়নাভিরাম তিস্তা নদী তীর ও চর",
            "descEn": "The Teesta Riverbank in Dimla Upazila offers awe-inspiring vistas of one of northern Bengal's most powerful water arteries. Here, the river expands into expansive braided channels cutting through glittering white sandbars known locally as 'chars'. Visitors can hire local fishermen's wooden boats to cruise between uninhabited islets, photograph majestic river bends, and witness vibrant riverine birdlife including kingfishers and river terns. The cool river winds, vast open skies, and vibrant rural fishing hamlets along the embankment provide an authentic, peaceful countryside getaway.",
            "descBn": "নীলফামারীর ডিমলা উপজেলায় অবস্থিত তিস্তা নদী তীর প্রকৃতির মুক্ত সৌন্দর্য উপভোগের জন্য এক অসাধারণ স্থান। এখানে তিস্তার স্রোতধারা বালুময় চরে বিভক্ত হয়ে একেকটি রূপালী জলরেখায় পরিণত হয়। পর্যটকরা স্থানীয় কাঠের নৌকায় চড়ে চরাঞ্চলে ঘুরতে পারেন, মাছ ধরার দৃশ্য দেখতে পারেন এবং দিগন্তজোড়া নীল আকাশের সাথে নদীর মিলন উপভোগ করতে পারেন। নদীর মুক্ত হাওয়া এবং স্নিগ্ধ নির্জন পরিবেশ যে কোনো প্রকৃতিপ্রেমীর ক্লান্তি দূর করে দেয়।",
            "locationEn": "Dimla and surrounding areas",
            "locationBn": "ডিমলা ও সংলগ্ন তিস্তা চর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Teesta%20Riverbank%2C%20Dimla%20and%20surrounding%20areas"
        },
        {
            "id": 3,
            "nameEn": "Chini Mosque",
            "nameBn": "চিনি মসজিদ (সৈয়দপুর)",
            "categoryEn": "Exquisite Porcelain Mosaic Architectural Marvel",
            "categoryBn": "চীনা মাটির টুকরায় খচিত ঐতিহ্যবাহী মসজিদ",
            "descEn": "The Chini Mosque (also known as the Porcelain Mosque) in Saidpur is an architectural jewel of Bangladesh. Founded in 1863 as a modest prayer hall by Haji Bakir Ali, the mosque was transformed into an astonishing artistic marvel in the early 20th century using the delicate 'Chini-Tikri' technique. Its facades, 27 minarets, and three large domes are meticulously encrusted with over 250 pieces of antique British porcelain, authentic Queen Victoria coins, and hundreds of thousands of colorful ceramic shards imported from Kolkata. The gleaming domes reflect morning sunlight in dazzling arrays of emerald, cobalt, and ruby hues, mesmerizing tourists and architecture lovers from around the world.",
            "descBn": "সৈয়দপুর শহরের ইসলামবাগ এলাকায় অবস্থিত চিনি মসজিদ বাংলাদেশের স্থাপত্যকলার এক অনন্য বিস্ময়। ১৮৬৩ সালে হাজী বাকির আলী এই মসজিদ প্রতিষ্ঠা করেন এবং পরবর্তীতে বিশ শতকের শুরুতে একে 'চিনি-টিকরি' মোজাইক শিল্পে রূপান্তর করা হয়। মসজিদের ২৭টি মিনার ও ৩টি সুবিশাল গম্বুজ প্রায় ২৫০টি দুর্লভ ভিক্টোরিয়ান মুদ্রা এবং কলকাতা থেকে আনা হাজার হাজার রঙিন চীনা মাটির পাত্রের টুকরো দিয়ে অপরূপভাবে সাজানো। সূর্যের আলোয় মসজিদের মিনারগুলো স্ফটিকের মতো জ্বলজ্বল করে, যা দেশ-বিদেশের স্থাপত্যপ্রেমী ও পর্যটকদের অবাক করে দেয়।",
            "locationEn": "Saidpur, Nilphamari",
            "locationBn": "সৈয়দপুর, নীলফামারী",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Chini%20Mosque%2C%20Saidpur%2C%20Nilphamari"
        },
        {
            "id": 4,
            "nameEn": "Saidpur Railway Workshop heritage area",
            "nameBn": "সৈয়দপুর রেলওয়ে কারখানা হেরিটেজ এলাকা",
            "categoryEn": "Historic Victorian Industrial Engineering Works",
            "categoryBn": "ঐতিহাসিক বৃহত্তম ব্রিটিশ রেলওয়ে কারখানা",
            "descEn": "Established in 1870 by the British Eastern Bengal Railway, the Saidpur Railway Workshop is the largest, oldest, and most storied locomotive and railway carriage manufacturing works in Bangladesh. Sprawling over 110 acres with 28 specialized heavy engineering shops, the complex retains vintage industrial iron foundry presses, operational steam locomotive repair bays, and colonial red-brick powerhouse towers. Although general entry requires prior administrative approval, heritage enthusiasts marvel at the sprawling railway infrastructure, antique railway tracks, and historic Victorian industrial ambiance that laid the technological backbone of northern Bengal's transportation network.",
            "descBn": "১৮৭০ সালে ব্রিটিশ শাসনামলে প্রতিষ্ঠিত সৈয়দপুর রেলওয়ে কারখানা বাংলাদেশের সর্ববৃহৎ ও সবচেয়ে প্রাচীন রেল কারখানা। প্রায় ১১০ একর জমির ওপর গড়ে ওঠা এই কারখানায় রয়েছে ২৮টি বিশেষায়িত শপ, যেখানে একসময় বাষ্পীয় ইঞ্জিন ও রেলের বগি মেরামত হতো। ব্রিটিশ আমলের সুবিশাল লাল ইটের শেড, ভারী লেদ মেশিন, ওভারহেড ক্রেন এবং রেল ট্র্যাকগুলো যেন এক উন্মুক্ত শিল্প জাদুঘর। যথাযথ কর্তৃপক্ষের অনুমতি নিয়ে এই ঐতিহাসিক কারখানা পরিদর্শন করা যে কোনো কারিগরি ও ইতিহাসপ্রেমীর জন্য এক অনন্য অভিজ্ঞতা।",
            "locationEn": "Saidpur; access may be restricted",
            "locationBn": "সৈয়দপুর রেলওয়ে চত্বর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Saidpur%20Railway%20Workshop%20heritage%20area%2C%20Saidpur%3B%20access%20may%20be%20restricted"
        },
        {
            "id": 5,
            "nameEn": "Saidpur old town and railway colony",
            "nameBn": "সৈয়দপুর ওল্ড টাউন ও রেলওয়ে কলোনি",
            "categoryEn": "Colonial Bungalows & Urban Heritage Enclave",
            "categoryBn": "ব্রিটিশ আমলের রেলওয়ে বাংলো ও কলোনি",
            "descEn": "The old town and Railway Colony of Saidpur form a unique cultural and architectural enclave preserved from British colonial times. Designed as an imperial railway township in the late 19th century, the neighborhood boasts tree-shaded boulevards lined with vintage brick bungalows featuring broad verandas, corrugated metal gables, chimney hearths, and lush private lawns built for British railway officers. The town is also renowned for its multicultural harmony, lively local bazaars, and legendary culinary heritage—especially its delicious Saidpur beef kababs, biryanis, and traditional sweets.",
            "descBn": "সৈয়দপুর শহরের পুরনো অংশ ও রেলওয়ে অফিসার্স কলোনি যেন ব্রিটিশ ঔপনিবেশিক স্থাপত্যের এক জীবন্ত প্রদর্শনী। উনিশ শতকের শেষভাগে ব্রিটিশ রেলওয়ে কর্মকর্তাদের বসবাসের জন্য নির্মিত লাল ইটের প্রশস্ত বাংলো, চিমনির ছাদ, বিশাল বাগান ও ছায়াঘেরা রাজপথ আজও অক্ষুণ্ণ রয়েছে। সেই সাথে সৈয়দপুরের বৈচিত্র্যময় সংস্কৃতি, ব্যস্ত বাজার এবং ঐতিহ্যবাহী মুখরোচক কাবাব ও মিষ্টির স্বাদ নিতে প্রতিদিন বহু পর্যটক এই ঐতিহ্যের শহরে ভিড় জমান।",
            "locationEn": "Saidpur, Nilphamari",
            "locationBn": "সৈয়দপুর শহর, নীলফামারী",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Saidpur%20old%20town%20and%20railway%20colony%2C%20Saidpur%2C%20Nilphamari"
        }
    ]
}

# 16. THAKURGAON
thakurgaon = {
    "slug": "thakurgaon",
    "en": "Thakurgaon",
    "bn": "ঠাকুরগাঁও",
    "hero_title_en": "Thakurgaon Ancient Zamindar Palaces & Sugar Mills",
    "hero_title_bn": "ঠাকুরগাঁওয়ের প্রাচীন রাজবাড়ি ও জামিদারী ঐতিহ্য",
    "hero_sub_en": "Jamalpur Zamindar Bari terracotta, Haripur Rajbari, and lush Shuk riverbanks.",
    "hero_sub_bn": "ঐতিহাসিক জামালপুর জমিদার বাড়ি, হরিপুর রাজবাড়ির ধ্বংসাবশেষ ও শুক নদীর শান্ত স্নিগ্ধ তীর।",
    "tagline_en": "An agricultural northern haven renowned for its magnificent terracotta zamindar estates, tranquil riverbeds of the Shuk and Tangon, and the historic legacy of north Bengal's sugar cultivation.",
    "tagline_bn": "উত্তরবঙ্গের শান্ত কৃষিপ্রধান জেলা, যা চমৎকার পোড়ামাটির কারুকার্যময় জামালপুর জমিদার বাড়ি, ঐতিহাসিক হরিপুর রাজবাড়ি এবং শুক নদীর মনোমুগ্ধকর তীরের জন্য সুপরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/thakurgaon/carousel-1.webp",
            "titleEn": "Jamalpur Zamindar Bari Terracotta Masterpiece",
            "titleBn": "জামালপুর জমিদার বাড়ি পোড়ামাটির অপূর্ব স্থাপত্য",
            "subtitleEn": "19th-century royal palace complex adorned with exquisite terracotta motifs and graceful domes",
            "subtitleBn": "উনবিংশ শতাব্দীর দৃষ্টিনন্দন জমিদার বাড়ি যা সূক্ষ্ম পোড়ামাটির অলংকরণ ও গম্বুজ দ্বারা শোভিত"
        },
        {
            "id": 2,
            "image": "images/districts/thakurgaon/carousel-2.webp",
            "titleEn": "Haripur Rajbari Historic Aristocratic Palace",
            "titleBn": "হরিপুর রাজবাড়ি প্রাচীন রাজপ্রাসাদের ধ্বংসাবশেষ",
            "subtitleEn": "Colonial-era palace ruins in Haripur featuring towering neoclassical colonnades",
            "subtitleBn": "হরিপুরে অবস্থিত রাজকীয় খিলান ও কারুকার্যময় প্রাচীন রাজপ্রাসাদের ঐতিহাসিক ধ্বংসাবশেষ"
        },
        {
            "id": 3,
            "image": "images/districts/thakurgaon/carousel-3.webp",
            "titleEn": "Balia Mosque Elegant Single-Dome Historic Shrine",
            "titleBn": "বালিয়া মসজিদ প্রাচীন এক গম্বুজ ঐতিহাসিক মসজিদ",
            "subtitleEn": "Centuries-old Islamic sanctuary featuring thick masonry arches and traditional domes",
            "subtitleBn": "বালিয়া গ্রামে অবস্থিত প্রাচীন স্থাপত্যশৈলীর ঐতিহাসিক মসজিদ ও মনোরম গ্রামীণ প্রাঙ্গণ"
        },
        {
            "id": 4,
            "image": "images/districts/thakurgaon/carousel-4.webp",
            "titleEn": "Rani Shankail Dighi Legendary Vast Water Reservoir",
            "titleBn": "রানীশংকৈল দিঘি ঐতিহাসিক সুবিশাল জলাশয়",
            "subtitleEn": "Ancient royal lake surrounded by earthen embankments and tranquil green village canopies",
            "subtitleBn": "রানীশংকৈলের ঐতিহ্যবাহী বিশাল দিঘি যার স্বচ্ছ জলরাশি ও পাড়ের বৃক্ষরাজি মন জুড়ায়"
        },
        {
            "id": 5,
            "image": "images/districts/thakurgaon/carousel-5.webp",
            "titleEn": "Thakurgaon Sugar Mill Historic Industrial Complex",
            "titleBn": "ঠাকুরগাঁও চিনি কল ঐতিহাসিক কৃষি-শিল্প কারখানা",
            "subtitleEn": "Pioneering agro-industrial enterprise processing regional sugarcane since the 1950s",
            "subtitleBn": "১৯৫০-এর দশকে স্থাপিত উত্তরবঙ্গের ঐতিহ্যবাহী চিনি উৎপাদন কারখানা ও চত্বর"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Baliadangi Zamindar Bari site",
            "nameBn": "বালিয়াডাঙ্গী জমিদার বাড়ি সাইট",
            "categoryEn": "Historic Feudal Estate & Surviving Relics",
            "categoryBn": "ঐতিহাসিক জমিদার বাড়ির অবশিষ্টাংশ",
            "descEn": "The Baliadangi Zamindar Bari site in Baliadangi Upazila preserves the historical legacy of the local landed aristocracy who held sway over the northern frontier during late British rule. The estate grounds feature surviving brick foundations, classical stone archways, decorative temple structures, and ancient stone ponds. Local lore recounts the zamindars' contributions to developing regional trade routes, weekly haats, and canal irrigation. Although several palatial wings have suffered the ravages of time, the atmospheric site provides a rich window into the feudal heritage and pastoral society of historical Dinajpur-Thakurgaon.",
            "descBn": "বালিয়াডাঙ্গী উপজেলায় অবস্থিত এই প্রাচীন জমিদার বাড়িটি ব্রিটিশ শাসনামলের স্থানীয় জমিদারদের শাসন ও ঐতিহ্যের স্মারক। এই বিস্তৃত এস্টেটে এখনও টিকে রয়েছে প্রাচীন ইটের সীমানা প্রাচীর, রাজকীয় খিলান, নাটমন্দির এবং বিশাল পুকুর। স্থানীয় হাট-বাজার ও কৃষির উন্নয়নে এই জমিদার পরিবারের বহু অবদান ছিল। কালের পরিক্রমায় প্রাসাদের অনেক অংশ ক্ষতিগ্রস্ত হলেও এর প্রাচীন স্থাপত্য ও নিস্তব্ধ পরিবেশ ইতিহাসানুরাগী ভ্রমণকারীদের অতীত দিনগুলোতে ফিরিয়ে নিয়ে যায়।",
            "locationEn": "Baliadangi; verify surviving structures",
            "locationBn": "বালিয়াডাঙ্গী, ঠাকুরগাঁও",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Baliadangi%20Zamindar%20Bari%20site%2C%20Baliadangi%3B%20verify%20surviving%20structures"
        },
        {
            "id": 2,
            "nameEn": "Jamalpur Zamindar Bari",
            "nameBn": "জামালপুর জমিদার বাড়ি",
            "categoryEn": "Exquisite Terracotta Heritage Palace & Mosque",
            "categoryBn": "পোড়ামাটির কারুকার্যময় রাজকীয় প্রাসাদ ও মসজিদ",
            "descEn": "Jamalpur Zamindar Bari, located in Jamalpur union under Thakurgaon Sadar Upazila, is widely celebrated as one of the finest architectural treasures of northern Bangladesh. Commissioned in 1862 by Zamindar Rowshan Ali and completed by his son Mohammad Pir Baksh, the complex features a magnificent palatial gatehouse, residential quarters, and an astonishing multi-domed mosque adorned with intricate floral terracotta plaques. Rising nearly 100 feet in height, the mosque’s minarets and terracotta walls echo Mughal and late Bengal Islamic craftsmanship. The preservation of its delicate motifs makes it a prized cultural landmark for architecture aficionados.",
            "descBn": "ঠাকুরগাঁও সদর উপজেলার জামালপুর ইউনিয়নে অবস্থিত জামালপুর জমিদার বাড়ি ও মসজিদ উত্তরবঙ্গের এক অতুলনীয় স্থাপত্যকীর্তি। ১৮৬২ সালে জমিদার রওশন আলী এর নির্মাণ কাজ শুরু করেন এবং পরবর্তীতে তাঁর পুত্র পীর বকশ এটি সমাপ্ত করেন। প্রাসাদের সুবিশাল ফটক এবং বিশেষ করে সংলগ্ন চার গম্বুজবিশিষ্ট জামে মসজিদটি চোখ জুড়ানো পোড়ামাটির লতাপাতা ও নকশায় সজ্জিত। এর দৃষ্টিনন্দন মিনার ও কারুকার্য মোঘল স্থাপত্যের স্মৃতি মনে করিয়ে দেয়। বাংলাদেশের প্রত্নতাত্ত্বিক ঐতিহ্যের এক অনন্য রত্ন হিসেবে এটি দর্শনার্থীদের মুগ্ধ করে।",
            "locationEn": "Jamalpur, Thakurgaon Sadar",
            "locationBn": "জামালপুর, ঠাকুরগাঁও সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Jamalpur%20Zamindar%20Bari%2C%20Jamalpur%2C%20Thakurgaon%20Sadar"
        },
        {
            "id": 3,
            "nameEn": "Rajbari ruins at Haripur",
            "nameBn": "হরিপুর রাজবাড়ির ধ্বংসাবশেষ",
            "categoryEn": "Colonial Neoclassical Aristocratic Palace",
            "categoryBn": "ব্রিটিশ আমলের রাজপ্রাসাদের ঐতিহাসিক ধ্বংসাবশেষ",
            "descEn": "The Rajbari ruins at Haripur, situated close to the Indo-Bangladesh border in Haripur Upazila, were built at the end of the 19th century by Zamindar Roghonandan Roy. The sprawling two-storied palace was designed in an elegant neoclassical European style blended with traditional Bengali palace courtyard planning. The complex features grand Corinthian columns, decorated arched windows, marble floors, a royal theater hall (Natmandir), and an expansive inner courtyard. Though currently weathered by time and overgrowth, the towering structural skeletons evoke a vivid sense of the aristocratic grandeur and cultural soirées that once animated this frontier palace.",
            "descBn": "হরিপুর উপজেলায় অবস্থিত হরিপুর রাজবাড়ি ঊনবিংশ শতাব্দীর শেষভাগে জমিদার রঘুনন্দন রায় কর্তৃক নির্মিত হয়। দোতলা বিশিষ্ট এই বিশাল রাজপ্রাসাদটি ইউরোপীয় স্থাপত্যরীতি ও দেশীয় রাজকীয় ঐতিহ্যের এক অপূর্ব সংমিশ্রণ। এতে রয়েছে সুউচ্চ করিন্থিয়ান স্তম্ভ, খিলানযুক্ত অলংকৃত জানালা, নাটমহল এবং মনোরম অন্দরমহল। কালের আবর্তে প্রাসাদের অনেক অংশ আজ ধ্বংসাবশেষে পরিণত হলেও এর সুউচ্চ দেয়াল ও রাজকীয় কাঠামো এখনও অতীত আভিজাত্য ও জৌলুসের নীরব সাক্ষী হয়ে দাঁড়িয়ে আছে।",
            "locationEn": "Haripur, Thakurgaon",
            "locationBn": "হরিপুর, ঠাকুরগাঁও",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Rajbari%20ruins%20at%20Haripur%2C%20Haripur%2C%20Thakurgaon"
        },
        {
            "id": 4,
            "nameEn": "Shalbagan Mosque",
            "nameBn": "শালবাগান ঐতিহাসিক মসজিদ",
            "categoryEn": "Historic Woodland Mosque Relic",
            "categoryBn": "শালবনের কোলে অবস্থিত প্রাচীন মসজিদ",
            "descEn": "The Shalbagan Mosque is an antique brick sanctuary nestled within the peaceful indigenous Sal forest groves of Thakurgaon district. Constructed during the late medieval period with thick hand-molded terracotta brickwork and lime mortar, the modest single-chambered structure features low vaulted arches and prayer niches designed to blend serenely with surrounding woodland nature. The mosque provided a serene spiritual sanctuary for traveling dervishes, traders, and local villagers trekking between northern settlements. The combination of ancient sacred architecture and rustling Sal foliage makes it an atmospheric destination for off-the-beaten-path travelers.",
            "descBn": "ঠাকুরগাঁও জেলার প্রাকৃতিক শালবনের সুনিবিড় ছায়াতলে অবস্থিত শালবাগান প্রাচীন মসজিদ এক অনন্য আধ্যাত্মিক নিদর্শন। মধ্যযুগীয় বাংলার ঐতিহ্যবাহী পোড়ামাটির ইট ও চুন-সুরকির গাঁথুনিতে নির্মিত এই প্রাচীন মসজিদটির গঠনশৈলী অত্যন্ত সুদৃঢ় ও মনোহর। প্রাচীনকালে এই পথ দিয়ে চলাচলকারী সুফি সাধক, ব্যবসায়ী ও পথচারীদের প্রার্থনার জন্য এটি তৈরি হয়েছিল। চারপাশের সবুজ শালগাছের স্নিগ্ধ বাতাস এবং পাখির কলকাকলির মাঝে দাঁড়িয়ে থাকা এই ঐতিহাসিক মসজিদটি মনকে অনাবিল শান্তিতে ভরিয়ে দেয়।",
            "locationEn": "Thakurgaon district; verify village",
            "locationBn": "শালবাগান এলাকা, ঠাকুরগাঁও",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Shalbagan%20Mosque%2C%20Thakurgaon%20district%3B%20verify%20village"
        },
        {
            "id": 5,
            "nameEn": "Pirganj historic mosque and temple sites",
            "nameBn": "পীরগঞ্জের ঐতিহাসিক মসজিদ ও মন্দির চত্বর",
            "categoryEn": "Interfaith Archaeological & Sacred Sites",
            "categoryBn": "ঐতিহাসিক প্রাচীন মসজিদ ও দেবালয় চত্বর",
            "descEn": "Pirganj Upazila in Thakurgaon hosts a cluster of venerable medieval heritage monuments representing the harmonious coexistence of Islamic and Hindu traditions. The area is home to ancient multi-domed terracotta mosques, dargahs of venerated Sufi saints, and century-old terracotta Hindu temple complexes dedicated to Lord Shiva and Krishna. These structures showcase fine relief work, curving 'do-chala' and 'chaar-chala' roof contours, and historic tank ghats where community festivals have been celebrated for centuries. Exploring Pirganj's heritage sites reveals the deep cultural syncretism that characterizes northern Bengal's shared history.",
            "descBn": "ঠাকুরগাঁওয়ের পীরগঞ্জ উপজেলায় ছড়িয়ে রয়েছে মধ্যযুগ ও ব্রিটিশ আমলের বহু ঐতিহাসিক মসজিদ, সুফি মাজার ও প্রাচীন দেবালয়ের নিদর্শন। এখানকার পোড়ামাটির কারুকার্যময় প্রাচীন মসজিদ এবং শতবর্ষী টেরাকোটা শিব ও রাধাকৃষ্ণ মন্দিরগুলো বাংলার চিরায়ত সাম্প্রদায়িক সম্প্রীতির উজ্জ্বল উদাহরণ। চারচালা ও দোচালা স্থাপত্যরীতি, প্রাচীন শিলালিপি এবং ঐতিহাসিক পুকুরঘাটগুলো এই অঞ্চলের সমৃদ্ধ ইতিহাসের জানান দেয়। গবেষক ও ভ্রমণপিপাসুদের জন্য পীরগঞ্জের এই প্রত্নস্থলগুলো অত্যন্ত শিক্ষণীয়।",
            "locationEn": "Pirganj; ask locally for specific sites",
            "locationBn": "পীরগঞ্জ, ঠাকুরগাঁও",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Pirganj%20historic%20mosque%20and%20temple%20sites%2C%20Pirganj%3B%20ask%20locally%20for%20specific%20sites"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Rani Shankail Dighi",
            "nameBn": "রানীশংকৈল দিঘি",
            "categoryEn": "Historic Royal Reservoir & Scenic Park",
            "categoryBn": "ঐতিহাসিক রানীর দিঘি ও মনোরম জলাশয়",
            "descEn": "Rani Shankail Dighi, located in Ranisankail Upazila of Thakurgaon, is an enormous historic royal tank excavated centuries ago by the local ruling queens of the northern estates. Spanning dozens of acres, the reservoir is bordered by wide earthen embankments planted with mango, jackfruit, and mahogany trees that cast deep green reflections upon the tranquil water. Locals and visitors gather along the ghats in the afternoons to enjoy cool breezes, birdwatch, and take scenic strolls around the perimeter. The serene, unhurried atmosphere makes it an essential leisure stop when exploring western Thakurgaon.",
            "descBn": "রানীশংকৈল উপজেলায় অবস্থিত ঐতিহাসিক রানীশংকৈল দিঘি উত্তরবঙ্গের এক সুপ্রাচীন সুবিশাল জলাশয়। স্থানীয় রাজপরিবারের রানীর স্মৃতিবিজড়িত এই বিশাল দিঘির চারপাশ ঘিরে রয়েছে সুউচ্চ পাড় ও ছায়াঘেরা আম-কাঁঠালের বাগান। দিঘির স্ফটিকস্বচ্ছ জলে আকাশের মেঘের ছায়া এবং বিকেলের মৃদুমন্দ হাওয়া দর্শনার্থীদের দারুণভাবে মুগ্ধ করে। স্থানীয় মানুষ ও পর্যটকদের জন্য এটি অবসরের এক প্রিয় বিনোদন ও প্রকৃতি দর্শনের স্থান।",
            "locationEn": "Ranisankail, Thakurgaon",
            "locationBn": "রানীশংকৈল, ঠাকুরগাঁও",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Rani%20Shankail%20Dighi%2C%20Ranisankail%2C%20Thakurgaon"
        },
        {
            "id": 2,
            "nameEn": "Shuk Riverbank",
            "nameBn": "শুক নদী তীর ও প্রাকৃতিক চত্বর",
            "categoryEn": "Tranquil Riverine Landscapes & Wildlife",
            "categoryBn": "শান্ত শুক নদীর মনোরম পাড় ও সূর্যাস্ত",
            "descEn": "The Shuk River is a gentle transboundary river meandering gracefully through the rural landscapes of Thakurgaon. Unlike raging deltaic rivers, the Shuk flows calmly between sandy banks, shallow pebbly shallows, and lush green agricultural fields of mustard, paddy, and wheat. In the winter months, golden sandbars emerge where children play, fishermen cast traditional nets, and migrating birds wade in the shallows. The riverbank offers a picturesque setting for peaceful afternoon picnics, photography, and watching romantic rural sunsets over northern waters.",
            "descBn": "ঠাকুরগাঁও জেলার বুক চিরে বয়ে চলা শুক নদী উত্তরবঙ্গের এক শান্ত ও স্নিগ্ধ নদীয় নিসর্গ। তীব্র স্রোতের পরিবর্তে এই নদীটির রয়েছে শান্ত জলধারা, স্বচ্ছ বালুময় তীর এবং দুপাশে দিগন্তবিস্তৃত সবুজ ফসলের মাঠ। শীতকালে নদীর চরে ফোটে কাশফুল এবং দেখা মেলে নানা জাতের জলচর পাখির। শুক নদীর তীরে বসে পড়ন্ত বিকেলে সূর্যাস্ত দেখা এবং বিশুদ্ধ নির্মল বাতাস উপভোগ করা যে কোনো পর্যটকের জন্য এক অপার্থিব শান্তির অনুভূতি এনে দেয়।",
            "locationEn": "Thakurgaon district",
            "locationBn": "শুক নদী তীর, ঠাকুরগাঁও",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Shuk%20Riverbank%2C%20Thakurgaon%20district"
        },
        {
            "id": 3,
            "nameEn": "Balia Mosque area",
            "nameBn": "বালিয়া মসজিদ এলাকা ও প্রাচীন নিসর্গ",
            "categoryEn": "Historic Village Landmark & Pastoral Heritage",
            "categoryBn": "ঐতিহাসিক বালিয়া মসজিদ ও গ্রামীণ পরিবেশ",
            "descEn": "The Balia Mosque area in Balia union under Thakurgaon Sadar Upazila is a picturesque countryside heritage enclave centered around the historic 19th-century Balia Mosque. Built by local master mason Meher Ali alongside renowned craftsmen from Murshidabad, the mosque features unique three-tiered domes, terracotta floral inlays, and slender minarets standing gracefully amid idyllic bamboo groves and village ponds. Visitors enjoy exploring the tranquil hamlet, interacting with hospitable village artisans, and photographing the architectural gem in its unspoiled rural setting.",
            "descBn": "ঠাকুরগাঁও সদর উপজেলার বালিয়া ইউনিয়নে অবস্থিত বালিয়া মসজিদ ও তার আশপাশের এলাকা গ্রামীণ ঐতিহ্যের এক অপূর্ব মিলনস্থল। উনবিংশ শতাব্দীতে স্থানীয় জমিদার মেহের আলীর উদ্যোগে মুর্শিদাবাদের কারিগরদের দ্বারা নির্মিত এই মসজিদটি তার চমৎকার খিলান ও কারুকার্যের জন্য বিখ্যাত। শান্ত পুকুরপাড় ও বাঁশবাগানের মনোরম পটভূমিতে মসজিদটির তিন গম্বুজ যেন এক জীবন্ত চিত্রকর্ম। নির্জন গ্রামীণ পরিবেশে স্থাপত্যের সৌন্দর্য উপভোগ করতে বহু দর্শনার্থী এখানে আসেন।",
            "locationEn": "Balia, Thakurgaon Sadar",
            "locationBn": "বালিয়া, ঠাকুরগাঁও সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Balia%20Mosque%20area%2C%20Balia%2C%20Thakurgaon%20Sadar"
        },
        {
            "id": 4,
            "nameEn": "Haripur countryside",
            "nameBn": "হরিপুরের মনোরম গ্রামীণ নিসর্গ",
            "categoryEn": "Border Countryside & Agricultural Landscapes",
            "categoryBn": "সীমান্তবর্তী সবুজ মেঠোপথ ও ফসলি জমি",
            "descEn": "The countryside of Haripur Upazila presents an open, sweeping panorama of northern rural life right along the Bangladesh-India borderlands. The region is carpeted with lush paddy fields, golden wheat paddocks, and fragrant mango orchards that stretch to the horizon under clear blue skies. Winding earthen roads shaded by towering eucalyptus and palm trees connect peaceful farming villages where traditional clay-and-thatch cottages remain common. Traveling through Haripur provides an authentic experience of rural hospitality, fresh seasonal produce, and the serene rhythm of northern village life.",
            "descBn": "হরিপুর উপজেলার গ্রামীণ নিসর্গ উত্তরবঙ্গের সীমান্ত অঞ্চলের শান্ত ও অকৃত্রিম সৌন্দর্যের প্রতীক। দূর দিগন্ত পর্যন্ত বিস্তৃত সবুজ ধানক্ষেত, শীতের হলুদ সরিষা এবং সোনালী গমের মাঠ চোখ জুড়িয়ে দেয়। ছায়াঘেরা কাঁচা মেঠোপথ ধরে হেঁটে গেলে চোখে পড়ে মাটির দেয়াল ও ছনের তৈরি ঐতিহ্যবাহী ঘরবাড়ি এবং কৃষকদের সহজ-সরল জীবনযাপন। কোলাহলমুক্ত স্নিগ্ধ বাতাস এবং সীমান্ত অঞ্চলের মুক্ত আকাশ যে কোনো ভ্রমণকারীকে মুগ্ধ করে।",
            "locationEn": "Haripur, Thakurgaon",
            "locationBn": "হরিপুর, ঠাকুরগাঁও",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Haripur%20countryside%2C%20Haripur%2C%20Thakurgaon"
        },
        {
            "id": 5,
            "nameEn": "Thakurgaon Sugar Mill area",
            "nameBn": "ঠাকুরগাঁও সুগার মিল চত্বর",
            "categoryEn": "Industrial Agro-Heritage & Green Campus",
            "categoryBn": "ঐতিহাসিক চিনি শিল্প এলাকা ও সবুজ ক্যাম্পাস",
            "descEn": "Thakurgaon Sugar Mills Limited, located in Thakurgaon Sadar, is one of the oldest and largest state-owned sugar refineries in Bangladesh, established in 1956. Sprawled across a lush campus dotted with vintage machinery, broad tree-lined avenues, residential quarters, and sugarcane storage yards, the mill area is a landmark of regional agricultural industry. During the winter harvesting season (November to February), the air is filled with the sweet aroma of boiling sugarcane juice as hundreds of tractor-trailers deliver freshly harvested cane. It offers an educational and evocative tour into Bangladesh’s foundational post-colonial agro-industries.",
            "descBn": "ঠাকুরগাঁও সদর উপজেলায় ১৯৫৬ সালে প্রতিষ্ঠিত ঠাকুরগাঁও চিনি কল বাংলাদেশের অন্যতম প্রাচীন ও প্রধান ভারী কৃষি-শিল্প প্রতিষ্ঠান। সুবিশাল কারখানা চত্বর, ব্রিটিশ-পরবর্তী আমলের যন্ত্রপাতি, বিশাল গুদামঘর এবং ছায়াঘেরা আবাসিক কলোনি নিয়ে এটি একটি আকর্ষণীয় শিল্প এলাকা। শীতকালে আখ মাড়াই মৌসুমে চারপাশের বাতাসে মিষ্টি গুড়ের সুবাস ছড়িয়ে পড়ে এবং শত শত আখের ট্রলি কারখানায় প্রবেশের দৃশ্য দেখার মতো হয়। উত্তরবঙ্গের কৃষিভিত্তিক শিল্পের ইতিহাস জানতে এটি একটি দারুণ দর্শনীয় স্থান।",
            "locationEn": "Thakurgaon Sadar; confirm public access",
            "locationBn": "ঠাকুরগাঁও সদর এলাকা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Thakurgaon%20Sugar%20Mill%20area%2C%20Thakurgaon%20Sadar%3B%20confirm%20public%20access"
        }
    ]
}

# 17. PANCHAGARH
panchagarh = {
    "slug": "panchagarh",
    "en": "Panchagarh",
    "bn": "পঞ্চগড়",
    "hero_title_en": "Panchagarh The Himalayan Gateway & Tetulia Tea Lands",
    "hero_title_bn": "পঞ্চগড়ের কাঞ্চনজঙ্ঘা দৃশ্য ও তেঁতুলিয়ার চা বাগান",
    "hero_sub_en": "Kanchenjunga mountain viewpoints, Mahananda River, and Banglabandha Zero Point.",
    "hero_sub_bn": "কাঞ্চনজঙ্ঘার বরফাবৃত রূপ, মহানন্দা নদীর স্ফটিক জলধারা ও সমতলের সবুজ চা বাগান।",
    "tagline_en": "The northernmost tip of Bangladesh, internationally celebrated for breathtaking autumn panoramas of Mount Kanchenjunga, sprawling organic flatland tea gardens, and the strategic border crossroads of Banglabandha Zero Point.",
    "tagline_bn": "বাংলাদেশের সর্বউত্তরের হিমালয়কন্যা পঞ্চগড়, যা শরৎ-হেমন্তে বরফশুভ্র কাঞ্চনজঙ্ঘার মায়াবী রূপ, সমতলের মনোমুগ্ধকর সবুজ চা বাগান এবং ঐতিহাসিক বাংলাবান্ধা জিরো পয়েন্টের জন্য সুখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/panchagarh/carousel-1.webp",
            "titleEn": "Mount Kanchenjunga Majestic Autumn Panoramas",
            "titleBn": "কাঞ্চনজঙ্ঘার বরফশুভ্র অপরূপ দৃশ্য",
            "subtitleEn": "Clear autumn views of the world's third highest Himalayan peak glowing golden at dawn from Tetulia",
            "subtitleBn": "তেঁতুলিয়ার আকাশ পরিষ্কার হলে সকালে ও গোধূলিতে দৃশ্যমান বিশ্বের ৩য় সর্বোচ্চ শৃঙ্গ কাঞ্চনজঙ্ঘা"
        },
        {
            "id": 2,
            "image": "images/districts/panchagarh/carousel-2.webp",
            "titleEn": "Tetulia Tea Gardens Lush Flatland Plantations",
            "titleBn": "তেঁতুলিয়ার সমতল চা বাগান ও সবুজ গালিচা",
            "subtitleEn": "Verdant manicured tea estates carpeting the plains between the Korotoa and Mahananda rivers",
            "subtitleBn": "হিমালয়ের পাদদেশের সমতলে গড়ে ওঠা দিগন্তজোড়া চোখ জুড়ানো সবুজ চা বাগান"
        },
        {
            "id": 3,
            "image": "images/districts/panchagarh/carousel-3.webp",
            "titleEn": "Banglabandha Zero Point International Borderland",
            "titleBn": "বাংলাবান্ধা জিরো পয়েন্ট সর্বউত্তরের সীমান্ত সংযোগ",
            "subtitleEn": "Historic four-nation junction connecting Bangladesh with India, Nepal, and Bhutan",
            "subtitleBn": "ভারত, নেপাল ও ভুটানের সাথে সংযুক্ত বাংলাদেশের সর্বউত্তরের আন্তর্জাতিক সীমান্তবিন্দু"
        },
        {
            "id": 4,
            "image": "images/districts/panchagarh/carousel-4.webp",
            "titleEn": "Mahananda River Shimmering Pebble Beds",
            "titleBn": "মহানন্দা নদী স্বচ্ছ জল ও পাথর আহরণ",
            "subtitleEn": "Transboundary Himalayan river flowing over glittering stones under the shadows of India's tea hills",
            "subtitleBn": "তেঁতুলিয়ার বুক চিরে বয়ে চলা স্ফটিকস্বচ্ছ হিমালয়কন্যা মহানন্দা নদী ও পাথুরে চর"
        },
        {
            "id": 5,
            "image": "images/districts/panchagarh/carousel-5.webp",
            "titleEn": "Mirzapur Shahi Mosque Mughal Terracotta Marvel",
            "titleBn": "মির্জাপুর শাহী মসজিদ মোঘল টেরাকোটা স্থাপত্য",
            "subtitleEn": "Centuries-old Mughal mosque at Atwari featuring ornate terracotta inlays and domed elegance",
            "subtitleBn": "আটোয়ারীতে অবস্থিত সপ্তদশ শতকের চোখ জুড়ানো পোড়ামাটির কারুকার্যময় ঐতিহাসিক মসজিদ"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Maharaja Dighi",
            "nameBn": "মহারাজার দীঘি (ভিতরগড়)",
            "categoryEn": "Ancient Fortified City Reservoir & Citadel Relic",
            "categoryBn": "প্রাচীন ভিতরগড় দুর্গের বিশাল মহারাজার দীঘi",
            "descEn": "Maharaja Dighi, also known as the historic Dighi of Bhitargarh, is an enormous 53-acre ancient waterbody located within the archaeological ramparts of the Bhitargarh Citadel in Tetulia-Panchagarh. Excavated around the 5th to 6th centuries CE by King Prithu (widely known as Maharaja Prithu Raja), the reservoir served as the sacred water source and central moat of this legendary fortified sovereign city-state. Surrounded by towering earthen dykes, stone embankments, and archaeological trenches that yielded ancient sandstone pillars and terracotta tiles, Maharaja Dighi stands as a monument to northern Bengal's deep pre-medieval urban civilization.",
            "descBn": "পঞ্চগড়ের ঐতিহাসিক ভিতরগড় দুর্গের অভ্যন্তরে অবস্থিত মহারাজার দীঘি প্রায় ৫৩ একর আয়তনের এক সুপ্রাচীন জলাশয়। আনুমানিক পঞ্চম-ষষ্ঠ শতাব্দীতে স্বাধীন ভিতরগড় রাজ্যের অধিপতি মহারাজ পৃথু এই সুবিশাল দীঘিটি খনন করিয়েছিলেন। বিশাল মাটির পাড় ও প্রাচীন পাথরের ঘাটে ঘেরা এই দীঘির চারপাশ থেকে বহু প্রাচীন শিলালিপি, পোড়ামাটির ফলক ও ইটের ভিত্তিমূল আবিষ্কৃত হয়েছে। ইতিহাস ও পুরাতত্ত্বপ্রেমীদের কাছে প্রাচীন বাংলার সার্বভৌম নগর সংস্কৃতির এক অবিস্মরণীয় নিদর্শন এই মহারাজার দীঘি।",
            "locationEn": "Tetulia, Panchagarh",
            "locationBn": "তেঁতুলিয়া, পঞ্চগড়",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Maharaja%20Dighi%2C%20Tetulia%2C%20Panchagarh"
        },
        {
            "id": 2,
            "nameEn": "Mirzapur Shahi Mosque",
            "nameBn": "মির্জাপুর শাহী মসজিদ",
            "categoryEn": "Mughal Terracotta Architectural Masterpiece",
            "categoryBn": "মোঘল আমলের পোড়ামাটির অনন্য শাহী মসজিদ",
            "descEn": "Mirzapur Shahi Mosque, located in Mirzapur village of Atwari Upazila, is a dazzling architectural gem of late Mughal Bengal. Erected in 1656 CE (circa 1066 Hijri) during the reign of Mughal Viceroy Prince Shah Shuja by Malik Niamatullah, the mosque features three hemispherical fluted domes, octagonal corner turrets, and ornate surface panels encrusted with delicate terracotta reliefs depicting floral vines and geometric motifs. Persian inscriptions above the central archway document its historical lineage. The harmonious proportions and preserved terracotta craftsmanship make it one of the premier Islamic architectural destinations in northern Bangladesh.",
            "descBn": "পঞ্চগড়ের আটোয়ারী উপজেলার মির্জাপুর গ্রামে অবস্থিত মির্জাপুর শাহী মসজিদ মোঘল স্থাপত্যকলার এক অনবদ্য রত্ন। ১৬৫৬ খ্রিষ্টাব্দে মোঘল সুবেদার শাহ সুজার শাসনামলে মালিক নেয়ামতউল্লাহ এই ঐতিহাসিক তিন গম্বুজবিশিষ্ট মসজিদটি নির্মাণ করেন। মসজিদের প্রবেশদ্বার ও দেয়ালগুলোতে পোড়ামাটির চমৎকার লতাপাতা ও জ্যামিতিক নকশার কারুকাজ রয়েছে। চার কোণে অষ্টভুজাকৃতির মিনার ও মাঝের প্রধান খিলানের ওপর ফার্সি শিলালিপি এর ঐতিহাসিক গুরুত্ব তুলে ধরে। শান্ত গ্রামীণ পরিবেশে দাঁড়িয়ে থাকা এই শৈল্পিক মসজিদ দর্শনার্থীদের মুগ্ধ করে।",
            "locationEn": "Mirzapur, Atwari",
            "locationBn": "মির্জাপুর, আটোয়ারী",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Mirzapur%20Shahi%20Mosque%2C%20Mirzapur%2C%20Atwari"
        },
        {
            "id": 3,
            "nameEn": "Bodeshwari Temple",
            "nameBn": "বোদেশ্বরী মহাপীঠ মন্দির",
            "categoryEn": "Ancient Hindu Pilgrimage Temple & Shakti Peeth",
            "categoryBn": "সুপ্রাচীন ঐতিহাসিক হিন্দু দেবালয় ও সতীপীঠ",
            "descEn": "The Bodeshwari Temple (also known as Bodeshwari Shakti Peeth), situated along the banks of the sacred Korotoa River in Boda Upazila, is an ancient religious shrine venerated across South Asia. According to Hindu mythology, the left breast ('Pinda') of Goddess Sati fell at this holy site, making it a sacred Shakti Peeth. The current heritage temple complex retains ancient carved stone bases, sacred stone idols, and traditional terracotta motifs dating back to the Pala and Sena epochs. An annual fair (Mela) during Maha Shivaratri and Durga Puja attracts thousands of devotees who offer oblations in the holy waters of the Korotoa.",
            "descBn": "বোদা উপজেলায় করতোয়া নদীর তীরে অবস্থিত সুপ্রাচীন বোদেশ্বরী মন্দির সনাতন ধর্মাবলম্বীদের এক অন্যতম মহাপীঠ। পৌরাণিক বিশ্বাস অনুসারে সতীর দেহের বাম স্তন বা পিণ্ড এখানে পতিত হয়েছিল, যার কারণে এই স্থানটি বোদেশ্বরী শক্তিপীঠ হিসেবে খ্যাত। এই মন্দিরের প্রাচীন পাথরের বেদি, টেরাকোটা ফলক ও দেবীমূর্তি পাল ও সেন যুগের প্রাচীন ধর্মীয় স্থাপত্যের সাক্ষ্য বহন করে। মহাশিবরাত্রি ও শারদীয় দুর্গাপূজার সময় এখানে বিশাল মেলার আয়োজন হয় এবং দূর-দূরান্ত থেকে পুণ্যার্থীরা এখানে প্রার্থনায় সমবেত হন।",
            "locationEn": "Boda, Panchagarh",
            "locationBn": "বোদা, পঞ্চগড়",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Bodeshwari%20Temple%2C%20Boda%2C%20Panchagarh"
        },
        {
            "id": 4,
            "nameEn": "Banglabandha Zero Point",
            "nameBn": "বাংলাবান্ধা জিরো পয়েন্ট",
            "categoryEn": "International Four-Nation Border Crossing",
            "categoryBn": "আন্তর্জাতিক চতুর্দেশীয় সীমান্ত জিরো পয়েন্ট",
            "descEn": "Banglabandha Zero Point, situated at the apex of Tetulia Upazila, is the northernmost geographic coordinate of Bangladesh. This strategic border landmark lies directly adjacent to Phulbari in West Bengal, India, and serves as an international multi-nation commercial gateway providing direct transit links to Nepal (via the Kakarbhitta corridor, just 61 km away) and Bhutan (via Jaigaon, 68 km away). Visitors can stand before the iconic boundary pillars under the supervision of Border Guard Bangladesh (BGB), observe joint retreat ceremonies, and marvel at the Himalayan mountain breezes that drift across this international geopolitical crossroad.",
            "descBn": "তেঁতুলিয়া উপজেলার সর্বউত্তরে অবস্থিত বাংলাবান্ধা জিরো পয়েন্ট বাংলাদেশের সবচেয়ে উত্তরের সীমান্তবিন্দু। এটি কেবল ভারত নয়, নিকটবর্তী নেপাল ও ভুটানের সাথে আন্তর্জাতিক ব্যবসা-বাণিজ্য ও ট্রানজিটের এক অনন্য চতুর্দেশীয় কেন্দ্র। বিজিবির তত্ত্বাবধানে এখানে অবস্থিত ঐতিহাসিক সীমান্ত পিলার, আন্তর্জাতিক ট্রানজিট টার্মিনাল এবং প্রতিদিনের জমকালো সীমান্ত অভিবাদন অনুষ্ঠান পর্যটকদের দারুণভাবে আকর্ষণ করে। হিমালয়ের অতি সন্নিকটে অবস্থিত এই সীমান্ত পয়েন্টে দাঁড়ালে এক অদ্ভুত রোমাঞ্চকর অনুভূতি অনুভূত হয়।",
            "locationEn": "Tetulia; border access rules apply",
            "locationBn": "বাংলাবান্ধা, তেঁতুলিয়া",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Banglabandha%20Zero%20Point%2C%20Tetulia%3B%20border%20access%20rules%20apply"
        },
        {
            "id": 5,
            "nameEn": "Panchagarh old railway station area",
            "nameBn": "পঞ্চগড় পুরাতন রেলওয়ে স্টেশন এলাকা",
            "categoryEn": "Historic British Frontier Railway Heritage",
            "categoryBn": "ব্রিটিশ আমলের ঐতিহাসিক রেলওয়ে স্টেশন এলাকা",
            "descEn": "The Old Railway Station area in Panchagarh town is a heritage site reflecting the northern expansion of the British railway grid during the early 20th century. Established as a vital terminus for transporting agricultural crops, timber, and Himalayan stone boulders, the precinct preserves vintage brick platform sheds, manual iron lever switching equipment, and colonial railway bungalows shaded by centenarian banyan trees. In recent decades, modern broad-gauge tracks and express passenger trains have transformed connectivity, yet the nostalgic old railway grounds remain a beloved historic gathering space for local residents.",
            "descBn": "পঞ্চগড় শহরের প্রাণকেন্দ্রে অবস্থিত পুরাতন রেলওয়ে স্টেশন এলাকা উত্তরবঙ্গের রেল যোগাযোগের শতবর্ষী ইতিহাসের এক নীরব সাক্ষী। ব্রিটিশ আমলে হিমালয়ের পাদদেশ থেকে কাঠ, পাথর ও কৃষিপণ্য পরিবহনের জন্য এই রেলপথ স্থাপন করা হয়েছিল। এখানকার লাল ইটের প্রাচীন প্ল্যাটফর্ম, হস্তচালিত রেলের সিগন্যাল ও চুন-সুরকির পুরনো ভবনগুলো অতীতের স্মৃতি জাগিয়ে তোলে। বর্তমানে আধুনিক ব্রডগেজ ট্রেন চালু হলেও এই পুরাতন স্টেশন চত্বরটি ইতিহাসপ্রেমীদের কাছে অত্যন্ত প্রিয় ও স্মৃতিবিজড়িত।",
            "locationEn": "Panchagarh town",
            "locationBn": "পঞ্চগড় শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Panchagarh%20old%20railway%20station%20area%2C%20Panchagarh%20town"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Tetulia Dak Bungalow",
            "nameBn": "তেঁতুলিয়া ডাকবাংলো ও পিকনিক কর্নার",
            "categoryEn": "Historic Colonial Hilltop Viewpoint",
            "categoryBn": "ঐতিহাসিক পাহাড়ি ডাকবাংলো ও মহানন্দা ভিউপয়েন্ট",
            "descEn": "Perched on a high bluff overlooking the sparkling waters of the Mahananda River, the Tetulia Dak Bungalow is the premier scenic viewpoint in northern Bangladesh. Built during the British colonial period by the Raja of Dighapatia, the stone bungalow features wide wooden verandas and expansive manicured gardens overlooking the river gorge below and the rolling green tea hills of India directly across the international border. It is world-renowned as the primary observation terrace where visitors gather during autumn mornings to watch the snow-capped peak of Mount Kanchenjunga blush golden against the northern sky.",
            "descBn": "মহানন্দা নদীর সুউচ্চ তীরে পাহাড়ের মতো টিলার ওপর অবস্থিত ঐতিহাসিক তেঁতুলিয়া ডাকবাংলো পঞ্চগড়ের প্রধান পর্যটন আকর্ষণ। ব্রিটিশ আমলে দিঘাপতিয়ার রাজা এই চমৎকার বাংলোটি নির্মাণ করেছিলেন। এর প্রশস্ত বারান্দা ও ফুলের বাগান থেকে নিচে মহানন্দা নদী এবং ঠিক ওপারে ভারতের চা বাগান ও কাঁটাতারের মনোরম দৃশ্য দেখা যায়। বিশেষ করে শরৎ ও হেমন্তের সকালে এখান থেকেই খালি চোখে দেখা মেলে হিমালয়ের বরফশুভ্র কাঞ্চনজঙ্ঘা পর্বতশৃঙ্গের সোনালী রূপ, যা হাজার হাজার পর্যটককে সম্মোহিত করে।",
            "locationEn": "Tetulia, Panchagarh",
            "locationBn": "তেঁতুলিয়া, পঞ্চগড়",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Tetulia%20Dak%20Bungalow%2C%20Tetulia%2C%20Panchagarh"
        },
        {
            "id": 2,
            "nameEn": "Mahananda Riverbank",
            "nameBn": "মহানন্দা নদী তীর ও পাথুরে ঘাট",
            "categoryEn": "Himalayan Riverbank & Stone Harvesting",
            "categoryBn": "স্বচ্ছ হিমালয়ান নদী ও পাথর তোলার দৃশ্য",
            "descEn": "The Mahananda River along Tetulia is an enchanting transboundary watercourse originating directly in the Himalayas. Flowing over shallow beds of glittering quartzite stones and smooth round boulders, its waters are famously crystal-clear, reflecting blue skies and forested banks. Visitors walk along the sandy riverbanks, wade into the cool refreshing shallows, and watch local laborers and divers skillfully extract high-grade construction stones from the riverbed using wooden skiffs. The gentle sound of trickling water and distant mountain vistas create an unforgettable sensory experience.",
            "descBn": "তেঁতুলিয়ার বুক চিরে প্রবাহিত মহানন্দা নদী সরাসরি হিমালয় থেকে নেমে আসা এক পাহাড়ি নদী। নদীর তলদেশ নুড়িপাথর ও স্ফটিকস্বচ্ছ জলে ভরা, যার ওপর দিয়ে হেঁটে যাওয়া এক অসাধারণ রোমাঞ্চকর অনুভূতি। স্থানীয় শ্রমিকদের নদীতে নেমে সনাতন পদ্ধতিতে পাথর তোলার কর্মচাঞ্চল্য এবং ওপারে ভারতের পাহাড়ের দৃশ্য পর্যটকদের মুগ্ধ করে। নদীর পাড়ে বসে হিমশীতল জলের স্পর্শ নেওয়া এবং প্রকৃতির সাথে একাত্ম হওয়া যে কোনো ভ্রমণপিপাসুর মনকে সতেজ করে তোলে।",
            "locationEn": "Tetulia, Panchagarh",
            "locationBn": "তেঁতুলিয়া, পঞ্চগড়",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Mahananda%20Riverbank%2C%20Tetulia%2C%20Panchagarh"
        },
        {
            "id": 3,
            "nameEn": "Banglabandha land port viewpoint",
            "nameBn": "বাংলাবান্ধা স্থলবন্দর ভিউপয়েন্ট",
            "categoryEn": "Strategic International Frontier Port Observation",
            "categoryBn": "আন্তর্জাতিক স্থলবন্দর ও সীমান্ত দৃশ্য",
            "descEn": "The Banglabandha Land Port viewpoint provides a fascinating vantage point over the only quadrilateral international commercial artery of Bangladesh. The viewpoint overlooks the busy customs terminal where colorful multi-ton freight transports cross between Bangladesh and India loaded with agricultural goods, stone boulders, and industrial merchandise bound for Bhutan and Nepal. Modern tourist galleries and border observation pavilions allow travelers to view the synchronized operations, international border fencing, and pristine Himalayan foothill horizons stretching into neighboring Siliguri and Darjeeling.",
            "descBn": "বাংলাবান্ধা স্থলবন্দর ভিউপয়েন্ট থেকে সরাসরি প্রত্যক্ষ করা যায় বাংলাদেশ, ভারত, নেপাল ও ভুটানের আন্তর্জাতিক বাণিজ্যিক কার্যক্রম। প্রতিদিন শত শত পণ্যবাহী ট্রাক, কাস্টমস ইয়ার্ড এবং আধুনিক সীমান্ত টার্মিনালের ব্যস্ততা এখান থেকে উপভোগ করা যায়। পর্যটকদের সুবিধার জন্য এখানে তৈরি করা হয়েছে দৃষ্টিনন্দন বসার স্থান ও পর্যবেক্ষণ পয়েন্ট, যেখান থেকে ওপারে ভারতের ফুলবাড়ী সীমান্ত এবং দূর পাহাড়ের সবুজ বনানী সুস্পষ্ট দেখা যায়।",
            "locationEn": "Tetulia; follow border restrictions",
            "locationBn": "বাংলাবান্ধা, তেঁতুলিয়া",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Banglabandha%20land%20port%20viewpoint%2C%20Tetulia%3B%20follow%20border%20restrictions"
        },
        {
            "id": 4,
            "nameEn": "Tea gardens of Tetulia",
            "nameBn": "তেঁতুলিয়ার সমতল চা বাগান",
            "categoryEn": "Expansive Flatland Organic Tea Plantations",
            "categoryBn": "সমতলের দৃষ্টিনন্দন সবুজ চা বাগান",
            "descEn": "The tea gardens of Tetulia represent an extraordinary agricultural revolution in Bangladesh. Unlike traditional sloping tea estates of Sylhet and Chittagong, Panchagarh pioneered flatland tea cultivation starting in 2000, now blanketing thousands of hectares in emerald-green carpeted bushes. Prominent estates like Kazi & Kazi Tea Estate produce world-class certified organic tea. Visitors can stroll through manicured tea avenues, watch skilled tea pluckers filling their cane baskets, photograph geometric rows of green foliage, and sample steaming cups of freshly brewed aromatic organic green and black tea at open-air garden cafes.",
            "descBn": "তেঁতুলিয়ার সমতল ভূমিতে গড়ে ওঠা চা বাগান বাংলাদেশের কৃষি বিপ্লবের এক অনন্য রূপকথা। সিলেট বা চট্টগ্রামের মতো পাহাড়ে নয়, বরং সমতল ভূমিতে দিগন্তজোড়া সবুজ কার্পেটের মতো বিছানো এই চা বাগানগুলো যেন এক সবুজ স্বর্গ। কাজী অ্যান্ড কাজী টি এস্টেটসহ বহু নামকরা অর্গানিক চা বাগান এখানে রয়েছে। চা বাগানের মাঝের সরু রাস্তা ধরে হাঁটা, চা শ্রমিকদের পাতা তোলার দৃশ্য ক্যামেরাবন্দি করা এবং বাগান সংলগ্ন ক্যাফেতে বসে সদ্য প্রস্তুত সুগন্ধি চায়ে চুমুক দেওয়া পঞ্চগড় ভ্রমণের প্রধান আকর্ষণ।",
            "locationEn": "Tetulia, Panchagarh",
            "locationBn": "তেঁতুলিয়া, পঞ্চগড়",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Tea%20gardens%20of%20Tetulia%2C%20Tetulia%2C%20Panchagarh"
        },
        {
            "id": 5,
            "nameEn": "Kanchanjangha viewpoint area",
            "nameBn": "কাঞ্চনজঙ্ঘা ভিউপয়েন্ট এলাকা (তেঁতুলিয়া)",
            "categoryEn": "Himalayan Snow-Peak Observation Sanctuary",
            "categoryBn": "কাঞ্চনজঙ্ঘা পর্বত দর্শনের প্রধান ভিউপয়েন্ট",
            "descEn": "The Kanchanjangha viewpoint areas around Tetulia—stretching from the Dak Bungalow to the banks of the Mahananda and open tea terraces—are celebrated across South Asia as the ultimate vantage point to witness Mount Kanchenjunga without leaving Bangladesh. During the clear, pollution-free autumn and early winter months from October to December, the snow-covered massif of the world's third highest mountain (8,586 meters) looms majestic on the northern horizon. In early dawn, the snowy crags shimmer pink and fiery orange under the morning sun, casting an unforgettable magical spell over tens of thousands of travelers who assemble to witness nature’s grandest spectacle.",
            "descBn": "তেঁতুলিয়া উপজেলার ডাকবাংলো, নদী তীর এবং বিস্তীর্ণ খোলা মাঠই হলো কাঞ্চনজঙ্ঘা পর্বত দর্শনের প্রধান ভিউপয়েন্ট। প্রতি বছর অক্টোবর থেকে ডিসেম্বর মাসে আকাশ মেঘমুক্ত ও কুয়াশাহীন হলে উত্তর আকাশে স্পষ্ট ভেসে ওঠে বরফে ঢাকা কাঞ্চনজঙ্ঘা শৃঙ্গ। ভোরের সোনালী রোদ যখন বরফের চূড়ায় পড়ে, তখন এটি লালচে-কমলা ও হীরার মতো জ্বলজ্বল করে ওঠে, যা দেখে মনে হয় আকাশেই যেন এক রূপালী স্বপ্ন ঝুলে আছে। প্রকৃতির এই রাজকীয় রূপ দর্শন করতে দেশ-বিদেশের লাখো পর্যটক পঞ্চগড়ে ভিড় জমান।",
            "locationEn": "Tetulia; visibility depends on weather",
            "locationBn": "তেঁতুলিয়া ভিউপয়েন্ট, পঞ্চগড়",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kanchanjangha%20viewpoint%20area%2C%20Tetulia%3B%20visibility%20depends%20on%20weather"
        }
    ]
}

# Output individual python data files
districts = [lalmonirhat, nilphamari, thakurgaon, panchagarh]

for d in districts:
    fname = f"scripts/data_districts_17/{d['slug']}.py"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write(f"data = {json.dumps(d, ensure_ascii=False, indent=4)}\n")
    print(f"Wrote {fname}")

print("Batch 14 to 17 complete!")
