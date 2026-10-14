# -*- coding: utf-8 -*-
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
os.makedirs('scripts/data_districts_17', exist_ok=True)

# 6. JOYPURHAT
joypurhat = {
    "slug": "joypurhat",
    "en": "Joypurhat",
    "bn": "জয়পুরহাট",
    "hero_title_en": "Joypurhat Barind Heritage & Historic Dighis",
    "hero_title_bn": "জয়পুরহাটের বরেন্দ্র ঐতিহ্য ও ঐতিহাসিক দীঘি",
    "hero_sub_en": "Ancient Hinda-Kasba Shahi Mosque, Lokma Rajbari ruins, and vast historical freshwater reservoirs.",
    "hero_sub_bn": "হিন্দা-কসবা শাহী মসজিদ, প্রাচীন লকমা রাজবাড়ি ও বরেন্দ্রভূমির ঐতিহ্যবাহী বিশাল দিঘি।",
    "tagline_en": "The compact agricultural and archaeological jewel of the northern Barind tract, celebrated for exquisite Mughal-style architecture, centuries-old royal palaces at Panchbibi, and legendary freshwater dighis.",
    "tagline_bn": "উত্তরবঙ্গের বরেন্দ্র অঞ্চলের এক নিবিড় ও ঐতিহ্যমণ্ডিত প্রত্নতাত্ত্বিক জেলা, যা হিন্দা-কসবা মসজিদ, পাঁচবিবির প্রাচীন রাজপ্রাসাদ এবং ঐতিহাসিক দিঘির জন্য সুপরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/joypurhat/carousel-1.webp",
            "titleEn": "Hinda-Kasba Shahi Mosque Ceramic Artistry",
            "titleBn": "হিন্দা-কসবা শাহী মসজিদের অনন্য নির্মাণশৈলী",
            "subtitleEn": "Magnificent Mughal-style mosque in Khetlal adorned with colorful glass mosaic chinikotuk craftsmanship",
            "subtitleBn": "ক্ষেতলালে অবস্থিত চোখজুড়ানো মুঘল স্থাপত্যরীতির মসজিদ, যার কাচ ও চিনামাটির অলংকরণ এক অনন্য শিল্পকীর্তি"
        },
        {
            "id": 2,
            "image": "images/districts/joypurhat/carousel-2.webp",
            "titleEn": "Lokma Rajbari Historic Aristocratic Gateway",
            "titleBn": "লকমা রাজবাড়ির প্রাচীন রাজতোরণ",
            "subtitleEn": "Weathered centuries-old royal zamindari palace in Panchbibi reflecting feudal majesty",
            "subtitleBn": "পাঁচবিবিতে অবস্থিত শতবর্ষী জমিদার প্রাসাদ, যার খিলান ও প্রাচীন স্তম্ভ সোনালী অতীতের সাক্ষ্য দেয়"
        },
        {
            "id": 3,
            "image": "images/districts/joypurhat/carousel-3.webp",
            "titleEn": "Asranga Dighi Legendary Freshwater Waterway",
            "titleBn": "ঐতিহাসিক আছরঙ্গা দীঘির রূপময় জলরাশি",
            "subtitleEn": "Massive medieval freshwater reservoir dug in Khetlal enveloped by tranquil village groves and migratory birdlife",
            "subtitleBn": "ক্ষেতলাল উপজেলার প্রাচীনতম বিশাল দীঘি, যার স্বচ্ছ জলরাশি ও পাড়ের স্নিগ্ধ পল্লী পরিবেশ মন জুড়িয়ে দেয়"
        },
        {
            "id": 4,
            "image": "images/districts/joypurhat/carousel-4.webp",
            "titleEn": "Nandail Dighi Vast Water Expanse",
            "titleBn": "নান্দাইল দীঘির দিগন্তবিস্তৃত নিসর্গ",
            "subtitleEn": "Historic Barind dighi famous for winter migratory waterfowl and tranquil waterside sunsets",
            "subtitleBn": "জয়পুরহাটের সুবিশাল ঐতিহাসিক জলাশয়, যেখানে শীতকালে অতিথি পাখির মেলা ও মনমাতানো সূর্যাস্ত দেখা যায়"
        },
        {
            "id": 5,
            "image": "images/districts/joypurhat/carousel-5.webp",
            "titleEn": "Little Jamuna Riverbank Rural Panorama",
            "titleBn": "ছোট যমুনা নদীতীরের শান্ত মেঠোপথ",
            "subtitleEn": "Quiet river corridor meandering through green fertile paddy plains and traditional pottery hamlets",
            "subtitleBn": "সবুজ শস্যক্ষেতের বুক চিরে বয়ে চলা ছোট যমুনা নদী, যার স্নিগ্ধ বাতাস ভ্রমণকারীদের প্রশান্তি জোগায়"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Hinda-Kasba Shahi Mosque",
            "nameBn": "হিন্দা-কসবা শাহী জামে মসজিদ",
            "categoryEn": "Mughal-Revival Ceramic Masterpiece",
            "categoryBn": "মুঘল রীতির অপূর্ব চিনিটিকরি ও কাচশিল্পের মসজিদ",
            "descEn": "Hinda-Kasba Shahi Mosque at Khetlal is widely celebrated as one of the most visually stunning Islamic monuments in northern Bangladesh. Designed in 1958 by master architect Abdul Gafur Chishti, this architectural jewel draws direct inspiration from imperial Mughal aesthetics, featuring five graceful bulbous domes, four slender corner minarets, and delicate scalloped arches. The entire exterior and interior facades are intricately embellished with thousands of multicolored ceramic porcelain fragments, cut glass, and terracotta floral rosettes. The central prayer hall accommodates hundreds of devotees under a glowing dome decorated with Arabic calligraphy. Visitors and architecture enthusiasts marvel at the harmony of Islamic devotion and exquisite ceramic mosaic craftsmanship.",
            "descBn": "জয়পুরহাটের ক্ষেতলাল উপজেলার হিন্দা গ্রামে অবস্থিত হিন্দা-কসবা শাহী জামে মসজিদ উত্তরবঙ্গের অন্যতম দৃষ্টিনন্দন আধুনিক-মুঘল স্থাপত্যের নিদর্শন। ১৯৫৮ সালে হজরত আবদুল গফুর চিশতী (রহ.) কর্তৃক নকশাকৃত এই মসজিদটির পাঁচটি সুদৃশ্য গম্বুজ ও চারটি আকাশচুম্বী মিনার বহুদূর থেকে নজর কাড়ে। এর দেওয়াল, মেহরাব ও গম্বুজে হাজার হাজার রঙিন চীনা মাটির টুকরা ও কাচ কেটে তৈরি করা হয়েছে অসাধারণ সব ফুল-লতাপাতার নকশা। মসজিদের ভেতরের প্রশান্ত পরিবেশ ও অপূর্ব আলোকসজ্জা ভক্তদের আত্মিক শান্তি এনে দেয়। নির্মাণশৈলীর অনন্য সৌন্দর্যের কারণে প্রতিদিন দূর-দূরান্ত থেকে শত শত পর্যটক এটি দেখতে আসেন।",
            "locationEn": "Khetlal, Joypurhat",
            "locationBn": "ক্ষেতলাল, জয়পুরহাট",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Hinda-Kasba%20Shahi%20Mosque%2C%20Khetlal%2C%20Joypurhat"
        },
        {
            "id": 2,
            "nameEn": "Lokma Rajbari",
            "nameBn": "লকমা রাজবাড়ি",
            "categoryEn": "Historic Feudal Aristocratic Palace",
            "categoryBn": "অষ্টাদশ শতকের জমিদার প্রাসাদ ও নাচঘর",
            "descEn": "Lokma Rajbari in Panchbibi Upazila is a magnificent eighteenth-century feudal palace complex constructed during the zenith of the local zamindari aristocracy. The estate comprises grand two-story residential wings, vaulted audience chambers, an elaborate dance hall (Nachghar), and a secure brick treasury vault. European neoclassical influences are clearly visible in the Corinthian columns, decorative plaster pediments, and arched verandas framing the central courtyards. Despite centuries of exposure to tropical weather, the weathered red-brick walls and ornate gateways still project an undeniable aura of feudal prestige and historic romance. It remains one of Joypurhat's premier archaeological attractions for photography and historical exploration.",
            "descBn": "জয়পুরহাটের পাঁচবিবি উপজেলায় ভারত সীমান্তবর্তী এলাকায় অবস্থিত লকমা রাজবাড়ি অষ্টাদশ শতাব্দীর এক সমৃদ্ধ জমিদারি প্রাসাদ। তৎকালীন প্রভাবশালী জমিদার ঈশ্বরচন্দ্র রায় ও তাঁর উত্তরসূরিদের প্রতিষ্ঠিত এই রাজবাড়িতে রয়েছে শতবর্ষী নাটমন্দির, জলসাঘর, খাজাঞ্চিখানা এবং অন্দরমহলের সুরম্য কক্ষসমূহ। ইউরোপীয় নির্মাণশৈলীর করিন্থিয়ান থাম ও দেশীয় চুন-সুরকির সমন্বয়ে নির্মিত এই প্রাসাদটি অত্যন্ত আভিজাত্যপূর্ণ। কালের পরিক্রমায় কিছুটা জরাজীর্ণ হলেও এর বিশাল খিলান ও কারুকার্যময় প্রবেশদ্বার এখনো রাজকীয় অহংকার প্রকাশ করে। ইতিহাসপ্রেমী পর্যটকদের কাছে এটি এক অত্যন্ত রোমাঞ্চকর স্থান।",
            "locationEn": "Panchbibi, Joypurhat",
            "locationBn": "পাঁচবিবি, জয়পুরহাট",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Lokma%20Rajbari%2C%20Panchbibi%2C%20Joypurhat"
        },
        {
            "id": 3,
            "nameEn": "Asranga Dighi",
            "nameBn": "আছরঙ্গা দীঘি",
            "categoryEn": "Immense Medieval Freshwater Reservoir",
            "categoryBn": "নবম শতাব্দীর ঐতিহাসিক মহা দীঘি",
            "descEn": "Asranga Dighi in Khetlal Upazila is an immense medieval freshwater lake covering an area of nearly 25 acres, excavated during the rule of King Tahirpal in the ninth century AD. Surrounded by high earthen defensive dykes shaded by ancient banyan and mahogany groves, the dighi provided clean drinking water and irrigation to ancient Barind settlements. Local folklore abounds with mystical legends regarding hidden treasure chests and saintly blessings associated with its crystal-clear depths. During the winter season, thousands of migratory waterfowl feed on its calm waters, transforming the lake into a thriving bird sanctuary. It stands as an enduring monument to medieval hydraulic engineering and communal welfare in northern Bengal.",
            "descBn": "ক্ষেতলাল উপজেলার মামুদপুর ইউনিয়নে অবস্থিত আছরঙ্গা দীঘি বরেন্দ্র অঞ্চলের অন্যতম বৃহৎ ও প্রাচীন ঐতিহাসিক জলাধার। নবম শতাব্দীর দিকে রাজা তাহিরপাল স্থানীয় প্রজাদের পানীয় জলের সংকট দূর করতে প্রায় ২৫ একর আয়তনের এই বিশাল দীঘিটি খনন করেন। দীঘির চারপাশের উঁচু সবুজ পাড় ও প্রাচীন বৃক্ষরাজি এক অপরূপ নিসর্গের সৃষ্টি করেছে। স্থানীয়দের মাঝে এই দীঘিকে কেন্দ্র করে বহু রূপকথা ও অলৌকিক কাহিনী প্রচলিত রয়েছে। শীতকালে অতিথি পাখির কলতানে মুখরিত এই দীঘিপাড়ে বসে মুক্ত বাতাস উপভোগ করা এক পরম প্রশান্তির অভিজ্ঞতা।",
            "locationEn": "Khetlal, Joypurhat",
            "locationBn": "ক্ষেতলাল, জয়পুরহাট",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Asranga%20Dighi%2C%20Khetlal%2C%20Joypurhat"
        },
        {
            "id": 4,
            "nameEn": "Belamla historic temple",
            "nameBn": "বেলআমলা ঐতিহাসিক বারোশিব মন্দির",
            "categoryEn": "Ancient Shiva Temple Ensemble",
            "categoryBn": "প্রাচীন দ্বাদশ শিব মন্দির ও পোড়ামাটির স্থাপত্য",
            "descEn": "The Belamla historic temple complex in Joypurhat Sadar is a sacred Hindu heritage sanctuary centered on an interconnected cluster of historic Shiva shrines. Built centuries ago along the banks of the Little Jamuna River, the temples feature traditional Bengali Chala roofs, ornate stone lingams, and terracotta exterior bands. Devotees gather in large numbers during Shivaratri and annual fairs to offer milk and holy river water at the sanctum shrines. Shaded by ancient sacred bilva (wood-apple) and neem trees, the quiet courtyard preserves a timeless atmosphere of meditative tranquility. It is treasured as an irreplaceable religious landmark anchoring the spiritual heritage of Joypurhat.",
            "descBn": "জয়পুরহাট সদর উপজেলার বেলআমলায় ছোট যমুনা নদীর তীরে অবস্থিত প্রাচীন বারোশিব মন্দির হিন্দু স্থাপত্য ও ভক্তির এক অনন্য স্মারক। বহু শতাব্দী পূর্বে স্থানীয় ভক্ত ও রাজাদের পৃষ্ঠপোষকতায় নির্মিত এই মন্দিরগুলোতে রয়েছে ঐতিহ্যবাহী শিবলিঙ্গ এবং প্রাচীন পোড়ামাটির কারুকাজ। শিবরাত্রি ও বিভিন্ন ধর্মীয় তিথিতে এখানে দূর-দূরান্ত থেকে ভক্তরা পুণ্য অর্জনে আসেন। প্রাচীন বেল ও বটবৃক্ষের শীতল ছায়ায় ঘেরা এই মন্দির প্রাঙ্গণ এক শান্ত ও পবিত্র পরিবেশ উপহার দেয়। প্রত্নতাত্ত্বিক ও আধ্যাত্মিক উভয় দিক থেকেই বেলআমলার এই মন্দির চত্বর অত্যন্ত তাৎপর্যপূর্ণ।",
            "locationEn": "Joypurhat Sadar",
            "locationBn": "জয়পুরহাট সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Belamla%20historic%20temple%2C%20Joypurhat%20Sadar"
        },
        {
            "id": 5,
            "nameEn": "Patharghata archaeological site",
            "nameBn": "পাথরঘাটা প্রত্নতাত্ত্বিক এলাকা",
            "categoryEn": "Pala-Era Stone Citadel Excavations",
            "categoryBn": "পাল ও সেন যুগের প্রাচীন পাথুরে প্রত্নস্থল",
            "descEn": "The Patharghata archaeological site in Panchbibi Upazila represents the remnants of an ancient riverine stone settlement and trading fortress dating from the Pala and Sena dynasties. Excavations along the Tulshiganga river basin have uncovered carved black stone door jambs, stone lintels, decorative terracotta bricks, and ancient coins. Historians suggest Patharghata functioned as an important customs terminal and religious pilgrimage river ghat connecting northern Bengal with eastern India. The elevated mounds and exposed ancient masonry continue to yield clues about medieval urban planning and inland river transport. It is a captivating destination for history buffs seeking the deep antiquity of the Barind tract.",
            "descBn": "পাঁচবিবি উপজেলায় তুলসীগঙ্গা নদীর তীরে অবস্থিত পাথরঘাটা এক সুপ্রাচীন প্রত্নতাত্ত্বিক স্থান, যা পাল ও সেন যুগের সমৃদ্ধ নদী বন্দর ও জনপদের পরিচয় বহন করে। এখানে খননকালে আবিষ্কৃত হয়েছে প্রাচীন কালো পাথরের স্তম্ভ, খোদাই করা দরজার চৌকাঠ, পোড়ামাটির ফলক এবং প্রাচীন মুদ্রা। ইতিহাসবিদদের মতে, এই অঞ্চলটি নদীপথে ব্যবসা-বাণিজ্য ও শুল্ক আদায়ের এক প্রধান কৌশলগত কেন্দ্র ছিল। নদীর বাঁকে অবস্থিত প্রাচীন ধ্বংসাবশেষ ও পাথুরে নিদর্শনসমূহ উত্তরবঙ্গের প্রাচীন সভ্যতার এক অনন্য দলিল। প্রত্নতত্ত্বপ্রেমীদের কাছে এটি অত্যন্ত রোমাঞ্চকর এক অনুসন্ধানস্থল।",
            "locationEn": "Panchbibi, Joypurhat",
            "locationBn": "পাঁচবিবি, জয়পুরহাট",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Patharghata%20archaeological%20site%2C%20Panchbibi%2C%20Joypurhat"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Nandail Dighi",
            "nameBn": "নান্দাইল দীঘি",
            "categoryEn": "Massive Scenic Freshwater Lake & Bird Sanctuary",
            "categoryBn": "বিশাল প্রাকৃতিক জলাশয় ও পরিযায়ী পাখির স্বর্গরাজ্য",
            "descEn": "Nandail Dighi is a magnificent historical freshwater reservoir spanning over 50 acres, celebrated as one of the largest and most picturesque lakes in northern Bangladesh. Originally excavated in the seventeenth century by local chieftains to ensure year-round water supply, the dighi is surrounded by towering eucalyptus and rain trees. In the winter months, the calm water surface attracts thousands of migratory ducks, herons, and cormorants, filling the crisp morning air with bird songs. Paved lakeside walkways and grassy banks offer ideal settings for family picnics, peaceful angling, and panoramic sunset photography. It provides an exceptional open-air eco-tourism escape in Joypurhat.",
            "descBn": "জয়পুরহাট জেলার কালাই উপজেলায় অবস্থিত নান্দাইল দীঘি প্রায় ৫০ একর এলাকা জুড়ে বিস্তৃত এক বিশাল ও অপরূপ প্রাকৃতিক জলাশয়। সপ্তদশ শতাব্দীতে খনন করা এই সুবিশাল দীঘির চারপাশ উঁচু সবুজ পাড় ও ছায়াঘেরা গাছে ঘেরা। শীতের মৌসুমে সুদূর সাইবেরিয়া ও হিমালয় অঞ্চল থেকে আসা হাজার হাজার অতিথি পাখির কলকাকলিতে দীঘিটি মুখরিত হয়ে ওঠে। শান্ত জলরাশির বুকে নৌভ্রমণ এবং পাড়ে বসে স্নিগ্ধ বাতাসে সময় কাটানো পর্যটকদের দারুণ আনন্দ দেয়। পরিবার-পরিজন নিয়ে পিকনিক ও পাখি দেখার জন্য নান্দাইল দীঘি এক আদর্শ পর্যটন কেন্দ্র।",
            "locationEn": "Joypurhat district; verify location",
            "locationBn": "কালাই, জয়পুরহাট জেলা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Nandail%20Dighi%2C%20Joypurhat%20district%3B%20verify%20location"
        },
        {
            "id": 2,
            "nameEn": "Jamalgonj archaeological area",
            "nameBn": "জামালগঞ্জ কয়লাখনি ও ঐতিহ্যবাহী এলাকা",
            "categoryEn": "Heritage Industrial Mining & Rail Enclave",
            "categoryBn": "ঐতিহাসিক কয়লাখনি অঞ্চল ও গ্রামীণ নিসর্গ",
            "descEn": "The Jamalgonj area in Akkelpur Upazila holds significant historical distinction as the site of Bangladesh's earliest and deepest underground coal discoveries. The enclave features historic mining observation towers, vintage railway sidings, and tranquil pastoral countryside fringed by the Little Jamuna River. Visitors can tour the heritage railway architecture, explore surrounding brick-making hamlets, and interact with warmhearted local farmers. The wide green vistas and peaceful rural lanes make Jamalgonj a delightful destination for countryside cycling and industrial heritage exploration. It offers a rare perspective on the intersection of modern geological history and traditional Barind life.",
            "descBn": "আক্কেলপুর উপজেলার জামালগঞ্জ বাংলাদেশের ভূতাত্ত্বিক ও কয়লা উত্তোলনের ইতিহাসের এক অত্যন্ত গুরুত্বপূর্ণ অঞ্চল। ১৯৬২ সালে এখানে দেশের অন্যতম গভীরতম কয়লাখনির সন্ধান পাওয়া যায়, যা তৎকালীন শিল্প সম্ভাবনার নতুন দ্বার উন্মোচন করেছিল। ঐতিহাসিক রেলওয়ে স্টেশন, ব্রিটিশ আমলের স্থাপনা এবং চারপাশের সবুজ ফসলি জমি এলাকাটিকে এক চমৎকার গ্রামীণ রূপ দিয়েছে। ছোট যমুনা নদীর কোল ঘেঁষে অবস্থিত এই জনপদে শান্ত মেঠোপথ ধরে সাইক্লিং করা পর্যটকদের কাছে দারুণ উপভোগ্য। শিল্প ইতিহাস ও প্রকৃতির শান্ত রূপের মেলবন্ধন দেখতে জামালগঞ্জ অত্যন্ত কৌতূহলোদ্দীপক।",
            "locationEn": "Jamalgonj, Akkelpur, Joypurhat",
            "locationBn": "জামালগঞ্জ, আক্কেলপুর, জয়পুরহাট",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Jamalgonj%20archaeological%20area%2C%20Jamalgonj%2C%20Akkelpur%2C%20Joypurhat"
        },
        {
            "id": 3,
            "nameEn": "Bhadsa village countryside",
            "nameBn": "ভাদসা গ্রামীণ নিসর্গ",
            "categoryEn": "Pastoral Barind Farmlands & Village Life",
            "categoryBn": "ঐতিহ্যবাহী বরেন্দ্র পল্লি ও শস্যক্ষেতের সৌন্দর্য",
            "descEn": "The Bhadsa village countryside in Joypurhat Sadar showcases the quintessential rustic charm of the fertile Barind plateau. Undulating red-clay soil roads connect idyllic thatched-roof courtyards shaded by dense mango orchards, date palms, and bamboo thickets. Travelers can observe traditional bullock-cart farming practices, organic vegetable harvest fields, and local artisans crafting hand-woven bamboo baskets. The warm hospitality of the villagers and the unhurried pace of pastoral life offer an authentic cultural immersion. Sunset over Bhadsa's golden mustard and paddy expanses is a visual feast for nature lovers.",
            "descBn": "জয়পুরহাট সদরের ভাদসা ইউনিয়নের গ্রামীণ নিসর্গ বরেন্দ্রভূমির লাল মাটির চিরন্তন সৌন্দর্যের এক অপূর্ব রূপ। এখানকার আঁকাবাঁকা মেঠোপথ, সুপারি ও বাঁশঝাড়ের ছায়াঘেরা মাটির ঘর এবং দিগন্তজোড়া ধানক্ষেত মন জুড়িয়ে দেয়। ঋতুভেদে হলুদ সরিষার ক্ষেত কিংবা সবুজ ফসলের ঢেউ এক মায়াবী পরিবেশ তৈরি করে। এখানকার কৃষিজীবী মানুষের সহজ-সরল জীবনযাত্রা ও অকৃত্রিম আতিথেয়তা পর্যটকদের হৃদয় স্পর্শ করে। শহুরে যান্ত্রিকতার বাইরে বাংলার নির্ভেজাল পল্লি প্রকৃতির স্বাদ পেতে ভাদসার গ্রামগুলোতে ভ্রমণ এক পরম শান্তির অভিজ্ঞতা।",
            "locationEn": "Bhadsa, Joypurhat Sadar",
            "locationBn": "ভাদসা, জয়পুরহাট সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Bhadsa%20village%20countryside%2C%20Bhadsa%2C%20Joypurhat%20Sadar"
        },
        {
            "id": 4,
            "nameEn": "Little Jamuna Riverbank",
            "nameBn": "ছোট যমুনা নদীতীর",
            "categoryEn": "Tranquil Freshwater Riverfront & Sandbanks",
            "categoryBn": "স্নিগ্ধ ছোট যমুনা নদীতীর ও চরাঞ্চল",
            "descEn": "The Little Jamuna Riverbank in Joypurhat is an enchanting freshwater stream that meanders gently across the northern plains before joining the Atrai system. During the monsoon, the river flows briskly, providing life-giving waters to surrounding paddy terraces, while dry winter months expose scenic silver sandbars. Visitors can take peaceful walks along the riverbank embankments, watching local boatmen paddle wooden skiffs against warm evening horizons. The soothing sound of gentle water currents and cool breezes under riverside willow trees create an idyllic haven for relaxation and landscape photography. It reflects the pure serenity of riverine life in the northern districts.",
            "descBn": "জয়পুরহাটের প্রধান প্রাকৃতিক নদী ছোট যমুনার তীর এক স্নিগ্ধ ও মনোরম প্রাকৃতিক ভ্রমণস্থল। এই নদীটি জেলার বিভিন্ন উপজেলার ওপর দিয়ে বয়ে গিয়ে বরেন্দ্রভূমির কৃষিতে প্রাণ সঞ্চার করেছে। নদীর শান্ত জলে ভেসে চলা ছোট ছোট ডিঙি নৌকা এবং তীরের কাশবন এক অসাধারণ রূপ ধারণ করে। বিকেলে নদীপাড়ের বাঁধের ওপর বসে মুক্ত বাতাস উপভোগ করতে স্থানীয় বাসিন্দারা ও ভ্রমণকারীরা সমবেত হন। সূর্যাস্তের সময় নদীর জলে আলোর ঝলকানি এবং জেলেদের জাল ফেলার দৃশ্য যে কোনো প্রকৃতিপ্রেমীর মনকে প্রশান্ত করে তোলে।",
            "locationEn": "Joypurhat district",
            "locationBn": "জয়পুরহাট জেলা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Little%20Jamuna%20Riverbank%2C%20Joypurhat%20district"
        },
        {
            "id": 5,
            "nameEn": "Joypurhat municipal park",
            "nameBn": "জয়পুরহাট শহীদ ডা. আবুল কাশেম ময়দান ও পার্ক",
            "categoryEn": "Central Urban Leisure Park & Promenades",
            "categoryBn": "শহরের প্রধান বিনোদন উদ্যান ও পরিবারিক চত্বর",
            "descEn": "Joypurhat Municipal Park, located conveniently in the town center, is the primary civic recreational green space for local families and visitors. The landscaped park includes well-paved walking circuits, flower gardens, shaded benches, and dedicated play structures for children. In the evening hours, gentle illumination turns the park into a vibrant social gathering spot where people unwind after busy workdays. Food kiosks near the entrances serve local savory snacks and seasonal fresh fruit juices, enhancing the festive leisure mood. It represents a clean, welcoming green oasis in the heart of Joypurhat town.",
            "descBn": "জয়পুরহাট শহরের কেন্দ্রস্থলে অবস্থিত পৌর পার্কটি শহরবাসীর প্রাত্যহিক অবসর যাপন ও শিশুদের বিনোদনের প্রধান কেন্দ্র। সুসজ্জিত ফুলের বাগান, পরিষ্কার হাঁটার পথ এবং ছায়াঘেরা বসার স্থান পার্কটিকে অত্যন্ত দৃষ্টিনন্দন করেছে। এখানে শিশুদের জন্য রয়েছে নিরাপদ দোলনা, স্লিপারসহ বিভিন্ন বিনোদনমূলক রাইড। বিকেলে এবং সন্ধ্যায় নির্মল বাতাসে পরিবার ও বন্ধুদের নিয়ে সময় কাটাতে প্রচুর মানুষ এখানে আসেন। শহরের কোলাহলমুক্ত পরিবেশে কিছু সময় স্বস্তিতে কাটানোর জন্য জয়পুরহাট পৌর পার্ক এক চমৎকার উন্মুক্ত স্থান।",
            "locationEn": "Joypurhat town",
            "locationBn": "জয়পুরহাট শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Joypurhat%20municipal%20park%2C%20Joypurhat%20town"
        }
    ]
}

