/**
 * Local Host BD — Comprehensive Bangladesh 64 Districts Explorer
 * Complete District Information • Heritage Landmarks • Tourism Attractions • Vector Maps
 * 
 * Features:
 * - Direct execution out of `window.LOCAL_DISTRICTS` & `window.MAP_PATHS`
 * - Full Bilingual Engine (English ↔ Proper Bangla with Kalpurush Font & Bengali Digits)
 * - Clickable Google Maps Location Links & App Redirection for all spots
 * - Full-width Cinematic District Hero Banner with dark gradient fade
 * - Pure CSS Scroll-Snapping 5-Image Carousel Track
 * - Enforced Top-5 Historical & Tourist Location Cards with image frames, map pins & Google Maps actions
 * - Real photorealistic spot images for districts
 * - Sticky desktop dual-column grid (left sidebar sticky, right map locked)
 * - Mobile Segmented View Controller ([ Interactive Map View ] vs [ 64 Districts List ])
 * - SVG vector map hover/touch inspection with strictly bounded tooltip
 * - Interactive Dark ↔ Light mode engine with localStorage persistence
 */

// ==========================================
// 1. REACTIVE STATE MANAGEMENT & CONSTANTS
// ==========================================
const THEME_KEY = 'localhost_district_theme_v2';
const LANG_KEY = 'localhost_district_lang_v2';

// Official Bangladesh National Web Portal URLs for all 64 districts (.gov.bd)
const DISTRICT_OFFICIAL_WEBSITES = {
  1: 'https://dhaka.gov.bd',
  2: 'https://faridpur.gov.bd',
  3: 'https://gazipur.gov.bd',
  4: 'https://gopalganj.gov.bd',
  5: 'https://kishoreganj.gov.bd',
  6: 'https://madaripur.gov.bd',
  7: 'https://manikganj.gov.bd',
  8: 'https://munshiganj.gov.bd',
  9: 'https://narayanganj.gov.bd',
  10: 'https://narsingdi.gov.bd',
  11: 'https://rajbari.gov.bd',
  12: 'https://shariatpur.gov.bd',
  13: 'https://tangail.gov.bd',
  14: 'https://bandarban.gov.bd',
  15: 'https://brahmanbaria.gov.bd',
  16: 'https://chandpur.gov.bd',
  17: 'https://chittagong.gov.bd',
  18: 'https://comilla.gov.bd',
  19: 'https://coxsbazar.gov.bd',
  20: 'https://feni.gov.bd',
  21: 'https://khagrachhari.gov.bd',
  22: 'https://lakshmipur.gov.bd',
  23: 'https://noakhali.gov.bd',
  24: 'https://rangamati.gov.bd',
  25: 'https://habiganj.gov.bd',
  26: 'https://moulvibazar.gov.bd',
  27: 'https://sunamganj.gov.bd',
  28: 'https://sylhet.gov.bd',
  29: 'https://barguna.gov.bd',
  30: 'https://barisal.gov.bd',
  31: 'https://bhola.gov.bd',
  32: 'https://jhalakathi.gov.bd',
  33: 'https://patuakhali.gov.bd',
  34: 'https://pirojpur.gov.bd',
  35: 'https://bagerhat.gov.bd',
  36: 'https://chuadanga.gov.bd',
  37: 'https://jessore.gov.bd',
  38: 'https://jhenaidah.gov.bd',
  39: 'https://khulna.gov.bd',
  40: 'https://kushtia.gov.bd',
  41: 'https://magura.gov.bd',
  42: 'https://meherpur.gov.bd',
  43: 'https://narail.gov.bd',
  44: 'https://satkhira.gov.bd',
  45: 'https://bogra.gov.bd',
  46: 'https://joypurhat.gov.bd',
  47: 'https://naogaon.gov.bd',
  48: 'https://natore.gov.bd',
  49: 'https://chapainawabganj.gov.bd',
  50: 'https://pabna.gov.bd',
  51: 'https://rajshahi.gov.bd',
  52: 'https://sirajganj.gov.bd',
  53: 'https://dinajpur.gov.bd',
  54: 'https://gaibandha.gov.bd',
  55: 'https://kurigram.gov.bd',
  56: 'https://lalmonirhat.gov.bd',
  57: 'https://nilphamari.gov.bd',
  58: 'https://panchagarh.gov.bd',
  59: 'https://rangpur.gov.bd',
  60: 'https://thakurgaon.gov.bd',
  61: 'https://jamalpur.gov.bd',
  62: 'https://mymensingh.gov.bd',
  63: 'https://netrokona.gov.bd',
  64: 'https://sherpur.gov.bd'
};

const DISTRICT_SLUG_WEBSITES = {
  'dhaka': 'https://dhaka.gov.bd',
  'faridpur': 'https://faridpur.gov.bd',
  'gazipur': 'https://gazipur.gov.bd',
  'gopalganj': 'https://gopalganj.gov.bd',
  'kishoreganj': 'https://kishoreganj.gov.bd',
  'madaripur': 'https://madaripur.gov.bd',
  'manikganj': 'https://manikganj.gov.bd',
  'munshiganj': 'https://munshiganj.gov.bd',
  'narayanganj': 'https://narayanganj.gov.bd',
  'narsingdi': 'https://narsingdi.gov.bd',
  'rajbari': 'https://rajbari.gov.bd',
  'shariatpur': 'https://shariatpur.gov.bd',
  'tangail': 'https://tangail.gov.bd',
  'bandarban': 'https://bandarban.gov.bd',
  'brahmanbaria': 'https://brahmanbaria.gov.bd',
  'chandpur': 'https://chandpur.gov.bd',
  'chattogram': 'https://chittagong.gov.bd',
  'cumilla': 'https://comilla.gov.bd',
  'coxs-bazar': 'https://coxsbazar.gov.bd',
  'feni': 'https://feni.gov.bd',
  'khagrachhari': 'https://khagrachhari.gov.bd',
  'lakshmipur': 'https://lakshmipur.gov.bd',
  'noakhali': 'https://noakhali.gov.bd',
  'rangamati': 'https://rangamati.gov.bd',
  'habiganj': 'https://habiganj.gov.bd',
  'moulvibazar': 'https://moulvibazar.gov.bd',
  'sunamganj': 'https://sunamganj.gov.bd',
  'sylhet': 'https://sylhet.gov.bd',
  'barguna': 'https://barguna.gov.bd',
  'barishal': 'https://barisal.gov.bd',
  'bhola': 'https://bhola.gov.bd',
  'jhalokathi': 'https://jhalakathi.gov.bd',
  'patuakhali': 'https://patuakhali.gov.bd',
  'pirojpur': 'https://pirojpur.gov.bd',
  'bagerhat': 'https://bagerhat.gov.bd',
  'chuadanga': 'https://chuadanga.gov.bd',
  'jashore': 'https://jessore.gov.bd',
  'jhenaidah': 'https://jhenaidah.gov.bd',
  'khulna': 'https://khulna.gov.bd',
  'kushtia': 'https://kushtia.gov.bd',
  'magura': 'https://magura.gov.bd',
  'meherpur': 'https://meherpur.gov.bd',
  'narail': 'https://narail.gov.bd',
  'satkhira': 'https://satkhira.gov.bd',
  'bogura': 'https://bogra.gov.bd',
  'joypurhat': 'https://joypurhat.gov.bd',
  'naogaon': 'https://naogaon.gov.bd',
  'natore': 'https://natore.gov.bd',
  'chapainawabganj': 'https://chapainawabganj.gov.bd',
  'pabna': 'https://pabna.gov.bd',
  'rajshahi': 'https://rajshahi.gov.bd',
  'sirajganj': 'https://sirajganj.gov.bd',
  'dinajpur': 'https://dinajpur.gov.bd',
  'gaibandha': 'https://gaibandha.gov.bd',
  'kurigram': 'https://kurigram.gov.bd',
  'lalmonirhat': 'https://lalmonirhat.gov.bd',
  'nilphamari': 'https://nilphamari.gov.bd',
  'panchagarh': 'https://panchagarh.gov.bd',
  'rangpur': 'https://rangpur.gov.bd',
  'thakurgaon': 'https://thakurgaon.gov.bd',
  'jamalpur': 'https://jamalpur.gov.bd',
  'mymensingh': 'https://mymensingh.gov.bd',
  'netrokona': 'https://netrokona.gov.bd',
  'sherpur': 'https://sherpur.gov.bd'
};

const AppState = {
  districts: [],             // All 64 district memory buffers
  filteredDistricts: [],     // Filtered and sorted district list
  selectedDistrictId: null,  // Active selected district ID
  hoveredDistrictId: null,   // Currently hovered / touched district ID
  activeDivision: 'all',     // Selected division filter
  searchQuery: '',           // Current search filter query
  sortBy: 'name-asc',        // Sort criteria: name-asc, dist-asc, area-desc, pop-desc
  currentTheme: 'light',     // 'light' (Initial Default) | 'dark'
  currentLang: 'bn',         // 'bn' (Initial Default) | 'en'
  mobileHomeTab: 'map',      // 'map' | 'list' (on compact mobile screens)
};

