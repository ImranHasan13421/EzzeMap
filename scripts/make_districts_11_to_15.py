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
# 11. BAGERHAT
# ==========================================
b_raw = all_data['bagerhat']
bagerhat_data = {
    "slug": "bagerhat",
    "en": "Bagerhat",
    "bn": "বাগেরহাট",
    "hero_title_en": "Bagerhat UNESCO Mosque City & Gateway to Sundarbans",
    "hero_title_bn": "বাগেরহাটের ইউনেস্কো বিশ্ব ঐতিহ্য মসজিদ শহর ও সুন্দরবনের দুয়ার",
    "hero_sub_en": "Fifteenth-century Sixty Dome Mosque, sacred tomb of Khan Jahan Ali, and wildlife gateways to the mangrove forest.",
    "hero_sub_bn": "পঞ্চদশ শতাব্দীর বিশ্বখ্যাত ষাট গম্বুজ মসজিদ, হযরত খান জাহান আলীর মাজার ও সুন্দরবনের ম্যানগ্রোভ অরণ্যের প্রবেশদ্বার।",
    "tagline_en": "The historic medieval city of Khalifatabad founded by saint-warrior Khan Jahan Ali, world-renowned for UNESCO World Heritage terracotta mosques and the marine gateway to the Sundarbans.",
    "tagline_bn": "সুফি সাধক ও বীর যোদ্ধা হযরত খান জাহান আলী প্রতিষ্ঠিত ঐতিহাসিক খলিফাতাবাদ, যা ইউনেস্কো স্বীকৃত ষাট গম্বুজ মসজিদ, নয় গম্বুজ মসজিদ ও মোংলা সমুদ্র বন্দরের জন্য আন্তর্জাতিক খ্যাতিসম্পন্ন।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/bagerhat/carousel-1.webp",
            "titleEn": "Sixty Dome Mosque UNESCO World Heritage Monument",
            "titleBn": "ষাট গম্বুজ মসজিদ ইউনেস্কো বিশ্ব ঐতিহ্য",
            "subtitleEn": "15th-century architectural masterpiece featuring seventy-seven brick domes and terracotta arched halls",
            "subtitleBn": "পঞ্চদশ শতাব্দীর মাঝামাঝি নির্মিত ৭৭টি গম্বুজযুক্ত বাংলার সর্ববৃহৎ সুলতানি আমলের স্থাপত্য বিস্ময়"
        },
        {
            "id": 2,
            "image": "images/districts/bagerhat/carousel-2.webp",
            "titleEn": "Khan Jahan Ali Shrine & Sacred Dighi",
            "titleBn": "হযরত খান জাহান (রহ.) মাজার ও পুণ্যময় দীঘি",
            "subtitleEn": "Sacred mausoleum complex in Bagerhat overlooking the ancient freshwater lake home to legendary marsh crocodiles",
            "subtitleBn": "ঐতিহাসিক খাঁনজহালী দীঘির পাড়ে অবস্থিত সুফি সাধকের পুণ্য সমাধি সৌধ ও শান্তিময় প্রাঙ্গণ"
        },
        {
            "id": 3,
            "image": "images/districts/bagerhat/carousel-3.webp",
            "titleEn": "Nine Dome Mosque Intricate Terracotta",
            "titleBn": "নয় গম্বুজ মসজিদের অপূর্ব পোড়ামাটির কারুকাজ",
            "subtitleEn": "Graceful nine-domed brick sanctuary resting on slender stone pillars near Thakur Dighi",
            "subtitleBn": "ঠাকুর দীঘির পশ্চিমে অবস্থিত অপরূপ নয়টি গম্বুজ বিশিষ্ট মধ্যযুগীয় বাংলার সুলতানি স্থাপত্য"
        },
        {
            "id": 4,
            "image": "images/districts/bagerhat/carousel-4.webp",
            "titleEn": "Sundarbans Gateway at Mongla Mangrove Riverfront",
            "titleBn": "মোংলায় সুন্দরবনের প্রবেশদ্বার ও পশুর নদী",
            "subtitleEn": "Vibrant maritime river port where launches embark on deep eco-tours into the world's largest mangrove forest",
            "subtitleBn": "পশুর নদীর মোহনায় অবস্থিত দেশের দ্বিতীয় বৃহত্তম সমুদ্র বন্দর ও সুন্দরবনের প্রধান পর্যটন প্রবেশদ্বার"
        },
        {
            "id": 5,
            "image": "images/districts/bagerhat/carousel-5.webp",
            "titleEn": "Dublar Char Coastal Island Wilderness",
            "titleBn": "দুবলার চরের দিগন্তবিস্তৃত সমুদ্র নিসর্গ",
            "subtitleEn": "Remote offshore island in the Bay of Bengal celebrated for traditional seasonal fisheries and Raas Mela",
            "subtitleBn": "সুন্দরবনের দক্ষিণে বঙ্গোপসাগরের বুকে জেগে ওঠা ঐতিহ্যবাহী শুঁটকি পল্লী ও বিখ্যাত রাস মেলার দ্বীপ"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Sixty Dome Mosque",
            "nameBn": "ষাট গম্বুজ মসজিদ",
            "categoryEn": "UNESCO World Heritage Site",
            "categoryBn": "ইউনেস্কো বিশ্ব ঐতিহ্যবাহী মসজিদ",
            "descEn": "Constructed in the mid-fifteenth century by the saint-ruler Khan Jahan Ali, the Sixty Dome Mosque (Shat Gombuj Masjid) is the largest and most architecturally awe-inspiring Sultanate-era monument in Bangladesh. Despite its traditional popular name, the colossal brick sanctuary actually boasts seventy-seven low-profile hemispherical domes supported by sixty faceted stone columns imported from afar, alongside four corner circular towers that double as minarets. Its immense exterior walls are constructed from tapered burnt terracotta brickwork, reflecting an extraordinary synthesis of indigenous Bengali curves and imperial Tughlaq fortress architecture. The interior prayer hall resembles a forest of stone pillars, illuminated by soft sunlight filtering through arched brick doorways onto finely carved terracotta mihrabs. Inscribed on the UNESCO World Heritage list in 1985, it stands as an enduring symbol of medieval engineering brilliance and Islamic civilization.",
            "descBn": "পঞ্চদশ শতাব্দীর মধ্যভাগে সুফি সাধক ও খলিফাতাবাদের প্রতিষ্ঠাতা হযরত খান জাহান আলী কর্তৃক নির্মিত ষাট গম্বুজ মসজিদ বাংলাদেশের সর্ববৃহৎ ও সর্বশ্রেষ্ঠ সুলতানি স্থাপত্য কীর্তি। মুখে 'ষাট গম্বুজ' বলা হলেও সুবিশাল এই মসজিদটিতে মূলত মোট ৭৭টি নান্দনিক গম্বুজ এবং ৬০টি সুদৃঢ় পাথরের স্তম্ভ রয়েছে যা মসজিদের সুবিশাল ছাদকে ধরে রেখেছে। এর চার কোণে থাকা চারটি সুরক্ষিত মিনার এবং পুরু ইটের দেওয়াল তুঘলক ও স্থানীয় বাংলা স্থাপত্যরীতির অপূর্ব মিশ্রণ প্রকাশ করে। মসজিদের অভ্যন্তরে পাথরের স্তম্ভের সারি ও পোড়ামাটির কারুকার্যময় মেহরাবগুলো এক অদ্ভুত আধ্যাত্মিক আবহ সৃষ্টি করে। ১৯৮৫ সালে ইউনেস্কো কর্তৃক বিশ্ব ঐতিহ্যবাহী স্থান হিসেবে ঘোষিত এই মসজিদটি মধ্যযুগীয় বাংলার প্রকৌশলবিদ্যার এক অনন্য বিস্ময়।",
            "locationEn": b_raw['hist_spots'][0]['location'],
            "locationBn": "খান জাহান আলী এলাকা, বাগেরহাট",
            "mapUrl": b_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Khan Jahan Ali's Tomb",
            "nameBn": "হযরত খান জাহান আলী (রহ.) এর মাজার",
            "categoryEn": "Sacred Medieval Mausoleum Complex",
            "categoryBn": "পবিত্র ঐতিহাসিক মাজার ও সুফি দরগাহ",
            "descEn": "Khan Jahan Ali's Tomb is the venerated resting place of the legendary fifteenth-century warrior-saint who cleared the Sundarbans wilderness to establish the flourishing medieval city of Khalifatabad. Perched atop an elevated terrace overlooking the expansive freshwater Khanjali Dighi, the single-domed square mausoleum features thick tapered brick walls, corner turrets, and elegant stone crypt inscriptions documenting his demise in October 1459 AD. Devotees of all backgrounds visit daily to pay respects, offer sweetmeats, and recite verses in remembrance of his benevolent governance. The adjacent ancient lake is famously inhabited by friendly freshwater marsh crocodiles (locally known as 'Kala Pahar' and 'Dhaola Pahar') that glide gracefully to the ghat steps when called by shrine attendants. The serene, sacred complex remains the spiritual and cultural heart of Bagerhat.",
            "descBn": "হযরত খান জাহান আলী (রহ.)-এর মাজার বাগেরহাটের এক পরম পুণ্যময় আধ্যাত্মিক কেন্দ্র, যেখানে চিরনিদ্রায় শায়িত আছেন সুন্দরবন আবাদ করে মধ্যযুগীয় খলিফাতাবাদ নগরী প্রতিষ্ঠাকারী এই মহান সুফি সাধক। সুবিশাল খাঁনজহালী দীঘির উত্তর পাড়ে উঁচু টিলার ওপর নির্মিত এক গম্বুজ বিশিষ্ট এই সমাধি সৌধটির স্থাপত্য অত্যন্ত সুদৃঢ় ও গাম্ভীর্যপূর্ণ। সৌধের ভেতরে থাকা পাথরের লিপিতে ১৪৫৯ খ্রিস্টাব্দে এই মহান সাধকের ওফাত দিবস লিপিবদ্ধ রয়েছে। মাজার সংলগ্ন প্রাচীন দীঘিতে বাস করে ঐতিহাসিক মিষ্টি পানির কুমির, যাদের দেখতে পর্যটকরা ভিড় জমান। ধর্ম-বর্ণ নির্বিশেষে প্রতিদিন হাজার হাজার মানুষ এখানে জিয়ারত ও মানত করতে আসেন। ভক্তি, ইতিহাস ও প্রশান্তির এক চিরন্তন মিলনমেলা এই পবিত্র মাজার প্রাঙ্গণ।",
            "locationEn": b_raw['hist_spots'][1]['location'],
            "locationBn": "খান জাহান আলী এলাকা, বাগেরহাট",
            "mapUrl": b_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Singair Mosque",
            "nameBn": "সিঙ্গাইর মসজিদ",
            "categoryEn": "Sultanate Single-Dome Brick Mosque",
            "categoryBn": "সুলতানি আমলের এক গম্বুজ মসজিদ",
            "descEn": "Located southeast of the Sixty Dome Mosque complex across the historic road, Singair Mosque is a classic fifteenth-century single-domed sanctuary exemplary of Khan Jahani architectural design. Constructed with deep red terracotta bricks and lime mortar, the square building is crowned by a monumental hemispherical dome and corner circular bastions that taper gently toward the roofline. The facade displays graceful curved cornices mimicking traditional Bengali thatched bamboo eaves, decorated with subtle terracotta bands and recessed archways. Inside, a beautifully proportioned stone and terracotta mihrab directs prayers in an intimate, tranquil acoustic environment. Standing amid rural date-palm groves and village water bodies, Singair Mosque is treasured by heritage travelers for its balanced proportions and pristine historic authenticity.",
            "descBn": "ষাট গম্বুজ মসজিদের দক্ষিণ-পূর্বে অবস্থিত সিঙ্গাইর মসজিদটি পঞ্চদশ শতাব্দীর খান জাহানী স্থাপত্যরীতির এক নিখুঁত ও দৃষ্টিনন্দন এক গম্বুজ বিশিষ্ট মসজিদ। লাল পোড়ামাটির ইট ও চুন-সুরকিতে নির্মিত এই বর্গাকার মসজিদের ছাদে রয়েছে একটি সুবিশাল গোলাকার গম্বুজ এবং চার কোণে চারটি বৃত্তাকার মিনার। মসজিদের বহির্দেয়ালে বাংলার ঐতিহ্যবাহী বাঁকানো কার্নিশ ও পোড়ামাটির লতাপাতার কারুকাজ অত্যন্ত চমৎকারভাবে ফুটে উঠেছে। ভেতরে পাথরের সূক্ষ্ম মেহরাব ও শান্ত পরিবেশ মুসল্লিদের মনে গভীর প্রশান্তি এনে দেয়। সুপারি বাগান ও গ্রামীণ সবুজের মাঝে একাকী দাঁড়িয়ে থাকা এই প্রাচীন উপাসনালয়টি মধ্যযুগীয় বাংলার স্থাপত্য সৌন্দর্যের এক উজ্জ্বল উদাহরণ।",
            "locationEn": b_raw['hist_spots'][2]['location'],
            "locationBn": "বাগেরহাট শহর এলাকা, বাগেরহাট",
            "mapUrl": b_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Nine Dome Mosque",
            "nameBn": "নয় গম্বুজ মসজিদ",
            "categoryEn": "Multi-Domed Sultanate Heritage Monument",
            "categoryBn": "সুলতানি আমলের নয় গম্বুজ মসজিদ",
            "descEn": "Situated on the western bank of the historic Thakur Dighi, the Nine Dome Mosque is one of the most aesthetically refined multi-domed structures in the Bagerhat UNESCO archaeological zone. Dating to the mid-fifteenth century, the square brick sanctuary is crowned by nine perfectly proportioned hemispherical domes arranged symmetrically in three rows of three, supported internally by slender stone columns. The exterior brickwork features ornate curved cornices, three arched doorways on three sides, and terracotta floral medallions that catch the warm afternoon light. The central western mihrab is deeply carved with delicate terracotta chain-and-bell motifs and floral rosettes. The peaceful breeze blowing off the adjacent lake makes visiting this serene medieval monument an unforgettable spiritual and architectural experience.",
            "descBn": "ঐতিহাসিক ঠাকুর দীঘির পশ্চিম পাড়ে অবস্থিত নয় গম্বুজ মসজিদ বাগেরহাটের ইউনেস্কো ঘোষিত মসজিদ নগরীর অন্যতম সুষম ও নান্দনিক স্থাপত্য নিদর্শন। পঞ্চদশ শতাব্দীর মধ্যভাগে নির্মিত এই বর্গাকার মসজিদে সুবিন্যস্তভাবে তিন সারিতে তিনটি করে মোট নয়টি সুদৃশ্য গম্বুজ রয়েছে, যা ভেতরে পাথরের স্তম্ভের ওপর স্থাপিত। মসজিদের দেওয়ালে থাকা বাঁকানো কার্নিশ, খিলানযুক্ত প্রবেশপথ এবং পোড়ামাটির ঝুলন্ত শিকল ও পদ্মফুলের মোটিফ তৎকালীন শিল্পীদের অনন্য দক্ষতার সাক্ষ্য দেয়। সংলগ্ন দীঘির জলরাশি থেকে ভেসে আসা শীতল হাওয়া এবং নির্জন ঐতিহাসিক পরিবেশ দর্শনার্থীদের মুগ্ধ করে। মধ্যযুগীয় বাংলার ইসলামী স্থাপত্যকলার এক অনন্য মাস্টারপিস এই নয় গম্বুজ মসজিদ।",
            "locationEn": b_raw['hist_spots'][3]['location'],
            "locationBn": "বাগেরহাট শহর এলাকা, বাগেরহাট",
            "mapUrl": b_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Bibi Begni Mosque",
            "nameBn": "বিবি বেগনী মসজিদ",
            "categoryEn": "Monumental Single-Dome Heritage Mosque",
            "categoryBn": "ঐতিহাসিক বিশালাকার এক গম্বুজ মসজিদ",
            "descEn": "Bibi Begni Mosque, traditionally believed to have been erected in memory of a pious noblewoman or companion of Khan Jahan Ali, is an imposing fifteenth-century single-domed monument situated in the historic core of Bagerhat. Constructed with exceptionally thick brick masonry reaching up to three meters in width, the massive square structure supports an expansive hemispherical dome that dominates the local landscape. The exterior displays characteristic curved eaves, round corner towers, and recessed arched doorways framed in delicate terracotta brick friezes. Its interior prayer chamber exhibits cool, silent acoustics anchored by a grand multi-tiered terracotta mihrab. Carefully conserved within green landscaped grounds, Bibi Begni Mosque offers visitors a profound encounter with the monumental durability of Sultanate engineering.",
            "descBn": "ঐতিহাসিক খলিফাতাবাদের অন্যতম গুরুত্বপূর্ণ প্রাচীন নিদর্শন বিবি বেগনী মসজিদ, যা ঐতিহ্য অনুসারে হযরত খান জাহান আলীর পরিবারের কোনো মহীয়সী নারীর স্মরণে পঞ্চদশ শতাব্দীতে নির্মিত হয়েছিল। প্রায় তিন মিটার পুরু ইটের দেওয়ালের ওপর নির্মিত এই বিশাল এক গম্বুজ বিশিষ্ট মসজিদটি তৎকালীন সুদৃঢ় নির্মাণরীতির এক চমৎকার প্রমাণ। এর চার কোণে গোলাকার মজবুত মিনার, বাঁকানো কার্নিশ এবং পোড়ামাটির কারুকার্যময় খিলানযুক্ত প্রবেশপথ রয়েছে। মসজিদের ভেতরের সুউচ্চ মেহরাব ও নিস্তব্ধ পরিবেশ দর্শনার্থীদের গভীর ভাবগাম্ভীর্যে আচ্ছন্ন করে। সবুজ লন দিয়ে ঘেরা সুন্দর পরিবেশে সংরক্ষিত এই প্রাচীন স্মৃতিস্তম্ভটি বাগেরহাটের অন্যতম মূল্যবান প্রত্নতাত্ত্বিক সম্পদ।",
            "locationEn": b_raw['hist_spots'][4]['location'],
            "locationBn": "বাগেরহাট ঐতিহাসিক মসজিদ এলাকা, বাগেরহাট",
            "mapUrl": b_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Sundarbans Gateway at Mongla",
            "nameBn": "মোংলায় সুন্দরবনের প্রবেশদ্বার",
            "categoryEn": "World Heritage Mangrove Gateway & Marine Port",
            "categoryBn": "সুন্দরবনের আন্তর্জাতিক প্রবেশদ্বার ও সমুদ্র বন্দর",
            "descEn": "Mongla is the premier terrestrial and nautical gateway to the Sundarbans, the world's largest contiguous tidal mangrove forest and a UNESCO World Heritage site. Situated at the confluence of the Pasur and Mongla rivers, the port town is the launching ground where modern eco-cruisers, traditional wooden launches, and motorboats depart on deep expeditions into the mangrove channels. Visitors embarking from Mongla cruise past sprawling mangrove forests where the elusive Royal Bengal Tiger, spotted deer, estuarine crocodiles, and playful Irrawaddy dolphins roam free. Waterfront observation points allow travelers to watch international cargo ships maneuvering in the tidal river while breathing in crisp salty ocean air. It is the indispensable starting point for any authentic exploration of Bangladesh's wild mangrove frontier.",
            "descBn": "মোংলা হলো ইউনেস্কো বিশ্ব ঐতিহ্যবাহী ম্যানগ্রোভ বন সুন্দরবনের প্রধান ও সবচেয়ে গুরুত্বপূর্ণ প্রবেশদ্বার। পশুর ও মোংলা নদীর সঙ্গমস্থলে অবস্থিত এই বন্দর শহর থেকেই আধুনিক পর্যটকবাহী জাহাজ, কাঠের লঞ্চ ও ট্রলার সুন্দরবনের গভীর অরণ্যের উদ্দেশ্যে যাত্রা করে। মোংলা থেকে নদীপথে যাত্রা শুরু করলেই চোখের সামনে ভেসে ওঠে শ্বাসমূলযুক্ত কেওড়া ও সুন্দরী গাছের সবুজ বনানী, যেখানে মুক্তভাবে বিচরণ করে রয়েল বেঙ্গল টাইগার, চিত্রা হরিণ, নোনা পানির কুমির ও ডলফিন। পশুর নদীর পাড়ে দাঁড়িয়ে বিশাল বিশাল আন্তর্জাতিক বাণিজ্যিক জাহাজের নোঙর করার দৃশ্য অত্যন্ত চমৎকার দেখায়। রোমাঞ্চকর সুন্দরবন অভিযানের জন্য মোংলা এক অপরিহার্য ও প্রাণবন্ত পর্যটন কেন্দ্র।",
            "locationEn": b_raw['tour_spots'][0]['location'],
            "locationBn": "মোংলা, বাগেরহাট",
            "mapUrl": b_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Mongla Port Riverfront",
            "nameBn": "মোংলা বন্দর নদীতীর",
            "categoryEn": "Scenic Maritime Riverfront Promenade",
            "categoryBn": "সমুদ্র বন্দর নদীতীর ও সূর্যাস্ত ভিউপয়েন্ট",
            "descEn": "The Mongla Port Riverfront along the wide banks of the Pasur River offers an exhilarating maritime panorama where industrial shipping activity harmonizes with coastal deltaic nature. The riverfront promenade provides sweeping views of massive international container carriers, tugboats, and naval vessels anchored in the deep river channel against backdrop sunsets. Local water taxis and wooden dinghies ferry passengers across the turbulent waters, offering affordable and scenic mini-cruises past port installations and mangrove banks. Waterfront seafood stalls serve freshly prepared mud crab, tiger prawns, and coastal fish dishes caught directly from the surrounding estuaries. It is a vibrant, breezy destination that captures the dynamic marine spirit of southern Bangladesh.",
            "descBn": "পশুর নদীর সুবিশাল তীরে অবস্থিত মোংলা বন্দর নদীতীর এমন একটি স্থান যেখানে আধুনিক সমুদ্রবাণিজ্যের বিশালতা ও নদীপ্রকৃতির সৌন্দর্য একাকার হয়ে গেছে। নদীতীরের বেড়িবাঁধ ও ঘাট থেকে নদীতে নোঙর করে থাকা আন্তর্জাতিক পণ্যবাহী জাহাজ, টাগবোট ও ফেরির দৃশ্য অত্যন্ত রোমাঞ্চকর। ছোট ছোট কাঠের নৌকায় চড়ে নদীর বুক চিরে ওপারে যাওয়া কিংবা সূর্যাস্তের আলোয় নদীর ঢেউয়ের খেলা দেখা পর্যটকদের দারুণ আনন্দ দেয়। নদীর পাড়ের হোটেলগুলোতে পাওয়া যায় সুন্দরবনের তাজা গলদা চিংড়ি, কাঁকড়া ও সামুদ্রিক মাছের জিভে জল আনা পদ। খোলা বাতাস আর সমুদ্র বন্দরের কর্মচাঞ্চল্য উপভোগে মোংলা নদীতীর এক দারুণ গন্তব্য।",
            "locationEn": b_raw['tour_spots'][1]['location'],
            "locationBn": "মোংলা, বাগেরহাট",
            "mapUrl": b_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Dublar Char",
            "nameBn": "দুবলার চর",
            "categoryEn": "Offshore Coastal Island & Historic Raas Mela",
            "categoryBn": "উপকূলীয় দ্বীপ, শুঁটকি পল্লী ও বিখ্যাত রাস মেলা",
            "descEn": "Dublar Char is a remote, breathtaking coastal island emerging in the southern Sundarbans right where the mangrove delta opens out into the boundless waters of the Bay of Bengal. Famous across the subcontinent as a temporary seasonal home for thousands of traditional fishermen who arrive in winter to catch and sun-dry millions of marine fish on bamboo racks, the island buzzes with authentic coastal culture. In autumn, the island hosts the historic three-day Dublar Char Raas Mela festival, where tens of thousands of Hindu pilgrims and ecotourists congregate to take ritual dips in the sea under the glowing full moon. Wild spotted deer regularly graze along the sandy dunes alongside fishermen's thatched huts. Visiting Dublar Char by guided sea trawler offers an untamed, once-in-a-lifetime adventure into Bangladesh's oceanic wilderness.",
            "descBn": "সুন্দরবনের একেবারে দক্ষিণাংশে বঙ্গোপসাগরের কোল ঘেঁষে অবস্থিত দুবলার চর এক রোমাঞ্চকর ও বৈচিত্র্যময় উপকূলীয় দ্বীপ। প্রতি বছর শীত মৌসুমে দেশের বিভিন্ন প্রান্ত থেকে হাজার হাজার জেলে এই দ্বীপে অস্থায়ী বসতি গড়ে তোলেন এবং ঐতিহ্যবাহী মাচায় সামুদ্রিক শুঁটকি শুকানোর বিশাল কর্মযজ্ঞ পরিচালনা করেন। কার্তিক পূর্ণিমায় এই দ্বীপে অনুষ্ঠিত হয় ঐতিহাসিক ও বিশ্বখ্যাত 'দুবলার চরের রাসমেলা', যেখানে পূর্ণিমার রাতে পুণ্যস্নান করতে লাখ লাখ ভক্ত ও পর্যটক সমবেত হন। চরের বালিয়াড়িতে জেলেদের কুঁড়েঘরের পাশেই নির্ভয়ে ঘুরে বেড়ায় বুনো চিত্রা হরিণের দল। গভীর সাগরের বুকে এই দ্বীপের জীবন ও অপরূপ প্রকৃতি প্রত্যক্ষ করা এক অবিস্মরণীয় অভিজ্ঞতা।",
            "locationEn": b_raw['tour_spots'][2]['location'],
            "locationBn": "সুন্দরবন, বাগেরহাট উপকূলীয় অঞ্চল",
            "mapUrl": b_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Hiron Point (Nilkamal)",
            "nameBn": "হিরণ পয়েন্ট (নীলকমল)",
            "categoryEn": "Deep Sundarbans Wildlife Sanctuary & Ecotourism Hub",
            "categoryBn": "সুন্দরবনের গভীর অরণ্য ও বন্যপ্রাণী অভয়ারণ্য",
            "descEn": "Hiron Point, officially designated as the Nilkamal Wildlife Sanctuary, is one of the deepest and most prestigious ecotourism landmarks within the southern Sundarbans mangrove forest. Situated along the banks of the Nilkamal River near the Bay of Bengal, the sanctuary is renowned as a primary habitat for Royal Bengal Tigers, saltwater crocodiles, monitor lizards, and vast herds of spotted deer. A network of raised wooden boardwalks allows guided visitors to walk deep into the dense mangrove forest safely, listening to the mysterious sounds of the wild canopy above. The high forest watchtower provides spectacular panoramic perspectives over endless miles of green tidal mangroves meeting the distant blue sea. It is the ultimate dream destination for hardcore wildlife photographers and adventurers.",
            "descBn": "সুন্দরবনের দক্ষিণ প্রান্তে নীলকমল নদীর তীরে অবস্থিত হিরণ পয়েন্ট বন্যপ্রাণীদের নিরাপদ আবাসস্থল হিসেবে আন্তর্জাতিকভাবে পরিচিত এক বিখ্যাত অভয়ারণ্য। গভীর অরণ্যের এই অংশে রাজকীয় রয়েল বেঙ্গল টাইগার, চিত্রা হরিণ, নোনা পানির কুমির, বানর ও নানা প্রজাতির বুনো পাখির অবাধ বিচরণ সবচেয়ে বেশি দেখা যায়। পর্যটকদের বনের ভেতরে নিরাপদে ঘুরে দেখার জন্য এখানে তৈরি করা হয়েছে চমৎকার কাঠের ওয়াকওয়ে বা ট্রেইল। বন বিভাগের সুউচ্চ ওয়াচ টাওয়ারে উঠলে চারপাশের সুবিশাল ম্যানগ্রোভ অরণ্য ও দূরবর্তী নীল সাগরের মিলনমেলা এক পলকে অবলোকন করা যায়। বন্যপ্রাণী দেখার রোমাঞ্চ ও সুন্দরবনের আসল নিস্তব্ধতা উপভোগে হিরণ পয়েন্ট এক অতুলনীয় তীর্থস্থান।",
            "locationEn": b_raw['tour_spots'][3]['location'],
            "locationBn": "সুন্দরবন, বাগেরহাট অঞ্চল",
            "mapUrl": b_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Bagerhat Museum",
            "nameBn": "বাগেরহাট প্রত্নতাত্ত্বিক জাদুঘর",
            "categoryEn": "Archaeological Heritage Museum & Cultural Archive",
            "categoryBn": "প্রত্নতাত্ত্বিক জাদুঘর ও খলিফাতাবাদ ইতিহাস প্রদর্শশালা",
            "descEn": "Located directly opposite the Sixty Dome Mosque within lush landscaped parklands, the Bagerhat Museum is an essential cultural archive curated by the Department of Archaeology. The museum houses an extraordinary collection of recovered medieval artifacts, including original terracotta plaques, Sultanate stone sculptures, inscribed coins, ancient pottery, and bronze weapons unearthed from the historic Khalifatabad sites. Detailed illustrated architectural models and multilingual historical display boards explain the ingenious urban planning, freshwater canal engineering, and brick construction techniques introduced by Khan Jahan Ali. An authentic black stone sarcophagus and antique Persian calligraphic tablets offer profound insights into medieval Islamic governance in Bengal. It is the ideal introductory destination before or after touring the surrounding UNESCO heritage monuments.",
            "descBn": "ঐতিহাসিক ষাট গম্বুজ মসজিদের ঠিক বিপরীত পাশে মনোরম সবুজ চত্বরে অবস্থিত বাগেরহাট প্রত্নতাত্ত্বিক জাদুঘর খলিফাতাবাদের সোনালী ইতিহাস জানার এক প্রধান তথ্যভাণ্ডার। এই জাদুঘরে সংরক্ষিত আছে বিভিন্ন প্রাচীন প্রত্নস্থল থেকে খননকালে উদ্ধারকৃত সুলতানি আমলের পোড়ামাটির ফলক, প্রাচীন ধাতব মুদ্রা, শিলালিপি, প্রাচীন মৃৎপাত্র ও মধ্যযুগীয় অস্ত্রশস্ত্র। হযরত খান জাহান আলীর পরিকল্পিত নগর ব্যবস্থাপনা, মিষ্টি পানির খাল খনন এবং অনন্য স্থাপত্যশৈলীর বিভিন্ন মডেল ও বিবরণ অত্যন্ত সুন্দরভাবে এখানে উপস্থাপন করা হয়েছে। প্রাচীন বাংলার সমৃদ্ধ মুসলিম সভ্যতার দুর্লভ প্রত্নবস্তুগুলো ইতিহাসপ্রেমী ও গবেষকদের জন্য অত্যন্ত শিক্ষণীয়। ষাট গম্বুজ পরিদর্শনের পাশাপাশি এই জাদুঘরটি ঘুরে দেখা এক দারুণ অভিজ্ঞতা।",
            "locationEn": b_raw['tour_spots'][4]['location'],
            "locationBn": "ষাট গম্বুজ মসজিদের নিকটে, বাগেরহাট",
            "mapUrl": b_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('bagerhat', bagerhat_data)

# ==========================================
# 12. BOGURA
# ==========================================
bo_raw = all_data['bogura']
bogura_data = {
    "slug": "bogura",
    "en": "Bogura",
    "bn": "বগুড়া",
    "hero_title_en": "Bogura Ancient Pundranagara Capital & Archaeological Cradle",
    "hero_title_bn": "বগুড়ার প্রাচীন পুণ্ড্রনগর মহাস্থানগড় ও যমুনা নদীবিধৌত ঐতিহ্য",
    "hero_sub_en": "Third-century BC Mahasthangarh fortified citadel, terracotta Buddhist monasteries at Bhasu Vihara, and historic Jamuna riverfronts.",
    "hero_sub_bn": "খ্রিস্টপূর্ব তৃতীয় শতাব্দীর প্রাচীন পুণ্ড্রবর্ধন মহাস্থানগড়, ভাসু বিহার ও বৈকালিক যমুনার রূপময় নদীতীর।",
    "tagline_en": "The oldest documented urban civilization and archaeological heart of Bangladesh, home to ancient Pundranagara at Mahasthangarh, world-famous curd (Doi), and historic Jamuna river corridors.",
    "tagline_bn": "বাংলাদেশের প্রাচীনতম রাজধানী পুণ্ড্রনগর মহাস্থানগড়ের গর্বিত জেলা, যা প্রায় আড়াই হাজার বছরের ইতিহাস, ভাসু বিহার, গোকুল মেথ, ঐতিহ্যবাহী বগুড়ার দই এবং যমুনার চরাঞ্চলের জন্য বিশ্বজুড়ে পরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/bogura/carousel-1.webp",
            "titleEn": "Mahasthangarh Citadel Ancient Ramparts",
            "titleBn": "মহাস্থানগড় প্রাচীন পুণ্ড্রনগরীর দুর্গপ্রাচীর",
            "subtitleEn": "3rd century BC fortified provincial capital of the Maurya, Gupta, and Pala empires overlooking the Karatoya River",
            "subtitleBn": "করতোয়া নদীর তীরে অবস্থিত আড়াই হাজার বছরের প্রাচীন দুর্গনগরের বিশালাকার প্রতিরক্ষা প্রাচীর ও প্রত্নস্থল"
        },
        {
            "id": 2,
            "image": "images/districts/bogura/carousel-2.webp",
            "titleEn": "Gokul Medh (Behula-Lakhindar Basor Ghar) Terracotta Stupa",
            "titleBn": "গোকুল মেথ (বেহুলা-লখিন্দরের বাসর ঘর)",
            "subtitleEn": "Massive terraced cellular brick stupa in Bogura Sadar entwined with the immortal folklore of Behula and Lakhindar",
            "subtitleBn": "স্তরে স্তরে নির্মিত প্রাচীন বহুকক্ষীয় বৌদ্ধ স্তূপ যা বাংলার অমর লোকগাথা বেহুলা-লখিন্দরের স্মৃতিবাহী"
        },
        {
            "id": 3,
            "image": "images/districts/bogura/carousel-3.webp",
            "titleEn": "Govinda Bhita Riverside Archaeological Promontory",
            "titleBn": "গোবিন্দ ভিটা প্রাচীন প্রত্নতাত্ত্বিক ঢিবি",
            "subtitleEn": "Elevated temple complex just outside the northern ramparts offering breathtaking views across the Karatoya",
            "subtitleBn": "মহাস্থানগড়ের উত্তর প্রাচীরের বাইরে করতোয়ার বাঁকে অবস্থিত বহু স্তরবিশিষ্ট প্রাচীন মন্দির ও দুর্গপ্রাসাদ"
        },
        {
            "id": 4,
            "image": "images/districts/bogura/carousel-4.webp",
            "titleEn": "Bhasu Vihara Ancient Buddhist Monastic Complex",
            "titleBn": "ভাসু বিহার প্রাচীন বৌদ্ধবিহার কমপ্লেক্স",
            "subtitleEn": "Historic monastic retreat in Shibganj visited by the 7th-century Chinese scholar-monk Xuanzang",
            "subtitleBn": "সপ্তম শতকে চীনা পরিব্রাজক হিউয়েন সাং কর্তৃক বর্ণিত ঐতিহাসিক পো থো শি বিহারের মনোরম অবশিষ্টাংশ"
        },
        {
            "id": 5,
            "image": "images/districts/bogura/carousel-5.webp",
            "titleEn": "Sariakandi Jamuna Riverbank Vast Water Horizon",
            "titleBn": "সারিয়াকান্দি যমুনা নদীতীর ও চরের দিগন্ত",
            "subtitleEn": "Dramatic riverfront embankment in Sariakandi where the mighty Jamuna spreads across infinite sandy islands",
            "subtitleBn": "প্রমত্তা যমুনার উত্তাল জলরাশি, বালুচর ও বাতাসে মন জুড়ানো সারিয়াকান্দির বিখ্যাত রিভার ভিউপয়েন্ট"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Mahasthangarh Archaeological Site",
            "nameBn": "মহাস্থানগড় প্রত্নতাত্ত্বিক স্থান",
            "categoryEn": "Ancient Fortified Capital City (Pundranagara)",
            "categoryBn": "প্রাচীন পুণ্ড্রনগর রাজধানী ও প্রত্নতাত্ত্বিক দুর্গনগরী",
            "descEn": "Dating back to at least the third century BC, Mahasthangarh in Shibganj is the oldest and most extensive fortified archaeological citadel in Bangladesh, identified with the legendary ancient capital of Pundranagara. Sprawled across the western bank of the sacred Karatoya River, the massive rectangular brick ramparts enclose an area of over one square kilometer filled with archaeological mounds, palatial foundations, and water reservoirs. Ruled successively by the Mauryan, Gupta, Pala, and early Muslim dynasties, the site yielded the famous 3rd-century BC Brahmi inscription stone, ancient silver coins, terracotta plaques, and golden jewelry. Walking along the high defensive ramparts past Bairagir Bhita and the Jiat Kunda well provides an awe-inspiring connection to over two millennia of continuous urban history. It is the premier archaeological landmark of Bangladesh.",
            "descBn": "শিবগঞ্জ উপজেলায় করতোয়া নদীর তীরে অবস্থিত মহাস্থানগড় বাংলাদেশের প্রাচীনতম ও সর্ববৃহৎ প্রত্নতাত্ত্বিক দুর্গনগরী, যা ইতিহাসের পাতায় 'পুণ্ড্রনগর' নামে খ্যাত। খ্রিস্টপূর্ব তৃতীয় শতাব্দী থেকে শুরু করে মৌর্য, গুপ্ত, পাল ও মুসলিম যুগ পর্যন্ত প্রায় আড়াই হাজার বছর ধরে এটি সমৃদ্ধ প্রাদেশিক রাজধানী হিসেবে ব্যবহৃত হয়েছে। সুবিশাল আয়তাকার এই দুর্গের চারপাশে রয়েছে সুউচ্চ ইটের প্রাচীর, পরিখা, বৈরাগীর ভিটা এবং ঐতিহ্যবাহী 'জিয়ত কুণ্ড' কূপ। এখানে প্রাপ্ত প্রাচীন ব্রাহ্মী শিলালিপি, রৌপ্যমুদ্রা ও পোড়ামাটির ফলক প্রাচীন বাংলার অত্যন্ত উন্নত নগর সভ্যতার সাক্ষ্য দেয়। সুউচ্চ দুর্গপ্রাচীরের ওপর দিয়ে হেঁটে প্রাচীন সভ্যতার ধ্বংসাবশেষ অবলোকন করা যে কোনো মানুষের জন্য এক রোমাঞ্চকর অভিজ্ঞতা।",
            "locationEn": bo_raw['hist_spots'][0]['location'],
            "locationBn": "শিবগঞ্জ, বগুড়া",
            "mapUrl": bo_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Govinda Bhita Archaeological Site",
            "nameBn": "গোবিন্দ ভিটা প্রত্নতাত্ত্বিক স্থান",
            "categoryEn": "Multi-Era Ancient Temple Complex",
            "categoryBn": "প্রাচীন বহুমুখী মন্দির কমপ্লেক্স ও প্রত্নস্থল",
            "descEn": "Govinda Bhita is a prominent elevated archaeological mound situated just outside the northern defensive ramparts of Mahasthangarh, directly overlooking a dramatic horseshoe bend of the Karatoya River. Systematic archaeological excavations revealed four successive phases of temple and secular construction spanning from the late Gupta period through the Pala and Sena dynastic eras. The site contains the foundations of two grand multi-roomed temples featuring stepped brick buttresses, defensive perimeter walls, and decorated brick plinths. Recovered artifacts include exquisite cast-bronze deity idols, glazed northern black pottery, and decorative terracotta lotus medallions. Perched above the riverbed amid ancient trees, Govinda Bhita offers one of the most picturesque and atmospheric archaeological viewpoints in northern Bengal.",
            "descBn": "মহাস্থানগড় দুর্গের উত্তর প্রাচীরের ঠিক বাইরে করতোয়া নদীর সুন্দর বাঁকের মুখে অবস্থিত গোবিন্দ ভিটা এক অত্যন্ত গুরুত্বপূর্ণ প্রাচীন প্রত্নতাত্ত্বিক ঢিবি। বিভিন্ন প্রত্নতাত্ত্বিক খননের মাধ্যমে এখানে গুপ্ত যুগ থেকে শুরু করে পাল ও সেন আমলের চারটি পৃথক ঐতিহাসিক পর্বের মন্দিরের ধ্বংসাবশেষ আবিষ্কৃত হয়েছে। এই স্থানে অবস্থিত পূর্ব ও পশ্চিমের দুটি সুবৃহৎ মন্দিরের অলংকৃত ইটের ভিত্তি এবং সুরম্য প্রবেশদ্বার প্রাচীন প্রকৌশলবিদ্যার উচ্চমান প্রদর্শন করে। এখান থেকে ব্রোঞ্জের দেব-দেবী মূর্তি, পোড়ামাটির ফলক ও প্রাচীন মৃৎপাত্রের অসংখ্য নিদর্শন পাওয়া গেছে। নদীর পাড়ে উঁচু ঢিবির ওপর থেকে চারপাশের প্রাকৃতিক রূপ ও প্রাচীন স্থাপত্যের মেলবন্ধন পর্যটকদের গভীরভাবে মুগ্ধ করে।",
            "locationEn": bo_raw['hist_spots'][1]['location'],
            "locationBn": "মহাস্থানগড়, শিবগঞ্জ, বগুড়া",
            "mapUrl": bo_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Gokul Medh (Behula-Lakhindar Basor Ghar)",
            "nameBn": "গোকুল মেথ (বেহুলা-লখিন্দরের বাসর ঘর)",
            "categoryEn": "Tiered Cellular Buddhist Stupa Complex",
            "categoryBn": "বহুকক্ষীয় প্রাচীন বৌদ্ধ স্তূপ ও লোকঐতিহ্য",
            "descEn": "Gokul Medh, universally celebrated in Bengali folklore as the 'Basor Ghar' (Bridal Chamber) of Behula and Lakhindar from the medieval Manasamangal ballad, is a monumental sixth-to-seventh-century tiered Buddhist temple stupa located in Gokul village. Rising over thirteen meters high, the structure is an engineering wonder consisting of 172 staggered, earth-packed cellular brick chambers arranged in concentric rising terraces to create an unshakeable architectural foundation. Atop the highest terrace stood a soaring octagonal shrine that was later converted into a Shiva temple during the Sena era. The legend tells that Lakhindar's father constructed this impenetrable iron-chamber atop the mound to protect his son from the snake-goddess Manasa's curse. The sheer scale, architectural complexity, and folkloric romance make Gokul Medh an unforgettable archaeological destination.",
            "descBn": "বগুড়া সদর উপজেলার গোকুল গ্রামে অবস্থিত গোকুল মেথ বাংলা লোকসাহিত্যের অমর চরিত্র বেহুলা ও লখিন্দরের বাসর ঘর হিসেবে দেশজুড়ে খ্যাত। বাস্তবে এটি ষষ্ঠ-সপ্তম শতকে নির্মিত এক বিশালাকার ও জটিল প্রকৌশলের বৌদ্ধ স্তূপ, যা প্রায় ১৩ মিটার উঁচুতে ধাপে ধাপে উঠে গেছে। এই স্তূপটির ভিত্তিকে শক্তিশালী করতে ১৭২টি আয়তাকার অন্ধ প্রকোষ্ঠ মাটির সাথে ইটের নিখুঁত গাঁথুনিতে স্তরে স্তরে নির্মাণ করা হয়েছিল, যার শীর্ষে ছিল মূল প্রার্থনালয়। পরবর্তীতে সেন যুগে এটি শিব মন্দিরে রূপান্তরিত হয়। মনসামঙ্গল কাব্যের পৌরাণিক স্মৃতি ও প্রাচীন স্থাপত্যের এই অদ্ভুত মেলবন্ধন দর্শনার্থীদের মনে প্রবল কৌতূহল ও রোমাঞ্চ সৃষ্টি করে। প্রাচীন নির্মাণকলার এক পরম বিস্ময় এই গোকুল মেথ।",
            "locationEn": bo_raw['hist_spots'][2]['location'],
            "locationBn": "গোকুল, বগুড়া সদর, বগুড়া",
            "mapUrl": bo_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Bhasu Vihara",
            "nameBn": "ভাসু বিহার",
            "categoryEn": "Ancient Buddhist Monastic Sanctuary",
            "categoryBn": "প্রাচীন বৌদ্ধবিহার ও বিশ্ববিদ্যালয় প্রাঙ্গণ",
            "descEn": "Bhasu Vihara in Shibganj, situated a few kilometers northwest of Mahasthangarh, is an exquisite eighth-to-tenth-century Buddhist monastic complex identified with the 'Po-Shi-Po' monastery described by the famed seventh-century Chinese pilgrim Xuanzang. Excavations revealed two large brick monasteries alongside a companion temple shrine, complete with residential monk cells, central prayer halls, columned verandas, and inner paved courtyards. The structures feature beautifully molded terracotta plaques on the facades, bronze Buddha sculptures, and terracotta sealings inscribed with monastic scripts. The surrounding rural greenery, ancient trees, and quiet atmosphere evoke the scholastic peace of ancient Buddhist monastic universities in Bengal. It is considered one of the finest and most tranquil excavated monastic sites in South Asia.",
            "descBn": "মহাস্থানগড় থেকে সামান্য দূরে শিবগঞ্জ উপজেলায় অবস্থিত ভাসু বিহার অষ্টম থেকে দশম শতাব্দীর এক অনিন্দ্যসুন্দর বৌদ্ধবিহার ও প্রাচীন শিক্ষাকেন্দ্র। সপ্তম শতাব্দীতে বিখ্যাত চীনা পরিব্রাজক হিউয়েন সাং তাঁর ভ্রমণবৃত্তান্তে যে সুবিশাল 'পো-শি-পো' মঠের বর্ণনা দিয়েছিলেন, প্রত্নতাত্ত্বিকগণ এই ভাসু বিহারকেই সেই ঐতিহাসিক প্রতিষ্ঠান হিসেবে চিহ্নিত করেছেন। খননের ফলে এখানে দুটি বৃহৎ বৌদ্ধবিহার ও একটি মন্দিরের ধ্বংসাবশেষ আবিষ্কৃত হয়েছে, যার মধ্যে ছিল ভিক্ষুদের সুসজ্জিত কক্ষ, উন্মুক্ত প্রাঙ্গণ ও প্রার্থনালয়। এখান থেকে প্রাপ্ত শত শত ব্রোঞ্জ মূর্তি ও পোড়ামাটির সিলমোহর তৎকালীন সমৃদ্ধ জ্ঞানচর্চার সাক্ষ্য দেয়। নিভৃত পল্লীর শান্ত পরিবেশে প্রাচীন বিহারের অবশিষ্টাংশ ঘুরে দেখা এক পরম প্রশান্তির অভিজ্ঞতা।",
            "locationEn": bo_raw['hist_spots'][3]['location'],
            "locationBn": "শিবগঞ্জ, বগুড়া",
            "mapUrl": bo_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Kherua Mosque",
            "nameBn": "খেরুয়া মসজিদ",
            "categoryEn": "Mughal-Transitional Historic Mosque",
            "categoryBn": "প্রাক-মুঘল যুগের ঐতিহাসিক তিন গম্বুজ মসজিদ",
            "descEn": "Constructed in 1582 AD during the turbulent transitional era of the Mughal conquest by Mirza Murad Khan, Kherua Mosque in Sherpur Upazila is a magnificent three-domed brick monument of northern Bengal. Built on an elevated rectangular plinth, the sanctuary features three ribbed hemispherical domes, four octagonal corner minarets, and three pointed-arch entrance portals decorated with delicate floral terracotta relief bands. The weathered red-brick exterior preserves classic Sultanate curved cornices while adopting early Mughal structural proportions, creating a unique synthesis of regional traditions. Inside, finely carved stone mihrabs and arched niches provide an intimate, reverent atmosphere. Surrounded by tranquil rural village homesteads and shaded courtyards, Kherua Mosque remains an active house of prayer and an architectural masterpiece.",
            "descBn": "১৫৮২ খ্রিস্টাব্দে সম্রাট আকবরের আমলে মির্জা মুরাদ খান কর্তৃক নির্মিত শেরপুর উপজেলার খেরুয়া মসজিদটি প্রাক-মুঘল ও সুলতানি নির্মাণরীতির এক অপূর্ব মেলবন্ধন। একটি উঁচু চত্বরের ওপর নির্মিত এই মসজিদে রয়েছে তিনটি সুষম গম্বুজ, চার কোণে চারটি অষ্টভুজাকৃতির মিনার এবং তিনটি খিলানযুক্ত প্রবেশপথ। এর বহির্দেয়ালে পোড়ামাটির ইটের সূক্ষ্ম অলংকরণ, বাঁকানো কার্নিশ এবং ভেতরের পাথরের খোদাই করা মেহরাব তৎকালীন নির্মাণশিল্পীদের উচ্চমানের রুচির পরিচয় দেয়। চার শতাব্দীরও বেশি সময় ধরে কালের ঝড়-ঝাপটা সহ্য করে আজও এটি তার আদি সৌন্দর্য ধরে রেখেছে। সবুজ বৃক্ষরাজিতে ঘেরা শান্ত পরিবেশে অবস্থিত এই প্রাচীন মসজিদটি ইতিহাস ও স্থাপত্যপ্রেমীদের মুগ্ধ করে।",
            "locationEn": bo_raw['hist_spots'][4]['location'],
            "locationBn": "শেরপুর উপজেলা, বগুড়া",
            "mapUrl": bo_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Mahasthangarh Museum",
            "nameBn": "মহাস্থানগড় প্রত্নতাত্ত্বিক জাদুঘর",
            "categoryEn": "National Archaeological Museum & Antiquities Archive",
            "categoryBn": "জাতীয় প্রত্নতাত্ত্বিক জাদুঘর ও প্রাচীন নিদর্শন প্রদর্শশালা",
            "descEn": "Located adjacent to the northern ramparts of the ancient citadel, the Mahasthangarh Museum is an internationally significant cultural institution housing thousands of priceless artifacts unearthed from Pundranagara and surrounding northern excavations. The galleries display remarkable collections of Mauryan Brahmi stone inscriptions, Gupta gold and silver punch-marked coins, terracotta plaques depicting mythological scenes, stone and bronze statues of Buddha and Hindu deities, and antique weaponry. Glass cases showcase fine northern black polished pottery and delicate terracotta beads, demonstrating advanced urban commerce dating back to the third century BC. The museum provides indispensable historical context and visual proof of ancient Bengal's metropolitan brilliance. It is the perfect starting point before wandering through the vast archaeological grounds.",
            "descBn": "মহাস্থানগড় দুর্গের উত্তর প্রাচীরের সন্নিকটে অবস্থিত মহাস্থানগড় জাদুঘর প্রাচীন পুণ্ড্রনগরীর হাজার বছরের ইতিহাস ও প্রত্নসম্পদ সংরক্ষণের প্রধান কেন্দ্র। এই জাদুঘরের বিভিন্ন গ্যালারিতে সংরক্ষিত আছে খ্রিস্টপূর্ব তৃতীয় শতাব্দীর মৌর্য ব্রাহ্মী শিলালিপি, গুপ্ত যুগের সোনার ও রুপার মুদ্রা, পোড়ামাটির ফলক, ব্রোঞ্জ ও পাথরের দেব-দেবী মূর্তি এবং প্রাচীন অলংকার ও অস্ত্রশস্ত্র। প্রাচীনকালের উন্নত মৃৎশিল্প ও দৈনন্দিন জীবনের সামগ্রীগুলো প্রাচীন বাংলার এক সমৃদ্ধ ও সুসংগঠিত নাগরিক সভ্যতার প্রামাণ্য দলিল। এই জাদুঘরটি ঘুরে দেখলে পুণ্ড্রনগরের ইতিহাস ও ঐতিহ্য চোখের সামনে জীবন্ত হয়ে ওঠে। মহাস্থানগড় ভ্রমণের পূর্ণতা পেতে এই জাদুঘর দর্শন অপরিহার্য।",
            "locationEn": bo_raw['tour_spots'][0]['location'],
            "locationBn": "মহাস্থানগড়, শিবগঞ্জ, বগুড়া",
            "mapUrl": bo_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Nawab Palace (Nawab Bari)",
            "nameBn": "নবাব প্যালেস (নবাব বাড়ি)",
            "categoryEn": "Colonial Aristocratic Mansion & Heritage Estate",
            "categoryBn": "উপনিবেশিক রাজপ্রাসাদ ও ঐতিহ্যবাহী নবাব বাড়ি",
            "descEn": "The Nawab Palace (famously known as Nawab Bari) in the heart of Bogura town was the grand residential and administrative seat of the prominent Nawab family of Bogura, whose most famous scion was Muhammad Ali Bogra, third Prime Minister of Pakistan. Constructed in the late nineteenth century in majestic Indo-Saracenic and colonial neoclassical styles, the sprawling estate features sweeping arched verandas, fluted porticos, grand chandeliers, and expansive green courtyards. The palatial compound preserves family heirlooms, vintage photographs, political memorabilia, and antique furnishings from the pre-partition era. The adjoining gardens and quiet avenues provide a tranquil oasis within the bustling commercial city. It stands as an honored symbol of Bogura's political influence and aristocratic heritage.",
            "descBn": "বগুড়া শহরের প্রাণকেন্দ্রে অবস্থিত নবাব প্যালেস (নবাব বাড়ি) এ অঞ্চলের একসময়ের প্রতাপশালী নবাব পরিবারের ঐতিহাসিক রাজপ্রাসাদ, যা আন্তর্জাতিক খ্যাতিসম্পন্ন রাজনীতিবিদ ও পাকিস্তানের সাবেক প্রধানমন্ত্রী মোহাম্মদ আলী বগুড়ার স্মৃতিবিজড়িত। উনিশ শতকের শেষভাগে নির্মিত এই সুরম্য প্রাসাদে রয়েছে ইউরোপীয় নিও-ক্লাসিক্যাল স্থাপত্যের স্তম্ভ, খিলানযুক্ত সুপরিসর বারান্দা এবং বিশাল সবুজ আঙিনা। প্রাসাদের ভেতরে সংরক্ষিত আছে নবাব পরিবারের প্রাচীন আসবাবপত্র, দুর্লভ পারিবারিক আলোকচিত্র ও ঐতিহাসিক স্মারক। শহরের কেন্দ্রস্থলে অবস্থিত হলেও এর চারপাশের মনোরম শান্ত পরিবেশ এক রাজকীয় আবহ তৈরি করে। বগুড়ার রাজনৈতিক ইতিহাস ও আভিজাত্যের প্রতীক হিসেবে নবাব বাড়ি অত্যন্ত দর্শনীয়।",
            "locationEn": bo_raw['tour_spots'][1]['location'],
            "locationBn": "বগুড়া শহর, বগুড়া",
            "mapUrl": bo_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Bogura Satmatha",
            "nameBn": "বগুড়া সাতমাথা",
            "categoryEn": "Iconic City Square & Epicenter of Bogura Doi",
            "categoryBn": "ঐতিহাসিক সাতমাথা চত্বর ও বিখ্যাত দইয়ের বাজার",
            "descEn": "Bogura Satmatha is the legendary commercial, cultural, and geographic heartbeat of Bogura city, where seven bustling major avenues converge at an illuminated central traffic rotary. Surrounded by historic landmarks including the Edward Park, Shaheed Minar, and classical colonial buildings, Satmatha hums with dynamic urban life day and night. The surrounding quarter is world-famous as the epicenter of authentic Bogura Doi (traditional sweetened yogurt prepared in earthen pots), alongside traditional sweetshops selling kheer, rasomalai, and crispy hot jilapis. Travelers gather here in the evenings to enjoy the vibrant northern city vibe, savor mouth-watering street food, and purchase famous clay pots of rich brown curd to take home. It is an unmissable sensory and gastronomic highlight of any visit to Bogura.",
            "descBn": "বগুড়া শহরের প্রাণস্পন্দন হলো এই ঐতিহাসিক 'সাতমাথা' চত্বর, যেখানে শহরের সাতটি প্রধান রাস্তা এসে একবিন্দুতে মিলিত হয়েছে। এডওয়ার্ড পার্ক, শহীদ মিনার এবং প্রাচীন বিপণিবিতানে ঘেরা এই চত্বরটি দিনরাত মানুষের প্রাণবন্ত পদচারণায় মুখরিত থাকে। সাতমাথার চারপাশের মিষ্টির দোকানগুলো বিশ্বখ্যাত খাঁটি 'বগুড়ার দই'-এর প্রধান কেন্দ্র, যেখানে মাটির হাঁড়িতে তৈরি সুস্বাদু ক্ষীরসা ও দই পাওয়া যায়। সন্ধ্যায় এই চত্বরে চায়ের আড্ডা, মুখরোচক স্ট্রিট ফুড ও প্রাণবন্ত শহরের আবহ উপভোগ করতে বহু মানুষ সমবেত হন। বগুড়া শহরের আসল স্পন্দন ও সংস্কৃতির স্বাদ পেতে সাতমাথা চত্বর এক অনন্য দর্শনীয় স্থান।",
            "locationEn": bo_raw['tour_spots'][2]['location'],
            "locationBn": "সাতমাথা, বগুড়া শহর, বগুড়া",
            "mapUrl": bo_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Sariakandi Jamuna Riverbank",
            "nameBn": "সারিয়াকান্দি যমুনা নদীতীর",
            "categoryEn": "Mighty Riverfront Embankment & Sunset Vista",
            "categoryBn": "প্রমত্তা যমুনার নদীতীর ও রিভার ভিউপয়েন্ট",
            "descEn": "The Sariakandi Jamuna Riverbank is an exhilarating ecotourism destination where the colossal Jamuna River sweeps past in an ocean-like expanse of swirling waters and endless seasonal sandbars. The well-constructed river protection embankments provide wide pedestrian promenades where visitors enjoy refreshing cool river breezes and dramatic panoramic views stretching to the horizon. Speedboats and wooden motorized trawlers offer thrilling rides across the river to isolated sand islands (chars) where rural farming and grazing communities thrive. During late afternoon, watching the massive golden sun sink directly into the distant waters is widely celebrated as one of the finest river sunset spectacles in northern Bangladesh. Riverside shacks serve fried river fish, spicy puffed rice, and fresh tea, making it an ideal weekend escape.",
            "descBn": "সারিয়াকান্দিতে যমুনা নদীর তীর উত্তরবঙ্গের অন্যতম জনপ্রিয় ও রোমাঞ্চকর পর্যটন কেন্দ্র, যেখানে প্রমত্তা যমুনা নদী সাগরের মতো বিশাল রূপ নিয়ে প্রবাহিত হচ্ছে। সুদৃঢ় বাঁধের ওপর নির্মিত মনোরম ওয়াকওয়ে দিয়ে হাঁটার সময় নদীর তীব্র শীতল বাতাস শরীর ও মন জুড়িয়ে দেয়। ইঞ্জিনচালিত নৌকা বা স্পিডবোটে চড়ে যমুনার বুক চিরে জেগে ওঠা বালুচরে ঘুরে বেড়ানোর অভিজ্ঞতা অত্যন্ত আনন্দদায়ক। বিকেলের রক্তিম সূর্য যখন যমুনার বিশাল জলরাশির বুকে ডুবে যায়, তখন সৃষ্টি হয় এক অপার্থিব রূপ। নদীতীরের ছোট ছোট দোকানে বসে তাজা যমুনার মাছ ভাজা ও গরম চা খাওয়ার আনন্দ ভ্রমণকে আরও মধুর করে তোলে।",
            "locationEn": bo_raw['tour_spots'][3]['location'],
            "locationBn": "সারিয়াকান্দি, বগুড়া",
            "mapUrl": bo_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Babu's Pond Mass Grave Memorial",
            "nameBn": "বাবুর পুকুর বধ্যভূমি স্মৃতিসৌধ",
            "categoryEn": "1971 Liberation War Historic Memorial Ground",
            "categoryBn": "১৯৭১ সালের মুক্তিযুদ্ধ বধ্যভূমি স্মৃতিসৌধ",
            "descEn": "Located in the Partekhur/Kharna area of Shahjahanpur Upazila, the Babu's Pond Mass Grave Memorial is a solemn historical landmark commemorating the sacrifices of innocent Bengali civilians and freedom fighters during the 1971 Liberation War. In late April and early May 1971, occupying forces conducted brutal roundups, executing dozens of patriotic citizens and burying them beside this historic rural pond. A dignified memorial monument featuring a soaring central marble pillar, inscribed roll of honor, and landscaped surrounding gardens was erected to honor the martyrs' memory. Visitors and students visit the quiet sanctuary to pay respectful tributes and learn about the harrowing sacrifices that led to Bangladesh's independence. It stands as an important, emotionally resonant chapter of Bogura's modern history.",
            "descBn": "শাহজাহানপুর উপজেলার পারতেখুর এলাকায় অবস্থিত 'বাবুর পুকুর বধ্যভূমি' ১৯৭১ সালের মহান মুক্তিযুদ্ধের এক করুণ ও আত্মত্যাগের ঐতিহাসিক স্মারক। ১৯৭১ সালে পাকিস্তানি হানাদার বাহিনী ও তাদের দোসররা এই পুকুরপাড়ে শত শত নিরীহ বাঙালি ও বীর মুক্তিযোদ্ধাকে নির্মমভাবে হত্যা করে গণকবর দেয়। শহীদদের চিরস্মরণীয় করে রাখতে এখানে নির্মিত হয়েছে মার্বেল পাথরের সুউচ্চ স্মৃতিস্তম্ভ ও স্মৃতি প্রাঙ্গণ। শান্ত গ্রামীণ পরিবেশে অবস্থিত এই বধ্যভূমিতে দাঁড়িয়ে শ্রদ্ধাবনত চিত্তে দেশের স্বাধীনতার মূল্য উপলব্ধি করা যায়। মুক্তিযুদ্ধের রক্তঝরা ইতিহাস ও জাতীয় আত্মত্যাগের স্মৃতি জানতে এটি বগুড়ার এক অত্যন্ত গুরুত্বপূর্ণ স্মারক স্থান।",
            "locationEn": bo_raw['tour_spots'][4]['location'],
            "locationBn": "পারতেখুর/খরনা এলাকা, শাহজাহানপুর, বগুড়া",
            "mapUrl": bo_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('bogura', bogura_data)

# ==========================================
# 13. NATORE
# ==========================================
na_raw = all_data['natore']
natore_data = {
    "slug": "natore",
    "en": "Natore",
    "bn": "নাটোর",
    "hero_title_en": "Natore Royal Palaces, Rani Bhabani Heritage & Chalan Beel",
    "hero_title_bn": "নাটোরের রাজবাড়ি, রানী ভবানীর স্মৃতি ও চলনবিলের রূপ",
    "hero_sub_en": "Uttara Ganabhaban royal governor's palace, Natore Rajbari royal complex, and the vast wetland waters of Chalan Beel.",
    "hero_sub_bn": "উত্তরা গণভবনের সুরম্য রাজপ্রাসাদ, রানী ভবানীর নাটোর রাজবাড়ি ও চলনবিলের দিগন্তবিস্তৃত জলজ নিসর্গ।",
    "tagline_en": "The storied royal capital of northern Bengal, immortalized by Rani Bhabani's benevolent reign, opulent Italian-marble palaces at Dighapatia, and world-famous sweet Kachagolla.",
    "tagline_bn": "উত্তরবঙ্গের ঐতিহাসিক রাজকীয় জেলা, যা রানী ভবানীর নাটোর রাজবাড়ি, উত্তরা গণভবন (দিঘাপতিয়া রাজবাড়ি), চলনবিলের অপার বিস্তার এবং খাঁটি কাঁচাগোল্লার জন্য বিশ্বখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/natore/carousel-1.webp",
            "titleEn": "Uttara Ganabhaban (Dighapatia Palace) Grand Gate",
            "titleBn": "উত্তরা গণভবন (দিঘাপতিয়া রাজবাড়ি) রাজকীয় সিংহদ্বার",
            "subtitleEn": "Historic 18th-century royal palace in Dighapatia serving as the official northern residence of the President and Prime Minister",
            "subtitleBn": "দিঘাপতিয়ার সুপ্রাচীন রাজপ্রাসাদ ও সুরম্য সিংহদ্বারের বিশাল ঘড়ি যা বর্তমানে প্রধানমন্ত্রীর উত্তরাঞ্চলীয় সরকারি বাসভবন"
        },
        {
            "id": 2,
            "image": "images/districts/natore/carousel-2.webp",
            "titleEn": "Natore Rajbari Rani Bhabani Palace Complex",
            "titleBn": "নাটোর রাজবাড়ি রানী ভবানীর ঐতিহাসিক প্রাসাদ",
            "subtitleEn": "Sprawling royal compound in Natore town surrounded by concentric defensive moats and ornate terracotta temples",
            "subtitleBn": "সুরম্য পরিখা ও দিঘি দিয়ে ঘেরা নাটোর শহরের সুবিশাল রাজপ্রাসাদ যা মহীয়সী রানী ভবানীর স্মৃতিধন্য"
        },
        {
            "id": 3,
            "image": "images/districts/natore/carousel-3.webp",
            "titleEn": "Chalan Beel Endless Monsoon Water Horizon",
            "titleBn": "চলনবিলের দিগন্তজোড়া জলরাশি ও নৌকা",
            "subtitleEn": "Largest wetland depression in northern Bangladesh transforming into an oceanic inland sea in monsoon",
            "subtitleBn": "সিঙ্গড়া ও গুরুদাসপুরের মধ্য দিয়ে বিস্তৃত দেশের বৃহত্তম বিল যা বর্ষাকালে সমুদ্রের মতো উত্তাল রূপ ধারণ করে"
        },
        {
            "id": 4,
            "image": "images/districts/natore/carousel-4.webp",
            "titleEn": "Green Valley Park Recreation Oasis",
            "titleBn": "গ্রিন ভ্যালি পার্কের আধুনিক বিনোদন নিসর্গ",
            "subtitleEn": "Sprawling family amusement and ecotourism park in Lalpur featuring boating lakes, cable cars, and lush gardens",
            "subtitleBn": "লালপুরে অবস্থিত সুবিশাল আধুনিক বিনোদন পার্ক যেখানে রয়েছে লেক, ক্যাবল কার ও চোখ জুড়ানো সবুজ বাগান"
        },
        {
            "id": 5,
            "image": "images/districts/natore/carousel-5.webp",
            "titleEn": "Halti Beel 'Mini Cox's Bazar' Submerged Highway",
            "titleBn": "হালতি বিল ও পাটুল ডুবন্ত সড়ক",
            "subtitleEn": "Iconic submerged paved road in Naldanga where tourists wade through gentle knee-deep waters across the lake",
            "subtitleBn": "নলডাঙ্গার পাটুলে বর্ষায় বিলের মাঝে ডুবে থাকা কংক্রিটের সড়ক যা 'মিনি কক্সবাজার' হিসেবে পর্যটকদের মাঝে সমাদৃত"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Uttara Ganabhaban",
            "nameBn": "উত্তরা গণভবন (দিঘাপতিয়া রাজবাড়ি)",
            "categoryEn": "Royal Palace & Official Presidential Residence",
            "categoryBn": "ঐতিহাসিক রাজপ্রাসাদ ও সরকারি উত্তরাঞ্চলীয় বাসভবন",
            "descEn": "Constructed originally in the early eighteenth century by Dayaram Roy, the brilliant dewan of the Natore Raj, and rebuilt with magnificent palatial opulence following the 1897 earthquake, Uttara Ganabhaban (Dighapatia Rajbari) is one of the grandest royal estates in South Asia. Spread across forty-one acres surrounded by deep defensive moats and landscaped lawns, the palace complex is entered via an imposing three-story gateway crowned with a giant vintage mechanical clock imported from England. The main palace edifice displays breathtaking neoclassical architecture with Italian marble floors, classical Corinthian columns, grand chandeliers, and classical Greek stone statues scattered across ornamental fountains. In 1972, Father of the Nation Bangabandhu Sheikh Mujibur Rahman designated the estate as the official 'Uttara Ganabhaban' (Northern Presidential Palace) of Bangladesh. It stands as a pinnacle of regal architectural grandeur and national heritage.",
            "descBn": "নাটোরের দিঘাপতিয়ায় অবস্থিত উত্তরা গণভবন (দিঘাপতিয়া রাজবাড়ি) অবিভক্ত বাংলার অন্যতম শ্রেষ্ঠ ও জাঁকজমকপূর্ণ রাজপ্রাসাদ, যা অষ্টাদশ শতাব্দীতে রাজা দয়ারাম রায় কর্তৃক প্রতিষ্ঠিত হয়েছিল। ১৮৯৭ সালের ভূমিকম্পের পর এই প্রাসাদটি ইউরোপীয় ও ভারতীয় রাজকীয় স্থাপত্যের মেলবন্ধনে পুনর্নির্মিত হয়। প্রায় ৪১ একর এলাকা জুড়ে বিস্তৃত এই প্রাসাদটি গভীর পরিখা দিয়ে ঘেরা, যার মূল প্রবেশদ্বারে রয়েছে লন্ডন থেকে আনা শতবর্ষী বিশাল ঘড়ির তোরণ। প্রাসাদের ভেতরে রয়েছে ইতালীয় মার্বেল পাথরের মেঝে, ক্রিস্টাল ঝাড়বাতি, দুর্লভ গ্রিক দেব-দেবীর শ্বেতপাথরের মূর্তি এবং ফোয়ারাযুক্ত রাজকীয় বাগান। ১৯৭২ সালে বঙ্গবন্ধু শেখ মুজিবুর রহমান এটিকে আনুষ্ঠানিকভাবে 'উত্তরা গণভবন' ঘোষণা করেন। ইতিহাস ও আভিজাত্যের এক অনন্য চূড়া এই উত্তরা গণভবন।",
            "locationEn": na_raw['hist_spots'][0]['location'],
            "locationBn": "দিঘাপতিয়া, নাটোর",
            "mapUrl": na_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Natore Rajbari",
            "nameBn": "নাটোর রাজবাড়ি (রানী ভবানীর রাজবাড়ি)",
            "categoryEn": "Historic Imperial Palace Complex & Dynastic Seat",
            "categoryBn": "ঐতিহাসিক রাজবাড়ি ও রানী ভবানীর স্মৃতিপীঠ",
            "descEn": "Natore Rajbari in the center of Natore town is the historic ancestral seat of the illustrious Natore royal dynasty, forever immortalized by the reign of the legendary Rani Bhabani (1716–1803), renowned across Bengal for her philanthropy, governance, and temple patronage. Covering nearly one hundred and twenty acres, the sprawling royal estate is divided into the 'Chhoto Taraf' and 'Boro Taraf' quarters, enclosed by two concentric protective water moats known as 'Shiv Dighi' and 'Rani Pukur'. The complex houses several magnificent palaces featuring classical colonnades, grand reception halls, and exquisitely sculpted terracotta temples dedicated to Shyam Sundar, Tarakeshwar Shiva, and Joykali. The lush gardens are shaded by centuries-old banyan and mahogany canopies reflecting off tranquil moat waters. It stands as a living museum of feudal Bengal's royal architecture and feminine leadership.",
            "descBn": "নাটোর শহরের কেন্দ্রস্থলে অবস্থিত নাটোর রাজবাড়ি অবিভক্ত বাংলার অন্যতম বৃহত্তম সামন্ত সাম্রাজ্যের রাজধানী, যা মহীয়সী নারী ও প্রজাদরদি শাসক রানী ভবানীর (১৭১৬–১৮০৩) স্মৃতিতে অমর হয়ে আছে। প্রায় ১২০ একর আয়তনের সুবিশাল এই রাজবাড়ি এলাকাটি 'বড় তরফ' ও 'ছোট তরফ' ভাগে বিভক্ত এবং সুরক্ষার জন্য দ্বৈত পরিখা ও দিঘি দ্বারা বেষ্টিত ছিল। রাজবাড়ি প্রাঙ্গণে রয়েছে শ্যামসুন্দর মন্দির, তারকেশ্বর শিব মন্দির ও জয়কালী মন্দিরসহ বেশ কয়েকটি সুরম্য প্রাসাদ, যার পোড়ামাটির কারুকাজ ও ইউরোপীয় খিলান অত্যন্ত দৃষ্টিনন্দন। ছায়াঘেরা রাজকীয় বাগান ও শান্ত পরিখার পাড় দর্শনার্থীদের অতীতের রাজকীয় দিনগুলোতে ফিরিয়ে নিয়ে যায়। বাংলার নারী নেতৃত্ব ও জমিদারি ইতিহাসের এক অবিনাশী স্মারক এই নাটোর রাজবাড়ি।",
            "locationEn": na_raw['hist_spots'][1]['location'],
            "locationBn": "নাটোর শহর, নাটোর",
            "mapUrl": na_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Dayarampur Rajbari",
            "nameBn": "দয়ারামপুর রাজবাড়ি",
            "categoryEn": "Colonial Feudal Palace Estate",
            "categoryBn": "ঐতিহাসিক জমিদারি প্রাসাদ ও কাচারি প্রাঙ্গণ",
            "descEn": "Located in Baraigram Upazila, Dayarampur Rajbari was established as a prestigious branch estate of the Dighapatia royal family, named in honor of the dynasty's founder, Raja Dayaram Roy. Built in the late nineteenth century, the palace features an imposing two-story residential building designed with high arched porticos, decorative brick pediments, and colonnaded corridors that overlook expansive royal courtyards. The estate served as an important administrative center overseeing thousands of acres of fertile agricultural estates, with historic courtrooms, treasury vaults, and staff quarters still visible today. Surrounded by mature mango and litchi orchards, the quiet premises retain an aura of aristocratic elegance. It provides an engaging historical visit for travelers exploring the wider royal estates of Natore district.",
            "descBn": "বড়াইগ্রাম উপজেলায় অবস্থিত দয়ারামপুর রাজবাড়ি দিঘাপতিয়া রাজবংশের প্রতিষ্ঠাতা রাজা দয়ারাম রায়ের স্মরণে গড়ে ওঠা এই বংশের অন্যতম গুরুত্বপূর্ণ শাখা রাজপ্রাসাদ। উনিশ শতকের শেষভাগে নির্মিত এই দোতলা সুরম্য প্রাসাদে রয়েছে সুউচ্চ খিলানযুক্ত প্রবেশদ্বার, চমৎকার বারান্দা ও অলংকৃত রাজকীয় প্রকোষ্ঠ। এই প্রাসাদ থেকেই তৎকালীন সময়ে বিশাল অঞ্চলের কৃষি ও খাজনা আদায় নিয়ন্ত্রিত হতো এবং এখানে রয়েছে প্রাচীন কাচারি ঘর ও ধনভাণ্ডার। আম ও লিচু বাগানে ঘেরা শান্ত পরিবেশে প্রাচীন এই প্রাসাদটি অতীতের আভিজাত্যের সাক্ষ্য বহন করে চলেছে। নাটোরের রাজকীয় ঐতিহ্যের আরেক অজানা রূপ প্রত্যক্ষ করতে দয়ারামপুর রাজবাড়ি এক চমৎকার স্থান।",
            "locationEn": na_raw['hist_spots'][2]['location'],
            "locationBn": "বড়াইগ্রাম, নাটোর",
            "mapUrl": na_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Chalan Beel Historic Waterways",
            "nameBn": "চলনবিলের ঐতিহাসিক নৌপথ",
            "categoryEn": "Ancient Wetland Trade Routes & Canal Heritage",
            "categoryBn": "ঐতিহাসিক জলপথ, প্রাচীন পরিখা ও নৌ বাণিজ্য কেন্দ্র",
            "descEn": "The Chalan Beel Historic Waterways across Singra and Gurudaspur upazilas represent centuries of deltaic maritime history that shaped northern Bengal's trade and defense. Historically connecting the mighty Ganges (Padma) and Brahmaputra river systems through a vast labyrinth of natural channels and excavated royal moats, these waterways allowed merchant fleets and royal armadas to traverse northern Bengal with ease. Folk legends recount how rebel commanders and local dacoits navigated these vast seasonal waters to resist imperial forces, while merchant boats traded dried fish, rice, and brassware across regional ports. Ancient brick ghats, submerged historic road causeways, and old wooden market terminals still dot the wetland edges. Exploring these channels provides deep appreciation for the unique aquatic civilization of the Chalan Beel basin.",
            "descBn": "সিংড়া ও গুরুদাসপুরের মধ্য দিয়ে বিস্তৃত চলনবিলের ঐতিহাসিক নৌপথ শতাব্দী ধরে উত্তরবঙ্গের নদীবাণিজ্য ও প্রতিরক্ষার প্রধান জলপথ হিসেবে ব্যবহৃত হয়ে এসেছে। পদ্মা ও যমুনা নদীর সংযোগকারী এই সুবিশাল প্রাকৃতিক জলপথ দিয়ে মধ্যযুগে রাজা-বাদশাহদের নৌবহর এবং বণিকদের পণ্যবাহী বজরা চলাচল করত। বর্ষাকালে এই নদীপথগুলো এক প্রাকৃতিক প্রতিরক্ষার কাজ করত, যা প্রতিরোধ যোদ্ধাদের সহায়তা করেছিল। চলনবিলের প্রাচীন ঘাট, ডুবে যাওয়া পুরোনো সড়ক এবং শতাব্দীপ্রাচীন নৌবন্দরগুলো অতীতের নদীমাতৃক বাণিজ্যের সাক্ষ্য বহন করে। চলনবিলের বুক চিরে চলে যাওয়া এই ঐতিহাসিক জলপথগুলো ভ্রমণ করলে প্রাচীন বাংলার জলকেন্দ্রিক সভ্যতার অপরূপ রূপ দেখা যায়।",
            "locationEn": na_raw['hist_spots'][3]['location'],
            "locationBn": "সিংড়া/গুরুদাসপুর অঞ্চল, নাটোর",
            "mapUrl": na_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Bara Ahnik Mandir Area",
            "nameBn": "বড় আহ্নিক মন্দির এলাকা",
            "categoryEn": "Terracotta Char-Chala Heritage Temple",
            "categoryBn": "ঐতিহাসিক চারচালা পোড়ামাটির মন্দির",
            "descEn": "The Bara Ahnik Mandir, located within the historic complex of the Natore Rajbari, is a masterwork of traditional eighteenth-century terracotta temple architecture in Bengal. Built in the indigenous 'Char-Chala' (four-roofed) idiom with curved cornices mimicking traditional rural thatched cottages, the temple was dedicated to daily devotional prayers (Ahnik) by the royal family. The entire exterior front facade is adorned with extraordinarily fine terracotta plaques depicting scenes from the Ramayana, Krishna Leela, mythical warriors, and floral arabesques. The delicate craftsmanship and harmonious proportions reflect the highest achievements of late medieval Bengali brick masonry under the patronage of Rani Bhabani. It stands as a prized destination for art lovers and cultural historians visiting Natore.",
            "descBn": "নাটোর রাজবাড়ি চত্বরে অবস্থিত বড় আহ্নিক মন্দির অষ্টাদশ শতাব্দীর বাংলার পোড়ামাটির মন্দির স্থাপত্যের এক অবিস্মরণীয় কীর্তি। ঐতিহ্যবাহী 'চারচালা' খড়ের ঘরের অনুকরণে বাঁকানো কার্নিশযুক্ত ছাদের ওপর নির্মিত এই মন্দিরটি রাজপরিবারের প্রত্যহ আহ্নিক বা প্রার্থনার জন্য ব্যবহৃত হতো। মন্দিরের সম্মুখভাগ জুড়ে থাকা শত শত পোড়ামাটির ফলকে রামায়ণ, মহাভারত, শ্রীকৃষ্ণের রাসলীলা এবং পৌরাণিক দৃশ্যাবলী অত্যন্ত সূক্ষ্ম ও নিপুণভাবে খোদাই করা রয়েছে। রানী ভবানীর শিল্পরুচি ও তৎকালীন মৃৎশিল্পীদের অসাধারণ প্রতিভার এক অমর স্মারক এই মন্দির। প্রাচীন বাংলার স্থাপত্য ও ভাস্কর্যকলার অনুরাগী যে কোনো দর্শনার্থীর কাছে এই বড় আহ্নিক মন্দির এক পরম বিস্ময়।",
            "locationEn": na_raw['hist_spots'][4]['location'],
            "locationBn": "নাটোর জেলা",
            "mapUrl": na_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Green Valley Park",
            "nameBn": "গ্রিন ভ্যালি পার্ক",
            "categoryEn": "Premier Family Amusement & Eco Park",
            "categoryBn": "আধুনিক বিনোদন ও পরিবারবান্ধব ইকোপার্ক",
            "descEn": "Green Valley Park in Lalpur Upazila is one of the largest and most dynamic modern amusement and ecotourism parks in northern Bangladesh, covering over one hundred and twenty acres of scenic undulating grounds. The park features an immense artificial lake with pedal boating and speedboat rides, a thrilling cable car crossing above landscaped gardens, high water slides in an aqua park, and thrilling amusement rides for all ages. Visitors stroll along tree-lined boulevards adorned with colorful flower gardens, animal sculptures, and shaded picnic gazebos. Complete with quality dining restaurants and family cottages, it has become the favored weekend getaway for thousands of tourists from across Rajshahi and Natore. It perfectly blends vibrant modern fun with refreshing natural open spaces.",
            "descBn": "লালপুর উপজেলায় অবস্থিত গ্রিন ভ্যালি পার্ক উত্তরবঙ্গের অন্যতম বৃহত্তম ও সর্বাধুনিক পারিবারিক বিনোদন কেন্দ্র, যা প্রায় ১২০ একর সুবিশাল প্রাকৃতিক ভূমির ওপর প্রতিষ্ঠিত। এই পার্কের প্রধান আকর্ষণগুলোর মধ্যে রয়েছে বিশাল লেকে প্যাডেল বোটিং ও স্পিডবোট, বোটানিক্যাল গার্ডেনের ওপর দিয়ে উড়ে চলা ক্যাবল কার, রোমাঞ্চকর ওয়াটার পার্ক এবং শিশুদের নানা রাইডস। পরিপাটি ফুলের বাগান, কৃত্রিম পাহাড়ি ঝরনা ও ছায়াঘেরা বসার স্থান পার্কটিকে দারুণ দৃষ্টিনন্দন করেছে। চমৎকার খাবার রেস্তোরাঁ ও কটেজ সুবিধা থাকার কারণে ছুটির দিনে হাজার হাজার পর্যটক এখানে পরিবার নিয়ে আনন্দঘন সময় কাটাতে আসেন। আধুনিক বিনোদনের এক চমৎকার রাজ্য এই গ্রিন ভ্যালি পার্ক।",
            "locationEn": na_raw['tour_spots'][0]['location'],
            "locationBn": "লালপুর, নাটোর",
            "mapUrl": na_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Natore Rajbari Gardens",
            "nameBn": "নাটোর রাজবাড়ি উদ্যান",
            "categoryEn": "Historic Palatial Gardens & Moat Walkway",
            "categoryBn": "ঐতিহাসিক রাজকীয় বাগান ও শান্ত পরিখা চত্বর",
            "descEn": "The Natore Rajbari Gardens comprise the expansive, peaceful parklands and moat walkways enveloping the royal palaces of Rani Bhabani in the center of Natore town. Shaded by ancient centenary mahogany, banyan, and rain trees, the gardens provide an oasis of cooling green lawns and blooming seasonal flowers. Visitors love strolling along the paved pathways flanking the historic Shiv Dighi and Rani Pukur moats, where cool breezes ripple across tranquil waters that reflect the ancient palace ruins. Local families and tourists gather here for relaxed afternoon walks, photography, and birdwatching beneath high canopies. Stepping outside the palace gates, tourists treat themselves to the legendary authentic Natore Kachagolla sweet at famous heritage sweetshops. It is an unmissable civic sanctuary steeped in history.",
            "descBn": "রানী ভবানীর নাটোর রাজবাড়ি ঘিরে গড়ে ওঠা ঐতিহাসিক উদ্যান নাটোর শহরের বুকে এক স্নিগ্ধ, সুশীতল ও শান্তিময় আশ্রয়স্থল। শতাব্দীপ্রাচীন মেহগনি, কড়ই ও বটগাছের বিশাল ছায়াতলে বিস্তৃত এই বাগানের বুক চিরে চলে গেছে পরিপাটি হাঁটার পথ। ঐতিহাসিক পরিখা ও দিঘির পাড়ে বসে স্নিগ্ধ বাতাস উপভোগ করা এবং প্রাচীন প্রাসাদের প্রতিবিম্ব দেখা এক অপার্থিব অনুভূতি এনে দেয়। বিকেলে বহু মানুষ পরিবার নিয়ে এই উদ্যানে হাঁটেন এবং রাজবাড়ির শান্ত পরিবেশ উপভোগ করেন। উদ্যান ভ্রমণের শেষে নাটোরের বিখ্যাত ও খাঁটি 'কাঁচাগোল্লা' মিষ্টির স্বাদ নেওয়া প্রতিটি পর্যটকের জন্য এক অপরিহার্য আনন্দ। ইতিহাস ও প্রকৃতির শান্তিময় মেলবন্ধন এই উদ্যান।",
            "locationEn": na_raw['tour_spots'][1]['location'],
            "locationBn": "নাটোর শহর, নাটোর",
            "mapUrl": na_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Chalan Beel",
            "nameBn": "চলনবিলের প্রাকৃতিক রূপ",
            "categoryEn": "Massive Wetland Ecosystem & Monsoon Water Wonderland",
            "categoryBn": "দেশের বৃহত্তম মিঠা পানির বিল ও জলপ্রকৃতি",
            "descEn": "Chalan Beel, spanning across Singra and Gurudaspur in Natore along with neighbouring districts, is the largest freshwater wetland ecosystem in northern Bangladesh. During the monsoon season, the beel transforms into an awe-inspiring, ocean-like freshwater sea where endless rippling waves stretch uninterrupted to the sky under swirling cloudscapes. Tourists embark on memorable wooden boat cruises across the boundless waters, enjoying fresh breeze, witnessing local fishermen cast traditional nets, and dining on piping hot freshwater fish cooked directly on the boat. In winter, the waters recede to expose lush green mustard fields and shallow lagoons that attract thousands of colorful migratory waterfowl. Chalan Beel represents an iconic, sublime natural spectacle of deltaic Bangladesh.",
            "descBn": "নাটোরের সিংড়া ও গুরুদাসপুরসহ বিস্তীর্ণ অঞ্চল জুড়ে বিস্তৃত চলনবিল বাংলাদেশের বৃহত্তম ও সবচেয়ে রোমাঞ্চকর প্রাকৃতিক মিঠা পানির জলাভূমি। বর্ষাকালে এই বিলের কূলহীন জলরাশি সাগরের মতো উত্তাল রূপ ধারণ করে যা ভ্রমণপ্রেমীদের এক অদ্ভুত মুগ্ধতায় আচ্ছন্ন করে। ইঞ্জিনচালিত কাঠের নৌকায় চড়ে চলনবিলের দিগন্তজোড়া বুকে ভেসে বেড়ানো এবং বিলের তাজা মাছের স্বাদ নেওয়া এক অনন্য অভিজ্ঞতা। শীতকালে বিলের পানি নেমে গেলে দিগন্তজোড়া হলুদ সরিষা ক্ষেতের সমারোহ ঘটে এবং হাজার হাজার অতিথি পাখির কলকাকলিতে মুখরিত হয় চারপাশ। নদীমাতৃক বাংলার রূপ ও বিশালতা প্রত্যক্ষ করতে চলনবিল ভ্রমণ এক অবিস্মরণীয় স্বপ্নযাত্রা।",
            "locationEn": na_raw['tour_spots'][2]['location'],
            "locationBn": "সিংড়া ও গুরুদাসপুর, নাটোর",
            "mapUrl": na_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Halti Beel",
            "nameBn": "হালতি বিল (পাটুল মিনি কক্সবাজার)",
            "categoryEn": "Submerged Highway & Inland Coastal Experience",
            "categoryBn": "ডুবন্ত সড়ক ও উত্তাল মিঠা পানির মিনি কক্সবাজার",
            "descEn": "Halti Beel in Naldanga Upazila has earned widespread national fame as the 'Mini Cox's Bazar of North Bengal' due to its unique submerged concrete highway at Patul. During the monsoon months, the vast beel fills with shimmering water that gently submerges the low-lying paved road in crystal-clear knee-deep water, allowing tourists to walk directly across the middle of the lake. The sensation of gentle waves lapping around one's feet with endless water on both sides attracts thousands of excited visitors, photographers, and youth daily. Traditional wooden boats offer fun cruises across the lake to picturesque isolated village islands, while waterfront vendors serve hot tea, snacks, and fried freshwater fish. It is one of the most vibrant, photogenic ecotourism phenomena in the nation.",
            "descBn": "নলডাঙ্গার পাটুলে অবস্থিত হালতি বিল সারা দেশে 'উত্তরবঙ্গের মিনি কক্সবাজার' হিসেবে দারুণ জনপ্রিয়তা লাভ করেছে। বর্ষাকালে হালতি বিলের অথৈ জলরাশি যখন পাটুল-খোলাবাড়িয়ার পিচঢালা সড়ককে হাঁটু পানিতে ডুবিয়ে দেয়, তখন তৈরি হয় এক অভূতপূর্ব রোমাঞ্চকর দৃশ্যপট। পানির ওপর দিয়ে হেঁটে চলা এবং দুই পাশে সাগরের মতো ঢেউয়ের কলতান পর্যটকদের সমুদ্র সৈকতের মতো অনুভূতি দেয়। শত শত রঙিন নৌকা পর্যটকদের নিয়ে বিলের বুকে ঘুরে বেড়ায় এবং বিলের মাঝে থাকা দ্বীপসদৃশ গ্রামগুলোতে নিয়ে যায়। নদীতীরের দোকানে গরম গরম ভাজা মাছ আর চায়ের কাপে আড্ডা জমে ওঠে। এক ভিন্নধর্মী প্রাকৃতিক রোমাঞ্চের স্বাদ পেতে হালতি বিল অতুলনীয়।",
            "locationEn": na_raw['tour_spots'][3]['location'],
            "locationBn": "নলডাঙ্গা, নাটোর",
            "mapUrl": na_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Dighapatia Palace Grounds",
            "nameBn": "দিঘাপতিয়া রাজপ্রাসাদ চত্বর",
            "categoryEn": "Landscaped Royal Gardens & Historic Promenade",
            "categoryBn": "ঐতিহাসিক রাজকীয় উদ্যান ও পরিখা চত্বর",
            "descEn": "The Dighapatia Palace Grounds encompass the sprawling exterior landscaped parklands, moat bridges, and botanical gardens of the Uttara Ganabhaban complex in Natore. Flanked by deep defensive water channels, the grounds feature majestic royal palm avenues, ancient banyan trees, manicured lawns, and rare historical flora planted during the nineteenth century. Visitors can marvel at the grand architectural facade of the palace across the moat, photograph the ornate mechanical clock tower, and walk through the historic deer park and bird sanctuary. The peaceful, impeccably maintained environment provides an inspiring setting that harmoniously links history, architecture, and lush nature. It is widely considered one of the most dignified and beautiful public heritage grounds in Bangladesh.",
            "descBn": "উত্তরা গণভবনের মূল প্রাসাদের বাইরে অবস্থিত দিঘাপতিয়া রাজপ্রাসাদ চত্বর সুবিশাল পরিখা, সুবিন্যস্ত রাজকীয় বাগান ও শতাব্দীপ্রাচীন বৃক্ষরাজিতে ঘেরা এক নয়নাভিরাম এলাকা। সুউচ্চ পাম গাছের সারি, প্রাচীন বটের ছায়া এবং সুদৃশ্য হ্রদ এই চত্বরটিকে অত্যন্ত রাজকীয় রূপ দান করেছে। পরিখার ওপর নির্মিত সেতু থেকে রাজপ্রাসাদের অপরূপ দৃশ্য দেখা যায় এবং প্রাচীন ঘড়ি তোরণের সামনে দাঁড়িয়ে ছবি তোলার জন্য এটি পর্যটকদের প্রিয় স্থান। পরিচ্ছন্ন ও সুরক্ষিত এই চত্বরে ঘুরে বেড়ালে শরীর ও মনে এক অপূর্ব শান্তি অনুভূত হয়। ইতিহাস, ঐতিহ্য ও রাজকীয় প্রকৃতির অনিন্দ্যসুন্দর মেলবন্ধন দেখতে দিঘাপতিয়া চত্বর সত্যিই এক পরম স্বর্গ।",
            "locationEn": na_raw['tour_spots'][4]['location'],
            "locationBn": "দিঘাপতিয়া, নাটোর",
            "mapUrl": na_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('natore', natore_data)

# ==========================================
# 14. PIROJPUR
# ==========================================
pi_raw = all_data['pirojpur']
pirojpur_data = {
    "slug": "pirojpur",
    "en": "Pirojpur",
    "bn": "পিরোজপুর",
    "hero_title_en": "Pirojpur Backwater Waterways, Floating Coconut Markets & River Ports",
    "hero_title_bn": "পিরোজপুরের ব্যাকওয়াটার নদী, ভাসমান নারিকেলের হাট ও কাউখালী বন্দর",
    "hero_sub_en": "Historic Rayerkathi Zamindar Bari, Kaukhali river port on the Baleshwar, and serene tidal canal networks.",
    "hero_sub_bn": "রায়রকাঠি জমিদার বাড়ি, বলেশ্বর ও সন্ধ্যা নদীর সঙ্গম, কাউখালী নদীবন্দর ও রূপময় খালের ব্যাকওয়াটার।",
    "tagline_en": "The southern riverine sanctuary of Bangladesh, famed for dense interlocking networks of freshwater canals, floating coconut bazaars at Kuriana, and grand zamindari palaces at Rayerkathi.",
    "tagline_bn": "দক্ষিণাঞ্চলের নদীমাতৃক প্রকৃতির আরেক বিস্ময়, যা শতাব্দীপ্রাচীন রায়রকাঠি জমিদার বাড়ি, কুড়িয়ানা ও আটঘরের ভাসমান বাজার, বলেশ্বর নদীর উত্তাল রূপ এবং কাউখালী নৌবন্দরের জন্য পরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/pirojpur/carousel-1.webp",
            "titleEn": "Rayerkathi Zamindar Bari Historic Palatial Complex",
            "titleBn": "রায়রকাঠি জমিদার বাড়ির প্রাচীন রাজপ্রাসাদ",
            "subtitleEn": "16th-century feudal estate founded by Raja Pitambar Roy featuring ancient Kali temples and massive brick ruins",
            "subtitleBn": "ষোড়শ শতাব্দীতে রাজা পীতাম্বর রায় কর্তৃক প্রতিষ্ঠিত ঐতিহ্যবাহী জমিদারি প্রাসাদ ও প্রাচীন দেবালয়"
        },
        {
            "id": 2,
            "image": "images/districts/pirojpur/carousel-2.webp",
            "titleEn": "Baleshwar Riverbank Scenic Wide Horizon",
            "titleBn": "বলেশ্বর নদীতীরের প্রমত্তা রূপ ও সূর্যাস্ত",
            "subtitleEn": "Mighty tidal river flowing gracefully toward the Sundarbans mangrove delta past lush green palm groves",
            "subtitleBn": "নারিকেল-সুপারির বাগান ঘেঁষে সুন্দরবনের পানে বয়ে চলা খরস্রোতা ও প্রমত্তা বলেশ্বর নদী"
        },
        {
            "id": 3,
            "image": "images/districts/pirojpur/carousel-3.webp",
            "titleEn": "Kaukhali River Port Historic Inland Terminal",
            "titleBn": "কাউখালী নদী বন্দরের প্রাণবন্ত নৌবাণিজ্য",
            "subtitleEn": "Legendary riverine trading hub at the junction of the Sandhya and Gabkhan waterways",
            "subtitleBn": "সন্ধ্যা নদী ও গাবখান চ্যানেলের সঙ্গমে অবস্থিত শতবর্ষী ঐতিহ্যবাহী নৌবন্দর ও লঞ্চঘাট"
        },
        {
            "id": 4,
            "image": "images/districts/pirojpur/carousel-4.webp",
            "titleEn": "Sarengakathi Canal Floating Market Landscape",
            "titleBn": "সারেঙ্গাকাঠির ব্যাকওয়াটার খাল ও ভাসমান নৌজীবন",
            "subtitleEn": "Scenic green backwater canals shaded by overhanging betel-nut palms where wooden canoes trade produce",
            "subtitleBn": "সবুজ সুপারি বাগান ও পেয়ারা বাগানের নিচ দিয়ে চলে যাওয়া ছায়াঘেরা শান্ত খালের মায়াবী নিসর্গ"
        },
        {
            "id": 5,
            "image": "images/districts/pirojpur/carousel-5.webp",
            "titleEn": "Mathbaria Waterways & Lush River Meadows",
            "titleBn": "মঠবাড়িয়ার নদ-নদী ও উপকূলীয় সবুজ চরাঞ্চল",
            "subtitleEn": "Meandering coastal waterways connecting rural southern delta settlements with fresh river breezes",
            "subtitleBn": "উপকূলীয় গ্রামীণ জীবনের শান্ত রূপ ও নদীর বুক চিরে ছুটে চলা ঐতিহ্যবাহী কাঠের নৌকা"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Rayerkathi Zamindar Bari",
            "nameBn": "রায়রকাঠি জমিদার বাড়ি",
            "categoryEn": "Ancient Feudal Capital & Heritage Palace",
            "categoryBn": "ষোড়শ শতাব্দীর প্রাচীন জমিদারি প্রাসাদ ও মন্দির",
            "descEn": "Founded in the late sixteenth century during the Mughal era by Raja Pitambar Roy, Rayerkathi Zamindar Bari in Pirojpur Sadar is one of the oldest and most extensive feudal palace complexes in southern Bangladesh. The historic compound spans several dozen acres, incorporating imposing multi-storied residential palaces, fortified armories, ceremonial dance pavilions (Jalsa Ghar), and ancient stepped bathing tanks. It is especially famous for hosting over two hundred historic Hindu temples, most notably the colossal Kali Temple and Shiva Mandir built with massive terracotta bricks and imported stone lingams. The architecture displays a captivating blend of pre-Mughal Sultanate motifs, neoclassical colonnades, and traditional Bengali brick arches. Exploring the ivy-clad ruins under the canopy of ancient banyan trees offers a profound journey into the feudal history of the southern delta.",
            "descBn": "মুঘল সম্রাট জাহাঙ্গীরের আমলে ষোড়শ শতাব্দীর শেষভাগে রাজা পীতাম্বর রায় কর্তৃক প্রতিষ্ঠিত রায়রকাঠি জমিদার বাড়ি দক্ষিণ বাংলার অন্যতম প্রাচীন ও সুবিশাল সামন্তযুগীয় রাজপ্রাসাদ। সুবিশাল এলাকা জুড়ে বিস্তৃত এই রাজবাড়িতে এককালে ছিল রাজকীয় নাটমন্দির, অস্ত্রাগার, দেওয়ানখানা এবং সুদৃশ্য শানবাঁধানো দীঘি। এই রাজবাড়িটি প্রায় দুই শতাধিক প্রাচীন মন্দিরের জন্য বিখ্যাত, যার মধ্যে বিশাল কালী মন্দির ও শিব মন্দির বিশেষভাবে উল্লেখযোগ্য। চুন-সুরকির প্রাচীন দেওয়াল, খিলানযুক্ত প্রবেশপথ এবং সুউচ্চ স্তম্ভ তৎকালীন রাজাদের অসীম প্রভাব ও শিল্পরুচির পরিচয় দেয়। প্রাচীন বটবৃক্ষের ছায়ায় শতাব্দীর প্রাচীন এই প্রাসাদের ধ্বংসাবশেষ ঘুরে দেখা ইতিহাসপ্রেমীদের মনে এক অদ্ভুত রোমাঞ্চ জাগায়।",
            "locationEn": pi_raw['hist_spots'][0]['location'],
            "locationBn": "রায়রকাঠি, পিরোজপুর সদর, পিরোজপুর",
            "mapUrl": pi_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Mathbaria Historic Market and River-Port Area",
            "nameBn": "মঠবাড়িয়া ঐতিহাসিক বাজার ও নদী বন্দর এলাকা",
            "categoryEn": "Colonial Coastal Maritime Trading Post",
            "categoryBn": "ঐতিহাসিক নদী বন্দর ও প্রাচীন বাণিজ্যিক বাজার",
            "descEn": "The Mathbaria Historic Market and River-Port Area in southern Pirojpur flourished during the eighteenth and nineteenth centuries as a crucial maritime trading center connecting the coastal Sundarbans to central Bengal. Bordering tidal riverways that flow directly toward the Bay of Bengal, the port bustled with wooden merchant vessels carrying sundari timber, betel nuts, coconuts, and sea salt. Surviving colonial-era wooden trading houses, ancient brick warehouses, and traditional boatbuilding yards line the historic riverfront. The settlement preserves rich oral memories of maritime trade, local resistance movements, and cultural interactions among diverse deltaic communities. Strolling through the vibrant old market quarters connects travelers to the living river trade traditions of coastal Barishal.",
            "descBn": "পিরোজপুরের দক্ষিণাংশে অবস্থিত মঠবাড়িয়া ঐতিহাসিক বাজার ও নদী বন্দর এলাকা অষ্টাদশ ও উনিশ শতকে উপকূলীয় সুন্দরবন এবং সমতল বাংলার মধ্যকার এক প্রধান বাণিজ্যপথ হিসেবে গড়ে উঠেছিল। বঙ্গোপসাগরের মুখে অবস্থিত হওয়ার কারণে সেকালে এই বন্দর দিয়ে সুন্দরী কাঠ, নারিকেল, সুপারি ও লবণের বিশাল কারবার চলত। নদীর তীরে আজও দেখা যায় প্রাচীন কাঠের দোতলা আড়তঘর, পুরোনো কাচারি এবং ঐতিহ্যবাহী নৌকা তৈরির ডকইয়ার্ড। স্থানীয় সংস্কৃতি ও উপকূলীয় নদীবাণিজ্যের বহু ইতিহাস জড়িয়ে আছে এই বাজারের সাথে। শতাব্দীর স্মৃতিবাহী এই প্রাণবন্ত নদী বন্দর এলাকাটি গ্রামীণ বাংলার নদীভিত্তিক অর্থনীতির এক চমৎকার উদাহরণ।",
            "locationEn": pi_raw['hist_spots'][1]['location'],
            "locationBn": "মঠবাড়িয়া, পিরোজপুর",
            "mapUrl": pi_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Indurkani Historic Mosque and Shrine Area",
            "nameBn": "ইন্দুরকানী ঐতিহাসিক মসজিদ ও মাজার এলাকা",
            "categoryEn": "Sacred Historical Sanctuary",
            "categoryBn": "ঐতিহাসিক সুফি দরবার ও প্রাচীন মসজিদ",
            "descEn": "The Indurkani Historic Mosque and Shrine Area in Zianagar Upazila preserves the sacred heritage of early Islamic missionaries and Sufi saints who navigated the remote tidal rivers of southern Bengal in the seventeenth century. Nestled beside tranquil river loops and shaded by towering betel nut palms, the historic mosques feature thick brick masonry, multi-tiered domes, and delicate plaster floral niches. The shrines commemorate revered spiritual mentors who cleared dense forest areas, established community welfare centers, and fostered peaceful harmony among settling communities. Annual devotional gatherings bring thousands of devotees to pray, share communal meals, and recite spiritual poetry in the tranquil village setting. It forms a cherished anchor of spiritual identity and heritage in Pirojpur.",
            "descBn": "ইন্দুরকানী (জিয়ানগর) উপজেলার ঐতিহাসিক মসজিদ ও মাজার প্রাঙ্গণ সপ্তদশ শতাব্দীতে দক্ষিণ বাংলার উপকূলীয় নদীবিধৌত অঞ্চলে ইসলাম প্রচারক ও সুফি সাধকদের আগমনের এক পুণ্যময় স্মারক। আঁকাবাঁকা শান্ত নদী ও সুপারি বাগানের মাঝে গড়ে ওঠা এই প্রাচীন মসজিদগুলোতে রয়েছে চুন-সুরকির মজবুত দেওয়াল, গম্বুজ এবং লতাপাতার সুন্দর অলংকরণ। তৎকালীন সময়ে বনাঞ্চল আবাদ করে জনবসতি গড়ে তুলতে এই সুফি সাধকগণ গুরুত্বপূর্ণ ভূমিকা পালন করেছিলেন। মাজার প্রাঙ্গণে বিরাজমান নিবিড় প্রশান্তি দর্শনার্থীদের মন ছুঁয়ে যায়। স্থানীয় ধর্মপ্রাণ মানুষের কাছে অত্যন্ত শ্রদ্ধেয় এই দরবার শতাব্দীপ্রাচীন আধ্যাত্মিক ঐতিহ্যের প্রতীক হয়ে টিকে আছে।",
            "locationEn": pi_raw['hist_spots'][2]['location'],
            "locationBn": "ইন্দুরকানী, পিরোজপুর",
            "mapUrl": pi_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Nazirpur Historic Zamindar-House Sites",
            "nameBn": "নাজিরপুর ঐতিহাসিক জমিদার বাড়ি এলাকা",
            "categoryEn": "Colonial Feudal Palatial Residencies",
            "categoryBn": "ঐতিহাসিক জমিদারি আবাস ও প্রাসাদ এলাকা",
            "descEn": "The Nazirpur Historic Zamindar-House Sites encompass the grand residential compounds and administrative estates of prominent agrarian landlords who held sway across northern Pirojpur during the nineteenth century. Featuring stately brick facades, classical European porticos, arched verandas, and inner zenana courtyards, these mansions showcase the luxurious lifestyle of regional landlords who profited from fertile rice and coconut lands. The zamindars dug expansive stepped dighis and patronized traditional rural educational institutions and theatrical jatras. Although time has draped portions of the brickwork in lush moss and wild climbing vines, the surviving columns and ornate entrance arches exude romantic historical charm. It offers a nostalgic, off-the-beaten-path cultural exploration in rural Pirojpur.",
            "descBn": "নাজিরপুর উপজেলার ঐতিহাসিক জমিদার বাড়ি এলাকা উনিশ শতকের সামন্ত প্রভুদের বিত্ত-বৈভব ও শাসনের স্মৃতিবাহী এক প্রাচীন প্রাসাদ প্রাঙ্গণ। ইউরোপীয় উপনিবেশিক স্থাপত্য ও স্থানীয় নির্মাণরীতির ছোঁয়ায় তৈরি এই ভবনগুলোতে ছিল বিশাল কাচারি ঘর, বাগানবাড়ি ও রাজকীয় অন্দরমহল। নাজিরপুরের উর্বর জমিতে উৎপাদিত ধান ও নারিকেল-সুপারির সমৃদ্ধ বাণিজ্য তৎকালীন জমিদারদের প্রভাব বৃদ্ধি করেছিল। প্রাসাদের প্রাচীন শানবাঁধানো দীঘি ও কারুকার্যময় স্তম্ভগুলো আজও অতীতের আভিজাত্যের সাক্ষ্য বহন করে। সবুজ প্রকৃতির কোলে নিস্তব্ধ দাঁড়িয়ে থাকা এই প্রাচীন ধ্বংসাবশেষ পর্যটকদের এক নস্টালজিক অনুভূতি উপহার দেয়।",
            "locationEn": pi_raw['hist_spots'][3]['location'],
            "locationBn": "নাজিরপুর, পিরোজপুর",
            "mapUrl": pi_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Baleshwar River Historic Ferry Area",
            "nameBn": "বলেশ্বর নদীর ঐতিহাসিক ফেরিঘাট এলাকা",
            "categoryEn": "Historic Maritime River Crossing & Transport Hub",
            "categoryBn": "ঐতিহাসিক নদী পারাপার ও ফেরিঘাট",
            "descEn": "The Baleshwar River Historic Ferry Area has served for centuries as the vital nautical crossing point connecting the Barishal division with Khulna and the Sundarbans coastal region. Before the construction of modern bridges, this vast river crossing witnessed millions of passengers, wooden cargo boats, and colonial steam launches navigating its sweeping tidal currents. The riverfront preserves old stone boarding ramps, historic passenger waiting pavilions, and traditional wooden tea stalls where travelers rested during their journeys. Standing on the breezy embankments, visitors feel the pulse of southern maritime travel and watch fishing boats brave the powerful currents. It remains an indelible cultural and geographic landmark in the history of southwestern Bangladesh.",
            "descBn": "বলেশ্বর নদীর এই ঐতিহাসিক ফেরিঘাট এলাকা শতাব্দী ধরে বরিশাল ও খুলনা বিভাগের মধ্যকার প্রধান নদী পারাপার ও যোগাযোগের সেতুবন্ধন হিসেবে ব্যবহৃত হয়ে এসেছে। সেতু নির্মাণের পূর্বে এই খরস্রোতা নদী পারাপারের জন্য ঐতিহ্যবাহী কাঠের নৌকা, ফেরি ও স্টিমারের ওপর নির্ভর করত পুরো দক্ষিণাঞ্চলের লাখ লাখ মানুষ। ঘাট সংলগ্ন পুরোনো চায়ের দোকান ও বাঁধের ওপর দাঁড়িয়ে প্রমত্তা বলেশ্বরের বিশাল ঢেউ এবং মাঝি-মাল্লাদের কর্মচাঞ্চল্য দেখার অনুভূতি অনন্য। গোধূলিলগ্নে নদীর বুকে ভেসে আসা শান্ত বাতাস শহরের ক্লান্তি দূর করে দেয়। দক্ষিণবঙ্গের নদীকেন্দ্রিক যাতায়াত ও ইতিহাসের এক জীবন্ত স্মারক এই ঐতিহাসিক ফেরিঘাট।",
            "locationEn": pi_raw['hist_spots'][4]['location'],
            "locationBn": "পিরোজপুর জেলা নদীতীর, পিরোজপুর",
            "mapUrl": pi_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Baleshwar Riverbank",
            "nameBn": "বলেশ্বর নদীতীর",
            "categoryEn": "Majestic Tidal Riverfront & Sunset Viewpoint",
            "categoryBn": "প্রমত্তা নদীতীর, স্নিগ্ধ বাঁধ ও সূর্যাস্ত ভিউপয়েন্ট",
            "descEn": "The Baleshwar Riverbank is a magnificent natural attraction where one of Bangladesh's mightiest coastal rivers flows with oceanic grandeur past palm-fringed shores. Strolling along the elevated protective embankments, visitors enjoy wide, unobstructed vistas across miles of sparkling tidal water, distant green chars, and wooden fishing boats dancing on gentle waves. During late afternoon, sunset transforms the river into a glittering molten-gold expanse while refreshing river winds provide a rejuvenating escape from urban heat. Waterfront stalls along the promenade serve authentic southern snacks, steamed pithas, and freshly caught river fish. It is widely cherished as the premier open-air relaxation and photography spot in Pirojpur.",
            "descBn": "বলেশ্বর নদীতীর পিরোজপুরের প্রকৃতির এক অপার সৌন্দর্যপীঠ, যেখানে খরস্রোতা নদীটি তার সুবিশাল জলরাশি নিয়ে বঙ্গোপসাগরের পানে বয়ে চলেছে। নদীর বাঁধের ওপর দিয়ে নির্মিত ওয়াকওয়ে ধরে হাঁটার সময় শরীর জুড়ানো দখিনা বাতাস ও ঢেউয়ের কলতান যে কাউকে মুগ্ধ করে। বিকেলে যখন পশ্চিমাকাশে সূর্য হেলে পড়ে, তখন নদীর বুকজুড়ে সৃষ্টি হয় রক্তিম আলোর মায়াবী ঝিলিক যা সূর্যাস্তপ্রেমীদের জন্য এক স্বপ্নিল দৃশ্য। নদীতীরের দোকানগুলোতে বসে গরম চা খাওয়া ও স্থানীয় টাটকা মাছ ভাজার স্বাদ নেওয়া ভ্রমণকে আরও আনন্দদায়ক করে তোলে। কোলাহলমুক্ত পরিবেশে নদীর অপার বিস্তার উপভোগে বলেশ্বর নদীতীর এক অনন্য স্থান।",
            "locationEn": pi_raw['tour_spots'][0]['location'],
            "locationBn": "পিরোজপুর জেলা, পিরোজপুর",
            "mapUrl": pi_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Kaukhali River Port",
            "nameBn": "কাউখালী নদী বন্দর",
            "categoryEn": "Historic Inland Waterway Terminal & Vibrant Bazaar",
            "categoryBn": "ঐতিহাসিক নদী বন্দর, লঞ্চ টার্মিনাল ও নৌবাণিজ্য কেন্দ্র",
            "descEn": "Kaukhali River Port is a legendary, vibrant inland waterway hub situated at the strategic confluence of the Sandhya River and the Gabkhan Channel. Renowned as a key transit terminal where massive passenger launches, cargo coasters, and fishing trawlers dock daily, the waterfront bustles with energetic trade and travel. Visitors love watching ships maneuver smoothly through the wide river channel and taking open-top wooden boat rides across the breezy waters. The waterfront is packed with vibrant traditional markets selling fresh seasonal fruits, coconuts, and freshly landed river hilsa fish directly from local boats. It provides an authentic, lively experience of southern Bengal's maritime commerce.",
            "descBn": "সন্ধ্যা নদী ও গাবখান চ্যানেলের সঙ্গমস্থলে অবস্থিত কাউখালী নদী বন্দর দক্ষিণ বাংলার অন্যতম ব্যস্ত ও ঐতিহাসিক নৌবাণিজ্য কেন্দ্র। প্রতিদিন বিশালাকার যাত্রীবাহী লঞ্চ, কার্গো জাহাজ ও মাছের ট্রলারের গমগমে উপস্থিতিতে এই বন্দর এলাকা দিনরাত মুখরিত থাকে। বন্দরের ঘাট থেকে কাঠের নৌকায় চড়ে নদীর বুক চিরে ঘুরে বেড়ানোর অভিজ্ঞতা অত্যন্ত রোমাঞ্চকর। ঘাটের পাশে বসা তাজা ফলের পাইকারি বাজার ও রূপালী ইলিশের আড়ত এই বন্দরকে আরও প্রাণবন্ত করে তুলেছে। নদীর তাজা বাতাস, জাহাজের সাইরেন আর স্থানীয় মানুষের প্রাণচাঞ্চল্য দেখতে কাউখালী নদী বন্দর এক অসাধারণ দর্শনীয় স্থান।",
            "locationEn": pi_raw['tour_spots'][1]['location'],
            "locationBn": "কাউখালী, পিরোজপুর",
            "mapUrl": pi_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Sarengakathi Canal Landscape",
            "nameBn": "সারেঙ্গাকাঠি খালের ব্যাকওয়াটার নিসর্গ",
            "categoryEn": "Pristine Backwater Canal Network & Canoe Trails",
            "categoryBn": "মনোরম খালের ব্যাকওয়াটার ও জলজ ভ্রমণ পথ",
            "descEn": "The Sarengakathi Canal Landscape is an enchanting labyrinth of winding tidal waterways cutting through dense betel-nut groves and traditional fruit orchards. Renowned among ecotourists as part of southern Bangladesh's famous 'Backwater Venice', the canals are navigated on silent wooden dinghies that glide smoothly beneath living arches of overhanging bamboo and water-coconut palms. Visitors love visiting the nearby seasonal floating markets where boats packed with green guavas, coconuts, and hog plums (amra) trade directly on the water. The crystalline reflection of green foliage in the calm canal water and the gentle chirp of kingfishers create an unforgettable fairy-tale atmosphere. It is a world-class ecotourism haven for photographers and nature lovers.",
            "descBn": "নেছারাবাদ (স্বরূপকাঠি) উপজেলার সারেঙ্গাকাঠি খালের ব্যাকওয়াটার নিসর্গ দক্ষিণ বাংলার প্রকৃতির এক রূপকথার মতো সুন্দর রূপ ফুটিয়ে তোলে। সুপারি বাগান, গোলপাতা ও পেয়ারা বাগানের নিচ দিয়ে এঁকেবেঁকে চলে যাওয়া শান্ত খালের বুক চিরে ছোট কাঠের ডিঙি নৌকায় ভ্রমণ এক অদ্ভুত জাদুকরী রোমাঞ্চ তৈরি করে। খালের বিভিন্ন বাঁকে দেখতে পাওয়া যায় শত শত নৌকায় সাজানো ভাসমান পেয়ারা ও নারিকেলের বাজার। স্বচ্ছ জলের ওপর সবুজের প্রতিবিম্ব এবং পাখির কলকাকলি যেন এক শান্ত স্বর্গরাজ্য তৈরি করেছে। প্রাচ্যের ভেনিসের আসল রূপ ও ব্যাকওয়াটার ভ্রমণের অনাবিল আনন্দ পেতে সারেঙ্গাকাঠি এক স্বপ্নিল গন্তব্য।",
            "locationEn": pi_raw['tour_spots'][2]['location'],
            "locationBn": "পিরোজপুর সদর এলাকা, পিরোজপুর",
            "mapUrl": pi_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Mathbaria Waterways",
            "nameBn": "মঠবাড়িয়া নদী ও খালের রূপ",
            "categoryEn": "Coastal Estuary Waterways & Rural Landscapes",
            "categoryBn": "উপকূলীয় নদী মোহনা ও শান্ত গ্রামীণ নিসর্গ",
            "descEn": "The Mathbaria Waterways comprise an expansive network of interconnected coastal rivers and tidal channels that weave through the southern tip of Pirojpur toward the Sundarbans mangrove fringe. Bordered by resilient mangrove vegetation and scenic village settlements, these waterways provide a peaceful setting for boat travel and fishing. Travel enthusiasts can charter traditional wooden trawlers to explore quiet river bends where white egrets wade in mudflats and fishermen mend nets on sunny banks. The fresh, unpolluted coastal winds and vast open horizons create an atmosphere of profound relaxation. It stands as an authentic destination for experiencing the gentle rhythm of deltaic river life.",
            "descBn": "মঠবাড়িয়ার নদ-নদী ও খালের বিস্তার সুন্দরবনের সীমানা ঘেঁষে গড়ে ওঠা এক অপরূপ উপকূলীয় জলজ প্রকৃতি। নদীর দুই তীরে গড়ে ওঠা নারকেল বাগান, কেওড়া বন ও শান্ত গ্রামীণ জনপদ এক স্নিগ্ধ রূপ ধারণ করে আছে। ট্রলারে চড়ে নদীর বুক চিরে ঘুরে বেড়ানোর সময় বকের সারি ও নদীর চরে জেলেদের জাল ফেলার দৃশ্য চোখ জুড়িয়ে দেয়। সমুদ্রের কাছাকাছি হওয়ার কারণে এখানকার মৃদু লবণাক্ত বাতাস শরীরে নতুন সজীবতা এনে দেয়। কোলাহলমুক্ত শান্ত পরিবেশে নদীমাতৃক জীবনের আসল ছন্দ উপভোগ করতে মঠবাড়িয়ার এই নদীপথগুলো এক অসাধারণ স্থান।",
            "locationEn": pi_raw['tour_spots'][3]['location'],
            "locationBn": "মঠবাড়িয়া, পিরোজপুর",
            "mapUrl": pi_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Indurkani River and Canal Scenery",
            "nameBn": "ইন্দুরকানী নদী ও খালের দৃশ্যপট",
            "categoryEn": "Scenic River Confluence & Canal Pathways",
            "categoryBn": "নদী সঙ্গম, শান্ত খাল ও গ্রামীণ পলিমাটির শোভা",
            "descEn": "The Indurkani River and Canal Scenery showcases the poetic beauty of southern delta geography, where wide river confluences meet quiet inland tidal canals. Lined with graceful nipa palm (golpata) groves, coconut trees, and verdant homestead gardens, the waterways form the true lifeblood of the community. Leisurely boat excursions along the canals allow visitors to observe traditional wooden canoe carving and witness rural farmers transporting harvests directly on watercraft. At dusk, the reflection of twilight colors across the smooth river water creates magical photographic opportunities. It captures the authentic, serene spirit of rural riverine life in Pirojpur.",
            "descBn": "ইন্দুরকানীর নদী ও খালের প্রাকৃতিক দৃশ্যপট দক্ষিণ বাংলার শান্ত গ্রামীণ নদীমাতৃক রূপের এক অনন্য উদাহরণ। গোলপাতা, সুপারি ও নারিকেল গাছের ছায়াঘেরা এই খালের নেটওয়ার্ক এ অঞ্চলের মানুষের জীবনের অন্যতম প্রধান চালিকাশক্তি। ছোট নৌকায় করে খালের শান্ত বুক চিরে ঘুরে বেড়ালে গ্রামীণ মানুষের সহজ-সরল জীবনযাত্রা ও নৌকার তৈরির কাজ প্রত্যক্ষ করা যায়। গোধূলিলগ্নে নদীর শান্ত জলে সূর্যাস্তের রঙের ছটা এক অদ্ভুত মায়াবী রূপ ধারণ করে যা আলোকচিত্রীদের পরম প্রিয়। শহরের ব্যস্ততা ভুলে নিঝুম প্রকৃতির কোলে সময় কাটাতে ইন্দুরকানীর এই নদী ও খালের রূপ এক অনবদ্য আশ্রয়।",
            "locationEn": pi_raw['tour_spots'][4]['location'],
            "locationBn": "ইন্দুরকানী, পিরোজপুর",
            "mapUrl": pi_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('pirojpur', pirojpur_data)

# ==========================================
# 15. KUSHTIA
# ==========================================
k_raw = all_data['kushtia']
kushtia_data = {
    "slug": "kushtia",
    "en": "Kushtia",
    "bn": "কুষ্টিয়া",
    "hero_title_en": "Kushtia Cultural Capital, Lalon Mystic Shrine & Rabindra Kuthibari",
    "hero_title_bn": "কুষ্টিয়ার সাংস্কৃতিক রাজধানী, বাউল লালন সাঁইজির মাজার ও শিলাইদহ কুঠিবাড়ি",
    "hero_sub_en": "Fakir Lalon Shah's mystical shrine at Cheuriya, Rabindranath Tagore's Shilaidaha Kuthibari, and the meandering Gorai riverbanks.",
    "hero_sub_bn": "ছেউড়িয়ায় বাউল সম্রাট লালন শাহের পুণ্য মাজার, বিশ্বকবি রবীন্দ্রনাথের শিলাইদহ কুঠিবাড়ি ও গড়াই নদীতীরের স্নিগ্ধ প্রকৃতি।",
    "tagline_en": "The undisputed cultural and spiritual capital of Bangladesh, immortalized by mystic philosopher Fakir Lalon Shah, Nobel laureate Rabindranath Tagore, and the historic Gorai River.",
    "tagline_bn": "বাংলাদেশের সাংস্কৃতিক রাজধানী ও আধ্যাত্মিক প্রাণকেন্দ্র, যা বাউল সম্রাট ফকির লালন শাহের ছেউড়িয়া আখড়া, বিশ্বকবি রবীন্দ্রনাথ ঠাকুরের শিলাইদহ কুঠিবাড়ি, মীর মশাররফ হোসেনের স্মৃতি ও তিলের খাজার জন্য বিশ্বখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/kushtia/carousel-1.webp",
            "titleEn": "Lalon Shah Shrine Mystic Baul Sanctuary",
            "titleBn": "বাউল সম্রাট ফকির লালন শাহের পবিত্র মাজার",
            "subtitleEn": "Sacred spiritual complex in Cheuriya where baul bards congregate to sing songs of humanism and divine love",
            "subtitleBn": "ছেউড়িয়ার পুণ্যধাম যেখানে একতারা ও দোতারার সুরে মানবপ্রেম ও সুফি বাউল দর্শনের অমর বাণী অনুরণিত হয়"
        },
        {
            "id": 2,
            "image": "images/districts/kushtia/carousel-2.webp",
            "titleEn": "Shilaidaha Rabindra Kuthibari Historic Residence",
            "titleBn": "শিলাইদহ রবীন্দ্র কুঠিবাড়ির রাজকীয় রূপ",
            "subtitleEn": "Colonial country mansion in Kumarkhali where Rabindranath Tagore penned his Nobel-winning Gitanjali poems",
            "subtitleBn": "পদ্মাপাড়ে বিশ্বকবি রবীন্দ্রনাথ ঠাকুরের পৈতৃক বাসভবন যেখানে বসে রচিত হয়েছিল কালজয়ী গীতাঞ্জলির অমর কবিতা"
        },
        {
            "id": 3,
            "image": "images/districts/kushtia/carousel-3.webp",
            "titleEn": "Gorai Riverbank Scenic Embankment Promenade",
            "titleBn": "গড়াই নদীতীরের মনোরম ওয়াকওয়ে ও সূর্যাস্ত",
            "subtitleEn": "Meandering river promenade in Kushtia town famous for gentle breezes, wooden boats, and sunset reflections",
            "subtitleBn": "কুষ্টিয়া শহর ঘেঁষে প্রবাহিত গড়াই নদীর পাড় যা ভ্রমণপিপাসুদের উপহার দেয় মুক্ত হাওয়া ও অপূর্ব গোধূলির দৃশ্য"
        },
        {
            "id": 4,
            "image": "images/districts/kushtia/carousel-4.webp",
            "titleEn": "Jhaudia Shahi Mosque Mughal Architectural Splendor",
            "titleBn": "ঝাউদিয়া শাহী মসজিদের প্রাচীন মুঘল স্থাপত্য",
            "subtitleEn": "18th-century three-domed brick monument adorned with delicate terracotta and arched entryways",
            "subtitleBn": "কুষ্টিয়া সদরের ঝাউদিয়ায় অবস্থিত মুঘল আমলের ঐতিহ্যবাহী তিন গম্বুজ মসজিদ যা শিল্পনৈপুণ্যে অনন্য"
        },
        {
            "id": 5,
            "image": "images/districts/kushtia/carousel-5.webp",
            "titleEn": "Mir Mosharraf Hossain Memorial Historic Complex",
            "titleBn": "মীর মশাররফ হোসেন স্মৃতি কমপ্লেক্স",
            "subtitleEn": "Birthplace and memorial of the author of Bishad Shindhu in Lahini Para celebrating pioneering Bengali literature",
            "subtitleBn": "লাহিনীপাড়ায় অবস্থিত 'বিষাদ সিন্ধু' রচয়িতা কালজয়ী সাহিত্যিক মীর মশাররফ হোসেনের স্মৃতিধন্য সংগ্রহশালা"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Shilaidaha Rabindra Kuthibari",
            "nameBn": "শিলাইদহ রবীন্দ্র কুঠিবাড়ি",
            "categoryEn": "National Literary Heritage Palace & Museum",
            "categoryBn": "বিশ্বকবির ঐতিহাসিক বাসভবন ও জাতীয় স্মৃতি জাদুঘর",
            "descEn": "Shilaidaha Rabindra Kuthibari in Kumarkhali Upazila is one of the most hallowed literary heritage shrines in South Asia, serving as the country residence of Nobel laureate Rabindranath Tagore during the most productive decade of his creative life (1890–1901). Set within a scenic estate near the Padma River, the three-story pyramid-roofed mansion was designed with classical colonial porticos, wooden shuttered verandas, and panoramic rooftop balconies. Here, enveloped by the tranquility of rural Bengal, Tagore composed masterpieces of poetry, short stories, and foundational translations of 'Gitanjali' that won the 1913 Nobel Prize in Literature. The house has been preserved as a museum housing his personal bed, desk, typewriter, family palanquins, and historic photographs. The lush garden paths, lotus ponds, and ancient trees inspire millions of literary pilgrims who visit annually.",
            "descBn": "কুমারখালী উপজেলার শিলাইদহে পদ্মা নদীর তীরে অবস্থিত রবীন্দ্র কুঠিবাড়ি বিশ্ব সাহিত্যের এক পরম পবিত্র স্মৃতিধাম, যেখানে বিশ্বকবি রবীন্দ্রনাথ ঠাকুর তাঁর জীবনের অন্যতম শ্রেষ্ঠ সৃজনশীল সময় (১৮৯০–১৯০১) অতিবাহিত করেছিলেন। পিরামিড আকৃতির ছাদবিশিষ্ট সুরম্য তিনতলা এই ঐতিহাসিক ভবনে রয়েছে সুপরিসর বারান্দা, কাঠের কারুকাজ এবং কবিগুরুর স্মৃতিবিজড়িত কক্ষ। এই কুঠিবাড়িতে বসেই রবীন্দ্রনাথ তাঁর বিখ্যাত 'গীতাঞ্জলি' কাব্যের বহু কবিতা, কালজয়ী ছোটগল্প এবং 'সোনার তরী' রচনা করেছিলেন যা তাঁকে ১৯১৩ সালে নোবেল পুরস্কার এনে দেয়। ভবনটি বর্তমানে একটি সমৃদ্ধ জাদুঘর যেখানে কবির ব্যবহৃত খাট, লেখার টেবিল, পদ্মা বোটের স্মারক ও দুর্লভ আলোকচিত্র সংরক্ষিত আছে। সাহিত্যপ্রেমীদের জন্য শিলাইদহ কুঠিবাড়ি এক পরম তীর্থক্ষেত্র।",
            "locationEn": k_raw['hist_spots'][0]['location'],
            "locationBn": "শিলাইদহ, কুমারখালী, কুষ্টিয়া",
            "mapUrl": k_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Lalon Shah Shrine",
            "nameBn": "বাউল সম্রাট লালন শাহের মাজার",
            "categoryEn": "World Mystic Spiritual Shrine & Baul Academy",
            "categoryBn": "বিশ্ববিখ্যাত সুফি বাউল দরবার ও স্মৃতি কমপ্লেক্স",
            "descEn": "The Lalon Shah Shrine in Cheuriya, Kushtia Sadar, is the globally renowned spiritual resting place of Fakir Lalon Shah (1774–1890), the towering mystic philosopher, composer, and father of Bengal's Baul tradition. Preaching universal humanism, freedom from religious dogma, and divine love within the human body through over a thousand immortal Baul songs, Lalon's philosophy influenced icons from Rabindranath Tagore to Allen Ginsberg. The shrine complex features an elegant white marble domed mausoleum, research academy, and open-air musical amphitheaters surrounded by serene gardens. Thousands of wandering Baul singers, dressed in saffron robes and playing ek tara and do tara instruments, congregate here during annual commemorative festivals to sing throughout the night. It is an internationally vital sanctuary of spiritual tolerance, humanist philosophy, and folk music.",
            "descBn": "কুষ্টিয়া সদর উপজেলার ছেউড়িয়ায় অবস্থিত লালন শাহের মাজার বিশ্ববিখ্যাত সুফি সাধক, মরমি কবি ও বাউল গানের সম্রাট ফকির লালন শাহের (১৭৭৪–১৮৯০) পবিত্র সমাধিস্থল। জাত-পাত ও ধর্মীয় গোঁড়ামির ঊর্ধ্বে উঠে মানবতার জয়গান গাওয়া লালন সাঁইজির অমর গান বিশ্বজুড়ে দর্শনের নতুন দিগন্ত উন্মোচন করেছে। শুভ্র মার্বেল পাথরে নির্মিত সুন্দর সমাধি সৌধ, লালন একাডেমি জাদুঘর এবং উন্মুক্ত সঙ্গীতমঞ্চ নিয়ে এই প্রাঙ্গণটি গড়ে উঠেছে। প্রতি বছর দোল পূর্ণিমা ও লালন তিরোধান দিবসে দেশ-বিদেশের লাখ লাখ বাউল, সাধু ও দর্শনার্থী এখানে সমবেত হন এবং একতারা-দোতারার সুরে রাতভর লালনগীতি পরিবেশন করেন। অহিংসা, মানবতাবাদ ও আত্মশুদ্ধির এক অনন্ত বিশ্বতীর্থ এই ছেউড়িয়া আখড়া।",
            "locationEn": k_raw['hist_spots'][1]['location'],
            "locationBn": "ছেউড়িয়া, কুষ্টিয়া সদর, কুষ্টিয়া",
            "mapUrl": k_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Jhaudia Shahi Mosque",
            "nameBn": "ঝাউদিয়া শাহী মসজিদ",
            "categoryEn": "Mughal Imperial Architecture",
            "categoryBn": "মুঘল আমলের ঐতিহ্যবাহী শাহী মসজিদ",
            "descEn": "Constructed in the early eighteenth century during the reign of Mughal Emperor Aurangzeb by Adalat Khan, Jhaudia Shahi Mosque in Kushtia Sadar is a magnificent historic monument of pre-colonial Bengal. Erected on an elevated brick plinth, the triple-domed sanctuary features thick lime-surki walls, four slender corner minarets, and three pointed-arch entrance doorways embellished with delicate floral stucco reliefs. The central bulbous dome rises majestically above the companion domes, creating a balanced silhouette that dominates the village skyline. Inside, the quiet prayer hall features deeply carved mihrabs and cool natural ventilation that enhances the spiritual atmosphere. Surrounded by tranquil rural homesteads and an ancient dighi, Jhaudia Shahi Mosque remains an active house of prayer and a prized architectural landmark.",
            "descBn": "কুষ্টিয়া সদর উপজেলার ঝাউদিয়া গ্রামে অবস্থিত ঝাউদিয়া শাহী মসজিদ মুঘল সম্রাট আওরঙ্গজেবের শাসনামলে অষ্টাদশ শতাব্দীর শুরুতে নির্মিত এক অনন্য ঐতিহাসিক উপাসনালয়। একটি উঁচু চত্বরের ওপর প্রতিষ্ঠিত তিন গম্বুজ বিশিষ্ট এই মসজিদের চার কোণে চারটি সুদৃশ্য মিনার এবং সম্মুখভাগে তিনটি খিলানযুক্ত প্রবেশপথ রয়েছে। চুন-সুরকির পুরু গাঁথুনি এবং বহির্দেয়ালে পোড়ামাটির লতাপাতার কারুকাজ মুঘল স্থাপত্যের আভিজাত্য প্রকাশ করে। মসজিদের ভেতরের মার্জিত মেহরাব ও শান্তিময় পরিবেশ শতাব্দী ধরে মুসল্লিদের আধ্যাত্মিক প্রশান্তি জুগিয়ে আসছে। চারপাশের গ্রামীণ সবুজ ও প্রাচীন পুকুরের পাড়ে অবস্থিত এই প্রাচীন মসজিদটি কুষ্টিয়ার ইসলামিক ঐতিহ্যের এক পরম অহংকার।",
            "locationEn": k_raw['hist_spots'][2]['location'],
            "locationBn": "ঝাউদিয়া, কুষ্টিয়া সদর, কুষ্টিয়া",
            "mapUrl": k_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Kushtia Collectorate Building",
            "nameBn": "কুষ্টিয়া কালেক্টরেট ভবন",
            "categoryEn": "Colonial Administrative Heritage Architecture",
            "categoryBn": "উপনিবেশিক প্রশাসনিক স্থাপত্য ও ঐতিহ্য ভবন",
            "descEn": "The Kushtia Collectorate Building in the heart of Kushtia town is a stately nineteenth-century administrative edifice established when Kushtia flourished as a major British industrial and railway district headquarters. Built in the classic Indo-Saracenic and Victorian colonial style, the massive two-story red-brick structure features high vaulted verandas, arched colonnades, grand central porticos, and decorative timber eaves. The building served as the seat of local governance through monumental historical events, including the Indigo Rebellions, the partition of Bengal, and the 1971 War of Liberation. Shaded by ancient centenary mahogany and banyan trees, the historic campus evokes the administrative grandeur of colonial Bengal. It stands as an important civic and architectural monument anchoring the town's history.",
            "descBn": "কুষ্টিয়া শহরের প্রাণকেন্দ্রে অবস্থিত কালেক্টরেট ভবন উনিশ শতকের ব্রিটিশ ঔপনিবেশিক প্রশাসনিক স্থাপত্যের এক চমৎকার ও ঐতিহাসিক নিদর্শন। লাল ইটের তৈরি বিশালাকার এই দোতলা ভবনে রয়েছে সুউচ্চ খিলানযুক্ত বারান্দা, প্রাচীন কাঠের সিঁড়ি এবং ভিক্টোরীয় নির্মাণরীতির অনন্য আভিজাত্য। এই ভবন থেকেই এককালে নীল বিদ্রোহ দমন, রেলওয়ে সম্প্রসারণ এবং স্থানীয় শাসনব্যবস্থা পরিচালিত হতো। ১৯৭১ সালের মহান মুক্তিযুদ্ধেও এই চত্বরের রয়েছে ঐতিহাসিক ভূমিকা। শতাব্দীপ্রাচীন মেহগনি গাছের ছায়ায় ঘেরা এই সুপ্রাচীন প্রশাসনিক ভবনটি কুষ্টিয়া শহরের ঐতিহ্য ও নাগরিক ইতিহাসের এক গৌরবময় স্মারক।",
            "locationEn": k_raw['hist_spots'][3]['location'],
            "locationBn": "কুষ্টিয়া শহর, কুষ্টিয়া",
            "mapUrl": k_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Mir Mosharraf Hossain Memorial Complex",
            "nameBn": "মীর মশাররফ হোসেন স্মৃতি কমপ্লেক্স",
            "categoryEn": "National Literary Memorial & Research Center",
            "categoryBn": "জাতীয় সাহিত্যিক স্মৃতিকেন্দ্র ও জাদুঘর",
            "descEn": "Located in Lahini Para of Kushtia Sadar, the Mir Mosharraf Hossain Memorial Complex honors the birthplace and legacy of Mir Mosharraf Hossain (1847–1912), the pioneering titan of modern Bengali prose literature and author of the immortal epic novel 'Bishad Shindhu'. The memorial complex encompasses his ancestral homestead grounds, a dedicated cultural museum, an auditorium, and a research library preserving first editions of his revolutionary novels and theatrical plays. Exhibits display personal memorabilia, original letters, and historical dioramas tracing his foundational role in modern Muslim Bengali literary renaissance. Set within quiet rural gardens, the complex attracts scholars, students, and literature lovers from across Bengal. It stands as an essential pilgrimage stop honoring the literary pioneers who shaped the Bengali language.",
            "descBn": "কুষ্টিয়া সদর উপজেলার লাহিনীপাড়ায় অবস্থিত মীর মশাররফ হোসেন স্মৃতি কমপ্লেক্স আধুনিক বাংলা গদ্য সাহিত্যের পথিকৃৎ এবং কালজয়ী মহাকাব্যিক উপন্যাস 'বিষাদ সিন্ধু'র রচয়িতা মীর মশাররফ হোসেনের (১৮৪৭–১৯১২) পৈতৃক জন্মভিটা। বাংলা সাহিত্যের প্রথম আধুনিক মুসলিম ঔপন্যাসিক ও নাট্যকারের স্মৃতি রক্ষার্থে এখানে গড়ে তোলা হয়েছে একটি সমৃদ্ধ জাদুঘর, গবেষণা গ্রন্থাগার ও মুক্তমঞ্চ। জাদুঘরে কবির ব্যবহৃত নিদর্শন, পাণ্ডুলিপির অনুলিপি এবং তৎকালীন ঐতিহাসিক সাহিত্যকর্ম সংরক্ষিত আছে। সবুজ পল্লী প্রকৃতির মাঝে শান্ত পরিবেশে গড়ে ওঠা এই স্মৃতিকেন্দ্রটি বাংলা সাহিত্যের ইতিহাস ও মুসলিম নবজাগরণের এক অনন্য অনুপ্রেরণাদায়ী স্থান।",
            "locationEn": k_raw['hist_spots'][4]['location'],
            "locationBn": "লাহিনী পাড়া, কুষ্টিয়া সদর, কুষ্টিয়া",
            "mapUrl": k_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Gorai Riverbank",
            "nameBn": "গড়াই নদীতীর",
            "categoryEn": "Scenic Urban Waterfront & Sunset Promenade",
            "categoryBn": "মনোরম নদীতীর, স্নিগ্ধ বাঁধ ও সূর্যাস্ত ভিউপয়েন্ট",
            "descEn": "The Gorai Riverbank, winding gracefully alongside Kushtia town, is the beloved recreational and scenic promenade of the cultural capital. Originating as a principal distributary of the Padma River, the Gorai flows with gentle currents between sandy banks and green groves. The municipal riverfront features paved walking boulevards, illuminated evening street lamps, and garden benches where residents and tourists gather to enjoy refreshing breezes. Traditional wooden boats offer gentle rides on the water, while waterfront cafes serve steaming tea, local street snacks, and Kushtia's famous sesame candy (Tiler Khaja). In the evening, the sun sets directly across the river, casting glowing crimson reflections across the water in a breathtaking display. It is the premier gathering spot for leisure in Kushtia.",
            "descBn": "কুষ্টিয়া শহরের কোল ঘেঁষে বয়ে যাওয়া গড়াই নদীতীর স্থানীয় নাগরিক ও ভ্রমণপিপাসুদের সবচেয়ে প্রিয় বিনোদন ও মুক্ত হাওয়া উপভোগের স্থান। পদ্মার অন্যতম প্রধান এই শাখানদীর তীরে গড়ে তোলা সুন্দর বাঁধ ও ওয়াকওয়ে ধরে হাঁটলে শরীর-মন জুড়িয়ে যায়। নদীর বুকে ছোট ছোট কাঠের নৌকায় চড়ে ঘুরে বেড়ানো এবং শান্ত জলে সূর্যাস্তের রক্তিম প্রতিফলন দেখা এক অপূর্ব অভিজ্ঞতা। নদীতীরের চায়ের স্টলগুলোতে বসে গরম চা এবং কুষ্টিয়ার বিখ্যাত ও মচমচে 'তিলের খাজা' খাওয়ার আনন্দ তুলনাহীন। বিকেলে বন্ধুদের সাথে আড্ডা দেওয়া কিংবা নদীর রূপ উপভোগে গড়াই নদীতীর এক চমৎকার গন্তব্য।",
            "locationEn": k_raw['tour_spots'][0]['location'],
            "locationBn": "কুষ্টিয়া শহর ও সংলগ্ন এলাকা, কুষ্টিয়া",
            "mapUrl": k_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Shilaidaha Riverfront",
            "nameBn": "শিলাইদহ পদ্মাপাড়",
            "categoryEn": "Poetic Riverfront Vista & Tagore Heritage Beach",
            "categoryBn": "কবির স্মৃতিবিজড়িত পদ্মাপাড় ও স্নিগ্ধ বালুচর",
            "descEn": "The Shilaidaha Riverfront on the banks of the mighty Padma River in Kumarkhali is a poignantly poetic landscape steeped in the memories of Rabindranath Tagore, who spent countless hours floating on his beloved houseboat 'Padma' while composing immortal songs. The riverfront features expansive sandy beaches, gently lapping waves, and unobstructed views of vast waters stretching to distant horizon tree lines. Travelers can hire traditional wooden rowboats to drift peacefully along the currents where Tagore found creative solace more than a century ago. During autumn, white kashful reeds sway across the river flats beneath azure skies, creating an ethereal setting. It provides an inspiring pilgrimage where nature and literature merge into timeless beauty.",
            "descBn": "কুমারখালীর শিলাইদহে পদ্মা নদীর পাড় প্রকৃতির এক পরম কাব্যিক ও মায়াবী বিস্তার, যেখানে বসে বিশ্বকবি রবীন্দ্রনাথ ঠাকুর তাঁর বিখ্যাত 'পদ্মা বোট'-এ চড়ে ভেসে বেড়াতেন এবং অমর গান ও কবিতা রচনা করতেন। পদ্মার দিগন্তজোড়া জলরাশি, বালুচর এবং শান্ত বাতাস যে কোনো মানুষকে কবির মতো ভাবুক করে তোলে। কাঠের নৌকায় চড়ে নদীর বুক চিরে ভেসে বেড়ানো এবং শতবর্ষ আগে কবিগুরুর দেখা প্রকৃতির রূপ অনুভব করা এক অভূতপূর্ব অভিজ্ঞতা। শরৎকালে পদ্মার চরে ফোটা ধবধবে সাদা কাশফুলের সমারোহ এই নদীতীরকে আরও স্বপ্নিল করে তোলে। সাহিত্যপ্রেমী ও প্রকৃতিপ্রেমীদের জন্য এই পদ্মাপাড় এক চিরন্তন ভালোলাগার স্থান।",
            "locationEn": k_raw['tour_spots'][1]['location'],
            "locationBn": "শিলাইদহ, কুমারখালী, কুষ্টিয়া",
            "mapUrl": k_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Lalon Shah Mela Grounds",
            "nameBn": "লালন শাহ মেলা প্রাঙ্গণ",
            "categoryEn": "World Baul Music Festival & Cultural Fairgrounds",
            "categoryBn": "ঐতিহাসিক লালন স্মরণোৎসব ও বাউল মেলা চত্বর",
            "descEn": "The Lalon Shah Mela Grounds in Cheuriya host the world-famous annual festivals dedicated to Fakir Lalon Shah, most prominently the Lalon Smaranotsab during Dol Purnima in spring and the Lalon Tirodhan Dibas in October. Covering expansive open-air fairgrounds adjacent to the sacred shrine, the grounds transform into an electrifying spiritual and musical city where hundreds of thousands of baul bards, philosophers, and travelers gather. Temporary stages, acoustic musical huts, and fairground stalls create a 24-hour festival atmosphere filled with the sound of ektaras, dotaras, and mystic vocal harmonies. Traditional village fairs feature regional handicrafts, wooden musical instruments, local sweets, and handmade baul robes. Experiencing the spiritual music under the moonlit sky here is an unforgettable, soul-stirring cultural highlight of Bengal.",
            "descBn": "ছেউড়িয়ার লালন মাজার সংলগ্ন মেলা প্রাঙ্গণটি বিশ্বখ্যাত 'লালন স্মরণোৎসব' ও 'তিরোধান দিবস' উপলক্ষে আয়োজিত বাউল মেলার প্রধান কেন্দ্র। প্রতি বছর দোল পূর্ণিমা ও অক্টোবর মাসে আয়োজিত এই মেলায় দেশ-বিদেশের লাখ লাখ মানুষ, সাধু-বাউল ও গবেষক সমবেত হন। মেলা প্রাঙ্গণের বিভিন্ন আখড়ায় রাতভর চলে একতারা, দোতারা ও বায়া বাজিয়ে লালনের গান গাওয়ার আসর যা পুরো পরিবেশকে এক অপার্থিব আধ্যাত্মিকতায় ভরিয়ে তোলে। মেলায় পাওয়া যায় ঐতিহ্যবাহী বাউল বাদ্যযন্ত্র, হস্তশিল্প সামগ্রী ও গ্রামীণ মিষ্টি। বাংলার অমর বাউল সংস্কৃতি ও দর্শনের সরাসরি সান্নিধ্য পেতে এই মেলা প্রাঙ্গণ এক অনন্য মহাতীর্থ।",
            "locationEn": k_raw['tour_spots'][2]['location'],
            "locationBn": "ছেউড়িয়া, কুষ্টিয়া",
            "mapUrl": k_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Kushtia Municipal Park",
            "nameBn": "কুষ্টিয়া পৌর পার্ক",
            "categoryEn": "Civic Lake Promenade & Urban Green Sanctuary",
            "categoryBn": "পৌর পার্ক, মনোরম লেক ও পারিবারিক বিনোদন কেন্দ্র",
            "descEn": "Situated in the central urban area of Kushtia town, the Municipal Park serves as the premier green recreational oasis for residents and travelers. Centered around a tranquil heritage lake, the park features paved jogging boulevards, colorful seasonal flower beds, shaded gazebos, and illuminated night fountains. Children enjoy well-equipped playground equipment and pedal-boat rides on the calm lake waters, while families stroll along the water's edge under mature canopy trees. Street vendors outside the gates sell authentic local delicacies, including the famed hot jilapi, roasted peanuts, and spicy street foods. It provides a welcoming, family-friendly urban leisure oasis right within the city.",
            "descBn": "কুষ্টিয়া শহরের কেন্দ্রস্থলে অবস্থিত পৌর পার্ক স্থানীয় নাগরিক ও দর্শনার্থীদের জন্য এক চমৎকার মুক্ত বিনোদন কেন্দ্র। সুন্দর একটি শান্ত লেক ঘিরে গড়ে ওঠা এই পার্কে রয়েছে পাকা হাঁটার রাস্তা, ফুলের বাগান, ফোয়ারা এবং ছায়াঘেরা বসার বেঞ্চ। লেকের জলে প্যাডেল বোট চালানো এবং শিশুদের জন্য খেলার সুন্দর রাইডস পার্কটিকে মুখরিত রাখে। বিকেলে ও সন্ধ্যায় মুক্ত বাতাস উপভোগ করতে এবং পরিবার নিয়ে অবসর কাটাতে প্রচুর মানুষ এখানে সমবেত হন। পার্কের বাইরে পাওয়া যায় গরম গরম জিলাপি, চটপটি ও মুখরোচক খাবার। শহরের কোলাহল ছেড়ে স্বস্তিতে কিছুটা সময় কাটাতে এই পৌর পার্কটি অত্যন্ত চমৎকার।",
            "locationEn": k_raw['tour_spots'][3]['location'],
            "locationBn": "কুষ্টিয়া শহর, কুষ্টিয়া",
            "mapUrl": k_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Kumarkhali Heritage Town",
            "nameBn": "কুমারখালী ঐতিহ্যবাহী শহর",
            "categoryEn": "Historic Handloom Capital & Literary Pioneer Town",
            "categoryBn": "ঐতিহাসিক তাঁত শিল্পের রাজধানী ও সাংবাদিকতার সূতিকাগার",
            "descEn": "Kumarkhali is an illustrious historic town nestled along the Gorai River, celebrated across the subcontinent as the historic cradle of pioneering Bengali journalism and handloom textile arts. Here, Kangal Harinath Majumdar founded the fearless historic newspaper 'Gram Barta Prakashika' in the late nineteenth century using his antique hand-operated printing press (MN Press). The town is internationally renowned for producing exquisite traditional cotton handloom fabrics, bedsheets, lungis, and sarees woven by skilled master weavers. Walking through the quiet historic quarters, visitors can inspect the historic printing press, tour active handloom weaving colonies, and taste authentic regional sweets. It represents a living museum of rural intellectual courage and refined textile craftsmanship.",
            "descBn": "কুমারখালী গড়াই নদীর তীরে অবস্থিত এক গৌরবোজ্জ্বল ঐতিহাসিক শহর, যা বাংলা সাংবাদিকতার অগ্রদূত কাঙ্গাল হরিনাথ মজুমদার এবং বিশ্বখ্যাত ঐতিহ্যবাহী তাঁতশিল্পের সূতিকাগার হিসেবে খ্যাত। উনিশ শতকে এই শহরেই প্রতিষ্ঠিত হয়েছিল কাঙ্গাল হরিনাথের ঐতিহাসিক 'এম এন প্রেস' এবং প্রকাশিত হয়েছিল নির্ভীক সংবাদপত্র 'গ্রামবার্তা প্রকাশিকা'। এছাড়া কুমারখালীর ঐতিহ্যবাহী তাঁতে বোনা সুতি বিছানার চাদর, লুঙ্গি ও শাড়ি দেশ-বিদেশে ব্যাপকভাবে সমাদৃত। শহরের প্রাচীন অলিগলিতে ঘুরলে তাঁতীদের নিপুণ হাতের কাজ প্রত্যক্ষ করা যায় এবং প্রাচীন মুদ্রণযন্ত্রের ইতিহাস জানা যায়। জ্ঞানচর্চা, নির্ভীক সাংবাদিকতা ও ঐতিহ্যবাহী তাঁতশিল্পের এক অনন্য জীবন্ত স্মারক এই কুমারখালী শহর।",
            "locationEn": k_raw['tour_spots'][4]['location'],
            "locationBn": "কুমারখালী, কুষ্টিয়া",
            "mapUrl": k_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('kushtia', kushtia_data)