# 7. SUNAMGANJ
sunamganj = {
    "slug": "sunamganj",
    "en": "Sunamganj",
    "bn": "সুনামগঞ্জ",
    "hero_title_en": "Sunamganj Majestic Tanguar Haor & Baul Heartland",
    "hero_title_bn": "সুনামগঞ্জের সুবিশাল টাঙ্গুয়ার হাওর ও বাউল গান",
    "hero_sub_en": "Endless inland freshwater seas, turquoise Niladri Lake at Tekerghat, and the mystic poetry of Hason Raja.",
    "hero_sub_bn": "রামসার সাইট টাঙ্গুয়ার হাওরের অপার জলরাশি, নীলাদ্রি লেকের নীল জল ও হাছন রাজার মরমী গানের দেশ।",
    "tagline_en": "The celestial wetlands capital of northeastern Bangladesh, world-celebrated for the Ramsar-inscribed Tanguar Haor, turquoise quarry waters of Niladri Lake beneath the Meghalaya hills, and the timeless mystic philosophy of mystic bard Hason Raja.",
    "tagline_bn": "উত্তর-পূর্বাঞ্চলের সুবিশাল জলাভূমির স্বর্গরাজ্য, যা আন্তর্জাতিক রামসার সাইট টাঙ্গুয়ার হাওর, মেঘালয় পাহাড়ের পাদদেশের নীলাদ্রি লেক এবং মরমি কবি হাছন রাজার অমর দর্শনের জন্য জগদ্বিখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/sunamganj/carousel-1.webp",
            "titleEn": "Tanguar Haor Ramsar Wetland Sanctuary",
            "titleBn": "টাঙ্গুয়ার হাওর আন্তর্জাতিক রামসার জলাভূমি",
            "subtitleEn": "Vast inland freshwater sea under the Meghalaya mountains sheltering millions of migratory birds and swamp forests",
            "subtitleBn": "মেঘালয়ের সুউচ্চ পাহাড়ের পাদদেশে বিস্তৃত সুবিশাল মিঠা পানির হাওর ও জলজ বনের বিস্ময়কর রূপ"
        },
        {
            "id": 2,
            "image": "images/districts/sunamganj/carousel-2.webp",
            "titleEn": "Niladri Lake (Shahid Siraj Lake) Turquoise Waters",
            "titleBn": "নীলাদ্রি লেক (শহীদ সিরাজ লেক) নীল জলরাশি",
            "subtitleEn": "Mesmerizing limestone quarry lake in Tekerghat glistening with deep blue waters framed by mountain ridges",
            "subtitleBn": "টেকেরঘাটে অবস্থিত চুনাপাথরের নীল জলের লেক, যা বাংলার 'সুইজারল্যান্ড' নামে ভ্রমণপিপাসুদের হৃদয়ে স্থান পেয়েছে"
        },
        {
            "id": 3,
            "image": "images/districts/sunamganj/carousel-3.webp",
            "titleEn": "Jadukata River Crystal Sands & Mountain Vista",
            "titleBn": "জাদুকাটা নদীর স্বচ্ছ জল ও বালুচর",
            "subtitleEn": "Pristine mountain river carrying icy waters from the Khasia hills across sparkling white sands in Tahirpur",
            "subtitleBn": "খাসিয়া পাহাড় থেকে নেমে আসা স্বচ্ছ কাঁচের মতো জল ও সাদা বালুচরের নয়নাভিরাম মিলনমেলা"
        },
        {
            "id": 4,
            "image": "images/districts/sunamganj/carousel-4.webp",
            "titleEn": "Barikka Tila Mountain Viewpoint Overlook",
            "titleBn": "বারিক্কা টিলার সুউচ্চ পাহাড়ি দৃশ্য",
            "subtitleEn": "Dramatic hilltop bluff in Tahirpur offering stunning views of Jadukata River winding into India's green mountains",
            "subtitleBn": "তাক লাগানো পাহাড়ি টিলা, যেখান থেকে ভারতের মেঘালয় পাহাড় ও জাদুকাটা নদীর মোহময় রূপ দেখা যায়"
        },
        {
            "id": 5,
            "image": "images/districts/sunamganj/carousel-5.webp",
            "titleEn": "Hason Raja Memorial Museum & Mystical Legacy",
            "titleBn": "হাছন রাজা জাদুঘর ও মরমী গানের ঐতিহ্য",
            "subtitleEn": "Historic mansion in Sunamganj town preserving the life, poetry, and philosophy of the legendary mystic bard",
            "subtitleBn": "সুনামগঞ্জ শহরে অবস্থিত মরমি গানের অমর স্রষ্টা হাছন রাজার স্মৃতিবিজড়িত রাজবাড়ি ও সংগ্রহশালা"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Hason Raja Museum",
            "nameBn": "হাছন রাজা স্মৃতি জাদুঘর",
            "categoryEn": "Mystic Poet Ancestral Manor & Museum",
            "categoryBn": "মরমি কবি হাছন রাজার ঐতিহাসিক বাড়ি ও জাদুঘর",
            "descEn": "The Hason Raja Museum in Sunamganj town is the ancestral home and memorial museum of the celebrated nineteenth-century mystic philosopher and Baul songwriter, Dewan Hason Raja Chowdhury. Renowned across Bengal for his soul-stirring songs examining mortality, spiritual love, and divine detachment, Hason Raja composed over a thousand classic songs from this very manor along the Surma River. The museum showcases the poet's personal silver-hilted swords, handwritten musical manuscripts, turban headgear, family photographs, and his famous horse carriage. The rustic brick mansion retains an atmosphere of meditative simplicity that mirrors the poet's transformation from wealthy landlord to spiritual wanderer. It is a mandatory pilgrimage site for anyone seeking the philosophical heart of Bengali folk mysticism.",
            "descBn": "সুনামগঞ্জ শহরের প্রাণকেন্দ্রে সুরমা নদীর তীরে অবস্থিত হাছন রাজা স্মৃতি জাদুঘর অবিভক্ত বাংলার প্রখ্যাত মরমি কবি ও বাউল গীতিকার দেওয়ান হাছন রাজার স্মৃতিবিজড়িত ঐতিহাসিক বাসস্থান। 'মাটির পিঞ্জিরায় সোনার ময়না রে' কিংবা 'লোকে বলে বলেরে ঘরবাড়ি ভালা না আমার'-এর মতো অসংখ্য অমর মরমি গানের জন্ম এই সুরম্য রাজবাড়িতেই। জাদুঘরে হাছন রাজার ব্যবহৃত তলোয়ার, খড়ম, পাগড়ি, হাতে লেখা গানের পাণ্ডুলিপি, আসবাবপত্র এবং ঐতিহাসিক আলোকচিত্র সংরক্ষিত রয়েছে। জমিদারির ভোগবিলাস ত্যাগ করে আধ্যাত্মিক সাধনায় নিমগ্ন এই মহান সাধকের জীবন ও সৃষ্টির প্রতি গভীর শ্রদ্ধা জানাতে দেশ-বিদেশের বহু সাহিত্যপ্রেমী এখানে আসেন।",
            "locationEn": "Sunamganj town; verify current venue",
            "locationBn": "সুনামগঞ্জ শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Hason%20Raja%20Museum%2C%20Sunamganj%20town%3B%20verify%20current%20venue"
        },
        {
            "id": 2,
            "nameEn": "Pagla Jame Mosque",
            "nameBn": "পাগলা ঐতিহাসিক জামে মসজিদ",
            "categoryEn": "Historic Mughal-Style Riverfront Mosque",
            "categoryBn": "নয়নাভিরাম মুঘল রীতির ঐতিহাসিক মসজিদ",
            "descEn": "Pagla Jame Mosque in South Sunamganj (Shantiganj) is an architectural marvel built along the Mahasing River in the early twentieth century by the philanthropist Mir Afsaruddin. Constructed in the grandeur of imperial Mughal design, this magnificent two-story brick and marble mosque features three gleaming bulbous domes and six soaring minarets visible from miles across the surrounding wetlands. Skilled masons from Kolkata and Delhi crafted the intricate plaster arabesques, stained-glass floral windows, and polished white-marble prayer floors. The reflection of the grand mosque in the adjacent river waters creates an unforgettable, ethereal vista at sunset. It stands as one of the most aesthetically distinguished religious sanctuaries in the Sylhet division.",
            "descBn": "সুনামগঞ্জের শান্তিগঞ্জ উপজেলায় মহাশিং নদীর তীরে অবস্থিত পাগলা জামে মসজিদ উত্তর-পূর্ব বাংলার অন্যতম নয়নাভিরাম ও স্থাপত্যশৈলীতে সমৃদ্ধ ঐতিহাসিক মসজিদ। বিংশ শতাব্দীর প্রারম্ভে স্থানীয় দানশীল ব্যক্তিত্ব মীর আফসার উদ্দিনের উদ্যোগে নির্মিত এই মসজিদে মুঘল স্থাপত্যের রাজকীয় প্রভাব স্পষ্ট। তিন গম্বুজ ও ছয়টি সুউচ্চ মিনার বিশিষ্ট এই মসজিদে রয়েছে দিল্লির শিল্পীদের খোদাই করা মার্বেল পাথর, সুদৃশ্য কাচ ও চমৎকার চুন-সুরকির নকশা। মহাশিং নদীর জলে মসজিদের প্রতিচ্ছবি এক অপার্থিব রূপ ধারণ করে। স্থাপত্যপ্রেমী ও ধর্মপ্রাণ পর্যটকদের জন্য এই মসজিদটি এক অবশ্য দর্শনীয় স্থান।",
            "locationEn": "Pagla area, Sunamganj",
            "locationBn": "পাগলা, শান্তিগঞ্জ, সুনামগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Pagla%20Jame%20Mosque%2C%20Pagla%20area%2C%20Sunamganj"
        },
        {
            "id": 3,
            "nameEn": "Lakshmansree historic settlement",
            "nameBn": "লক্ষণশ্রী প্রাচীন জনপদ ও জমিদার বাড়ি",
            "categoryEn": "Historic Riverine Settlement & Feudal Estate",
            "categoryBn": "ঐতিহাসিক নদী বন্দর ও প্রাচীন জনপদ",
            "descEn": "Lakshmansree in Sunamganj Sadar is a historic riverine locality that served as the primary administrative and feudal heart of Sunamganj before the modern town emerged. It was the ancestral seat of the influential Dewan family, including Hason Raja's noble forebears, who established trading posts and river security along the Surma corridor. Surviving structures feature antique brick archways, broad bathing ghats leading to the river, and family shrines shaded by century-old tamarind trees. Regional folklore associates Lakshmansree with classical musical soirees where legendary folk singers congregated to exchange songs during monsoon floods. Exploring the tranquil paths of Lakshmansree provides deep historical context for the cultural evolution of the wetland district.",
            "descBn": "সুনামগঞ্জ সদরের লক্ষণশ্রী সুরমা নদীর তীরে অবস্থিত এক অতি প্রাচীন জনপদ, যা আধুনিক সুনামগঞ্জ শহর গড়ে ওঠার পূর্বেই শিক্ষা ও বাণিজ্যের প্রধান কেন্দ্র ছিল। এটি প্রখ্যাত দেওয়ান পরিবার ও হাছন রাজার পূর্বপুরুষদের আদি নিবাস হিসেবে ঐতিহাসিকভাবে গুরুত্বপূর্ণ। এই এলাকায় এখনো প্রাচীন পাকা ঘাট, পুরানো ভবনের অবশিষ্টাংশ এবং শতবর্ষী বৃক্ষরাজি অতীতের সমৃদ্ধির সাক্ষ্য দেয়। বর্ষাকালে নদীবেষ্টিত এই জনপদে একসময় কবি ও সাধকদের নিয়মিত গানের আসর বসত। সুরমা নদীর নির্মল বাতাসের সাথে ইতিহাসের সুবাস পেতে লক্ষণশ্রী ভ্রমণ অত্যন্ত তাৎপর্যপূর্ণ।",
            "locationEn": "Lakshmansree, Sunamganj Sadar",
            "locationBn": "লক্ষণশ্রী, সুনামগঞ্জ সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Lakshmansree%20historic%20settlement%2C%20Lakshmansree%2C%20Sunamganj%20Sadar"
        },
        {
            "id": 4,
            "nameEn": "Tahirpur historic haor settlements",
            "nameBn": "তাহিরপুরের ঐতিহাসিক হাওর জনপদ",
            "categoryEn": "Indigenous Wetland Heritage & Water Culture",
            "categoryBn": "ঐতিহাসিক হাওর জীবন ও প্রাচীন দ্বীপ গ্রাম",
            "descEn": "The historic haor settlements of Tahirpur represent centuries of human adaptation to one of the most dynamic wetland ecosystems on planet earth. Isolated as island villages ('hati') amidst endless inland seas during the six-month monsoon, these communities developed unique floating boat cultures, bamboo architecture, and community fishing traditions. Ancient stone anchors, wooden boat-building yards, and oral ballads passed through generations describe maritime skirmishes with medieval pirate flotillas. Visiting these resilient village hamlets offers travelers an extraordinary glimpse into an authentic water civilization that thrives in harmony with nature's seasonal pulse. It is an invaluable cultural component of any Sunamganj exploration.",
            "descBn": "তাহিরপুরের ঐতিহাসিক হাওর জনপদগুলো বিশ্বের অন্যতম বৈচিত্র্যময় জলাভূমিতে মানুষের বেঁচে থাকার সংগ্রাম ও সংস্কৃতির এক জীবন্ত দলিল। বছরের প্রায় ছয় মাস সুবিশাল জলরাশির বুকে দ্বীপের মতো ভেসে থাকা এই 'হাটি' বা গ্রামগুলোর জীবনযাত্রা অত্যন্ত বিস্ময়কর। এখানকার মানুষের নিজস্ব নৌকা তৈরি, বাঁশের মাটির উঁচু ভিটা এবং জাল ফেলার চিরায়ত ঐতিহ্য বহু শতাব্দীর প্রাচীন। লোকসঙ্গীত ও মাঝিদের কণ্ঠে গাওয়া ভাটিয়ালি গান হাওরের বিস্তৃত আকাশে এক মায়াবী সুর তোলে। প্রকৃতির সাথে যুদ্ধ করে গড়ে ওঠা এই অনন্য জলজ সভ্যতার রূপ দেখতে তাহিরপুরের হাওর গ্রামগুলো অনন্য।",
            "locationEn": "Tahirpur; ask locally for named sites",
            "locationBn": "তাহিরপুর, সুনামগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Tahirpur%20historic%20haor%20settlements%2C%20Tahirpur%3B%20ask%20locally%20for%20named%20sites"
        },
        {
            "id": 5,
            "nameEn": "Jamalganj historic market area",
            "nameBn": "জামালগঞ্জ ঐতিহাসিক নৌ-বন্দর ও বাজার",
            "categoryEn": "Colonial Inland River Port & Grain Emporium",
            "categoryBn": "ঐতিহাসিক নদী বন্দর ও প্রাচীন শস্য বাণিজ্য কেন্দ্র",
            "descEn": "Jamalganj historic market area along the Surma River was historically one of the premier inland river ports and rice-trading emporiums of the northeastern Sylhet basin. Established during early colonial trade expansions, large cargo sailing craft called 'Goyna' gathered here to transport tons of sun-dried boro rice, dried fish (shutki), and timber from the Meghalaya border to urban centers. The vintage market lanes still retain traditional tin-roofed wooden trading godowns, sweetmeat tea shops, and stone-paved riverside unloading ramps. The bustling river traffic and wholesale agricultural auctions offer travelers a lively, sensory connection to the maritime commerce that built Sunamganj's prosperity. It remains a fascinating hub of rural river life.",
            "descBn": "সুরমা নদীর তীরবর্তী জামালগঞ্জ বাজার একসময় উত্তর-পূর্ব বাংলার অন্যতম বৃহত্তম নদী বন্দর ও খাদ্যশস্যের প্রধান বাণিজ্য কেন্দ্র হিসেবে পরিচিত ছিল। ব্রিটিশ ও পাকিস্তান আমলে সুনামগঞ্জের বিস্তীর্ণ হাওরাঞ্চলে উৎপাদিত বোরো ধান এবং শুঁটকি মাছ এই বন্দর থেকেই বড় বড় গয়না নৌকায় করে দেশের বিভিন্ন প্রান্তে যেত। প্রাচীন কাঠের আড়ত, টিনের ছাউনিযুক্ত ঐতিহাসিক দোকান এবং ব্যস্ত নদীঘাট এখনো সেই সমৃদ্ধ বাণিজ্যিক অতীতের স্মৃতি ধরে রেখেছে। হাওরের মাছ ও ফসলের কেনাবেচায় মুখরিত জামালগঞ্জ বাজার নদীমাতৃক অর্থনীতির এক চমৎকার প্রতিচ্ছবি।",
            "locationEn": "Jamalganj, Sunamganj",
            "locationBn": "জামালগঞ্জ, সুনামগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Jamalganj%20historic%20market%20area%2C%20Jamalganj%2C%20Sunamganj"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Tanguar Haor",
            "nameBn": "টাঙ্গুয়ার হাওর",
            "categoryEn": "UNESCO Ramsar Wetland & Inland Sea",
            "categoryBn": "আন্তর্জাতিক রামসার সাইট ও সুবিশাল হাওর",
            "descEn": "Tanguar Haor, spanning Tahirpur and Dharmapasha Upazilas, is an internationally acclaimed Ramsar wetland site covering over 100 square kilometers beneath the soaring Khasi-Jaintia mountain range. During the monsoon, the haor transforms into a breathtaking inland freshwater ocean where sky and crystal-blue waters merge seamlessly into the horizon. Submerged swamp forests of Hijal and Koroch trees emerge gracefully from the depths, creating surreal green archipelagos navigable by traditional wooden houseboats. In the winter season, the waters recede to expose lush marshes that host upwards of 200 species of migratory birds, including rare Baer's Pochards and Pallas's Fish Eagles. Sleeping on a wooden houseboat under starlit haor skies is widely celebrated as one of the ultimate ecotourism experiences in Asia.",
            "descBn": "মেঘালয় পাহাড়ের পাদদেশে সুনামগঞ্জের তাহিরপুর ও ধর্মপাশা জুড়ে বিস্তৃত টাঙ্গুয়ার হাওর বাংলাদেশের দ্বিতীয় রামসার সাইট এবং এক অনন্য প্রাকৃতিক বিস্ময়। বর্ষাকালে প্রায় ১০০ বর্গকিলোমিটার এলাকা জুড়ে সৃষ্টি হয় এক অন্তহীন স্বচ্ছ জলধি, যেখানে নীল আকাশ আর হাওরের পানি যেন একাকার হয়ে যায়। পানির নিচ থেকে জেগে ওঠা হিজল ও করচ গাছের জলজ বন হাওরটিকে এক পরাবাস্তব রূপ দান করে। শীতকালে এখানে আগমন ঘটে লক্ষ লক্ষ দুর্লভ পরিযায়ী পাখির, যা পাখিপ্রেমীদের জন্য এক স্বর্গরাজ্য। সুসজ্জিত কাঠের হাউসবোটে চড়ে হাওরের বুকে রাত্রিযাপন ও মেঘালয় পাহাড়ের দৃশ্য অবলোকন করা জীবনের অন্যতম সেরা ভ্রমণ অভিজ্ঞতা।",
            "locationEn": "Tahirpur and Dharmapasha, Sunamganj",
            "locationBn": "তাহিরপুর ও ধর্মপাশা, সুনামগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Tanguar%20Haor%2C%20Tahirpur%20and%20Dharmapasha%2C%20Sunamganj"
        },
        {
            "id": 2,
            "nameEn": "Niladri Lake (Shahid Siraj Lake)",
            "nameBn": "নীলাদ্রি লেক (শহীদ সিরাজ লেক)",
            "categoryEn": "Turquoise Limestone Quarry Lake & Hills",
            "categoryBn": "চুনাপাথরের নীল হ্রদ ও মেঘালয় পাহাড় ভিউপয়েন্ট",
            "descEn": "Niladri Lake, officially named Shahid Siraj Lake in honor of a heroic 1971 freedom fighter, is an enchanting turquoise lake nestled against the international border at Tekerghat. Formed in an abandoned limestone quarry once worked by the Chhatak Cement Factory, the lake's mineral-rich water sparkles with an intense, crystalline cyan-blue hue. Steep emerald hillocks dotted with grazing goats and rustic wooden cottages frame the lake, with the cloud-capped green mountains of Meghalaya rising dramatically in the immediate background. Travelers can hire small paddle boats to glide across the tranquil blue waters or picnic along the scenic hill ridges. Known popularly as the 'Switzerland of Bengal', its dreamlike beauty makes it one of the most photographed attractions in Bangladesh.",
            "descBn": "সুনামগঞ্জের সীমান্তবর্তী টেকেরঘাটে অবস্থিত নীলাদ্রি লেক (শহীদ সিরাজ লেক) তার স্ফটিকের মতো নীল জলরাশি ও চারপাশের সবুজের জন্য ভ্রমণপিপাসুদের কাছে বাংলার 'সুইজারল্যান্ড' নামে পরিচিত। একসময়ের চুনাপাথর খনির গভীর গর্তে বৃষ্টির পানি ও পাহাড়ি ঝিরির স্বচ্ছ জল জমে এই মনোমুগ্ধকর হ্রদের সৃষ্টি হয়েছে। লেকের ঠিক পেছনেই খাড়া হয়ে দাঁড়িয়ে আছে ভারতের মেঘালয়ের সুউচ্চ সবুজ পাহাড়মালা, যার চূড়ায় মেঘের দল ভেসে বেড়ায়। লেকের শান্ত জলে ছোট নৌকায় ভেসে বেড়ানো কিংবা উঁচু টিলায় বসে বাতাস উপভোগ করা এক অনন্য স্বর্গীয় অনুভূতি। ভ্রমণপ্রেমীদের কাছে নীলাদ্রি এক পরম স্বপ্নময় গন্তব্য।",
            "locationEn": "Tekerghat, Tahirpur",
            "locationBn": "টেকেরঘাট, তাহিরপুর, সুনামগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Niladri%20Lake%20(Shahid%20Siraj%20Lake)%2C%20Tekerghat%2C%20Tahirpur"
        },
        {
            "id": 3,
            "nameEn": "Jadukata River",
            "nameBn": "জাদুকাটা নদী",
            "categoryEn": "Crystal Clear Mountain River & White Sands",
            "categoryBn": "স্বচ্ছ কাঁচের জল ও শুভ্র বালুর জাদুকাটা নদী",
            "descEn": "The Jadukata River in Tahirpur is celebrated as one of the cleanest, most picturesque rivers in the entire Indian subcontinent. Emerging directly from the rain-drenched Khasi hills of Meghalaya, its crystal-clear water reveals every pebble, grain of sand, and school of darting fish beneath its rippling surface. Flanked on one side by lush green mountains and on the other by vast blindingly white sandbars, thousands of local workers can be seen diving into the riverbed to harvest valuable construction sand and river gravel. During twilight, the setting sun casts a dazzling kaleidoscope of amber, pink, and turquoise over the river waters. Standing on its banks is an unforgettable sensory communion with nature's pure majesty.",
            "descBn": "তাহিরপুরের জাদুকাটা নদীকে বলা হয় বাংলাদেশের অন্যতম স্বচ্ছ ও রূপবতী পাহাড়ি নদী। ভারতের মেঘালয়ের খাসিয়া পাহাড় থেকে নেমে আসা এই নদীর জল এতটাই স্বচ্ছ ও নির্মল যে তলদেশের প্রতিটি নুড়িপাথর ও বালুকণা স্পষ্ট দেখা যায়। একপাশে সুবিশাল মেঘালয় পাহাড়ের দেয়াল এবং অন্যপাশে সাদা বালুর বিস্তীর্ণ চর নদীটিকে এক অদ্ভুত মায়াবী রূপ দান করেছে। হাজার হাজার শ্রমিকের ঐতিহ্যবাহী উপায়ে নদী থেকে বালু ও পাথর তোলার কর্মব্যস্ত দৃশ্যও দেখার মতো। গোধূলির আলোয় যখন জাদুকাটার স্বচ্ছ জলে পাহাড়ের ছায়া পড়ে, তখন সেই জাদুকরী রূপ দেখে মুগ্ধ না হয়ে উপায় থাকে না।",
            "locationEn": "Tahirpur, Sunamganj",
            "locationBn": "তাহিরপুর, সুনামগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Jadukata%20River%2C%20Tahirpur%2C%20Sunamganj"
        },
        {
            "id": 4,
            "nameEn": "Barikka Tila",
            "nameBn": "বারিক্কা টিলা",
            "categoryEn": "Panoramic Mountain Bluff & Border Overlook",
            "categoryBn": "সুউচ্চ সীমান্ত টিলা ও জাদুকাটা নদী ভিউপয়েন্ট",
            "descEn": "Barikka Tila in Tahirpur is an imposing highland bluff rising sharply above the eastern bank of the Jadukata River. From the breezy summit of the tila, visitors are rewarded with a breathtaking, cinematic bird's-eye panorama encompassing the Jadukata River curving out of mountain canyons, wide sandy beaches, and endless green hill ranges stretching into India. Shaded by jackfruit trees, wild berries, and flowering shrubs, the hill offers an ideal vantage point for landscape photography and refreshing highland relaxation. Local tea stalls perched on the slopes serve hot spiced tea and crispy snacks as travelers soak in the cool mountain breezes. It is considered an essential stop on any haor expedition.",
            "descBn": "তাহিরপুরে জাদুকাটা নদীর ঠিক পাড় ঘেঁষে মাথা তুলে দাঁড়িয়ে থাকা সুউচ্চ বারিক্কা টিলা উত্তর-পূর্বাঞ্চলের অন্যতম সেরা ভিউপয়েন্ট। টিলার চূড়ায় উঠলে এক অভাবনীয় দৃশ্যের অবতারণা হয়—নিচে রূপসী জাদুকাটা নদী এঁকেবেঁকে চলে গেছে আর সামনেই ভারতের সবুজ পাহাড়ের সুবিশাল প্রাচীর। টিলার ওপর থেকে বহুদূর পর্যন্ত নদী, বালুচর আর সবুজের মিলনমেলা এক পলকেই অবলোকন করা যায়। পাহাড়ি স্নিগ্ধ বাতাস এবং স্থানীয় চায়ের দোকানে বসে মেঘ-পাহাড়ের রূপ উপভোগ করা পর্যটকদের পরম আনন্দ এনে দেয়। প্রাকৃতিক সৌন্দর্য ও অ্যাডভেঞ্চারের জন্য বারিক্কা টিলা এক অনন্য আকর্ষণ।",
            "locationEn": "Tahirpur, Sunamganj",
            "locationBn": "তাহিরপুর, সুনামগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Barikka%20Tila%2C%20Tahirpur%2C%20Sunamganj"
        },
        {
            "id": 5,
            "nameEn": "Haor boat routes",
            "nameBn": "হাওর জলপথ ও হাউসবোট ক্রুজ",
            "categoryEn": "Authentic Houseboat Cruising & Water Safari",
            "categoryBn": "ঐতিহ্যবাহী হাউসবোট ভ্রমণ ও নদীজলপথ",
            "descEn": "The interconnected Haor Boat Routes of Sunamganj offer travelers one of the most romantic and immersive water safari adventures in the world. Modern wooden houseboats equipped with air-conditioned sleeping cabins, open-air sun decks, traditional handloom furnishings, and authentic Sylheti culinary kitchens cruise leisurely across hundreds of miles of open freshwater channels. Gliding past solitary wetland mosques, grazing duck flotillas, and remote island communities under immense tropical skies, travelers experience the rhythm of life in an authentic water world. Stargazing at night from the roof deck with only the sound of gentle waves lapping against the hull is an unforgettable, restorative journey. It represents the gold standard of modern eco-tourism in Bangladesh.",
            "descBn": "সুনামগঞ্জের দিগন্তবিস্তৃত হাওর জলপথ জুড়ে আধুনিক কাঠের হাউসবোটে ভ্রমণ বর্তমানে বাংলাদেশের সবচেয়ে রোমাঞ্চকর ও জনপ্রিয় পর্যটন অভিজ্ঞতা। মনোরম কেবিন, ছাদের ওপর বসার সুদৃশ্য ডেক এবং ঐতিহ্যবাহী স্থানীয় খাবারের সুব্যবস্থা সমৃদ্ধ এই হাউসবোটগুলো পর্যটকদের নিয়ে ভেসে চলে টাঙ্গুয়ার হাওর, জাদুকাটা নদী ও টেকেরঘাটের নীল জলে। দিনে দিগন্তজোড়া জলরাশি ও মেঘালয়ের পাহাড়ের দৃশ্য এবং রাতে শান্ত হাওরের বুকে লক্ষ তারার মেলা অবলোকন করা এক স্বর্গীয় অনুভূতি এনে দেয়। প্রকৃতির কোলে সম্পূর্ণ নির্ভার হয়ে কয়েকদিন কাটানোর জন্য হাওর বোট ক্রুজ এক অবিস্মরণীয় অবকাশ।",
            "locationEn": "Sunamganj; services vary by season",
            "locationBn": "সুনামগঞ্জ হাওর অঞ্চল",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Haor%20boat%20routes%2C%20Sunamganj%3B%20services%20vary%20by%20season"
        }
    ]
}