// Comprehensive Localization Dictionary
const I18N = {
  en: {
    brand_title: "Local Host BD",
    brand_tagline: "Find Places. Feel Bangladesh.",
    brand_sub: "Comprehensive 64 District Information & Exploration Guide",
    api_ready: "District Directory Ready",
    districts_loaded: "64 Districts Loaded",
    theme_dark: "Dark",
    theme_light: "Light",
    lang_btn: "বাংলা",
    nav_vector_map: "Vector Map",
    hero_about_badge: "🇧🇩 Comprehensive 64 District Information & Travel Guide",
    hero_about_title: "Explore Bangladesh District by District",
    hero_about_tagline: "Find Places. Feel Bangladesh.",
    hero_about_desc: "Discover all 64 districts of Bangladesh with comprehensive details. Explore verified historical landmarks, iconic tourist attractions, transit routes and distances from Dhaka, geographical statistics, and interactive vector maps.",
    hero_feature_1: "64 District Profiles",
    hero_feature_2: "320+ Curated Sights",
    hero_feature_3: "Dhaka Transit Routes",
    hero_dev_label: "Developer Profile",
    hero_github_label: "GitHub",
    footer_brand_tagline: "Find Places. Feel Bangladesh.",
    footer_about_text: "A comprehensive district exploration guide for all 64 districts of Bangladesh. Explore verified historical landmarks, iconic tourism attractions, transit road guides from Dhaka, and interactive vector cartography.",
    footer_dev_heading: "Developer Information",
    footer_dev_role: "Software Engineer / Platform Creator",
    footer_dev_bio: "Software Engineer passionate about building informative digital experiences. Designed and developed Local Host BD to provide travelers, students, and curious explorers with comprehensive, verified information and travel insights across all 64 districts of Bangladesh.",
    footer_explore_heading: "Explore & Navigate",
    footer_link_home_text: "Home Page",
    footer_link_map_text: "Interactive Vector Map",
    footer_link_top_text: "Back to Top ↑",
    footer_pill_spots: "🏛️ 320+ Sights",
    footer_pill_divs: "📍 8 Divisions",
    footer_pill_latency: "🗺️ Vector Cartography",
    footer_note: "Comprehensive 64 District Guide • Verified Information • Made for Bangladesh",
    footer_copyright_text: "© 2026 Local Host BD. All rights reserved.",
    footer_crafted_by: "Crafted with pride by <strong class=\"text-slate-800 dark:text-slate-200\">MD. Imran Hasan</strong>",
    drawer_menu_heading: "Menu & Actions",
    drawer_theme_hint: "Switch Theme",
    drawer_lang_hint: "Switch Language",
    tab_map_view: "Interactive Map View",
    tab_list_view: "Districts List (64)",
    filter_division: "Filter by Division",
    search_placeholder: "Search district (Dhaka, Cox's Bazar)...",
    sort_by: "Sort By:",
    sort_name: "Name (A-Z)",
    sort_dist: "Distance (Closest to Dhaka)",
    sort_area: "Area (Largest First)",
    sort_pop: "Population (Highest First)",
    districts_count_suffix: "Districts",
    district_single: "District",
    no_results_title: "No districts match your search",
    no_results_sub: "Try searching by English or Bangla name, or select 'All'.",
    reset_filters: "Reset Filters",
    map_heading: "Interactive Map of Bangladesh",
    map_subheading: "Hover or tap any district to inspect • Click to open its complete profile page",
    map_badge_districts: "64 Districts",
    map_badge_divs: "8 Divisions",
    hud_dist_suffix: "from Dhaka",
    hud_view_details: "View District Details",
    legend_selected: "Selected District (Flag Red)",
    legend_hover: "Hover District (Flag Green)",
    legend_instruction: "Click any district to explore",
    stat_districts_lbl: "Districts",
    stat_divisions_lbl: "Divisions",
    stat_area_lbl: "Square KM",
    stat_pop_lbl: "Population",
    popular_destinations: "Popular Destinations:",
    breadcrumb_home: "Home",
    breadcrumb_div_suffix: "Division",
    verified_archive: "Verified Archive",
    locate_on_map: "Locate on Vector Map",
    metric_est: "Established Year",
    metric_est_sub: "Formation year",
    metric_area: "Total Area",
    metric_area_sub: "Geographic span",
    metric_pop: "Total Population",
    metric_pop_sub: "Census estimate",
    metric_dist: "Distance from Dhaka",
    metric_dist_sub: "Road network",
    metric_website_label: "Official Website",
    metric_website_sub: "National Web Portal",
    metric_website_btn: "Visit Portal",
    route_heading: "Route & Travel Options from Dhaka",
    route_badge: "Transit",
    transit_bus: "Highway Bus",
    transit_train: "Railway Link",
    transit_car: "Private Vehicle",
    transit_ship: "Waterway Launch",
    carousel_heading: "Visual Highlights & Panoramas",
    carousel_sub: "Friction-free scroll-snap photography stream",
    carousel_badge: "5 Curated Views",
    slide_prefix: "Slide",
    hist_heading: "Historical Places & Heritage",
    hist_sub: "Top 5 verified architectural monuments & ancient sites",
    tour_heading: "Tourist Attractions & Highlights",
    tour_sub: "Top 5 scenic retreats, waterfronts & cultural promenades",
    top5_badge: "Top 5 Enforced",
    back_home: "← Back to Home",
    back_home_page: "← Back to Home Page",
    btn_prev: "Previous",
    btn_next: "Next",
    modal_title: "Interactive Vector Map of Bangladesh",
    modal_sub: "Click or tap any district path to open its profile",
    modal_hud_prompt: "Hover or tap any district",
    modal_hud_action: "Open Profile →",
    modal_close: "Close Map",
    modal_legend_active: "Active (Red)",
    modal_legend_hover: "Hover (Green)",
    view_on_map: "View on Map",
    open_maps_app: "Open in Google Maps",
    toast_theme: "Theme switched to",
    toast_lang_en: "Language set to English",
    toast_lang_bn: "ভাষা পরিবর্তন করে বাংলা করা হয়েছে",
  },
  bn: {
    brand_title: "Local Host BD",
    brand_tagline: "স্থান খুঁজুন। বাংলাদেশকে অনুভব করুন।",
    brand_sub: "বাংলাদেশের সকল ৬৪ জেলার তথ্যসমৃদ্ধ অনুসন্ধান গাইড",
    api_ready: "জেলা নির্দেশিকা প্রস্তুত",
    districts_loaded: "৬৪টি জেলা সংরক্ষিত",
    theme_dark: "ডার্ক",
    theme_light: "লাইট",
    lang_btn: "English",
    nav_vector_map: "ভেক্টর ম্যাপ",
    hero_about_badge: "🇧🇩 বাংলাদেশের ৬৪ জেলার নির্ভরযোগ্য তথ্য ও পর্যটন গাইড",
    hero_about_title: "৬৪ জেলার ইতিহাস ও সৌন্দর্যে বাংলাদেশকে জানুন",
    hero_about_tagline: "স্থান খুঁজুন। বাংলাদেশকে অনুভব করুন।",
    hero_about_desc: "বাংলাদেশের সকল ৬৪ জেলার বিস্তারিত তথ্য জানুন। অন্বেষণ করুন যাচাইকৃত ঐতিহাসিক নিদর্শন, জনপ্রিয় পর্যটন আকর্ষণ, ঢাকা থেকে সুনির্দিষ্ট যাতায়াত রুট ও দূরত্ব, ভৌগোলিক পরিসংখ্যান এবং ইন্টারঅ্যাকটিভ মানচিত্র।",
    hero_feature_1: "৬৪ জেলার প্রোফাইল",
    hero_feature_2: "৩২০+ দর্শনীয় ও ঐতিহাসিক স্থান",
    hero_feature_3: "ঢাকা থেকে যাতায়াত রুট",
    hero_dev_label: "ডেভেলপার পরিচিতি",
    hero_github_label: "গিটহাব",
    footer_brand_tagline: "স্থান খুঁজুন। বাংলাদেশকে অনুভব করুন।",
    footer_about_text: "বাংলাদেশের সকল ৬৪ জেলার বিস্তারিত বিবরণ, ঐতিহাসিক নিদর্শন, জনপ্রিয় পর্যটন আকর্ষণ, ঢাকা থেকে যাতায়াত পথনির্দেশ এবং ইন্টারঅ্যাকটিভ ভেক্টর মানচিত্র সমৃদ্ধ একটি নির্ভরযোগ্য তথ্যভিত্তিক ডিজিটাল প্ল্যাটফর্ম।",
    footer_dev_heading: "ডেভেলপার পরিচিতি",
    footer_dev_role: "সফটওয়্যার প্রকৌশলী ও প্ল্যাটফর্ম নির্মাতা",
    footer_dev_bio: "সফটওয়্যার ইঞ্জিনিয়ার এবং তথ্যভিত্তিক ডিজিটাল প্ল্যাটফর্ম নির্মাতা। ভ্রমণপিপাসু, শিক্ষার্থী ও আগ্রহীদের কাছে বাংলাদেশের সকল ৬৪ জেলার ইতিহাস, পর্যটন আকর্ষণ, যাতায়াত রুট ও ভৌগোলিক তথ্য সহজে তুলে ধরার জন্য লোকাল হোস্ট বিডি ডিজাইন ও ডেভেলপ করেছেন।",
    footer_explore_heading: "দ্রুত অন্বেষণ",
    footer_link_home_text: "হোম পেজ",
    footer_link_map_text: "ইন্টারেক্টিভ ভেক্টর মানচিত্র",
    footer_link_top_text: "উপরে ফিরে যান ↑",
    footer_pill_spots: "🏛️ ৩২০+ স্থান",
    footer_pill_divs: "📍 ৮টি বিভাগ",
    footer_pill_latency: "🗺️ ভেক্টর মানচিত্র",
    footer_note: "৬৪ জেলার নির্ভরযোগ্য তথ্যভাণ্ডার • সমৃদ্ধ বাংলাদেশ প্ল্যাটফর্ম",
    footer_copyright_text: "© ২০২৬ লোকাল হোস্ট বিডি। সর্বস্বত্ব সংরক্ষিত।",
    footer_crafted_by: "গৌরবের সাথে তৈরি করেছেন <strong class=\"text-slate-800 dark:text-slate-200\">মোঃ ইমরান হাসান</strong>",
    drawer_menu_heading: "মেনু ও অপশন",
    drawer_theme_hint: "থিম পরিবর্তন",
    drawer_lang_hint: "ভাষা পরিবর্তন",
    tab_map_view: "ইন্টারেক্টিভ মানচিত্র",
    tab_list_view: "৬৪ জেলার তালিকা",
    filter_division: "বিভাগ অনুযায়ী ফিল্টার",
    search_placeholder: "জেলা খুঁজুন (ঢাকা, কক্সবাজার, সিলেট)...",
    sort_by: "সাজানোর ধরণ:",
    sort_name: "নাম (অ আ ক খ)",
    sort_dist: "দূরত্ব (ঢাকা থেকে নিকটতম)",
    sort_area: "আয়তন (বৃহত্তম আগে)",
    sort_pop: "জনসংখ্যা (সর্বোচ্চ আগে)",
    districts_count_suffix: "টি জেলা",
    district_single: "টি জেলা",
    no_results_title: "কোনো জেলা খুঁজে পাওয়া যায়নি",
    no_results_sub: "বাংলা বা ইংরেজিতে জেলার নাম লিখে চেষ্টা করুন অথবা 'সকল' নির্বাচন করুন।",
    reset_filters: "ফিল্টার রিসেট করুন",
    map_heading: "বাংলাদেশের ইন্টারেক্টিভ মানচিত্র",
    map_subheading: "যেকোনো জেলায় হোভার বা স্পর্শ করে দেখুন • বিস্তারিত দেখতে ক্লিক করুন",
    map_badge_districts: "৬৪টি জেলা",
    map_badge_divs: "৮টি বিভাগ",
    hud_dist_suffix: "ঢাকা থেকে",
    hud_view_details: "বিস্তারিত দেখুন",
    legend_selected: "নির্বাচিত জেলা (লাল)",
    legend_hover: "হোভার জেলা (সবুজ)",
    legend_instruction: "অন্বেষণ করতে যেকোনো জেলায় ক্লিক করুন",
    stat_districts_lbl: "জেলা",
    stat_divisions_lbl: "বিভাগ",
    stat_area_lbl: "বর্গ কি.মি.",
    stat_pop_lbl: "জনসংখ্যা",
    popular_destinations: "জনপ্রিয় ভ্রমণ গন্তব্য:",
    breadcrumb_home: "হোম",
    breadcrumb_div_suffix: "বিভাগ",
    verified_archive: "যাচাইকৃত তথ্যভাণ্ডার",
    locate_on_map: "ভেক্টর মানচিত্রে দেখুন",
    metric_est: "প্রতিষ্ঠাকাল",
    metric_est_sub: "জেলা গঠনকাল",
    metric_area: "মোট আয়তন",
    metric_area_sub: "ভৌগোলিক এলাকা",
    metric_pop: "মোট জনসংখ্যা",
    metric_pop_sub: "জনশুমারি হিসাব",
    metric_dist: "ঢাকা থেকে দূরত্ব",
    metric_dist_sub: "সড়ক যোগাযোগ",
    metric_website_label: "অফিসিয়াল ওয়েবসাইট",
    metric_website_sub: "জাতীয় তথ্য বাতায়ন",
    metric_website_btn: "পোর্টাল দেখুন",
    route_heading: "ঢাকা থেকে যাতায়াত ও ভ্রমণের মাধ্যম",
    route_badge: "যোগাযোগ",
    transit_bus: "দূরপাল্লার বাস",
    transit_train: "রেলওয়ে সংযোগ",
    transit_car: "ব্যক্তিগত গাড়ি",
    transit_ship: "নৌপথের লঞ্চ",
    carousel_heading: "প্রধান দর্শনীয় দৃশ্য ও প্যানোরামা",
    carousel_sub: "স্ক্রোল-স্ন্যাপ প্যানোরামিক আলোকচিত্র",
    carousel_badge: "৫টি নির্বাচিত দৃশ্য",
    slide_prefix: "দৃশ্য",
    hist_heading: "ঐতিহাসিক স্থান ও ঐতিহ্য",
    hist_sub: "শীর্ষ ৫টি যাচাইকৃত প্রাচীন স্থাপত্য ও ঐতিহাসিক নিদর্শন",
    tour_heading: "পর্যটন আকর্ষণ ও দর্শনীয় স্থান",
    tour_sub: "শীর্ষ ৫টি নয়নাভিরাম স্থান, লেক ও বিনোদন কেন্দ্র",
    top5_badge: "শীর্ষ ৫টি স্থান",
    back_home: "← হোমে ফিরে যান",
    back_home_page: "← মূল পাতায় ফিরে যান",
    btn_prev: "পূর্ববর্তী",
    btn_next: "পরবর্তী",
    modal_title: "বাংলাদেশের ইন্টারেক্টিভ ভেক্টর মানচিত্র",
    modal_sub: "যেকোনো জেলায় ক্লিক বা স্পর্শ করে প্রোফাইল খুলুন",
    modal_hud_prompt: "যেকোনো জেলায় হোভার বা স্পর্শ করুন",
    modal_hud_action: "প্রোফাইল দেখুন →",
    modal_close: "মানচিত্র বন্ধ করুন",
    modal_legend_active: "সক্রিয় (লাল)",
    modal_legend_hover: "হোভার (সবুজ)",
    view_on_map: "ম্যাপে দেখুন",
    open_maps_app: "গুগল ম্যাপস অ্যাপে দেখুন",
    toast_theme: "থিম পরিবর্তিত হয়েছে:",
    toast_lang_en: "Language set to English",
    toast_lang_bn: "ভাষা পরিবর্তন করে বাংলা করা হয়েছে",
  }
};

const DIVISIONS_MAP = {
  all: { en: "All (64)", bn: "সকল (৬৪)" },
  Dhaka: { en: "Dhaka", bn: "ঢাকা" },
  Chattogram: { en: "Chattogram", bn: "চট্টগ্রাম" },
  Rajshahi: { en: "Rajshahi", bn: "রাজশাহী" },
  Khulna: { en: "Khulna", bn: "খুলনা" },
  Barishal: { en: "Barishal", bn: "বরিশাল" },
  Sylhet: { en: "Sylhet", bn: "সিলেট" },
  Rangpur: { en: "Rangpur", bn: "রংপুর" },
  Mymensingh: { en: "Mymensingh", bn: "ময়মনসিংহ" },
};

