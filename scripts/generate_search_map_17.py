# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/curated_all_64.json', 'r', encoding='utf-8') as f:
    master_64 = json.load(f)

districts_17 = [
    'magura', 'narail', 'naogaon', 'satkhira', 'khagrachhari',
    'joypurhat', 'sunamganj', 'gaibandha', 'rangpur', 'rangamati',
    'chapainawabganj', 'bandarban', 'barguna', 'lalmonirhat',
    'nilphamari', 'thakurgaon', 'panchagarh'
]

# Specific search query overrides for higher accuracy
SEARCH_OVERRIDES = {
    "magura": {
        "hero": ["Magura District", "মাগুরা জেলা", "Magura, Bangladesh"],
        "carousel-1": ["Sitaram Ray", "রাজা সীতারাম রায়", "Mohammadpur Upazila"],
        "carousel-2": ["Siddheshwari Kali Temple", "মাগুরা", "Siddheshwari Math"],
        "carousel-3": ["Nabaganga River", "নবগঙ্গা নদী", "Magura"],
        "carousel-4": ["Madhumati River", "মধুমতী নদী", "Magura"],
        "carousel-5": ["Ghoranach Mandir", "Mohammadpur, Magura", "Magura District"],
        "hist-1": ["Sitaram Ray", "রাজা সীতারাম রায়", "Mohammadpur Upazila, Magura"],
        "hist-2": ["Siddheshwari Kali Temple", "সিদ্ধেশ্বরী কালী মন্দির", "Magura District"],
        "hist-3": ["Mohammadpur Upazila", "মোহাম্মদপুর উপজেলা (মাগুরা)", "Magura District"],
        "hist-4": ["Nilkuthi", "নীলকুঠি", "Magura District"],
        "hist-5": ["Sreepur Upazila, Magura", "শ্রীপুর উপজেলা, মাগুরা", "Magura District"],
        "tour-1": ["Nabaganga River", "নবগঙ্গা নদী", "Magura"],
        "tour-2": ["Madhumati River", "মধুমতী নদী", "Mohammadpur Upazila"],
        "tour-3": ["Mohammadpur Upazila", "Sitaram Ray", "Magura"],
        "tour-4": ["Sreepur Upazila, Magura", "শ্রীপুর উপজেলা", "Magura"],
        "tour-5": ["Magura District", "মাগুরা জেলা", "Rural Bangladesh"]
    },
    "narail": {
        "hero": ["SM Sultan", "এস এম সুলতান", "Narail District"],
        "carousel-1": ["SM Sultan", "এস এম সুলতান", "Narail"],
        "carousel-2": ["Chitra River", "চিত্রা নদী", "Narail"],
        "carousel-3": ["Victoria Collegiate School", "নড়াইল ভিক্টোরিয়া কলেজ", "Narail"],
        "carousel-4": ["SM Sultan Shishuswargo", "শিশুস্বর্গ", "Narail"],
        "carousel-5": ["Lohagara Upazila, Narail", "লোহাগড়া উপজেলা", "Narail District"],
        "hist-1": ["SM Sultan", "এস এম সুলতান", "Narail"],
        "hist-2": ["Narail Victoria Collegiate School", "ভিক্টোরিয়া কলেজিয়েট স্কুল", "Narail"],
        "hist-3": ["Lohagara Upazila, Narail", "লোহাগড়া", "Narail District"],
        "hist-4": ["SM Sultan", "Chitra River", "Narail"],
        "hist-5": ["Lohagara Upazila, Narail", "লোহাগড়া", "Narail District"],
        "tour-1": ["Chitra River", "চিত্রা নদী", "Narail"],
        "tour-2": ["SM Sultan", "শিশুস্বর্গ", "Narail"],
        "tour-3": ["Lohagara Upazila, Narail", "নড়াইল জেলা", "Narail"],
        "tour-4": ["Kalia Upazila", "কালিয়া উপজেলা", "Narail District"],
        "tour-5": ["Chitra River", "Narail town", "নড়াইল"]
    },
    "naogaon": {
        "hero": ["Somapura Mahavihara", "সোমপুর মহাবিহার", "Naogaon District"],
        "carousel-1": ["Somapura Mahavihara", "সোমপুর মহাবিহার", "Paharpur, Naogaon"],
        "carousel-2": ["Kusumba Mosque", "কুসুম্বা মসজিদ", "Manda Upazila"],
        "carousel-3": ["Dubalhati Rajbari", "দুবলহাটি রাজবাড়ি", "Naogaon"],
        "carousel-4": ["Alta Dighi National Park", "আলতাদীঘি জাতীয় উদ্যান", "Dhamoirhat"],
        "carousel-5": ["Balihar Rajbari", "বলিহার রাজবাড়ি", "Naogaon"],
        "hist-1": ["Somapura Mahavihara", "সোমপুর মহাবিহার", "Paharpur"],
        "hist-2": ["Kusumba Mosque", "কুসুম্বা মসজিদ", "Manda, Naogaon"],
        "hist-3": ["Dubalhati Rajbari", "দুবলহাটি রাজবাড়ি", "Naogaon"],
        "hist-4": ["Balihar Rajbari", "বলিহার রাজবাড়ি", "Naogaon"],
        "hist-5": ["Somapura Mahavihara Museum", "পাহাড়পুর প্রত্নতাত্ত্বিক জাদুঘর", "Naogaon"],
        "tour-1": ["Somapura Mahavihara", "সোমপুর মহাবিহার", "Paharpur"],
        "tour-2": ["Kusumba Mosque", "কুসুম্বা মসজিদ দিঘি", "Manda Upazila"],
        "tour-3": ["Alta Dighi National Park", "আলতাদীঘি জাতীয় উদ্যান", "Dhamoirhat"],
        "tour-4": ["Atrai River", "আত্রাই নদী", "Naogaon"],
        "tour-5": ["Jabai Beel", "জাবাই বিল", "Sapahar, Naogaon"]
    },
    "satkhira": {
        "hero": ["Sundarbans", "সুন্দরবন", "Satkhira District"],
        "carousel-1": ["Sundarbans West Wildlife Sanctuary", "সুন্দরবন", "Satkhira"],
        "carousel-2": ["Jesoreshwari Kali Temple", "যশোরেশ্বরী কালী মন্দির", "Ishwaripur"],
        "carousel-3": ["Tetulia Jami Mosque", "তেঁতুলিয়া জামে মসজিদ", "Tala Upazila"],
        "carousel-4": ["Mandarbari Beach", "মান্দারবাড়িয়া সমুদ্র সৈকত", "Satkhira"],
        "carousel-5": ["Kalindi River", "কালিন্দী নদী", "Shyamnagar, Satkhira"],
        "hist-1": ["Jesoreshwari Kali Temple", "যশোরেশ্বরী কালী মন্দির", "Ishwaripur, Shyamnagar"],
        "hist-2": ["Jesoreshwari Kali Temple", "যশোরেশ্বরী কালী মন্দির", "Shyamnagar"],
        "hist-3": ["Tetulia Jami Mosque", "তেঁতুলিয়া জামে মসজিদ", "Tala, Satkhira"],
        "hist-4": ["Satkhira District", "সাতক্ষীরা জেলা", "Labsa, Satkhira"],
        "hist-5": ["Pratapaditya", "প্রতাপাদিত্য", "Dhumghat, Shyamnagar"],
        "tour-1": ["Sundarbans", "সুন্দরবন", "Satkhira"],
        "tour-2": ["Mandarbari Beach", "সুন্দরবন সমুদ্র সৈকত", "Satkhira"],
        "tour-3": ["Raimangal River", "রায়মঙ্গল নদী", "Kalindi River"],
        "tour-4": ["Sundarbans mangrove", "সুন্দরবন ম্যানগ্রোভ", "Shyamnagar"],
        "tour-5": ["Debhata Upazila", "দেবহাটা উপজেলা", "Ichamati River, Debhata"]
    },
    "khagrachhari": {
        "hero": ["Alutila Cave", "আলুটিলা গুহা", "Khagrachhari District"],
        "carousel-1": ["Alutila Cave", "আলুটিলা গুহা", "Matiranga"],
        "carousel-2": ["Risang Waterfall", "রিসাং ঝর্ণা", "Khagrachhari"],
        "carousel-3": ["Tareng", "তারেং", "Khagrachhari"],
        "carousel-4": ["Hajachhari Waterfall", "হাজাচড়া ঝর্ণা", "Dighinala"],
        "carousel-5": ["Mayabini Lake", "মায়াবিনী লেক", "Panchhari"],
        "hist-1": ["Manikchhari Upazila", "মানিকছড়ি", "Mong Circle"],
        "hist-2": ["Khagrachhari District", "বৌদ্ধ বিহার খাগড়াছড়ি", "Buddhist temple"],
        "hist-3": ["Alutila Cave", "আলুটিলা গুহা", "Matiranga, Khagrachhari"],
        "hist-4": ["Ramgarh Upazila", "রামগড় উপজেলা", "Khagrachhari"],
        "hist-5": ["Dighinala Upazila", "দীঘিনালা উপজেলা", "Khagrachhari"],
        "tour-1": ["Alutila Cave", "আলুটিলা রহস্যময় গুহা", "Khagrachhari"],
        "tour-2": ["Risang Waterfall", "রিসাং ঝর্ণা", "Khagrachhari"],
        "tour-3": ["Tareng", "তারেং পাহাড়", "Khagrachhari"],
        "tour-4": ["Hajachhari Waterfall", "হাজাচড়া ঝর্ণা", "Dighinala"],
        "tour-5": ["Mayabini Lake", "মায়াবিনী লেক", "Panchhari, Khagrachhari"]
    },
    "joypurhat": {
        "hero": ["Joypurhat District", "জয়পুরহাট জেলা", "Paharpur"],
        "carousel-1": ["Lockma Rajbari", "লকমা রাজবাড়ি", "Panchbibi"],
        "carousel-2": ["Hinda Kasba Jame Mosque", "হিন্দা-কসবা শাহী জামে মসজিদ", "Khetlal"],
        "carousel-3": ["Patharghata, Joypurhat", "পাথরঘাটা জয়পুরহাট", "Panchbibi"],
        "carousel-4": ["Chhota Jamuna River", "ছোট যমুনা নদী", "Joypurhat"],
        "carousel-5": ["Joypurhat Sugar Mill", "জয়পুরহাট চিনি কল", "Joypurhat"],
        "hist-1": ["Lockma Rajbari", "লকমা রাজবাড়ি", "Panchbibi, Joypurhat"],
        "hist-2": ["Patharghata, Joypurhat", "পাথরঘাটা", "Joypurhat District"],
        "hist-3": ["Hinda Kasba Jame Mosque", "হিন্দা-কসবা শাহী মসজিদ", "Khetlal"],
        "hist-4": ["Agradigun", "অগ্রদ্বিগুন", "Dhamoirhat"],
        "hist-5": ["Khetlal Upazila", "ক্ষেতলাল উপজেলা", "Joypurhat"],
        "tour-1": ["Panchbibi Upazila", "পাঁচবিবি", "Joypurhat"],
        "tour-2": ["Chhota Jamuna River", "ছোট যমুনা নদী", "Joypurhat"],
        "tour-3": ["Panchbibi Upazila", "জয়পুরহাট জেলা", "Panchbibi"],
        "tour-4": ["Joypurhat Sugar Mill", "জয়পুরহাট সুগার মিল", "Joypurhat"],
        "tour-5": ["Khetlal Upazila", "ক্ষেতলাল", "Joypurhat"]
    },
    "sunamganj": {
        "hero": ["Tanguar Haor", "টাঙ্গুয়ার হাওর", "Sunamganj District"],
        "carousel-1": ["Tanguar Haor", "টাঙ্গুয়ার হাওর", "Tahirpur"],
        "carousel-2": ["Shimul Bagan", "শিমুল বাগান তাহিরপুর", "Jadukata River"],
        "carousel-3": ["Jadukata River", "যাদুকাটা নদী", "Tahirpur, Sunamganj"],
        "carousel-4": ["Niladri Lake", "নীলাদ্রি লেক", "Tekerghat"],
        "carousel-5": ["Hason Raja", "হাসন রাজা জাদুঘর", "Sunamganj"],
        "hist-1": ["Hason Raja", "হাসন রাজা", "Hason Raja Museum"],
        "hist-2": ["Baghaura", "বাঘাউড়া", "Sunamganj District"],
        "hist-3": ["Laur Kingdom", "লাউড় রাজ্য", "Tahirpur"],
        "hist-4": ["Dharampasha Upazila", "ধর্মপাশা", "Sunamganj"],
        "hist-5": ["Sukhair Zamindar Bari", "সুখাইড় জমিদার বাড়ি", "Dharampasha"],
        "tour-1": ["Tanguar Haor", "টাঙ্গুয়ার হাওর", "Tahirpur, Sunamganj"],
        "tour-2": ["Shimul Bagan", "শিমুল বাগান", "Jadukata River"],
        "tour-3": ["Jadukata River", "যাদুকাটা নদী", "Tahirpur"],
        "tour-4": ["Barek Tila", "বারেক টিলা", "Tahirpur, Sunamganj"],
        "tour-5": ["Niladri Lake", "শহীদ সিরাজ লেক", "Tekerghat, Sunamganj"]
    },
    "gaibandha": {
        "hero": ["Brahmaputra River", "ব্রহ্মপুত্র নদ", "Gaibandha District"],
        "carousel-1": ["Brahmaputra River", "ব্রহ্মপুত্র নদ গাইবান্ধা", "Gaibandha"],
        "carousel-2": ["Balashi Ghat", "বালাসী ঘাট", "Fulchhari"],
        "carousel-3": ["Teesta River", "তিস্তা নদী", "Sundarganj"],
        "carousel-4": ["Bardhankuthi", "বর্ধনকুঠী", "Govindaganj"],
        "carousel-5": ["Ghaghot River", "ঘাঘট নদী", "Gaibandha"],
        "hist-1": ["Bardhankuthi", "বর্ধনকুঠী রাজবাড়ি", "Govindaganj, Gaibandha"],
        "hist-2": ["Naldanga, Gaibandha", "নলডাঙ্গা", "Sadullapur Upazila"],
        "hist-3": ["Gaibandha Sadar Upazila", "গাইবান্ধা সদর", "Gaibandha"],
        "hist-4": ["Bhabaniganj, Gaibandha", "ভবানীগঞ্জ", "Gaibandha"],
        "hist-5": ["Govindaganj Upazila", "গোবিন্দগঞ্জ", "Gaibandha District"],
        "tour-1": ["Brahmaputra River", "ব্রহ্মপুত্র নদ", "Fulchhari"],
        "tour-2": ["Balashi Ghat", "বালাসী ঘাট", "Fulchhari, Gaibandha"],
        "tour-3": ["Teesta River", "তিস্তা ও যমুনা মিলনস্থল", "Sundarganj"],
        "tour-4": ["Ghaghot River", "ঘাঘট নদী", "Gaibandha town"],
        "tour-5": ["Fulchhari Upazila", "ফুলছড়ি চর", "Gaibandha"]
    },
    "rangpur": {
        "hero": ["Tajhat Palace", "তাজহাট রাজবাড়ি", "Rangpur, Bangladesh"],
        "carousel-1": ["Tajhat Palace", "তাজহাট জমিদার বাড়ি", "Rangpur"],
        "carousel-2": ["Carmichael College, Rangpur", "কারমাইকেল কলেজ", "Rangpur"],
        "carousel-3": ["Vinnya Jagat", "ভিন্ন জগত", "Gangachhara"],
        "carousel-4": ["Chikli Water Park", "চিকলি বিল", "Rangpur"],
        "carousel-5": ["Begum Rokeya", "বেগম রোকেয়া স্মৃতি কেন্দ্র", "Pairaband"],
        "hist-1": ["Tajhat Palace", "তাজহাট রাজবাড়ি", "Rangpur town"],
        "hist-2": ["Carmichael College, Rangpur", "কারমাইকেল কলেজ রংপুর", "Rangpur"],
        "hist-3": ["Dimla Rajbari", "ডিমলা রাজবাড়ি", "Rangpur District"],
        "hist-4": ["Keramatia Mosque", "কেরামতিয়া জামে মসজিদ", "Rangpur"],
        "hist-5": ["Pirgachha Upazila", "পীরগাছা", "Rangpur District"],
        "tour-1": ["Chikli Water Park", "চিকলি বিল পার্ক", "Rangpur"],
        "tour-2": ["Vinnya Jagat", "ভিন্ন জগত রংপুর", "Gangachhara"],
        "tour-3": ["Rangpur Zoo", "রংপুর চিড়িয়াখানা", "Rangpur"],
        "tour-4": ["Teesta River", "তিস্তা নদী", "Gangachhara, Rangpur"],
        "tour-5": ["Begum Rokeya", "পায়রাবন্দ বেগম রোকেয়া", "Mithapukur"]
    },
    "rangamati": {
        "hero": ["Kaptai Lake", "কাপ্তাই হ্রদ", "Rangamati District"],
        "carousel-1": ["Sajek Valley", "সাজেক ভ্যালি", "Baghaichhari"],
        "carousel-2": ["Kaptai Lake", "কাপ্তাই লেক", "Rangamati"],
        "carousel-3": ["Hanging Bridge, Rangamati", "ঝুলন্ত সেতু রাঙ্গামাটি", "Kaptai Lake"],
        "carousel-4": ["Rajban Vihara", "রাজবন বিহার", "Bana Bhante"],
        "carousel-5": ["Shuvolong Waterfall", "শুভলং ঝর্ণা", "Kaptai Lake"],
        "hist-1": ["Chakma Rajbari", "চাকমা রাজবাড়ি", "Chakma Circle"],
        "hist-2": ["Rajban Vihara", "রাজবন বিহার", "Rangamati"],
        "hist-3": ["Tabalchhari", "তবলছড়ি বৌদ্ধ মন্দির", "Rangamati"],
        "hist-4": ["Kaptai Dam", "কাপ্তai জলবিদ্যুৎ কেন্দ্র", "Kaptai Upazila"],
        "hist-5": ["Chitmorom", "চিৎমরম বৌদ্ধ বিহার", "Kaptai"],
        "tour-1": ["Sajek Valley", "সাজেক ভ্যালি মেঘের রাজ্য", "Rangamati"],
        "tour-2": ["Kaptai Lake", "কাপ্তাই হ্রদ", "Rangamati"],
        "tour-3": ["Hanging Bridge, Rangamati", "রাঙ্গামাটি ঝুলন্ত সেতু", "Kaptai Lake"],
        "tour-4": ["Shuvolong Waterfall", "শুভলং ঝরনা", "Rangamati"],
        "tour-5": ["Polwel Park", "পলওয়েল পার্ক", "Kaptai Lake"]
    },
    "chapainawabganj": {
        "hero": ["Choto Sona Mosque", "ছোট সোনা মসজিদ", "Chapainawabganj District"],
        "carousel-1": ["Choto Sona Mosque", "ছোট সোনা মসজিদ", "Shibganj"],
        "carousel-2": ["Darasbari Mosque", "দারাসবাড়ি মসজিদ", "Gaur (city)"],
        "carousel-3": ["Khania Dighi Mosque", "খঞ্জনীয়া মসজিদ", "Shibganj"],
        "carousel-4": ["Shah Niamatullah Wali", "শাহ নেয়ামতউল্লাহ ওয়ালী", "Firozpur"],
        "carousel-5": ["Mahananda River", "মহানন্দা নদী", "Chapainawabganj"],
        "hist-1": ["Choto Sona Mosque", "ছোট সোনা মসজিদ", "Gaur"],
        "hist-2": ["Darasbari Mosque", "দারাসবাড়ি মসজিদ ও মাদ্রাসা", "Shibganj"],
        "hist-3": ["Khania Dighi Mosque", "চামচিকা মসজিদ", "Shibganj, Chapainawabganj"],
        "hist-4": ["Dhunichak Mosque", "ধনিচক মসজিদ", "Shibganj"],
        "hist-5": ["Shah Niamatullah Wali", "শাহ নেয়ামতউল্লাহর মাজার", "Shibganj"],
        "tour-1": ["Mango Bangladesh", "চাঁপাইনবাবগঞ্জের আম বাগান", "Shibganj"],
        "tour-2": ["Padma River", "পদ্মা নদী", "Shibganj, Chapainawabganj"],
        "tour-3": ["Mahananda River", "মহানন্দা নদী তীর", "Chapainawabganj town"],
        "tour-4": ["Rohanpur", "রহনপুর", "Punarbhaba River"],
        "tour-5": ["Nachole Upazila", "নাচোল উপজেলা", "Barind Tract"]
    },
    "bandarban": {
        "hero": ["Bandarban District", "বান্দরবান জেলা", "Nilgiri Bandarban"],
        "carousel-1": ["Boga Lake", "বগা লেক", "Ruma, Bandarban"],
        "carousel-2": ["Nilgiri, Bandarban", "নীলগিরি", "Bandarban"],
        "carousel-3": ["Nafakhum", "নাফাখুম জলপ্রপাত", "Thanchi"],
        "carousel-4": ["Buddha Dhatu Jadi", "স্বর্ণ মন্দির বান্দরবান", "Golden Temple Bandarban"],
        "carousel-5": ["Nilachal", "নীলাচল বান্দরবান", "Bandarban town"],
        "hist-1": ["Bohmong Circle", "বোমাং রাজবাড়ি", "Bandarban"],
        "hist-2": ["Buddha Dhatu Jadi", "বুদ্ধ ধাতু জাদি", "Bandarban"],
        "hist-3": ["Chimbuk Hill", "চিম্বুক পাহাড়", "Bandarban"],
        "hist-4": ["Ruma Upazila", "রুমা উপজেলা", "Bandarban"],
        "hist-5": ["Ali Kadam Upazila", "আলীকদম গুহা", "Bandarban"],
        "tour-1": ["Nilgiri, Bandarban", "নীলগিরি রিসোর্ট", "Bandarban"],
        "tour-2": ["Nafakhum", "নাফাখুম জলপ্রপাত", "Sangu River"],
        "tour-3": ["Boga Lake", "বগালেক", "Ruma Upazila"],
        "tour-4": ["Sangu River", "সাঙ্গু নদী", "Bandarban"],
        "tour-5": ["Nilachal", "নীলাচল", "Bandarban town"]
    },
    "barguna": {
        "hero": ["Bibi Chini Mosque", "বিবি চিনি মসজিদ", "Barguna District"],
        "carousel-1": ["Bibi Chini Mosque", "বিবি চিনি মসজিদ", "Betagi"],
        "carousel-2": ["Shuvo Sandhya Sea Beach", "শুভ সন্ধ্যা সমুদ্র সৈকত", "Taltali"],
        "carousel-3": ["Payra River", "পায়রা নদী", "Barguna"],
        "carousel-4": ["Harinbaria", "হরিণবাড়িয়া বন", "Patharghata"],
        "carousel-5": ["Bishkhali River", "বিষখালী নদী", "Barguna"],
        "hist-1": ["Bibi Chini Mosque", "বিবি চিনি মসজিদ", "Betagi, Barguna"],
        "hist-2": ["Patharghata Upazila", "পাথরঘাটা", "Barguna District"],
        "hist-3": ["Taltali Upazila", "তালতলী রাখাইন পল্লী", "Barguna"],
        "hist-4": ["Barguna town", "বরগুনা জেলা", "Barguna"],
        "hist-5": ["Amtali Upazila", "আমতলী উপজেলা", "Barguna"],
        "tour-1": ["Shuvo Sandhya Sea Beach", "শুভ সন্ধ্যা সৈকত", "Taltali, Barguna"],
        "tour-2": ["Harinbaria", "হরিণবাড়িয়া ম্যানগ্রোভ", "Patharghata"],
        "tour-3": ["Payra River", "পায়রা নদী", "Amtali, Barguna"],
        "tour-4": ["Bishkhali River", "বিষখালী নদী", "Barguna"],
        "tour-5": ["Haringhata", "লালদিয়া বন ও সৈকত", "Patharghata"]
    },
    "lalmonirhat": {
        "hero": ["Teesta Barrage", "তিস্তা ব্যারেজ", "Lalmonirhat District"],
        "carousel-1": ["Teesta Barrage", "তিস্তা ব্যারেজ", "Dalia, Lalmonirhat"],
        "carousel-2": ["Tin Bigha Corridor", "তিন বিঘা করিডোর", "Patgram"],
        "carousel-3": ["Kakina Zamindar Bari", "কাকিনা জমিদার বাড়ি", "Kaliganj"],
        "carousel-4": ["Harano Masjid", "হারানো মসজিদ", "Ramdas, Lalmonirhat"],
        "carousel-5": ["Burimari", "বুড়িমারী স্থলবন্দর", "Patgram"],
        "hist-1": ["Kakina Zamindar Bari", "কাকিনা জমিদার বাড়ি", "Kaliganj, Lalmonirhat"],
        "hist-2": ["Nidaria Mosque", "নিদারিয়া মসজিদ", "Lalmonirhat Sadar"],
        "hist-3": ["Harano Masjid", "হারানো মসজিদ ৬৯ হিজরি", "Lalmonirhat"],
        "hist-4": ["Sheikh Fazlul Karim", "কবি শেখ ফজলল করিম", "Kakina"],
        "hist-5": ["Lalmonirhat Airport", "লালমনিরহাট বিমানবন্দর", "Lalmonirhat"],
        "tour-1": ["Teesta Barrage", "তিস্তা ব্যারেজ ডালিয়া", "Hatibandha"],
        "tour-2": ["Teesta River", "তিস্তা নদী চর", "Hatibandha, Lalmonirhat"],
        "tour-3": ["Burimari", "বুড়িমারী স্থলবন্দর", "Patgram, Lalmonirhat"],
        "tour-4": ["Tin Bigha Corridor", "তিন বিঘা করিডোর", "Dahagram-Angarpota"],
        "tour-5": ["Kakina", "কাকিনা", "Kaliganj, Lalmonirhat"]
    },
    "nilphamari": {
        "hero": ["Nilsagar", "নীলসাগর", "Nilphamari District"],
        "carousel-1": ["Nilsagar", "নীলসাগর দীঘি", "Gorgram"],
        "carousel-2": ["Chini Mosque", "চিনি মসজিদ সৈয়দপুর", "Saidpur"],
        "carousel-3": ["Saidpur Railway Workshop", "সৈয়দপুর রেলওয়ে কারখানা", "Saidpur"],
        "carousel-4": ["Nilphamari Sadar Upazila", "নটখানা নীলকুঠি", "Nilphamari"],
        "carousel-5": ["Teesta River", "তিস্তা নদী ডিমলা", "Dimla Upazila"],
        "hist-1": ["Nilphamari Sadar Upazila", "নীলকুঠি নটখানা", "Nilphamari"],
        "hist-2": ["King Birat", "রাজা বিরাট দীঘি", "Nilphamari District"],
        "hist-3": ["Dharmapal Garh", "ধর্মপাল গড়", "Jaldhaka, Nilphamari"],
        "hist-4": ["Harishchandra", "হরিশচন্দ্রের পাঠ", "Nilphamari"],
        "hist-5": ["Nilsagar", "নীলসাগর দিঘি", "Gorgram, Nilphamari"],
        "tour-1": ["Nilsagar", "নীলসাগর পর্যটন কেন্দ্র", "Gorgram"],
        "tour-2": ["Dimla Upazila", "ডিমলা তিস্তা নদী", "Nilphamari"],
        "tour-3": ["Chini Mosque", "চিনি মসজিদ", "Saidpur, Nilphamari"],
        "tour-4": ["Saidpur Railway Workshop", "সৈয়দপুর রেলওয়ে ওয়ার্কশপ", "Saidpur"],
        "tour-5": ["Saidpur, Bangladesh", "সৈয়দপুর শহর", "Nilphamari"]
    },
    "thakurgaon": {
        "hero": ["Jamalpur Zamindar Bari", "জামালপুর জমিদার বাড়ি", "Thakurgaon District"],
        "carousel-1": ["Jamalpur Zamindar Bari", "জামালপুর জমিদার বাড়ি", "Thakurgaon Sadar"],
        "carousel-2": ["Haripur Rajbari", "হরিপুর রাজবাড়ি", "Haripur, Thakurgaon"],
        "carousel-3": ["Balia Mosque", "বালিয়া মসজিদ", "Thakurgaon"],
        "carousel-4": ["Ranisankail Upazila", "রানীশংকৈল দিঘি", "Thakurgaon"],
        "carousel-5": ["Thakurgaon Sugar Mills Limited", "ঠাকুরগাঁও চিনি কল", "Thakurgaon"],
        "hist-1": ["Baliadangi Upazila", "বালিয়াডাঙ্গী জমিদার বাড়ি", "Thakurgaon"],
        "hist-2": ["Jamalpur Zamindar Bari", "জামালপুর জমিদার বাড়ি মসজিদ", "Thakurgaon Sadar"],
        "hist-3": ["Haripur Rajbari", "হরিপুর রাজবাড়ি", "Haripur Upazila"],
        "hist-4": ["Thakurgaon District", "শালবাগান মসজিদ", "Thakurgaon"],
        "hist-5": ["Pirganj Upazila, Thakurgaon", "পীরগঞ্জ ঐতিহাসিক নিদর্শন", "Thakurgaon"],
        "tour-1": ["Ranisankail Upazila", "রানীশংকৈল রাজবাড়ি দিঘি", "Thakurgaon"],
        "tour-2": ["Thakurgaon District", "শুক নদী", "Tangon River"],
        "tour-3": ["Balia Mosque", "বালিয়া মসজিদ চত্বর", "Thakurgaon"],
        "tour-4": ["Haripur Upazila, Thakurgaon", "হরিপুর গ্রামীণ নিসর্গ", "Thakurgaon"],
        "tour-5": ["Thakurgaon Sugar Mills Limited", "ঠাকুরগাঁও সুগার মিল", "Thakurgaon"]
    },
    "panchagarh": {
        "hero": ["Tetulia Dak Bungalow", "তেঁতুলিয়া", "Kangchenjunga"],
        "carousel-1": ["Kangchenjunga", "কাঞ্চনজঙ্ঘা তেঁতুলিয়া", "Tetulia"],
        "carousel-2": ["Tetulia tea garden", "তেঁতুলিয়া চা বাগান", "Kazi & Kazi Tea"],
        "carousel-3": ["Banglabandha", "বাংলাবান্ধা জিরো পয়েন্ট", "Zero Point Banglabandha"],
        "carousel-4": ["Mahananda River", "মহানন্দা নদী", "Tetulia, Panchagarh"],
        "carousel-5": ["Mirzapur Shahi Mosque", "মির্জাপুর শাহী মসজিদ", "Atwari"],
        "hist-1": ["Bhitargarh", "মহারাজার দীঘি ভিতরগড়", "Maharaja Dighi"],
        "hist-2": ["Mirzapur Shahi Mosque", "মির্জাপুর শাহী মসজিদ", "Atwari, Panchagarh"],
        "hist-3": ["Boda Upazila", "বোদেশ্বরী মন্দির", "Panchagarh"],
        "hist-4": ["Banglabandha", "বাংলাবান্ধা জিরো পয়েন্ট", "Tetulia"],
        "hist-5": ["Panchagarh railway station", "পঞ্চগড় রেলওয়ে স্টেশন", "Panchagarh"],
        "tour-1": ["Tetulia Dak Bungalow", "তেঁতুলিয়া ডাকবাংলো", "Panchagarh"],
        "tour-2": ["Mahananda River", "মহানন্দা নদী পাথর", "Tetulia"],
        "tour-3": ["Banglabandha", "বাংলাবান্ধা স্থলবন্দর", "Tetulia"],
        "tour-4": ["Tetulia tea garden", "পঞ্চগড় চা বাগান", "Tetulia"],
        "tour-5": ["Kangchenjunga", "কাঞ্চনজঙ্ঘা ভিউপয়েন্ট", "Tetulia"]
    }
}