# 8. GAIBANDHA
gaibandha = {
    "slug": "gaibandha",
    "en": "Gaibandha",
    "bn": "গাইবান্ধা",
    "hero_title_en": "Gaibandha Mighty Rivers & Zamindari Estates",
    "hero_title_bn": "গাইবান্ধার তিস্তা-ব্রহ্মপুত্র মোহনা ও বর্ধন কুঠি",
    "hero_sub_en": "Historic palatial ruins of Bardhan Kuthi, scenic Balashi Ghat, and vast Brahmaputra charlands.",
    "hero_sub_bn": "ঐতিহাসিক বর্ধন কুঠির প্রাচীন প্রাসাদ, মনোরম বালাসী ঘাট ও ব্রহ্মপুত্রের সুবিশাল চরাঞ্চলের নিসর্গ।",
    "tagline_en": "The storied riverine gateway of northern Bengal where the mighty Brahmaputra and Teesta rivers converge, celebrated for the ancient feudal citadel of Bardhan Kuthi and panoramic riverside vistas.",
    "tagline_bn": "উত্তরবঙ্গের তিস্তা ও ব্রহ্মপুত্র নদীর সঙ্গমস্থল, যা প্রাচীন বর্ধন কুঠির জমিদারি ইতিহাস, ঐতিহ্যবাহী বালাসী ঘাট এবং ব্রহ্মপুত্রের সুবিশাল চরাঞ্চলের জন্য সুপরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/gaibandha/carousel-1.webp",
            "titleEn": "Bardhan Kuthi Ancient Feudal Palace",
            "titleBn": "বর্ধন কুঠির ঐতিহাসিক রাজপ্রাসাদ",
            "subtitleEn": "Centuries-old royal citadel in Gobindaganj featuring medieval brick ramparts and sacred terracotta temples",
            "subtitleBn": "গোবিন্দগঞ্জে অবস্থিত রাজা হরিনাথের প্রাচীন প্রাসাদ, যার দেওয়াল ও মন্দির শতবর্ষের ঐতিহ্যের সাক্ষী"
        },
        {
            "id": 2,
            "image": "images/districts/gaibandha/carousel-2.webp",
            "titleEn": "Balashi Ghat Historic Brahmaputra Riverfront",
            "titleBn": "বালাসী ঘাটের ব্রহ্মপুত্র নদী দর্শন",
            "subtitleEn": "Famous historic river port and ferry terminal in Fulchhari offering boundless views across the mighty river waters",
            "subtitleBn": "ফুলছড়িতে অবস্থিত বিখ্যাত নদী বন্দর ও ঘাট, যেখান থেকে ব্রহ্মপুত্রের উত্তাল রূপ ও দিগন্তজোড়া বাতাস উপভোগ করা যায়"
        },
        {
            "id": 3,
            "image": "images/districts/gaibandha/carousel-3.webp",
            "titleEn": "Brahmaputra Vast Charland Island Vistas",
            "titleBn": "ব্রহ্মপুত্রের সুবিশাল চরাঞ্চল ও জীবনধারা",
            "subtitleEn": "Dynamic sand islands adorned with golden kashbon blossoms, grazing cattle, and traditional fishing boats",
            "subtitleBn": "নদীর বুকে জেগে ওঠা বিস্তীর্ণ চরাঞ্চল, যেখানে সাদা কাশফুল ও গ্রামীণ জীবন এক চমৎকার দৃশ্যপট তৈরি করে"
        },
        {
            "id": 4,
            "image": "images/districts/gaibandha/carousel-4.webp",
            "titleEn": "Bamondanga Historic Railway Station & Colony",
            "titleBn": "বামনডাঙ্গা ঐতিহাসিক রেলওয়ে স্টেশন",
            "subtitleEn": "Colonial-era railway architectural landmark in Sundarganj serving north Bengal for over a century",
            "subtitleBn": "সুন্দরগঞ্জের শতবর্ষী প্রাচীন ব্রিটিশ রেলওয়ে স্টেশন ও হেরিটেজ অবকাঠামো"
        },
        {
            "id": 5,
            "image": "images/districts/gaibandha/carousel-5.webp",
            "titleEn": "Teesta River Confluence & Embankments",
            "titleBn": "তিস্তা নদী ও তীরের স্নিগ্ধ নিসর্গ",
            "subtitleEn": "Meandering northern river flowing gently into the Brahmaputra basin amidst fertile green alluvial plains",
            "subtitleBn": "তিস্তা ও ব্রহ্মপুত্রের মোহনা অঞ্চল, যার স্নিগ্ধ নদীসৈকত ও মুক্ত হাওয়া ভ্রমণকারীদের মুগ্ধ করে"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Bardhan Kuthi",
            "nameBn": "বর্ধন কুঠি",
            "categoryEn": "Ancient Feudal Citadel & Palace Ruins",
            "categoryBn": "সপ্তদশ শতকের ঐতিহাসিক রাজপ্রাসাদ ও ধ্বংসাবশেষ",
            "descEn": "Bardhan Kuthi, situated at Bharatkhali in Gobindaganj Upazila, is the legendary seat of the ancient kings of Gobindaganj dating back to the sixteenth century. Established by Raja Harinath and expanded by his royal descendants, the fortress compound housed royal residential palaces, armories, audience chambers, and ornate terracotta temples. The precinct includes surviving brick gateposts, deep defensive perimeter moats, and ancient Hindu shrines dedicated to Lord Shiva and Radharani. Historians identify Bardhan Kuthi as a key strategic stronghold during anti-Mughal resistances in the northern delta. Today, the weathered red-brick ruins standing under ancient sacred banyans offer visitors an atmospheric journey into northern Bengal's heroic royal heritage.",
            "descBn": "গাইবান্ধার গোবিন্দগঞ্জ উপজেলায় অবস্থিত বর্ধন কুঠি উত্তরবঙ্গের এক অতি প্রাচীন ও গৌরবোজ্জ্বল ঐতিহাসিক রাজপ্রাসাদ। ষোড়শ শতাব্দীতে রাজা হরিনাথ কর্তৃক প্রতিষ্ঠিত এই রাজবাড়িতে ছিল সুরম্য অট্টালিকা, সৈন্যনিবাস, রাজদরবার এবং নান্দনিক পোড়ামাটির মন্দির। প্রাচীন পরিখা ও ইটের তোরণগুলো তৎকালীন রাজাদের সামরিক দূরদর্শিতা ও শিল্পরুচির পরিচয় দেয়। প্রাঙ্গণে অবস্থিত শতাব্দীপ্রাচীন শিব মন্দির ও কালী মন্দিরগুলো আজও পুণ্যার্থীদের শ্রদ্ধা আকর্ষণ করে। স্থানীয় লোকগাথা ও ঐতিহাসিক যুদ্ধের স্মৃতিবিজড়িত বর্ধন কুঠির ধ্বংসাবশেষ প্রাচীন ঐতিহ্যের এক পরম রোমাঞ্চকর নিদর্শন।",
            "locationEn": "Bharatkhali area; verify exact site",
            "locationBn": "গোবিন্দগঞ্জ, গাইবান্ধা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Bardhan%20Kuthi%2C%20Bharatkhali%20area%3B%20verify%20exact%20site"
        },
        {
            "id": 2,
            "nameEn": "Shib Bari Temple",
            "nameBn": "শিব বাড়ি মন্দির",
            "categoryEn": "Heritage Hindu Shiva Sanctuary",
            "categoryBn": "প্রাচীন শিব মন্দির ও আধ্যাত্মিক তীর্থ",
            "descEn": "Shib Bari Temple in Gaibandha is a venerable Hindu sanctuary of significant spiritual and architectural antiquity. Consecrated centuries ago under royal patronage, the temple features an imposing brick sikhara decorated with traditional terracotta panels and floral relief cornices. The sanctum enshrines an ancient black stone Shiva lingam where rituals and sacred prayers have been performed continuously across generations. The temple courtyard is shaded by towering sacred bilva and neem trees, providing a cool and contemplative atmosphere for pilgrims and visitors. During the Maha Shivaratri festival, the temple grounds come alive with traditional devotional singing and vibrant religious fairs that reflect the cultural warmth of Gaibandha.",
            "descBn": "গাইবান্ধা জেলার শতাব্দীপ্রাচীন শিব বাড়ি মন্দির সনাতন ধর্মাবলম্বীদের এক পরম পবিত্র ও ঐতিহাসিক উপাসনালয়। বহু শতাব্দী পূর্বে নির্মিত এই মন্দিরে রয়েছে ঐতিহ্যবাহী শিখর স্থাপত্য এবং পোড়ামাটির অপূর্ব কারুকাজ। মন্দিরের গর্ভগৃহে প্রতিষ্ঠিত রয়েছে প্রাচীন কষ্টিপাথরের শিবলিঙ্গ, যা ভক্তদের গভীর ভক্তির পাত্র। মন্দির প্রাঙ্গণের শান্ত ও স্নিগ্ধ পরিবেশ মনকে নির্মল প্রশান্তিতে ভরিয়ে তোলে। প্রতি বছর মহা শিবরাত্রি উপলক্ষে এখানে বিশাল মেলা ও ভক্তদের ঢল নামে। গাইবান্ধার ধর্মীয় ঐতিহ্য ও প্রাচীন স্থাপত্যের অন্যতম নিদর্শন হিসেবে এই মন্দিরটি সমাদৃত।",
            "locationEn": "Gaibandha district; verify village",
            "locationBn": "গাইবান্ধা জেলা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Shib%20Bari%20Temple%2C%20Gaibandha%20district%3B%20verify%20village"
        },
        {
            "id": 3,
            "nameEn": "Bamondanga historic rail area",
            "nameBn": "বামনডাঙ্গা ঐতিহাসিক রেলওয়ে স্টেশন",
            "categoryEn": "Colonial Railway Architecture & Heritage",
            "categoryBn": "ব্রিটিশ আমলের ঐতিহাসিক রেলওয়ে স্টেশন ও কলোনি",
            "descEn": "The Bamondanga historic rail area in Sundarganj Upazila preserves the distinctive colonial-era infrastructure of the late nineteenth-century Bengal Dooars Railway. Constructed in 1899 to transport timber, jute, and agricultural produce from northern forests to coastal ports, the station features pitched iron-truss roofs, red-brick ticket halls, and vintage lever-operated mechanical signal cabins. The adjacent railway staff colony and platform avenues shaded by ancient rain trees provide a picturesque step back into early transportation history. Photographers and rail enthusiasts appreciate the unhurried old-world ambiance that still permeates the platform as passenger trains arrive amidst ringing platform bells. It represents a proud chapter in northern Bengal's modern economic development.",
            "descBn": "সুন্দরগঞ্জের বামনডাঙ্গা রেলওয়ে স্টেশন উত্তরবঙ্গের রেল যোগাযোগের এক শতবর্ষী ঐতিহাসিক সাক্ষী। ১৮৯৯ সালে ব্রিটিশ আমলে আসাম-বেঙ্গল ও ডুয়র্স রেলওয়ের অংশ হিসেবে এই স্টেশনটি নির্মিত হয়, যা পাট ও কৃষি পণ্য পরিবহনে গুরুত্বপূর্ণ ভূমিকা রেখেছিল। লাল ইটের তৈরি প্রাচীন স্টেশন ভবন, কাঠের টিকিট কাউন্টার এবং ঐতিহ্যবাহী সিগন্যাল ব্যবস্থা আজও ঔপনিবেশিক আমলের স্মৃতি বহন করে। প্ল্যাটফর্মের দুই পাশে থাকা শতবর্ষী কড়ই ও মেহগনি গাছের ছায়া স্টেশনটিকে এক মনোরম স্নিগ্ধ রূপ দিয়েছে। প্রাচীন রেল ঐতিহ্যের প্রতি যাদের আগ্রহ রয়েছে, তাদের জন্য বামনডাঙ্গা এক চমৎকার দর্শনীয় স্থান।",
            "locationEn": "Bamondanga, Sundarganj",
            "locationBn": "বামনডাঙ্গা, সুন্দরগঞ্জ, গাইবান্ধা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Bamondanga%20historic%20rail%20area%2C%20Bamondanga%2C%20Sundarganj"
        },
        {
            "id": 4,
            "nameEn": "Fulchhari historic river settlements",
            "nameBn": "ফুলছড়ি ঐতিহাসিক নদী বন্দর ও জনপদ",
            "categoryEn": "Colonial River Port & Ghat Enclave",
            "categoryBn": "ঐতিহাসিক নদী বন্দর ও প্রাচীন ঘাট এলাকা",
            "descEn": "The Fulchhari historic river settlements represent a storied inland maritime center that flourished along the turbulent Brahmaputra corridor during the nineteenth and early twentieth centuries. In its heyday, Fulchhari served as a crucial railway steamer junction connecting passenger trains with massive paddle-wheel steamers navigating toward Assam and Kolkata. Remnants of stone mooring bollards, historic warehouse foundations, and vintage river-gauge posts can still be found along the shoreline. Local elder boatmen recount legendary tales of steam sirens, bustling river bazaars, and maritime navigators who mastered the unpredictable river channels. Exploring these shoreline communities provides rich insights into the dynamic riverine history of the Brahmaputra basin.",
            "descBn": "ফুলছড়ি ঘাট একসময় ব্রিটিশ ও পাকিস্তান আমলে অবিভক্ত বাংলার অন্যতম প্রধান রেল-স্টিমার ঘাট ও নদী বন্দর হিসেবে বিখ্যাত ছিল। আসাম ও কলকাতার মধ্যে চলাচলকারী সুবিশাল যাত্রীবাহী ও মালবাহী স্টিমারগুলো এই ঘাটে ভিড়ত এবং ট্রেনের মাধ্যমে যোগাযোগ স্থাপন করত। নদীর ভাঙা-গড়ার সাথে সাথে ঘাটের অবস্থান পরিবর্তিত হলেও এখানকার ঐতিহাসিক গুরুত্ব অমলিন। নদীর তীরের প্রাচীন জনপদগুলোতে এখনো সেই সময়ের কর্মব্যস্ততা ও নদী বাণিজ্যের স্মৃতিগাথা বেঁচে আছে। নদীমাতৃক বাংলার বিশালতা ও মানুষের নদীকেন্দ্রিক জীবনের ইতিহাস উপলব্ধি করতে ফুলছড়ির তুলনা নেই।",
            "locationEn": "Fulchhari, Gaibandha",
            "locationBn": "ফুলছড়ি, গাইবান্ধা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Fulchhari%20historic%20river%20settlements%2C%20Fulchhari%2C%20Gaibandha"
        },
        {
            "id": 5,
            "nameEn": "Gaibandha old town and market",
            "nameBn": "গাইবান্ধা পুরাতন শহর ও ঐতিহ্যবাহী বাজার",
            "categoryEn": "Centennial Commercial Heritage Quarter",
            "categoryBn": "শতবর্ষী বাণিজ্যিক শহর ও ঐতিহ্যবাহী মিষ্টির বাজার",
            "descEn": "The Gaibandha Old Town and market quarter represents the historic municipal core that grew alongside the Ghagot River during the late nineteenth century. The bustling bazaar lanes are lined with traditional two-story timber-framed merchant shops, antique wholesale spice warehouses, and celebrated sweetmeat confectioneries famous for regional sweets like 'Roshmanjuri'. Artisans here continue centuries-old traditions of crafting brass utensils, hand-rolled clay pottery, and bamboo agricultural tools. The energetic atmosphere, rich aromas of roasted spices, and warm local hospitality offer visitors an authentic slice of everyday northern lifestyle. It is the beating heart of commerce, culture, and community in the district.",
            "descBn": "গাইবান্ধা শহরের পুরাতন বাজার এলাকা শতবর্ষের সমৃদ্ধ বাণিজ্যিক ও সাংস্কৃতিক ঐতিহ্যের ধারক। ঘাঘট নদীর তীর ঘেঁষে গড়ে ওঠা এই বাজারে রয়েছে ব্রিটিশ আমলের কাঠের ও টিনের তৈরি প্রাচীন দোকানপাট এবং পাইকারি পণ্যের আড়ত। বিশেষ করে এখানকার বিখ্যাত ও সুস্বাদু মিষ্টি 'রসমঞ্জরী' সমগ্র দেশে সমাদৃত, যার স্বাদ নিতে বহু দূর থেকে ভোজনরসিকরা আসেন। ঐতিহ্যবাহী কাঁসা-পিতলের বাসনপত্র ও দেশীয় হস্তশিল্পের জন্যও এই বাজারটি সুপরিচিত। স্থানীয় মানুষের আন্তরিকতা ও প্রাণবন্ত নাগরিক জীবনের স্পর্শ পেতে গাইবান্ধা পুরাতন শহর এক চমৎকার অভিজ্ঞতা।",
            "locationEn": "Gaibandha town",
            "locationBn": "গাইবান্ধা শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Gaibandha%20old%20town%20and%20market%2C%20Gaibandha%20town"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Balashi Ghat",
            "nameBn": "বালাসী ঘাট",
            "categoryEn": "Mighty Brahmaputra Waterfront & Sunset Beach",
            "categoryBn": "মনোরম ব্রহ্মপুত্র নদীতীর ও পর্যটন ঘাট",
            "descEn": "Balashi Ghat in Fulchhari Upazila is the most renowned and scenic riverfront tourist destination in Gaibandha, resting gracefully on the bank of the colossal Brahmaputra River. Once functioning as a major railway ferry transit hub connecting north Bengal with Mymensingh, the ghat today attracts nature lovers with its vast horizon of sparkling waters and cool river breezes. Visitors can hire motorized wooden boats to explore the expansive river channels and sandy islands, enjoying breathtaking panoramic views of sunset over the water. The paved shoreline embankment features viewing kiosks, riverside tea stalls, and local fish markets offering freshly caught hilsa and river catfish. It is a premier weekend recreational retreat for thousands of travelers.",
            "descBn": "গাইবান্ধার ফুলছড়িতে অবস্থিত ঐতিহ্যবাহী বালাসী ঘাট ব্রহ্মপুত্র নদের অপার সৌন্দর্য উপভোগের প্রধান পর্যটন কেন্দ্র। একসময়ের বিখ্যাত এই ফেরি ঘাটটি বর্তমানে প্রকৃতিপ্রেমীদের এক পরম তীর্থক্ষেত্রে পরিণত হয়েছে। এখান থেকে ব্রহ্মপুত্রের সুবিশাল জলরাশি এবং দিগন্তবিস্তৃত চরাঞ্চলের দৃশ্য চোখ জুড়িয়ে দেয়। পর্যটকরা দেশীয় ট্রলারে চড়ে নদীর বুকে ভেসে বেড়াতে পারেন এবং নদীর তাজা মাছ ভাজার চমৎকার স্বাদ নিতে পারেন। বিকেলে নদীপাড়ের শীতল বাতাসে সূর্যাস্ত দেখা এক অপার্থিব অনুভূতি এনে দেয়। গাইবান্ধা ভ্রমণে বালাসী ঘাট এক অপরিহার্য ও আনন্দময় গন্তব্য।",
            "locationEn": "Fulchhari, Gaibandha",
            "locationBn": "ফুলছড়ি, গাইবান্ধা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Balashi%20Ghat%2C%20Fulchhari%2C%20Gaibandha"
        },
        {
            "id": 2,
            "nameEn": "Teesta Riverbank",
            "nameBn": "তিস্তা নদীতীর",
            "categoryEn": "Pristine Northern Riverfront & Meandering Channels",
            "categoryBn": "নয়নাভিরাম তিস্তা নদীতীর ও সবুজ চরাঞ্চল",
            "descEn": "The Teesta Riverbank in Sundarganj Upazila offers visitors a tranquil encounters with one of Bengal's most legendary alpine rivers as it nears its confluence with the Brahmaputra. The river's sweeping braided streams flow over smooth sandbars, creating a dramatic landscape that changes with every season. During the autumn months, fluffy white kashbon flowers carpet the dry riverbeds, providing romantic backdrops for nature walks and photography. Friendly local boatmen ferry passengers in traditional wooden skiffs across crystal currents where fresh river breezes whisper through riverside reeds. It provides an authentic, quiet sanctuary for travelers seeking the undisturbed natural soul of northern Bengal.",
            "descBn": "সুন্দরগঞ্জের তিস্তা নদীর তীর উত্তরবঙ্গের এক অনন্য প্রাকৃতিক রূপের অধিকারী। হিমালয় থেকে নেমে আসা খরস্রোতা এই নদী তার রূপালী জলধারা ও বালুময় চরের জন্য বিখ্যাত। শরৎকালে নদীর চরে ফোটা শুভ্র কাশফুলের মেলা এক স্বপ্নিল পরিবেশের সৃষ্টি করে। নদীর দুই তীরে গ্রামীণ কৃষকদের কর্মব্যস্ততা এবং পালতোলা নৌকার ধীর পদচারণা মনকে ছুঁয়ে যায়। শহরের ব্যস্ততা ভুলে নির্জন নদীতীরে বসে শান্ত বাতাস ও জলের কলতান শুনতে প্রচুর পর্যটক এখানে আসেন। তিস্তার মনমাতানো নিসর্গ গাইবান্ধার প্রকৃতিকে করেছে অনন্য ও সমৃদ্ধ।",
            "locationEn": "Sundarganj and surrounding areas",
            "locationBn": "সুন্দরগঞ্জ, গাইবান্ধা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Teesta%20Riverbank%2C%20Sundarganj%20and%20surrounding%20areas"
        },
        {
            "id": 3,
            "nameEn": "Brahmaputra char landscapes",
            "nameBn": "ব্রহ্মপুত্রের সুবিশাল চরাঞ্চল",
            "categoryEn": "Dynamic River Island Expanses & Ecotourism",
            "categoryBn": "ব্রহ্মপুত্রের বিস্তীর্ণ বালুচর ও রোমাঞ্চকর জীবন",
            "descEn": "The Brahmaputra char landscapes spanning Fulchhari and Saghata Upazilas present an astonishing ecological tapestry of shifting sand islands born from the river's immense silt loads. These vast, golden island formations stretch for miles across the horizon, supporting thriving pastoral settlements, peanut fields, and herds of grazing buffalo. Exploring the chars by wooden river cruiser reveals the courageous, resilient lifestyle of char-dwellers who farm the fertile soils amidst untamed water frontiers. Flocks of river terns, plovers, and migratory geese populate the shallow sandbars, creating marvelous birdwatching opportunities. It is a world of breathtaking spatial freedom and elemental beauty unique to Bangladesh's mighty river deltas.",
            "descBn": "ফুলছড়ি ও সাঘাটা জুড়ে ব্রহ্মপুত্র নদের বুকে জেগে ওঠা বিস্তীর্ণ চরাঞ্চল এক অদ্ভুত ও রোমাঞ্চকর পৃথিবীর রূপ উপস্থাপন করে। মাইলের পর মাইল বিস্তৃত বালুচরে রয়েছে সবুজ চিনা-বাদাম ও ভুট্টার ক্ষেত, মহিষের বাথান এবং সাহসী চরবাসীর সহজ-সরল জীবনযাত্রা। নৌকায় চড়ে এই নির্জন চরগুলোতে ভ্রমণ এক পরম অ্যাডভেঞ্চারের অনুভূতি দেয়। নদীর বুক চিরে ভেসে ওঠা বালুকাবেলায় শত শত প্রজাতির বুনো পাখি ও অতিথি পাখির অবাধ বিচরণ দেখা যায়। দিগন্তখোলা নীল আকাশ ও ব্রহ্মপুত্রের উত্তাল জলরাশির মাঝে চরাঞ্চলের এই রূপ যে কোনো ভ্রমণকারীর মনকে মুগ্ধ করে।",
            "locationEn": "Fulchhari and Saghata",
            "locationBn": "ফুলছড়ি ও সাঘাটা, গাইবান্ধা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Brahmaputra%20char%20landscapes%2C%20Fulchhari%20and%20Saghata"
        },
        {
            "id": 4,
            "nameEn": "Ghagot Riverbank",
            "nameBn": "ঘাঘট নদীতীর",
            "categoryEn": "Urban Waterfront Promenade & Green Embankment",
            "categoryBn": "ঘাঘট নদীতীর ওয়াকওয়ে ও লেকভিউ চত্বর",
            "descEn": "The Ghagot Riverbank, which meanders peacefully through Gaibandha town, is the primary public recreational and leisure corridor for city residents. Paved pedestrian boulevards along the flood control dikes are shaded by dense mahogany and weeping willow trees, featuring comfortable benches and decorative streetlamps. Families, joggers, and young people gather in large numbers every morning and evening to enjoy the refreshing river breezes and watch small fishing boats cast their nets. Modern riverside cafes and open-air food courts nearby serve steaming tea and regional snacks against tranquil water views. It stands as a vital civic sanctuary that enriches urban life in Gaibandha.",
            "descBn": "গাইবান্ধা শহরের বুক চিরে বয়ে চলা শান্ত ঘাঘট নদীর তীর শহরবাসীর প্রাত্যহিক অবসর ও শরীরচর্চার প্রধান উন্মুক্ত চত্বর। নদীর পাড় বরাবর গড়ে তোলা পাকা ওয়াকওয়ে, বৃক্ষশোভিত ছায়াঘেরা পথ এবং বসার বেঞ্চ অত্যন্ত পরিচ্ছন্ন ও মনোরম পরিবেশ নিশ্চিত করেছে। প্রতিদিন সকালে ও বিকেলে হাজারো মানুষ এখানে মুক্ত বাতাসে হাঁটতে ও নদীর নির্মল পরিবেশ উপভোগ করতে আসেন। সন্ধ্যার পর নদীর বুকে মৃদু আলোর প্রতিচ্ছবি এবং পাশের মুখরোচক খাবারের দোকানগুলো পুরো এলাকাকে প্রাণবন্ত করে তোলে। গাইবান্ধা শহরের অন্যতম সুন্দর ও আরামদায়ক স্থান হিসেবে এটি সমাদৃত।",
            "locationEn": "Gaibandha town and district",
            "locationBn": "গাইবান্ধা শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Ghagot%20Riverbank%2C%20Gaibandha%20town%20and%20district"
        },
        {
            "id": 5,
            "nameEn": "Saghata countryside and river views",
            "nameBn": "সাঘাটা পল্লি ও নদী মোহনা নিসর্গ",
            "categoryEn": "Picturesque Rural Plains & River Confluence",
            "categoryBn": "মনোরম গ্রামীণ শস্যক্ষেত ও যমুনা মোহনা",
            "descEn": "The Saghata countryside in southern Gaibandha presents an idyllic panorama where fertile green agricultural plains gently meet the sprawling channels of the lower Brahmaputra and Jamuna basin. Quaint village homesteads nestled under groves of betel nut palms, mango trees, and bamboo groves border shimmering water canals crisscrossing the landscape. Visitors traveling along the scenic rural roads encounter traditional fishing cooperatives, thriving chili drying fields, and warmhearted village communities. Elevated river overlooks offer breathtaking views of passing cargo barges and passenger wooden launches plying the regional waterways. It is a serene, restorative destination for travelers seeking genuine pastoral beauty.",
            "descBn": "গাইবান্ধার সর্বদক্ষিণে অবস্থিত সাঘাটার পল্লি নিসর্গ নদী ও গ্রামীণ সবুজের এক অপূর্ব মিলনমেলা। যমুনা ও ব্রহ্মপুত্রের সঙ্গমস্থলের নিকটবর্তী এই অঞ্চলের সুজলা-সুফলা ফসলের মাঠ, নারিকেল-সুপারির বাগান এবং মাটির শান্ত কুটির মনকে জুড়িয়ে দেয়। নদীর চরে চরে লাল মরিচ শুকানোর দৃশ্য এবং কৃষকদের কর্মমুখর জীবনযাত্রা অত্যন্ত প্রাণবন্ত। নদীপাড়ের উঁচু বাঁধ থেকে দিগন্তবিস্তৃত নদী ও ভেসে চলা মালবাহী জাহাজের দৃশ্য দেখতে প্রচুর মানুষ এখানে আসেন। নির্ভেজাল গ্রামীণ সৌন্দর্য ও নদীমাতৃক বাংলার সরল রূপ উপভোগ করতে সাঘাটা এক চমৎকার পর্যটন গন্তব্য।",
            "locationEn": "Saghata, Gaibandha",
            "locationBn": "সাঘাটা, গাইবান্ধা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Saghata%20countryside%20and%20river%20views%2C%20Saghata%2C%20Gaibandha"
        }
    ]
}