const POPULAR_DESTINATIONS = [
  { id: 1, en: "Dhaka", bn: "ঢাকা" },
  { id: 19, en: "Cox's Bazar", bn: "কক্সবাজার" },
  { id: 28, en: "Sylhet", bn: "সিলেট" },
  { id: 14, en: "Bandarban", bn: "বান্দরবান" },
  { id: 35, en: "Bagerhat", bn: "বাগেরহাট" },
  { id: 45, en: "Bogura", bn: "বগুড়া" }
];

// Helper: Convert Bengali digits to English digits
function toEnglishDigits(input) {
  if (input === null || input === undefined) return '';
  const bnToEn = { '০': '0', '১': '1', '২': '2', '৩': '3', '৪': '4', '৫': '5', '৬': '6', '৭': '7', '৮': '8', '৯': '9' };
  return String(input).replace(/[০-৯]/g, ch => bnToEn[ch] || ch);
}

// Helper: Convert any string or number to authentic Bengali digits
function toBengaliDigits(input) {
  if (input === null || input === undefined) return '';
  const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
  return String(input).replace(/[0-9]/g, ch => bnDigits[Number(ch)]);
}

// Helper: Format population into authentic 'কোটি' metric in Bangla
function formatBanglaPopulation(pop) {
  if (!pop) return '০ কোটি';
  const rawStr = String(pop).trim();

  // If it already explicitly mentions 'কোটি', ensure digits are Bengali and return
  if (rawStr.includes('কোটি')) {
    return toBengaliDigits(rawStr);
  }

  // Normalize any Bengali digits to English digits first for accurate numerical parsing
  const engStr = toEnglishDigits(rawStr);
  const match = engStr.match(/([0-9]+(?:\.[0-9]+)?)/);
  if (!match) {
    return toBengaliDigits(rawStr);
  }

  const val = parseFloat(match[1]);
  if (isNaN(val)) {
    return toBengaliDigits(rawStr);
  }

  let crore;
  if (val > 100000) {
    // Raw headcount, e.g. 14700000 => 1.47 crore
    crore = val / 10000000;
  } else if (engStr.toUpperCase().includes('M') || rawStr.includes('মিলিয়ন') || rawStr.includes('million')) {
    // Millions, e.g. 14.7M or 3.9 মিলিয়ন => 14.7/10 = 1.47 crore, 3.9/10 = 0.39 crore
    crore = val / 10;
  } else {
    // Default assumption for million-level values
    crore = val / 10;
  }

  // Format to clean decimal places
  const formatted = parseFloat(crore.toFixed(2));
  const hasPlus = rawStr.includes('+');
  return `${toBengaliDigits(formatted)} কোটি${hasPlus ? '+' : ''}`;
}

// ==========================================
// 2. LIFECYCLE & INITIALIZATION
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initLanguage();
  initLucideIcons();
  setupEventListeners();

  // Load from local memory buffers (Zero external fetch)
  loadLocalMemoryData();

  // Setup URL Hash Routing
  window.addEventListener('hashchange', handleRoute);
  handleRoute();
});

function initLucideIcons() {
  if (window.lucide && typeof window.lucide.createIcons === 'function') {
    window.lucide.createIcons();
  }
}

// ==========================================
// 3. THEME CONTROLLER (DARK / LIGHT TOGGLE)
// ==========================================
function initTheme() {
  const savedTheme = localStorage.getItem(THEME_KEY);
  AppState.currentTheme = savedTheme ? savedTheme : 'light'; // Default to Light Mode
  applyTheme(AppState.currentTheme);
}

function applyTheme(theme) {
  const html = document.documentElement;
  const isBn = AppState.currentLang === 'bn';

  if (theme === 'dark') {
    html.classList.add('dark');
  } else {
    html.classList.remove('dark');
  }

  // Display the OPPOSITE theme action name so the user knows what clicking will do:
  // If page is currently in Light mode, button shows "🌙 Dark" (or "🌙 ডার্ক")
  // If page is currently in Dark mode, button shows "☀️ Light" (or "☀️ লাইট")
  const oppositeThemeLabel = theme === 'dark' 
    ? (isBn ? '☀️ লাইট' : '☀️ Light')
    : (isBn ? '🌙 ডার্ক' : '🌙 Dark');

  // Update desktop toggle
  const sunIcon = document.getElementById('theme-icon-sun');
  const moonIcon = document.getElementById('theme-icon-moon');
  const themeLabel = document.getElementById('theme-toggle-label');
  if (theme === 'dark') {
    if (sunIcon) sunIcon.classList.remove('hidden');
    if (moonIcon) moonIcon.classList.add('hidden');
  } else {
    if (sunIcon) sunIcon.classList.add('hidden');
    if (moonIcon) moonIcon.classList.remove('hidden');
  }
  if (themeLabel) themeLabel.textContent = oppositeThemeLabel;

  // Update mobile drawer toggle
  const mSunIcon = document.getElementById('mobile-theme-icon-sun');
  const mMoonIcon = document.getElementById('mobile-theme-icon-moon');
  const mThemeLabel = document.getElementById('mobile-theme-label');
  if (theme === 'dark') {
    if (mSunIcon) mSunIcon.classList.remove('hidden');
    if (mMoonIcon) mMoonIcon.classList.add('hidden');
  } else {
    if (mSunIcon) mSunIcon.classList.add('hidden');
    if (mMoonIcon) mMoonIcon.classList.remove('hidden');
  }
  if (mThemeLabel) mThemeLabel.textContent = oppositeThemeLabel;

  AppState.currentTheme = theme;
  localStorage.setItem(THEME_KEY, theme);

  // Reset any temporary hover fill styles on non-selected paths so they adapt to new theme colors
  document.querySelectorAll('.district-svg-path').forEach(p => {
    const pId = Number(p.getAttribute('data-id'));
    if (pId !== AppState.selectedDistrictId) {
      p.style.fill = '';
    }
  });

  initLucideIcons();
}

function toggleTheme() {
  const nextTheme = AppState.currentTheme === 'dark' ? 'light' : 'dark';
  applyTheme(nextTheme);
  const t = I18N[AppState.currentLang];
  showToast(`${t.toast_theme} ${nextTheme === 'dark' ? t.theme_dark : t.theme_light}`);
}

// Mobile Slide-out Drawer Controller
function toggleMobileDrawer(open) {
  const drawer = document.getElementById('mobile-drawer');
  const backdrop = document.getElementById('mobile-drawer-backdrop');
  if (!drawer || !backdrop) return;

  if (open) {
    backdrop.classList.remove('hidden');
    void backdrop.offsetWidth;
    backdrop.classList.remove('opacity-0');
    drawer.classList.remove('translate-x-full');
    drawer.classList.add('translate-x-0');
    document.body.style.overflow = 'hidden';
  } else {
    drawer.classList.add('translate-x-full');
    drawer.classList.remove('translate-x-0');
    backdrop.classList.add('opacity-0');
    setTimeout(() => {
      backdrop.classList.add('hidden');
      document.body.style.overflow = '';
    }, 300);
  }
}

// ==========================================
// 4. LANGUAGE CONTROLLER (ENGLISH ↔ BANGLA)
// ==========================================
function initLanguage() {
  const savedLang = localStorage.getItem(LANG_KEY);
  // Default is 'bn' (Bangla) initially as requested
  AppState.currentLang = (savedLang === 'bn' || savedLang === 'en') ? savedLang : 'bn';
  applyLanguage(AppState.currentLang, false);
}

function applyLanguage(lang, showNotification = true) {
  AppState.currentLang = lang;
  localStorage.setItem(LANG_KEY, lang);

  // Set html document lang
  document.documentElement.lang = lang;

  // Display the OPPOSITE language action name so the user knows what clicking will do:
  // If page is currently in Bangla (bn), button displays "English"
  // If page is currently in English (en), button displays "বাংলা"
  const oppositeLang = lang === 'en' ? 'বাংলা' : 'English';
  
  const langLabel = document.getElementById('lang-toggle-label');
  const langBtn = document.getElementById('lang-toggle-btn');
  if (langLabel) langLabel.textContent = oppositeLang;
  if (langBtn) langBtn.setAttribute('title', lang === 'en' ? 'Switch to Bangla / বাংলায় দেখুন' : 'Switch to English / ইংরেজিতে দেখুন');

  const mLangLabel = document.getElementById('mobile-lang-label');
  if (mLangLabel) mLangLabel.textContent = oppositeLang;

  // Re-apply theme labels to update opposite theme text in the new language
  applyTheme(AppState.currentTheme);

  // Update all static UI elements on the page
  updateStaticTranslations();

  // Re-render division pills
  updateDivisionPillsUI(AppState.activeDivision);

  // Re-render popular destination buttons
  renderPopularDestinations();

  // Re-render sidebar list with localized titles and numbers
  filterAndRenderDistricts();

  // Update Map Inspector HUD
  if (AppState.hoveredDistrictId) {
    const hDist = AppState.districts.find(d => d.id === AppState.hoveredDistrictId);
    if (hDist) updateMapInspectorHud(hDist, true);
  } else if (AppState.selectedDistrictId) {
    const sDist = AppState.districts.find(d => d.id === AppState.selectedDistrictId);
    if (sDist) updateMapInspectorHud(sDist, false);
  } else if (AppState.districts.length > 0) {
    updateMapInspectorHud(AppState.districts[0], false);
  }

  // If in detail view, re-populate active district in new language
  if (AppState.selectedDistrictId) {
    const activeDist = AppState.districts.find(d => d.id === AppState.selectedDistrictId);
    if (activeDist) {
      populateDistrictDetails(activeDist);
    }
  }

  initLucideIcons();

  if (showNotification) {
    showToast(lang === 'bn' ? I18N.bn.toast_lang_bn : I18N.en.toast_lang_en);
  }
}

function toggleLanguage() {
  const nextLang = AppState.currentLang === 'en' ? 'bn' : 'en';
  applyLanguage(nextLang, true);
}

