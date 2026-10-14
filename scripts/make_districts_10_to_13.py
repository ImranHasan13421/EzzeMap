# -*- coding: utf-8 -*-
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
os.makedirs('scripts/data_districts_17', exist_ok=True)

# 10. RANGAMATI
rangamati = {
    "slug": "rangamati",
    "en": "Rangamati",
    "bn": "রাঙ্গামাটি",
    "hero_title_en": "Rangamati Blue Kaptai Lake & Cloud Kingdom Sajek",
    "hero_title_bn": "রাঙ্গামাটির নীল কাপ্তাই হ্রদ ও মেঘের রাজ্য সাজেক",
    "hero_sub_en": "Asia's largest artificial lake, misty valleys of Sajek, and sacred Rajban Vihara.",
    "hero_sub_bn": "সুবিশাল কাপ্তাই হ্রদের নীল জলরাশি, মেঘের দেশ সাজেক ভ্যালি ও পবিত্র রাজবন বিহার।",
    "tagline_en": "The spellbinding hill-lake district of the Chittagong Hill Tracts, famous across the world for the sprawling emerald waters of Kaptai Lake, the iconic Hanging Bridge, and the ethereal cloud kingdom of Sajek Valley.",
    "tagline_bn": "পার্বত্য চট্টগ্রামের নৈসর্গিক হ্রদ ও পাহাড়ের রানী, যা সুবিশাল নীল কাপ্তাই লেক, বিখ্যাত ঝুলন্ত সেতু এবং মেঘের উপত্যকা সাজেক ভ্যালির জন্য বিশ্বজুড়ে সুখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/rangamati/carousel-1.webp",
            "titleEn": "Sajek Valley Kingdom of Clouds",
            "titleBn": "সাজেক ভ্যালি মেঘের উপত্যকা",
            "subtitleEn": "High-altitude mountain ridge where clouds float freely into wooden cottages and winding hill trails",
            "subtitleBn": "মেঘের ওপর দাঁড়িয়ে থাকা স্বপ্নিল পাহাড়ি উপত্যকা, যেখানে মেঘের দল ঘরের জানালায় এসে দোলা দেয়"
        },
        {
            "id": 2,
            "image": "images/districts/rangamati/carousel-2.webp",
            "titleEn": "Kaptai Lake Emerald Waters & Mountain Islands",
            "titleBn": "কাপ্তাই হ্রদের নীল জল ও পাহাড়ি দ্বীপ",
            "subtitleEn": "Vast freshwater mountain reservoir dotted with lush islets and traditional fishing skiffs",
            "subtitleBn": "সবুজ পাহাড়ের খাঁজে খাঁজে ছড়িয়ে থাকা এশিয়ার বৃহত্তম কৃত্রিম হ্রদের জাদুকরী রূপ"
        },
        {
            "id": 3,
            "image": "images/districts/rangamati/carousel-3.webp",
            "titleEn": "Rangamati Iconic Hanging Bridge",
            "titleBn": "রাঙ্গামাটির বিখ্যাত ঝুলন্ত সেতু",
            "subtitleEn": "335-foot pedestrian suspension bridge arching across Kaptai Lake between scenic forested promontories",
            "subtitleBn": "কাপ্তাই হ্রদের দুই পাহাড়ের সংযোগকারী ৩৩৫ ফুট দীর্ঘ ঝুলন্ত সেতু, যা পর্যটকদের প্রধান আকর্ষণ"
        },
        {
            "id": 4,
            "image": "images/districts/rangamati/carousel-4.webp",
            "titleEn": "Rajban Vihara Sacred Buddhist Pagoda Complex",
            "titleBn": "পবিত্র রাজবন বিহার ও স্বর্ণালী প্যাগোডা",
            "subtitleEn": "Renowned international Buddhist monastery sanctuary and meditation retreat founded by Ven. Sadhanananda Mahathera",
            "subtitleBn": "বনভান্তের স্মৃতিবিজড়িত আন্তর্জাতিক খ্যাতিসম্পন্ন বৌদ্ধ বিহার ও ধ্যান সাধনার পবিত্র পুণ্যভূমি"
        },
        {
            "id": 5,
            "image": "images/districts/rangamati/carousel-5.webp",
            "titleEn": "Shuvolong Waterfall Mountain Cascade",
            "titleBn": "শুভলং পাহাড়ি ঝরনা ও গিরিখাত",
            "subtitleEn": "Majestic mountain waterfall plunging from rocky cliffs directly into Kaptai Lake accessible only by boat",
            "subtitleBn": "সুউচ্চ পাহাড়ের খাড়া খাদ বেয়ে কাপ্তাই লেকের জলে আছড়ে পড়া নয়নাভিরাম শুভলং ঝরনা"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Chakma Rajbari",
            "nameBn": "চাকমা রাজবাড়ি",
            "categoryEn": "Royal Ancestral Palace & Seat of the Chakma King",
            "categoryBn": "ঐতিহাসিক চাকমা রাজার রাজপ্রাসাদ ও ঐতিহ্য",
            "descEn": "The Chakma Rajbari in Rangamati town is the royal administrative seat and ancestral palace of the Chakma Raja, the traditional monarch of the largest indigenous nation in the Chittagong Hill Tracts. Located on a scenic promontory jutting into Kaptai Lake, the royal estate includes royal audience halls, ancestral heritage collections, and ceremonial courtyards where the King administers customary tribal law. The compound houses antique royal regalia, ceremonial swords, British colonial charters, and heirloom hand-woven textiles. The annual Rajpunyah durbar brings together hundreds of traditional headmen ('Mouza Headmen') in rich traditional dress to reaffirm ancestral allegiance and community governance. The palace stands as an enduring symbol of indigenous sovereignty and cultural preservation.",
            "descBn": "রাঙ্গামাটি শহরে কাপ্তাই হ্রদের তীরে মনোরম টিলায় অবস্থিত চাকমা রাজবাড়ি পার্বত্য অঞ্চলের বৃহত্তম নৃগোষ্ঠীর ঐতিহ্যবাহী রাজকীয় আসন। শত শত বছর ধরে নিজস্ব প্রথা ও বিচার ব্যবস্থার প্রধান কেন্দ্র হিসেবে এই রাজপ্রাসাদটি অত্যন্ত শ্রদ্ধেয়। প্রাসাদে সংরক্ষিত আছে প্রাচীন রাজকীয় অস্ত্রশস্ত্র, পোশাক, ব্রিটিশ সনদ ও ঐতিহাসিক রাজদণ্ড। প্রতি বছর রাজা কর্তৃক আয়োজিত ঐতিহ্যবাহী 'রাজপুণ্যাহ' দরবারে শত শত কার্বারি ও হেডম্যান রাজকীয় পোশাকে খাজনা দিতে সমবেত হন। চাকমা জাতির সুপ্রাচীন ঐতিহ্য, সংস্কৃতি ও স্বকীয়তার এক জীবন্ত প্রতীক এই চাকমা রাজবাড়ি।",
            "locationEn": "Rangamati town",
            "locationBn": "রাঙ্গামাটি শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Chakma%20Rajbari%2C%20Rangamati%20town"
        },
        {
            "id": 2,
            "nameEn": "Rajban Vihara",
            "nameBn": "রাজবন বিহার আন্তর্জাতিক বৌদ্ধ বিহার",
            "categoryEn": "International Buddhist Monastery & Shrine",
            "categoryBn": "আন্তর্জাতিক বৌদ্ধ বিহার ও মহাধর্মস্থান",
            "descEn": "Rajban Vihara in Rangamati is the largest and most prestigious Buddhist monastery complex in Bangladesh, founded in the 1970s under the spiritual guidance of the venerated forest monk Ven. Sadhanananda Mahathera (widely known as 'Bana Bhante'). Spanning 33 acres of forested hillocks beside Kaptai Lake, the sanctuary features gleaming multi-tiered pagodas, massive bronze and stone statues of Buddha, and the glass sanctum preserving the preserved body of Bana Bhante. Thousands of monks and pilgrims gather annually for the Kathin Chibar Dan festival, where yellow robes are hand-spun and woven from raw cotton within 24 hours. The serene woodland footpaths, chiming temple bells, and gentle breezes create an atmosphere of transcendent spiritual elevation.",
            "descBn": "কাপ্তাই হ্রদের কোলে প্রায় ৩৩ একর সবুজ পাহাড়ি ভূমিতে অবস্থিত রাজবন বিহার বাংলাদেশের সর্ববৃহৎ ও সবচেয়ে পবিত্র বৌদ্ধ বিহার। পরম পূজ্য বনভান্তে (শ্রীমৎ সাধনানন্দ মহাস্থবীর)-এর নেতৃত্বে প্রতিষ্ঠিত এই মহাপুণ্যভূমিতে রয়েছে কারুকার্যময় প্যাগোডা, বিশালাকার বুদ্ধমূর্তি এবং বনভান্তের সংরক্ষিত দেহাবশেষ। প্রতি বছর অনুষ্ঠিত 'কঠিন চীবর দান' উৎসবে লাখো পুণ্যার্থীর সমাগম ঘটে, যেখানে ২৪ ঘণ্টার মধ্যে সুতা কেটে তৈরি করা হয় বিশেষ চীবর। ছায়াঘেরা বনপথ ও ধর্মীয় স্তূপের শান্ত পরিবেশ ভক্ত ও পর্যটকদের মনকে আধ্যাত্মিক শান্তিতে ভরিয়ে দেয়।",
            "locationEn": "Rangamati town",
            "locationBn": "রাঙ্গামাটি শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Rajban%20Vihara%2C%20Rangamati%20town"
        },
        {
            "id": 3,
            "nameEn": "Buddhist Temple at Tabalchhari",
            "nameBn": "তবলছড়ি আনন্দ বিহার ও বৌদ্ধ মন্দির",
            "categoryEn": "Historic Hilltop Buddhist Temple",
            "categoryBn": "ঐতিহাসিক পাহাড়ি বৌদ্ধ বিহার ও সাধনা কেন্দ্র",
            "descEn": "The Buddhist Temple at Tabalchhari (Ananda Vihara) is an ancient religious retreat perched atop a serene hill overlooking the bustling lakeside settlement of Tabalchhari. The monastery compound features an authentic Burmese-influenced prayer hall with intricately carved wooden pillars, golden stupas, and ancient brass bells. Buddhist devotees and visitors climb the long flight of shaded stone steps to offer lotus blossoms and light prayer candles before the smiling Buddha statues. The elevated terrace offers a peaceful panoramic viewpoint across the surrounding mountain waters of Kaptai Lake. The temple plays an integral role in preserving the religious customs, scriptures, and educational traditions of the local Buddhist community.",
            "descBn": "রাঙ্গামাটির তবলছড়িতে অবস্থিত আনন্দ বিহার এক সুপ্রাচীন ও ঐতিহ্যবাহী পাহাড়ি বৌদ্ধ মন্দির। পাহাড়ের শীর্ষে স্থাপিত এই মন্দিরে রয়েছে বার্মিজ ও স্থানীয় পাহাড়ি স্থাপত্যরীতির নিপুণ কাঠের অলংকরণ এবং সোনালী বুদ্ধমূর্তি। সিঁড়ি বেয়ে ওপরে উঠলে চোখে পড়ে শান্ত প্রার্থনা কক্ষ এবং প্রদীপ প্রজ্বলনের পবিত্র বেদি। মন্দির প্রাঙ্গণ থেকে কাপ্তাই লেকের নীল জলরাশি ও দূর পাহাড়ের অপরূপ দৃশ্য অবলোকন করা যায়। স্থানীয় পাহাড়ি জনগোষ্ঠীর ধর্মীয় উৎসব ও প্রার্থনার অন্যতম প্রধান মিলনস্থল হিসেবে তবলছড়ির এই মন্দিরটি অত্যন্ত শ্রদ্ধেয় ও দর্শনীয়।",
            "locationEn": "Tabalchhari, Rangamati",
            "locationBn": "তবলছড়ি, রাঙ্গামাটি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Buddhist%20Temple%20at%20Tabalchhari%2C%20Tabalchhari%2C%20Rangamati"
        },
        {
            "id": 4,
            "nameEn": "Kaptai Dam and hydroelectric project",
            "nameBn": "কাপ্তাই জলবিদ্যুৎ প্রকল্প ও বাঁধ",
            "categoryEn": "Monumental Hydroelectric Engineering Marvel",
            "categoryBn": "দেশের একমাত্র জলবিদ্যুৎ বাঁধ ও ঐতিহাসিক হ্রদ সৃষ্টি",
            "descEn": "The Kaptai Dam and Hydroelectric Project, completed in 1962 across the powerful Karnaphuli River, is an monumental engineering landmark that reshaped the geography of southeastern Bangladesh. Spanning 670 meters with an immense 16-gate spillway, this historic earth-fill dam created Kaptai Lake—the largest artificial freshwater reservoir in South Asia covering over 700 square kilometers. The project continues to generate clean hydroelectric energy through its five massive turbine units. From the scenic public observation overlooks, travelers can marvel at the roaring spillway gates discharging thousands of tons of white foam water into the river gorge below. The surrounding landscaped parks and hill reserves provide a captivating vantage point on Bangladesh's mid-century technological ambitions.",
            "descBn": "১৯৬২ সালে খরস্রোতা কর্ণফুলী নদীর ওপর নির্মিত কাপ্তাই জলবিদ্যুৎ বাঁধ বাংলাদেশের প্রকৌশল ইতিহাসের এক যুগান্তকারী ও সুবিশাল স্থাপনা। ৬৭০ মিটার দীর্ঘ এই মাটির বাঁধ নির্মাণের ফলেই সৃষ্টি হয়েছিল এশিয়ার সর্ববৃহৎ কৃত্রিম হ্রদ 'কাপ্তাই লেক'। বাঁধের ১৬টি বিশালাকার স্পিলওয়ে দিয়ে যখন বর্ষাকালে গর্জন করে পানি নির্গত হয়, তখন সেই জলরাশির ফোয়ারা এক চোখধাঁধানো রূপ ধারণ করে। দেশের একমাত্র এই জলবিদ্যুৎ কেন্দ্রটি জাতীয় গ্রিডে গুরুত্বপূর্ণ বিদ্যুৎ সরবরাহ করে আসছে। বাঁধের চারপাশের সবুজ পাহাড় ও নদী অববাহিকার দৃশ্য পর্যটকদের জন্য এক অত্যন্ত আকর্ষণীয় ও শিক্ষণীয় অভিজ্ঞতা।",
            "locationEn": "Kaptai, Rangamati",
            "locationBn": "কাপ্তাই, রাঙ্গামাটি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kaptai%20Dam%20and%20hydroelectric%20project%2C%20Kaptai%2C%20Rangamati"
        },
        {
            "id": 5,
            "nameEn": "Traditional Chakma cultural areas",
            "nameBn": "ঐতিহ্যবাহী চাকমা সাংস্কৃতিক জনপদ",
            "categoryEn": "Indigenous Ethnic Heritage Village & Crafts",
            "categoryBn": "আদিবাসী চাকমা জীবনধারা ও তাঁতশিল্প পল্লী",
            "descEn": "The traditional Chakma cultural areas distributed across Rangamati offer travelers authentic immersion into the unique customs, textile arts, and culinary heritage of the Chakma nation. Rural homesteads characterized by wooden houses elevated on stilts are nestled among bamboo thickets on hillsides overlooking Kaptai Lake. Visitors can observe skilled women artisans operating indigenous waist-looms (Bain) to weave vibrant 'Pinon' and 'Hadi' dresses featuring intricate geometric 'Alam' patterns. Local village eateries serve authentic hill delicacies like bamboo shoot curries and steamed delicacies wrapped in banana leaves. Respectful visits to these hamlets reveal the harmonious, nature-aligned lifestyle that has defined hill life for over five centuries.",
            "descBn": "রাঙ্গামাটির চারপাশের চাকমা জনপদগুলো তাদের প্রাচীন কৃষ্টি, হস্তশিল্প ও নিজস্ব জীবনরীতির জন্য বিখ্যাত। পাহাড়ের ঢালে কাঠের তৈরি ঐতিহ্যবাহী মাচাং ঘর এবং আঙিনায় শাকসবজির চাষ পাহাড়ি জীবনের সারল্য প্রকাশ করে। এখানকার নারীরা নিজস্ব 'কোমর তাঁত' ব্যবহার করে নিপুণ হাতে পিনোন, হাদি এবং বিখ্যাত 'আলম' নকশার রঙিন পোশাক বুনে থাকেন। স্থানীয় খাবারের দোকানগুলোতে বাঁশকোড়ল ও পাহাড়ের ঐতিহ্যবাহী সুস্বাদু খাবারের স্বাদ পাওয়া যায়। পাহাড়ি সংস্কৃতির সৌন্দর্য ও আদিবাসী মানুষের সরল আতিথেয়তা দর্শকদের মনে চিরস্মরণীয় দাগ কাটে।",
            "locationEn": "Rangamati; visit respectfully",
            "locationBn": "রাঙ্গামাটি পাহাড়ি অঞ্চল",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Traditional%20Chakma%20cultural%20areas%2C%20Rangamati%3B%20visit%20respectfully"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Kaptai Lake",
            "nameBn": "কাপ্তাই হ্রদ",
            "categoryEn": "Asia's Largest Mountain Freshwater Lake",
            "categoryBn": "এশিয়ার বৃহত্তম কৃত্রিম পাহাড়ি হ্রদ",
            "descEn": "Kaptai Lake in Rangamati is a breathtaking freshwater mountain wonderland, covering over 700 square kilometers of turquoise waterways nestled within endless emerald hill ranges. Formed in the valley of the Karnaphuli basin, the lake features labyrinthine water corridors where green mountain peaks emerge from sparkling depths like tropical fjords. Visitors can embark on motorized country boat cruises to explore secluded mountain gorges, island monasteries, and floating tribal bazaars. Swimming in crystal waters, dining on grilled lake fish at bamboo waterfront restaurants, and enjoying cool breezes under tropical skies make Kaptai Lake an iconic paradise. It stands as the crown jewel of tourism in Bangladesh.",
            "descBn": "কাপ্তাই হ্রদ বাংলাদেশের পর্যটনের মুকুটমণি এবং দক্ষিণ এশিয়ার সর্ববৃহৎ মিঠা পানির পাহাড়ি হ্রদ। প্রায় ৭০০ বর্গকিলোমিটার বিস্তৃত এই হ্রদের স্বচ্ছ নীল জলরাশি এবং চারপাশের সবুজ পাহাড়ের অনন্ত সারি এক রূপকথার রাজ্য গড়ে তুলেছে। লেকের বুকে কাঠের বোটে চড়ে দূর পাহাড়ি গিরিখাত, ঝুলন্ত সেতু ও আদিবাসী ভাসমান হাটে ঘুরে বেড়ানো এক অবিস্মরণীয় অভিজ্ঞতা। লেকের মাঝে অবস্থিত বিভিন্ন দ্বীপে গড়ে উঠেছে আধুনিক রিসোর্ট ও বাঁশের তৈরি রেস্তোরাঁ, যেখানে তাজা পাহাড়ি মাছের স্বাদ নেওয়া যায়। জল ও পাহাড়ের এমন অপার্থিব সৌন্দর্য ভ্রমণপিপাসুদের বারবার কাছে টেনে নেয়।",
            "locationEn": "Rangamati",
            "locationBn": "রাঙ্গামাটি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kaptai%20Lake%2C%20Rangamati"
        },
        {
            "id": 2,
            "nameEn": "Hanging Bridge",
            "nameBn": "ঝুলন্ত সেতু",
            "categoryEn": "Iconic Suspension Bridge Over Kaptai Lake",
            "categoryBn": "রাঙ্গামাটির আইকনিক ঝুলন্ত সেতু ও লেক ভিউ",
            "descEn": "The Rangamati Hanging Bridge (Jhulantool) is the world-famous postcard symbol of tourism in the Chittagong Hill Tracts. Built by the Bangladesh Parjatan Corporation, this 335-foot-long suspension footbridge gently spans an inlet of Kaptai Lake, connecting two verdant hillocks. Walking across the vibrant red and yellow wooden deck provides a delightful bouncing sensation while offering sweeping vistas of turquoise waters dotted with speedboats and soaring eagles. Colorful souvenir stalls and tribal textile kiosks border the bridge approach, offering handmade crafts and hill honey. It is an indispensable photo stop for every traveler visiting Rangamati.",
            "descBn": "রাঙ্গামাটির ঝুলন্ত সেতু বাংলাদেশের পর্যটনের সবচেয়ে পরিচিত ও প্রতীকী দর্শনীয় স্থান। বাংলাদেশ পর্যটন কর্পোরেশন কর্তৃক নির্মিত ৩৩৫ ফুট দীর্ঘ এই ঝুলন্ত সেতুটি কাপ্তাই হ্রদের দুই পাহাড়ের মধ্যে এক অপূর্ব সেতুবন্ধন রচনা করেছে। সেতুর ওপর দিয়ে হাঁটার সময় মৃদু দুলুনি এবং নিচে শান্ত নীল জলরাশি পর্যটকদের মধ্যে এক রোমাঞ্চকর অনুভূতি জাগায়। সেতু থেকে চারপাশের সবুজ পাহাড় ও দূরবর্তী নৌকার দৃশ্য ক্যামেরাবন্দি করার জন্য এটি সেরা স্থান। সেতু সংলগ্ন বিপণিগুলোতে পাহাড়ি তাঁতের পোশাক ও সুভ্যেনির কিনতে পাওয়া যায়। রাঙ্গামাটি ভ্রমণে এই ঝুলন্ত সেতু দর্শন অপরিহার্য।",
            "locationEn": "Rangamati town",
            "locationBn": "রাঙ্গামাটি শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Hanging%20Bridge%2C%20Rangamati%20town"
        },
        {
            "id": 3,
            "nameEn": "Shuvolong Waterfall",
            "nameBn": "শুভলং ঝরনা",
            "categoryEn": "Spectacular Lakeside Cliff Waterfall",
            "categoryBn": "কাপ্তাই লেকের কোল ঘেঁষা পাহাড়ি জলপ্রপাত",
            "descEn": "Shuvolong Waterfall, located deep within the mountain folds along Kaptai Lake, is a magnificent natural waterfall that drops directly from towering rocky precipices into the lake waters. Reached via a thrilling two-hour boat cruise through steep mountain gorges, the waterfall presents its most dramatic spectacle during the monsoon when sheets of white mountain water plunge 140 feet against black slate cliffs. Travelers maneuver their boats right to the base of the rock wall to be drenched by refreshing mountain mist. The tranquil boat journey through the towering Shuvolong canyon offers some of the most breathtaking highland scenery in the country. It is an essential highland water adventure.",
            "descBn": "কাপ্তাই হ্রদের গভীরে বরকল উপজেলায় অবস্থিত শুভলং ঝরনা এক নয়নাভিরাম ও রোমাঞ্চকর পাহাড়ি জলপ্রপাত। রাঙ্গামাটি শহর থেকে নৌপথে সুবিশাল পাহাড়ের গিরিখাত পেরিয়ে প্রায় দুই ঘণ্টার চমৎকার বোট জার্নি শেষে এই ঝরনায় পৌঁছানো যায়। প্রায় ১৪০ ফুট উঁচু খাড়া পাহাড়ের গা বেয়ে স্বচ্ছ জলরাশি সরাসরি কাপ্তাই লেকের বুকে আছড়ে পড়ে। বিশেষ করে বর্ষাকালে ঝরনার গর্জন ও পানির তোড়ে সৃষ্টি হওয়া শীতল জলকণা পর্যটকদের শরীর ও মনকে নিমেষেই জুড়িয়ে দেয়। আকাশচুম্বী পাহাড়ের মাঝ দিয়ে শুভলং যাওয়ার এই জলপথ ভ্রমণ এক আজীবন মনে রাখার মতো অভিজ্ঞতা।",
            "locationEn": "Kaptai Lake; boat access required",
            "locationBn": "শুভলং, বরকল, রাঙ্গামাটি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Shuvolong%20Waterfall%2C%20Kaptai%20Lake%3B%20boat%20access%20required"
        },
        {
            "id": 4,
            "nameEn": "Polwel Park and Cottage",
            "nameBn": "পলওয়েল পার্ক অ্যান্ড কটেজ",
            "categoryEn": "Luxury Lakeside Eco-Park & Resort",
            "categoryBn": "কাপ্তাই হ্রদের বিলাসবহুল ইকো-পার্ক ও লাভ পয়েন্ট",
            "descEn": "Polwel Park and Cottage, developed by the district police administration, is a premier lakeside leisure resort perched on a pine-studded bluff overlooking Kaptai Lake. The park features manicured flower terraces, illuminated pedestrian pathways, luxury wooden chalets, and the famous 'Love Point' cantilevered viewing deck extending dramatically over the blue water. Visitors can enjoy thrilling zip-line rides across forest hollows, relax at waterfront coffee lounges, or hire private pedal boats to tour the quiet coves. Sunset at Polwel Park, when the sky turns crimson and ambient lighting sparkles across the water, offers an unforgettable romantic ambiance. It is widely praised as the most modern leisure haven in the hill tracts.",
            "descBn": "রাঙ্গামাটি জেলা পুলিশ কর্তৃক পরিচালিত পলওয়েল পার্ক অ্যান্ড কটেজ কাপ্তাই হ্রদের তীরে অবস্থিত এক অত্যন্ত পরিচ্ছন্ন, আধুনিক ও মনোরম বিনোদন পার্ক। হ্রদের বাঁকে উঁচু পাহাড়ের গায়ে গড়ে তোলা এই পার্কে রয়েছে সুদৃশ্য কটেজ, লাভ পয়েন্ট, চমৎকার বসার জায়গা এবং দৃষ্টিনন্দন ঝুলন্ত সেতু। লেকের নীল জলের ওপর দিয়ে টানানো রোমাঞ্চকর জিপ-লাইন তরুণদের কাছে দারুণ জনপ্রিয়। বিকেলে লেকের পাড়ে বসে কফি পান এবং সূর্যাস্তের রক্তিম আভা দেখা এক অদ্ভুত রোমান্টিক আবহ তৈরি করে। পরিবার ও যুগলদের জন্য পলওয়েল পার্ক রাঙ্গামাটির এক শ্রেষ্ঠ আধুনিক অবসর কেন্দ্র।",
            "locationEn": "Rangamati town",
            "locationBn": "রাঙ্গামাটি শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Polwel%20Park%20and%20Cottage%2C%20Rangamati%20town"
        },
        {
            "id": 5,
            "nameEn": "Sajek Valley",
            "nameBn": "সাজেক ভ্যালি (মেঘের উপত্যকা)",
            "categoryEn": "Highland Mountain Ridge & Cloud Kingdom",
            "categoryBn": "সমুদ্রপৃষ্ঠ থেকে ১৮০০ ফুট উঁচুতে মেঘের রাজ্য",
            "descEn": "Sajek Valley in Baghaichhari Upazila is the internationally famous 'Kingdom of Clouds' perched atop mountain ridges at an altitude of 1,800 feet near the Mizoram border. Known as the Queen of the Hills in Bangladesh, Sajek features winding highland roads where fluffy white clouds billow through cozy wooden cottages, strawberry farms, and tribal hamlets. From the high observation peaks of Konglak Pahar and Ruilui Para, travelers can witness breathtaking sunrises rising over endless layers of blue mountain horizons veiled in mist. Stargazing at night under crystal unpolluted skies while listening to gentle mountain breezes provides an unforgettable escape from the modern world. Sajek Valley represents the pinnacle of highland beauty in Bangladesh.",
            "descBn": "রাঙ্গামাটির বাঘাইছড়িতে অবস্থিত সাজেক ভ্যালি সমুদ্রপৃষ্ঠ থেকে প্রায় ১৮০০ ফুট উঁচুতে মেঘের রাজ্য হিসেবে খ্যাত বাংলাদেশের সবচেয়ে জনপ্রিয় পর্যটন গন্তব্য। সবুজ পাহাড়ের শৈলশিরার ওপর দিয়ে চলে যাওয়া আঁকাবাঁকা পথ এবং দুই পাশে কাঠের সুদৃশ্য রিসোর্ট সাজেককে এক মায়াবী রূপ দিয়েছে। এখানে সকাল ও সন্ধ্যায় চোখের সামনে ভেসে বেড়ায় সাদা মেঘের তুলোর মতো ভেলা, যা হাত বাড়ালেই ছোঁয়া যায়। কংলাক পাহাড়ের চূড়া ও রুইলুই পাড়া থেকে দূরবর্তী ভারতের মিজোরামের পাহাড়ের অনন্ত ঢেউ দেখা যায়। মেঘের দেশে হারিয়ে যাওয়ার এই স্বপ্নিল অনুভূতি ভ্রমণপ্রেমীদের কাছে এক অবিস্মরণীয় স্বর্গীয় অভিজ্ঞতা।",
            "locationEn": "Baghaichhari, Rangamati; check access rules",
            "locationBn": "সাজেক, বাঘাইছড়ি, রাঙ্গামাটি",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Sajek%20Valley%2C%20Baghaichhari%2C%20Rangamati%3B%20check%20access%20rules"
        }
    ]
}

