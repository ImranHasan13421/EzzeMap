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
# 6. NOAKHALI
# ==========================================
no_raw = all_data['noakhali']
noakhali_data = {
    "slug": "noakhali",
    "en": "Noakhali",
    "bn": "নোয়াখালী",
    "hero_title_en": "Noakhali Coastal Frontier, Nijhum Dweep & Historic Shrines",
    "hero_title_bn": "নোয়াখালীর উপকূলীয় নিঝুম দ্বীপ ও ঐতিহাসিক ঐতিহ্য",
    "hero_sub_en": "Mughal-era Bajra Shahi Mosque, Mahatma Gandhi peace ashram, and wild spotted deer havens at Nijhum Dweep.",
    "hero_sub_bn": "মুঘল আমলের ঐতিহাসিক বজরা শাহী মসজিদ, মহাত্মা গান্ধীর স্মৃতিবিজড়িত শান্তি আশ্রম ও নিঝুম দ্বীপের হরিণ বিচরণের স্বর্গরাজ্য।",
    "tagline_en": "A legendary maritime frontier district on the Bay of Bengal estuary, celebrated for resilient coastal culture, historic Mughal mosques, and the pristine wilderness of Nijhum Dweep.",
    "tagline_bn": "বঙ্গোপসাগরের মোহনায় অবস্থিত এক প্রাচীন উপকূলীয় জেলা, যা বজরা শাহী মসজিদ, ঐতিহাসিক গান্ধী আশ্রম এবং নিঝুম দ্বীপ ও হাতিয়ার প্রাকৃতিক রূপের জন্য খ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/noakhali/carousel-1.webp",
            "titleEn": "Nijhum Dweep National Park Island Wildlife",
            "titleBn": "নিঝুম দ্বীপ জাতীয় উদ্যান ও বন্যপ্রাণী অভয়ারণ্য",
            "subtitleEn": "Remote offshore island sanctuary in the Bay of Bengal famous for thousands of free-roaming spotted deer",
            "subtitleBn": "বঙ্গোপসাগরের বুকে জেগে ওঠা নির্জন দ্বীপ যা হাজার হাজার চিত্রা হরিণ ও কেওড়া বনের জন্য বিখ্যাত"
        },
        {
            "id": 2,
            "image": "images/districts/noakhali/carousel-2.webp",
            "titleEn": "Bajra Shahi Mosque Mughal Architectural Splendor",
            "titleBn": "বজরা শাহী মসজিদের মুঘল স্থাপত্যশৈলী",
            "subtitleEn": "1741 AD triple-domed sanctuary adorned with imported Chinese ceramic mosaic tiles in Sonaimuri",
            "subtitleBn": "১৭৪১ সালে নির্মিত ঐতিহাসিক তিন গম্বুজ মসজিদ যা প্রাচীন চীনা চীনামাটির ফলকে অলংকৃত"
        },
        {
            "id": 3,
            "image": "images/districts/noakhali/carousel-3.webp",
            "titleEn": "Gandhi Ashram Trust Historic Peace Campus",
            "titleBn": "গান্ধী আশ্রম ট্রাস্টের ঐতিহাসিক শান্তি ভবন",
            "subtitleEn": "Sacred humanitarian center in Jayag commemorating Mahatma Gandhi's historic 1946 peace mission in Noakhali",
            "subtitleBn": "জয়াগে অবস্থিত মহাত্মা গান্ধীর ১৯৪৬ সালের শান্তি মিশনের ঐতিহাসিক স্মৃতিবিজড়িত আশ্রম"
        },
        {
            "id": 4,
            "image": "images/districts/noakhali/carousel-4.webp",
            "titleEn": "Chairman Ghat Coastal Gateway to Offshore Islands",
            "titleBn": "চেয়ারম্যান ঘাট উপকূলীয় নদী বন্দর ও মোহনা",
            "subtitleEn": "Bustling coastal terminal linking the mainland to Hatiya Island and Sandwip channel",
            "subtitleBn": "মেঘনা মোহনার সুবিশাল জলরাশি ও হাতিয়ায় যাতায়াতের অন্যতম প্রধান উপকূলীয় ঘাট"
        },
        {
            "id": 5,
            "image": "images/districts/noakhali/carousel-5.webp",
            "titleEn": "Namar Bazar Pristine Golden Sea Beach",
            "titleBn": "নামার বাজার সমুদ্র সৈকত ও সূর্যাস্ত",
            "subtitleEn": "Tranquil sandy beach on southern Nijhum Dweep framing dramatic sunrises and sunsets over open sea",
            "subtitleBn": "নিঝুম দ্বীপের দক্ষিণাংশে অবস্থিত বিস্তীর্ণ বালুকাবেলা ও সমুদ্রের বুকে রক্তিম সূর্যাস্তের দৃশ্য"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Bajra Shahi Mosque",
            "nameBn": "বজরা শাহী মসজিদ",
            "categoryEn": "Mughal Imperial Architecture",
            "categoryBn": "মুঘল স্থাপত্যকীর্তি ও ঐতিহাসিক মসজিদ",
            "descEn": "Constructed in 1741 AD during the reign of Mughal Emperor Muhammad Shah by Amanullah Zamindar, Bajra Shahi Mosque in Sonaimuri is one of the most magnificent historical sanctuaries in southeastern Bangladesh. Built in deliberate imitation of the grand imperial mosques of Delhi, the structure features three graceful ribbed bulbous domes, twelve minarets, and an elevated gateway entrance. The exterior facade and interior prayer chambers were later meticulously embellished with imported Chinese ceramic mosaic tiles (chinitikri work), creating an iridescent sparkle under the sunlight. The mosque stands above a massive stone-paved courtyard with a deep heritage dighi reflecting its architectural silhouettes. It remains a prized destination for architectural scholars, historians, and pilgrims.",
            "descBn": "মুঘল সম্রাট মুহম্মদ শাহের রাজত্বকালে ১৭৪১ খ্রিস্টাব্দে জমিদার আমানুল্লাহ কর্তৃক নির্মিত সোনাইমুড়ীর বজরা শাহী মসজিদ দক্ষিণ-পূর্ব বাংলার অন্যতম শ্রেষ্ঠ মুঘল স্থাপত্য নিদর্শন। দিল্লির শাহী জামে মসজিদের অনুকরণে তৈরি এই মসজিদে রয়েছে তিনটি সুদৃশ্য গম্বুজ, বারোটি সুউচ্চ মিনার এবং একটি রাজকীয় সিংহদ্বার। পরবর্তীকালে মসজিদটির ভেতর ও বাইরে রঙিন চীনা মাটির টুকরো (চিনিক্রি কাজ) দিয়ে অত্যন্ত নিখুঁতভাবে সাজানো হয়, যা রোদের আলোয় ঝলমল করে ওঠে। সুবিশাল শানবাঁধানো প্রাঙ্গণ এবং সংলগ্ন বিশাল দীঘির স্বচ্ছ জল মসজিদের স্থাপত্যকে আরও মনোহর করে তুলেছে। শতাব্দীর পর শতাব্দী ধরে এটি ইতিহাসপ্রেমী ও ধর্মপ্রাণ মানুষের পরম আকর্ষণের কেন্দ্রবিন্দু।",
            "locationEn": no_raw['hist_spots'][0]['location'],
            "locationBn": "বজরা, সোনাইমুড়ী, নোয়াখালী",
            "mapUrl": no_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Gandhi Ashram",
            "nameBn": "গান্ধী আশ্রম ট্রাস্ট",
            "categoryEn": "Historical Peace & Human Rights Landmark",
            "categoryBn": "ঐতিহাসিক শান্তি সৌধ ও স্মৃতি কমপ্লেক্স",
            "descEn": "The Gandhi Ashram in Jayag, Sonaimuri, is a world-renowned historical sanctuary commemorating Mahatma Gandhi's historic peace mission to Noakhali in late 1946. Seeking to heal communal wounds and restore human brotherhood following regional unrest, Gandhi walked barefoot from village to village spreading messages of nonviolence and compassion. Local barrister Hemanta Kumar Ghosh donated his ancestral estate to establish the ashram, which continues Gandhi's legacy through cottage industries, rural education, and social development. The museum exhibits personal belongings of Gandhi, rare archival photographs of the peace march, and spinning wheels (charkhas). Visitors from around the world visit to pay homage to the enduring ideals of peace, communal harmony, and human dignity.",
            "descBn": "সোনাইমুড়ী উপজেলার জয়াগে অবস্থিত গান্ধী আশ্রম বিশ্বখ্যাত এক ঐতিহাসিক স্থান, যা ১৯৪৬ সালে নোয়াখালীতে মহাত্মা গান্ধীর ঐতিহাসিক শান্তি অভিযানের স্মৃতি বহন করে। দাঙ্গা-বিধ্বস্ত নোয়াখালীতে শান্তি ও সাম্প্রদায়িক সম্প্রীতি ফিরিয়ে আনতে গান্ধীজি খালি পায়ে গ্রামে গ্রামে হেঁটে অহিংসা ও ভ্রাতৃত্বের বাণী প্রচার করেছিলেন। স্থানীয় জমিদার হেমন্ত কুমার ঘোষ তাঁর পুরো সম্পত্তি এই মহতী কাজের জন্য দান করে আশ্রমটি প্রতিষ্ঠা করেন। বর্তমানে এখানে থাকা জাদুঘরে সংরক্ষিত আছে গান্ধীর ব্যবহৃত সামগ্রী, ঐতিহাসিক আলোকচিত্র এবং সেই বিখ্যাত চরকা। শান্তি, সম্প্রীতি ও অহিংসার জীবন্ত স্মারক হিসেবে দেশ-বিদেশের বহু গবেষক ও পর্যটক এই আশ্রমে আসেন।",
            "locationEn": no_raw['hist_spots'][1]['location'],
            "locationBn": "জয়াগ, সোনাইমুড়ী, নোয়াখালী",
            "mapUrl": no_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Noakhali Zilla School Historic Campus",
            "nameBn": "নোয়াখালী জিলা স্কুল ঐতিহাসিক ক্যাম্পাস",
            "categoryEn": "Centenary Educational Heritage Site",
            "categoryBn": "শতবর্ষী শিক্ষাঙ্গন ও স্থাপত্যিক ঐতিহ্য",
            "descEn": "Founded in 1850 during the early Victorian colonial era, Noakhali Zilla School in Maijdee is one of the oldest and most prestigious secondary educational institutions in the Bengal delta. Having been relocated inland alongside the district headquarters after the old coastal town was engulfed by the Meghna River in the mid-twentieth century, the campus stands as a symbol of regional resilience. The school features classic colonial brick buildings with expansive colonnaded corridors, arched entryways, and spacious sports grounds shaded by ancient banyan trees. The institution educated many of the nation's leading scholars, civil servants, poets, and national leaders who shaped modern Bangladesh. It remains an honored anchor of Noakhali's intellectual and cultural heritage.",
            "descBn": "১৮৫০ সালে প্রতিষ্ঠিত নোয়াখালী জিলা স্কুল বৃহত্তর নোয়াখালী অঞ্চলের প্রাচীনতম ও শ্রেষ্ঠতম ঐতিহ্যবাহী বিদ্যাপীঠগুলোর অন্যতম। মেঘনা নদীর অব্যাহত ভাঙনে পুরোনো শহর বিলীন হয়ে যাওয়ার পর জেলা শহরের সাথে এই ঐতিহাসিক স্কুলটিও মাইজদীতে স্থানান্তরিত হয়, যা এ অঞ্চলের মানুষের অদম্য টিকে থাকার প্রতীক। লাল ইটের উপনিবেশিক স্থাপত্য, সুপরিসর বারান্দা, খিলানযুক্ত ক্লাসরুম ও বিশাল সবুজ খেলার মাঠ বিদ্যালয়টিকে এক অনন্য গাম্ভীর্য দান করেছে। এই বিদ্যাপীঠ থেকে শিক্ষা লাভ করেছেন দেশের বহু প্রথিতযশা বিজ্ঞানী, শিক্ষাবিদ, রাজনীতিবিদ ও সংস্কৃতিজন। দেড় শতাব্দীরও বেশি সময় ধরে জ্ঞানের আলো ছড়ানো এই প্রতিষ্ঠানটি নোয়াখালীর মানুষের পরম গর্ব।",
            "locationEn": no_raw['hist_spots'][2]['location'],
            "locationBn": "মাইজদী, নোয়াখালী",
            "mapUrl": no_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Sonapur Historic Settlement Area",
            "nameBn": "সোনাপুর ঐতিহাসিক জনপদ এলাকা",
            "categoryEn": "Historic Railway Terminus & Maritime Trading Hub",
            "categoryBn": "ঐতিহাসিক রেল প্রান্তিক ও উপকূলীয় বাণিজ্য কেন্দ্র",
            "descEn": "Sonapur in southern Noakhali Sadar is a historic railway terminus and bustling river-port town that served as the final southern outpost of the Assam Bengal Railway network. Established as a vital trading post where railway cargoes met coastal seafaring vessels navigating the Meghna estuary, the settlement preserves antique rail sidings, brick godowns, and bustling trading alleys. Merchants from across Bengal once gathered here to trade betel nuts, coconuts, dried fish, and salt harvested along the coastal flats. Surviving colonial-era structures and old tea stalls create a nostalgic atmosphere where travelers catch passenger transport heading towards the islands. It provides a fascinating glimpse into the commercial and maritime logistics of coastal Bengal.",
            "descBn": "নোয়াখালী সদরের দক্ষিণে অবস্থিত সোনাপুর এক ঐতিহাসিক জনপদ ও বিখ্যাত রেলওয়ে টার্মিনাস, যা আসাম বেঙ্গল রেলওয়ের শেষ প্রান্তিক স্টেশন হিসেবে প্রতিষ্ঠিত হয়েছিল। উপকূলীয় সমুদ্রবাণিজ্য এবং রেলওয়ে যোগাযোগের সেতুবন্ধন হিসেবে সোনাপুর শতাব্দী ধরে ধান, সুপারি, নারকেল ও শুঁটকির বিশাল পাইকারি বাণিজ্য কেন্দ্র হিসেবে ভূমিকা পালন করেছে। এখানকার পুরোনো রেললাইন, ব্রিটিশ আমলের গুদামঘর ও ঐতিহাসিক বাজারের অলিগলি একসময়ের সমৃদ্ধ বাণিজ্যের কথা মনে করিয়ে দেয়। হাতিয়া ও উপকূলীয় চরাঞ্চলে যাওয়ার মূল প্রবেশদ্বার হিসেবেও সোনাপুরের গুরুত্ব অপরিসীম। ইতিহাস ও আধুনিক জীবনের চমৎকার মেলবন্ধন দেখা যায় এই সোনাপুরে।",
            "locationEn": no_raw['hist_spots'][3]['location'],
            "locationBn": "সোনাপুর, নোয়াখালী সদর, নোয়াখালী",
            "mapUrl": no_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Chatkhil Historic Mosque and Shrine Sites",
            "nameBn": "চাটখিল ঐতিহাসিক মসজিদ ও দরবার এলাকা",
            "categoryEn": "Sacred Historical Sanctuary",
            "categoryBn": "ঐতিহাসিক সুফি দরবার ও ঐতিহ্যবাহী মসজিদ",
            "descEn": "The historic mosque and shrine sites of Chatkhil Upazila represent an unbroken tradition of spiritual scholarship and Sufi contemplation spanning over three centuries in northern Noakhali. Nestled beside ancestral water reservoirs and shade-bearing banyan trees, the historic mosques feature lime-surki brickwork, ornamental multi-tiered minarets, and classical arched entrances. Revered spiritual mentors settled here to establish community learning centers, teaching ethical values and caring for underprivileged deltaic communities. Annual commemorative gatherings and weekly prayers draw devotees from far and wide seeking solace and inner reflection in the peaceful village atmosphere. These sanctified grounds are treasured by locals as enduring sanctuaries of faith, community solidarity, and heritage.",
            "descBn": "চাটখিল উপজেলার ঐতিহাসিক মসজিদ ও মাজার প্রাঙ্গণ উত্তর নোয়াখালীর সুফি সাধনা ও ধর্মীয় ঐতিহ্যের এক পরম পবিত্র কেন্দ্র। প্রায় তিন শতাব্দী ধরে এ অঞ্চলের ইসলাম প্রচারক ও আউলিয়াদের স্মৃতিবিজড়িত এই স্থানগুলোতে রয়েছে চুন-সুরকির প্রাচীন মসজিদ, সুদৃশ্য মিনার এবং ছায়াঘেরা শান্ত পরিবেশ। ধর্মীয় শিক্ষার পাশাপাশি অসহায় মানুষের সেবায় তৎকালীন সুফি সাধকগণ এখানে খানকাহ ও মাদ্রাসা পরিচালনা করতেন। গ্রামীণ স্নিগ্ধ পরিবেশে অবস্থিত এই উপাসনালয়গুলোতে আজও ধর্মপ্রাণ মানুষ মানসিক শান্তি ও আধ্যাত্মিক উন্নতির কামনায় সমবেত হন। শতাব্দীর স্মৃতিবাহী এই দরবার চাটখিলের লোকসংস্কৃতি ও ধর্মীয় ইতিহাসে অত্যন্ত শ্রদ্ধার স্থান অধিকার করে আছে।",
            "locationEn": no_raw['hist_spots'][4]['location'],
            "locationBn": "চাটখিল, নোয়াখালী",
            "mapUrl": no_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Nijhum Dweep National Park",
            "nameBn": "নিঝুম দ্বীপ জাতীয় উদ্যান",
            "categoryEn": "Offshore Island Wildlife Sanctuary & Eco Park",
            "categoryBn": "উপকূলীয় দ্বীপ জাতীয় উদ্যান ও হরিণ অভয়ারণ্য",
            "descEn": "Nijhum Dweep National Park is an extraordinary offshore island eco-wonder situated in the Bay of Bengal estuary south of Hatiya Upazila. Famous across South Asia for harboring over forty thousand free-roaming spotted deer (Chitra Horin), the island features dense mangrove forests of keora, bain, and gewa trees crisscrossed by tidal canals. Visitors taking early morning boat cruises along narrow mangrove creeks often witness herds of wild deer grazing peacefully along water edges and swimming across channels. The island serves as an internationally vital winter haven for thousands of rare migratory shorebirds, including Indian skimmers and spoon-billed sandpipers. It is an unmatched destination for adventurous nature lovers and wildlife photographers.",
            "descBn": "হাতিয়া উপজেলার দক্ষিণে বঙ্গোপসাগরের বুকে অবস্থিত নিঝুম দ্বীপ জাতীয় উদ্যান বাংলাদেশের অন্যতম প্রধান ও রোমাঞ্চকর বন্যপ্রাণী অভয়ারণ্য। প্রায় ৪০ হাজারেরও বেশি মায়াবী চিত্রা হরিণের অবাধ বিচরণের জন্য দ্বীপটি বিশ্বজুড়ে পরিচিত। সুবিশাল কেওড়া ও বাইন বনের বুক চিরে চলে যাওয়া জোয়ার-ভাটার খালে ভোরে নৌকায় ঘুরলে খালের পাড়ে জলপানরত ও ঘাস খাওয়া হরিণের দলের দেখা মেলে। শীতকালে সুদূর সাইবেরিয়া থেকে আসা লাখ লাখ বিরল পরিযায়ী পাখির কলতানে মুখরিত থাকে এই দ্বীপের বালুচর। শহরের কোলাহল থেকে বহুদূরে সমুদ্রের ঢেউ আর বুনো হরিণের সান্নিধ্য পেতে নিঝুম দ্বীপ এক অনন্য রোমাঞ্চকর স্বর্গরাজ্য।",
            "locationEn": no_raw['tour_spots'][0]['location'],
            "locationBn": "হাতিয়া, নোয়াখালী",
            "mapUrl": no_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Namar Bazar",
            "nameBn": "নামার বাজার ও সৈকত এলাকা",
            "categoryEn": "Island Beach & Coastal Bazaar Hub",
            "categoryBn": "দ্বীপের সমুদ্র সৈকত ও প্রাণবন্ত বাজার",
            "descEn": "Namar Bazar is the vibrant southern coastal hub of Nijhum Dweep, serving as the primary tourist gateway to the island's pristine beaches and mangrove forests. Bordering a wide expanse of unspoiled sandy seashore, the beach offers tranquil strolls where red fiddler crabs scuttle across the flats and waves crash softly along the gentle slope. During evenings, travelers gather in the bustling open-air market to taste freshly grilled sea fish, dried seafood delicacies, and warm coconut water served by hospitable local islanders. The absence of heavy commercial crowds makes watching fiery oceanic sunrises and sunsets an deeply poetic experience. It forms the social and culinary heart of any expedition to Nijhum Dweep.",
            "descBn": "নিঝুম দ্বীপের দক্ষিণাংশে অবস্থিত নামার বাজার দ্বীপটির পর্যটন ও স্থানীয় জীবনের প্রধান কেন্দ্রবিন্দু। বাজারের ঠিক পাশেই রয়েছে বিস্তীর্ণ কুমারী সমুদ্র সৈকত, যেখানে হাজার হাজার লাল কাঁকড়ার অবাধ ছোটাছুটি এক অদ্ভুত রক্তিম সৌন্দর্যের সৃষ্টি করে। সন্ধ্যায় পর্যটকরা এই বাজারে এসে সমুদ্রের টাটকা সামুদ্রিক মাছ ভাজা, শুঁটকি ও সুস্বাদু ডাবের পানি উপভোগ করেন। সৈকতে দাঁড়িয়ে উন্মুক্ত সমুদ্রের বুক চিরে লাল সূর্যের উদয় ও অস্ত যাওয়ার দৃশ্য দেখার অনুভূতি অতুলনীয়। গ্রামীণ দ্বীপের সহজ-সরল মানুষের আতিথেয়তা এবং সমুদ্রের শান্ত নির্জনতা উপভোগ করতে নামার বাজার পর্যটকদের প্রিয় ঠিকানা।",
            "locationEn": no_raw['tour_spots'][1]['location'],
            "locationBn": "নিঝুম দ্বীপ, হাতিয়া, নোয়াখালী",
            "mapUrl": no_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Damar Char",
            "nameBn": "দমার চর",
            "categoryEn": "Pristine Offshore Sandbar & Bird Sanctuary",
            "categoryBn": "নির্জন সমুদ্রচর ও পরিযায়ী পাখির চারণভূমি",
            "descEn": "Damar Char is an isolated sandbar island emerging south of Nijhum Dweep in the active deltaic waters of the Bay of Bengal. Uninhabited by permanent human settlements, this pristine wilderness is blanketed in natural coastal grass, emergent mangroves, and expansive soft mudflats. In winter, it becomes one of the densest congregation grounds in the subcontinent for globally threatened migratory waterbirds and gulls feeding on rich aquatic invertebrates. Traveling to the char by traditional mechanized trawler over rolling sea swells offers a truly exhilarating oceanic adventure. For intrepid eco-tourists and ornithologists, Damar Char provides an untouched encounter with the untamed frontier of the Bengal delta.",
            "descBn": "নিঝুম দ্বীপের দক্ষিণে বঙ্গোপসাগরের বুকে জেগে ওঠা এক নির্জন ও অপরূপ বালুচর হলো দমার চর। স্থায়ী জনবসতিহীন এই চরে রয়েছে বিস্তীর্ণ ঘাসবন, নবগঠিত কেওড়া বাগান এবং মাইলের পর মাইল বিস্তৃত নরম কাদার উপকূল। শীতের মৌসুমে এই চরটি পরিযায়ী জলচর পাখি ও গাঙচিলদের এক অভয়ারণ্যে পরিণত হয়, যেখানে বিরল প্রজাতির পাখির ঝাঁক দেখা যায়। ট্রলারে চড়ে উত্তাল সমুদ্রের বুক চিরে এই নির্জন চরে পা রাখার অভিজ্ঞতা অত্যন্ত রোমাঞ্চকর। জনমানবহীন প্রকৃতির আসল রূপ, সমুদ্রের গর্জন এবং হাজার হাজার পাখির ওড়াউড়ি প্রত্যক্ষ করতে দমার চর এক অবিস্মরণীয় স্থান।",
            "locationEn": no_raw['tour_spots'][2]['location'],
            "locationBn": "হাতিয়া উপকূলীয় এলাকা, নোয়াখালী",
            "mapUrl": no_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Chairman Ghat",
            "nameBn": "চেয়ারম্যান ঘাট",
            "categoryEn": "Coastal Ferry Terminal & Scenic Estuary",
            "categoryBn": "উপকূলীয় নদী বন্দর ও মোহনার দৃশ্যপট",
            "descEn": "Chairman Ghat in Companiganj/Subarnachar region is the bustling maritime gateway connecting mainland Bangladesh with the offshore islands of Hatiya and Nijhum Dweep. Situated on the turbulent banks of the Lower Meghna estuary, the ghat bustles constantly with passenger launches, sea-trucks, and wooden trawlers loading goods and travellers. Visitors standing on the embankment witness the sheer, immense power of Bengal's greatest river system merging into the northern Bay of Bengal. The waterfront is packed with vibrant fish auctions where glistening Hilsa, pomfret, and giant estuary prawns are landed directly from fishing boats. It is a thrilling destination for experiencing the vibrant maritime pulse and cuisine of coastal Noakhali.",
            "descBn": "সুবর্ণচর ও কোম্পানীগঞ্জের সংযোগস্থলে অবস্থিত চেয়ারম্যান ঘাট নোয়াখালী মূল ভূখণ্ডের সাথে হাতিয়া ও নিঝুম দ্বীপের নৌযোগাযোগের প্রধান প্রবেশদ্বার। মেঘনার উত্তাল মোহনার তীরে অবস্থিত এই ঘাটে সবসময় সি-ট্রাক, যাত্রীবাহী লঞ্চ ও মাছের ট্রলারের ব্যস্ত আনাগোনা চোখে পড়ে। ঘাটের পাড়ে দাঁড়ালে মেঘনা নদীর সমুদ্রসম রূপ ও বাতাসের গর্জন এক রোমাঞ্চকর অনুভূতি জাগায়। ঘাট সংলগ্ন মাছের আড়তে জেলেরা নদী ও সাগরের তাজা রূপালী ইলিশ, রূপচাঁদা ও গলদা চিংড়ি পাইকারি দরে বিক্রি করেন। সমুদ্রযাত্রা শুরুর আগে কিংবা মোহনার মুক্ত হাওয়া উপভোগে চেয়ারম্যান ঘাট পর্যটকদের কাছে অত্যন্ত জনপ্রিয়।",
            "locationEn": no_raw['tour_spots'][3]['location'],
            "locationBn": "কোম্পানীগঞ্জ, নোয়াখালী",
            "mapUrl": no_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Hatiya Coastal Riverbank",
            "nameBn": "হাতিয়া উপকূলীয় নদীতীর",
            "categoryEn": "Island Riverfront & Embankment Vista",
            "categoryBn": "উপকূলীয় বেড়িবাঁধ ও নদী মোহনার দৃশ্য",
            "descEn": "The coastal riverbanks of Hatiya Island present an awe-inspiring panorama where the sky opens up across immense expanses of swirling tidal waterways and protective green embankments. Lined with casuarina (jhau) groves and resilient mangrove plantations, the dykes protect fertile villages while providing superb scenic walkways for visitors. Strolling along the riverfront at twilight allows travelers to observe traditional fishing boats navigating tidal currents against glowing sunset horizons. Fresh sea winds blow continuously across the water, providing an invigorating, revitalizing escape from urban stress. It stands as an authentic testament to the beauty and resilience of Bangladesh's offshore island communities.",
            "descBn": "ঐতিহাসিক হাতিয়া দ্বীপের উপকূলীয় নদীতীর ও বেড়িবাঁধ এলাকা প্রকৃতির এক সুবিশাল ও অনন্ত সৌন্দর্যের প্রকাশ। দ্বীপের চারপাশ ঘিরে থাকা এই বাঁধে দাঁড়ালে নদী আর সমুদ্রের উত্তাল ঢেউয়ের অবিরাম খেলা দেখা যায়। বাঁধের পাশে গড়ে ওঠা ঝাউবাগান ও প্যারাবন পরিবেশকে এক স্নিগ্ধ শ্যামল শোভা দান করেছে। বিকেলে নদীর পাড় ধরে হাঁটলে দেখা যায় জেলেরা জাল তুলে ফিরছেন আর পশ্চিমের আকাশ রক্তিম রঙে নদীর বুক রাঙিয়ে দিচ্ছে। সমুদ্রের নির্মল লবণাক্ত বাতাস শরীরে এক নতুন সজীবতা এনে দেয়। দ্বীপের মানুষের জীবনসংগ্রাম ও প্রকৃতির অপরূপ মেলবন্ধন দেখতে হাতিয়ার এই নদীতীর অনন্য।",
            "locationEn": no_raw['tour_spots'][4]['location'],
            "locationBn": "হাতিয়া, নোয়াখালী",
            "mapUrl": no_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('noakhali', noakhali_data)

# ==========================================
# 7. SHERPUR
# ==========================================
sh_raw = all_data['sherpur']
sherpur_data = {
    "slug": "sherpur",
    "en": "Sherpur",
    "bn": "শেরপুর",
    "hero_title_en": "Sherpur Garo Hills, Madhutila Eco Parks & Borderland Panoramas",
    "hero_title_bn": "শেরপুরের গারো পাহাড়, মধুটিলা ও গজনী অবকাশ কেন্দ্র",
    "hero_sub_en": "Picturesque foothills of Meghalaya, pine-clad Madhutila Eco Park, Gajni Leisure Center, and crystal border rivers.",
    "hero_sub_bn": "মেঘালয় সীমান্তঘেরা গারো পাহাড়ের পাদদেশ, মধুটিলা ও গজনী অবকাশ কেন্দ্রের প্রাকৃতিক সৌন্দর্য এবং পাহাড়ি নদীর রূপ।",
    "tagline_en": "A tranquil borderland district in northern Mymensingh division, famed for undulating Garo mountain ridges, lush sal forests, and captivating eco-tourism havens at Gajni and Madhutila.",
    "tagline_bn": "ময়মনসিংহ বিভাগের উত্তরাংশে মেঘালয় সীমান্ত সংলগ্ন এক রূপসী পাহাড়ি জেলা, যা গারো পাহাড়ের নীল শৈলশিরা, শালবন, গজনী অবকাশ কেন্দ্র ও মধুটিলা ইকোপার্কের জন্য বিশ্বস্ত পর্যটন স্বর্গ।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/sherpur/carousel-1.webp",
            "titleEn": "Gajni Leisure Center Elevated Watchtower",
            "titleBn": "গজনী অবকাশ কেন্দ্রের ওয়াচ টাওয়ার ও পাহাড়",
            "subtitleEn": "Picturesque hillock amusement park in Jhenaigati framed by rolling Garo hills and natural spring lakes",
            "subtitleBn": "ঝিনাইগাতীর সুউচ্চ টিলার ওপর অবস্থিত চমৎকার পর্যটন কেন্দ্র যা চারপাশের সবুজ পাহাড় ও পাহাড়ি লেকে ঘেরা"
        },
        {
            "id": 2,
            "image": "images/districts/sherpur/carousel-2.webp",
            "titleEn": "Madhutila Eco Park Pine Forest Trails",
            "titleBn": "মধুটিলা ইকোপার্কের পাইন ও শালবন ট্রেইল",
            "subtitleEn": "Dense evergreen border forest in Nalitabari with suspension footbridges, pedal lakes, and wild wildlife",
            "subtitleBn": "নালিতাবাড়ীর সীমান্তঘেরা শাল ও সেগুন বন যেখানে রয়েছে ঝুলন্ত সেতু, কৃত্রিম লেক ও পাহাড়ি নিসর্গ"
        },
        {
            "id": 3,
            "image": "images/districts/sherpur/carousel-3.webp",
            "titleEn": "Panihata-Tarani Hills Scenic Borderlands",
            "titleBn": "পানিহাটা-তারানি পাহাড়ের অপার্থিব রূপ",
            "subtitleEn": "Dramatic rolling hills and pristine mountain streams right on the international border in Nalitabari",
            "subtitleBn": "মেঘালয় সীমান্তরেখা ঘেঁষে অবস্থিত সর্পিল পাহাড় ও ঝিরিপথের অপূর্ব কুমারী নিসর্গ"
        },
        {
            "id": 4,
            "image": "images/districts/sherpur/carousel-4.webp",
            "titleEn": "Sherpur Rajbari Site Historic Remnants",
            "titleBn": "শেরপুর রাজবাড়ির ঐতিহাসিক স্মৃতিচিহ্ন",
            "subtitleEn": "Ancestral seat of the historic Sherpur zamindars who governed the northern frontier under the Mughals",
            "subtitleBn": "শেরপুর শহরের প্রাচীন সামন্তযুগীয় রাজবাড়ি ও জমিদারদের স্মৃতিবিজড়িত ঐতিহাসিক এলাকা"
        },
        {
            "id": 5,
            "image": "images/districts/sherpur/carousel-5.webp",
            "titleEn": "Bhogai River Border Waterways & Pebble Shores",
            "titleBn": "ভোগাই নদী ও পাহাড়ি বালুকাবেলা",
            "subtitleEn": "Shimmering mountain river carrying smooth stones and cool waters from Meghalaya into the plains",
            "subtitleBn": "পাহাড় থেকে নেমে আসা স্বচ্ছ শীতল ভোগাই নদী যা বালু ও পাথরের চরে আলো ছড়িয়ে বয়ে চলেছে"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Sherpur Rajbari Site",
            "nameBn": "শেরপুর রাজবাড়ি এলাকা",
            "categoryEn": "Ancient Feudal Capital & Palace Ground",
            "categoryBn": "ঐতিহাসিক জমিদার বাড়ি ও রাজকীয় ধ্বংসাবশেষ",
            "descEn": "The Sherpur Rajbari Site preserves the ancestral administrative capital of the illustrious nine-anna and seven-anna zamindar branches who governed the territory during Mughal and British rule. Founded centuries ago when the locality was named Sherpur after Mughal general Sher Ali Gazi, the estate featured grand palatial residences, ornate wooden dance pavilions, royal armories, and sacrificial temples. The zamindars patronized traditional theater, literature, and regional irrigation infrastructure. Surviving architectural gateways, antique ponds, and moss-covered brick boundaries still evoke the regal presence of the frontier rulers. Heritage travelers visit to trace the aristocratic history that gave Sherpur its modern name and cultural identity.",
            "descBn": "শেরপুর রাজবাড়ি এলাকা মুঘল ও ব্রিটিশ আমলের প্রতাপশালী নয়আনি ও সাতআনি জমিদারদের প্রাচীন প্রশাসনিক কেন্দ্র ও রাজপ্রাসাদ প্রাঙ্গণ। মুঘল সেনাপতি শের আলী গাজীর নামানুসারে প্রতিষ্ঠিত এই রাজবাড়িতে এককালে ছিল সুরম্য অন্দরমহল, জলসাঘর, বিচারালয় ও সুদৃশ্য দেবালয়। শেরপুরের জমিদারগণ শিক্ষা, সাহিত্য এবং সমাজকল্যাণে গুরুত্বপূর্ণ ভূমিকা রেখেছিলেন। প্রাসাদের প্রাচীন সিংহদ্বারের তোরণ, প্রাচীন পুকুর ও ইটের ধ্বংসাবশেষ তৎকালীন ঐশ্বর্যময় ইতিহাসের নীরব সাক্ষী হয়ে দাঁড়িয়ে আছে। শেরপুরের রাজনৈতিক ও সাংস্কৃতিক শিকড় অনুসন্ধানে এই রাজবাড়ি এলাকা ইতিহাসপ্রেমীদের জন্য অত্যন্ত তাৎপর্যপূর্ণ।",
            "locationEn": sh_raw['hist_spots'][0]['location'],
            "locationBn": "শেরপুর শহর, শেরপুর",
            "mapUrl": sh_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Baraibari Historic Mosque Area",
            "nameBn": "বড়ইবাড়ি ঐতিহাসিক মসজিদ এলাকা",
            "categoryEn": "Medieval Sultanate-Era Mosque Site",
            "categoryBn": "মধ্যযুগীয় সুলতানি আমলের ঐতিহাসিক মসজিদ",
            "descEn": "The Baraibari Historic Mosque Area in Sherpur Sadar preserves the venerable architectural remains of an early Islamic sanctuary dating back to the pre-Mughal Sultanate period. Constructed with seasoned terracotta bricks and sturdy lime mortar, the surviving structure features deeply recessed prayer niches, thick brick masonry, and traditional terracotta relief plaques. Historians trace the mosque to the spiritual efforts of traveling Sufi saints who established settlements along the old Brahmaputra river valleys. The surrounding hamlet retains antique burial mounds and historic water tanks shaded by ancient mango groves. It stands as one of the oldest tangible testaments to Islamic architectural heritage in the northern Mymensingh-Sherpur frontier.",
            "descBn": "শেরপুর সদর উপজেলার বড়ইবাড়ি ঐতিহাসিক মসজিদ এলাকা প্রাক-মুঘল সুলতানি আমলের প্রাচীন মুসলিম স্থাপত্যকলার এক অনন্য নিদর্শন। প্রাচীন পোড়ামাটির ইট ও চুন-সুরকির সমন্বয়ে নির্মিত এই মসজিদের পুরু দেওয়াল, খিলানযুক্ত মেহরাব এবং টেরাকোটার অলংকরণ মধ্যযুগীয় বাংলার নির্মাণশৈলীর পরিচয় দেয়। তৎকালীন সময়ে সুফি সাধকদের হাত ধরে ব্রহ্মপুত্র অববাহিকায় যে ধর্মীয় ও সামাজিক জাগরণ ঘটেছিল, এই মসজিদ তারই স্মৃতি বহন করে। সংলগ্ন প্রাচীন দীঘি ও ছায়াঘেরা গ্রামীণ পরিবেশ দর্শনার্থীদের মনে ভক্তি ও প্রশান্তি জাগায়। উত্তরবঙ্গের প্রাচীন ইসলামিক ঐতিহ্যের এক অমূল্য স্মারক হিসেবে বড়ইবাড়ি মসজিদ বিশেষ স্থান দখল করে আছে।",
            "locationEn": sh_raw['hist_spots'][1]['location'],
            "locationBn": "শেরপুর সদর, শেরপুর",
            "mapUrl": sh_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Nakla Historic Zamindar-House Sites",
            "nameBn": "নকলা ঐতিহাসিক জমিদার বাড়ি এলাকা",
            "categoryEn": "Colonial Aristocratic Mansion Site",
            "categoryBn": "উপনিবেশিক জমিদারি প্রাসাদ ও কাচারি প্রাঙ্গণ",
            "descEn": "The Nakla Historic Zamindar-House Sites encompass the grand residential estates of nineteenth-century agrarian landlords who managed agricultural estates across the fertile plains of southern Sherpur. The architecture blends classical European neoclassical colonnades with traditional multi-courtyard Bengali domestic layouts, including reception lounges and residential chambers. The zamindars dug sprawling freshwater dighis and patronized traditional weekly haats that remain the commercial backbone of Nakla today. Walking past the surviving brick columns and arched windows reveals the faded luxury of colonial-era landed nobility. It provides an engaging destination for travelers exploring regional rural history.",
            "descBn": "নকলা উপজেলার ঐতিহাসিক জমিদার বাড়ি এলাকা উনিশ শতকের গ্রামীণ সামন্তপ্রভুদের আভিজাত্য ও শাসনব্যবস্থার স্মৃতিবাহী এক প্রাচীন প্রাসাদ প্রাঙ্গণ। ইউরোপীয় নিও-ক্লাসিক্যাল স্তম্ভ এবং বাংলার ঐতিহ্যবাহী চারমহলা নকশার সমন্বয়ে নির্মিত এই ভবনগুলোতে ছিল বিশাল কাচারি ঘর, বাগানবাড়ি ও উৎসবের প্রাঙ্গণ। তৎকালীন জমিদারদের প্রতিষ্ঠিত সুবিশাল পুকুর ও প্রাচীন হাট আজও নকলা এলাকার জনজীবনে অত্যন্ত গুরুত্বপূর্ণ ভূমিকা পালন করছে। ইটের সুদৃঢ় গাঁথুনি ও খিলানযুক্ত বারান্দাগুলো অতীতের বিলাসবহুল জীবনযাত্রার কথা মনে করিয়ে দেয়। গ্রামীণ শান্ত পরিবেশে অতীতের জমিদারি ঐতিহ্য প্রত্যক্ষ করতে এটি এক চমৎকার স্থান।",
            "locationEn": sh_raw['hist_spots'][2]['location'],
            "locationBn": "নকলা, শেরপুর",
            "mapUrl": sh_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Madhutila Forest Heritage Zone",
            "nameBn": "মধুটিলা বন ঐতিহাসিক ঐতিহ্য এলাকা",
            "categoryEn": "Ancient Frontier Forest Heritage",
            "categoryBn": "ঐতিহাসিক সীমান্ত অরণ্য ও গারো ঐতিহ্য অঞ্চল",
            "descEn": "The Madhutila Forest Heritage Zone in Nalitabari represents centuries of frontier forestry and indigenous Garo tribal civilization tucked along the Himalayan foothill edges. Historically forming part of the dense Susang and Sherpur wild border reserves, the forest was inhabited by native forest-dwelling tribes who developed deep ecological harmony with the flora and fauna. Ancient elephant migration corridors crossed through these sal and teak valleys connecting Assam to the Bengal plains. In modern times, the historical forestry trails have been integrated into protected conservation areas while honoring indigenous cultural memories. Exploring the forest heritage zone offers profound insights into how nature and frontier communities coexisted across generations.",
            "descBn": "নালিতাবাড়ীর মধুটিলা বন ঐতিহাসিক ঐতিহ্য এলাকা মেঘালয় পাহাড়ের পাদদেশে গড়ে ওঠা শতাব্দীর প্রাচীন সীমান্ত অরণ্য ও গারো আদিবাসী ঐতিহ্যের এক সমৃদ্ধ ক্ষেত্র। প্রাচীনকালে এই গভীর শাল ও সেগুন বন সুসং ও শেরপুর রাজ্যের এক প্রাকৃতিক প্রতিরক্ষা প্রাচীর হিসেবে কাজ করত এবং বন্য হাতির চলাচলের ঐতিহাসিক পথ ছিল। যুগ যুগ ধরে গারো ও অন্যান্য ক্ষুদ্র নৃ-গোষ্ঠী এই অরণ্যের সাথে নিবিড় সম্পর্ক বজায় রেখে তাদের সংস্কৃতি ও জীবনধারা গড়ে তুলেছে। ইতিহাসের বিভিন্ন যুগে সীমান্ত পাহারা ও বনজ বাণিজ্যে এই অঞ্চলের বিশেষ ভূমিকা ছিল। বনের প্রাচীন ট্রেইল ধরে হাঁটার সময় ইতিহাস ও বন্য প্রকৃতির মেলবন্ধন গভীরভাবে উপলব্ধি করা যায়।",
            "locationEn": sh_raw['hist_spots'][3]['location'],
            "locationBn": "মধুটিলা, নালিতাবাড়ী, শেরপুর",
            "mapUrl": sh_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Gajni Borderland Historic Area",
            "nameBn": "গজনী সীমান্ত ঐতিহাসিক এলাকা",
            "categoryEn": "Historical Border Outpost & Frontier Heritage",
            "categoryBn": "ঐতিহাসিক সীমান্ত ফাঁড়ি ও প্রত্নস্থল",
            "descEn": "The Gajni Borderland Historic Area in Jhenaigati holds strategic historical importance as an ancient frontier gateway connecting the northern plains of Bengal to the Khasi and Garo hill territories. Serving as a military border outpost during Sultanate and Mughal campaigns, the undulating hillocks saw troop movements, elephant caravans, and trade missions. Colonial administrators later established tea and rubber experimental stations and forest monitoring posts along these scenic ridgelines. Today, surviving stone boundary markers, old observation hillocks, and local oral traditions keep the borderland's colorful historical lore alive. It serves as a fascinating historical backdrop to the popular natural leisure park that now graces the summit.",
            "descBn": "ঝিনাইগাতী উপজেলার গজনী সীমান্ত ঐতিহাসিক এলাকা প্রাচীন ও মধ্যযুগীয় বাংলার উত্তর সীমান্ত প্রতিরক্ষার এক অত্যন্ত গুরুত্বপূর্ণ কৌশলগত অঞ্চল। মধ্যযুগে সমতল বাংলার সাথে খাসিয়া ও গারো পাহাড়ের যোগাযোগের প্রধান বাণিজ্যপথ ও সামরিক পর্যবেক্ষণ কেন্দ্র ছিল এই পাহাড়ি এলাকা। মুঘল ও ব্রিটিশ আমলে সীমান্তে শান্তি রক্ষা এবং হাতির বাণিজ্যে গজনীর উঁচু টিলাগুলো বিশেষ ভূমিকা পালন করেছিল। এখানকার প্রাচীন সীমানা পিলার এবং স্থানীয় লোকগাথা অতীতের সীমান্ত জীবনের বহু রোমাঞ্চকর কাহিনী মনে করিয়ে দেয়। প্রাকৃতিক সৌন্দর্যের পাশাপাশি এই ঐতিহাসিক পটভূমি গজনীকে পর্যটকদের কাছে আরও বেশি আকর্ষণীয় করে তুলেছে।",
            "locationEn": sh_raw['hist_spots'][4]['location'],
            "locationBn": "গজনী, ঝিনাইগাতী, শেরপুর",
            "mapUrl": sh_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Madhutila Eco Park",
            "nameBn": "মধুটিলা ইকোপার্ক",
            "categoryEn": "Foothill Eco Tourism Park & Forest Sanctuary",
            "categoryBn": "পাহাড়ি ইকোপার্ক ও বোটানিক্যাল পর্যটন কেন্দ্র",
            "descEn": "Madhutila Eco Park in Nalitabari is one of northern Bangladesh's premier ecotourism destinations, spread across hundreds of acres of undulating hillocks cloaked in pine, sal, and teak forest. The park features an artificial lake with pedal boating, an exhilarating suspension walking bridge spanning a forest ravine, and a high observation tower offering sweeping views into the misty green mountains of Meghalaya. Nature trails weave through fragrant herbal plant gardens, mini-zoos, and picnic pavilions shaded by giant forest canopies. Families and travelers love spending the entire day exploring the cool forested trails and enjoying wholesome outdoor recreations. It represents a magical communion with the tranquil foothill nature of the Garo range.",
            "descBn": "নালিতাবাড়ী উপজেলায় অবস্থিত মধুটিলা ইকোপার্ক শেরপুরের অন্যতম সেরা ও নয়নাভিরাম পরিবেশবান্ধব পর্যটন কেন্দ্র, যা শত শত একর পাহাড়ি শাল ও সেগুন বনের মাঝে গড়ে উঠেছে। এই ইকোপার্কের মূল আকর্ষণ হলো গভীর খাদে তৈরি দৃষ্টিনন্দন ঝুলন্ত সেতু, সুউচ্চ ওয়াচ টাওয়ার এবং কৃত্রিম লেকে প্যাডেল বোটিংয়ের ব্যবস্থা। ওয়াচ টাওয়ারে উঠলে ভারতের মেঘালয়ের নীল পাহাড়ের সারি ও কুয়াশার চাদর এক পলকে দেখা যায়। বনের ভেতর দিয়ে চলে যাওয়া সর্পিল মাটির ট্রেইল ধরে হাঁটার সময় বুনো পাখির গান ও পাহাড়ি বাতাসের স্পর্শ দেহ-মন জুড়িয়ে দেয়। পরিবার-পরিজন নিয়ে অবকাশ যাপনে মধুটিলা ইকোপার্ক এক অপূর্ব স্বর্গরাজ্য।",
            "locationEn": sh_raw['tour_spots'][0]['location'],
            "locationBn": "নালিতাবাড়ী, শেরপুর",
            "mapUrl": sh_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Gajni Leisure Center",
            "nameBn": "গজনী অবকাশ কেন্দ্র",
            "categoryEn": "Iconic Hilltop Recreation & Nature Park",
            "categoryBn": "শীর্ষস্থানীয় পাহাড়ি পর্যটন ও অবকাশ কেন্দ্র",
            "descEn": "Gajni Leisure Center (Gajni Obakash Kendra) in Jhenaigati is an iconic nature and amusement park nestled right amidst the scenic slopes of the Garo Hills. Perched on rolling terrain surrounded by natural springs and crystal mountain lakes, the park features a dramatic multi-story observation tower, a thrilling hill cave tunnel, pedal boating facilities, and colorful children's play parks. The summit provides unmatched panoramic views of the green forests of Bangladesh extending seamlessly into the blue mountainous terrain of India. Indigenous Garo and Koch cultural crafts, bamboo handicrafts, and fresh hill pineapples are sold in lively local stalls near the entrance. It is the most celebrated holiday attraction in Sherpur district.",
            "descBn": "ঝিনাইগাতী উপজেলার গারো পাহাড়ের কোলে অবস্থিত গজনী অবকাশ কেন্দ্র শেরপুরের সবচেয়ে জনপ্রিয় ও ঐতিহ্যবাহী পর্যটন কেন্দ্র। উঁচু-নিচু টিলা, পাহাড়ি ঝিরি এবং স্বচ্ছ জলের লেকের মাঝে গড়ে ওঠা এই পার্কে রয়েছে রোমাঞ্চকর পাতালপুরী সুরঙ্গ, আকাশছোঁয়া ওয়াচ টাওয়ার ও ক্যাবল কার সুবিধা। ওয়াচ টাওয়ারের শীর্ষে দাঁড়ালে মেঘালয়ের সুউচ্চ পাহাড় ও বাংলাদেশের সমতল সবুজের মিলনমেলা অপূর্ব দেখায়। আদিবাসী গারো ও কোচদের তৈরি ঐতিহ্যবাহী পোশাক, বাঁশের কারুপণ্য ও সুস্বাদু পাহাড়ি আনারস এখানকার অন্যতম আকর্ষণ। ছুটির দিনে আনন্দঘন মুহূর্ত কাটাতে প্রতিদিন হাজার হাজার ভ্রমণপিপাসু গজনী অবকাশ কেন্দ্রে ভিড় জমান।",
            "locationEn": sh_raw['tour_spots'][1]['location'],
            "locationBn": "গজনী, ঝিনাইগাতী, শেরপুর",
            "mapUrl": sh_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Panihata-Tarani Hills",
            "nameBn": "পানিহাটা-তারানি পাহাড়",
            "categoryEn": "Pristine Mountain Frontier & Untouched Nature",
            "categoryBn": "কুমারী পাহাড়ি সীমান্ত ও প্রাকৃতিক ঝিরিপথ",
            "descEn": "Panihata-Tarani Hills in northern Nalitabari is an untouched ecotourism paradise where rugged green mountain ridges drop steeply into crystal-clear mountain streams right along the international border. Unlike commercialized parks, this location retains untamed wilderness characterized by whispering bamboo forests, wild wildflowers, and dramatic rocky bluffs. Visitors can trek along shallow rocky streams where cool water washes over smooth river pebbles and gaze at the towering blue wall of the Meghalaya plateau rising directly ahead. The serenity, cool mountain breeze, and absence of crowds make it deeply revered among hikers, backpackers, and solitude seekers. It is widely considered the most poetically scenic natural spot in Sherpur.",
            "descBn": "নালিতাবাড়ীর সীমান্ত সংলগ্ন পানিহাটা-তারানি পাহাড় শেরপুরের এক অনাবিষ্কৃত প্রাকৃতিক স্বর্গরাজ্য, যেখানে কুমারী পাহাড়ের কোল ঘেঁষে বয়ে চলেছে স্ফটিকস্বচ্ছ পাহাড়ি নদী। বাণিজ্যিক কোলাহলমুক্ত এই স্থানে রয়েছে সবুজে মোড়া সুউচ্চ টিলা, ঝিরিপথ এবং ওপারে ভারতের মেঘালয় রাজ্যের খাড়া পাথুরে পাহাড়ের বিস্ময়কর বিস্তার। নদীর ঠান্ডা জলে পা ডুবিয়ে বসে থাকা এবং পাথরের ওপর দিয়ে পানি গড়িয়ে পড়ার কলকল ধ্বনি এক অপার্থিব প্রশান্তি এনে দেয়। ট্র্যাকিং ও অ্যাডভেঞ্চারপ্রেমীদের জন্য এই পাহাড়ি পথ ধরে হাঁটা এক রোমাঞ্চকর অভিজ্ঞতা। প্রকৃতির একান্ত সান্নিধ্য পেতে পানিহাটা-তারানি পাহাড় এক অতুলনীয় গন্তব্য।",
            "locationEn": sh_raw['tour_spots'][2]['location'],
            "locationBn": "নালিতাবাড়ী, শেরপুর",
            "mapUrl": sh_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Malijhi Riverbank",
            "nameBn": "মালিঝি নদীতীর",
            "categoryEn": "Meandering Riverfront Promenade",
            "categoryBn": "স্নিগ্ধ পাহাড়ি নদীতীর ও গ্রামীণ নিসর্গ",
            "descEn": "Originating in the Garo Hills and winding gently through the heart of Sherpur district, the Malijhi Riverbank offers a serene countryside escape. Characterized by curving sandbars, gentle water currents, and shade-giving bamboo groves along its embankments, the river serves as a vital irrigation artery for rural farmers. Strolling down the riverbank in the late afternoon allows travelers to watch local wooden dinghies navigate the current and witness villagers tending mustard and paddy fields. The open river horizon provides beautiful vantage points for catching glowing sunsets over rural water reflections. It offers an authentic, relaxing taste of peaceful riverside life in northern Bengal.",
            "descBn": "গারো পাহাড় থেকে উৎপন্ন হয়ে শেরপুরের বুক চিরে প্রবাহিত হওয়া মালিঝি নদী এ অঞ্চলের এক অত্যন্ত মনোরম পাহাড়ি নদী। নদীর দুই তীরে গড়ে ওঠা বালুচর, বাঁশঝাড় ও সবুজ ফসলের মাঠ এক চিরন্তন শান্ত রূপ ধারণ করে আছে। বিকেলের মিষ্টি রোদে নদীর পাড় ধরে হাঁটলে ঠান্ডা বাতাস দেহ-মন জুড়িয়ে দেয় এবং স্থানীয় কৃষকদের কর্মব্যস্ত জীবন প্রত্যক্ষ করা যায়। নদীর শান্ত জলে সূর্যের রক্তিম আভার প্রতিফলন আলোকচিত্রীদের জন্য এক অপূর্ব দৃশ্য উপহার দেয়। শহরের ক্লান্তি ভুলে গ্রামীণ নদীর আসল রূপ ও শান্তিময় পরিবেশ উপভোগ করতে মালিঝি নদীতীর এক চমৎকার স্থান।",
            "locationEn": sh_raw['tour_spots'][3]['location'],
            "locationBn": "শেরপুর জেলা নদীতীর, শেরপুর",
            "mapUrl": sh_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Bhogai River and Border Scenery",
            "nameBn": "ভোগাই নদী ও সীমান্ত নিসর্গ",
            "categoryEn": "Pebble-Strewn Mountain River & Border Vista",
            "categoryBn": "স্বচ্ছ পাহাড়ি নদী ও সীমান্ত প্রাকৃতিক দৃশ্যপট",
            "descEn": "The Bhogai River and Border Scenery in the Nalitabari frontier is an exhilarating natural attraction where the turbulent mountain river rushes down from the Meghalaya plateau into Bangladesh over white sand and river rocks. Renowned for its crystalline cool waters and rich deposits of mountain sand and pebbles, the river is constantly alive with traditional stone collectors navigating wooden boats against the gentle rapids. Standing on the riverbank, observers enjoy an unobstructed view of the majestic green mountain wall towering right behind the border fence. The rushing sound of water over rocks combined with fresh mountain air creates an invigorating, restorative environment. It is an unforgettable highlight of visiting Sherpur's northern borderlands.",
            "descBn": "নালিতাবাড়ী সীমান্তে অবস্থিত ভোগাই নদী ও এর চারপাশের প্রাকৃতিক দৃশ্যপট শেরপুরের অন্যতম প্রধান আকর্ষণ, যেখানে পাহাড় থেকে নেমে আসা নদীটি সমতলে এসে শান্ত রূপ ধারণ করেছে। পাহাড়ি বালু ও চকচকে পাথরে ভরা এই নদীর স্বচ্ছ জলে পা ভেজালে ক্লান্তি এক মুহূর্তে দূর হয়ে যায়। স্থানীয় পাথর সংগ্রহকারী ও মাঝিদের কর্মচাঞ্চল্য নদীর বুকে এক জীবন্ত ছবি তৈরি করে। নদীর ওপারে দাঁড়িয়ে থাকা মেঘালয়ের সুউচ্চ সবুজ পাহাড়ের দৃশ্য যেন চোখের সামনে এক বিশাল জীবন্ত পোস্টার। পাহাড়ের বাতাস আর নদীপ্রবাহের কলতান উপভোগ করতে ভোগাই নদীর তীর ভ্রমণপ্রেমীদের কাছে অত্যন্ত প্রিয়।",
            "locationEn": sh_raw['tour_spots'][4]['location'],
            "locationBn": "নালিতাবাড়ী/ঝিনাইগাতী সীমান্ত এলাকা, শেরপুর",
            "mapUrl": sh_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('sherpur', sherpur_data)

# ==========================================
# 8. JASHORE
# ==========================================
j_raw = all_data['jashore']
jashore_data = {
    "slug": "jashore",
    "en": "Jashore",
    "bn": "যশোর",
    "hero_title_en": "Jashore Literary Cradle, Godkhali Flower Capital & Baor Wetlands",
    "hero_title_bn": "যশোরের মাইকেল মধুসূদন স্মৃতি, গদখালীর ফুলের রাজধানী ও বাওড় প্রকৃতি",
    "hero_sub_en": "Madhupalli birthplace of Michael Madhusudan Dutt, vibrant floral fields of Godkhali, and ancient Bharat Bhayna archaeological stupas.",
    "hero_sub_bn": "মহাকবি মাইকেল মধুসূদন দত্তের স্মৃতিবিজড়িত মধুপল্লী, গদখালীর বর্ণিল ফুলের সাম্রাজ্য ও প্রাচীন ভরত ভায়না বৌদ্ধ স্তূপ।",
    "tagline_en": "The first liberated district of Bangladesh, renowned as the flower capital of the nation at Godkhali, birthplace of epic poet Michael Madhusudan Dutt, and home to scenic oxbow lakes.",
    "tagline_bn": "বাংলাদেশের প্রথম মুক্ত জেলা, যা গদখালীর সুবাসিত ফুলের বাগান, কপোতাক্ষ নদের তীরে মহাকবি মধুসূদনের মধুপল্লী, প্রাচীন চাঁচড়া শিব মন্দির ও বিশাল বাওড়ের জন্য পরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/jashore/carousel-1.webp",
            "titleEn": "Michael Madhusudan Dutt Birthplace (Madhupalli)",
            "titleBn": "মাইকেল মধুসূদন দত্তের জন্মভূমি (মধুপল্লী)",
            "subtitleEn": "Historic mansion in Sagardari on the banks of Kapotakkho River honoring the pioneer of modern Bengali epic poetry",
            "subtitleBn": "কপোতাক্ষ নদের তীরে সাগরদাঁড়ির স্মৃতিধন্য বাড়ি যেখানে আধুনিক বাংলা সাহিত্যের মহাকবি জন্মগ্রহণ করেছিলেন"
        },
        {
            "id": 2,
            "image": "images/districts/jashore/carousel-2.webp",
            "titleEn": "Godkhali Flower Market & Endless Blossoming Fields",
            "titleBn": "গদখালীর ফুলের বাজার ও দিগন্তজোড়া ফুলের মাঠ",
            "subtitleEn": "Flower capital of Bangladesh in Jhikargachha carpeted with roses, gerberas, tuberoses, and marigolds",
            "subtitleBn": "ঝিকরগাছার সুবিশাল ফুলের বাগান যা প্রতিদিন ভোরে দেশের বৃহত্তম ও বর্ণিল ফুলের বাজারে পরিণত হয়"
        },
        {
            "id": 3,
            "image": "images/districts/jashore/carousel-3.webp",
            "titleEn": "Chanchra Shiva Temple Terracotta Heritage",
            "titleBn": "চাঁচড়া শিব মন্দিরের প্রাচীন টেরাকোটা",
            "subtitleEn": "1668 AD historic at-chala terracotta brick temple built by Raja Manohar Roy in Jashore Sadar",
            "subtitleBn": "১৬৬৮ খ্রিস্টাব্দে রাজা মনোহর রায় কর্তৃক নির্মিত আটচালা স্থাপত্যের ঐতিহাসিক পোড়ামাটির মন্দির"
        },
        {
            "id": 4,
            "image": "images/districts/jashore/carousel-4.webp",
            "titleEn": "Jhanpa Baor Floating Bridge & Oxbow Water Horizon",
            "titleBn": "ঝাঁপা বাওড়ের ভাসমান সেতু ও স্বচ্ছ জলরাশি",
            "subtitleEn": "Massive freshwater oxbow lake in Monirampur famous for its community-engineered floating bridge",
            "subtitleBn": "মণিরামপুরের সুবিশাল প্রাকৃতিক বাওড় যা প্লাস্টিক ড্রামের ওপর নির্মিত দীর্ঘতম ভাসমান সেতুর জন্য পরিচিত"
        },
        {
            "id": 5,
            "image": "images/districts/jashore/carousel-5.webp",
            "titleEn": "Bharat Bhayna Archaeological Stupa Mound",
            "titleBn": "ভরত ভায়না প্রাচীন প্রত্নতাত্ত্বিক বৌদ্ধ স্তূপ",
            "subtitleEn": "5th-century Gupta-era colossal cruciform brick stupa rising majestically beside the riverbed in Keshabpur",
            "subtitleBn": "কেশবপুরে অবস্থিত গুপ্ত যুগের পঞ্চম শতাব্দীর বিশালাকার ঐতিহাসিক বৌদ্ধ স্তূপের প্রত্নস্থল"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Michael Madhusudan Dutt Birthplace (Madhupalli)",
            "nameBn": "মাইকেল মধুসূদন দত্তের জন্মভিটা (মধুপল্লী)",
            "categoryEn": "National Literary Heritage Memorial",
            "categoryBn": "জাতীয় সাহিত্যিক স্মৃতিকেন্দ্র ও জাদুঘর",
            "descEn": "Madhupalli in Sagardari, Keshabpur, is the sacred ancestral estate where Michael Madhusudan Dutt, the monumental pioneer of modern Bengali poetry and sonnet forms, was born in 1824. Flanking the historic Kapotakkho River that inspired his immortal verses of exile and longing, the sprawling estate has been preserved as a national cultural memorial and museum. The colonial-era residential mansion features vintage family furniture, original handwritten letters, rare first-edition publications of Meghnad Badh Kavya, and antique sculptures. The surrounding gardens include the famous 'Badam' almond tree where the poet read in childhood and a paved memorial ghat on the riverbank. Every year in January, the Madhumela festival attracts literary scholars and millions of poetry lovers from across Bengal.",
            "descBn": "কেশবপুর উপজেলার সাগরদাঁড়িতে অবস্থিত মধুপল্লী আধুনিক বাংলা সাহিত্যের মহাকবি ও সনেটের জনক মাইকেল মধুসূদন দত্তের পবিত্র পৈতৃক জন্মভিটা। ১৮২৪ সালে এই বাড়িতেই কবির জন্ম হয় এবং সংলগ্ন প্রমত্তা কপোতাক্ষ নদ তাঁর বিখ্যাত 'কপোতাক্ষ নদ' সনেট রচনার অনুপ্রেরণা যুগিয়েছিল। প্রাচীন চুন-সুরকির সুরম্য বাসভবনটিকে বর্তমানে একটি সমৃদ্ধ জাতীয় জাদুঘরে রূপান্তর করা হয়েছে, যেখানে কবির ব্যবহৃত প্রাচীন আসবাবপত্র, দুর্লভ পাণ্ডুলিপি ও আলোকচিত্র সংরক্ষিত আছে। বাড়ির আঙিনায় রয়েছে কবির স্মৃতিবিজড়িত বাদামগাছ এবং কপোতাক্ষের শানবাঁধানো ঘাট। প্রতি বছর জানুয়ারি মাসে আয়োজিত সপ্তাহব্যাপী মধুমেলো সাহিত্যপ্রেমীদের মিলনমেলায় পরিণত হয়। বাংলা সাহিত্যের অনুরাগীদের জন্য এটি এক পরম তীর্থস্থান।",
            "locationEn": j_raw['hist_spots'][0]['location'],
            "locationBn": "সাগরদাঁড়ি, কেশবপুর, যশোর",
            "mapUrl": j_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Jashore Collectorate Building",
            "nameBn": "যশোর কালেক্টরেট ভবন",
            "categoryEn": "Colonial Administrative Heritage Monument",
            "categoryBn": "উপনিবেশিক প্রশাসনিক স্থাপত্য ও ঐতিহ্য ভবন",
            "descEn": "The Jashore Collectorate Building in Daratana is one of the oldest surviving colonial administrative headquarters in Bangladesh, having served as the seat of British district governance since the late eighteenth century. Designed with imposing Indo-Saracenic and neoclassical architectural elements, the massive two-story brick edifice features soaring arcaded verandas, fluted pilasters, high ceilings, and grand pedimented porticos. Surrounding the historic secretariat are centuries-old rain trees and the famous Collectorate Lake, which provides a serene reflecting pool for the historic architecture. On December 6, 1971, Jashore made history as the very first district of Bangladesh to be liberated from occupying forces, with public celebrations centered right in front of this landmark. It remains a proud symbol of civic history and heritage.",
            "descBn": "যশোর শহরের দড়াটানায় অবস্থিত কালেক্টরেট ভবন অবিভক্ত বাংলার অন্যতম প্রাচীন ও দৃষ্টিনন্দন উপনিবেশিক প্রশাসনিক ভবন। অষ্টাদশ শতাব্দীর শেষভাগে নির্মিত দোতলা এই বিশালাকার লাল ইটের ভবনে রয়েছে সুউচ্চ খিলানযুক্ত বারান্দা, অলংকৃত স্তম্ভ এবং ঐতিহ্যবাহী কাঠের কারুকাজ। ভবনের সামনে থাকা শতাব্দীপ্রাচীন কড়ই গাছ এবং কালেক্টরেট পার্কের শান্ত দীঘি ভবনটির গাম্ভীর্য আরও বাড়িয়ে দিয়েছে। ১৯৭১ সালের ৬ ডিসেম্বর যশোর বাংলাদেশের প্রথম হানাদারমুক্ত জেলা হিসেবে স্বাধীন হওয়ার ঐতিহাসিক গৌরব অর্জন করে এবং এই চত্বরেই বিজয়ের প্রথম পতাকা উত্তোলিত হয়েছিল। প্রশাসনিক ঐতিহ্যের পাশাপাশি মুক্তিযুদ্ধের এক জীবন্ত স্মারক হিসেবে এই ভবনটি অত্যন্ত মর্যাদাপূর্ণ।",
            "locationEn": j_raw['hist_spots'][1]['location'],
            "locationBn": "দড়াটানা, যশোর শহর, যশোর",
            "mapUrl": j_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Chanchra Shiva Temple",
            "nameBn": "চাঁচড়া শিব মন্দির",
            "categoryEn": "Terracotta At-Chala Heritage Temple",
            "categoryBn": "ঐতিহাসিক আটচালা পোড়ামাটির শিব মন্দির",
            "descEn": "Constructed in 1668 AD by Raja Manohar Roy, a prominent ruler of the historic Chanchra zamindar dynasty, the Chanchra Shiva Temple is an extraordinary specimen of seventeenth-century Bengal brick architecture. Designed in the indigenous 'At-Chala' (eight-roofed) architectural idiom, the temple features a four-sloped lower roof topped by a matching miniature upper chamber. The entire front facade is adorned with deeply sculpted terracotta relief tiles illustrating scenes from Hindu epics, warrior processions, floral vines, and contemporary feudal life. The intricate craftsmanship demonstrates the remarkable height achieved by regional artists under royal zamindari patronage. Though centuries of weather have weathered the surfaces, the surviving terracotta panels remain a source of profound fascination for art historians.",
            "descBn": "১৬৬৮ খ্রিস্টাব্দে চাঁচড়ার রাজা মনোহর রায় কর্তৃক প্রতিষ্ঠিত চাঁচড়া শিব মন্দির সপ্তদশ শতাব্দীর বাংলার পোড়ামাটির স্থাপত্যের এক অনন্য শিল্পকর্ম। ঐতিহ্যবাহী 'আটচালা' রীতিতে নির্মিত এই মন্দিরে রয়েছে চারচালা ভিত্তির ওপর আরেকটি ক্ষুদ্রাকার চারচালা ছাদের নান্দনিক সংযোজন। মন্দিরের সম্মুখভাগ জুড়ে থাকা পোড়ামাটির ফলকগুলোতে রামায়ণ, মহাভারত, পৌরাণিক যুদ্ধ ও তৎকালীন গ্রামীণ জীবনের দৃশ্য অত্যন্ত নিপুণভাবে খোদাই করা রয়েছে। মধ্যযুগীয় বাংলার শিল্পরীতি ও সামন্ত রাজাদের ধর্মীয় পৃষ্ঠপোষকতার এক অসাধারণ স্মারক এই মন্দির। প্রত্নতাত্ত্বিক গুরুত্ব ও ঐতিহাসিক সৌন্দর্যের কারণে চাঁচড়া শিব মন্দির ইতিহাসানুরাগীদের কাছে অত্যন্ত আকর্ষণীয়।",
            "locationEn": j_raw['hist_spots'][2]['location'],
            "locationBn": "চাঁচড়া, যশোর সদর, যশোর",
            "mapUrl": j_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Dhiraj Bhattacharya's House",
            "nameBn": "ধীরাজ ভট্টাচার্যের বাড়ি",
            "categoryEn": "Literary & Cinematic Heritage Residence",
            "categoryBn": "সাহিত্যিক ও চিত্রনায়কের ঐতিহাসিক জন্মভিটা",
            "descEn": "Located in Panjia village of Keshabpur Upazila, this historic brick residence was the birthplace and ancestral home of Dhiraj Bhattacharya (1905–1959), a celebrated pioneering actor of early Bengali cinema and renowned author. Renowned as a dashing romantic hero in pre-partition Calcutta silent movies and talkies, Bhattacharya also penned the celebrated autobiographical memoir 'Jakhon Police Chhilam' (When I Was a Policeman), recounting his real-life posting in Teknaf. The ancestral compound features colonial-style brick living quarters, an inner courtyard, and traditional village ponds shaded by mango orchards. Literary tourists and film enthusiasts visit the tranquil village to pay homage to an iconic cultural figure whose creative footprint spanned literature, law enforcement, and cinema.",
            "descBn": "কেশবপুর উপজেলার ঐতিহ্যবাহী পাঁজিয়া গ্রামে অবস্থিত এই প্রাচীন বাসভবনটি বাংলা চলচ্চিত্রের অগ্রপথিক অভিনেতা ও প্রখ্যাত লেখক ধীরাজ ভট্টাচার্যের (১৯০৫–১৯৫৯) পৈতৃক ভিটা। অবিভক্ত বাংলার নির্বাক ও সবাক চলচ্চিত্রের অন্যতম সুদর্শন নায়ক হিসেবে তিনি ব্যাপক জনপ্রিয়তা অর্জন করেছিলেন এবং তাঁর লেখা 'যখন পুলিশ ছিলাম' গ্রন্থটি বাংলা সাহিত্যের এক কালজয়ী আত্মজীবনীমূলক সৃষ্টি। চুন-সুরকির তৈরি এই পুরোনো বাড়িতে রয়েছে স্মৃতিবিজড়িত বারান্দা, উঠান এবং প্রাচীন পুকুর যা অতীতের স্মৃতি জাগিয়ে তোলে। চলচ্চিত্রের ইতিহাস ও সাহিত্যের অনুরাগী পর্যটকদের কাছে নিভৃত পাঁজিয়া গ্রামের এই বাড়িটি এক পরম আবেগের স্থান।",
            "locationEn": j_raw['hist_spots'][3]['location'],
            "locationBn": "পাঁজিয়া, কেশবপুর, যশোর",
            "mapUrl": j_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Bharat Bhayna Archaeological Mound",
            "nameBn": "ভরত ভায়না প্রত্নতাত্ত্বিক ঢিবি",
            "categoryEn": "Ancient Gupta-Era Buddhist Stupa Sanctuary",
            "categoryBn": "গুপ্ত আমলের প্রাচীন বৌদ্ধ স্তূপ ও প্রত্নস্থল",
            "descEn": "Bharat Bhayna Archaeological Mound in Keshabpur is a monumental fifth-century Buddhist brick stupa complex, dating back to the illustrious Gupta Empire and post-Gupta periods of Bengal. Excavations conducted by the Department of Archaeology unearthed a colossal cruciform temple foundation rising in tiered brick terraces with hundreds of interlocking cellular chambers. The structure originally supported a soaring ceremonial dome and was encircled by a wide circumambulatory pathway for monks and pilgrims. Intricate stepped masonry, massive burnt-clay bricks, and surviving decorative cornices demonstrate advanced classical civil engineering capabilities. Located beside the dried ancient bed of the Bhadra River, Bharat Bhayna stands as one of the most significant pre-medieval Buddhist archaeological monuments in southwest Bangladesh.",
            "descBn": "কেশবপুর উপজেলার ভদ্রা নদীর প্রাচীন অববাহিকায় অবস্থিত ভরত ভায়না ঢিবি পঞ্চম শতাব্দীর গুপ্ত যুগের এক বিশালাকার ও সুপ্রাচীন বৌদ্ধ স্তূপের প্রত্নতাত্ত্বিক নিদর্শন। প্রত্নতাত্ত্বিক খননের মাধ্যমে এখানে আবিষ্কৃত হয়েছে স্তরে স্তরে নির্মিত বিশাল ইটের স্তূপ, যাতে রয়েছে বহু পরস্পর সংযুক্ত প্রকোষ্ঠ এবং প্রদক্ষিণ পথ। প্রাচীনকালে এটি এক সুউচ্চ প্রার্থনাস্থল ও বৌদ্ধ জ্ঞানচর্চার কেন্দ্র হিসেবে ব্যবহৃত হতো যা শতাব্দীর পর শতাব্দী মাটির নিচে চাপা পড়েছিল। ব্যবহৃত বিশালাকার প্রাচীন ইট এবং সূক্ষ্ম প্রকৌশল প্রাচীন বাংলার সমৃদ্ধ স্থাপত্যবিদ্যার পরিচয় দেয়। দক্ষিণ-পশ্চিমাঞ্চলের প্রাচীন বৌদ্ধ সভ্যতার শিকড় অনুসন্ধানে ভরত ভায়না এক ঐতিহাসিক বিস্ময়।",
            "locationEn": j_raw['hist_spots'][4]['location'],
            "locationBn": "কেশবপুর, যশোর",
            "mapUrl": j_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Godkhali Flower Market and Flower Fields",
            "nameBn": "গদখালীর ফুলের বাজার ও ফুলের মাঠ",
            "categoryEn": "National Flower Capital & Agro-Tourism Wonderland",
            "categoryBn": "বাংলাদেশের ফুলের রাজধানী ও বর্ণিল ফুলের রাজ্য",
            "descEn": "Godkhali in Jhikargachha Upazila is celebrated as the undisputed 'Flower Capital of Bangladesh', supplying nearly seventy percent of the nation's commercial flowers from miles of vibrant blossoming fields. Stretching across villages like Panisara and Gadadharpur, the landscape is blanketed in blooming carpets of scarlet roses, purple gerberas, fragrant white tuberoses (rajnigandha), gladioli, and golden marigolds. At the crack of dawn, the bustling Godkhali wholesale flower market comes alive as hundreds of farmers arrive carrying vibrant bundles of fresh-cut flowers on bicycles and vans. Tourists flock here to stroll through fragrant flower farms, capture spectacular colorful photographs, and purchase fresh bouquets straight from the fields. It is a sensory wonderland and the crown jewel of tourism in Jashore.",
            "descBn": "ঝিকরগাছা উপজেলার গদখালী বাংলাদেশের অবিসংবাদিত 'ফুলের রাজধানী', যা দেশের প্রায় ৭০ শতাংশ ফুলের চাহিদা একাই পূরণ করে থাকে। পানিসারা ও সংলগ্ন গ্রামগুলোতে মাইলের পর মাইল বিস্তৃত জমিতে ফুটে থাকে লাল গোলাপ, জারবেরা, রজনীগন্ধা, গ্লাডিওলাস ও গাঁদা ফুলের বর্ণিল সমাহার। প্রতিদিন সূর্য ওঠার সাথে সাথে গদখালী পাইকারি বাজারে সাইকেল ও ভ্যানে করে তাজা ফুলের পসরা নিয়ে হাজির হন চাষীরা, যা এক অপূর্ব রঙিন দৃশ্যের জন্ম দেয়। হাজার হাজার পর্যটক এখানে আসেন ফুলের খেতে হেঁটে ছবি তুলতে, মিষ্টি সুবাস নিতে এবং সুলভ মূল্যে তাজা ফুল সংগ্রহ করতে। রঙের মেলা ও সুবাসিত প্রকৃতির এমন অপরূপ রূপ বাংলাদেশের আর কোথাও দেখা যায় না।",
            "locationEn": j_raw['tour_spots'][0]['location'],
            "locationBn": "গদখালী, ঝিকরগাছা, যশোর",
            "mapUrl": j_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Jhanpa Baor",
            "nameBn": "ঝাঁপা বাওড়",
            "categoryEn": "Vast Oxbow Lake & Famous Floating Bridge",
            "categoryBn": "বিশাল প্রাকৃতিক বাওড় ও দীর্ঘতম ভাসমান সেতু",
            "descEn": "Jhanpa Baor in Monirampur Upazila is a breathtaking horseshoe-shaped oxbow lake (baor) that gained nationwide renown for hosting the longest human-engineered floating bridge in Bangladesh. Constructed innovatively by local villagers using linked plastic drums and iron railings, the floating bridge spans nearly a thousand feet across the shimmering waters, connecting remote island communities to the mainland. The lake stretches for miles across lush countryside, offering tranquil boat excursions, rich freshwater fisheries, and peaceful waterfront viewpoints. During sunsets, the calm waters reflect dramatic skies while soft breezes ripple through blooming water lilies. It stands as an inspiring monument to community enterprise set against stunning natural wetland beauty.",
            "descBn": "মণিরামপুর উপজেলার ঝাঁপা বাওড় এক সুবিশাল অশ্বখুরাকৃতি প্রাকৃতিক জলাভূমি, যা বাংলাদেশের দীর্ঘতম ভাসমান সেতুর জন্য দেশজুড়ে পরিচিতি লাভ করেছে। স্থানীয় গ্রামবাসীদের নিজস্ব উদ্যোগে শত শত প্লাস্টিকের ড্রাম ও লোহার কাঠামোর ওপর নির্মিত এই ভাসমান সেতুটি বাওড়ের এপার-ওপারের মানুষকে যুক্ত করেছে। বাওড়ের শান্ত স্বচ্ছ জলরাশি এবং চারপাশের সবুজ গ্রামীন পরিবেশ পর্যটকদের দারুণভাবে আকর্ষণ করে। নৌকায় চড়ে বাওড়ের বুকে ভেসে বেড়ানো এবং ভাসমান সেতুর ওপর দিয়ে হেঁটে বাতাস উপভোগ করা এক অনন্য রোমাঞ্চকর অভিজ্ঞতা। গ্রামীণ প্রযুক্তি ও প্রকৃতির চমৎকার সমন্বয় দেখতে ঝাঁপা বাওড় ভ্রমণকারীদের প্রিয় ঠিকানা।",
            "locationEn": j_raw['tour_spots'][1]['location'],
            "locationBn": "ঝাঁপা, মণিরামপুর, যশোর",
            "mapUrl": j_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Gadadharpur Baor",
            "nameBn": "গদাধরপুর বাওড়",
            "categoryEn": "Serene Oxbow Wetland & Aquatic Sanctuary",
            "categoryBn": "স্নিগ্ধ প্রাকৃতিক বাওড় ও জলজ জীববৈচিত্র্য",
            "descEn": "Nestled near the fertile borderlands of Chougachha Upazila, Gadadharpur Baor is a pristine oxbow wetland celebrated for its crystalline waters and thriving freshwater aquatic ecosystem. Enclosed by whispering bamboo groves, date-palm trees, and green paddy fields, the baor serves as a community sanctuary for indigenous freshwater fish species and local biodiversity. Anglers and nature lovers gather on its peaceful grassy shores to enjoy peaceful fishing sessions and observe water birds such as kingfishers, herons, and cormorants plunging into the glassy water. Traditional wooden rowboats provide gentle rides across the tranquil surface, far away from mechanized city noise. It is an idyllic, rejuvenating eco-retreat in rural Jashore.",
            "descBn": "চৌগাছা উপজেলার শান্ত পল্লি প্রকৃতির মাঝে অবস্থিত গদাধরপুর বাওড় এক স্নিগ্ধ ও অক্ষত প্রাকৃতিক জলাশয়। বাওড়ের স্বচ্ছ জলরাশি, চারপাশের খেজুর গাছের সারি ও সবুজ ধানের প্রান্তর গ্রামীণ বাংলার এক চিরায়ত সুন্দর ছবি তুলে ধরে। এই বাওড়ে দেশীয় প্রজাতির প্রচুর মাছ পাওয়া যায় এবং মাছরাঙা, বক ও পানকৌড়ির মতো জলজ পাখির অবাধ বিচরণ চোখে পড়ে। শহরের কোলাহল ছেড়ে শান্ত পরিবেশে ছিপ ফেলে মাছ ধরা কিংবা নৌকায় চড়ে অলস সময় কাটাতে প্রকৃতিপ্রেমীরা এখানে আসেন। স্নিগ্ধ বাতাস ও গ্রামীণ নিসর্গের নিবিড় প্রশান্তি পেতে গদাধরপুর বাওড় এক অপূর্ব স্থান।",
            "locationEn": j_raw['tour_spots'][2]['location'],
            "locationBn": "গদাধরপুর, চৌগাছা, যশোর",
            "mapUrl": j_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Benapole Land Port Area",
            "nameBn": "বেনাপোল স্থলবন্দর এলাকা",
            "categoryEn": "International Border Crossing & Trade Gateway",
            "categoryBn": "আন্তর্জাতিক স্থলবন্দর ও সীমান্ত প্রবেশদ্বার",
            "descEn": "Benapole Land Port in Sharsha Upazila is the largest and most vital international land crossing connecting Bangladesh with India, handling over ninety percent of all cross-border passenger and commercial road traffic. Situated directly across from Petrapole in West Bengal, the bustling port area features modern passenger immigration terminals, expansive cargo freight yards, and dynamic commercial markets. In the late afternoon, the Joint Retreat Ceremony conducted by the Border Guard Bangladesh (BGB) and India's BSF at the zero point provides a patriotic, ceremonial spectacle popular with domestic tourists. Nearby duty-free markets and bazaars offer regional culinary treats, including warm Jashore date-jaggery sweets. It offers a lively, historic look at international border connectivity.",
            "descBn": "শার্শা উপজেলায় অবস্থিত বেনাপোল স্থলবন্দর বাংলাদেশ ও ভারতের মধ্যকার বৃহত্তম এবং সর্বাধিক গুরুত্বপূর্ণ আন্তর্জাতিক স্থল সীমান্ত বন্দর। প্রতিদিন হাজার হাজার পাসপোর্টধারী যাত্রী এবং শত শত পণ্যবাহী ট্রাকের আনাগোনায় এই বন্দর এলাকা চব্বিশ ঘণ্টা প্রাণবন্ত থাকে। সীমান্তের শূন্যরেখায় বর্ডার গার্ড বাংলাদেশ (বিজিবি) ও ভারতীয় সীমান্তরক্ষী বাহিনীর (বিএসএফ) প্রতিদিনের সম্মিলিত ফ্ল্যাগ রিট্রিট প্যারেড দেখতে বহু পর্যটক বিকেলে এখানে জড়ো হন। বন্দর সংলগ্ন বাজারে যশোরের বিখ্যাত খেজুরের গুড়ের তৈরি সন্দেশ ও মুখরোচক খাবার পাওয়া যায়। আন্তর্জাতিক সীমান্ত জীবনের অভিজ্ঞতা এবং বাণিজ্যের গতিশীল রূপ দেখতে বেনাপোল এক আকর্ষণীয় স্থান।",
            "locationEn": j_raw['tour_spots'][3]['location'],
            "locationBn": "বেনাপোল, শার্শা, যশোর",
            "mapUrl": j_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Jashore Municipal Park",
            "nameBn": "যশোর পৌর পার্ক",
            "categoryEn": "Civic Lake Promenade & Urban Green Sanctuary",
            "categoryBn": "পৌর পার্ক, লেক ওয়াকওয়ে ও বিনোদন কেন্দ্র",
            "descEn": "Situated in the central urban heart of Jashore municipality, the Municipal Park serves as the premier civic green sanctuary and recreational space for town residents and visiting tourists. Bordering a tranquil heritage lake, the park features paved jogging boulevards, colorful seasonal flower beds, shaded gazebos, and illuminated night fountains. Children enjoy well-equipped playground equipment and pedal-boat rides on the calm lake waters, while families stroll along the water's edge under mature canopy trees. Street vendors outside the gates sell authentic local delicacies, including the famed Jashore kanchagolla, jilapi, and spiced puffed rice. It provides a welcoming, family-friendly urban leisure oasis right within the city.",
            "descBn": "যশোর শহরের প্রাণকেন্দ্রে অবস্থিত পৌর পার্ক স্থানীয় নাগরিক ও ভ্রমণকারীদের জন্য এক চমৎকার সবুজ বিনোদন কেন্দ্র। সুন্দর একটি শান্ত লেক ঘিরে গড়ে ওঠা এই পার্কে রয়েছে পাকা হাঁটার পথ, ফোয়ারা, ফুলের বাগান এবং ছায়াঘেরা বসার বেঞ্চ। লেকের জলে প্যাডেল বোট চালানো এবং শিশুদের খেলার জন্য আকর্ষণীয় রাইড পার্কটিকে সবসময় আনন্দমুখর রাখে। বিকেলে ও সন্ধ্যায় মুক্ত বাতাস উপভোগ করতে শহরের বহু মানুষ পরিবার নিয়ে এখানে সমবেত হন। পার্কের বাইরে পাওয়া যায় যশোরের বিখ্যাত মিষ্টি, কাঁচাগোল্লা ও গরম গরম জিলাপি। শহরের ভেতরেই কিছুটা সময় স্বস্তিতে কাটাতে এই পার্কটি অত্যন্ত জনপ্রিয়।",
            "locationEn": j_raw['tour_spots'][4]['location'],
            "locationBn": "যশোর শহর, যশোর",
            "mapUrl": j_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('jashore', jashore_data)

# ==========================================
# 9. JHALOKATHI
# ==========================================
jh_raw = all_data['jhalokathi']
jhalokathi_data = {
    "slug": "jhalokathi",
    "en": "Jhalokathi",
    "bn": "ঝালকাঠি",
    "hero_title_en": "Jhalokathi Riverine Venice, Gabkhan Canal & Floating Guava Markets",
    "hero_title_bn": "ঝালকাঠির ভাসমান পেয়ারা বাজার, গাবখান চ্যানেল ও সুগন্ধার রূপ",
    "hero_sub_en": "Asia's largest floating guava markets at Bhimruli, iconic Gabkhan Channel 'Suez of Bengal', and historic river ports.",
    "hero_sub_bn": "ভিমরুলির বিখ্যাত ভাসমান পেয়ারার হাট, বাংলার সুয়েজ খাল খ্যাত গাবখান চ্যানেল ও সুগন্ধা নদীর মনোহর রূপ।",
    "tagline_en": "The enchanting riverine heart of southern Bengal, famed globally as the 'Venice of the East' for canal networks, floating agriculture, and the majestic Gabkhan Channel.",
    "tagline_bn": "দক্ষিণাঞ্চলের নদীমাতৃক রানী ও প্রাচ্যের ভেনিসখ্যাত জেলা, যা ভিমরুলির শতাব্দীপ্রাচীন ভাসমান পেয়ারার হাট, গাবখান চ্যানেল, সুগন্ধা ও বিষখালী নদীর অপূর্ব রূপের জন্য পরিচিত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/jhalokathi/carousel-1.webp",
            "titleEn": "Gabkhan Channel 'Suez of Bengal' Waterway",
            "titleBn": "বাংলার সুয়েজ খালখ্যাত গাবখান চ্যানেল",
            "subtitleEn": "Historic man-made international shipping canal dug during the colonial era connecting the Mongla and Barishal river routes",
            "subtitleBn": "উপনিবেশিক আমলে খননকৃত গভীর নৌপথ যা বিষখালী ও সুগন্ধা নদীকে যুক্ত করে সৃষ্টি করেছে নৌবাণিজ্যের বিস্ময়"
        },
        {
            "id": 2,
            "image": "images/districts/jhalokathi/carousel-2.webp",
            "titleEn": "Floating Guava Market Canal Confluence",
            "titleBn": "ভিমরুলির বিশ্বখ্যাত ভাসমান পেয়ারার হাট",
            "subtitleEn": "Asia's premier floating agricultural bazaar at Bhimruli where hundreds of wooden canoes trade crisp green guavas",
            "subtitleBn": "খালের মোহনায় শত শত ডিঙি নৌকায় পেয়ারা কেনাবেচার অপরূপ শতবর্ষী ঐতিহ্যবাহী ভাসমান বাজার"
        },
        {
            "id": 3,
            "image": "images/districts/jhalokathi/carousel-3.webp",
            "titleEn": "Sugandha Riverfront Historic Launch Terminal",
            "titleBn": "সুগন্ধা নদীর ঐতিহাসিক লঞ্চ ঘাট ও নদীতীর",
            "subtitleEn": "Legendary river-port waterfront of Jhalokathi where grand double-decker passenger launches cruise daily",
            "subtitleBn": "ঐতিহাসিক নদী বন্দরের প্রাণবন্ত নদীতীর যেখানে সুবিশাল যাত্রীবাহী লঞ্চ ও পণ্যবাহী জাহাজের আনাগোনা"
        },
        {
            "id": 4,
            "image": "images/districts/jhalokathi/carousel-4.webp",
            "titleEn": "Bishkhali Riverbank Wide Estuary Panorama",
            "titleBn": "বিষখালী নদীতীরের দিগন্তবিস্তৃত রূপ",
            "subtitleEn": "Mighty southern tidal river flowing towards the Bay of Bengal past coconut groves and tranquil chars",
            "subtitleBn": "নারিকেল বাগান ও পলিমাটির চরাঞ্চল ঘেঁষে সাগরের পানে বয়ে চলা খরস্রোতা বিষখালী নদী"
        },
        {
            "id": 5,
            "image": "images/districts/jhalokathi/carousel-5.webp",
            "titleEn": "Nalchity Historic River-Port Promenade",
            "titleBn": "নলছিটি ঐতিহাসিক নদী বন্দর ও নদীতীর",
            "subtitleEn": "Centuries-old trading terminal on the riverfront celebrated for maritime commerce and tranquil sunset views",
            "subtitleBn": "সুগন্ধার তীরে প্রাচীন বাণিজ্য কেন্দ্র ও গোধূলির রক্তিম আভায় রাঙানো স্নিগ্ধ নদীতীর"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Nalchity Historic River-Port Area",
            "nameBn": "নলছিটি ঐতিহাসিক নদী বন্দর এলাকা",
            "categoryEn": "Colonial Maritime Trading Port",
            "categoryBn": "ঐতিহাসিক নদী বন্দর ও বাণিজ্যিক জনপদ",
            "descEn": "The Nalchity Historic River-Port Area on the banks of the Sugandha River was one of the most prominent nineteenth-century inland shipping ports in southern Bengal. Operating as a pivotal transit hub connecting Kolkata, Dhaka, and the Sundarbans coastal routes, Nalchity bustled with wooden merchant barges laden with betel nuts, rice, salt, and handwoven textiles. Colonial trading godowns, brick custom houses, and historic stepping ghats still line the water's edge. The settlement gave birth to influential merchant communities and cultural patrons who helped shape the maritime commerce of Barishal division. Exploring the quiet old trading alleys offers a nostalgic encounter with the golden era of Bengal's steamship and barge trade.",
            "descBn": "সুগন্ধা নদীর তীরে অবস্থিত নলছিটি ঐতিহাসিক নদী বন্দর এলাকা উনিশ শতকের দক্ষিণ বাংলার অন্যতম প্রধান নৌবাণিজ্য কেন্দ্র ছিল। কলকাতা, ঢাকা এবং উপকূলীয় সুন্দরবনের সাথে সংযোগকারী এই বন্দর দিয়ে সেকালে ধান, পান, সুপারি, লবণ ও তাঁত বস্ত্রের বিশাল বাণিজ্য পরিচালিত হতো। নদীর তীরে আজও দেখা যায় ব্রিটিশ আমলের পুরোনো গুদামঘর, কাচারি এবং শানবাঁধানো পুরোনো ঘাট। এই নৌবন্দরকে কেন্দ্র করেই এই অঞ্চলে বহু প্রভাবশালী বণিক পরিবার ও ঐতিহ্যবাহী ব্যবসাকেন্দ্র গড়ে উঠেছিল। পুরোনো বাজারের অলিগলি দিয়ে হাঁটলে উনিশ শতকের সমৃদ্ধ নদীবাণিজ্যের এক জীবন্ত আবহ অনুভূত হয়।",
            "locationEn": jh_raw['hist_spots'][0]['location'],
            "locationBn": "নলছিটি, ঝালকাঠি",
            "mapUrl": jh_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Jhalokathi Old Launch Terminal",
            "nameBn": "ঝালকাঠি পুরোনো লঞ্চ টার্মিনাল",
            "categoryEn": "Historic Passenger River Port",
            "categoryBn": "ঐতিহাসিক যাত্রীবাহী নৌ টার্মিনাল ও নদীতীর",
            "descEn": "Jhalokathi Old Launch Terminal is a legendary landmark of Bengal's river transportation, situated along the bustling Sugandha riverfront in the district headquarters. For over a century, the terminal served as the principal transit gateway where historic steam paddle-boats (such as the famous 'Rocket Steamer' fleet) and modern double-decker passenger launches connected southern districts to Dhaka and Narayanganj. The terminal area bustles with traditional tea stalls, luggage porter crews, and floating fruit boats selling fresh seasonal produce. The rhythmic sound of ships' horns echoing across the river at dusk evokes the romance of Bengal's riverine heritage. It remains an indelible cultural anchor in the memories of generations of southern travelers.",
            "descBn": "ঝালকাঠি শহরের সুগন্ধা নদীর পাড়ে অবস্থিত পুরোনো লঞ্চ টার্মিনালটি দক্ষিণ বাংলার নদীকেন্দ্রিক যোগাযোগের এক শতাব্দীপ্রাচীন ঐতিহাসিক স্মারক। ব্রিটিশ আমলের ঐতিহ্যবাহী প্যাডেল স্টিমার (রকেট স্টিমার) থেকে শুরু করে আধুনিক বিশালাকার দোতলা লঞ্চের প্রধান ঘাট হিসেবে এটি যুগ যুগ ধরে সেবা দিয়ে আসছে। প্রতিদিন ভোরে ও সন্ধ্যায় যাত্রীদের পদচারণা, কুলি-মজুরদের হাঁকডাক এবং নদীর বুকে ভেসে থাকা নৌকাগুলোর দৃশ্য অত্যন্ত প্রাণবন্ত। গোধূলিলগ্নে নদীর বুকে ভেসে আসা লঞ্চের সুমধুর সাইরেনের শব্দ নদীমাতৃক বাংলার এক চিরচেনা আবহ তৈরি করে। দক্ষিণবঙ্গের মানুষের স্মৃতি ও সংস্কৃতির সাথে এই পুরোনো ঘাটটি ওতপ্রোতভাবে জড়িয়ে আছে।",
            "locationEn": jh_raw['hist_spots'][1]['location'],
            "locationBn": "ঝালকাঠি শহর নদীতীর, ঝালকাঠি",
            "mapUrl": jh_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Gabkhan Channel Historic Route",
            "nameBn": "গাবখান চ্যানেল ঐতিহাসিক নৌপথ",
            "categoryEn": "Historic Man-Made Canal Engineering Marvel",
            "categoryBn": "ঐতিহাসিক কৃত্রিম খাল ও নৌপ্রকৌশল বিস্ময়",
            "descEn": "Dug between 1918 and 1928 under the British colonial administration, the Gabkhan Channel is celebrated globally as the 'Suez Canal of Bengal', engineered to dramatically shorten shipping journeys between Barishal and the Bay of Bengal ports. Cutting directly through eighteen kilometers of deltaic landmass to link the Sugandha and Bishkhali rivers, this deep canal transformed the economic geography of southern Bengal. Ocean-going cargo vessels, oil tankers, and passenger steamers navigate its winding waters daily, bordered by steep lush green embankments and coconut palm canopies. The channel represents an awe-inspiring testament to twentieth-century civil engineering in a dynamic wetland landscape. It stands as a vital international trade conduit and prime sightseeing route.",
            "descBn": "১৯১৮ থেকে ১৯২৮ সালের মধ্যে ব্রিটিশ প্রকৌশলীদের দ্বারা খননকৃত গাবখান চ্যানেলকে এর কৌশলগত গুরুত্বের জন্য 'বাংলার সুয়েজ খাল' বলা হয়। সুগন্ধা ও বিষখালী নদীর মধ্যবর্তী প্রায় ১৮ কিলোমিটার পথ সরাসরি যুক্ত করতে এই গভীর খালটি খনন করা হয়েছিল, যা নৌপথের দূরত্ব প্রায় এক-তৃতীয়াংশ কমিয়ে দেয়। বিশালাকার পণ্যবাহী জাহাজ, তেলবাহী ট্যাংকার ও যাত্রীবাহী লঞ্চ প্রতিনিয়ত এই খালের বুক চিরে চলাচল করে। খালের দুই পাড়ের খাড়া সবুজ ঢাল, নারিকেল গাছের সারি ও শান্ত নিসর্গ এক অপরূপ দৃশ্যপট তৈরি করে। আধুনিক নৌপ্রকৌশল এবং দক্ষিণবঙ্গের অর্থনীতির এক যুগান্তকারী স্মারক এই গাবখান চ্যানেল।",
            "locationEn": jh_raw['hist_spots'][2]['location'],
            "locationBn": "গাবখান চ্যানেল, ঝালকাঠি",
            "mapUrl": jh_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Rajapur Historic Mosque and Shrine Area",
            "nameBn": "রাজাপুর ঐতিহাসিক মসজিদ ও দরবার এলাকা",
            "categoryEn": "Medieval Sacred Religious Sanctuary",
            "categoryBn": "ঐতিহাসিক সুফি দরবার ও প্রাচীন মসজিদ",
            "descEn": "The Rajapur Historic Mosque and Shrine Area preserves the spiritual heritage of early Islamic scholars who journeyed through the forested waterways of southern Bengal in the sixteenth and seventeenth centuries. Nestled amid ancient water bodies and dense fruit orchards, the historic mosques feature lime-mortar brick construction, multi-tiered domes, and ornate floral stucco reliefs. The shrines commemorate revered darweshes who established spiritual sanctuaries, dug drinking water tanks, and promoted intercommunal brotherhood among coastal settlers. Annual Urs festivals draw thousands of devotees who gather to recite devotional poems, distribute charity, and pray for healing. Visiting Rajapur provides an intimate encounter with the deep spiritual history embedded within Jhalokathi's river landscape.",
            "descBn": "রাজাপুর উপজেলার ঐতিহাসিক মসজিদ ও মাজার এলাকা দক্ষিণ বাংলার নদীমাতৃক অঞ্চলে সুফি সাধকদের আগমন ও ধর্মীয় জাগরণের এক সুপ্রাচীন স্মারক। ষোড়শ ও সপ্তদশ শতকে ইসলাম প্রচার ও মানবসেবায় আত্মনিয়োগকারী সাধকদের হাত ধরে এই উপাসনালয়গুলো প্রতিষ্ঠিত হয়েছিল। চুন-সুরকির প্রাচীন গাঁথুনি, দৃষ্টিনন্দন গম্বুজ এবং ছায়াঘেরা শান্ত পরিবেশ এই স্থানকে এক বিশেষ মর্যাদা দান করেছে। মাজার প্রাঙ্গণে থাকা প্রাচীন পুকুর ও বৃক্ষরাজি ভক্তদের মনে গভীর প্রশান্তি এনে দেয়। বার্ষিক ওরস ও ধর্মীয় অনুষ্ঠানে দূর-দূরান্ত থেকে বহু ধর্মপ্রাণ মানুষ এখানে সমবেত হন। আধ্যাত্মিক ঐতিহ্য ও ঐতিহাসিক সৌন্দর্যের এক অনন্য নিদর্শন এই রাজাপুর দরবার এলাকা।",
            "locationEn": jh_raw['hist_spots'][3]['location'],
            "locationBn": "রাজাপুর, ঝালকাঠি",
            "mapUrl": jh_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Traditional River-Port Settlement Area",
            "nameBn": "ঐতিহ্যবাহী নদী বন্দর জনপদ এলাকা",
            "categoryEn": "Heritage Maritime Bazaar & Settlement",
            "categoryBn": "ঐতিহ্যবাহী নদী বন্দর ও প্রাচীন বাণিজ্যিক বাজার",
            "descEn": "The Traditional River-Port Settlement Area of Jhalokathi town represents the surviving architectural and urban fabric of one of Bengal's greatest historic timber, salt, and agricultural trading entrepôts. Intersected by natural tidal canals and connected to the river by wooden jetties, the historic bazaar preserves vintage wooden trading houses, century-old sweetmeat shops, and metal craft workshops. For generations, skilled carpenters here crafted traditional wooden boats, while merchants transacted goods arriving from remote coastal islands. Walking through the narrow waterfront avenues, visitors witness active boatbuilders repairing wooden trawlers alongside centuries-old family businesses. It forms an authentic living museum of Bengal's enduring riverine urbanism.",
            "descBn": "ঝালকাঠি শহরের এই ঐতিহ্যবাহী নদী বন্দর জনপদ এলাকা এককালে অবিভক্ত বাংলার অন্যতম প্রধান লবণ, কাঠ, সুপারি ও চালের আন্তর্জাতিক বাণিজ্য কেন্দ্র ছিল। খালের নেটওয়ার্ক ও নদীর তীরে গড়ে ওঠা এই পুরোনো বাজারে আজও কাঠের প্রাচীন দোতলা আড়ত, শতবর্ষী মিষ্টির দোকান ও কাঁসা-পিতলের কর্মশালা দেখা যায়। এ অঞ্চলের দক্ষ কারিগরদের তৈরি ঐতিহ্যবাহী কাঠের নৌকা বাংলাজুড়ে সমাদৃত ছিল। খালের পাড় ঘেঁষে সারি সারি কাঠের ট্রলার নোঙর করে রাখার দৃশ্য এবং ব্যবসায়ীদের ব্যস্ততা প্রাচীন নৌবাণিজ্যের ঐতিহ্যের কথা মনে করিয়ে দেয়। নদীমাতৃক বাংলার জীবন্ত ইতিহাসের ছোঁয়া পেতে এই বন্দর এলাকা অত্যন্ত সমৃদ্ধ।",
            "locationEn": jh_raw['hist_spots'][4]['location'],
            "locationBn": "ঝালকাঠি শহর, ঝালকাঠি",
            "mapUrl": jh_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Gabkhan Channel and Gabkhan Bridge",
            "nameBn": "গাবখান চ্যানেল ও পঞ্চম চীন-বাংলাদেশ মৈত্রী সেতু",
            "categoryEn": "Man-Made River Canal & Monumental Bridge View",
            "categoryBn": "কৃত্রিম নৌখাল ও সুউচ্চ ঝুলন্ত সেতু ভিউপয়েন্ট",
            "descEn": "The Gabkhan Channel is a spectacular river tourism landmark where modern mega-infrastructure meets scenic deltaic waterways. Spanning high over the canal is the monumental Gabkhan Bridge (Fifth Bangladesh-China Friendship Bridge), which rises steeply to allow massive seafaring cargo vessels to pass unimpeded below. Standing atop the bridge or taking an open-top boat ride along the canal below reveals breathtaking aerial panoramas of winding emerald water bordered by palm plantations and village homesteads. Tourists love watching foreign cargo ships and large oil tankers maneuver through the narrow canal turns while refreshing river breezes cool the air. It is an exhilarating destination that showcases the vibrant maritime vitality of southern Bangladesh.",
            "descBn": "গাবখান চ্যানেল ও এর ওপর নির্মিত পঞ্চম চীন-বাংলাদেশ মৈত্রী সেতু ঝালকাঠির অন্যতম প্রধান ও রোমাঞ্চকর পর্যটন আকর্ষণ। খালের ওপর দিয়ে বিশালাকার সমুদ্রগামী জাহাজ চলাচলের সুবিধার্থে সেতুটি অত্যন্ত উঁচুতে ধনুকের মতো বাঁকিয়ে নির্মাণ করা হয়েছে। সেতুর চূড়ায় দাঁড়ালে নিচে গভীর গাবখান খালের সর্পিল গতিপথ, নারকেল-সুপারির বাগান এবং নদীর বুকে ছুটে চলা জাহাজের অপূর্ব দৃশ্য এক পলকে দেখা যায়। ট্রলারে করে খালের বুক চিরে ঘুরে বেড়ানো এবং ওপর দিয়ে চলে যাওয়া বিশাল সেতুর নিচ দিয়ে অতিক্রম করার অনুভূতি অত্যন্ত রোমাঞ্চকর। প্রকৌশল ও নদীপ্রকৃতির এই মেলবন্ধন ভ্রমণপ্রেমীদের মুগ্ধ করে।",
            "locationEn": jh_raw['tour_spots'][0]['location'],
            "locationBn": "ঝালকাঠি জেলা, ঝালকাঠি",
            "mapUrl": jh_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Bishkhali Riverbank",
            "nameBn": "বিষখালী নদীতীর",
            "categoryEn": "Expansive Tidal Riverfront Panorama",
            "categoryBn": "প্রমত্তা নদীতীর ও উপকূলীয় সূর্যাস্ত পয়েন্ট",
            "descEn": "The Bishkhali Riverbank offers an awe-inspiring natural escape where one of southern Bangladesh's most powerful tidal rivers flows toward the sea. Stretching along vast embankments, the riverbank provides sweeping, unobstructed views of wide rippling waters, distant green chars, and traditional fishermen casting large circular nets from wooden dinghies. During the late afternoon, the river takes on shimmering golden tones as the sunset reflects across the vast water surface. Visitors enjoy relaxing along the breezy embankments, tasting freshly caught hilsa fish at local riverside eateries, and soaking in the untouched peaceful atmosphere. It is a premier location for photography and peaceful nature appreciation.",
            "descBn": "বিষখালী নদীতীর ঝালকাঠির প্রকৃতির এক অপার রূপময় বিস্তার, যেখানে প্রমত্তা নদীটি সাগরের পানে ছুটে চলার বিশাল রূপ প্রদর্শন করে। বেড়িবাঁধের ওপর দিয়ে হাঁটলে শরীর জুড়ানো দখিনা বাতাস ও ঢেউয়ের কলতান যে কাউকে মুগ্ধ করে। নদীতে ঐতিহ্যবাহী কাঠের নৌকায় জেলেদের মাছ ধরার দৃশ্য এবং দূরবর্তী সবুজ চরাঞ্চল এক চমৎকার ক্যানভাস তৈরি করে। বিকেলে যখন সূর্য হেলে পড়ে, তখন নদীর জলরাশি সোনালী রঙে রূপ নেয় যা সূর্যাস্তপ্রেমীদের জন্য এক স্বর্গীয় অনুভূতি। নদীর পাড়ে বসে নদীর তাজা ইলিশ ভাজা খাওয়া ও শান্ত নিসর্গ উপভোগ করতে বহু পর্যটক এখানে ছুটে আসেন।",
            "locationEn": jh_raw['tour_spots'][1]['location'],
            "locationBn": "ঝালকাঠি জেলা, ঝালকাঠি",
            "mapUrl": jh_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Sugandha Riverfront",
            "nameBn": "সুগন্ধা নদীতীর",
            "categoryEn": "Scenic Urban Waterfront & Sunset Promenade",
            "categoryBn": "শহর সংলগ্ন নদীতীর ও মনোরম ওয়াকওয়ে",
            "descEn": "Flowing directly past Jhalokathi town, the Sugandha Riverfront is the beloved scenic promenade and recreational hub of the district. The municipal riverfront features paved walkways, decorative garden lamp posts, seating benches, and viewing gazebos where residents and tourists gather to enjoy cool river breezes. The river is constantly alive with the vibrant passage of colorful wooden motorboats, trawlers, and grand passenger launches cruising toward Dhaka. At twilight, the glowing lights of rivercraft reflect brilliantly across the water as riverside tea vendors serve steaming cardamom tea and local delicacies. It represents the quintessential soulful urban waterfront of southern Bengal.",
            "descBn": "ঝালকাঠি শহরের পাশ ঘেঁষে প্রবাহিত সুগন্ধা নদীতীর স্থানীয় বাসিন্দা ও পর্যটকদের প্রিয় বিনোদন ও সান্ধ্যকালীন ভ্রমণের কেন্দ্রস্থল। নদীতীরে গড়ে ওঠা বাঁধ ও ওয়াকওয়েতে রয়েছে বসার সুন্দর বেঞ্চ, বাগান এবং সন্ধ্যার মনোরম আলোকসজ্জা। সুগন্ধা নদীর বুকে সারাক্ষণ রঙিন কাঠের নৌকা, ট্রলার ও বিশালাকার লঞ্চের যাতায়াত এক জীবন্ত নদীমাতৃক পরিবেশের সৃষ্টি করে। সন্ধ্যায় নদীর মিষ্টি হাওয়া উপভোগ করতে এবং নদীর বুকে প্রতিফলিত শহরের আলো দেখতে বহু মানুষ এখানে আড্ডা জমান। নদীতীরের চায়ের দোকানে গরম চা আর তাজা নদীর মাছের স্ন্যাকস খাওয়ার আনন্দ সুগন্ধার পাড়ে এক পরম তৃপ্তি এনে দেয়।",
            "locationEn": jh_raw['tour_spots'][2]['location'],
            "locationBn": "ঝালকাঠি শহর, ঝালকাঠি",
            "mapUrl": jh_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Nalchity Riverbank",
            "nameBn": "নলছিটি নদীতীর",
            "categoryEn": "Tranquil Riverside Escape & Countryside Vista",
            "categoryBn": "স্নিগ্ধ নদীতীর ও গ্রামীণ পলিমাটির নিসর্গ",
            "descEn": "The Nalchity Riverbank stretches along the peaceful eastern reaches of the Sugandha River, framed by sweeping paddy fields and thick groves of coconut palms. The gentle slope of the grassy riverbank provides an ideal vantage point for watching the daily rhythms of village river life, from women washing brass vessels to fishermen casting delicate gillnets. Open wooden country boats offer affordable, gentle cruises along the river bends where water birds skim past floating hyacinths. The unhurried pace of life and fresh unpolluted air make it a favorite stop for travelers seeking authentic rural tranquility. It captures the gentle, pastoral soul of Jhalokathi's river country.",
            "descBn": "নলছিটি নদীতীর সুগন্ধা নদীর বাঁকে গড়ে ওঠা এক অপূর্ব শান্তিময় প্রাকৃতিক আশ্রয়স্থল, যার চারপাশ নারিকেল বাগান ও সবুজ ধানের খেতে ঘেরা। নদীতীরের স্নিগ্ধ ঘাসের ওপর বসে নদীর শান্ত প্রবাহ দেখা এবং গ্রামীণ জীবনের সরল ছন্দ প্রত্যক্ষ করা অত্যন্ত আনন্দদায়ক। ছোট ছোট কাঠের নৌকায় চড়ে নদীর বুক চিরে শান্তভাবে ভেসে বেড়ালে প্রকৃতির সাথে এক নিবিড় আত্মীয়তা তৈরি হয়। কোলাহলমুক্ত নির্মল বাতাস এবং নদীর বুকে জলজ পাখির ওড়াউড়ি ভ্রমণকারীদের মন ভরিয়ে দেয়। গ্রামবাংলার চিরন্তন নদীমাতৃক রূপ ও প্রশান্তি উপভোগ করতে নলছিটি নদীতীর এক অসাধারণ গন্তব্য।",
            "locationEn": jh_raw['tour_spots'][3]['location'],
            "locationBn": "নলছিটি, ঝালকাঠি",
            "mapUrl": jh_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Rajapur Countryside and Canal Landscape",
            "nameBn": "রাজাপুর গ্রামীণ নিসর্গ ও খালের রূপ",
            "categoryEn": "Intricate Canal Network & Backwater Landscape",
            "categoryBn": "খালবেষ্টিত গ্রামীণ নিসর্গ ও ব্যাকওয়াটার প্রকৃতি",
            "descEn": "The Rajapur Countryside and Canal Landscape is a mesmerizing labyrinth of natural and excavated tidal waterways that meander through dense fruit orchards and traditional homesteads. Resembling the backwaters of Kerala or European canal towns, transportation here is conducted largely via wooden canoes through arched tunnels of overhanging bamboo and betel nut trees. The canals lead into famous local floating agricultural markets, including the seasonal guava, amra (hog plum), and betel nut trading posts. Taking a canoe trip through these tranquil waterways allows visitors to experience life completely attuned to the tides. It stands as an authentic, enchanting manifestation of Jhalokathi's title as the 'Venice of Bengal'.",
            "descBn": "রাজাপুর গ্রামীণ এলাকা ও এর খালের নেটওয়ার্ক দক্ষিণ বাংলার ব্যাকওয়াটার প্রকৃতির এক অপূর্ব বিস্ময়, যা প্রাচ্যের ভেনিসের আসল রূপ ফুটিয়ে তোলে। শত শত ছোট-বড় খালের মাধ্যমে সংযুক্ত এই গ্রামের প্রতিটি বাড়ির সাথে যোগাযোগের প্রধান মাধ্যম হলো ছোট কাঠের ডিঙি নৌকা। বাঁশঝাড়, সুপারি বাগান ও পেয়ারা বাগানের নিচ দিয়ে চলে যাওয়া ছায়াঘেরা খালের বুক চিরে নৌভ্রমণ এক অদ্ভুত জাদুকরী রোমাঞ্চ তৈরি করে। খালের বিভিন্ন মোড়ে বসে ভাসমান পেয়ারা ও আমড়ার হাট, যা দেখতে দেশি-বিদেশি বহু পর্যটক আসেন। খালের শান্ত জলে ভেসে বেড়ানো এবং গ্রামীণ মানুষের জলকেন্দ্রিক জীবনধারা প্রত্যক্ষ করতে রাজাপুর এক পরম স্বপ্নিল গন্তব্য।",
            "locationEn": jh_raw['tour_spots'][4]['location'],
            "locationBn": "রাজাপুর, ঝালকাঠি",
            "mapUrl": jh_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('jhalokathi', jhalokathi_data)

# ==========================================
# 10. MOULVIBAZAR
# ==========================================
m_raw = all_data['moulvibazar']
moulvibazar_data = {
    "slug": "moulvibazar",
    "en": "Moulvibazar",
    "bn": "মৌলভীবাজার",
    "hero_title_en": "Moulvibazar Tea Capital, Lawachara Rainforest & Madhabkunda Falls",
    "hero_title_bn": "মৌলভীবাজারের চায়ের দেশ, লাউয়াছড়া বন ও মাধবকুণ্ড জলপ্রপাত",
    "hero_sub_en": "World-famous tea gardens of Sreemangal, Lawachara National Park rainforest, and Hakaluki Haor wetlands.",
    "hero_sub_bn": "শ্রীমঙ্গলের সুবিশাল সবুজ চা বাগান, লাউয়াছড়া জাতীয় উদ্যানের চিরসবুজ অরণ্য ও দেশের বৃহত্তম হাকালুকি হাওর।",
    "tagline_en": "The iconic tea capital of Bangladesh, blessed with rolling emerald tea slopes, primeval rainforests harboring hoolock gibbons, cascading mountain waterfalls, and vast haors.",
    "tagline_bn": "সবুজের সমারোহে ঘেরা চায়ের রাজধানী মৌলভীবাজার, যা শ্রীমঙ্গলের দিগন্তজোড়া চা বাগান, লাউয়াছড়ার জীববৈচিত্র্য, মাধবকুণ্ডের গর্জন এবং হাকালুকি হাওরের অপার রূপের জন্য বিশ্বখ্যাত।",
    "carousel": [
        {
            "id": 1,
            "image": "images/districts/moulvibazar/carousel-1.webp",
            "titleEn": "Lawachara National Park Tropical Rainforest",
            "titleBn": "লাউয়াছড়া জাতীয় উদ্যানের চিরসবুজ অরণ্য",
            "subtitleEn": "Primeval semi-evergreen rainforest sanctuary in Kamalganj famous for rare Hoolock gibbons and forest railway tracks",
            "subtitleBn": "কমলগঞ্জের গভীর চিরসবুজ বন যা বিলুপ্তপ্রায় উল্লুক, বুনো উদ্ভিদ ও বনের বুক চিরে যাওয়া রেললাইনের জন্য বিখ্যাত"
        },
        {
            "id": 2,
            "image": "images/districts/moulvibazar/carousel-2.webp",
            "titleEn": "Madhabkunda Waterfall Rocky Cascade",
            "titleBn": "মাধবকুণ্ড জলপ্রপাতের গর্জন",
            "subtitleEn": "Bangladesh's largest natural mountain waterfall in Barlekha plunging over 60 meters down rocky basalt bluffs",
            "subtitleBn": "বড়লেখার পাথুরে পাহাড়ের বুক চিরে প্রায় ২০০ ফুট উপর থেকে আছড়ে পড়া দেশের প্রধান জলপ্রপাত"
        },
        {
            "id": 3,
            "image": "images/districts/moulvibazar/carousel-3.webp",
            "titleEn": "Sreemangal Rolling Emerald Tea Estates",
            "titleBn": "শ্রীমঙ্গলের দিগন্তজোড়া সবুজ চা বাগান",
            "subtitleEn": "Endless undulating carpets of tea bushes stretching across the hills, celebrated as the Tea Capital of Bangladesh",
            "subtitleBn": "টিলার খাঁজে খাঁজে বিছানো সতেজ সবুজ চা পাতার চাদর যা বিশ্বজুড়ে চায়ের রাজধানী হিসেবে সমাদৃত"
        },
        {
            "id": 4,
            "image": "images/districts/moulvibazar/carousel-4.webp",
            "titleEn": "Hakaluki Haor Vast Wetland Horizon",
            "titleBn": "হাকালুকি হাওরের দিগন্তবিস্তৃত জলরাশি",
            "subtitleEn": "Largest inland wetland haor in Bangladesh, serving as an internationally critical winter habitat for migratory birds",
            "subtitleBn": "বাংলাদেশের সর্ববৃহৎ মিঠা পানির হাওর যা শীতকালে লাখ লাখ বিদেশি পরিযায়ী পাখির নিরাপদ আশ্রয়"
        },
        {
            "id": 5,
            "image": "images/districts/moulvibazar/carousel-5.webp",
            "titleEn": "Baikka Beel Wetland Bird Sanctuary",
            "titleBn": "বাইক্কা বিলের পাখি অভয়ারণ্য ও ওয়াচ টাওয়ার",
            "subtitleEn": "Permanently protected lotus and water lily lagoon in Hail Haor harboring thousands of rare aquatic birds",
            "subtitleBn": "শ্রীমঙ্গলের হাইল হাওরে অবস্থিত সংরক্ষিত জীববৈচিত্র্য ও পরিযায়ী পাখির স্বর্গরাজ্য"
        }
    ],
    "hist": [
        {
            "id": 1,
            "nameEn": "Madhabkunda Temple and Waterfall Heritage Area",
            "nameBn": "মাধবকুণ্ড মন্দির ও জলপ্রপাত ঐতিহ্য এলাকা",
            "categoryEn": "Sacred Pilgrimage Sanctuary & Natural Heritage",
            "categoryBn": "পবিত্র তীর্থস্থান ও প্রাকৃতিক ঐতিহ্য এলাকা",
            "descEn": "The Madhabkunda Temple and Waterfall Heritage Area in Barlekha Upazila is a sacred spiritual and natural sanctuary revered for centuries in northeastern Bengal. Dedicated to Lord Shiva, the ancient Hindu temple sits perched on the rocky bluffs above the natural gorge where the roaring waterfall descends. Devotees visit throughout the year to take ritual holy dips in the cool mineral-rich mountain pool during the annual Madhukrishna Trayodashi festival in spring. The surrounding rocky amphitheater and ancient banyan groves preserve fascinating legends of meditating sages who sought spiritual enlightenment amid nature. It represents an enchanting confluence of ancient sacred geology and living religious heritage.",
            "descBn": "বড়লেখা উপজেলার মাধবকুণ্ড মন্দির ও জলপ্রপাত এলাকা শতাব্দীর প্রাচীন এক পবিত্র তীর্থস্থান ও প্রাকৃতিক ঐতিহ্যের মিলনক্ষেত্র। সুউচ্চ পাথুরে পাহাড়ের কোল ঘেঁষে প্রতিষ্ঠিত শ্রী শ্রী মাধবেশ্বর শিব মন্দির সনাতন ধর্মাবলম্বীদের কাছে অত্যন্ত পবিত্র। প্রতি বছর চৈত্র মাসে মধুকৃষ্ণা ত্রয়োদশী তিথিতে বারুণী স্নান উপলক্ষে হাজার হাজার পুণ্যার্থী এখানে পুণ্যস্নানে সমবেত হন। বিশালাকার জলপ্রপাতের গর্জন এবং প্রাচীন বটবৃক্ষবেষ্টিত শান্ত পরিবেশ এক অপার্থিব আধ্যাত্মিক অনুভূতির সৃষ্টি করে। প্রাকৃতিক জলপ্রপাতের রূপমাধুর্য এবং শতবর্ষী ধর্মীয় ঐতিহ্যের চমৎকার মেলবন্ধন দেখতে এটি এক পরম তীর্থস্থান।",
            "locationEn": m_raw['hist_spots'][0]['location'],
            "locationBn": "বড়লেখা, মৌলভীবাজার",
            "mapUrl": m_raw['hist_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Sreemangal Railway-Era Heritage Area",
            "nameBn": "শ্রীমঙ্গল রেলওয়ে যুগের ঐতিহ্য এলাকা",
            "categoryEn": "Colonial Railway Infrastructure & Architecture",
            "categoryBn": "উপনিবেশিক রেলওয়ে ঐতিহ্য ও স্থাপত্য",
            "descEn": "The Sreemangal Railway-Era Heritage Area preserves the historic late nineteenth-century infrastructure built by the Assam Bengal Railway to transport tea from the lush hills of Sylhet to Chittagong port. The complex features picturesque British-era red-brick station buildings, high timber-vaulted platforms, historic signal cabins, and vintage railway staff bungalows shaded by centenary rain trees. A specialized antique train carriage and steam-era memorabilia narrate the transformative impact of railways on the commercial tea industry. The station still bustles daily with long-distance trains arriving from Dhaka and Chittagong carrying thousands of tourists into tea country. It stands as a romantic and nostalgic portal into the industrial development of British Bengal.",
            "descBn": "শ্রীমঙ্গল রেলওয়ে ঐতিহ্যের এলাকা উনিশ শতকের শেষভাগে আসাম বেঙ্গল রেলওয়ে কর্তৃক চা শিল্পের প্রসারে নির্মিত ঐতিহাসিক অবকাঠামোর এক চমৎকার স্মারক। লাল ইটের তৈরি ভিক্টোরীয় স্থাপত্যের স্টেশন ভবন, প্রাচীন সিগন্যাল কেবিন এবং শতবর্ষী গাছের ছায়ায় ঘেরা ব্রিটিশ বাংলোগুলো অতীতের সোনালী রেলযুগের সাক্ষ্য বহন করে। এই রেলপথের মাধ্যমেই শ্রীমঙ্গলের বাগানের বিখ্যাত চা সারা বিশ্বে রপ্তানির জন্য চট্টগ্রাম বন্দরে পৌঁছাতো। আজও প্রতিদিন ঢাকা ও চট্টগ্রাম থেকে শত শত পর্যটক এই স্টেশনে নেমে চায়ের দেশের মায়াবী রাজ্যে প্রবেশ করেন। শিল্প ইতিহাস ও রোমাঞ্চকর রেল ভ্রমণের চমৎকার প্রতীক এই ঐতিহাসিক স্টেশন এলাকা।",
            "locationEn": m_raw['hist_spots'][1]['location'],
            "locationBn": "শ্রীমঙ্গল, মৌলভীবাজার",
            "mapUrl": m_raw['hist_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Kamalganj Tea-Estate Bungalow Area",
            "nameBn": "কমলগঞ্জ চা বাগান বাংলো এলাকা",
            "categoryEn": "Colonial Plantation Heritage Architecture",
            "categoryBn": "উপনিবেশিক চা বাগান বাংলো ও আভিজাত্যের ঐতিহ্য",
            "descEn": "The Kamalganj Tea-Estate Bungalow Area features an exceptional cluster of authentic British colonial planters' residences nestled amidst rolling green tea valleys. Constructed in the late nineteenth and early twentieth centuries with local timber framing, stone fireplaces, wide wraparound verandas, and polished teakwood floors, these bungalows exemplify high colonial plantation architecture. Surrounding the historic residences are meticulously manicured private gardens overflowing with English roses, hydrangeas, and ancient fruit trees. Many of these historic properties continue to host visiting tea executives and discerning heritage travelers seeking vintage luxury. They provide an evocative glimpse into the disciplined, elegant lifestyle of colonial tea estate managers.",
            "descBn": "কমলগঞ্জ উপজেলার বিভিন্ন চা বাগানের উঁচু টিলায় অবস্থিত ব্রিটিশ আমলের ঐতিহাসিক বাংলোগুলো চা শিল্পের অভিজাত ঐতিহ্যের এক জীবন্ত উদাহরণ। উনিশ ও বিশ শতকের শুরুতে কাঠ, চুন-সুরকি ও টিনের ছাউনিতে নির্মিত এই বাংলোগুলোতে রয়েছে সুবিশাল খিলানযুক্ত বারান্দা, ফায়ারপ্লেস, প্রাচীন কাঠের আসবাব এবং চোখ জুড়ানো ফুলের বাগান। উঁচু পাহাড়ের চূড়া থেকে চারপাশের সবুজ চা বাগানের দিগন্তজোড়া দৃশ্য এই বাংলোগুলোকে রাজকীয় রূপ দান করেছে। শান্ত স্নিগ্ধ পরিবেশে ব্রিটিশ প্ল্যান্টারদের আভিজাত্যপূর্ণ জীবনযাত্রার ছাপ আজও এসব বাংলোতে স্পষ্ট। ইতিহাস ও প্রকৃতির নিবিড় সান্নিধ্য পেতে এই বাংলো এলাকা অত্যন্ত আকর্ষণীয়।",
            "locationEn": m_raw['hist_spots'][2]['location'],
            "locationBn": "কমলগঞ্জ, মৌলভীবাজার",
            "mapUrl": m_raw['hist_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Bhanugachh Historic Settlement Area",
            "nameBn": "ভানুকাছ ঐতিহাসিক জনপদ এলাকা",
            "categoryEn": "Historic Forest Settlement & Indigenous Trading Post",
            "categoryBn": "ঐতিহাসিক পাহাড়ি জনপদ ও প্রাচীন বাণিজ্য কেন্দ্র",
            "descEn": "Bhanugachh in Kamalganj Upazila is an ancient forested settlement deeply intertwined with regional history, tribal migrations, and the development of early forest trails through the Tripura hills. Serving as a crucial trading post where hill communities exchanged timber, wild honey, and woven textiles with lowland Bengali traders, the area retains authentic multi-ethnic heritage. The surrounding forests were the scene of historic agrarian movements and community resistance during the colonial expansion of commercial tea estates. Today, the settlement features historic wooden bazaars, traditional tea stalls, and gateways leading into the adjacent Lawachara National Park. It connects visitors to the rich sociocultural tapestry of Moulvibazar's borderland communities.",
            "descBn": "কমলগঞ্জের ভানুকাছ এলাকা এক সুপ্রাচীন অরণ্যঘেরা জনপদ, যা ত্রিপুরা পাহাড় ও সমতল বাংলার আদিবাসী সংস্কৃতি ও প্রাচীন বাণিজ্যের সেতুবন্ধন হিসেবে পরিচিত। শতাব্দী পূর্বে এই এলাকাটি পাহাড়ি মধু, কাঠ ও আদিবাসী তাঁতপণ্যের প্রধান বিনিময় কেন্দ্র ছিল। পরবর্তীতে এই বনাঞ্চলের মধ্য দিয়েই গড়ে ওঠে ব্রিটিশ চা বাগান ও যোগাযোগ ব্যবস্থা। ঔপনিবেশিক যুগে স্থানীয় জনগোষ্ঠীর অধিকার আদায়ের সংগ্রামের বহু ঐতিহাসিক স্মৃতি এই মাটির সাথে জড়িয়ে আছে। প্রাচীন কাঠের বাজার এবং সংলগ্ন লাউয়াছড়া বনের প্রবেশপথ হিসেবে ভানুকাছ আজও অত্যন্ত প্রাণবন্ত। পাহাড় ও বনের মানুষের ঐতিহ্য অনুধাবনে এটি এক তাৎপর্যপূর্ণ স্থান।",
            "locationEn": m_raw['hist_spots'][3]['location'],
            "locationBn": "কমলগঞ্জ, মৌলভীবাজার",
            "mapUrl": m_raw['hist_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Manipuri Cultural Heritage Area",
            "nameBn": "মণিপুরী সাংস্কৃতিক ঐতিহ্য এলাকা",
            "categoryEn": "Indigenous Cultural Heritage & Textile Sanctuary",
            "categoryBn": "মণিপুরী ক্ষুদ্র নৃ-গোষ্ঠী ঐতিহ্য ও তাঁতশিল্পের কেন্দ্র",
            "descEn": "The Manipuri Cultural Heritage Area across villages like Madhabpur and Ramnagar in Kamalganj is the vibrant heart of the indigenous Manipuri community in Bangladesh. Renowned worldwide for their exquisite classical dance forms and intricate handloom weaving, the Manipuri people preserve centuries of refined aesthetic traditions. The area features sacred temples dedicated to Radha and Krishna, traditional courtyards where the celestial Raas Leela dance festival is performed under the full moon in autumn, and bustling handloom workshops where women craft colourful shawls, sarees, and blankets. Visitors are warmly welcomed into village homesteads to observe weaving techniques and experience rich hospitality. It is a world-class cultural destination celebrating living heritage in harmony with nature.",
            "descBn": "কমলগঞ্জের মাধবপুর ও সংলগ্ন গ্রামগুলোতে গড়ে ওঠা মণিপুরী সাংস্কৃতিক ঐতিহ্য এলাকা বাংলাদেশের অন্যতম শ্রেষ্ঠ ঐতিহ্যবাহী সাংস্কৃতিক কেন্দ্র। মণিপুরীদের সমৃদ্ধ হস্তশিল্প, ঐতিহ্যবাহী তাঁতে বোনা রঙিন শাড়ি, চাদর এবং বিশ্বখ্যাত মণিপুরী নৃত্য এই জনপদকে আন্তর্জাতিক পরিচিতি দিয়েছে। প্রতি বছর কার্তিক পূর্ণিমায় মাধবপুরের জোড়ামণ্ডপে আয়োজিত ঐতিহ্যবাহী 'রাসোৎসব' দেখতে দেশ-বিদেশের লাখ লাখ মানুষ এখানে সমবেত হন। মণিপুরী পল্লীর পরিপাটি মাটির ঘর, ফুলের বাগান এবং তাঁতের খটখট শব্দে মুখরিত পরিবেশ দর্শনার্থীদের মন ছুঁয়ে যায়। আদিবাসী সংস্কৃতির অপূর্ব মাধুর্য ও ঐতিহ্যের স্বাদ পেতে এটি এক অনন্য স্থান।",
            "locationEn": m_raw['hist_spots'][4]['location'],
            "locationBn": "মৌলভীবাজার জেলা",
            "mapUrl": m_raw['hist_spots'][4]['mapUrl']
        }
    ],
    "tour": [
        {
            "id": 1,
            "nameEn": "Lawachara National Park",
            "nameBn": "লাউয়াছড়া জাতীয় উদ্যান",
            "categoryEn": "Primeval Semi-Evergreen Tropical Rainforest",
            "categoryBn": "চিরসবুজ রেইনফরেস্ট ও বন্যপ্রাণী অভয়ারণ্য",
            "descEn": "Lawachara National Park in Kamalganj is one of the most famous and ecologically significant tropical rainforest reserves in South Asia, preserving an astonishing biodiversity hotspot across twelve hundred hectares. Home to the world's most viable surviving population of endangered Western Hoolock Gibbons, the park resounds each morning with their melodic territorial calls echoing from dense forest canopies. Shaded hiking trails wind past towering ancient trees, hanging climbing lianas, wild figs, and clear forest streams where capped langurs and barking deer roam. The historic Dhaka-Sylhet railway line cutting dramatically through the heart of the jungle creates one of the most photographed forest settings in the nation. It is an unmissable world-class destination for ecotourists, birdwatchers, and adventurers.",
            "descBn": "কমলগঞ্জে অবস্থিত লাউয়াছড়া জাতীয় উদ্যান বাংলাদেশের সবচেয়ে বিখ্যাত ও সমৃদ্ধ চিরসবুজ রেইনফরেস্ট। প্রায় ১,২৫০ হেক্টর আয়তনের এই গভীর বনাঞ্চল বিশ্বজুড়ে বিপন্ন উল্লুকের (হুলক গিবন) অন্যতম প্রধান নিরাপদ আবাসস্থল হিসেবে পরিচিত। বনের উঁচু গাছের ডালপালা থেকে ভেসে আসা উল্লুকের ডাক এবং পাখিদের কলতান এক জাদুকরী বুনো পরিবেশ তৈরি করে। বনের বুক চিরে চলে যাওয়া ঐতিহাসিক ব্রিটিশ রেললাইন এবং ট্র্যাকিং ট্রেইল ধরে হাঁটার সময় মুখপোড়া হনুমান, লজ্জাবতী বানর ও শত শত বিরল উদ্ভিদের দেখা মেলে। প্রকৃতির গভীর রহস্য ও চিরসবুজ অরণ্যের নির্মল স্বাদ নিতে লাউয়াছড়া জাতীয় উদ্যান এক অতুলনীয় স্বর্গরাজ্য।",
            "locationEn": m_raw['tour_spots'][0]['location'],
            "locationBn": "কমলগঞ্জ, মৌলভীবাজার",
            "mapUrl": m_raw['tour_spots'][0]['mapUrl']
        },
        {
            "id": 2,
            "nameEn": "Madhabkunda Waterfall",
            "nameBn": "মাধবকুণ্ড জলপ্রপাত",
            "categoryEn": "Monumental Natural Mountain Waterfall",
            "categoryBn": "দেশের প্রধান প্রাকৃতিক পাহাড়ি জলপ্রপাত",
            "descEn": "Madhabkunda Waterfall in Barlekha Upazila is the largest and most famous natural mountain waterfall in Bangladesh, plunging over sixty meters down a sheer volcanic basalt cliff into a swirling green pool below. Framed by dense subtropical forest, wild banana groves, and echoing rock bluffs, the roaring cascade creates a perpetual cooling mist that refreshes visitors even on hot days. Pathways with stone railings lead tourists directly to viewing points near the base where the sheer scale and thundering acoustics of falling water inspire awe. The surrounding eco-park grounds feature botanical gardens, picnic areas, and souvenir stalls offering local forest crafts. It remains an iconic, breathtaking highlight of travel in Bangladesh.",
            "descBn": "বড়লেখা উপজেলার পাথারিয়া পাহাড়ের বুক চিরে বয়ে আসা মাধবকুণ্ড জলপ্রপাত বাংলাদেশের সর্ববৃহৎ ও সর্বাধিক পরিচিত প্রাকৃতিক জলপ্রপাত। প্রায় ২০০ ফুট উঁচু খাড়া পাথুরে পাহাড় থেকে অবিরাম গর্জন তুলে নিচে আছড়ে পড়া জলরাশি এক অপূর্ব স্বর্গীয় দৃশ্যের অবতারণা করে। জলপ্রপাতের তীব্র স্রোতে উড়ে আসা স্নিগ্ধ জলকণা দূর থেকেই দর্শনার্থীদের শরীর ও মন জুড়িয়ে দেয়। চারপাশের গভীর সবুজ অরণ্য ও পাথুরে গিরিখাত এই স্থানটিকে প্রকৃতির এক পরম বিস্ময়ে পরিণত করেছে। জলপ্রপাতের সৌন্দর্য উপভোগের জন্য রয়েছে নিরাপদ ওয়াকওয়ে ও ভিউপয়েন্ট। মৌলভীবাজার ভ্রমণের সবচেয়ে রোমাঞ্চকর অভিজ্ঞতাই হলো এই মাধবকুণ্ড দর্শন।",
            "locationEn": m_raw['tour_spots'][1]['location'],
            "locationBn": "বড়লেখা, মৌলভীবাজার",
            "mapUrl": m_raw['tour_spots'][1]['mapUrl']
        },
        {
            "id": 3,
            "nameEn": "Hakaluki Haor",
            "nameBn": "হাকালুকি হাওর",
            "categoryEn": "Largest Inland Freshwater Wetland in Bangladesh",
            "categoryBn": "দেশের সর্ববৃহৎ মিঠা পানির হাওর ও জলাভূমি",
            "descEn": "Hakaluki Haor is the largest freshwater wetland ecosystem in Bangladesh, spanning over eighteen thousand hectares across Barlekha, Kulaura, and Juri upazilas. In the monsoon season, the haor transforms into an immense inland sea where gentle waves stretch to the horizon and fishing communities navigate on traditional wooden boats. During the winter dry season, hundreds of interconnected beels (lakes) emerge, attracting over one hundred and fifty species of migratory aquatic waterfowl from across the Eurasian flyway. Watching flocks of migratory ducks take flight against glowing pink sunsets while gliding in a silent rowboat is a transcendent ecotourism experience. It is a Ramsar-quality ecological wonder of global importance.",
            "descBn": "মৌলভীবাজার ও সিলেট জেলার বিস্তৃত অঞ্চল জুড়ে অবস্থিত হাকালুকি হাওর বাংলাদেশের তথা এশিয়ার অন্যতম বৃহত্তম মিঠা পানির প্রাকৃতিক জলাভূমি। বর্ষাকালে এই হাওর এক কূলহীন মহাসমুদ্রে রূপ নেয়, যেখানে দিগন্তবিস্তৃত জলরাশি আর মেঘেদের মেলা বসে। শীত মৌসুমে পানি কমে গেলে জেগে ওঠে শত শত বিল ও চরাঞ্চল, যা সুদূর সাইবেরিয়া ও হিমালয় অঞ্চল থেকে আসা লাখ লাখ অতিথি পাখির নিরাপদ স্বর্গে পরিণত হয়। নৌকায় চড়ে হাওরের বুকে সূর্যাস্ত দেখা এবং পাখির কলকাকলি শোনা এক অপার্থিব অনুভূতি উপহার দেয়। নদীমাতৃক বাংলার আসল বিশালতা ও জীববৈচিত্র্য উপভোগে হাকালুকি হাওর এক পরম বিস্ময়।",
            "locationEn": m_raw['tour_spots'][2]['location'],
            "locationBn": "বড়লেখা/কুলাউড়া/জুড়ী এলাকা, মৌলভীবাজার",
            "mapUrl": m_raw['tour_spots'][2]['mapUrl']
        },
        {
            "id": 4,
            "nameEn": "Baikka Beel Wetland Sanctuary",
            "nameBn": "বাইক্কা বিল পাখি অভয়ারণ্য",
            "categoryEn": "Protected Aquatic Sanctuary & Observation Tower",
            "categoryBn": "সংরক্ষিত জলাভূমি ও আন্তর্জাতিক পক্ষী অভয়ারণ্য",
            "descEn": "Baikka Beel, located within the expansive Hail Haor basin of Sreemangal, is a permanently protected wetland sanctuary dedicated to aquatic conservation and migratory bird safety. The calm lagoon is carpeted in blooming pink lotus flowers and purple water lilies, framed by tall native reeds where rare wetland birds nest. The sanctuary features a modern multi-tiered observation tower equipped with binoculars, offering birdwatchers breathtaking views of whistling teals, purple swamphens, fishing eagles, and migratory storks. Strict local community conservation guidelines have preserved abundant fish populations and pristine clean water. It provides one of the most serene, environmentally inspiring birdwatching spots in South Asia.",
            "descBn": "শ্রীমঙ্গলের হাইল হাওরের অংশ বাইক্কা বিল বাংলাদেশের অন্যতম শ্রেষ্ঠ সংরক্ষিত জলাভূমি ও আন্তর্জাতিক মানের পাখি অভয়ারণ্য। প্রায় ১০০ হেক্টর এলাকা জুড়ে বিস্তৃত এই বিলে পদ্ম ও নীল শাপলার সমারোহ এক চোখ জুড়ানো রূপ তৈরি করেছে। বিলের মাঝে স্থাপিত আধুনিক দ্বিতল ওয়াচ টাওয়ার থেকে দূরবীন দিয়ে শত শত প্রজাতির দেশি ও বিদেশি পরিযায়ী পাখির অবাধ বিচরণ দেখা যায়। শিকার নিষিদ্ধ হওয়ায় এখানে নির্ভয়ে ঘুরে বেড়ায় পানকৌড়ি, ডাহুক, বালিহাঁস ও বিরল প্রজাতির ঈগল। প্রকৃতির নিস্তব্ধতা এবং হাজার হাজার পাখির কলকাকলিতে মুখরিত এই বিল প্রকৃতিপ্রেমী ও আলোকচিত্রীদের পরম তীর্থস্থান।",
            "locationEn": m_raw['tour_spots'][3]['location'],
            "locationBn": "শ্রীমঙ্গল, মৌলভীবাজার",
            "mapUrl": m_raw['tour_spots'][3]['mapUrl']
        },
        {
            "id": 5,
            "nameEn": "Sreemangal Tea Gardens",
            "nameBn": "শ্রীমঙ্গলের চা বাগান",
            "categoryEn": "Endless Emerald Tea Valleys & Scenic Estates",
            "categoryBn": "চায়ের রাজধানী ও রূপময় পাহাড়ি চা বাগান",
            "descEn": "The Sreemangal Tea Gardens form an endless, rolling green paradise that has earned Sreemangal international renown as the 'Tea Capital of Bangladesh'. Home to over forty extensive tea estates, including the famous Finlay, BTRI, and Zareen gardens, the undulating hills are blanketed with lush, meticulously trimmed tea bushes shaded by silver-barked albizia trees. Scenic paved roads wind through the hills, providing heavenly cycling and walking routes enveloped in cool, fragrant mountain air. Visiting the famous Seven-Color Tea cabin in Sreemangal allows tourists to taste the legendary multi-layered beverage invented right in these hills. It is the defining romantic and picturesque landscape of eastern Bangladesh.",
            "descBn": "শ্রীমঙ্গলের চা বাগানগুলো সবুজের এক অনন্ত গালিচা যা শ্রীমঙ্গলকে এনে দিয়েছে বিশ্বখ্যাত 'চায়ের রাজধানী'র খেতাব। ফিনলে, বাংলাদেশ চা গবেষণা ইনস্টিটিউট (বিটিআরআই) ও নূরজাহানসহ প্রায় অর্ধশত সুরম্য চা বাগানের উঁচু-নিচু টিলা চোখ জুড়ানো সবুজ চা পাতায় মোড়া। বাগানের মধ্য দিয়ে এঁকেবেঁকে চলে যাওয়া ছায়াঘেরা শান্ত পথ ধরে সাইকেল চালানো কিংবা হাঁটার আনন্দ অতুলনীয়। নারী চা শ্রমিকদের নিপুণ হাতে চা পাতা তোলার দৃশ্য এবং শ্রীমঙ্গলের বিখ্যাত সাত রঙের চায়ের স্বাদ নেওয়া প্রতিটি পর্যটকের জন্য এক অনন্য অভিজ্ঞতা। সতেজ পাহাড়ি বাতাস ও সবুজের মাঝে নিজেকে নতুন করে আবিষ্কার করতে শ্রীমঙ্গল এক স্বপ্নপুরী।",
            "locationEn": m_raw['tour_spots'][4]['location'],
            "locationBn": "শ্রীমঙ্গল, মৌলভীবাজার",
            "mapUrl": m_raw['tour_spots'][4]['mapUrl']
        }
    ]
}
write_module('moulvibazar', moulvibazar_data)