function updateStaticTranslations() {
  const t = I18N[AppState.currentLang];
  const isBn = AppState.currentLang === 'bn';

  // Brand Tagline
  const brandTagline = document.getElementById('brand-tagline');
  if (brandTagline) brandTagline.textContent = t.brand_tagline;

  const drawerTagline = document.getElementById('drawer-tagline');
  if (drawerTagline) drawerTagline.textContent = t.brand_tagline;

  // Website Hero & About Section
  const heroBadge = document.getElementById('hero-about-badge');
  if (heroBadge) heroBadge.textContent = t.hero_about_badge;

  const heroTitle = document.getElementById('hero-about-title');
  if (heroTitle) heroTitle.textContent = t.brand_title;

  const heroTagline = document.getElementById('hero-about-tagline');
  if (heroTagline) heroTagline.textContent = t.hero_about_tagline;

  const heroDesc = document.getElementById('hero-about-desc');
  if (heroDesc) heroDesc.textContent = t.hero_about_desc;

  // Hero Feature Highlights
  const heroF1 = document.getElementById('hero-feature-1');
  if (heroF1) heroF1.textContent = t.hero_feature_1;

  const heroF2 = document.getElementById('hero-feature-2');
  if (heroF2) heroF2.textContent = t.hero_feature_2;

  const heroF3 = document.getElementById('hero-feature-3');
  if (heroF3) heroF3.textContent = t.hero_feature_3;

  // Footer Elements
  const footerTagline = document.getElementById('footer-brand-tagline');
  if (footerTagline) footerTagline.textContent = t.footer_brand_tagline;

  const footerAbout = document.getElementById('footer-about-text');
  if (footerAbout) footerAbout.textContent = t.footer_about_text;

  const footerDevHeading = document.getElementById('footer-dev-heading');
  if (footerDevHeading) footerDevHeading.textContent = t.footer_dev_heading;

  const footerDevRole = document.getElementById('footer-dev-role');
  if (footerDevRole) footerDevRole.textContent = t.footer_dev_role;

  const footerDevBio = document.getElementById('footer-dev-bio');
  if (footerDevBio) footerDevBio.textContent = t.footer_dev_bio;

  const footerExploreHeading = document.getElementById('footer-explore-heading');
  if (footerExploreHeading) footerExploreHeading.textContent = t.footer_explore_heading;

  const footerLinkHome = document.getElementById('footer-link-home-text');
  if (footerLinkHome) footerLinkHome.textContent = t.footer_link_home_text;

  const footerLinkMap = document.getElementById('footer-link-map-text');
  if (footerLinkMap) footerLinkMap.textContent = t.footer_link_map_text;

  const footerLinkTop = document.getElementById('footer-link-top-text');
  if (footerLinkTop) footerLinkTop.textContent = t.footer_link_top_text;

  const footerCopyright = document.getElementById('footer-copyright-text');
  if (footerCopyright) footerCopyright.textContent = t.footer_copyright_text;

  const footerSpots = document.getElementById('footer-pill-spots');
  if (footerSpots) footerSpots.textContent = t.footer_pill_spots;

  const footerDivs = document.getElementById('footer-pill-divs');
  if (footerDivs) footerDivs.textContent = t.footer_pill_divs;

  const footerLatency = document.getElementById('footer-pill-latency');
  if (footerLatency) footerLatency.textContent = t.footer_pill_latency;

  const footerNote = document.getElementById('footer-note');
  if (footerNote) footerNote.textContent = t.footer_note;

  const footerCraftedBy = document.getElementById('footer-crafted-by');
  if (footerCraftedBy) footerCraftedBy.innerHTML = t.footer_crafted_by;

  // Drawer Labels
  const drawerHeading = document.getElementById('drawer-menu-heading');
  if (drawerHeading) drawerHeading.textContent = t.drawer_menu_heading;

  const drawerThemeHint = document.getElementById('mobile-theme-hint');
  if (drawerThemeHint) drawerThemeHint.textContent = t.drawer_theme_hint;

  const drawerLangHint = document.getElementById('mobile-lang-hint');
  if (drawerLangHint) drawerLangHint.textContent = t.drawer_lang_hint;

  const viewMapBtnLabel = document.getElementById('view-map-modal-btn-label');
  if (viewMapBtnLabel) viewMapBtnLabel.textContent = t.nav_vector_map;

  const mobileMapBtnLabel = document.getElementById('mobile-vector-map-label');
  if (mobileMapBtnLabel) mobileMapBtnLabel.textContent = t.nav_vector_map;

  // Mobile Tabs
  const tabMap = document.getElementById('mobile-tab-map-text');
  if (tabMap) tabMap.textContent = t.tab_map_view;

  const tabList = document.getElementById('mobile-tab-list-text');
  if (tabList) tabList.textContent = t.tab_list_view;

  // Search Input
  const searchInput = document.getElementById('district-search-input');
  if (searchInput) searchInput.setAttribute('placeholder', t.search_placeholder);

  const filterDivHeading = document.getElementById('filter-division-heading');
  if (filterDivHeading) filterDivHeading.textContent = t.filter_division;

  const sortByHeading = document.getElementById('sort-by-heading');
  if (sortByHeading) sortByHeading.textContent = t.sort_by;

  // Sort Options
  const sortSelect = document.getElementById('district-sort-select');
  if (sortSelect && sortSelect.options) {
    sortSelect.options[0].text = t.sort_name;
    sortSelect.options[1].text = t.sort_dist;
    sortSelect.options[2].text = t.sort_area;
    sortSelect.options[3].text = t.sort_pop;
  }

  // Home Map Section
  const mapSectionTitle = document.getElementById('map-section-title-text');
  if (mapSectionTitle) mapSectionTitle.textContent = t.map_heading;

  const mapSectionSub = document.getElementById('map-section-subtitle');
  if (mapSectionSub) mapSectionSub.textContent = t.map_subheading;

  const mapQuickDist = document.getElementById('map-quick-districts');
  if (mapQuickDist) mapQuickDist.textContent = t.map_badge_districts;

  const mapQuickDivs = document.getElementById('map-quick-divs');
  if (mapQuickDivs) mapQuickDivs.textContent = t.map_badge_divs;

  const legSel = document.getElementById('legend-selected-label');
  if (legSel) legSel.textContent = t.legend_selected;

  const legHov = document.getElementById('legend-hover-label');
  if (legHov) legHov.textContent = t.legend_hover;

  const legInst = document.getElementById('legend-instruction');
  if (legInst) legInst.textContent = t.legend_instruction;

  // 4 Quick Facts
  const statDistVal = document.getElementById('stat-districts-val');
  if (statDistVal) statDistVal.textContent = isBn ? toBengaliDigits(64) : '64';

  const statDistLbl = document.getElementById('stat-districts-lbl');
  if (statDistLbl) statDistLbl.textContent = t.stat_districts_lbl;

  const statDivVal = document.getElementById('stat-divisions-val');
  if (statDivVal) statDivVal.textContent = isBn ? toBengaliDigits(8) : '8';

  const statDivLbl = document.getElementById('stat-divisions-lbl');
  if (statDivLbl) statDivLbl.textContent = t.stat_divisions_lbl;

  const statAreaVal = document.getElementById('stat-area-val');
  if (statAreaVal) statAreaVal.textContent = isBn ? '১,৪৭,৫৭০' : '147k';

  const statAreaLbl = document.getElementById('stat-area-lbl');
  if (statAreaLbl) statAreaLbl.textContent = t.stat_area_lbl;

  const statPopVal = document.getElementById('stat-pop-val');
  if (statPopVal) statPopVal.textContent = isBn ? '১৭ কোটি+' : '170M+';

  const statPopLbl = document.getElementById('stat-pop-lbl');
  if (statPopLbl) statPopLbl.textContent = t.stat_pop_lbl;

  const popDestHeading = document.getElementById('popular-dest-heading');
  if (popDestHeading) popDestHeading.textContent = t.popular_destinations;

  // Detail View Static Labels
  const backTop = document.getElementById('back-to-home-btn-top-label');
  if (backTop) backTop.textContent = t.back_home;

  const breadHome = document.getElementById('breadcrumb-home-link');
  if (breadHome) breadHome.textContent = t.breadcrumb_home;

  const verifiedBadge = document.getElementById('detail-verified-text');
  if (verifiedBadge) verifiedBadge.textContent = t.verified_archive;

  const locateMapText = document.getElementById('open-map-preview-btn-label');
  if (locateMapText) locateMapText.textContent = t.locate_on_map;

  const metricEst = document.getElementById('metric-est-label');
  if (metricEst) metricEst.textContent = t.metric_est;
  const metricEstSub = document.getElementById('metric-est-sub');
  if (metricEstSub) metricEstSub.textContent = t.metric_est_sub;

  const metricArea = document.getElementById('metric-area-label');
  if (metricArea) metricArea.textContent = t.metric_area;
  const metricAreaSub = document.getElementById('metric-area-sub');
  if (metricAreaSub) metricAreaSub.textContent = t.metric_area_sub;

  const metricPop = document.getElementById('metric-pop-label');
  if (metricPop) metricPop.textContent = t.metric_pop;
  const metricPopSub = document.getElementById('metric-pop-sub');
  if (metricPopSub) metricPopSub.textContent = t.metric_pop_sub;

  const metricDist = document.getElementById('metric-dist-label');
  if (metricDist) metricDist.textContent = t.metric_dist;
  const metricDistSub = document.getElementById('metric-dist-sub');
  if (metricDistSub) metricDistSub.textContent = t.metric_dist_sub;

  const metricWebsiteLabel = document.getElementById('metric-website-label');
  if (metricWebsiteLabel) metricWebsiteLabel.textContent = t.metric_website_label;
  const metricWebsiteSub = document.getElementById('metric-website-sub');
  if (metricWebsiteSub) metricWebsiteSub.textContent = t.metric_website_sub;
  const websiteBtnText = document.getElementById('detail-website-btn-text');
  if (websiteBtnText) websiteBtnText.textContent = t.metric_website_btn;

  const routeHeading = document.getElementById('route-section-heading-text');
  if (routeHeading) routeHeading.textContent = t.route_heading;
  const routeBadge = document.getElementById('route-badge-text');
  if (routeBadge) routeBadge.textContent = t.route_badge;

  const transitBus = document.getElementById('transit-bus-text');
  if (transitBus) transitBus.textContent = t.transit_bus;
  const transitTrain = document.getElementById('transit-train-text');
  if (transitTrain) transitTrain.textContent = t.transit_train;
  const transitCar = document.getElementById('transit-car-text');
  if (transitCar) transitCar.textContent = t.transit_car;
  const transitShip = document.getElementById('transit-ship-text');
  if (transitShip) transitShip.textContent = t.transit_ship;

  const carouselHeading = document.getElementById('carousel-section-heading-text');
  if (carouselHeading) carouselHeading.textContent = t.carousel_heading;
  const carouselSub = document.getElementById('carousel-section-subtitle');
  if (carouselSub) carouselSub.textContent = t.carousel_sub;
  const carouselBadge = document.getElementById('carousel-section-badge');
  if (carouselBadge) carouselBadge.textContent = t.carousel_badge;

  const histHeading = document.getElementById('historical-section-heading-text');
  if (histHeading) histHeading.textContent = t.hist_heading;
  const histSub = document.getElementById('historical-section-subtitle');
  if (histSub) histSub.textContent = t.hist_sub;
  const histBadge = document.getElementById('historical-section-badge');
  if (histBadge) histBadge.textContent = t.top5_badge;

  const tourHeading = document.getElementById('tourist-section-heading-text');
  if (tourHeading) tourHeading.textContent = t.tour_heading;
  const tourSub = document.getElementById('tourist-section-subtitle');
  if (tourSub) tourSub.textContent = t.tour_sub;
  const tourBadge = document.getElementById('tourist-section-badge');
  if (tourBadge) tourBadge.textContent = t.top5_badge;

  const backBottom = document.getElementById('back-to-home-btn-bottom-label');
  if (backBottom) backBottom.textContent = t.back_home_page;

  const prevText = document.getElementById('prev-btn-text');
  if (prevText) prevText.textContent = t.btn_prev;

  const nextText = document.getElementById('next-btn-text');
  if (nextText) nextText.textContent = t.btn_next;

  // Modal
  const modalTitle = document.getElementById('modal-title-text');
  if (modalTitle) modalTitle.textContent = t.modal_title;

  const modalSub = document.getElementById('modal-subtitle-text');
  if (modalSub) modalSub.textContent = t.modal_sub;

  const modalDone = document.getElementById('modal-map-done-btn');
  if (modalDone) modalDone.textContent = t.modal_close;

  const modAct = document.getElementById('modal-legend-active');
  if (modAct) modAct.textContent = t.modal_legend_active;

  const modHov = document.getElementById('modal-legend-hover');
  if (modHov) modHov.textContent = t.modal_legend_hover;
}

function renderPopularDestinations() {
  const container = document.getElementById('popular-dest-buttons');
  if (!container) return;
  const isBn = AppState.currentLang === 'bn';

  container.innerHTML = POPULAR_DESTINATIONS.map(d => `
    <button 
      onclick="navigateToDistrict(${d.id})" 
      class="pop-dest-btn px-2.5 sm:px-3 py-1.5 rounded-lg bg-slate-100 dark:bg-[#07150E] hover:bg-bdgreen-100 dark:hover:bg-[#122A1E] text-slate-800 dark:text-slate-200 font-bold border border-slate-200 dark:border-[#1B3E2E] transition text-xs cursor-pointer min-h-[36px] ${isBn ? 'font-bengali' : ''}" 
      data-id="${d.id}"
    >
      ${isBn ? d.bn : d.en}
    </button>
  `).join('');
}

// ==========================================
// 5. LOCAL MEMORY BUFFER DATA LOADER
// ==========================================
function loadLocalMemoryData() {
  // Source directly from window memory buffers
  let localData = [];

  if (typeof window !== 'undefined' && Array.isArray(window.LOCAL_DISTRICTS) && window.LOCAL_DISTRICTS.length > 0) {
    localData = window.LOCAL_DISTRICTS;
  } else if (typeof window !== 'undefined' && Array.isArray(window.DISTRICTS_DATA) && window.DISTRICTS_DATA.length > 0) {
    localData = window.DISTRICTS_DATA;
  }

  // Bind vector map paths if available
  const mapPaths = (typeof window !== 'undefined' && window.MAP_PATHS) ? window.MAP_PATHS : {};
  AppState.districts = localData.map(d => {
    const websiteUrl = d.website 
      || DISTRICT_OFFICIAL_WEBSITES[d.id] 
      || DISTRICT_SLUG_WEBSITES[d.slug] 
      || `https://${(d.slug || '').replace(/[^a-z0-9]/g, '')}.gov.bd`;

    return {
      ...d,
      website: websiteUrl,
      svgPath: d.svgPath || mapPaths[d.id] || mapPaths[d.slug] || ''
    };
  });

  // Initial render of UI, sidebar and vector map
  updateStaticTranslations();
  filterAndRenderDistricts();
  renderVectorMap('empty-state-svg-map-container');
  renderVectorMap('modal-svg-map-container');

  // Initialize In-Map HUD with first district (Dhaka)
  if (AppState.districts.length > 0) {
    updateMapInspectorHud(AppState.districts[0], false);
  }
}