# 9. RANGPUR
rangpur = {
    "slug": "rangpur",
    "en": "Rangpur",
    "bn": "রংপুর",
    "hero_title_en": "Rangpur Palatial Majesty & Cultural Capital",
    "hero_title_bn": "রংপুরের তাজহাট রাজবাড়ি ও বরেন্দ্র গৌরব",
    "hero_sub_en": "Magnificent neoclassical Tajhat Palace, centennial Carmichael College campus, and Begum Rokeya memorial.",
    "hero_sub_bn": "সুরম্য তাজহাট রাজপ্রাসাদ, শতবর্ষী কারমাইকেল কলেজ ও মহীয়সী নারী বেগম রোকেয়ার স্মৃতিধন্য পুণ্যভূমি।",
    "tagline_en": "The historic metropolitan and cultural capital of northern Bangladesh, world-renowned for the monumental neoclassical Tajhat Palace, pioneer feminist Begum Rokeya's heritage, and distinguished educational citadels.",
    "tagline_bn": "উত্তরবঙ্গের ঐতিহ্যবাহী বিভাগীয় ও সাংস্কৃতিক রাজধানী, যা রাজকীয় তাজহাট রাজপ্রাসাদ, নারী জাগরণের অগ্রদূত বেগম রোকেয়ার জন্মভূমি এবং শতবর্ষী কারমাইকেল কলেজের জন্য আন্তর্জাতিকভাবে খ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/rangpur/carousel-1.webp",
            "titleEn": "Tajhat Palace Neoclassical Architectural Wonder",
            "titleBn": "তাজহাট রাজপ্রাসাদ ও মার্বেল পাথরের সিঁড়ি",
            "subtitleEn": "Colossal early-twentieth-century palace in Rangpur city featuring classical Greco-Roman colonnades and landscaped royal grounds",
            "subtitleBn": "রংপুর শহরের প্রাণকেন্দ্রে অবস্থিত সুউচ্চ মার্বেল পাথরের রাজপ্রাসাদ, যা উত্তরবঙ্গের স্থাপত্যকলার শ্রেষ্ঠ মুকুট"
        },
        {
            "id": 2,
            "image": "images/districts/rangpur/carousel-2.webp",
            "titleEn": "Carmichael College Historic Red-Brick Campus",
            "titleBn": "শতবর্ষী কারমাইকেল কলেজের রাজকীয় ক্যাম্পাস",
            "subtitleEn": "Colonial academic masterpiece founded in 1916 featuring magnificent Indo-Saracenic brick arches and grand domes",
            "subtitleBn": "১৯১৬ সালে প্রতিষ্ঠিত ইন্দো-সারাসেনিক স্থাপত্যের সুরম্য লাল ইটের বিদ্যাপীঠ, যা শিক্ষার ঐতিহাসিক কেন্দ্র"
        },
        {
            "id": 3,
            "image": "images/districts/rangpur/carousel-3.webp",
            "titleEn": "Begum Rokeya Memorial Centre & Ancestral Estate",
            "titleBn": "মহীয়সী বেগম রোকেয়া স্মৃতি কেন্দ্র",
            "subtitleEn": "Hallowed birthplace of the pioneer of South Asian women's liberation and education in Pairabondh",
            "subtitleBn": "পায়রাবন্দে অবস্থিত উপমহাদেশে নারী জাগরণের অগ্রদূত বেগম রোকেয়ার জন্মভিটা ও স্মৃতি জাদুঘর"
        },
        {
            "id": 4,
            "image": "images/districts/rangpur/carousel-4.webp",
            "titleEn": "Chikli Water Park & Serene Urban Lake",
            "titleBn": "চিকলি ওয়াটার পার্ক ও নান্দনিক লেক",
            "subtitleEn": "Picturesque city lake sanctuary offering speedboat rides, illuminated walkways, and waterfront dining",
            "subtitleBn": "রংপুর শহরের আধুনিক বিনোদন লেক, যেখানে স্পিডবোটিং ও শান্ত জলরাশির হাওয়া উপভোগ করা যায়"
        },
        {
            "id": 5,
            "image": "images/districts/rangpur/carousel-5.webp",
            "titleEn": "Vinnya Jagat Sprawling Amusement Park",
            "titleBn": "ভিন্ন জগত সুবিশাল ইকোপার্ক ও বিনোদন কেন্দ্র",
            "subtitleEn": "Massive regional family theme park in Rangpur Sadar featuring landscaped gardens, planetarium, and recreation lakes",
            "subtitleBn": "সবুজে ঘেরা উত্তরবঙ্গের বৃহত্তম বিনোদন পার্ক, যেখানে পরিবার নিয়ে আনন্দময় অবকাশ যাপন করা যায়"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Tajhat Palace",
            "nameBn": "তাজহাট রাজবাড়ি (তাজহাট জমিদার বাড়ি)",
            "categoryEn": "Neoclassical Imperial Palace & Archaeological Museum",
            "categoryBn": "নয়নাভিরাম রাজপ্রাসাদ ও সরকারি প্রত্নতাত্ত্বিক জাদুঘর",
            "descEn": "Tajhat Palace, situated in the southern outskirts of Rangpur city, is one of the most magnificent neoclassical royal palaces in South Asia. Constructed in the early twentieth century by Maharaja Kumar Gopal Lal Roy, this colossal two-story palace features a sweeping central marble staircase, an imposing semi-octagonal ribbed dome, and majestic Corinthian colonnades modeled after classical Greco-Roman architecture. The palace facades stretch for hundreds of feet across manicured royal gardens adorned with ornamental fountains, date palm avenues, and broad freshwater moats. Today, the palace houses the government archaeological museum, displaying priceless eleventh-century black basalt Buddhist and Hindu sculptures, ancient Sanskrit manuscripts, and Mughal gold coins. It stands as an iconic symbol of northern Bengal's palatial elegance and royal history.",
            "descBn": "রংপুর শহরের দক্ষিণ প্রান্তে অবস্থিত তাজহাট রাজবাড়ি সমগ্র দক্ষিণ এশিয়ার অন্যতম দৃষ্টিনন্দন ও সুরম্য রাজপ্রাসাদ। বিংশ শতাব্দীর প্রারম্ভে মহারাজা গোপাল লাল রায় কর্তৃক নির্মিত এই প্রাসাদটিতে রয়েছে গ্রিক-রোমান স্থাপত্যের অনুকরণে বিশাল মার্বেল পাথরের রাজকীয় সিঁড়ি, আকাশচুম্বী গম্বুজ এবং সুউচ্চ করিন্থিয়ান স্তম্ভ। প্রাসাদের চারপাশ ঘিরে রয়েছে নয়নাভিরাম ফুলের বাগান, নারিকেল বীথি ও বিশাল চারটি রাজদীঘি। বর্তমানে এই প্রাসাদে সরকারি প্রত্নতাত্ত্বিক জাদুঘর স্থাপন করা হয়েছে, যেখানে পাল ও সেন আমলের দুর্লভ কষ্টিপাথরের ভাস্কর্য এবং প্রাচীন পাণ্ডুলিপি সংরক্ষিত আছে। উত্তরবঙ্গের রাজকীয় আভিজাত্য ও ঐতিহ্যের শ্রেষ্ঠ স্মারক হিসেবে তাজহাট রাজবাড়ি বিশ্বজুড়ে সমাদৃত।",
            "locationEn": "Tajhat, Rangpur city",
            "locationBn": "তাজহাট, রংপুর শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Tajhat%20Palace%2C%20Tajhat%2C%20Rangpur%20city"
        },
        {
            "id": 2,
            "nameEn": "Carmichael College historic campus",
            "nameBn": "কারমাইকেল কলেজ ঐতিহাসিক ক্যাম্পাস",
            "categoryEn": "Centennial Indo-Saracenic Academic Monument",
            "categoryBn": "শতবর্ষী রাজকীয় ইন্দো-সারাসেনিক স্থাপত্যের ক্যাম্পাস",
            "descEn": "Carmichael College, established in 1916 at Lalbagh in Rangpur, is an architectural and academic jewel of international renown. Spread over an extraordinary 300-acre lush green campus, the college's main building is an imposing red-brick palace built in the Indo-Saracenic architectural style, integrating Mughal ribbed domes, Mughal jali screens, and British colonial archways. The foundation was laid by Lord Carmichael, then Governor of Bengal, with generous financial patronage from northern Bengal's prominent landed gentry. The campus features majestic tree-lined avenues of ancient mahogany and rain trees, botanical water tanks, and historic student hostels that fostered generations of Bangladesh's leading scholars, jurists, and liberation war heroes. It remains one of the most intellectually revered and architecturally breathtaking campuses in Asia.",
            "descBn": "১৯১৬ সালে প্রতিষ্ঠিত রংপুরের কারমাইকেল কলেজ উপমহাদেশের অন্যতম প্রাচীন, বৃহত্তম ও স্থাপত্যশৈলীতে সমৃদ্ধ শিক্ষা প্রতিষ্ঠান। প্রায় ৩০০ একর সবুজ বনানী ঘেরা এই ক্যাম্পাসের প্রধান ভবনটি ইন্দো-সারাসেনিক স্থাপত্যরীতির এক অপূর্ব রাজপ্রাসাদ, যার ছাদে রয়েছে একাধিক মুঘল ধাঁচের গম্বুজ ও চমৎকার লাল ইটের খিলান। বাংলার তৎকালীন গভর্নর লর্ড কারমাইকেলের নামানুসারে প্রতিষ্ঠিত এই বিদ্যাপীঠ নির্মাণে উত্তরবঙ্গের জমিদারগণ অকাতরে অর্থ দান করেছিলেন। ছায়াঘেরা শতবর্ষী মেহগনি গাছের বীথি, সুবিশাল খেলার মাঠ ও ঐতিহ্যবাহী পুকুর ক্যাম্পাসটিকে এক অনন্য রূপ দিয়েছে। শিক্ষা ও স্থাপত্যের এক রাজকীয় মিলনমেলা হিসেবে এই কলেজ প্রাঙ্গণ পর্যটকদের মুগ্ধ করে।",
            "locationEn": "Lalbagh, Rangpur",
            "locationBn": "লালবাগ, রংপুর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Carmichael%20College%20historic%20campus%2C%20Lalbagh%2C%20Rangpur"
        },
        {
            "id": 3,
            "nameEn": "Begum Rokeya Memorial Centre",
            "nameBn": "বেগম রোকেয়া স্মৃতি কেন্দ্র",
            "categoryEn": "Pioneer Feminist Heritage & Memorial Complex",
            "categoryBn": "নারী জাগরণের অগ্রদূত বেগম রোকেয়ার জন্মভিটা ও স্মৃতি কেন্দ্র",
            "descEn": "The Begum Rokeya Memorial Centre at Pairabondh in Mithapukur Upazila is the hallowed ancestral birthplace of Begum Rokeya Sakhawat Hossain (1880–1932), the pioneering social reformer, essayist, and founder of women's liberation in South Asia. The memorial complex includes an educational auditorium, seminar library, research gallery, and dedicated handicraft training center for women. Adjacent to the complex stand the preserved brick foundations and boundary walls of the ancestral Sabir family mansion where the visionary writer was raised in strict seclusion before breaking social barriers with her revolutionary feminist texts like 'Sultana's Dream'. Visiting the tranquil grounds is a profoundly moving pilgrimage celebrating courage, intellectual freedom, and human equality.",
            "descBn": "রংপুরের মিঠাপুকুর উপজেলার পায়রাবন্দে অবস্থিত বেগম রোকেয়া স্মৃতি কেন্দ্রটি ভারতীয় উপমহাদেশে নারী জাগরণ ও নারী শিক্ষার অগ্রদূত মহীয়সী বেগম রোকেয়া সাখাওয়াত হোসেনের স্মৃতিবিজড়িত পুণ্যভূমি। ১৮৮০ সালে এই পায়রাবন্দের বনেদি সাবের পরিবারে জন্মগ্রহণ করেছিলেন এই কালজয়ী নারী। স্মৃতি কেন্দ্রটিতে রয়েছে একটি আধুনিক জাদুঘর, সমৃদ্ধ পাঠাগার, গবেষণা কেন্দ্র এবং রোকেয়ার জীবন ও সৃষ্টির স্মারকসমূহ। পাশে সংরক্ষিত রয়েছে তাঁর প্রাচীন জন্মভিটার ইটের ভিত ও দেয়াল। সমাজ সংস্কার, নারীর ক্ষমতায়ন ও মানবতার পক্ষে রোকেয়ার আজীবন সংগ্রামকে স্মরণ করতে দেশ-বিদেশের হাজার হাজার মানুষ প্রতিদিন এখানে শ্রদ্ধা জানাতে আসেন।",
            "locationEn": "Pairabondh, Mithapukur",
            "locationBn": "পায়রাবন্দ, মিঠাপুকুর, রংপুর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Begum%20Rokeya%20Memorial%20Centre%2C%20Pairabondh%2C%20Mithapukur"
        },
        {
            "id": 4,
            "nameEn": "Kellaband Mosque",
            "nameBn": "কেল্লাবন্দ ঐতিহাসিক মসজিদ",
            "categoryEn": "Ancient Sultanate-Mughal Fortified Mosque",
            "categoryBn": "মুঘল আমলের প্রাচীন কেল্লা মসজিদ",
            "descEn": "Kellaband Mosque is a historic Islamic monument located in the Kellaband area of Rangpur, reflecting the strategic military and spiritual presence during the Mughal expansion into northern Bengal. Constructed with heavy kilned terracotta bricks and thick lime mortar, the mosque features sturdy corner minarets, arched entryways, and traditional bulbous domes built to withstand seasonal tremors and floods. The interior prayer chamber maintains a cool, tranquil sanctuary decorated with recessed prayer niches (mihrabs) and floral geometric cornices. The adjacent ancient water tank and verdant village trees enhance the spiritual stillness of the historic grounds. It remains an active and beloved community prayer center anchoring local heritage pride.",
            "descBn": "রংপুরের কেল্লাবন্দ এলাকায় অবস্থিত এই প্রাচীন মসজিদটি মধ্যযুগীয় সামরিক ঘাঁটি ও মুঘল স্থাপত্যরীতির এক অনন্য ঐতিহাসিক নিদর্শন। প্রাচীনকালে এই অঞ্চলে সেনা ছাউনি বা কেল্লা থাকার কারণে মসজিদটির নামকরণ 'কেল্লাবন্দ মসজিদ' হয়েছিল বলে জানা যায়। চুন-সুরকি ও পোড়ামাটির নিপুণ গাঁথুনিতে নির্মিত এই মসজিদে রয়েছে সুদৃঢ় গম্বুজ, খিলানযুক্ত প্রবেশদ্বার এবং কারুকার্যময় মেহরাব। মসজিদের ভেতরের শীতল ও আধ্যাত্মিক আবহ মুসল্লি ও দর্শনার্থীদের পরম শান্তি এনে দেয়। রংপুর অঞ্চলে ইসলামি ঐতিহ্যের প্রাচীনতম সাক্ষী হিসেবে এই মসজিদটি অত্যন্ত তাৎপর্যপূর্ণ।",
            "locationEn": "Rangpur district; verify locality",
            "locationBn": "কেল্লাবন্দ, রংপুর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kellaband%20Mosque%2C%20Rangpur%20district%3B%20verify%20locality"
        },
        {
            "id": 5,
            "nameEn": "Rangpur Town Hall historic building",
            "nameBn": "রংপুর ঐতিহাসিক টাউন হল",
            "categoryEn": "Nineteenth-Century Civic Cultural Monument",
            "categoryBn": "ঊনবিংশ শতাব্দীর ঐতিহাসিক সাংস্কৃতিক কেন্দ্র ও মুক্তমঞ্চ",
            "descEn": "The Rangpur Town Hall, constructed in the late nineteenth century in the heart of Rangpur city, is an iconic civic and cultural landmark that has served as the nerve center for northern Bengal's intellectual, political, and theatrical life. Built with elegant Victorian colonial brick architecture, the building features arched colonnaded verandas, high clerestory windows, and a historic performance auditorium where classic Bengali dramas, political rallies of the independence movement, and literary symposia took place. Luminaries including Netaji Subhas Chandra Bose and Rabindranath Tagore were hosted in this venerated assembly hall. It stands today as an enduring monument to Rangpur's proud cultural consciousness, democratic activism, and artistic vigor.",
            "descBn": "রংপুর শহরের কেন্দ্রস্থলে অবস্থিত রংপুর টাউন হল ভবনটি ঊনবিংশ শতাব্দীর শেষভাগে নির্মিত এক ঐতিহাসিক সাংস্কৃতিক ও রাজনৈতিক মিলনকেন্দ্র। ব্রিটিশ ভিক্টোরিয়ান স্থাপত্যরীতিতে লাল ইটে নির্মিত এই ভবনে রয়েছে দৃষ্টিনন্দন খিলান, প্রশস্ত বারান্দা এবং বিশাল মিলনায়তন। অবিভক্ত বাংলা থেকে শুরু করে ভাষা আন্দোলন ও মহান মুক্তিযুদ্ধ পর্যন্ত উত্তরবঙ্গের সব ঐতিহাসিক রাজনৈতিক সমাবেশ ও নাট্য আন্দোলনের প্রাণকেন্দ্র ছিল এই টাউন হল। এখানে পদার্পণ করেছিলেন নেতাজি সুভাষচন্দ্র বসু, বিশ্বকবি রবীন্দ্রনাথ ঠাকুরসহ বহু বিশ্ববরেণ্য ব্যক্তিত্ব। রংপুরের সাংস্কৃতিক চেতনা ও গণতান্ত্রিক ঐতিহ্যের জীবন্ত প্রতীক হিসেবে এই ভবনটি গর্বের সাথে দাঁড়িয়ে আছে।",
            "locationEn": "Rangpur city",
            "locationBn": "রংপুর শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Rangpur%20Town%20Hall%20historic%20building%2C%20Rangpur%20city"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Vinnya Jagat amusement park",
            "nameBn": "ভিন্ন জগত ইকোপার্ক",
            "categoryEn": "Mega Family Amusement Park & Resort",
            "categoryBn": "উত্তরবঙ্গের বৃহত্তম পরিবারিক থিম পার্ক ও রিসোর্ট",
            "descEn": "Vinnya Jagat, situated in Khaleya Ganjipur within Rangpur Sadar, is the premier mega-scale amusement park and eco-resort in northern Bangladesh, covering over 100 acres of beautifully landscaped grounds. The park features an impressive array of family attractions, including the country's first private planetarium, 3D and 9D virtual reality cinemas, roller coasters, cable car ropeways, and an extensive amusement lake with pedal boats. Sprawling botanical gardens, miniature world landmark replicas, a mini-zoo housing exotic wildlife, and comfortable resort cottages make it a favorite holiday getaway for visitors from all across the nation. It provides an all-inclusive world of wholesome family entertainment and leisure.",
            "descBn": "রংপুরের গঞ্জিপুরে প্রায় ১০০ একর সুবিশাল এলাকা জুড়ে গড়ে ওঠা 'ভিন্ন জগত' উত্তরবঙ্গের সর্ববৃহৎ ও সবচেয়ে আধুনিক বিনোদন কেন্দ্র। সবুজে শ্যামল প্রাকৃতিক পরিবেশে তৈরি এই পার্কে রয়েছে দেশের প্রথম বেসরকারি প্ল্যানেটোরিয়াম, রোলার কোস্টার, ক্যাবল কার, থ্রিডি মুভি থিয়েটার এবং প্যাডেল বোটিংয়ের জন্য বিশাল লেক। বিশ্বের বিখ্যাত স্মৃতিস্তম্ভের রেপ্লিকা, মিনি চিড়িয়াখানা এবং শিশুদের অসংখ্য রোমাঞ্চকর রাইড পার্কটিকে দারুণ আকর্ষণীয় করেছে। দূর-দূরান্ত থেকে আসা পর্যটকদের জন্য এখানে রয়েছে আধুনিক কটেজ ও অবকাশ যাপনের সুব্যবস্থা। পরিবার ও বন্ধুদের নিয়ে আনন্দময় দিন কাটাতে ভিন্ন জগত এক অনন্য ঠিকানা।",
            "locationEn": "Rangpur Sadar area",
            "locationBn": "রংপুর সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Vinnya%20Jagat%20amusement%20park%2C%20Rangpur%20Sadar%20area"
        },
        {
            "id": 2,
            "nameEn": "Chikli Water Park",
            "nameBn": "চিকলি ওয়াটার পার্ক ও বিনোদন লেক",
            "categoryEn": "Urban Lakeside Amusement & Speedboat Haven",
            "categoryBn": "আধুনিক বিনোদন লেক, স্পিডবোটিং ও ওয়াকওয়ে",
            "descEn": "Chikli Water Park, set surrounding the expansive Chikli Beel lake within Rangpur city, is the trendiest urban leisure destination in the division. The waterfront features thrilling speedboats, pontoon cruisers, and paddle boats gliding across sparkling open waters. Paved, tree-shaded pedestrian promenades wrap around the lake, furnished with viewing pavilions, illuminated fountains, and modern amusement rides for young children. Waterfront restaurants and street food gazebos serve sizzling kebabs and crispy snacks as families enjoy the refreshing evening lake breezes. It offers a lively, energetic civic haven that brings resort-style aquatic leisure directly into the urban center.",
            "descBn": "রংপুর শহরের প্রাণকেন্দ্রে সুবিশাল চিকলি বিলকে কেন্দ্র করে গড়ে ওঠা চিকলি ওয়াটার পার্ক স্থানীয় বাসিন্দা ও পর্যটকদের এক অন্যতম প্রধান বিনোদন কেন্দ্র। লেকের শান্ত জলে স্পিডবোটিং, প্যাডেল বোটিং এবং লেকভিউ ওয়াকওয়েতে হাঁটাচলা দারুণ এক বিনোদনমূলক আবহ তৈরি করে। শিশুদের জন্য রয়েছে বিভিন্ন আধুনিক রাইড এবং বড়দের জন্য লেকপাড়ে বসে মুক্ত হাওয়া উপভোগের সুন্দর ব্যবস্থা। সন্ধ্যায় বর্ণিল ফোয়ারা ও চমৎকার আলোকসজ্জা পুরো লেককে এক মায়াবী রূপ দেয়। শহরের ভেতরেই জল আর সবুজের অপূর্ব মেলবন্ধন উপভোগ করতে চিকলি ওয়াটার পার্ক এক চমৎকার স্থান।",
            "locationEn": "Rangpur city",
            "locationBn": "রংপুর শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Chikli%20Water%20Park%2C%20Rangpur%20city"
        },
        {
            "id": 3,
            "nameEn": "Rangpur Zoo",
            "nameBn": "রংপুর চিড়িয়াখানা",
            "categoryEn": "Zoological Gardens & Botanical Sanctuary",
            "categoryBn": "ঐতিহাসিক চিড়িয়াখানা ও পরিবারিক উদ্যান",
            "descEn": "Rangpur Zoo, located centrally in Rangpur city, is the second-largest zoological garden in Bangladesh, covering over 21 acres of serene, park-like grounds. Established in 1989, the zoo is home to numerous rare and endangered animal species, including majestic Royal Bengal tigers, African lions, spotted deer, black bears, saltwater crocodiles, and an extensive aviary with colorful migratory and native birds. Giant shade trees, tranquil artificial ponds, and winding paved footpaths offer a peaceful, nature-filled walking environment for visitors of all generations. Educational signage and interactive viewing enclosures make it an essential recreational and learning destination for school excursions and family outings.",
            "descBn": "রংপুর শহরের কেন্দ্রস্থলে প্রায় ২১ একর জায়গা জুড়ে অবস্থিত রংপুর চিড়িয়াখানা ঢাকার পর বাংলাদেশের দ্বিতীয় বৃহত্তম সরকারি চিড়িয়াখানা। ১৯৮৯ সালে প্রতিষ্ঠিত এই চিড়িয়াখানায় রয়েছে রয়েল বেঙ্গল টাইগার, সিংহ, চিত্রা হরিণ, কালো ভাল্লুক, ময়ূর, কুমিরসহ দেশি-বিদেশি বহু প্রজাতির পশুপাখি। চারপাশের ছায়াঘেরা বিশাল বৃক্ষরাজি ও সুদৃশ্য লেক চিড়িয়াখানা প্রাঙ্গণকে এক চমৎকার প্রাকৃতিক উদ্যানের রূপ দিয়েছে। বিশেষ করে শিশু-কিশোর ও পরিবারের সদস্যদের জন্য এটি জীববৈচিত্র্য দর্শন ও আনন্দদায়ক সময় কাটানোর এক অত্যন্ত শিক্ষণীয় ও জনপ্রিয় স্থান।",
            "locationEn": "Rangpur city",
            "locationBn": "রংপুর শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Rangpur%20Zoo%2C%20Rangpur%20city"
        },
        {
            "id": 4,
            "nameEn": "Teesta Barrage regional excursion",
            "nameBn": "তিস্তা ব্যারেজ আঞ্চলিক পর্যটন কেন্দ্র",
            "categoryEn": "Monumental Hydraulic Dam & Panoramic Lake",
            "categoryBn": "দেশের বৃহত্তম সেচ প্রকল্প ও তিস্তা নদীর দিগন্ত",
            "descEn": "The Teesta Barrage excursion, located at Dalia near the Rangpur-Lalmonirhat border, is a celebrated regional sightseeing destination centering on the country's largest irrigation project. The monumental concrete barrage spans 615 meters across the roaring Teesta River, containing 44 massive sluice gates that control irrigation waters for northern agricultural plains. Upstream of the dam, the river swells into a vast artificial reservoir resembling an inland sea, framed by distant views of the Himalayan foothills on exceptionally clear days. Downstream, sand islands and wooden fishing boats create picturesque riverine vistas. Visitors enjoy brisk walks across the barrage walkway, sampling freshly fried river fish at local waterside restaurants.",
            "descBn": "রংপুর ও লালমনিরহাট সীমান্তের ডালিয়ায় অবস্থিত তিস্তা ব্যারেজ বাংলাদেশের সর্ববৃহৎ সেচ প্রকল্প এবং উত্তরবঙ্গের অন্যতম প্রধান পর্যটন আকর্ষণ। তিস্তা নদীর ওপর নির্মিত ৬১৫ মিটার দীর্ঘ এই ব্যারেজে রয়েছে ৪৪টি বিশালাকার স্লুইস গেট, যা বর্ষাকালে নদীর উত্তাল রূপকে এক রাজকীয় দৃশ্য দেয়। ব্যারেজের উজানে জমে থাকা বিশাল জলরাশি দেখতে ঠিক যেন সাগরের মতো মনে হয়। দূর-দূরান্ত থেকে আসা পর্যটকরা ব্যারেজের ওপর হেঁটে মুক্ত বাতাস উপভোগ করেন এবং স্থানীয় বাজারে নদীর টাটকা বৈরালী ও বোয়াল মাছ ভাজার স্বাদ নেন। প্রকৌশলবিদ্যা ও নদীপ্রকৃতির অপূর্ব রূপ দেখতে এটি এক অসাধারণ ভ্রমণস্থল।",
            "locationEn": "Dalia, Hatibandha, Lalmonirhat; outside Rangpur",
            "locationBn": "ডালিয়া, তিস্তা ব্যারেজ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Teesta%20Barrage%20regional%20excursion%2C%20Dalia%2C%20Hatibandha%2C%20Lalmonirhat%3B%20outside%20Rangpur"
        },
        {
            "id": 5,
            "nameEn": "Rangpur city parks and gardens",
            "nameBn": "রংপুর সুরভী উদ্যান ও সেন্ট্রাল পার্ক",
            "categoryEn": "Civic Botanical Garden & Promenade",
            "categoryBn": "সুরভী উদ্যান ও নাগরিক বিনোদন চত্বর",
            "descEn": "Rangpur City Parks and Gardens, anchored by the beloved Surobhi Uddan and adjacent municipal squares, provide the green civic soul of the metropolitan division. Filled with flowering shrubs, towering eucalyptus trees, well-trimmed hedges, and circular pedestrian tracks, the park serves as the gathering place for morning walkers, senior citizens, and cultural clubs. Colorful children's play corners, seasonal flower exhibitions, and open-air musical bandstands host lively community activities throughout the year. The aromatic scents of blooming night-jasmine and seasonal roses give Surobhi Uddan its poetic name and timeless charm. It is an indispensable oasis of tranquility within the bustling commercial rhythm of Rangpur city.",
            "descBn": "রংপুর শহরের প্রাণকেন্দ্রে অবস্থিত সুরভী উদ্যান শহরবাসীর প্রতিদিনের হাঁটাচলা, আড্ডা ও মানসিক প্রশান্তির সবচেয়ে জনপ্রিয় সবুজ চত্বর। হরেক রঙের ফুলের বাগান, সুদৃশ্য ফোয়ারা এবং ছায়াঘেরা পথ এই উদ্যানটিকে অত্যন্ত পরিচ্ছন্ন ও মনোরম রূপ দিয়েছে। প্রতিদিন ভোরে ও বিকেলে শহরের নানা বয়সের মানুষ এখানে শরীরচর্চা ও নির্মল বাতাস উপভোগ করতে আসেন। শিশুদের খেলাধুলার জন্য রয়েছে বিশেষ কর্নার এবং বিভিন্ন জাতীয় দিবসে এখানে বসে বর্ণাঢ্য সাংস্কৃতিক আসর। ইট-পাথরের শহরের মাঝে এক টুকরো স্নিগ্ধ সবুজের পরশ পেতে সুরভী উদ্যান অতুলনীয়।",
            "locationEn": "Rangpur city",
            "locationBn": "রংপুর শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Rangpur%20city%20parks%20and%20gardens%2C%20Rangpur%20city"
        }
    ]
}

data_dict = {
    "joypurhat": joypurhat,
    "sunamganj": sunamganj,
    "gaibandha": gaibandha,
    "rangpur": rangpur
}

for slug, data in data_dict.items():
    fp = f"scripts/data_districts_17/{slug}.py"
    with open(fp, "w", encoding="utf-8") as f:
        f.write(f"# -*- coding: utf-8 -*-\nDISTRICT_DATA = {json.dumps(data, ensure_ascii=False, indent=4)}\n")
    print(f"Wrote {fp}")

print("Batch 6 to 9 complete!")