# 11. CHAPAINAWABGANJ
chapainawabganj = {
    "slug": "chapainawabganj",
    "en": "Chapainawabganj",
    "bn": "চাঁপাইনবাবগঞ্জ",
    "hero_title_en": "Chapainawabganj Capital of Gaur & Mango Kingdom",
    "hero_title_bn": "চাঁপাইনবাবগঞ্জের ঐতিহাসিক গৌড় ও আমের রাজধানী",
    "hero_sub_en": "Medieval Sultanate monuments of Choto Sona Mosque, Darasbari ruins, and vast sweet mango orchards.",
    "hero_sub_bn": "মধ্যযুগীয় স্বাধীন সুলতানি রাজধানী গৌড়ের ছোট সোনা মসজিদ, দারাসবাড়ি ও সুমিষ্ট ফজলি আমের রাজ্য।",
    "tagline_en": "The historic western gateway of medieval Bengal, home to the glorious Sultanate ruins of ancient Gaur, peerless stone terracotta architecture at Choto Sona Mosque, and the undisputed Mango Capital of Bangladesh.",
    "tagline_bn": "মধ্যযুগীয় বাংলার স্বাধীন সুলতানি রাজধানী গৌড়ের পুণ্যভূমি, যেখানে রয়েছে ঐতিহাসিক ছোট সোনা মসজিদের পাথুরে স্থাপত্য এবং দেশের সর্বশ্রেষ্ঠ ও সুস্বাদু আমের বিশাল বাগান।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/chapainawabganj/carousel-1.webp",
            "titleEn": "Choto Sona Mosque Sultanate Stone Jewel",
            "titleBn": "ছোট সোনা মসজিদের অলংকৃত পাথুরে গম্বুজ",
            "subtitleEn": "Fifteenth-century Sultanate stone sanctuary in Gaur famous for gilded domes and delicate stone rosettes",
            "subtitleBn": "গৌড় নগরের বিশ্বখ্যাত সুলতানি মসজিদ, যার খোদাই করা পাথর ও একসময়ের সোনালী গম্বুজ ঐতিহ্যের প্রতীক"
        },
        {
            "id": 2,
            "image": "images/districts/chapainawabganj/carousel-2.webp",
            "titleEn": "Darasbari Mosque & Ancient Madrasa Complex",
            "titleBn": "দারাসবাড়ি মসজিদ ও প্রাচীন মাদ্রাসা ধ্বংসাবশেষ",
            "subtitleEn": "Colossal fifteenth-century brick academy and mosque complex built during the reign of Sultan Shamsuddin Yusuf Shah",
            "subtitleBn": "পঞ্চদশ শতকের সুবিশাল সুলতানি উচ্চশিক্ষা প্রতিষ্ঠান ও টেরাকোটা অলংকৃত ঐতিহাসিক মসজিদ"
        },
        {
            "id": 3,
            "image": "images/districts/chapainawabganj/carousel-3.webp",
            "titleEn": "Tahkhana Palace & Complex of Shah Shuja",
            "titleBn": "শাহ সুজার ঐতিহাসিক তোহাখানা কমপ্লেক্স",
            "subtitleEn": "Mughal royal air-cooled two-story palace and summer pavilion built beside a sacred freshwater lake",
            "subtitleBn": "মুঘল সুবেদার শাহ সুজা কর্তৃক নির্মিত শীতাতপ নিয়ন্ত্রিত ঐতিহাসিক প্রাসাদ ও সুফি দরবার"
        },
        {
            "id": 4,
            "image": "images/districts/chapainawabganj/carousel-4.webp",
            "titleEn": "Kansat Sprawling Mango Trading Market",
            "titleBn": "কানসাটের ঐতিহ্যবাহী এশিয়ার বৃহত্তম আম বাজার",
            "subtitleEn": "Legendary wholesale mango marketplace buzzing with thousands of boats and bullock carts during harvest season",
            "subtitleBn": "মৌসুমে ফজলি, ল্যাংড়া ও খিরসাপাত আমের গন্ধে মুখরিত এশিয়ার অন্যতম বৃহত্তম আম বিপণন কেন্দ্র"
        },
        {
            "id": 5,
            "image": "images/districts/chapainawabganj/carousel-5.webp",
            "titleEn": "Mahananda Riverfront Promenade & Sunset",
            "titleBn": "মহানন্দা নদীর শান্ত জলরাশি ও সূর্যাস্ত",
            "subtitleEn": "Scenic freshwater river meandering gracefully along the town borders lined with lush mango groves",
            "subtitleBn": "চাঁপাইনবাবগঞ্জ শহরের কোল ঘেঁষে বয়ে চলা মহানন্দা নদী, যার তীরে স্নিগ্ধ হাওয়া ও সূর্যাস্তের রঙ মুগ্ধ করে"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Choto Sona Mosque",
            "nameBn": "ছোট সোনা মসজিদ",
            "categoryEn": "Fifteenth-Century Sultanate Stone Masterpiece",
            "categoryBn": "সুলতানি আমলের পাথরে খোদাই করা ঐতিহাসিক মসজিদ",
            "descEn": "Choto Sona Mosque, located at Shahbazpur in Shibganj Upazila within the ancient citadel of Gaur, is widely revered as the 'Gem of Bengal Sultanate Architecture'. Built between 1493 and 1519 AD during the reign of Sultan Alauddin Husain Shah by the royal courtier Wali Muhammad, this magnificent rectangular sanctuary is faced completely with finely carved black basalt stone blocks. It is crowned by fifteen domes, including three elegant Bengali Chala-vaulted central roofs originally layered with pure gold leaf that gave the monument its gilded name. The outer stone walls feature deeply carved lotus rosettes, foliate arabesques, and arched niches of astonishing refinement. The sacred precinct is framed by landscaped lawns and the resting places of two heroic 1971 Bir Sreshtho freedom fighters. It stands as an absolute masterpiece of medieval South Asian Islamic heritage.",
            "descBn": "চাঁপাইনবাবগঞ্জের শিবগঞ্জ উপজেলার গৌড় ঐতিহাসিক নগরে অবস্থিত ছোট সোনা মসজিদকে বলা হয় 'বাংলার সুলতানি স্থাপত্যের রত্ন'। ১৪৯৩ থেকে ১৫১৯ খ্রিস্টাব্দের মধ্যে সুলতান আলাউদ্দিন হোসেন শাহের শাসনামলে ওয়ালী মোহাম্মদ নামক জনৈক রাজকর্মকর্তা এটি নির্মাণ করেন। সম্পূর্ণ কালো ব্যাসাল্ট পাথরে মোড়ানো এই মসজিদে রয়েছে ১৫টি গম্বুজ, যার মাঝে থাকা ৩টি চৌচালা গম্বুজ একসময় খাঁটি সোনার পাত দিয়ে মোড়ানো ছিল বলেই এর নাম 'সোনা মসজিদ'। পাথরের দেওয়ালে খোদাই করা পদ্মফুল ও নকশা মধ্যযুগীয় কারিগরদের শ্রেষ্ঠ শিল্পকলার পরিচয় বহন করে। মসজিদের প্রাঙ্গণেই শায়িত আছেন বীরশ্রেষ্ঠ শহীদ ক্যাপ্টেন মহিউদ্দিন জাহাঙ্গীর। এই মসজিদটি বাংলাদেশের গর্ব ও আন্তর্জাতিক ঐতিহ্যের এক অমূল্য নিদর্শন।",
            "locationEn": "Shahbazpur, Shibganj",
            "locationBn": "শাহবাজপুর, শিবগঞ্জ, চাঁপাইনবাবগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Choto%20Sona%20Mosque%2C%20Shahbazpur%2C%20Shibganj"
        },
        {
            "id": 2,
            "nameEn": "Darasbari Mosque and Madrasa ruins",
            "nameBn": "দারাসবাড়ি মসজিদ ও প্রাচীন মাদ্রাসা",
            "categoryEn": "Grand Sultanate Islamic University Complex",
            "categoryBn": "পঞ্চদশ শতকের সুবিশাল সুলতানি বিশ্ববিদ্যালয় ও মসজিদ",
            "descEn": "Darasbari Mosque and Madrasa complex, situated in Gaur near the international border, represents the largest medieval Islamic educational center excavated in Bangladesh. Constructed in 1479 AD by Sultan Shamsuddin Yusuf Shah, the historic brick mosque once featured an expansive multi-domed prayer hall supported by massive stone pillars and intricately carved terracotta walls. Adjacent archaeological excavations revealed the colossal square collegiate madrasa featuring 40 student cells surrounding a central courtyard—a medieval residential university that educated scholars from across the Islamic world. Although the roof has collapsed over centuries, the soaring terracotta arches and ornamental brick mihrabs preserve a profound scholarly grandeur. It is an indispensable archaeological monument for understanding medieval intellectual life in Bengal.",
            "descBn": "গৌড় ঐতিহাসিক নগরের দারাসবাড়ি মসজিদ ও মাদ্রাসা বাংলার সুলতানি আমলের সর্ববৃহৎ আবাসিক বিশ্ববিদ্যালয় ও মসজিদ কমপ্লেক্স। ১৪৭৯ খ্রিস্টাব্দে সুলতান শামসুদ্দিন ইউসুফ শাহের আমলে প্রতিষ্ঠিত এই প্রাঙ্গণে ছিল সুবিশাল মসজিদ এবং শিক্ষার্থীদের থাকার জন্য ৪০টি সুসজ্জিত আবাসিক কক্ষ। 'দারাসবাড়ি' শব্দের অর্থ পাঠশালা বা বিশ্ববিদ্যালয়। ছাদবিহীন হলেও এর সুউচ্চ লাল ইটের খিলান, দেওয়ালে খোদাই করা পোড়ামাটির লতাপাতার কারুকাজ এবং বিশালাকার মেহরাব প্রাচীন জ্ঞানসাধনার রাজকীয় আবহ ফুটিয়ে তোলে। মধ্যযুগীয় বাংলার শিক্ষা ও স্থাপত্যের এক অনন্য বিস্ময় হিসেবে দারাসবাড়ি পর্যটকদের গভীরভাবে মুগ্ধ করে।",
            "locationEn": "Shahbazpur, Shibganj",
            "locationBn": "শাহবাজপুর, শিবগঞ্জ, চাঁপাইনবাবগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Darasbari%20Mosque%20and%20Madrasa%20ruins%2C%20Shahbazpur%2C%20Shibganj"
        },
        {
            "id": 3,
            "nameEn": "Khania Dighi Mosque",
            "nameBn": "খনিয়া দীঘি মসজিদ (চমকন মসজিদ)",
            "categoryEn": "Exquisite Fifteenth-Century Brick Sanctuary",
            "categoryBn": "সুলতানি আমলের অনুপম পোড়ামাটির কারুকার্যময় মসজিদ",
            "descEn": "Khania Dighi Mosque, also known locally as Chamchika Mosque or Rajbibi Mosque, is an exceptionally well-preserved single-domed brick monument standing near the vast freshwater Khania Dighi lake. Built around 1480 AD during the Later Iliyas Shahi dynasty, the square sanctuary features a massive hemispherical brick dome supported by heavy brick squinches and corner minarets. The exterior facades are densely embellished with some of the finest terracotta floral medallions, hanging chain motifs, and geometric paneling in Bengal. The interior prayer chamber, cooled by gentle lake breezes, centers on a masterfully carved terracotta mihrab. The peaceful surroundings of rustic mango orchards and mirror-like dighi waters make it a treasured spot for contemplative heritage exploration.",
            "descBn": "খনিয়া দীঘি মসজিদ (যা রাজবিবি মসজিদ বা চমকন মসজিদ নামেও পরিচিত) প্রাচীন গৌড় নগরের খনিয়া দীঘির পাড়ে অবস্থিত এক অপূর্ব পোড়ামাটির স্থাপত্য। আনুমানিক ১৪৮০ খ্রিস্টাব্দে নির্মিত এই এক গম্বুজ বিশিষ্ট মসজিদটির চারপাশের দেওয়াল এবং মেহরাবে রয়েছে চোখজুড়ানো টেরাকোটার কাজ। ঝুলন্ত শিকল, পদ্মফুল এবং জ্যামিতিক নকশার এমন সুনিপুণ উপস্থাপন তৎকালীন সুলতানি স্থাপত্যকলার এক শ্রেষ্ঠ পরাকাষ্ঠা। বিশাল দীঘির শীতল বাতাস এবং আমবাগানের শান্ত ছায়া মসজিদ প্রাঙ্গণে এক অপার্থিব স্নিগ্ধতা দান করেছে। ঐতিহ্যের রূপ ও ইতিহাসের গভীরতা উপভোগ করতে এটি এক চমৎকার স্থান।",
            "locationEn": "Shahbazpur, Shibganj",
            "locationBn": "শাহবাজপুর, শিবগঞ্জ, চাঁপাইনবাবগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Khania%20Dighi%20Mosque%2C%20Shahbazpur%2C%20Shibganj"
        },
        {
            "id": 4,
            "nameEn": "Tahkhana Complex",
            "nameBn": "তোহাখানা কমপ্লেক্স ও শাহ সুজার প্রাসাদ",
            "categoryEn": "Mughal Subahdar Palace, Hammam & Mazar",
            "categoryBn": "মুঘল সুবেদার শাহ সুজার গ্রীষ্মকালীন প্রাসাদ ও মাজার",
            "descEn": "The Tahkhana Complex at Firozpur in Shibganj is a fascinating two-story Mughal palace, hammam, and spiritual complex constructed in the mid-seventeenth century by Mughal Prince and Subahdar of Bengal, Shah Shuja. Built primarily as an air-cooled summer palace and retreat for his revered spiritual mentor, Saint Shah Niamatullah Wali, the palace features thick lime-plastered walls and subterranean water channels fed by the adjacent Dakhil Dighi. The complex encompasses the palatial residential quarters, a classic three-domed Mughal mosque, and the sacred single-domed mausoleum of Saint Niamatullah Wali. The harmonious synthesis of royal leisure architecture and spiritual devotion makes Tahkhana one of the most distinctive Mughal heritage destinations in Bangladesh.",
            "descBn": "চাঁপাইনবাবগঞ্জের ফিরোজপুরে অবস্থিত ঐতিহাসিক তোহাখানা কমপ্লেক্স সপ্তদশ শতাব্দীর মাঝামাঝি সময়ে মুঘল সুবেদার শাহ সুজা কর্তৃক তাঁর আধ্যাত্মিক পীর হজরত শাহ নিয়ামতুল্লাহ ওয়ালীর সম্মানে নির্মিত এক অপূর্ব প্রাসাদ। 'তোহাখানা' শব্দের অর্থ ঠান্ডা ভবন বা ভূগর্ভস্থ শীতাতপ নিয়ন্ত্রিত কক্ষ। দুই তলা বিশিষ্ট এই সুরম্য প্রাসাদের নিচতলায় রয়েছে পানির নালিকা বিশিষ্ট রাজকীয় স্নানাগার, যা গ্রীষ্মের প্রচণ্ড তাপেও শীতল থাকত। প্রাঙ্গণে রয়েছে তিন গম্বুজ বিশিষ্ট মুঘল মসজিদ এবং সুফি সাধক শাহ নিয়ামতুল্লাহর পবিত্র মাজার। বিশাল দীঘির পাড়ে সবুজে ঘেরা এই রাজকীয় ও আধ্যাত্মিক স্থাপনাটি মুঘল ইতিহাসের এক জীবন্ত দলিল।",
            "locationEn": "Firozpur, Shibganj",
            "locationBn": "ফিরোজপুর, শিবগঞ্জ, চাঁপাইনবাবগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Tahkhana%20Complex%2C%20Firozpur%2C%20Shibganj"
        },
        {
            "id": 5,
            "nameEn": "Dhania Chak Mosque",
            "nameBn": "ধানিয়াচক মসজিদ",
            "categoryEn": "Sultanate-Era Terracotta Monument",
            "categoryBn": "সুলতানি আমলের তিন গম্বুজ বিশিষ্ট টেরাকোটা মসজিদ",
            "descEn": "Dhania Chak Mosque in Shibganj is an ancient multi-domed brick monument dating from the late fifteenth century, nestled gracefully amidst the mango orchards of the Gaur archaeological landscape. The rectangular mosque features three domes resting on sturdy stone-faced pillars and pointed brick arches. Its east facade and interior mihrabs display exceptional terracotta ornamental friezes depicting intertwining creepers, rosettes, and miniature hanging lamp motifs. Archaeological restoration by the government department has carefully revived its structural integrity while preserving authentic centuries-old brick details. The gentle rustling of surrounding mango foliage and the quiet solitude of the site provide a deeply peaceful experience for heritage travelers.",
            "descBn": "গৌড় প্রত্নতাত্ত্বিক অঞ্চলের আমবাগানের শান্ত নিসর্গে অবস্থিত ধানিয়াচক মসজিদ পঞ্চদশ শতকের শেষভাগের এক ঐতিহ্যবাহী তিন গম্বুজ মসজিদ। লাল ইটের অপূর্ব গাঁথুনি এবং পাথরের স্তম্ভের ওপর নির্মিত এই মসজিদের প্রবেশদ্বার ও মেহরাবে রয়েছে চোখজুড়ানো পোড়ামাটির অলংকরণ। ঝুলন্ত ঘণ্টা, পদ্ম ও বুনো লতাপাতার নিখুঁত খোদাই তৎকালীন শিল্পীদের উচ্চমানের দক্ষতার প্রমাণ দেয়। নির্জন গ্রামীণ পরিবেশে অবস্থিত এই প্রাচীন স্থাপত্যটি দর্শনার্থীদের মধ্যযুগীয় বাংলার স্থাপত্যকলার সমৃদ্ধ ইতিহাসের সাথে পরিচয় করিয়ে দেয়। প্রত্নতাত্ত্বিকদের কাছে এটি অত্যন্ত মূল্যবান একটি নিদর্শন।",
            "locationEn": "Shibganj, Chapainawabganj",
            "locationBn": "শিবগঞ্জ, চাঁপাইনবাবগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Dhania%20Chak%20Mosque%2C%20Shibganj%2C%20Chapainawabganj"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Mahananda Riverbank",
            "nameBn": "মহানন্দা নদীতীর",
            "categoryEn": "Scenic Riverfront Promenade & Boat Haven",
            "categoryBn": "মনোরম মহানন্দা নদীতীর ওয়াকওয়ে ও সূর্যাস্ত",
            "descEn": "The Mahananda Riverbank flanking Chapainawabganj town is a picturesque freshwater promenade celebrated for its cool evening breezes, sandy shoals, and scenic river crossings. Originating in the Himalayas, the river's gentle waters glide past lush green mango orchards, historic trading ghats, and peaceful pottery hamlets. A modern paved riverfront boulevard features shaded seating alcoves, decorative streetlamps, and panoramic sunset viewing decks where local families and visitors unwind daily. Traditional wooden country boats ferry travelers across to agricultural sandbars, offering relaxing riverboat excursions against golden twilight skies. It provides a delightful civic sanctuary connecting urban life with nature.",
            "descBn": "চাঁপাইনবাবগঞ্জ শহরের বুক চিরে বয়ে চলা শান্ত মহানন্দা নদীর তীর শহরবাসীর প্রাণ জুড়ানো সান্ধ্যকালীন বিনোদনের প্রধান কেন্দ্র। হিমালয় থেকে নেমে আসা এই নদীর দুই পাড়ের সবুজে ঘেরা আমবাগান এবং স্বচ্ছ জলরাশি মনকে মুগ্ধ করে। নদীপাড়ের আধুনিক ওয়াকওয়েতে হাঁটতে এবং বিকেলে শীতল বাতাসে বসে সূর্যাস্ত দেখতে হাজারো মানুষ এখানে সমবেত হন। দেশীয় ছোট ছোট নৌকায় চড়ে নদীর বুকে ভেসে বেড়ানো পর্যটকদের দারুণ আনন্দ দেয়। নদীর শান্ত ঢেউ আর দূরবর্তী চরের রূপ মিলে মহানন্দা নদীতীর এক অসাধারণ স্নিগ্ধ পরিবেশ সৃষ্টি করেছে।",
            "locationEn": "Chapainawabganj town",
            "locationBn": "চাঁপাইনবাবগঞ্জ শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Mahananda%20Riverbank%2C%20Chapainawabganj%20town"
        },
        {
            "id": 2,
            "nameEn": "Bholahat mango orchards",
            "nameBn": "ভোলাহাটের সুবিশাল আমবাগান",
            "categoryEn": "World-Famous Heritage Agro-Orchard Lands",
            "categoryBn": "ঐতিহাসিক ফজলি ও খিরসাপাত আমের সবুজ বাগান",
            "descEn": "The Bholahat mango orchards represent the agricultural crown jewel of Chapainawabganj, producing some of the sweetest, largest, and most coveted mango varieties on earth. Spanning thousands of contiguous acres along the Mahananda River basin, the orchards feature towering heritage trees over a century old yielding legendary cultivars including Fazli, Khirsapat (Himsagar), Langra, and Ashwina. In the summer harvest season from May to July, the entire countryside is saturated with the intoxicating fragrance of ripening mangoes, with farmers carefully hand-picking fruits using long bamboo poles. Agritourists visit to walk under the cooling green canopy, sample freshly harvested fruits directly from growers, and experience the joyous festivities of northern harvest culture. It is an unforgettable sensory adventure.",
            "descBn": "চাঁপাইনবাবগঞ্জের ভোলাহাট উপজেলার সুবিশাল আমবাগান সমগ্র বাংলাদেশের গর্ব ও বিশ্বখ্যাত সুস্বাদু আমের প্রধান রাজধানী। মহানন্দা নদীর উর্বর পললভূমিতে মাইলের পর মাইল জুড়ে বিস্তৃত এই বাগানগুলোতে রয়েছে শতবর্ষী বিশাল আমগাছ। গ্রীষ্মের মৌসুমে ফজলি, খিরসাপাত (হিমসাগর), ল্যাংড়া, গোপালভোগ ও লক্ষণভোগ আমের ম ম গন্ধে সমগ্র অঞ্চল মাতোয়ারা হয়ে ওঠে। দূর-দূরান্ত থেকে পর্যটকরা এই সবুজ বাগানের ছায়ায় ঘুরতে আসেন এবং গাছ থেকে সরাসরি পাড়া মিষ্টি আমের তাজা স্বাদ গ্রহণ করেন। আম চাষীদের কর্মমুখর জীবন ও ঐতিহ্যবাহী ফলন উৎসব দেখতে ভোলাহাট এক অনন্য স্বর্গরাজ্য।",
            "locationEn": "Bholahat; best in mango season",
            "locationBn": "ভোলাহাট, চাঁপাইনবাবগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Bholahat%20mango%20orchards%2C%20Bholahat%3B%20best%20in%20mango%20season"
        },
        {
            "id": 3,
            "nameEn": "Kansat mango market",
            "nameBn": "কানসাট এশিয়ার বৃহত্তম আম বাজার",
            "categoryEn": "Asia's Largest Wholesale Mango Emporium",
            "categoryBn": "এশিয়ার বৃহত্তম আম বাজার ও মৌসুমি মহাউৎসব",
            "descEn": "Kansat Mango Market in Shibganj Upazila is celebrated as the largest wholesale mango trading hub in Asia, transforming into an astonishing spectacle of commerce during the summer months. Stretches for over two kilometers along the regional highway, tens of thousands of growers arrive daily on custom bicycle vans, bullock carts, and wooden boats laden with tons of golden mangoes. Multi-ton wholesale deals for Fazli, Himsagar, and Amrapali take place amid energetic bargaining, while fleets of courier trucks and trucks transport the fruits across Bangladesh and to international export terminals. The sheer scale, vibrant energy, sweet aromas, and friendly chaos of Kansat provide an exhilarating, world-class cultural phenomenon found nowhere else on earth.",
            "descBn": "শিবগঞ্জ উপজেলার কানসাট আম বাজার এশিয়ার বৃহত্তম এবং সবচেয়ে প্রাণবন্ত আমের পাইকারি বিপণন কেন্দ্র। প্রতি বছর মে থেকে জুলাই মাসে প্রায় দুই কিলোমিটার জুড়ে গড়ে ওঠা এই বাজারে প্রতিদিন হাজার হাজার টন সুস্বাদু আম কেনাবেচা হয়। ভোর থেকেই হাজারো ভ্যানগাড়ি, সাইকেল ও ট্রাকে করে চাষিরা টাটকা আম নিয়ে এখানে আসেন, যা দেখতে সমগ্র দেশ থেকে পর্যটক ও পাইকাররা ভিড় জমান। বিখ্যাত ফজলি ও খিরসাপাত আমের পাহাড় আর ক্রেতা-বিক্রেতার উৎসবমুখর কোলাহলে পুরো কানসাট মুখরিত থাকে। বাংলাদেশের কৃষি অর্থনীতি ও ফল উৎসবের এমন মহাকাব্যিক রূপ দেখতে কানসাট এক অনন্য বিস্ময়।",
            "locationEn": "Kansat, Shibganj",
            "locationBn": "কানসাট, শিবগঞ্জ, চাঁপাইনবাবগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Kansat%20mango%20market%2C%20Kansat%2C%20Shibganj"
        },
        {
            "id": 4,
            "nameEn": "Nawabganj municipal park",
            "nameBn": "নবাবগঞ্জ পৌর পার্ক ও ক্লাব চত্বর",
            "categoryEn": "Civic Botanical Garden & Promenade",
            "categoryBn": "পৌর বিনোদন উদ্যান ও পরিবারিক অবসর চত্বর",
            "descEn": "Nawabganj Municipal Park, centrally located within Chapainawabganj town, is the primary urban recreation haven providing green leisure for local residents. The park boasts manicured lawns, circular jogging tracks, shaded pavilions, and a peaceful water pond populated by fish and lotus blossoms. Dedicated play zones equipped with swings and slides keep young children engaged, while comfortable benches under mature trees host lively intellectual debates among elders. Evening lighting creates a warm, welcoming ambiance for relaxing after a day exploring the historical monuments of Gaur. It is a clean, family-friendly oasis in the district center.",
            "descBn": "চাঁপাইনবাবগঞ্জ জেলা শহরের প্রাণকেন্দ্রে অবস্থিত নবাবগঞ্জ পৌর পার্ক শহরবাসীর দৈনিক শরীরচর্চা ও পরিবারের সাথে মনোরম সময় কাটানোর এক চমৎকার সবুজ চত্বর। রঙিন ফুলের বাগান, সুদৃশ্য জলাশয় এবং পাকা হাঁটার পথ পার্কটিকে দৃষ্টিনন্দন রূপ দিয়েছে। শিশুদের জন্য রয়েছে নিরাপদ খেলার রাইড এবং বড়দের জন্য ছায়াঘেরা বসার ব্যবস্থা। গৌড়ের ঐতিহাসিক প্রাচীন নিদর্শন ঘুরে আসার পর সন্ধ্যায় নির্মল পরিবেশে ক্লান্তি দূর করতে পর্যটকদের জন্য এটি এক নিখুঁত বিশ্রামস্থল। শহরের নাগরিক জীবনে আনন্দ ও স্বস্তি এনে দিতে এই পার্কটির ভূমিকা অত্যন্ত প্রশংসনীয়।",
            "locationEn": "Chapainawabganj town",
            "locationBn": "চাঁপাইনবাবগঞ্জ শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Nawabganj%20municipal%20park%2C%20Chapainawabganj%20town"
        },
        {
            "id": 5,
            "nameEn": "Padma Riverbank",
            "nameBn": "পদ্মা নদীতীর ও চরাঞ্চল",
            "categoryEn": "Mighty Padma River Corridor & Sandbars",
            "categoryBn": "ঐতিহাসিক পদ্মা নদীতীর, বালিচর ও সূর্যাস্ত",
            "descEn": "The Padma Riverbank in southern Chapainawabganj is an awe-inspiring natural frontier where one of the world's greatest rivers enters Bangladesh from India. Spanning immense widths of shimmering silver water, the river corridor features vast seasonal char islands, rolling sand dunes, and brisk winds carrying the scent of river water. Visitors can hire country boats to voyage across the sweeping currents, watching local fishermen haul in prize hilsa fish and river prawns against endless horizons. Sunset over the Padma is an unforgettable natural theater where golden and purple reflections dance across the roaring waves. It offers an inspiring, soul-stirring communion with Bangladesh's most majestic river.",
            "descBn": "চাঁপাইনবাবগঞ্জের দক্ষিণ প্রান্তে অবস্থিত পদ্মা নদীর তীর বাংলাদেশের অন্যতম বৃহৎ ও উন্মুক্ত নদী সীমানা। ভারত থেকে বাংলাদেশে প্রবেশের মুখেই পদ্মা এখানে এক সুবিশাল ও উত্তাল রূপ ধারণ করেছে। নদীর ধূ-ধূ বালুচর, বাতাসে উড়ে চলা সাদা কাশফুল এবং বিশাল জলরাশি এক অপার্থিব দৃশ্যের জন্ম দেয়। দেশীয় নৌকায় চড়ে পদ্মার বুকে ভেসে বেড়ানো এবং জেলেদের পদ্মার তাজা ইলিশ শিকারের দৃশ্য যে কোনো পর্যটককে রোমাঞ্চিত করে। গোধূলিবেলায় পদ্মার ঢেউয়ে সূর্যের রক্তিম আলোর ঝিকমিক এক মোহনীয় রূপ ধারণ করে। নদীমাতৃক বাংলার আদিম ও রুদ্রসুন্দর রূপ দেখতে পদ্মার এই তীর এক চমৎকার গন্তব্য।",
            "locationEn": "Chapainawabganj district; check river conditions",
            "locationBn": "পদ্মা নদীতীর, চাঁপাইনবাবগঞ্জ",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Padma%20Riverbank%2C%20Chapainawabganj%20district%3B%20check%20river%20conditions"
        }
    ]
}