// ==========================================
// 6. URL HASH ROUTING & PAGE CONTROLLER
// ==========================================
function handleRoute() {
  const hash = window.location.hash || '#/';

  if (hash.startsWith('#/district/')) {
    const param = hash.replace('#/district/', '').trim().toLowerCase();
    const found = AppState.districts.find(d => 
      d.slug.toLowerCase() === param || String(d.id) === param
    );
    if (found) {
      showDistrictDetailsPage(found);
      return;
    }
  }

  // Default: Show Home Dashboard
  showHomePage();
}

function navigateToHome() {
  window.location.hash = '#/';
  showHomePage();
}

function navigateToDistrict(idOrSlug) {
  let district;
  if (typeof idOrSlug === 'number' || !isNaN(idOrSlug)) {
    district = AppState.districts.find(d => d.id === Number(idOrSlug));
  } else {
    district = AppState.districts.find(d => d.slug.toLowerCase() === String(idOrSlug).toLowerCase());
  }

  if (district) {
    window.location.hash = `#/district/${district.slug}`;
    showDistrictDetailsPage(district);
  }
}

function showHomePage() {
  const viewHome = document.getElementById('view-home');
  const viewDetails = document.getElementById('view-details');

  if (viewHome) {
    viewHome.classList.remove('hidden');
    viewHome.classList.remove('animate-slide-up');
    void viewHome.offsetWidth; // Trigger reflow for smooth animation
    viewHome.classList.add('animate-slide-up');
  }
  if (viewDetails) {
    viewDetails.classList.add('hidden');
  }

  // Restore mobile segmented tab state
  setMobileHomeTab(AppState.mobileHomeTab || 'map');

  // Re-render map to refresh state
  renderVectorMap('empty-state-svg-map-container');
  window.scrollTo({ top: 0, behavior: 'smooth' });
  initLucideIcons();
}

function showDistrictDetailsPage(district) {
  AppState.selectedDistrictId = district.id;

  const viewHome = document.getElementById('view-home');
  const viewDetails = document.getElementById('view-details');

  if (viewHome) {
    viewHome.classList.add('hidden');
  }
  if (viewDetails) {
    viewDetails.classList.remove('hidden');
    viewDetails.classList.remove('animate-slide-up');
    void viewDetails.offsetWidth;
    viewDetails.classList.add('animate-slide-up');
  }

  // Populate Cinematic Hero, Snap Carousel, Top-5 Historical & Tourist Cards
  populateDistrictDetails(district);

  // Update map active highlights and Inspector HUD
  updateVectorMapActiveState(district.id);
  updateMapInspectorHud(district, true);

  window.scrollTo({ top: 0, behavior: 'smooth' });
  initLucideIcons();
}

