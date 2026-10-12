# -*- coding: utf-8 -*-
"""
curate_district_places.py
Master dataset generator for the 12 target districts:
Narayanganj, Feni, Cumilla, Bhola, Barishal, Chattogram, Sylhet, Noakhali, Rajshahi, Cox's Bazar, Kurigram, Dinajpur.
Each spot has:
- Exact name from PDF (with Bengali translation)
- Expanded 5-6 line comprehensive description in English
- Proper, natural Bengali translation of the description
- Exact location from PDF (with Bengali translation)
- Exact Google Maps direct link from PDF
- Category / tag (EN + BN)
- Search query terms for automatic image sourcing and fallback generation
"""

TARGET_DISTRICTS = [
    {
        "slug": "narayanganj",
        "en": "Narayanganj",
        "bn": "নারায়ণগঞ্জ",
        "hero_title_en": "Narayanganj Heritage & River Hub",
        "hero_title_bn": "নারায়ণগঞ্জের ঐতিহাসিক ঐতিহ্য ও নদীবন্দর",
        "hero_sub_en": "Ancient Golden Bengal capital of Sonargaon, medieval river fortifications, and Shitalakshya trade corridors.",
        "hero_sub_bn": "সোনারগাঁয়ের প্রাচীন রাজধানী, মধ্যযুগীয় নদী দুর্গ ও শীতলক্ষ্যার সমৃদ্ধ বাণিজ্যিক ঐতিহ্য।",
        "tagline_en": "The legendary medieval capital of Subah Bangla and bustling riverine port, uniting centuries of merchant prosperity and Mughal river defense.",
        "tagline_bn": "সুবে বাংলার ঐতিহাসিক প্রাচীন রাজধানী সোনারগাঁও ও প্রাণবন্ত নদীবন্দর, যেখানে শতাব্দীর বণিক সমৃদ্ধি ও মুঘল নদী প্রতিরক্ষার স্মারক বিদ্যমান।",
        "carousel": [
            {
                "id": 1,
                "image": "images/districts/narayanganj/carousel-1.webp",
                "titleEn": "Panam Nagar Merchant Mansions",
                "titleBn": "পানাম নগরের ঐতিহাসিক বণিক অট্টালিকা",
                "subtitleEn": "19th-century colonial brick street of wealthy textile merchants in Sonargaon",
                "subtitleBn": "সোনারগাঁওয়ে ধনী মসলিন ও বস্ত্র ব্যবসায়ীদের ১৯শ শতকের ঔপনিবেশিক সুরম্য নগরী"
            },
            {
                "id": 2,
                "image": "images/districts/narayanganj/carousel-2.webp",
                "titleEn": "Folk Art & Crafts Foundation",
                "titleBn": "বাংলাদেশ লোক ও কারুশিল্প ফাউন্ডেশন",
                "subtitleEn": "Zainul Abedin museum preserving traditional Jamdani, terracotta, and folk woodwork",
                "subtitleBn": "শিল্পাচার্য জয়নুল আবেদিন প্রতিষ্ঠিত জামদানি, পোড়ামাটি ও লোকশিল্পের জাদুঘর"
            },
            {
                "id": 3,
                "image": "images/districts/narayanganj/carousel-3.webp",
                "titleEn": "Sonakanda & Hajiganj Forts",
                "titleBn": "সোনাকান্দা ও হাজীগঞ্জ মুঘল জলদুর্গ",
                "subtitleEn": "17th-century riverside cannon bastions guarding against Portuguese and Magh pirates",
                "subtitleBn": "পর্তুগিজ ও মগ জলদস্যু প্রতিহত করতে শীতলক্ষ্যা তীরে নির্মিত মুঘল কামান বুরুজ"
            },
            {
                "id": 4,
                "image": "images/districts/narayanganj/carousel-4.webp",
                "titleEn": "Murapara Palace & Lakes",
                "titleBn": "মুড়াপাড়া জমিদার প্রাসাদ ও দীঘি",
                "subtitleEn": "Grand Greco-Roman columns and symmetrical verandas of the Rupganj zamindars",
                "subtitleBn": "গ্রেকো-রোমান স্থাপত্যের সুবিশাল স্তম্ভ ও রূপগঞ্জের জমিদারদের রাজকীয় প্রাসাদ"
            },
            {
                "id": 5,
                "image": "images/districts/narayanganj/carousel-5.webp",
                "titleEn": "Zinda Park Botanical Sanctuary",
                "titleBn": "জিন্দা পার্ক ইকো ও বোটানিক্যাল উদ্যান",
                "subtitleEn": "Community-driven eco-retreat featuring lush pine groves, wooden bridges, and serene lakes",
                "subtitleBn": "ঝাউবন, কাঠের সাঁকো ও শান্ত সরোবরে ঘেরা নান্দনিক কমিউনিটি ইকো পার্ক"
            }
        ],
        "hist": [
            {
                "id": 1,
                "nameEn": "Panam Nagar",
                "nameBn": "পানাম নগর",
                "categoryEn": "Historic Merchant City",
                "categoryBn": "ঐতিহাসিক বণিক নগরী",
                "descEn": "Panam Nagar is one of the most historically significant ruined cities in Bangladesh, flourishing as a prominent trading hub under the Sonargaon sultanate and colonial eras. Built along a single narrow street stretching roughly 600 meters, it features over fifty remarkably preserved brick mansions exhibiting Indo-Saracenic, European Neoclassical, and local Bengali architectural styles. Wealthy Hindu cotton and muslin merchants constructed these grand two- and three-story residences with decorative cast-iron brackets, imported porcelain inlays, and geometric arched balconies. The atmospheric corridor offers visitors a spellbinding journey through 19th-century mercantile grandeur. Today, it remains an internationally recognized conservation priority and architectural wonderland.",
                "descBn": "পানাম নগর বাংলাদেশের অন্যতম সুপ্রাচীন ও সংরক্ষিত ঐতিহাসিক নগরী, যা সোনারগাঁওয়ের সুলতানি ও ব্রিটিশ ঔপনিবেশিক আমলে বিখ্যাত বাণিজ্য কেন্দ্র হিসেবে গড়ে ওঠে। প্রায় ৬০০ মিটার দীর্ঘ একটিমাত্র রাস্তার দুপাশে অবস্থিত অর্ধশতাধিক ইন্দো-সারাসেনিক ও ইউরোপীয় নিওক্লাসিক্যাল স্থাপত্যের সুরম্য অট্টালিকা একে অনন্য রূপ দিয়েছে। ধনী মসলিন ও সুতা ব্যবসায়ীদের নির্মিত এই দোতলা ও তিনতলা ভবনে রয়েছে নকশাদার লোহার রেলিং, রঙিন চিনামাটির কারুকাজ ও অপূর্ব খিলানযুক্ত বারান্দা। প্রাচীন স্থাপত্যের এই নির্জন পথ ধরে হাঁটলে উনিশ শতকের আভিজাত্য প্রত্যক্ষ করা যায়। এটি বর্তমানে একটি সুরক্ষিত জাতীয় প্রত্নতাত্ত্বিক ঐতিহ্য।",
                "locationEn": "Panam, Sonargaon Upazila",
                "locationBn": "পানাম, সোনারগাঁও উপজেলা",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Panam+Nagar+Sonargaon+Narayanganj%2C+Bangladesh"
            },
            {
                "id": 2,
                "nameEn": "Bangladesh Folk Art and Crafts Foundation",
                "nameBn": "বাংলাদেশ লোক ও কারুশিল্প ফাউন্ডেশন",
                "categoryEn": "Folk Heritage Museum",
                "categoryBn": "লোক ও কারুশিল্প জাদুঘর",
                "descEn": "Founded in 1975 by pioneer artist Shilpacharya Zainul Abedin in the historic Boro Sardar Bari of Sonargaon, this sprawling 50-hectare cultural complex preserves Bengal's artisanal genius. The beautifully restored palace compound showcases authentic handwoven Jamdani sarees, Kantha quilts, ornate copperware, folk terracotta pottery, and carved wooden puppets. Live craft demonstrations allow visitors to observe master weavers operating traditional pit-looms under shady groves of centuries-old mahogany trees. The complex also features an expansive ornamental lotus pond where traditional wooden country boats rest against landscaped banks. An annual folk fair enlivens the grounds with traditional Baul musicians, rural artisans, and folk culinary delicacies.",
                "descBn": "১৯৭৫ সালে শিল্পাচার্য জয়নুল আবেদিন কর্তৃক সোনারগাঁওয়ের ঐতিহাসিক বড় সর্দার বাড়িতে প্রতিষ্ঠিত এই সুপরিসর সাংস্কৃতিক কমপ্লেক্সটি বাংলার লোকঐতিহ্য সংরক্ষণের জাতীয় পীঠস্থান। সুরম্যভাবে সংস্কারকৃত এই রাজপ্রাসাদে সংরক্ষিত রয়েছে ঐতিহ্যবাহী জামদানি শাড়ি, নকশিকাঁথা, ধাতব শিল্পকর্ম, পোড়ামাটির ফলক ও কাঠের কারুশিল্পের বিশাল সংগ্রহ। ছায়াঘেরা বাগানের মাঝে ঐতিহ্যবাহী তাঁতশালায় কারিগরদের সরাসরি বুননশিল্প প্রদর্শন দর্শনার্থীদের দারুণভাবে মুগ্ধ করে। শান্ত পদ্মপুকুর ও সবুজ বৃক্ষরাজিতে ঘেরা এই প্রাঙ্গণে প্রতি বছর মাসব্যাপী জাতীয় লোককারুশিল্প মেলা অনুষ্ঠিত হয়, যা গ্রামীণ সংস্কৃতি ও বাউল গানের সুরে প্রাণবন্ত থাকে।",
                "locationEn": "Sonargaon, Narayanganj",
                "locationBn": "সোনারগাঁও, নারায়ণগঞ্জ",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Bangladesh+Folk+Art+and+Crafts+Foundation+Sonargaon%2C+Bangladesh"
            },
            {
                "id": 3,
                "nameEn": "Goaldi Mosque",
                "nameBn": "গোয়ালদি মসজিদ",
                "categoryEn": "Sultanate Architecture",
                "categoryBn": "সুলতানি আমলের স্থাপত্য",
                "descEn": "Constructed in 1519 AD during the reign of Sultan Alauddin Husain Shah by Mulla Hizabar Akbar Khan, Goaldi Mosque represents the crowning pinnacle of pre-Mughal Bengal brick architecture. The elegant square single-domed sanctuary features exposed deep-red terracotta bricks carved with intricate floral rosettes, hanging bell-and-chain patterns, and lotus medallions. Its thick masonry walls are anchored at each corner by circular engaged turrets crowned with miniature cornices that mirror traditional Bengali curved rooflines. The central mihrab is crafted from polished black basalt stone bordered by finely carved floral arabesques that testify to medieval stonecutting artistry. Situated amidst tranquil village orchards, it remains one of the finest surviving Sultanate-era religious monuments in the region.",
                "descBn": "১৫১৯ খ্রিস্টাব্দে সুলতান আলাউদ্দিন হোসেন শাহের শাসনামলে মোল্লা হিজাবর আকবর খান কর্তৃক নির্মিত গোয়ালদি মসজিদ প্রাক-মুঘল বাংলার পোড়ামাটির স্থাপত্যের এক অনন্য নিদর্শন। বর্গাকৃতির এই একক গম্বুজ বিশিষ্ট মসজিদটির বহির্দেয়াল গভীর লাল রঙের টেরাকোটা ফুল, ঝুলন্ত ঘণ্টার শিকল ও পদ্মমোটিফের চমৎকার নকশায় অলঙ্কৃত। ঐতিহ্যবাহী বাংলার বাঁকানো কার্নিশ ও চার কোণের বৃত্তাকার বুরুজ সুলতানি স্থাপত্যের ঐতিহ্যকে চমৎকারভাবে তুলে ধরে। মসজিদের কেন্দ্রীয় মেহরাবটি সূক্ষ্মভাবে খোদাইকৃত কালো ব্যাসল্ট পাথর দিয়ে নির্মিত, যা মধ্যযুগীয় কারুকলার অনুপম সাক্ষ্য দেয়। নিভৃত পল্লী প্রকৃতির মাঝে অবস্থিত এই মসজিদটি প্রত্নতত্ত্বপ্রেমীদের জন্য এক অবশ্য দর্শনীয় স্থান।",
                "locationEn": "Goaldi village, Sonargaon",
                "locationBn": "গোয়ালদি গ্রাম, সোনারগাঁও",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Goaldi+Mosque+Sonargaon%2C+Bangladesh"
            },
            {
                "id": 4,
                "nameEn": "Hajiganj Fort",
                "nameBn": "হাজীগঞ্জ দুর্গ",
                "categoryEn": "Mughal River Fortress",
                "categoryBn": "মুঘল জলদুর্গ",
                "descEn": "Erected around 1650 by Mughal Subahdar Islam Khan or Mir Jumla, Hajiganj Fort (also called Khizrpur Fort) formed a crucial part of the maritime triangle defending Dhaka against Magh and Portuguese corsairs. Strategically positioned at the confluence of the Shitalakshya and Old Brahmaputra rivers, this hexagonal fortification features robust battlemented curtains lined with musket loops. An imposing square artillery platform dominates the enclosure, once housing heavy iron cannon batteries capable of commanding enemy gunboats navigating upstream. Inside the brick ramparts, an ancient stepped brick well and subterranean ammunition magazines highlight Mughal military civil engineering. The fort grounds now host well-maintained lawns where visitors can inspect historic defense ramparts and enjoy panoramic river views.",
                "descBn": "১৬৫০ খ্রিস্টাব্দের দিকে মুঘল সুবেদার ইসলাম খান অথবা মীর জুমলা কর্তৃক নির্মিত হাজীগঞ্জ দুর্গ (বা খিজিরপুর দুর্গ) তৎকালীন রাজধানী ঢাকাকে মগ ও পর্তুগিজ জলদস্যুদের আক্রমণ থেকে রক্ষা করতে নির্মিত অন্যতম শক্তিশালী জলদুর্গ। শীতলক্ষ্যা ও পুরাতন ব্রহ্মপুত্র নদের সংযোগস্থলে অবস্থিত এই ষড়ভুজাকৃতির দুর্গে রয়েছে বন্দুকের ফোকরযুক্ত মজবুত প্রাচীর ও সুউচ্চ পর্যবেক্ষণ বুরুজ। দুর্গের অভ্যন্তরে একটি বিশালাকার কামান মঞ্চ রয়েছে, যেখান থেকে একসময় নদীতে চলাচলকারী শত্রু জাহাজের ওপর গোলাবর্ষণ করা হতো। এছাড়া দুর্গের প্রাচীন কূপ ও গোলাবারুদ সংরক্ষণাগার মুঘল সামরিক প্রকৌশলের সাক্ষ্য বহন করে। সবুজ ঘাসে আচ্ছাদিত এই দুর্গ প্রাঙ্গণ দর্শনার্থীদের কাছে দারুণ ঐতিহাসিক আকর্ষণ।",
                "locationEn": "Godenail area, Narayanganj city",
                "locationBn": "গোদনাইল এলাকা, নারায়ণগঞ্জ শহর",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Hajiganj+Fort+Narayanganj%2C+Bangladesh"
            },
            {
                "id": 5,
                "nameEn": "Sonakanda Fort",
                "nameBn": "সোনাকান্দা দুর্গ",
                "categoryEn": "Mughal Defensive Bastion",
                "categoryBn": "মুঘল প্রতিরক্ষামূলক দুর্গ",
                "descEn": "Positioned directly opposite Hajiganj Fort on the eastern bank of the Shitalakshya River in Bandar, Sonakanda Fort is a 17th-century river fortress attributed to Subahdar Mir Jumla. The structure consists of a massive pentagonal defensive curtain wall flanked by a raised circular artillery battery commanding the entire water bend. Stepped stone staircases lead to the elevated cannon turret, from which Mughal sentries monitored international maritime shipping routes toward Dhaka. Defensive embrasures, arched gateways, and crenellated parapets reflect defensive architecture optimized for heavy artillery and swivel guns. Surrounded by historic riverside communities, the fort provides captivating sunset vistas across bustling riverboat channels.",
                "descBn": "নারায়ণগঞ্জের বন্দর এলাকায় শীতলক্ষ্যা নদীর পূর্ব তীরে হাজীগঞ্জ দুর্গের বিপরীতে অবস্থিত সোনাকান্দা দুর্গ ১৭শ শতকের একটি বিখ্যাত মুঘল প্রতিরক্ষা স্থাপনা। সুবেদার মীর জুমলার আমলে নির্মিত এই দুর্গটি পঞ্চভুজাকৃতির মজবুত প্রাচীর এবং একটি বিশালাকার বৃত্তাকার কামান মঞ্চ নিয়ে গঠিত। সিঁড়ি বেয়ে কামান মঞ্চে উঠলে পুরো নদীর দূরবর্তী বাঁক পর্যন্ত স্পষ্ট নজরদারি করা যায়, যা নদীপথে ঢাকায় অনুপ্রবেশকারী শত্রু জাহাজ প্রতিহত করতে ব্যবহৃত হতো। দুর্গের প্রাচীরে বন্দুক চালনার উপযোগী অসংখ্য ফোকর ও খিলানযুক্ত প্রবেশদ্বার মুঘল স্থাপত্যশৈলীর পরিচয় দেয়। নদীপাড়ের এই ঐতিহাসিক শান্ত চত্বর থেকে সূর্যাস্তের মনোরম দৃশ্য উপভোগ করা যায়।",
                "locationEn": "Bandar, near the Shitalakshya River",
                "locationBn": "বন্দর, শীতলক্ষ্যা নদীর তীরবর্তী",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Sonakanda+Fort+Bandar+Narayanganj%2C+Bangladesh"
            }
        ],
        "tour": [
            {
                "id": 1,
                "nameEn": "Murapara Rajbari",
                "nameBn": "মুড়াপাড়া রাজবাড়ি",
                "categoryEn": "Palatial Heritage Architecture",
                "categoryBn": "ঐতিহাসিক প্রাসাদ ও স্থাপত্য",
                "descEn": "Commissioned in 1889 by Ramratan Banerjee and completed by his successors, the Murapara Rajbari stands as an opulent palace of the colonial zamindari era in Rupganj. The imposing two-story mansion features neoclassical Greek columns, arched verandas, elaborate stucco friezes, and an ornate crowned pediment that overlooks a grand reflecting pond. Surrounding the palace are extensive courtyards, ancient banyan trees, and subsidiary guest pavilions that evoke nineteenth-century aristocratic splendor. Today functioning as the Murapara Government College, the palace welcomes travelers and history enthusiasts who admire its grand symmetry and cinematic beauty. It is frequently sought out by photographers and film directors for its historic grandeur.",
                "descBn": "১৮৮৯ সালে রামরতন ব্যানার্জী কর্তৃক সূচিত এবং পরবর্তীতে তার উত্তরসূরিদের দ্বারা সম্পন্ন মুড়াপাড়া রাজবাড়ি রূপগঞ্জের এক দৃষ্টিনন্দন ঔপনিবেশিক জমিদার প্রাসাদ। বিশাল দোতলা এই প্রাসাদের সম্মুখভাগে রয়েছে গ্রিক রীতির স্তম্ভ, কারুকার্যময় খিলানযুক্ত বারান্দা এবং সুন্দর একটি দিঘির প্রতিফলন। প্রাসাদের সুবিশাল প্রাঙ্গণ, শতবর্ষী বটগাছ ও নান্দনিক নকশা উনিশ শতকের আভিজাত্যকে স্মরণ করিয়ে দেয়। বর্তমানে এখানে মুড়াপাড়া সরকারি কলেজ পরিচালিত হলেও এর ঐতিহাসিক স্থাপত্য অক্ষুণ্ণ রাখা হয়েছে। ভ্রমণপিপাসু ও আলোকচিত্রীদের কাছে এই সুরম্য রাজপ্রাসাদটি অত্যন্ত জনপ্রিয় একটি আকর্ষণ।",
                "locationEn": "Murapara, Rupganj Upazila",
                "locationBn": "মুড়াপাড়া, রূপগঞ্জ উপজেলা",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Murapara+Rajbari+Rupganj%2C+Bangladesh"
            },
            {
                "id": 2,
                "nameEn": "Zinda Park",
                "nameBn": "জিন্দা পার্ক (ঐক্যতান)",
                "categoryEn": "Community Eco-Park",
                "categoryBn": "কমিউনিটি ইকো পার্ক",
                "descEn": "Conceived and nurtured through voluntary community efforts over three decades, Zinda Park spans over 150 lush acres in Daudpur Union of Rupganj. The self-sustaining green sanctuary boasts thousands of native trees, whispering pine groves, tranquil lotus ponds, and charming wooden footbridges. Visitors can stroll along tree-canopied earthen trails, rent wooden boats for relaxed rowing, and explore an architecturally striking brick library nestled on an islet. Designed with ecological sustainability and community ownership at its heart, the park operates without commercial blare, offering an idyllic respite for families and nature lovers. Cozy dining pavilions serve authentic rural meals prepared using fresh local produce.",
                "descBn": "রূপগঞ্জের দাউদপুর ইউনিয়নে প্রায় দেড়শ একর জায়গাজুড়ে স্থানীয় বাসিন্দাদের ত্রিশ বছরের স্বেচ্ছাশ্রম ও সমবায়ে গড়ে ওঠা জিন্দা পার্ক এক অনন্য পরিবেশবান্ধব উদ্যান। এই প্রাকৃতিক উদ্যানে রয়েছে হাজার হাজার দেশীয় বৃক্ষ, ঝাউবনের স্নিগ্ধ ছায়া, পদ্মপুকুর ও কাঠের মনোরম সাঁকো। দর্শনার্থীরা মাটির সুদৃশ্য পথ ধরে হেঁটে বেড়াতে পারেন, শান্ত লেকে নৌকায় ভাসতে পারেন এবং দ্বীপের মাঝে অবস্থিত নান্দনিক স্থাপত্যের পাঠাগারটি পরিদর্শন করতে পারেন। বাণিজ্যিক কোলাহলমুক্ত এই সবুজ অভয়ারণ্যটি পরিবার নিয়ে সময় কাটানোর জন্য অতুলনীয়। উদ্যানের ভেতরে দেশীয় খাবারের ক্যাফেটেরিয়া রয়েছে।",
                "locationEn": "Zinda, Rupganj Upazila",
                "locationBn": "জিন্দা, রূপগঞ্জ উপজেলা",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Zinda+Park+Rupganj%2C+Bangladesh"
            },
            {
                "id": 3,
                "nameEn": "Langalbandh",
                "nameBn": "লাঙ্গলবন্দ তীর্থভূমি",
                "categoryEn": "Sacred Pilgrimage Site",
                "categoryBn": "পবিত্র তীর্থস্থান ও ঘাট",
                "descEn": "Nestled gracefully along the Old Brahmaputra River in Bandar, Langalbandh is one of the ancient and holiest Hindu pilgrimage sanctuaries in South Asia. According to Hindu mythology, Parashurama bathed in these sacred river waters to wash away mortal sins, creating a tradition that attracts hundreds of thousands of pilgrims annually on Ashtami Snan. The two-kilometer riverside promenade is lined with dozens of historic masonry bathing ghats, decorated shrines, ashrams, and devotional temples. Shaded by ancient banyan trees, the ghats provide an evocative spiritual experience reflecting centuries of uninterrupted faith. Cultural explorers visit year-round to experience the riverine spirituality and ritual heritage of rural Bengal.",
                "descBn": "বন্দর উপজেলায় পুরাতন ব্রহ্মপুত্র নদের তীরে অবস্থিত লাঙ্গলবন্দ সনাতন ধর্মাবলম্বীদের দক্ষিণ এশিয়ার অন্যতম সুপ্রাচীন ও পবিত্র তীর্থস্থান। পৌরাণিক বিশ্বাস অনুসারে মহর্ষি পরশুরাম ব্রহ্মপুত্রের এই পবিত্র জলে স্নান করে পাপমুক্ত হয়েছিলেন, যার স্মরণে প্রতি বছর চৈত্র মাসের মহাষ্টমীতে লক্ষাধিক পুণ্যার্থীর অষ্টমী স্নান অনুষ্ঠিত হয়। প্রায় দুই কিলোমিটার দীর্ঘ নদীতীরজুড়ে রয়েছে বহু ঐতিহাসিক পাকা ঘাট, স্মৃতিমন্দির, প্রাচীন আশ্রম ও পুণ্যালয়। শতবর্ষী বটবৃক্ষের ছায়ায় ঘেরা এই নদীপ্রান্তর বাংলার হাজার বছরের ধর্মীয় সম্প্রীতি ও আধ্যাত্মিক চেতনার জীবন্ত প্রতীক। সারা বছরই দর্শনার্থীরা এখানে নদীতীরবর্তী রূপ ও ইতিহাস দর্শনে আসেন।",
                "locationEn": "Langalbandh, Bandar Upazila",
                "locationBn": "লাঙ্গলবন্দ, বন্দর উপজেলা",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Langalbandh+Narayanganj%2C+Bangladesh"
            },
            {
                "id": 4,
                "nameEn": "Mary Anderson Floating Restaurant",
                "nameBn": "মেরি অ্যান্ডারসন ভাসমান রেস্তোরাঁ ও নদীতট",
                "categoryEn": "Riverboat Dining & Pier",
                "categoryBn": "নৌ-পর্যটন ও ভাসমান বিনোদন",
                "descEn": "Moored historically along the Buriganga riverbank at Pagla in Fatullah, the Mary Anderson was originally an antique British-era riverboat converted into a floating restaurant by Bangladesh Parjatan Corporation. Serving as a pioneer of riverine culinary tourism, the double-decked vessel offered diners authentic local dishes accompanied by refreshing river breezes. While dynamic operations and vessel locations can periodically vary along the ghat, the Pagla waterfront continues to attract travelers seeking river launch cruises and picturesque waterside strolls. Visitors gather in the afternoon to watch the rhythmic maritime commerce of country boats, sand barges, and sleek passenger steamers. It represents an authentic window into Narayanganj's living river transport lifestyle.",
                "descBn": "ফতুল্লার পাগলায় বুড়িগঙ্গা নদীর তীরে ঐতিহ্যবাহী ব্রিটিশ আমলের ইঞ্জিনচালিত জলযানকে সংস্কার করে বাংলাদেশ পর্যটন কর্পোরেশন কর্তৃক ভাসমান রেস্তোরাঁ হিসেবে পরিচালিত হয়েছিল মেরি অ্যান্ডারসন। নদীর বুকে ভাসমান থেকে তাজা বাতাস ও দেশীয় খাবারের স্বাদ উপভোগ করার পথিকৃৎ ছিল এই ঐতিহ্যবাহী জলযানটি। নদীর নাব্যতা ও স্থান পরিবর্তনের প্রেক্ষিতে কার্যক্রম ওঠানামা করলেও পাগলার এই ঘাট এলাকা নদীভ্রমণ ও বৈকালিক ভ্রমণের জন্য জনপ্রিয়। এখান থেকে নৌকা ও ট্রলারে করে নদীভ্রমণ করা যায় এবং বুড়িগঙ্গার চঞ্চল নৌজীবন উপভোগ করা যায়। এটি নারায়ণগঞ্জের নদীতীরবর্তী জীবনের এক অনন্য দিক।",
                "locationEn": "Pagla, Fatullah area",
                "locationBn": "পাগলা, ফতুল্লা এলাকা",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Mary+Anderson+Floating+Restaurant+Narayanganj%2C+Bangladesh"
            },
            {
                "id": 5,
                "nameEn": "DC Theme Park",
                "nameBn": "ডিসি থিম পার্ক (নারায়ণগঞ্জ)",
                "categoryEn": "Family Recreation Parkway",
                "categoryBn": "পারিবারিক বিনোদন পার্ক",
                "descEn": "Developed by the Narayanganj District Administration to provide high-quality urban open space, the DC Theme Park features landscaped family grounds and leisure attractions. The park provides green walkways, vibrant floral gardens, children's amusement rides, and shaded recreational kiosks designed for all age groups. It serves as an essential recreational outlet for urban families seeking a safe, clean, and refreshing outdoor environment within easy reach of the city center. Visitors frequently praise the peaceful ambiance, evening decorative illumination, and child-friendly play zones. It exemplifies contemporary efforts to enhance public leisure infrastructure across the riverine district.",
                "descBn": "নারায়ণগঞ্জ জেলা প্রশাসনের উদ্যোগে গড়ে ওঠা ডিসি থিম পার্ক নগরবাসীর সুস্থ বিনোদনের এক চমৎকার স্থান। মনোরম সবুজ ঘাসের চত্বর, দৃষ্টিনন্দন ফুলের বাগান, শিশুদের জন্য রাইডস ও ছায়াঘেরা বসার ব্যবস্থা নিয়ে পার্কটি সাজানো হয়েছে। শহরের কোলাহল পেরিয়ে পরিবার-পরিজন নিয়ে আনন্দময় সময় কাটাতে এবং সান্ধ্যকালীন বিশুদ্ধ বাতাস উপভোগ করতে বহু মানুষ এখানে আসেন। পার্কের পরিচ্ছন্ন পরিবেশ, নিরাপত্তা ও আলোকসজ্জা দর্শনার্থীদের জন্য আনন্দদায়ক অভিজ্ঞতা প্রদান করে। আধুনিক নাগরিক জীবনের বিনোদনে এটি নারায়ণগঞ্জের একটি উল্লেখযোগ্য সংযোজন।",
                "locationEn": "Narayanganj district",
                "locationBn": "নারায়ণগঞ্জ জেলা সদর এলাকা",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=DC+Theme+Park+Narayanganj%2C+Bangladesh"
            }
        ]
    }
]

print("Module loaded with", len(TARGET_DISTRICTS), "districts definition")