# 12. BANDARBAN
bandarban = {
    "slug": "bandarban",
    "en": "Bandarban",
    "bn": "বান্দরবান",
    "hero_title_en": "Bandarban Soaring Peaks & Cloud Sanctuaries",
    "hero_title_bn": "বান্দরবানের নীলগিরি ও স্বর্ণমন্দিরের স্বর্গরাজ্য",
    "hero_sub_en": "Highest peaks of Bangladesh, majestic golden temples, and wild Sangu river gorges.",
    "hero_sub_bn": "মেঘে ঢাকা নীলগিরির চূড়া, স্বর্ণ মন্দির এবং খরস্রোতা সাঙ্গু নদীর পাথুরে গিরিখাত।",
    "tagline_en": "The roof of Bangladesh and the ultimate highland wilderness, renowned for the cloud-draped peaks of Nilgiri and Nilachal, sacred gilded Buddhist stupas at Buddha Dhatu Jadi, and the untamed beauty of the Sangu River.",
    "tagline_bn": "বাংলাদেশের ছাদ খ্যাত সর্বোচ্চ পাহাড়ি জেলা, যা মেঘের দেশ নীলগিরি ও নীলাচল, স্বর্ণালী বুদ্ধ ধাতু জাদি এবং রহস্যময় সাঙ্গু নদীর অপার সৌন্দর্যের জন্য বিশ্বজোড়া খ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/bandarban/carousel-1.webp",
            "titleEn": "Nilgiri Mountain Peak in the Clouds",
            "titleBn": "নীলগিরির মেঘের ওপর দাঁড়িয়ে থাকা পাহাড়চূড়া",
            "subtitleEn": "Spectacular highland peak at 2,200 feet where rolling clouds envelop visitors under endless mountain horizons",
            "subtitleBn": "সমুদ্রপৃষ্ঠ থেকে ২২০০ ফুট উঁচুতে অবস্থিত মেঘের রাজ্য, যেখানে মেঘের সমুদ্র এসে ছুঁয়ে যায় পাহাড়ের শরীর"
        },
        {
            "id": 2,
            "image": "images/districts/bandarban/carousel-2.webp",
            "titleEn": "Buddha Dhatu Jadi (Golden Temple)",
            "titleBn": "স্বর্ণ মন্দির (বুদ্ধ ধাতু জাদি)",
            "subtitleEn": "Gleaming golden Theravada Buddhist temple perched majestically atop a high peak in Balaghata",
            "subtitleBn": "বালাঘাটায় পাহাড়ের চূড়ায় অবস্থিত চোখধাঁধানো স্বর্ণালী বুদ্ধ মন্দির, যা দেশের বৃহত্তম বৌদ্ধ ধাতু জাদি"
        },
        {
            "id": 3,
            "image": "images/districts/bandarban/carousel-3.webp",
            "titleEn": "Nilachal Breathtaking Mountain Sunset Overlook",
            "titleBn": "নীলাচলের অপার্থিব সূর্যাস্ত ও মেঘের খেলা",
            "subtitleEn": "Panoramic ridge overlooking Bandarban town offering sensational sunsets and rolling green hill waves",
            "subtitleBn": "টাইগারপাড়ায় অবস্থিত সুউচ্চ ভিউপয়েন্ট, যেখান থেকে রক্তিম সূর্যাস্ত ও চারপাশের সবুজ পাহাড়ের দৃশ্য মুগ্ধ করে"
        },
        {
            "id": 4,
            "image": "images/districts/bandarban/carousel-4.webp",
            "titleEn": "Sangu River Stone Gorges & Crystal Rapids",
            "titleBn": "সাঙ্গু নদীর পাথুরে গিরিখাত ও স্বচ্ছ জলধারা",
            "subtitleEn": "Pristine mountain river carving dramatically through steep stone cliffs and remote tribal hamlets",
            "subtitleBn": "পাহাড়ের বুক চিরে বয়ে চলা পাহাড়ি নদী সাঙ্গু, যার পাথুরে বাঁক ও স্বচ্ছ জলরাশি এক পরম বিস্ময়"
        },
        {
            "id": 5,
            "image": "images/districts/bandarban/carousel-5.webp",
            "titleEn": "Chimbuk Hill Third Highest Peak",
            "titleBn": "চিম্বুক পাহাড়ের সুউচ্চ শৈলশিরা",
            "subtitleEn": "Historic highland range known as the 'Darjeeling of Bengal' offering panoramic cloud seas and fresh mountain air",
            "subtitleBn": "বাংলার দার্জিলিং খ্যাত চিম্বুক পাহাড়ের সুউচ্চ চূড়া, যেখান থেকে দেখা যায় মেঘ আর পাহাড়ের অনন্ত খেলা"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Buddha Dhatu Jadi (Golden Temple)",
            "nameBn": "বুদ্ধ ধাতু জাদি (স্বর্ণ মন্দির)",
            "categoryEn": "Sacred Golden Theravada Temple & Relic Stupa",
            "categoryBn": "পবিত্র স্বর্ণ মন্দির ও দেশের বৃহত্তম বৌদ্ধ ধাতু জাদি",
            "descEn": "Buddha Dhatu Jadi, famously known as the Bandarban Golden Temple, is a breathtaking Theravada Buddhist sanctuary perched majestically atop a 300-foot-high forested hill at Balaghata. Completed in 2000 under the spiritual inspiration of Ven. U Pannya Jota Mahathero, this architectural wonder is the largest Buddhist stupa in Bangladesh. Built in authentic Southeast Asian Arakanese style, the dazzling multi-tiered temple is entirely coated in glistening gold leaf, housing a sacred second-century relic (dhatu) of Gautama Buddha alongside a massive black and gold stone Buddha statue. The elevated sanctum features marble courtyards, ornamental mythical guardian figures, and a sacred lotus pond named 'Debota Pukur'. It stands as a beacon of Buddhist enlightenment, architectural majesty, and spiritual tranquility.",
            "descBn": "বান্দরবান শহরের অদূরে বালাঘাটায় পাহাড়ের চূড়ায় অবস্থিত বুদ্ধ ধাতু জাদি (স্বর্ণ মন্দির) বাংলাদেশের সবচেয়ে দৃষ্টিনন্দন ও সর্ববৃহৎ থেরবাদ বৌদ্ধ মন্দির। ২০০০ সালে নির্মিত এই মন্দিরটি সম্পূর্ণ মিয়ানমার ও আরাকানি স্থাপত্যরীতির অনুসরণে সোনালী রঙে সজ্জিত। মন্দিরের মূল বেদিতে সংরক্ষিত রয়েছে গৌতম বুদ্ধের পবিত্র ধাতু (দেহের স্মৃতিচিহ্ন) এবং এক বিশাল স্বর্ণালী বুদ্ধমূর্তি। মন্দির প্রাঙ্গণে রয়েছে শ্বেতপাথরের চত্বর, ড্রাগনের মূর্তি এবং পাহাড়ের শীর্ষে অবস্থিত এক অলৌকিক 'দেবতা পুকুর'। পাহাড়ের শীতল বাতাস ও ঘণ্টার মধুর ধ্বনি এক অপার্থিব আধ্যাত্মিক পরিবেশের সৃষ্টি করে, যা দেশ-বিদেশের পর্যটকদের অভিভূত করে।",
            "locationEn": "Balaghata, Bandarban Sadar",
            "locationBn": "বালাঘাটা, বান্দরবান সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Buddha%20Dhatu%20Jadi%20(Golden%20Temple)%2C%20Balaghata%2C%20Bandarban%20Sadar"
        },
        {
            "id": 2,
            "nameEn": "Bandarban Royal Palace",
            "nameBn": "বান্দরবান বোমাং রাজবাড়ি",
            "categoryEn": "Ancestral Seat of the Bohmong King",
            "categoryBn": "ঐতিহাসিক বোমাং রাজার রাজপ্রাসাদ ও দরবার",
            "descEn": "The Bandarban Royal Palace is the historic administrative seat and royal residence of the Bohmong King, the revered traditional ruler of the Bohmong Circle encompassing southern Chittagong Hill Tracts. Located in the heart of Bandarban town, the palace complex features traditional Marma architectural elements blended with colonial administrative halls, royal audience pavilions, and ancestral heritage collections. The royal lineage traces back over four centuries to the Arakanese kings of Burma. Every winter, the palace grounds host the historic 'Rajpunyah' festival, where the Bohmong King, clad in royal silk robes and gold crowns, receives tax tributes and homage from hundreds of tribal headmen amidst colorful traditional dances and music. It remains a living monument to indigenous monarchical heritage.",
            "descBn": "বান্দরবান শহরের প্রাণকেন্দ্রে অবস্থিত বোমাং রাজবাড়ি পাহাড়ি মারমা জনগোষ্ঠীর সুপ্রাচীন ঐতিহ্য ও রাজকীয় শাসনের প্রধান কেন্দ্র। চারশত বছরেরও বেশি প্রাচীন ইতিহাস সমৃদ্ধ এই রাজবংশ আরাকানি রাজপরিবারের সাথে ঐতিহাসিকভাবে সম্পর্কিত। রাজপ্রাসাদে সংরক্ষিত আছে প্রাচীন রাজদণ্ড, ঐতিহ্যবাহী তরবারি, পোশাক এবং রাজপরিবারের স্মৃতিস্মারক। প্রতি বছর শীতকালে এই রাজবাড়ি প্রাঙ্গণে অনুষ্ঠিত হয় শতাব্দীপ্রাচীন 'রাজপুণ্যাহ' মেলা, যেখানে রাজা প্রজাদের সাথে মিলিত হন এবং বার্ষিক রাজস্ব গ্রহণ করেন। পাহাড়ি জাতিগোষ্ঠীর আত্মপরিচয়, কৃষ্টি ও সাংস্কৃতিক স্বকীয়তার এক রাজকীয় প্রতীক এই বোমাং রাজবাড়ি।",
            "locationEn": "Bandarban town; access may be restricted",
            "locationBn": "বান্দরবান শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Bandarban%20Royal%20Palace%2C%20Bandarban%20town%3B%20access%20may%20be%20restricted"
        },
        {
            "id": 3,
            "nameEn": "Rijuk Buddhist temple area",
            "nameBn": "রিজুক ঐতিহাসিক বৌদ্ধ মন্দির",
            "categoryEn": "Sacred Mountain Monastery & Forest Shrine",
            "categoryBn": "পাহাড়ি বৌদ্ধ বিহার ও সাধনা কেন্দ্র",
            "descEn": "The Rijuk Buddhist Temple area, located deep in the mountainous valleys near Ruma along the pristine Sangu River, is an ancient monastic haven of deep spiritual significance. Built atop forested stone slopes, the temple features hand-carved teakwood shrines, gilded Buddha statues, and open-air meditation pavilions where forest monks practice mindfulness away from worldly noise. Local indigenous Marma and Bawm pilgrims hike along river trails to offer forest honey, wild fruits, and lotus blooms during holy Full Moon observances. The whispering sounds of the nearby Rijuk Waterfall and the chanting of monastic prayers create an atmosphere of profound serenity. It is a treasured destination for travelers seeking peaceful spiritual contemplation.",
            "descBn": "রুমা উপজেলার সাঙ্গু নদীর তীরবর্তী নিবিড় পাহাড়ি অঞ্চলে অবস্থিত রিজুক বৌদ্ধ মন্দির এক সুপ্রাচীন ও শান্তিময় আধ্যাত্মিক সাধনা কেন্দ্র। পাহাড়ের পাথুরে ধাপে গড়ে ওঠা এই মন্দিরে রয়েছে প্রাচীন কাঠের কারুকাজ এবং ধ্যানমগ্ন বুদ্ধের বিগ্রহ। পাহাড়ি ভিক্ষুরা এখানে নির্জন প্রকৃতির কোলে ধ্যানচর্চা করে থাকেন। মারমা ও বম সম্প্রদায়ের মানুষ বিভিন্ন পূর্ণিমা তিথিতে এখানে এসে পূজা ও চীবর দান করে থাকেন। কাছেই অবস্থিত গর্জনকারী রিজুক ঝরনার জলপ্রপাত এবং মন্দিরের আধ্যাত্মিক আবহ মিলে এক অপার্থিব পরিবেশের সৃষ্টি করেছে, যা ভ্রমণকারীদের মনকে নির্মল প্রশান্তি দান করে।",
            "locationEn": "Bandarban region; confirm access",
            "locationBn": "রুমা, বান্দরবান",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Rijuk%20Buddhist%20temple%20area%2C%20Bandarban%20region%3B%20confirm%20access"
        },
        {
            "id": 4,
            "nameEn": "Traditional Marma cultural area",
            "nameBn": "ঐতিহ্যবাহী মারমা সাংস্কৃতিক জনপদ",
            "categoryEn": "Indigenous Ethnic Marma Heritage & Architecture",
            "categoryBn": "মারমা আদিবাসী সংস্কৃতি, মাচাং ঘর ও ঐতিহ্য",
            "descEn": "The traditional Marma cultural areas spread across the Bandarban valleys offer visitors an enriching encounter with the indigenous heritage of the district's largest ethnic community. Marma villages are characterized by picturesque raised wooden houses on stilts (machang), built from seasoned bamboo and hardwood along river corridors. Visitors can observe community life, including traditional waist-loom weaving of colorful 'Thami' garments, organic ginger and turmeric farming, and traditional silver jewelry smithing. During the mid-April 'Sangrai' New Year festival, these villages burst into joy with the famous Water Festival ('Pani Khela'), where young and old splash water to wash away the sorrows of the past year. It is a heartwarming cultural experience that celebrates harmony with nature.",
            "descBn": "বান্দরবানের বিভিন্ন উপত্যকায় গড়ে ওঠা মারমা জনপদগুলো তাদের সমৃদ্ধ সংস্কৃতি, ঐতিহ্যবাহী কাঠের মাচাং ঘর এবং সরল জীবনযাত্রার জন্য সুপরিচিত। এখানকার প্রতিটি গ্রামে দেখা যায় প্রকৃতির সাথে একাত্ম হয়ে বাঁচার এক অপূর্ব ছন্দ। মারমা নারীদের নিপুণ হাতে বোনা থামি, রূপার গহনা এবং পাহাড়ি খাবারের সংস্কৃতি অত্যন্ত বৈচিত্র্যময়। বিশেষ করে প্রতি বছর চৈত্র সংক্রান্তিতে আয়োজিত ঐতিহ্যবাহী 'সাংগ্রাই' উৎসব ও জলকেলি (পানি খেলা) পুরো জনপদকে এক আনন্দমুখর মিলনমেলায় পরিণত করে। মারমা জনগোষ্ঠীর গভীর সংস্কৃতি ও আন্তরিক আতিথেয়তা পর্যটকদের মুগ্ধ করে।",
            "locationEn": "Bandarban; visit respectfully",
            "locationBn": "বান্দরবান পাহাড়ি অঞ্চল",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Traditional%20Marma%20cultural%20area%2C%20Bandarban%3B%20visit%20respectfully"
        },
        {
            "id": 5,
            "nameEn": "Nilachal viewpoint area",
            "nameBn": "নীলাচল ঐতিহাসিক পাহাড় চূড়া ও স্মৃতি",
            "categoryEn": "Highland Mountain Summit & Sunset Lookout",
            "categoryBn": "টাইগারপাড়া নীল পাহাড় ও ঐতিহাসিক স্মৃতিচিহ্ন",
            "descEn": "The Nilachal viewpoint area at Tigerpara, situated at an altitude of nearly 2,000 feet above sea level, is one of the most historically iconic mountain lookouts in Bandarban. Known poetically as the 'Blue Hill' because of the violet mist that covers its peaks at twilight, the summit features traditional open-air bamboo cottages, spiral pedestrian viewing ramps, and dramatic clifftop terraces. Local indigenous history recounts that ancient lookouts used this high peak to monitor approaching naval flotillas along the Sangu River basin. Today, visitors stand atop the breezeswept ridge to watch rolling cloud seas flow beneath their feet as the setting sun paints distant hill ranges in shades of crimson and gold. It offers a majestic and soul-stirring communion with the highland soul of Bangladesh.",
            "descBn": "বান্দরবান শহর থেকে মাত্র ৫ কিলোমিটার দূরে টাইগারপাড়ায় অবস্থিত নীলাচল প্রায় ২০০০ ফুট উঁচুতে এক স্বপ্নিল পাহাড়ি ভিউপয়েন্ট। গোধূলিবেলায় দূর পাহাড়ের গায়ে নীলচে কুয়াশার চাদর বিছিয়ে যায় বলেই এর নাম 'নীলাচল'। পাহাড়ের চূড়ায় নির্মিত গোলঘর, সুদৃশ্য কাঠের কটেজ এবং চারপাশের খাড়া খাদ থেকে মেঘের উড়ে চলা অবলোকন করা যায়। এখান থেকে এক পলকে দেখা যায় পুরো বান্দরবান শহর এবং সাঙ্গু নদীর রুপালী রেখা। বিকেলে নীলাচলের চূড়া থেকে সূর্যাস্তের রক্তিম আভা দেখা জীবনের অন্যতম শ্রেষ্ঠ রোমাঞ্চকর অভিজ্ঞতা। মেঘ-পাহাড়ের মিতালী দেখতে নীলাচল এক অনন্য স্বর্গোদ্যান।",
            "locationEn": "Tigerpara, Bandarban Sadar",
            "locationBn": "টাইগারপাড়া, বান্দরবান সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Nilachal%20viewpoint%20area%2C%20Tigerpara%2C%20Bandarban%20Sadar"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Nilgiri",
            "nameBn": "নীলগিরি",
            "categoryEn": "High-Altitude Cloud Kingdom & Mountain Resort",
            "categoryBn": "মেঘের রাজ্য নীলগিরি ও ২২০০ ফুট উঁচুতে রিসোর্ট",
            "descEn": "Nilgiri, situated approximately 50 kilometers south of Bandarban town along the Thanchi highway, is the internationally celebrated 'Crown of Bangladesh Highland Tourism'. Perched at an astonishing elevation of over 2,200 feet above sea level, this mountain resort operated by the Bangladesh Army allows visitors to literally walk inside drifting clouds. The breathtaking panoramic views from the summit take in endless waves of blue mountains stretching into neighboring Myanmar, while the silver Sangu River glistens like a thin ribbon in the deep ravines below. Luxury wooden cottages perched on clifftops, helicopter pads, and viewing decks offer world-class hospitality in the high wilderness. Experiencing dawn at Nilgiri, as golden light pierces oceans of white clouds, is universally acclaimed as the ultimate mountain spectacle in Bangladesh.",
            "descBn": "বান্দরবান-থানচি সড়কে সমুদ্রপৃষ্ঠ থেকে প্রায় ২২০০ ফুট উঁচুতে অবস্থিত নীলগিরি বাংলাদেশের পর্যটনের সবচেয়ে উঁচু ও স্বর্গীয় মেঘের রাজ্য। বাংলাদেশ সেনাবাহিনী কর্তৃক পরিচালিত এই চমৎকার পাহাড়ি রিসোর্টে মেঘের দল যেন ঘরের বারান্দায় এসে খেলা করে। পাহাড়চূড়া থেকে চারপাশের অনন্ত নীল পাহাড়ের ঢেউ এবং নিচে সাঙ্গু নদীর বয়ে চলা এক অভাবনীয় রূপ প্রকাশ করে। মেঘমুক্ত দিনে এখান থেকে সুদূর বঙ্গোপসাগরের আভাসও পাওয়া যায়। মেঘের সমুদ্রে গা ভাসিয়ে সূর্যোদয় ও সূর্যাস্ত দেখা এক অপার্থিব জীবনের অনুভূতি এনে দেয়। প্রকৃতির শ্রেষ্ঠতম রোমাঞ্চ উপভোগ করতে নীলগিরি ভ্রমণ এক পরম স্বপ্নময় অভিজ্ঞতা।",
            "locationEn": "Thanchi road; check current security/access",
            "locationBn": "থানচি সড়ক, বান্দরবান",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Nilgiri%2C%20Thanchi%20road%3B%20check%20current%20security/access"
        },
        {
            "id": 2,
            "nameEn": "Nilachal",
            "nameBn": "নীলাচল পর্যটন কমপ্লেক্স",
            "categoryEn": "Panoramic Hilltop Park & Cloud Observation",
            "categoryBn": "নীলাচল মেঘ দর্শন ডেক ও সূর্যাস্ত পয়েন্ট",
            "descEn": "Nilachal, perched atop Tigerpara just 5 kilometers from Bandarban town, is the premier highland escape offering effortless access to the magical world of the hills. Rising nearly 2,000 feet, the site features modern clifftop viewing balconies, thatched resting pavilions, beautifully landscaped flowerbeds, and the iconic 'Jhulanta Kureegor' cottages cantilevered over deep ravines. Visitors can stroll along paved ridge paths breathing in pure mountain air, watching rainclouds sweep rapidly across the forested valleys below. During twilight, the entire horizon transforms into a glowing canvas of purple, gold, and crimson light that illuminates the distant mountain silhouettes. It is widely loved as the most accessible and visually rewarding sunset spot in the district.",
            "descBn": "বান্দরবান শহর থেকে মাত্র কয়েক কিলোমিটার দূরে অবস্থিত নীলাচল পর্যটন কেন্দ্র তার জাদুকরী সৌন্দর্য ও মেঘের খেলার জন্য বিখ্যাত। প্রায় ২০০০ ফুট উঁচুতে অবস্থিত এই পাহাড়চূড়া থেকে চারপাশের দিগন্তজোড়া সবুজ পাহাড়ের দৃশ্য চোখ জুড়িয়ে দেয়। এখানে পাহাড়ের ঢালে রয়েছে দৃষ্টিনন্দন কটেজ, ঝুলন্ত ব্যালকনি এবং বিশ্রামের ছাদযুক্ত শেড। বর্ষায় ও শীতে এখানে মেঘের দল এসে পর্যটকদের শরীর ভিজিয়ে দিয়ে যায়। বিকেলে পাহাড়ের ওপারে রক্তিম সূর্যের অস্ত যাওয়ার দৃশ্য এক মায়াবী অনুভূতি তৈরি করে। স্বল্প সময়ে পাহাড় আর মেঘের অপার সৌন্দর্য উপভোগ করতে নীলাচল এক অতুলনীয় গন্তব্য।",
            "locationEn": "Tigerpara, Bandarban Sadar",
            "locationBn": "টাইগারপাড়া, বান্দরবান সদর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Nilachal%2C%20Tigerpara%2C%20Bandarban%20Sadar"
        },
        {
            "id": 3,
            "nameEn": "Meghla Tourist Complex",
            "nameBn": "মেঘলা পর্যটন কমপ্লেক্স",
            "categoryEn": "Family Eco-Park, Lake & Hanging Bridges",
            "categoryBn": "পাহাড়ি লেক, ক্যাবল কার ও ঝুলন্ত সেতু কমপ্লেক্স",
            "descEn": "Meghla Tourist Complex, situated on the entrance gateway to Bandarban town, is an enchanting family eco-park and recreation haven spread over extensive hilly terrain. The park is centered on a serene artificial lake framed by emerald hills, spanned by two dramatic suspension hanging footbridges that sway gently as visitors cross. Attractions include a scenic passenger cable car ropeway gliding high above the water, paddle boat rentals, a mini zoo with indigenous wildlife, and lush botanical gardens with children's amusement rides. Shaded picnic gazebos and paved trails winding through teak and mahogany plantations provide delightful leisure for travelers of all generations. It is Bandarban's most popular family entertainment destination.",
            "descBn": "বান্দরবান শহরের প্রবেশমুখে অবস্থিত মেঘলা পর্যটন কমপ্লেক্স পাহাড় ও হ্রদের মেলবন্ধনে গড়ে ওঠা এক চমৎকার পারিবারিক বিনোদন কেন্দ্র। পাহাড়ের কোল ঘেঁষে তৈরি কৃত্রিম হ্রদের ওপর টানানো রয়েছে দুটি দীর্ঘ ও রোমাঞ্চকর ঝুলন্ত সেতু। লেকের ওপর দিয়ে উড়ে চলা ক্যাবল কারে চড়ে পাখির চোখে চারপাশের সবুজের দৃশ্য উপভোগ করা যায়। এছাড়াও এখানে রয়েছে প্যাডেল বোটিং, মিনি চিড়িয়াখানা, শিশুদের বিভিন্ন রাইড এবং চমৎকার পিকনিক স্পট। সবুজে ঘেরা ছায়াশীতল পরিবেশ এবং পাহাড়-হ্রদের অপূর্ব সৌন্দর্য মেঘলাকে পর্যটকদের কাছে এক অত্যন্ত প্রিয় গন্তব্যে পরিণত করেছে।",
            "locationEn": "Bandarban town outskirts",
            "locationBn": "বান্দরবান শহরতলী",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Meghla%20Tourist%20Complex%2C%20Bandarban%20town%20outskirts"
        },
        {
            "id": 4,
            "nameEn": "Chimbuk Hill",
            "nameBn": "চিম্বুক পাহাড়",
            "categoryEn": "Historic Third-Highest Peak & Scenic Ridge",
            "categoryBn": "বাংলার দার্জিলিং খ্যাত চিম্বুক পাহাড়ের চূড়া",
            "descEn": "Chimbuk Hill, situated about 25 kilometers from Bandarban along the Thanchi highway, is the third-highest mountain peak in Bangladesh and one of its earliest famous hill attractions. Rising to an altitude of approximately 2,500 feet, the historic mountain range was affectionately christened the 'Darjeeling of Bengal' by early explorers because of its cool climate and mist-covered evergreen peaks. A winding highway hugs the mountain ridges, offering breathtaking drop-offs into deep gorges on both sides. From the summit observation towers, visitors look out over an endless ocean of mountain waves stretching as far as the eye can see, dotted with authentic Bawm and Murong tribal hamlets. Fresh wild fruits, roasted mountain corn, and panoramic breezes make Chimbuk an unforgettable mountain stop.",
            "descBn": "বান্দরবান শহর থেকে থানচি যাওয়ার পথে অবস্থিত চিম্বুক পাহাড় বাংলাদেশের অন্যতম সুউচ্চ ও প্রাচীনতম দর্শনীয় পাহাড়। প্রায় ২৫০০ ফুট উঁচু এই পাহাড় তার হিমশীতল বাতাস ও বছরজুড়ে কুয়াশার চাদরে ঢাকা থাকার কারণে 'বাংলার দার্জিলিং' হিসেবে সুপরিচিত। পাহাড়ের শৈলশিরা ধরে এগিয়ে চলা পিচঢালা পথটির দুই পাশে গভীর খাদ এবং অবারিত সবুজের দৃশ্য এক রুদ্ধশ্বাস অনুভূতি দেয়। চিম্বুক চূড়ার ওয়াচটাওয়ার থেকে মেঘের সমুদ্র এবং দূরে সাঙ্গু নদীর আঁকাবাঁকা গতিপথ স্পষ্ট দেখা যায়। স্থানীয় পাহাড়ি বম ও ম্রোদের তৈরি হস্তশিল্প ও তাজা ফলের স্বাদ নিতে নিতে চিম্বুকের চূড়ায় সময় কাটানো এক অনন্য অভিজ্ঞতা।",
            "locationEn": "Bandarban–Thanchi road; check access rules",
            "locationBn": "চিম্বুক, বান্দরবান",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Chimbuk%20Hill%2C%20Bandarban%E2%80%93Thanchi%20road%3B%20check%20access%20rules"
        },
        {
            "id": 5,
            "nameEn": "Sangu River",
            "nameBn": "সাঙ্গু নদী",
            "categoryEn": "Pristine Mountain River Canyon & Boat Safari",
            "categoryBn": "খরস্রোতা পাহাড়ি নদী সাঙ্গু ও ক্যানিয়ন বোট সাফারি",
            "descEn": "The Sangu River (known locally as the Rigrei Khyang) is the sacred lifeline of Bandarban and the only major river in Bangladesh that originates and flows entirely within the country's borders. Cascading out of the deep mountain gorges of the Arakan range, the river carves an astonishing canyon through sheer limestone cliffs, giant boulder beds, and pristine rainforests. Traveling on motorized wooden long-tail boats along the turquoise waters between Ruma, Thanchi, and Remakri offers one of the most thrilling wild river safaris on earth. Visitors glide past remote tribal hamlets, cascading waterfalls splashing into the river, and towering green canyon walls echoing with songbirds. It is the untamed, poetic soul of the Chittagong Hill Tracts.",
            "descBn": "সাঙ্গু নদী বান্দরবানের জীবনরেখা এবং বাংলাদেশের একমাত্র নদী যা দেশের অভ্যন্তরের পাহাড় থেকেই উৎপন্ন হয়ে দেশেতেই শেষ হয়েছে। আরাকান পাহাড়ের গভীর থেকে নেমে আসা এই নদীর জল কাঁচের মতো স্বচ্ছ এবং এর গতিপথ পর্বতঘেরা গিরিখাতের মধ্য দিয়ে। বান্দরবান থেকে রুমা ও থানচি হয়ে রেমাক্রি পর্যন্ত কাঠের ইঞ্জিন বোটে সাঙ্গুর বুকে ভ্রমণ সমগ্র বিশ্বের অন্যতম রোমাঞ্চকর নদী সাফারি। দুই পাশে খাড়া পাথুরে পাহাড়ের দেয়াল, ওপর থেকে নেমে আসা বুনো ঝরনা এবং আদিবাসী জীবনের নৈসর্গিক রূপ সাঙ্গুকে এক পরাবাস্তব সৌন্দর্য দিয়েছে। প্রকৃতির বুনো রূপের স্বাদ পেতে সাঙ্গু নদীতে বোট ভ্রমণ এক অতুলনীয় অভিজ্ঞতা।",
            "locationEn": "Bandarban town and river corridor",
            "locationBn": "সাঙ্গু নদী, বান্দরবান",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Sangu%20River%2C%20Bandarban%20town%20and%20river%20corridor"
        }
    ]
}