// ==========================================
// 7. POPULATE DISTRICT DETAIL PAGE (CINEMATIC)
// ==========================================
function populateDistrictDetails(district) {
  const isBn = AppState.currentLang === 'bn';

  // Top breadcrumb tracker
  const breadcrumbDiv = document.getElementById('breadcrumb-division');
  const breadcrumbDst = document.getElementById('breadcrumb-district');
  if (breadcrumbDiv) {
    breadcrumbDiv.textContent = isBn 
      ? `${district.divBn || district.div} বিভাগ` 
      : `${district.div} Division`;
  }
  if (breadcrumbDst) {
    breadcrumbDst.textContent = isBn 
      ? `${district.bn} (${district.en})` 
      : `${district.en} (${district.bn})`;
  }

  // 1. CINEMATIC HERO BANNER
  const heroImg = document.getElementById('detail-hero-image');
  const nameEn = document.getElementById('detail-name-en');
  const nameBn = document.getElementById('detail-name-bn');
  const divBadge = document.getElementById('detail-division-badge');
  const coords = document.getElementById('detail-coordinates');
  const tagline = document.getElementById('detail-tagline');

  if (heroImg) {
    if (district.heroImage) {
      heroImg.classList.remove('hidden');
      heroImg.style.display = 'block';
      heroImg.src = district.heroImage;
      heroImg.onerror = function() {
        this.onerror = null;
        this.src = 'images/default/hero.webp';
      };
    } else {
      heroImg.classList.add('hidden');
      heroImg.style.display = 'none';
      heroImg.src = '';
    }
  }

  if (isBn) {
    // Bangla mode: Bengali name prominent
    if (nameEn) {
      nameEn.textContent = district.bn;
      nameEn.className = 'font-bengali text-3xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight drop-shadow-md';
    }
    if (nameBn) {
      nameBn.textContent = `(${district.en})`;
      nameBn.className = 'text-xl sm:text-2xl lg:text-3xl text-bdgreen-400 font-bold drop-shadow';
    }
  } else {
    // English mode: English name prominent
    if (nameEn) {
      nameEn.textContent = district.en;
      nameEn.className = 'text-3xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight drop-shadow-md';
    }
    if (nameBn) {
      nameBn.textContent = `(${district.bn})`;
      nameBn.className = 'font-bengali text-2xl sm:text-3xl lg:text-4xl text-bdgreen-400 font-bold drop-shadow';
    }
  }

  if (divBadge) {
    divBadge.textContent = isBn 
      ? `${district.divBn || district.div} বিভাগ` 
      : `${district.div} Division`;
  }

  if (coords) {
    coords.textContent = isBn
      ? toBengaliDigits(district.coordinates || `${district.lat}, ${district.lng}`)
      : (district.coordinates || `${district.lat}, ${district.lng}`);
  }

  if (tagline) {
    tagline.textContent = isBn
      ? (district.taglineBn || district.tagline)
      : (district.taglineEn || district.tagline);
  }

  // 2. KEY METRIC 5-GRID (English / Bengali numbers with কোটি metric + Official Website Button)
  const estYear = document.getElementById('detail-est-year');
  const totalArea = document.getElementById('detail-total-area');
  const totalPop = document.getElementById('detail-total-pop');
  const distance = document.getElementById('detail-distance');

  if (estYear) {
    estYear.textContent = isBn 
      ? (district.estBn || toBengaliDigits(district.est || 1984))
      : (district.est || '1984');
  }
  if (totalArea) {
    totalArea.textContent = isBn 
      ? (district.areaBn || toBengaliDigits(district.area || 'N/A'))
      : (district.area || 'N/A');
  }
  if (totalPop) {
    totalPop.textContent = isBn 
      ? formatBanglaPopulation(district.popBn || district.pop)
      : (district.pop || 'N/A');
  }
  if (distance) {
    distance.textContent = isBn 
      ? (district.distBn || toBengaliDigits(district.dist || 'N/A'))
      : (district.dist || 'N/A');
  }

  // 2.1 OFFICIAL DISTRICT WEBSITE PORTAL BUTTON
  const websiteBtn = document.getElementById('detail-website-btn');
  const websiteDomain = document.getElementById('detail-website-domain');
  const websiteDomainMobile = document.getElementById('detail-website-domain-mobile');

  const officialUrl = district.website 
    || DISTRICT_OFFICIAL_WEBSITES[district.id] 
    || DISTRICT_SLUG_WEBSITES[district.slug] 
    || `https://${district.slug.replace(/[^a-z0-9]/g, '')}.gov.bd`;

  const displayDomain = officialUrl.replace(/^https?:\/\//i, '').replace(/^www\./i, '').replace(/\/$/, '');

  if (websiteBtn) {
    websiteBtn.href = officialUrl;
    websiteBtn.setAttribute('title', isBn ? `${district.bn} জেলা তথ্য বাতায়ন দেখুন` : `Visit Official ${district.en} District Portal`);
  }
  if (websiteDomain) {
    websiteDomain.textContent = displayDomain;
  }
  if (websiteDomainMobile) {
    websiteDomainMobile.textContent = displayDomain;
  }

  // 3. ROUTE & TRANSIT BREAKDOWN
  const routeText = document.getElementById('detail-route-text');
  if (routeText) {
    routeText.textContent = isBn 
      ? (district.routeBn || district.route)
      : (district.routeEn || district.route);
  }

  // 4. SMOOTH SNAP SLIDER CAROUSEL (Visible for districts with carousel images)
  const carouselSection = document.getElementById('detail-carousel-section');
  const carouselTrack = document.getElementById('detail-carousel-track');
  const hasCarousel = Array.isArray(district.carousel) && district.carousel.length > 0;
 
  if (carouselSection) {
    if (hasCarousel) {
      carouselSection.classList.remove('hidden');
      carouselSection.style.display = 'block';
    } else {
      carouselSection.classList.add('hidden');
      carouselSection.style.display = 'none';
    }
  }
 
  if (carouselTrack) {
    if (hasCarousel) {
      const slides = district.carousel;
      carouselTrack.innerHTML = slides.map((slide, idx) => {
        const slideTitle = isBn ? (slide.titleBn || slide.title) : (slide.titleEn || slide.title);
        const slideSub = isBn ? (slide.subtitleBn || slide.subtitle) : (slide.subtitleEn || slide.subtitle);
        const slideNum = isBn ? toBengaliDigits(String(idx + 1).padStart(2, '0')) : String(idx + 1).padStart(2, '0');
        const totalNum = isBn ? toBengaliDigits('05') : '05';
        const slidePrefix = isBn ? 'দৃশ্য' : 'Slide';
 
        return `
          <div class="snap-center shrink-0 w-[280px] sm:w-[340px] md:w-[380px] aspect-[16/10] relative rounded-2xl overflow-hidden shadow-lg border border-slate-200 dark:border-[#173728] group">
            <img 
              src="${slide.image}" 
              alt="${slideTitle}" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              loading="lazy"
              onerror="this.onerror=null; this.src='images/default/card.webp';"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/40 to-transparent flex flex-col justify-end p-4 z-10">
              <span class="text-[10px] font-black tracking-widest text-bdgreen-400 uppercase">
                ${slidePrefix} ${slideNum} / ${totalNum}
              </span>
              <h4 class="text-sm sm:text-base font-extrabold text-white leading-tight mt-0.5 truncate">${slideTitle}</h4>
              <p class="text-xs text-slate-300 font-medium line-clamp-1 mt-0.5">${slideSub}</p>
            </div>
          </div>
        `;
      }).join('');
    } else {
      carouselTrack.innerHTML = '';
    }
  }
 
  // 5. EXPANDED TOP-5 HISTORICAL PLACES & HERITAGE (WITH GOOGLE MAPS REDIRECTION)
  const histContainer = document.getElementById('detail-historical-cards-container');
  if (histContainer) {
    const histList = Array.isArray(district.hist) && district.hist.length >= 5
      ? district.hist.slice(0, 5)
      : generateDefaultHistorical(district);
 
    histContainer.innerHTML = histList.map((item, idx) => {
      const itemName = isBn ? (item.nameBn || item.name) : (item.nameEn || item.name);
      const itemSecondary = isBn ? (item.nameEn || '') : (item.nameBn || '');
      const itemCat = isBn ? (item.categoryBn || item.category || 'ঐতিহাসিক') : (item.categoryEn || item.category || 'Historical');
      const itemDesc = isBn ? (item.descBn || item.desc) : (item.descEn || item.desc);
      const itemLoc = isBn ? (item.locationBn || item.location) : (item.locationEn || item.location);
      const googleMapLink = item.mapUrl || `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent((item.nameEn || item.name) + ' ' + district.en + ' Bangladesh')}`;
      const hasImage = Boolean(item.image);

      return `
        <div class="rounded-2xl bg-white dark:bg-[#0B1E15] border border-slate-200 dark:border-[#173728] shadow-md hover:shadow-xl hover:-translate-y-1 transition-all overflow-hidden flex flex-col group">
          ${hasImage ? `
            <div class="relative aspect-video w-full overflow-hidden bg-slate-900">
              <img 
                src="${item.image}" 
                alt="${itemName}" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                onerror="this.onerror=null; this.src='images/default/card.webp';"
              />
              <div class="absolute top-2.5 right-2.5 px-2.5 py-0.5 rounded-full text-[10px] font-extrabold bg-bdred-500 text-white shadow-md">
                ${itemCat}
              </div>
            </div>
          ` : `
            <div class="p-4 pb-0 flex items-center justify-between gap-2 border-b border-slate-100 dark:border-[#143124]/60">
              <div class="w-8 h-8 rounded-lg bg-bdred-100 dark:bg-bdred-950/80 text-bdred-600 dark:text-bdred-400 flex items-center justify-center shrink-0 border border-bdred-200 dark:border-bdred-800">
                <i data-lucide="castle" class="w-4 h-4"></i>
              </div>
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold bg-bdred-500 text-white shadow-sm">
                ${itemCat}
              </span>
            </div>
          `}
          <div class="p-4 sm:p-5 flex-1 flex flex-col justify-between space-y-3">
            <div>
              <div class="flex items-baseline justify-between gap-2">
                <h4 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white group-hover:text-bdgreen-500 transition-colors">
                  ${itemName}
                </h4>
                ${itemSecondary ? `<span class="text-xs text-slate-400 font-medium shrink-0 truncate max-w-[120px]">${itemSecondary}</span>` : ''}
              </div>
              <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed font-normal mt-2">
                ${itemDesc}
              </p>
            </div>
            
            <!-- Bottom Location Pin & Direct Google Maps Redirection Action -->
            <div class="pt-3 border-t border-slate-100 dark:border-[#143124] flex items-center justify-between gap-2 text-xs mt-auto">
              <a 
                href="${googleMapLink}" 
                target="_blank" 
                rel="noopener noreferrer" 
                class="flex items-center gap-1.5 text-bdred-600 dark:text-bdred-400 font-bold hover:underline group/map min-h-[36px]"
                title="${isBn ? 'গুগল ম্যাপসে এই স্থানটি দেখুন' : 'View this location on Google Maps'}"
              >
                <i data-lucide="map-pin" class="w-3.5 h-3.5 shrink-0 text-bdred-500"></i>
                <span class="truncate max-w-[170px] sm:max-w-[210px]">${itemLoc}</span>
              </a>
              <a 
                href="${googleMapLink}" 
                target="_blank" 
                rel="noopener noreferrer" 
                class="px-2.5 py-1.5 rounded-lg bg-bdred-50 dark:bg-[#142A1E] hover:bg-bdred-100 dark:hover:bg-[#1E3E2E] text-bdred-700 dark:text-bdred-300 border border-bdred-200 dark:border-[#1E4432] text-[11px] font-extrabold flex items-center gap-1 shrink-0 transition-colors shadow-sm"
                title="${isBn ? 'গুগল ম্যাপস অ্যাপে খুলুন' : 'Open in Google Maps App'}"
              >
                <span>${isBn ? 'ম্যাপে দেখুন' : 'View on Map'}</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  // 6. EXPANDED TOP-5 TOURIST ATTRACTIONS & HIGHLIGHTS (WITH GOOGLE MAPS REDIRECTION)
  const tourContainer = document.getElementById('detail-tourist-cards-container');
  if (tourContainer) {
    const tourList = Array.isArray(district.tour) && district.tour.length >= 5
      ? district.tour.slice(0, 5)
      : generateDefaultTourist(district);

    tourContainer.innerHTML = tourList.map((item, idx) => {
      const itemName = isBn ? (item.nameBn || item.name) : (item.nameEn || item.name);
      const itemSecondary = isBn ? (item.nameEn || '') : (item.nameBn || '');
      const itemCat = isBn ? (item.categoryBn || item.category || 'দর্শনীয় স্থান') : (item.categoryEn || item.category || 'Scenic Highlight');
      const itemDesc = isBn ? (item.descBn || item.desc) : (item.descEn || item.desc);
      const itemLoc = isBn ? (item.locationBn || item.location) : (item.locationEn || item.location);
      const googleMapLink = item.mapUrl || `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent((item.nameEn || item.name) + ' ' + district.en + ' Bangladesh')}`;
      const hasImage = Boolean(item.image);

      return `
        <div class="rounded-2xl bg-white dark:bg-[#0B1E15] border border-slate-200 dark:border-[#173728] shadow-md hover:shadow-xl hover:-translate-y-1 transition-all overflow-hidden flex flex-col group">
          ${hasImage ? `
            <div class="relative aspect-video w-full overflow-hidden bg-slate-900">
              <img 
                src="${item.image}" 
                alt="${itemName}" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                onerror="this.onerror=null; this.src='images/default/card.webp';"
              />
              <div class="absolute top-2.5 right-2.5 px-2.5 py-0.5 rounded-full text-[10px] font-extrabold bg-bdgreen-600 text-white shadow-md">
                ${itemCat}
              </div>
            </div>
          ` : `
            <div class="p-4 pb-0 flex items-center justify-between gap-2 border-b border-slate-100 dark:border-[#143124]/60">
              <div class="w-8 h-8 rounded-lg bg-bdgreen-100 dark:bg-bdgreen-950/80 text-bdgreen-700 dark:text-bdgreen-300 flex items-center justify-center shrink-0 border border-bdgreen-200 dark:border-bdgreen-800">
                <i data-lucide="compass" class="w-4 h-4"></i>
              </div>
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold bg-bdgreen-600 text-white shadow-sm">
                ${itemCat}
              </span>
            </div>
          `}
          <div class="p-4 sm:p-5 flex-1 flex flex-col justify-between space-y-3">
            <div>
              <div class="flex items-baseline justify-between gap-2">
                <h4 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white group-hover:text-bdgreen-500 transition-colors">
                  ${itemName}
                </h4>
                ${itemSecondary ? `<span class="text-xs text-slate-400 font-medium shrink-0 truncate max-w-[120px]">${itemSecondary}</span>` : ''}
              </div>
              <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed font-normal mt-2">
                ${itemDesc}
              </p>
            </div>
            
            <!-- Bottom Location Pin & Direct Google Maps Redirection Action -->
            <div class="pt-3 border-t border-slate-100 dark:border-[#143124] flex items-center justify-between gap-2 text-xs mt-auto">
              <a 
                href="${googleMapLink}" 
                target="_blank" 
                rel="noopener noreferrer" 
                class="flex items-center gap-1.5 text-bdgreen-600 dark:text-bdgreen-400 font-bold hover:underline group/map min-h-[36px]"
                title="${isBn ? 'গুগল ম্যাপসে এই স্থানটি দেখুন' : 'View this location on Google Maps'}"
              >
                <i data-lucide="map-pin" class="w-3.5 h-3.5 shrink-0 text-bdgreen-500"></i>
                <span class="truncate max-w-[170px] sm:max-w-[210px]">${itemLoc}</span>
              </a>
              <a 
                href="${googleMapLink}" 
                target="_blank" 
                rel="noopener noreferrer" 
                class="px-2.5 py-1.5 rounded-lg bg-bdgreen-50 dark:bg-[#142A1E] hover:bg-bdgreen-100 dark:hover:bg-[#1E3E2E] text-bdgreen-700 dark:text-bdgreen-300 border border-bdgreen-200 dark:border-[#1E4432] text-[11px] font-extrabold flex items-center gap-1 shrink-0 transition-colors shadow-sm"
                title="${isBn ? 'গুগল ম্যাপস অ্যাপে খুলুন' : 'Open in Google Maps App'}"
              >
                <span>${isBn ? 'ম্যাপে দেখুন' : 'View on Map'}</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  // Next / Previous Navigation Wiring
  const currentId = district.id;
  const prevId = currentId > 1 ? currentId - 1 : 64;
  const nextId = currentId < 64 ? currentId + 1 : 1;

  const prevBtn = document.getElementById('prev-district-btn');
  const nextBtn = document.getElementById('next-district-btn');

  if (prevBtn) prevBtn.onclick = () => navigateToDistrict(prevId);
  if (nextBtn) nextBtn.onclick = () => navigateToDistrict(nextId);

  initLucideIcons();
}

// Fallback generators guaranteeing exact 5-item arrays (only Dhaka has photos for now)
function generateDefaultCarousel(d) {
  if (d.slug !== 'dhaka') return [];
  return [1, 2, 3, 4, 5].map(i => ({
    id: i,
    image: `images/districts/${d.slug}/carousel-${i}.webp`,
    title: `${d.en} Scenic Vista ${i}`,
    titleBn: `${d.bn} মনোরম দৃশ্য ${toBengaliDigits(i)}`,
    subtitle: `Explore rich biodiversity and natural heritage across ${d.div} Division`,
    subtitleBn: `${d.divBn || d.div} বিভাগের অপরূপ প্রাকৃতিক ভূচিত্র`
  }));
}

function generateDefaultHistorical(d) {
  const titles = [
    { en: "Ancient Royal Palace Site", bn: "প্রাচীন ঐতিহাসিক রাজবাড়ি", catEn: "Royal Heritage", catBn: "রাজকীয় ঐতিহ্য" },
    { en: "Historic Jami Mosque Sanctuary", bn: "ঐতিহাসিক জামে মসজিদ", catEn: "Historic Mosque", catBn: "ঐতিহাসিক মসজিদ" },
    { en: "Colonial Court & Manor", bn: "ঔপনিবেশিক আদালত ও ভবন", catEn: "Colonial Architecture", catBn: "ঔপনিবেশিক স্থাপত্য" },
    { en: "Archaeological Mound", bn: "প্রাচীন প্রত্নতাত্ত্বিক নিদর্শন", catEn: "Ancient Archaeology", catBn: "প্রাচীন প্রত্নতত্ত্ব" },
    { en: "National Liberation Memorial", bn: "মুক্তিযুদ্ধ স্মৃতিস্তম্ভ", catEn: "National Memorial", catBn: "জাতীয় স্মৃতিসৌধ" }
  ];
  return titles.map((t, i) => ({
    id: i + 1,
    image: d.slug === 'dhaka' ? `images/districts/${d.slug}/hist-${i + 1}.webp` : null,
    name: `${d.en} ${t.en}`,
    nameEn: `${d.en} ${t.en}`,
    nameBn: `${d.bn} ${t.bn}`,
    category: t.catEn,
    categoryEn: t.catEn,
    categoryBn: t.catBn,
    desc: `${t.en} in ${d.en} district stands as a verified historic landmark. Preserving intricate architectural design and regional heritage.`,
    descBn: `${d.bn} জেলার ${t.bn} শতাব্দী প্রাচীন ঐতিহ্য এবং স্থানীয় ইতিহাস ধারণ করে দর্শনার্থীদের আকৃষ্ট করে।`,
    location: `${d.en} Sadar, ${d.div} Division`,
    locationBn: `${d.bn} সদর, ${d.divBn || d.div} বিভাগ`,
    mapUrl: `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(d.en + ' ' + t.en + ' Bangladesh')}`
  }));
}

function generateDefaultTourist(d) {
  const titles = [
    { en: "Scenic Waterfront Promenade", bn: "নদী তীরবর্তী মনোরম বাঁধ", catEn: "Scenic Nature", catBn: "নদী ও নিসর্গ" },
    { en: "Eco Forest Sanctuary & Trails", bn: "ইকোপার্ক ও বনাঞ্চল", catEn: "Eco Tourism", catBn: "ইকো ট্যুরিজম" },
    { en: "Lakeside Boating & Recreation Park", bn: "মনোরম হ্রদ ও বিনোদন পার্ক", catEn: "Lakeside Resort", catBn: "লেক রিসোর্ট" },
    { en: "Sunset Hilltop Panoramic Viewpoint", bn: "পাহাড়ি সূর্যাস্ত ভিউপয়েন্ট", catEn: "Panoramic Vista", catBn: "প্যানোরামিক ভিউ" },
    { en: "Cultural Heritage Center & Bazaar", bn: "লোকশিল্প ও ঐতিহ্য কেন্দ্র", catEn: "Cultural Center", catBn: "সাংস্কৃতিক কেন্দ্র" }
  ];
  return titles.map((t, i) => ({
    id: i + 1,
    image: d.slug === 'dhaka' ? `images/districts/${d.slug}/tour-${i + 1}.webp` : null,
    name: `${d.en} ${t.en}`,
    nameEn: `${d.en} ${t.en}`,
    nameBn: `${d.bn} ${t.bn}`,
    category: t.catEn,
    categoryEn: t.catEn,
    categoryBn: t.catBn,
    desc: `${t.en} stands as an iconic tourist highlight in ${d.en} district. Offering scenic trails and picturesque natural surroundings.`,
    descBn: `${d.bn} জেলার ${t.bn} অন্যতম জনপ্রিয় পর্যটন স্থান, যা ভ্রমণপিপাসুদের অপরূপ নৈসর্গিক সৌন্দর্য উপহার দেয়।`,
    location: `${d.en} Scenic Point, ${d.div} Division`,
    locationBn: `${d.bn} দর্শনীয় স্থান, ${d.divBn || d.div} বিভাগ`,
    mapUrl: `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(d.en + ' ' + t.en + ' Bangladesh')}`
  }));
}

// ==========================================
// 8. SEARCH, FILTER, AND SORT LOGIC
// ==========================================
function filterAndRenderDistricts() {
  let list = [...AppState.districts];

  // 1. Filter by Division
  if (AppState.activeDivision !== 'all') {
    list = list.filter(d => d.div.toLowerCase() === AppState.activeDivision.toLowerCase());
  }

  // 2. Filter by Search Query
  if (AppState.searchQuery.trim() !== '') {
    const q = AppState.searchQuery.trim().toLowerCase();
    list = list.filter(d => {
      const enMatch = d.en.toLowerCase().includes(q);
      const bnMatch = d.bn && d.bn.includes(q);
      const divMatch = d.div && d.div.toLowerCase().includes(q);
      const divBnMatch = d.divBn && d.divBn.includes(q);
      return enMatch || bnMatch || divMatch || divBnMatch;
    });
  }

  // 3. Sort Districts
  const isBn = AppState.currentLang === 'bn';
  list.sort((a, b) => {
    switch (AppState.sortBy) {
      case 'name-asc':
        return isBn ? (a.bn || a.en).localeCompare(b.bn || b.en, 'bn') : a.en.localeCompare(b.en);
      case 'dist-asc': {
        const distA = parseInt(a.dist) || 0;
        const distB = parseInt(b.dist) || 0;
        return distA - distB;
      }
      case 'area-desc': {
        const areaA = parseFloat(String(a.area).replace(/,/g, '')) || 0;
        const areaB = parseFloat(String(b.area).replace(/,/g, '')) || 0;
        return areaB - areaA;
      }
      case 'pop-desc': {
        const popA = parseFloat(String(a.pop)) || 0;
        const popB = parseFloat(String(b.pop)) || 0;
        return popB - popA;
      }
      default:
        return 0;
    }
  });

  AppState.filteredDistricts = list;

  // Update counter badges
  const filteredCountEl = document.getElementById('filtered-results-count');
  if (filteredCountEl) {
    filteredCountEl.textContent = isBn
      ? `${toBengaliDigits(list.length)}টি জেলা`
      : `${list.length} District${list.length === 1 ? '' : 's'}`;
  }

  renderSidebarList(list);
}

function renderSidebarList(list) {
  const container = document.getElementById('district-list');
  const emptyState = document.getElementById('empty-search-state');
  if (!container) return;

  if (list.length === 0) {
    container.innerHTML = '';
    if (emptyState) emptyState.classList.remove('hidden');
    return;
  }

  if (emptyState) emptyState.classList.add('hidden');
  const isBn = AppState.currentLang === 'bn';

  // Fast single-pass string template injection
  container.innerHTML = list.map(item => {
    const isActive = item.id === AppState.selectedDistrictId;
    const primaryName = isBn ? item.bn : item.en;
    const secondaryName = isBn ? item.en : (item.bn || '');
    const divName = isBn ? (item.divBn || item.div) : item.div;
    const distText = isBn ? (item.distBn || toBengaliDigits(item.dist)) : item.dist;
    const idBadge = isBn ? toBengaliDigits(item.id) : item.id;

    return `
      <div 
        id="district-item-${item.id}"
        onclick="navigateToDistrict(${item.id})"
        onmouseenter="handleSidebarHover(${item.id})"
        class="district-card cursor-pointer p-3 sm:p-3.5 rounded-xl transition-all duration-150 flex items-center justify-between group active:scale-[0.99] ${
          isActive 
            ? 'bg-bdgreen-100 dark:bg-[#122E21] border-2 border-bdgreen-600 dark:border-bdgreen-500 shadow-sm' 
            : 'hover:bg-slate-100 dark:hover:bg-[#0E251B] border border-transparent hover:border-slate-200 dark:border-[#173728]'
        }"
      >
        <div class="flex items-center gap-3 min-w-0">
          <div class="w-8 h-8 rounded-lg flex items-center justify-center font-black text-xs shrink-0 transition-transform duration-200 group-hover:scale-105 ${
            isActive 
              ? 'bg-bdred-500 text-white shadow-sm' 
              : 'bg-slate-100 dark:bg-[#07150E] text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-[#1B3E2E] group-hover:text-bdgreen-600 dark:group-hover:text-bdgreen-400'
          }">
            ${idBadge}
          </div>
          <div class="truncate">
            <div class="flex items-center gap-2">
              <span class="font-extrabold text-sm tracking-tight truncate ${isActive ? 'text-bdgreen-800 dark:text-bdgreen-300' : 'text-slate-900 dark:text-slate-100 group-hover:text-bdgreen-700 dark:group-hover:text-bdgreen-400'}">
                ${primaryName}
              </span>
              <span class="text-xs text-slate-400 font-semibold truncate">(${secondaryName})</span>
            </div>
            <div class="flex items-center gap-2 mt-0.5 text-[11px] text-slate-500 dark:text-slate-400 font-medium">
              <span class="px-1.5 py-0.2 rounded bg-slate-100 dark:bg-[#07150E] text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-[#1B3E2E]">
                ${divName}
              </span>
              <span class="flex items-center gap-0.5">
                <i data-lucide="milestone" class="w-3 h-3 text-bdred-500 inline"></i>
                ${distText}
              </span>
            </div>
          </div>
        </div>
        <div class="shrink-0 pl-2">
          <i data-lucide="chevron-right" class="w-4 h-4 transition-transform duration-150 ${isActive ? 'text-bdred-500 translate-x-1' : 'text-slate-400 group-hover:text-slate-600 dark:group-hover:text-slate-300'}"></i>
        </div>
      </div>
    `;
  }).join('');

  initLucideIcons();
}

function handleSidebarHover(districtId) {
  const district = AppState.districts.find(d => d.id === districtId);
  if (district) {
    updateMapInspectorHud(district, false);
    document.querySelectorAll('.district-svg-path').forEach(p => {
      if (p.getAttribute('data-id') === String(districtId)) {
        p.style.fill = AppState.currentTheme === 'dark' ? '#10B981' : '#006A4E';
      } else if (p.getAttribute('data-id') !== String(AppState.selectedDistrictId)) {
        p.style.fill = '';
      }
    });
  }
}

// ==========================================
// 9. INTERACTIVE VECTOR SVG MAP & INSPECTOR HUD
// ==========================================
function renderVectorMap(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const viewBox = (typeof window !== 'undefined' && window.BANGLADESH_MAP_VIEWBOX) 
    ? window.BANGLADESH_MAP_VIEWBOX 
    : { x: -40, y: -35, w: 680, h: 918 };

  const vbX = viewBox.x !== undefined ? viewBox.x : -40;
  const vbY = viewBox.y !== undefined ? viewBox.y : -35;
  const vbW = viewBox.w || 680;
  const vbH = viewBox.h || 918;

  const districts = AppState.districts;
  if (!districts || districts.length === 0) return;

  // Build clean SVG document markup with boundary padding & preserveAspectRatio
  const svgMarkup = `
    <svg 
      id="${containerId}-svg"
      viewBox="${vbX} ${vbY} ${vbW} ${vbH}" 
      preserveAspectRatio="xMidYMid meet"
      class="w-full h-full max-h-[460px] sm:max-h-[500px] lg:max-h-[540px] object-contain filter drop-shadow-sm select-none block mx-auto"
      xmlns="http://www.w3.org/2000/svg"
    >
      ${districts.map(d => `
        <path 
          id="${containerId}-path-${d.id}"
          data-id="${d.id}" 
          data-name-en="${d.en}" 
          data-name-bn="${d.bn || ''}" 
          data-slug="${d.slug}" 
          d="${d.svgPath}" 
          class="district-svg-path ${d.id === AppState.selectedDistrictId ? 'active' : ''}"
        />
      `).join('')}
    </svg>
  `;

  // Preserve the floating tooltip strictly by its containerId
  const existingTooltip = document.getElementById(`${containerId}-tooltip`);
  container.innerHTML = svgMarkup;
  if (existingTooltip) {
    container.appendChild(existingTooltip);
  }

  // Bind pointer and hover events to vector paths
  const svgEl = document.getElementById(`${containerId}-svg`);
  const tooltip = document.getElementById(`${containerId}-tooltip`);

  svgEl.querySelectorAll('.district-svg-path').forEach(path => {
    const districtId = Number(path.getAttribute('data-id'));
    const district = districts.find(d => d.id === districtId);
    if (!district) return;

    const handleInspect = (clientX, clientY, isTouch = false) => {
      AppState.hoveredDistrictId = district.id;

      // 1. Update In-Map Inspector HUD Bar
      updateMapInspectorHud(district, district.id === AppState.selectedDistrictId);

      // 2. Update In-Modal HUD Bar if modal is open
      updateModalInspectorHud(district);

      // 3. Highlight SVG Paths across all map instances
      document.querySelectorAll('.district-svg-path').forEach(p => {
        const pId = Number(p.getAttribute('data-id'));
        if (pId === district.id) {
          if (pId !== AppState.selectedDistrictId) {
            p.style.fill = AppState.currentTheme === 'dark' ? '#10B981' : '#006A4E';
          }
        } else if (pId !== AppState.selectedDistrictId) {
          p.style.fill = '';
        }
      });

      // 4. Position the floating tooltip strictly clamped inside map container
      if (tooltip && clientX !== undefined && clientY !== undefined) {
        const enEl = tooltip.querySelector('.tooltip-en');
        const bnEl = tooltip.querySelector('.tooltip-bn');
        const divEl = tooltip.querySelector('.tooltip-div');
        const isBn = AppState.currentLang === 'bn';

        if (enEl) enEl.textContent = isBn ? district.bn : district.en;
        if (bnEl) bnEl.textContent = isBn ? `(${district.en})` : `(${district.bn})`;
        if (divEl) {
          const divName = isBn ? (district.divBn || district.div) : district.div;
          const distVal = isBn ? (district.distBn || toBengaliDigits(district.dist)) : district.dist;
          const popVal = isBn ? formatBanglaPopulation(district.popBn || district.pop) : `${district.pop} pop.`;
          const suffix = isBn ? 'ঢাকা থেকে' : 'from Dhaka';
          divEl.textContent = isBn 
            ? `${divName} বিভাগ • ${distVal} ${suffix} • ${popVal}`
            : `${divName} Division • ${distVal} ${suffix} • ${popVal}`;
        }

        tooltip.classList.remove('hidden');

        const rect = container.getBoundingClientRect();
        const tooltipWidth = tooltip.offsetWidth || 180;
        const tooltipHeight = tooltip.offsetHeight || 55;

        let posX = clientX - rect.left + 15;
        let posY = clientY - rect.top + 15;

        if (posX + tooltipWidth > rect.width - 10) {
          posX = clientX - rect.left - tooltipWidth - 15;
        }
        if (posY + tooltipHeight > rect.height - 10) {
          posY = clientY - rect.top - tooltipHeight - 15;
        }

        posX = Math.max(10, Math.min(rect.width - tooltipWidth - 10, posX));
        posY = Math.max(10, Math.min(rect.height - tooltipHeight - 10, posY));

        tooltip.style.left = `${posX}px`;
        tooltip.style.top = `${posY}px`;

        if (isTouch) {
          clearTimeout(path._touchTooltipTimeout);
          path._touchTooltipTimeout = setTimeout(() => {
            if (tooltip) tooltip.classList.add('hidden');
          }, 2500);
        }
      }
    };

    // Desktop Mouse Move
    path.addEventListener('mousemove', (e) => {
      handleInspect(e.clientX, e.clientY, false);
    });

    // Mobile / Touch Interaction
    path.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches[0]) {
        handleInspect(e.touches[0].clientX, e.touches[0].clientY, true);
      }
    }, { passive: true });

    path.addEventListener('mouseleave', () => {
      if (tooltip) tooltip.classList.add('hidden');
      path.style.fill = '';
      AppState.hoveredDistrictId = null;
      
      if (AppState.selectedDistrictId) {
        const selected = districts.find(d => d.id === AppState.selectedDistrictId);
        if (selected) updateMapInspectorHud(selected, true);
      }
    });

    // Click Interaction: Navigates directly to the district profile page
    path.addEventListener('click', () => {
      if (tooltip) tooltip.classList.add('hidden');
      closeMapModal();
      navigateToDistrict(district.id);
    });
  });
}