search_map_17 = {}

for slug in districts_17:
    dist = master_64.get(slug)
    if not dist:
        print(f"Warning: slug {slug} not found in master_64")
        continue

    dist_map = {}
    overrides = SEARCH_OVERRIDES.get(slug, {})

    # 1. Hero
    dist_map["hero"] = overrides.get("hero", [f"{dist['en']} District", f"{dist['bn']} জেলা", f"{dist['en']} Bangladesh"])

    # 2. Carousel 1-5
    for i in range(1, 6):
        key = f"carousel-{i}"
        if key in overrides:
            dist_map[key] = overrides[key]
        else:
            c = dist['carousel'][i - 1]
            dist_map[key] = [c['titleEn'], c['titleBn'], f"{dist['en']} District"]

    # 3. Hist 1-5
    for i in range(1, 6):
        key = f"hist-{i}"
        if key in overrides:
            dist_map[key] = overrides[key]
        else:
            h = dist['hist'][i - 1]
            dist_map[key] = [h['nameEn'], h['nameBn'], f"{h['nameEn']} {dist['en']}"]

    # 4. Tour 1-5
    for i in range(1, 6):
        key = f"tour-{i}"
        if key in overrides:
            dist_map[key] = overrides[key]
        else:
            t = dist['tour'][i - 1]
            dist_map[key] = [t['nameEn'], t['nameBn'], f"{t['nameEn']} {dist['en']}"]

    search_map_17[slug] = dist_map
    print(f"Prepared search terms for {slug}: 16 items")

with open('scripts/search_map_17.json', 'w', encoding='utf-8') as f:
    json.dump(search_map_17, f, ensure_ascii=False, indent=2)

print("Saved scripts/search_map_17.json successfully!")