# 13. BARGUNA
barguna = {
    "slug": "barguna",
    "en": "Barguna",
    "bn": "বরগুনা",
    "hero_title_en": "Barguna Coastal Mangroves & Ancient Mosques",
    "hero_title_bn": "বরগুনার টেংরাগিরি বন ও সুলতানি বিবিচিনি মসজিদ",
    "hero_sub_en": "Sultanate Bibichini Shahi Mosque, pristine Tengragiri mangrove eco-forest, and Haringhata beaches.",
    "hero_sub_bn": "সুদূর সুলতানি আমলের বিবিচিনি শাহী মসজিদ, টেংরাগিরি ইকো পার্ক ও হরিণঘাটার উপকূলীয় অরণ্য।",
    "tagline_en": "The enchanting coastal frontier of southern Bangladesh bordering the Bay of Bengal, celebrated for the pre-Mughal brick architecture of Bibichini Mosque, the untamed mangrove wilderness of Tengragiri, and endless river estuaries.",
    "tagline_bn": "বঙ্গোপসাগরের মোহনায় অবস্থিত দক্ষিণ বাংলার এক মনোমুগ্ধকর উপকূলীয় জেলা, যা প্রাচীন সুলতানি স্থাপত্যের বিবিচিনি মসজিদ, সুবিশাল টেংরাগিরি ম্যানগ্রোভ বন এবং হরিণঘাটার বন্য নিসর্গের জন্য বিখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/barguna/carousel-1.webp",
            "titleEn": "Tengragiri Eco Park (Fatrar Bon) Mangrove Forest",
            "titleBn": "টেংরাগিরি ইকোপার্ক ও ফাতরার বনের নিসর্গ",
            "subtitleEn": "Sprawling coastal mangrove forest reserve in Taltali bordering the open Bay of Bengal waters",
            "subtitleBn": "তালতলীতে অবস্থিত দ্বিতীয় সুন্দরবন খ্যাত সুবিশাল উপকূলীয় ম্যানগ্রোভ বন ও হরিণের অভয়ারণ্য"
        },
        {
            "id": 2,
            "image": "images/districts/barguna/carousel-2.webp",
            "titleEn": "Bibichini Shahi Mosque Sultanate Heritage",
            "titleBn": "বিবিচিনি শাহী জামে মসজিদের প্রাচীন রূপ",
            "subtitleEn": "Centuries-old brick sanctuary in Betagi built by Saint Shah Niamatullah atop an elevated riverine mound",
            "subtitleBn": "বেতাগীতে এক টিলার ওপর নির্মিত সুফি সাধক শাহ নেয়ামত উল্লাহর স্মৃতিবিজড়িত সুলতানি আমলের মসজিদ"
        },
        {
            "id": 3,
            "image": "images/districts/barguna/carousel-3.webp",
            "titleEn": "Haringhata Coastal Eco Forest & Sea Beach",
            "titleBn": "হরিণঘাটা সংরক্ষিত উপকূলীয় বন ও সৈকত",
            "subtitleEn": "Picturesque coastal forest reserve in Patharghata teeming with spotted deer and migratory bird sanctuaries",
            "subtitleBn": "পাথরঘাটায় অবস্থিত চিত্রা হরিণ, লাল কাঁকড়া ও সাগরের ঢেউয়ে মুখরিত এক চমৎকার প্রাকৃতিক বন"
        },
        {
            "id": 4,
            "image": "images/districts/barguna/carousel-4.webp",
            "titleEn": "Bihanga Island Offshore Marine Sanctuary",
            "titleBn": "বিহঙ্গ দ্বীপ ও সাগরের মোহনা",
            "subtitleEn": "Isolated offshore island at the confluence of the Baleshwar River and Bay of Bengal",
            "subtitleBn": "বলেশ্বর নদীর মোহনায় জেগে ওঠা এক নির্জন স্বর্গীয় দ্বীপ, যেখানে পাখির কলকাকলি ও সাগরের হাওয়া দোলা দেয়"
        },
        {
            "id": 5,
            "image": "images/districts/barguna/carousel-5.webp",
            "titleEn": "Payra-Baleshwar Vast Estuary Waterways",
            "titleBn": "পায়রা-বলেশ্বর নদীর সুবিশাল মোহনা",
            "subtitleEn": "Endless river horizons where mighty southern rivers meet oceanic tides along the coastal fringe",
            "subtitleBn": "বরগুনার নদীমাতৃক উপকূল, যেখানে উত্তাল নদী মোহনায় জেলেদের ট্রলার আর সোনালী সূর্যাস্ত দেখা যায়"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Bibichini Shahi Mosque",
            "nameBn": "বিবিচিনি শাহী মসজিদ",
            "categoryEn": "Pre-Mughal Sultanate Terracotta Sanctuary",
            "categoryBn": "সুলতানি আমলের প্রাচীন ঐতিহাসিক এক গম্বুজ মসজিদ",
            "descEn": "Bibichini Shahi Mosque at Betagi Upazila is an ancient historical monument and the oldest surviving Islamic sanctuary in Barguna district. Established in the mid-seventeenth century by the revered Persian saint Hazrat Shah Niamatullah upon arriving from Delhi to preach Islam in the coastal wilderness, the mosque is named after his beloved sister, Bibi Chini. Built atop an unusually high 30-foot earthen hillock, this fortress-like brick sanctuary features exceptionally thick walls (nearly 6 feet), pointed archways, and a monumental hemispherical dome with ornamental terracotta cornices. The adjacent twin tombs of Shah Niamatullah and Bibi Chini, shaded by sacred ancient trees, preserve an aura of deep spiritual sanctity. It stands as an enduring beacon of early Islamic heritage in the southern coastal delta.",
            "descBn": "বরগুনার বেতাগী উপজেলার বিবিচিনি গ্রামে অবস্থিত বিবিচিনি শাহী মসজিদ দক্ষিণ বাংলার প্রাচীনতম ও অত্যন্ত মর্যাদাপূর্ণ এক ইসলামিক ঐতিহাসিক নিদর্শন। আনুমানিক ১৬৫৯ খ্রিস্টাব্দে ইসলাম প্রচারের উদ্দেশ্যে সুদূর পারস্য থেকে আগমনকারী মহান সাধক শাহ নেয়ামত উল্লাহ তাঁর বোন 'বিবি চিনি'-র নামানুসারে এই মসজিদটি নির্মাণ করেন। প্রায় ৩০ ফুট উঁচু এক টিলার ওপর নির্মিত এই মসজিদের দেওয়ালগুলো প্রায় ছয় ফুট পুরু, যা তৎকালীন প্রতিরক্ষা ও স্থাপত্য কৌশলের অপূর্ব নিদর্শন। মসজিদের পাশে চিরনিদ্রায় শায়িত আছেন শাহ নেয়ামত উল্লাহ ও বিবি চিনি। প্রাচীন স্থাপত্য ও আধ্যাত্মিক আবহ উপভোগ করতে প্রতিদিন বহু পর্যটক ও পুণ্যার্থী এখানে আসেন।",
            "locationEn": "Bibichini, Betagi, Barguna",
            "locationBn": "বিবিচিনি, বেতাগী, বরগুনা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Bibichini%20Shahi%20Mosque%2C%20Bibichini%2C%20Betagi%2C%20Barguna"
        },
        {
            "id": 2,
            "nameEn": "Taltali Buddhist Temple",
            "nameBn": "তালতলী প্রাচীন রাখাইন বৌদ্ধ মন্দির",
            "categoryEn": "Historic Rakhine Coastal Monastery & Relic Stupa",
            "categoryBn": "ঐতিহাসিক রাখাইন বৌদ্ধ বিহার ও প্রাচীন ভাস্কর্য",
            "descEn": "Taltali Buddhist Temple is a historic coastal monastery that anchors the cultural and spiritual legacy of the indigenous Rakhine community in southern Barguna. Established in the eighteenth century following the Rakhine migration from Arakan, the temple complex features traditional multi-tiered wooden pagodas, hand-carved dragon lintels, and ancient brass bells. The sanctum enshrines an exquisite centuries-old bronze Buddha statue weighing several tons, along with sacred Pali manuscripts and ceremonial drums. The tranquil temple precinct is shaded by flowering champak and banyan trees, providing a peaceful sanctuary for meditation and community gatherings. During the annual Sangrai Water Festival, the temple grounds become a vibrant center of colorful traditional dance and celebrations.",
            "descBn": "বরগুনার তালতলী উপজেলায় অবস্থিত এই প্রাচীন রাখাইন বৌদ্ধ মন্দিরটি উপকূলীয় রাখাইন জনগোষ্ঠীর ঐতিহ্য ও ধর্মীয় সংস্কৃতির এক উজ্জ্বল প্রতিচ্ছবি। অষ্টাদশ শতাব্দীতে আরাকান থেকে আগত রাখাইন সম্প্রদায়ের মানুষেরা এই সুরম্য মন্দিরটি প্রতিষ্ঠা করেন। মন্দিরের গর্ভগৃহে রয়েছে পিতল ও ব্রোঞ্জের তৈরি বিশালাকার অতি প্রাচীন বুদ্ধমূর্তি এবং কাঠে খোদাই করা বার্মিজ স্থাপত্যের সূক্ষ্ম কারুকাজ। সকাল-সন্ধ্যায় ঘণ্টার ধ্বনি ও শান্ত পরিবেশ মনকে পবিত্র প্রশান্তিতে ভরিয়ে তোলে। নববর্ষের 'সাংগ্রাই' উৎসবের সময় মন্দির প্রাঙ্গণ বর্ণাঢ্য সাংস্কৃতিক অনুষ্ঠান ও জলকেলিতে মুখরিত হয়ে ওঠে। উপকূলীয় নৃগোষ্ঠীর ইতিহাস জানতে এটি এক অনন্য স্থান।",
            "locationEn": "Taltali, Barguna",
            "locationBn": "তালতলী, বরগুনা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Taltali%20Buddhist%20Temple%2C%20Taltali%2C%20Barguna"
        },
        {
            "id": 3,
            "nameEn": "Old coastal settlement sites",
            "nameBn": "বরগুনার প্রাচীন উপকূলীয় জনপদ",
            "categoryEn": "Historic Maritime Pioneer Settlements",
            "categoryBn": "ঐতিহাসিক উপকূলীয় আবাদ ও প্রাচীন জনপদ",
            "descEn": "The old coastal settlement sites of Barguna represent the courageous pioneer communities who settled the volatile coastal islands and estuaries against tidal surges, storms, and Portuguese-Magh pirates. Centuries-old earthen embankments ('Bheri Badh'), ancient freshwater dighis, and weathered brick masonry foundations document early land reclamation efforts in the southern Sundarbans fringe. Local oral ballads celebrate legendary local chieftains and forest workers who cleared mangrove wilderness while establishing self-reliant agricultural cooperatives. Exploring these historic village hamlets offers visitors deep appreciation for the indomitable maritime resilience of the coastal Bengali people. It is an essential chapter in regional environmental and social history.",
            "descBn": "বরগুনার প্রাচীন উপকূলীয় জনপদগুলো বঙ্গোপসাগরের উত্তাল মোহনায় প্রতিকূল প্রকৃতির সাথে লড়াই করে গড়ে ওঠা মানব বসতির এক গৌরবময় ইতিহাস বহন করে। শত শত বছর ধরে পর্তুগিজ ও মগ জলদস্যুদের আক্রমণ এবং সামুদ্রিক জলোচ্ছ্বাসের বিরুদ্ধে লড়াই করে স্থানীয় মানুষ এখানে কৃষিকাজ ও নদী বাণিজ্যের সূচনা করেছিল। প্রাচীন মাটির কেল্লা, বিশালাকার মিষ্টি পানির প্রাচীন দীঘি এবং শতবর্ষী বসতির স্মৃতিচিহ্নগুলো উপকূলীয় মানুষের সাহসিকতার সাক্ষ্য দেয়। নদীমাতৃক ঐতিহ্য এবং উপকূলীয় জীবন সংগ্রামের গভীর রূপ উপলব্ধি করতে এই প্রাচীন জনপদগুলো অত্যন্ত শিক্ষণীয়।",
            "locationEn": "Barguna; verify named site locally",
            "locationBn": "বরগুনা উপকূলীয় অঞ্চল",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Old%20coastal%20settlement%20sites%2C%20Barguna%3B%20verify%20named%20site%20locally"
        },
        {
            "id": 4,
            "nameEn": "Patharghata historic river-port area",
            "nameBn": "পাথরঘাটা ঐতিহাসিক মৎস্য বন্দর ও নদীঘাট",
            "categoryEn": "Centennial Marine Fishing Port & Trading Haven",
            "categoryBn": "দেশের বৃহত্তম সামুদ্রিক মৎস্য অবতরণ কেন্দ্র ও বন্দর",
            "descEn": "Patharghata historic river-port area, nestled at the confluence of the Baleshwar and Bishkhali rivers near the Bay of Bengal, is one of the oldest and most important marine fishing ports in Bangladesh. For over a century, fleets of wooden sailing trawlers and steam launches converged here to land tons of silvery Hilsa, pomfret, and coastal sea catches. The historic harbor retains traditional boatyards where master carpenters construct massive seaworthy wooden trawlers without modern blueprints, using centuries-old nautical techniques. The lively fish auction markets, sun-drying fields (shutki palli), and maritime commerce provide a vibrant, sensory connection to the country's rich coastal economy. It stands as a vital living monument to marine heritage.",
            "descBn": "বলেশ্বর ও বিষখালী নদীর সঙ্গমস্থলে বঙ্গোপসাগরের তীরে অবস্থিত পাথরঘাটা বাংলাদেশের অন্যতম প্রাচীন ও বৃহত্তম সামুদ্রিক মৎস্য বন্দর। শতবর্ষ ধরে এটি উপকূলীয় অঞ্চলের ইলিশ ও সামুদ্রিক মাছের প্রধান বাণিজ্য কেন্দ্র হিসেবে পরিচিত। বন্দরের ঘাটে নোঙর করা শত শত কাঠের রঙিন ট্রলার এবং জেলেদের কর্মমুখর জীবনযাত্রা এক রোমাঞ্চকর দৃশ্যপট তৈরি করে। এখানকার ঐতিহ্যবাহী ডকইয়ার্ডগুলোতে কোনো আধুনিক নকশা ছাড়াই কারিগরদের নিপুণ হাতে বিশাল কাঠের সমুদ্রগামী ট্রলার তৈরির দৃশ্য দেখার মতো। দেশের সামুদ্রিক অর্থনীতি ও উপকূলীয় বাণিজ্যের প্রাণস্পন্দন অনুভব করতে পাথরঘাটা এক অপূর্ব বন্দর নগরী।",
            "locationEn": "Patharghata, Barguna",
            "locationBn": "পাথরঘাটা, বরগুনা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Patharghata%20historic%20river-port%20area%2C%20Patharghata%2C%20Barguna"
        },
        {
            "id": 5,
            "nameEn": "Liberation War memorial sites",
            "nameBn": "বরগুনা মুক্তিযুদ্ধ স্মৃতিসৌধ ও বধ্যভূমি",
            "categoryEn": "1971 Liberation War Historic Memorial",
            "categoryBn": "১৯৭১ সালের মহান মুক্তিযুদ্ধ স্মৃতিসৌধ ও গণকবর",
            "descEn": "The Liberation War memorial sites across Barguna town and district commemorate the profound sacrifices of local freedom fighters and citizens during the historic 1971 War of Independence. Key sites include the poignant memorial monument in Barguna town and the preserved mass killing grounds ('Baddhabhumi') where Pakistani occupation forces and collaborators perpetrated brutal massacres before the area was liberated by valiant Mukti Bahini guerrillas. The monuments feature striking architectural spires symbolizing the rising spirit of independence, inscribed with the names of local martyrs. Commemorative plaques and quiet memorial plazas host national remembrance ceremonies, educating younger generations on the heroic cost of sovereign freedom. It is a revered sanctuary of national honor.",
            "descBn": "বরগুনা জেলা শহর ও সন্নিহিত এলাকায় অবস্থিত মুক্তিযুদ্ধ স্মৃতিসৌধ ও বধ্যভূমিসমূহ ১৯৭১ সালের মহান মুক্তিযুদ্ধে আত্মোৎসর্গকারী বীর শহীদদের স্মৃতির উদ্দেশ্যে নির্মিত এক পরম শ্রদ্ধার স্থান। বরগুনা কারাগার সংলগ্ন বধ্যভূমিসহ বিভিন্ন স্থানে পাকিস্তানি হানাদার বাহিনী ও তাদের দোসররা নির্মম গণহত্যা চালিয়েছিল, যা পরে বীর মুক্তিযোদ্ধাদের প্রবল প্রতিরোধে মুক্ত হয়। শহরের প্রধান স্মৃতিসৌধটি আত্মত্যাগের রক্তিম ইতিহাস এবং বাঙালির বিজয়ের প্রতীক হিসেবে মাথা উঁচু করে দাঁড়িয়ে আছে। প্রতি বছর জাতীয় দিবসগুলোতে এখানে পুষ্পস্তবক অর্পণ ও শহীদদের স্মরণ করা হয়। এটি নতুন প্রজন্মের জন্য দেশপ্রেমের এক চিরন্তন প্রেরণা।",
            "locationEn": "Barguna town and district",
            "locationBn": "বরগুনা শহর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Liberation%20War%20memorial%20sites%2C%20Barguna%20town%20and%20district"
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Tengragiri Eco Park",
            "nameBn": "টেংরাগিরি ইকোপার্ক (ফাতরার বন)",
            "categoryEn": "Pristine Coastal Mangrove Forest & Safari",
            "categoryBn": "উপকূলীয় সংরক্ষিত দ্বিতীয় সুন্দরবন ও হরিণ অভয়ারণ্য",
            "descEn": "Tengragiri Eco Park, famously known as 'Fatrar Bon' or the 'Second Sundarbans', is a breathtaking 13,000-acre coastal mangrove forest reserve in Taltali Upazila bordering the Bay of Bengal. Intersected by winding tidal creeks and wooden footbridges, the dense forest is home to herds of wild spotted deer, wild boars, rhesus macaques, and diverse monitor lizards. A scenic wooden canopy walkway stretches deep into the mangrove jungle, leading visitors to a tranquil sandy beach overlooking the vast oceanic horizon. The park includes a wildlife breeding sanctuary, observation watchtowers, and eco-cottages where travelers can experience the untamed poetry of the mangrove wilderness. It is an extraordinary eco-tourism destination in southern Bangladesh.",
            "descBn": "তালতলী উপজেলায় বঙ্গোপসাগরের কোল ঘেঁষে অবস্থিত টেংরাগিরি ইকোপার্ক (ফাতরার বন) প্রায় ১৩ হাজার একর এলাকা জুড়ে বিস্তৃত বাংলাদেশের দ্বিতীয় বৃহত্তম ম্যানগ্রোভ অরণ্য। সুন্দরী, কেওড়া, গরান ও গোলপাতার নিবিড় এই বনে বাস করে শত শত চিত্রা হরিণ, বুনো শূকর, বানর এবং অসংখ্য প্রজাতির পাখি। বনের ভেতর দিয়ে চলে যাওয়া দীর্ঘ কাঠের তৈরি ফুটট্রেইল পর্যটকদের বনের গভীরে নিয়ে যায়, যার শেষ প্রান্তে দেখা মেলে সাগরের বিস্তৃত নির্জন বেলাভূমি। সুউচ্চ ওয়াচটাওয়ার থেকে সবুজের অপার সমুদ্র আর সাগরের ঢেউ এক সাথে অবলোকন করা যায়। প্রকৃতির আদিম রূপ ও বন্যপ্রাণী দেখার জন্য টেংরাগিরি এক রোমাঞ্চকর স্বর্গরাজ্য।",
            "locationEn": "Taltali, Barguna",
            "locationBn": "তালতলী, বরগুনা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Tengragiri%20Eco%20Park%2C%20Taltali%2C%20Barguna"
        },
        {
            "id": 2,
            "nameEn": "Bihanga Island",
            "nameBn": "বিহঙ্গ দ্বীপ (পাখির চর)",
            "categoryEn": "Pristine Offshore Bird Sanctuary Island",
            "categoryBn": "সাগর মোহনায় জেগে ওঠা নির্জন দ্বীপ ও পাখির স্বর্গ",
            "descEn": "Bihanga Island, locally celebrated as 'Pakhir Char' (Bird Island), is an enchanting offshore island resting in the wide estuary where the Baleshwar River merges into the Bay of Bengal. Accessible only by motorized boat from Patharghata, the uninhabited island is covered with lush mangrove saplings, golden sandbanks, and thousands of red fiddler crabs. As its name implies, the island serves as an essential roosting sanctuary for thousands of migratory and resident coastal birds, including sea eagles, kingfishers, and pelicans. Visitors can wander along pristine sandbars with only the sound of roaring ocean breakers and calling birds, enjoying absolute serenity far away from civilization. It is an untouched paradise for eco-adventurers.",
            "descBn": "পাথরঘাটার বলেশ্বর নদী ও বঙ্গোপসাগরের মোহনায় জেগে ওঠা বিহঙ্গ দ্বীপ (পাখির চর) প্রকৃতির এক অপূর্ব ও নির্জন সৃষ্টি। ইঞ্জিন বোটে নদীপথ পাড়ি দিয়ে পৌঁছানো এই দ্বীপে কোনো স্থায়ী মানববসতি নেই, যা এটিকে বুনো সৌন্দর্যের স্বর্গরাজ্যে পরিণত করেছে। শীতকালে এখানে হাজার হাজার দেশি ও পরিযায়ী পাখির মেলা বসে, যাদের কলকাকলিতে পুরো দ্বীপ মুখরিত থাকে। দ্বীপের শুভ্র বালুকাবেলায় হেঁটে বেড়ানো এবং লাল কাঁকড়ার অবাধ ছোটাছুটি দেখা এক চমৎকার অভিজ্ঞতা। সাগরের উত্তাল ঢেউ আর দিগন্তবিস্তৃত নীল আকাশের মাঝে সম্পূর্ণ নির্জনতায় সময় কাটাতে বিহঙ্গ দ্বীপ এক স্বপ্নিল গন্তব্য।",
            "locationEn": "Patharghata coast; boat access required",
            "locationBn": "পাথরঘাটা উপকূল, বরগুনা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Bihanga%20Island%2C%20Patharghata%20coast%3B%20boat%20access%20required"
        },
        {
            "id": 3,
            "nameEn": "Fatrar Char regional excursion",
            "nameBn": "ফাতরার চর আঞ্চলিক পর্যটন ও বনভ্রমণ",
            "categoryEn": "Coastal Mangrove Island Wilderness & Beach",
            "categoryBn": "উপকূলীয় চরাঞ্চল, শ্বাসমূলের বন ও নৌবিহার",
            "descEn": "The Fatrar Char regional excursion offers travelers an unforgettable boat journey through the pristine coastal mangrove islands that fringe the border between Barguna and Patuakhali. Formed by the rich alluvial silt of southern river deltas, the island features dense stands of mangrove vegetation, tidal mudflats, and hidden sandy lagoons. Travelers hire local wooden trawlers to weave through labyrinthine saltwater canals where monkeys leap through the canopy and mudskippers scurry along the banks. At the southern edge, the forest opens onto sweeping ocean horizons where waves crash against fallen driftwood trees. It provides a thrilling, authentic glimpse into the dynamic coastal frontier of the Bengal delta.",
            "descBn": "বরগুনা ও পটুয়াখালী উপকূলীয় সীমানায় অবস্থিত ফাতরার চরের জলপথ ভ্রমণ দক্ষিণ বাংলার সবচেয়ে আকর্ষণীয় ম্যানগ্রোভ অ্যাডভেঞ্চারগুলোর অন্যতম। সুবিশাল ট্রলারে চড়ে শ্বাসমূলের বনের ভেতর দিয়ে এঁকেবেঁকে চলা নদী ও খাঁড়িপথ পাড়ি দেওয়া এক পরাবাস্তব রোমাঞ্চকর অনুভূতি দেয়। বনের ভেতর চিত্রা হরিণের বিচরণ, বানরের দল এবং নদীর পাড়ে কাদায় ঘুরে বেড়ানো কাদার মাছ (মাডস্কিপার) চোখ জুড়িয়ে দেয়। চরের দক্ষিণ প্রান্তে সাগরের বিশাল সৈকত রয়েছে, যেখানে প্রকৃতির নিঃশব্দ রূপ অনুভূত হয়। ম্যানগ্রোভ অরণ্য আর বঙ্গোপসাগরের মিলনস্থলে একদিন কাটানোর জন্য ফাতরার চর এক চমৎকার ভ্রমণস্থল।",
            "locationEn": "Mostly Patuakhali coastal region; verify route",
            "locationBn": "উপকূলীয় ফাতরার চর",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Fatrar%20Char%20regional%20excursion%2C%20Mostly%20Patuakhali%20coastal%20region%3B%20verify%20route"
        },
        {
            "id": 4,
            "nameEn": "Payra-Baleshwar estuary views",
            "nameBn": "পায়রা-বলেশ্বর মোহনার সূর্যাস্ত ভিউ",
            "categoryEn": "Panoramic River-Sea Confluence & Overlook",
            "categoryBn": "বিশাল নদী মোহনা, সাগরের জলরাশি ও সূর্যাস্ত",
            "descEn": "The Payra-Baleshwar estuary viewpoints in Patharghata and Barguna Sadar offer jaw-dropping panoramas where the immense Payra, Bishkhali, and Baleshwar rivers converge before meeting the Bay of Bengal. The water surface stretches so wide that the opposite shore disappears from view, creating the sensation of standing on the edge of an infinite sea. Concrete flood embankments and shoreline piers provide breezy, elevated vantage points where travelers can watch hundreds of colorful fishing trawlers navigate the choppy waves. Twilight at the estuary is legendary, with the setting sun creating a blazing path of gold and crimson across the water. It is an inspiring sanctuary celebrating the untamed riverine grandeur of southern Bangladesh.",
            "descBn": "পাথরঘাটার কোল ঘেঁষে পায়রা, বিষখালী ও বলেশ্বর নদীর মোহনায় বঙ্গোপসাগরের সাথে মিলনের দৃশ্য এক অভাবনীয় প্রাকৃতিক বিস্ময়। এখানে নদীগুলো এতই প্রশস্ত যে ওপারের কোনো কূল দেখা যায় না, মনে হয় যেন সাগরের অনন্ত জলধির সামনে দাঁড়িয়ে আছি। বাঁধের ওপর দাঁড়িয়ে সমুদ্রের মাতাল হাওয়া উপভোগ করা এবং দূর সাগরে মাছ ধরতে যাওয়া শত শত জেলে নৌকার দৃশ্য দেখার মতো সুন্দর। বিকেলে যখন নদীর বুকে সূর্য অস্ত যায়, তখন আকাশ আর পানির রঙ রক্তিম আভায় রঙিন হয়ে ওঠে। নদী ও সাগরের এই মেলবন্ধনের রূপ পর্যটকদের আত্মাকে এক অপার্থিব প্রশান্তিতে ভরিয়ে তোলে।",
            "locationEn": "Patharghata, Barguna",
            "locationBn": "পাথরঘাটা, বরগুনা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Payra-Baleshwar%20estuary%20views%2C%20Patharghata%2C%20Barguna"
        },
        {
            "id": 5,
            "nameEn": "Haringhata forest area",
            "nameBn": "হরিণঘাটা সংরক্ষিত বন ও ইকো পার্ক",
            "categoryEn": "Spotted Deer Sanctuary & Coastal Footbridge",
            "categoryBn": "চিত্রা হরিণের অভয়ারণ্য, ঝুলন্ত সেতু ও সৈকত",
            "descEn": "The Haringhata forest area in Patharghata is an enchanting coastal eco-sanctuary renowned as one of the best places in Bangladesh to observe wild spotted deer grazing in their natural habitat. Positioned where the Baleshwar River meets the sea, this dense forest features an impressive kilometer-long raised wooden footbridge that meanders gracefully above tidal forest floors and breathing mangrove roots. Visitors walking along the canopy walkway frequently encounter deer herds, playful monkeys, wild boars, and exotic kingfishers. The trail culminates at a peaceful, untouched sea beach lined with golden sands and casuarina groves. It provides an exceptional, world-class wilderness immersion for nature enthusiasts and photographers.",
            "descBn": "পাথরঘাটা উপজেলার সর্বদক্ষিণে অবস্থিত হরিণঘাটা বন বরগুনা জেলার সবচেয়ে আকর্ষণীয় ও অনন্য ইকো-ট্যুরিজম কেন্দ্র। বলেশ্বর নদীর তীরে গড়ে ওঠা এই নিবিড় প্রাকৃতিক বনটি চিত্রা হরিণের নিরাপদ অভয়ারণ্য হিসেবে বিখ্যাত। বনের ভেতর দিয়ে প্রায় এক কিলোমিটার দীর্ঘ কাঠের চমৎকার ফুটট্রেইল তৈরি করা হয়েছে, যার ওপর দিয়ে হাঁটতে হাঁটতে পর্যটকরা বনের হরিণ ও বানরের অবাধ বিচরণ খুব কাছ থেকে দেখতে পান। কাঠের ব্রিজের শেষ মাথায় রয়েছে ঝাউবন পরিবেষ্টিত এক চমৎকার নিরিবিলি সমুদ্র সৈকত। বুনো প্রকৃতির ছোঁয়া ও হরিণের সান্নিধ্য পেতে হরিণঘাটা এক পরম রোমাঞ্চকর ভ্রমণ গন্তব্য।",
            "locationEn": "Patharghata, Barguna",
            "locationBn": "পাথরঘাটা, বরগুনা",
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Haringhata%20forest%20area%2C%20Patharghata%2C%20Barguna"
        }
    ]
}

data_dict = {
    "rangamati": rangamati,
    "chapainawabganj": chapainawabganj,
    "bandarban": bandarban,
    "barguna": barguna
}

for slug, data in data_dict.items():
    fp = f"scripts/data_districts_17/{slug}.py"
    with open(fp, "w", encoding="utf-8") as f:
        f.write(f"# -*- coding: utf-8 -*-\nDISTRICT_DATA = {json.dumps(data, ensure_ascii=False, indent=4)}\n")
    print(f"Wrote {fp}")

print("Batch 10 to 13 complete!")