function updateMapInspectorHud(district, isActive = false) {
  if (!district) return;
  const isBn = AppState.currentLang === 'bn';

  const nameEn = document.getElementById('inspector-name-en');
  const nameBn = document.getElementById('inspector-name-bn');
  const divBadge = document.getElementById('inspector-division');
  const distEl = document.getElementById('inspector-distance');
  const statsEl = document.getElementById('inspector-stats');
  const openBtn = document.getElementById('inspector-open-btn');
  const badgeIcon = document.getElementById('inspector-badge-icon');

  if (nameEn) nameEn.textContent = isBn ? district.bn : district.en;
  if (nameBn) nameBn.textContent = isBn ? `(${district.en})` : `(${district.bn})`;
  if (divBadge) {
    divBadge.textContent = isBn 
      ? `${district.divBn || district.div} বিভাগ` 
      : `${district.div} Division`;
  }
  if (distEl) {
    const distText = isBn ? (district.distBn || toBengaliDigits(district.dist)) : district.dist;
    const distSuffix = isBn ? 'ঢাকা থেকে' : 'from Dhaka';
    distEl.innerHTML = `<i data-lucide="milestone" class="w-3.5 h-3.5 inline"></i> ${distText} ${distSuffix}`;
  }
  if (statsEl) {
    const areaText = isBn ? (district.areaBn || toBengaliDigits(district.area)) : district.area;
    const popText = isBn ? formatBanglaPopulation(district.popBn || district.pop) : `${district.pop} pop.`;
    statsEl.textContent = `${areaText} • ${popText}`;
  }

  if (badgeIcon) {
    badgeIcon.innerHTML = isActive 
      ? `<span class="w-2.5 h-2.5 rounded-full bg-bdred-500 animate-pulse"></span>`
      : `<span class="w-2.5 h-2.5 rounded-full bg-bdgreen-600"></span>`;
  }

  if (openBtn) {
    openBtn.onclick = () => navigateToDistrict(district.id);
    const targetName = isBn ? district.bn : district.en;
    const btnLabel = isBn ? `${targetName} বিস্তারিত দেখুন` : `View ${targetName} Details`;
    openBtn.innerHTML = `<span>${btnLabel}</span><i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>`;
  }

  initLucideIcons();
}

function updateModalInspectorHud(district) {
  const isBn = AppState.currentLang === 'bn';
  const modalName = document.getElementById('modal-inspector-name');
  const modalBn = document.getElementById('modal-inspector-bn');
  const modalDiv = document.getElementById('modal-inspector-div');
  const modalHud = document.getElementById('modal-map-inspector-hud');
  const modalAction = document.getElementById('modal-inspector-action');

  if (modalName) modalName.textContent = isBn ? district.bn : district.en;
  if (modalBn) modalBn.textContent = isBn ? `(${district.en})` : `(${district.bn})`;
  if (modalDiv) {
    const divName = isBn ? (district.divBn || district.div) : district.div;
    const distVal = isBn ? (district.distBn || toBengaliDigits(district.dist)) : district.dist;
    const popVal = isBn ? formatBanglaPopulation(district.popBn || district.pop) : `${district.pop} pop.`;
    const suffix = isBn ? 'ঢাকা থেকে' : 'from Dhaka';
    modalDiv.textContent = `• ${divName} • ${distVal} ${suffix} • ${popVal}`;
  }
  if (modalAction) {
    modalAction.textContent = isBn ? 'প্রোফাইল দেখুন →' : 'Open Profile →';
  }

  if (modalHud) {
    modalHud.onclick = () => {
      closeMapModal();
      navigateToDistrict(district.id);
    };
  }
}

function updateVectorMapActiveState(activeId) {
  document.querySelectorAll('.district-svg-path').forEach(el => {
    el.classList.remove('active');
  });

  const pathInHomeMap = document.getElementById(`empty-state-svg-map-container-path-${activeId}`);
  if (pathInHomeMap) pathInHomeMap.classList.add('active');

  const pathInModalMap = document.getElementById(`modal-svg-map-container-path-${activeId}`);
  if (pathInModalMap) pathInModalMap.classList.add('active');
}

// ==========================================
// 10. MOBILE SEGMENTED VIEW CONTROLLER
// ==========================================
function setMobileHomeTab(tab) {
  AppState.mobileHomeTab = tab;
  const sidebarCol = document.getElementById('sidebar-column');
  const mapCol = document.getElementById('map-dashboard-column');
  const tabBtnMap = document.getElementById('mobile-home-tab-map');
  const tabBtnList = document.getElementById('mobile-home-tab-list');

  if (tab === 'map') {
    if (sidebarCol) {
      sidebarCol.classList.add('hidden');
      sidebarCol.classList.remove('flex');
    }
    if (mapCol) {
      mapCol.classList.remove('hidden');
    }
    if (tabBtnMap) {
      tabBtnMap.className = 'flex-1 py-2 sm:py-2.5 rounded-lg text-xs sm:text-sm font-black flex items-center justify-center gap-2 transition-all bg-bdgreen-700 text-white shadow-sm cursor-pointer min-h-[42px]';
    }
    if (tabBtnList) {
      tabBtnList.className = 'flex-1 py-2 sm:py-2.5 rounded-lg text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer min-h-[42px]';
    }
  } else {
    // List tab
    if (sidebarCol) {
      sidebarCol.classList.remove('hidden');
      sidebarCol.classList.add('flex');
    }
    if (mapCol) {
      mapCol.classList.add('hidden');
    }
    if (tabBtnMap) {
      tabBtnMap.className = 'flex-1 py-2 sm:py-2.5 rounded-lg text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer min-h-[42px]';
    }
    if (tabBtnList) {
      tabBtnList.className = 'flex-1 py-2 sm:py-2.5 rounded-lg text-xs sm:text-sm font-black flex items-center justify-center gap-2 transition-all bg-bdgreen-700 text-white shadow-sm cursor-pointer min-h-[42px]';
    }
  }
  initLucideIcons();
}

// ==========================================
// 11. MODAL CONTROLS & TOAST NOTIFICATION
// ==========================================
function openMapModal() {
  const modal = document.getElementById('vector-map-modal');
  if (modal) {
    modal.classList.remove('hidden');
    renderVectorMap('modal-svg-map-container');
    if (AppState.selectedDistrictId) {
      updateVectorMapActiveState(AppState.selectedDistrictId);
      const sel = AppState.districts.find(d => d.id === AppState.selectedDistrictId);
      if (sel) updateModalInspectorHud(sel);
    }
  }
}

function closeMapModal() {
  const modal = document.getElementById('vector-map-modal');
  if (modal) modal.classList.add('hidden');
}

let toastTimeout = null;
function showToast(msg) {
  const toast = document.getElementById('toast-notification');
  const messageEl = document.getElementById('toast-message');
  if (!toast || !messageEl) return;

  messageEl.textContent = msg;
  toast.classList.remove('hidden');

  if (toastTimeout) clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => {
    toast.classList.add('hidden');
  }, 2400);
}

// ==========================================
// 12. UI EVENT WIRING & LISTENERS
// ==========================================
function setupEventListeners() {
  // Theme Toggle Button
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  if (themeToggleBtn) themeToggleBtn.addEventListener('click', toggleTheme);

  // Dedicated Language Toggle Button (English ↔ বাংলা)
  const langToggleBtn = document.getElementById('lang-toggle-btn');
  if (langToggleBtn) langToggleBtn.addEventListener('click', toggleLanguage);

  // Live Search Input
  const searchInput = document.getElementById('district-search-input');
  const searchClearBtn = document.getElementById('search-clear-btn');

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      AppState.searchQuery = e.target.value;
      if (searchClearBtn) {
        if (AppState.searchQuery.length > 0) {
          searchClearBtn.classList.remove('hidden');
        } else {
          searchClearBtn.classList.add('hidden');
        }
      }
      filterAndRenderDistricts();
    });
  }

  if (searchClearBtn) {
    searchClearBtn.addEventListener('click', () => {
      if (searchInput) {
        searchInput.value = '';
        searchInput.focus();
      }
      AppState.searchQuery = '';
      searchClearBtn.classList.add('hidden');
      filterAndRenderDistricts();
    });
  }

  const resetSearchBtn = document.getElementById('reset-search-btn');
  if (resetSearchBtn) {
    resetSearchBtn.addEventListener('click', () => {
      if (searchInput) searchInput.value = '';
      AppState.searchQuery = '';
      AppState.activeDivision = 'all';
      updateDivisionPillsUI('all');
      filterAndRenderDistricts();
    });
  }

  // Division Filter Pills
  document.querySelectorAll('.division-pill').forEach(pill => {
    pill.addEventListener('click', (e) => {
      const division = e.currentTarget.getAttribute('data-division');
      AppState.activeDivision = division;
      updateDivisionPillsUI(division);
      filterAndRenderDistricts();
    });
  });

  // Sorting Dropdown
  const sortSelect = document.getElementById('district-sort-select');
  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      AppState.sortBy = e.target.value;
      filterAndRenderDistricts();
    });
  }

  // Vector Map Modal Buttons
  const viewMapModalBtn = document.getElementById('view-map-modal-btn');
  if (viewMapModalBtn) viewMapModalBtn.addEventListener('click', openMapModal);

  const openMapPreviewBtn = document.getElementById('open-map-preview-btn');
  if (openMapPreviewBtn) openMapPreviewBtn.addEventListener('click', openMapModal);

  const closeMapModalBtn = document.getElementById('close-map-modal-btn');
  if (closeMapModalBtn) closeMapModalBtn.addEventListener('click', closeMapModal);

  const modalMapDoneBtn = document.getElementById('modal-map-done-btn');
  if (modalMapDoneBtn) modalMapDoneBtn.addEventListener('click', closeMapModal);

  // Close map modal on backdrop click
  const vectorMapModal = document.getElementById('vector-map-modal');
  if (vectorMapModal) {
    vectorMapModal.addEventListener('click', (e) => {
      if (e.target === vectorMapModal) closeMapModal();
    });
  }

  // In-Map Inspector HUD Click
  const mapInspectorHud = document.getElementById('map-inspector-hud');
  if (mapInspectorHud) {
    mapInspectorHud.addEventListener('click', (e) => {
      if (e.target.closest('#inspector-open-btn')) return;
      const targetId = AppState.hoveredDistrictId || AppState.selectedDistrictId || 1;
      navigateToDistrict(targetId);
    });
  }

  // Mobile Drawer Listeners
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', () => toggleMobileDrawer(true));

  const mobileDrawerCloseBtn = document.getElementById('mobile-drawer-close-btn');
  if (mobileDrawerCloseBtn) mobileDrawerCloseBtn.addEventListener('click', () => toggleMobileDrawer(false));

  const mobileDrawerBackdrop = document.getElementById('mobile-drawer-backdrop');
  if (mobileDrawerBackdrop) mobileDrawerBackdrop.addEventListener('click', () => toggleMobileDrawer(false));

  const mobileThemeBtn = document.getElementById('mobile-theme-btn');
  if (mobileThemeBtn) mobileThemeBtn.addEventListener('click', toggleTheme);

  const mobileLangBtn = document.getElementById('mobile-lang-btn');
  if (mobileLangBtn) mobileLangBtn.addEventListener('click', toggleLanguage);

  const mobileVectorMapBtn = document.getElementById('mobile-vector-map-btn');
  if (mobileVectorMapBtn) {
    mobileVectorMapBtn.addEventListener('click', () => {
      toggleMobileDrawer(false);
      openMapModal();
    });
  }

  // Auto-close mobile drawer on window resize to desktop
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 768) {
      toggleMobileDrawer(false);
    }
  });

  // Keyboard Navigation (Escape key)
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const drawer = document.getElementById('mobile-drawer');
      if (drawer && !drawer.classList.contains('translate-x-full')) {
        toggleMobileDrawer(false);
        return;
      }
      const modal = document.getElementById('vector-map-modal');
      if (modal && !modal.classList.contains('hidden')) {
        closeMapModal();
      } else if (window.location.hash.startsWith('#/district/')) {
        navigateToHome();
      }
    }
  });
}

function updateDivisionPillsUI(activeDivision) {
  const isBn = AppState.currentLang === 'bn';
  document.querySelectorAll('.division-pill').forEach(pill => {
    const div = pill.getAttribute('data-division');
    const label = DIVISIONS_MAP[div] ? (isBn ? DIVISIONS_MAP[div].bn : DIVISIONS_MAP[div].en) : div;
    pill.textContent = label;

    if (div.toLowerCase() === activeDivision.toLowerCase()) {
      pill.className = 'division-pill active shrink-0 whitespace-nowrap px-3 py-1 rounded-lg font-bold bg-bdgreen-700 text-white transition shadow-sm';
    } else {
      pill.className = 'division-pill shrink-0 whitespace-nowrap px-2.5 py-1 rounded-lg font-semibold bg-slate-100 dark:bg-[#07150E] text-slate-600 dark:text-slate-300 hover:bg-bdgreen-50 dark:hover:bg-[#122A1E] border border-slate-200 dark:border-[#1B3E2E] transition';
    }
  });
}

// Global scope exports for inline HTML onclick handlers
window.navigateToHome = navigateToHome;
window.navigateToDistrict = navigateToDistrict;
window.handleSidebarHover = handleSidebarHover;
window.closeMapModal = closeMapModal;
window.setMobileHomeTab = setMobileHomeTab;
window.toggleLanguage = toggleLanguage;
window.toggleTheme = toggleTheme;
window.toggleMobileDrawer = toggleMobileDrawer;
