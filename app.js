/**
 * Local Host — 100% Self-Hosted, Local-First Application Architecture
 * Zero External Dependencies • Pure In-Memory Buffers
 * 
 * Features:
 * - Direct execution out of `window.LOCAL_DISTRICTS` & `window.MAP_PATHS`
 * - Full-width Cinematic District Hero Banner with dark gradient fade
 * - Pure CSS Scroll-Snapping 5-Image Carousel Track
 * - Enforced Top-5 Historical & Tourist Location Cards with image frames & map pins
 * - Sticky desktop dual-column grid (left sidebar sticky, right map locked)
 * - Mobile Segmented View Controller ([ Interactive Map View ] vs [ 64 Districts List ])
 * - SVG vector map hover/touch inspection with strictly bounded tooltip
 * - Interactive Dark ↔ Light mode engine with localStorage persistence
 */

// ==========================================
// 1. REACTIVE STATE MANAGEMENT
// ==========================================
const AppState = {
  districts: [],             // All 64 district memory buffers
  filteredDistricts: [],     // Filtered and sorted district list
  selectedDistrictId: null,  // Active selected district ID
  hoveredDistrictId: null,   // Currently hovered / touched district ID
  activeDivision: 'all',     // Selected division filter
  searchQuery: '',           // Current search filter query
  sortBy: 'name-asc',        // Sort criteria: name-asc, dist-asc, area-desc, pop-desc
  currentTheme: 'dark',      // 'dark' | 'light'
  mobileHomeTab: 'map',      // 'map' | 'list' (on compact mobile screens)
};

const THEME_KEY = 'localhost_district_theme_v2';

// ==========================================
// 2. LIFECYCLE & INITIALIZATION
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
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
  AppState.currentTheme = savedTheme ? savedTheme : 'dark';
  applyTheme(AppState.currentTheme);
}

function applyTheme(theme) {
  const html = document.documentElement;
  const sunIcon = document.getElementById('theme-icon-sun');
  const moonIcon = document.getElementById('theme-icon-moon');
  const themeLabel = document.getElementById('theme-toggle-label');

  if (theme === 'dark') {
    html.classList.add('dark');
    if (sunIcon) sunIcon.classList.remove('hidden');
    if (moonIcon) moonIcon.classList.add('hidden');
    if (themeLabel) themeLabel.textContent = 'Dark';
  } else {
    html.classList.remove('dark');
    if (sunIcon) sunIcon.classList.add('hidden');
    if (moonIcon) moonIcon.classList.remove('hidden');
    if (themeLabel) themeLabel.textContent = 'Light';
  }
  AppState.currentTheme = theme;
  localStorage.setItem(THEME_KEY, theme);
  initLucideIcons();
}

function toggleTheme() {
  const nextTheme = AppState.currentTheme === 'dark' ? 'light' : 'dark';
  applyTheme(nextTheme);
  showToast(`Switched to ${nextTheme === 'dark' ? 'Dark' : 'Light'} Mode`);
}

// ==========================================
// 4. LOCAL MEMORY BUFFER DATA LOADER
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
    return {
      ...d,
      svgPath: d.svgPath || mapPaths[d.id] || mapPaths[d.slug] || ''
    };
  });

  // Update status indicators in navigation bar
  const statusBeacon = document.getElementById('api-beacon');
  const statusText = document.getElementById('api-status-text');
  const countBadge = document.getElementById('api-district-count');

  if (statusBeacon) {
    statusBeacon.className = 'w-2.5 h-2.5 rounded-full bg-bdgreen-500 beacon-pulse shrink-0';
  }
  if (statusText) {
    statusText.textContent = 'Offline Memory Ready';
  }
  if (countBadge) {
    countBadge.textContent = `${AppState.districts.length} Districts Loaded`;
  }

  // Initial render of sidebar and vector map
  filterAndRenderDistricts();
  renderVectorMap('empty-state-svg-map-container');
  renderVectorMap('modal-svg-map-container');

  // Initialize In-Map HUD with first district (Dhaka)
  if (AppState.districts.length > 0) {
    updateMapInspectorHud(AppState.districts[0], false);
  }
}

// ==========================================
// 5. URL HASH ROUTING & PAGE CONTROLLER
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
// 6. POPULATE DISTRICT DETAIL PAGE (CINEMATIC)
// ==========================================
function populateDistrictDetails(district) {
  // Top breadcrumb tracker
  const breadcrumbDiv = document.getElementById('breadcrumb-division');
  const breadcrumbDst = document.getElementById('breadcrumb-district');
  if (breadcrumbDiv) breadcrumbDiv.textContent = `${district.div} Division`;
  if (breadcrumbDst) breadcrumbDst.textContent = `${district.en} (${district.bn})`;

  // 1. CINEMATIC HERO BANNER
  const heroImg = document.getElementById('detail-hero-image');
  const nameEn = document.getElementById('detail-name-en');
  const nameBn = document.getElementById('detail-name-bn');
  const divBadge = document.getElementById('detail-division-badge');
  const coords = document.getElementById('detail-coordinates');
  const tagline = document.getElementById('detail-tagline');

  if (heroImg) {
    heroImg.src = district.heroImage || `images/districts/${district.slug}/hero.webp`;
    heroImg.onerror = function() {
      this.onerror = null;
      this.src = 'images/default/hero.webp';
    };
  }
  if (nameEn) nameEn.textContent = district.en;
  if (nameBn) nameBn.textContent = district.bn;
  if (divBadge) divBadge.textContent = `${district.div} Division`;
  if (coords) coords.textContent = district.coordinates || `${district.lat}, ${district.lng}`;
  if (tagline) {
    tagline.textContent = district.tagline || 
      `${district.en} (${district.bn}) is a picturesque and historically significant administrative district located under ${district.div} Division, Bangladesh.`;
  }

  // 2. KEY METRIC 4-GRID
  const estYear = document.getElementById('detail-est-year');
  const totalArea = document.getElementById('detail-total-area');
  const totalPop = document.getElementById('detail-total-pop');
  const distance = document.getElementById('detail-distance');

  if (estYear) estYear.textContent = district.est || '1984';
  if (totalArea) totalArea.textContent = district.area || 'N/A';
  if (totalPop) totalPop.textContent = district.pop || 'N/A';
  if (distance) distance.textContent = district.dist || 'N/A';

  // 3. ROUTE & TRANSIT BREAKDOWN
  const routeText = document.getElementById('detail-route-text');
  if (routeText) {
    routeText.textContent = district.route || 
      `Direct express highway connections and regional transit links connect ${district.en} with Dhaka and surrounding administrative districts.`;
  }

  // 4. SMOOTH SNAP SLIDER CAROUSEL (5-IMAGE PURE CSS SCROLL-SNAP)
  const carouselTrack = document.getElementById('detail-carousel-track');
  if (carouselTrack) {
    const slides = Array.isArray(district.carousel) && district.carousel.length > 0
      ? district.carousel
      : generateDefaultCarousel(district);

    carouselTrack.innerHTML = slides.map((slide, idx) => `
      <div class="snap-center shrink-0 w-[280px] sm:w-[340px] md:w-[380px] aspect-[16/10] relative rounded-2xl overflow-hidden shadow-lg border border-slate-200 dark:border-[#173728] group">
        <img 
          src="${slide.image}" 
          alt="${slide.title}" 
          class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          loading="lazy"
          onerror="this.onerror=null; this.src='images/default/card.webp';"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/40 to-transparent flex flex-col justify-end p-4 z-10">
          <span class="text-[10px] font-black tracking-widest text-bdgreen-400 uppercase">Slide 0${idx + 1} / 05</span>
          <h4 class="text-sm sm:text-base font-extrabold text-white leading-tight mt-0.5 truncate">${slide.title}</h4>
          <p class="text-xs text-slate-300 font-medium line-clamp-1 mt-0.5">${slide.subtitle}</p>
        </div>
      </div>
    `).join('');
  }

  // 5. EXPANDED TOP-5 HISTORICAL PLACES & HERITAGE (ENFORCED MINIMUM 5 CARDS)
  const histContainer = document.getElementById('detail-historical-cards-container');
  if (histContainer) {
    const histList = Array.isArray(district.hist) && district.hist.length >= 5
      ? district.hist.slice(0, 5)
      : generateDefaultHistorical(district);

    histContainer.innerHTML = histList.map((item, idx) => `
      <div class="rounded-2xl bg-white dark:bg-[#0B1E15] border border-slate-200 dark:border-[#173728] shadow-md hover:shadow-xl hover:-translate-y-1 transition-all overflow-hidden flex flex-col group">
        <div class="relative aspect-video w-full overflow-hidden bg-slate-900">
          <img 
            src="${item.image || `images/districts/${district.slug}/hist-${idx + 1}.webp`}" 
            alt="${item.name}" 
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            loading="lazy"
            onerror="this.onerror=null; this.src='images/default/card.webp';"
          />
          <div class="absolute top-2.5 right-2.5 px-2.5 py-0.5 rounded-full text-[10px] font-extrabold bg-bdred-500 text-white shadow-md">
            ${item.category || 'Historical'}
          </div>
        </div>
        <div class="p-4 sm:p-5 flex-1 flex flex-col justify-between space-y-3">
          <div>
            <div class="flex items-baseline justify-between gap-2">
              <h4 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white group-hover:text-bdgreen-500 transition-colors">
                ${item.name}
              </h4>
              ${item.nameBn ? `<span class="font-bengali text-xs font-semibold text-bdgreen-600 dark:text-bdgreen-400 shrink-0">${item.nameBn}</span>` : ''}
            </div>
            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed font-normal mt-2">
              ${item.desc}
            </p>
          </div>
          <div class="pt-3 border-t border-slate-100 dark:border-[#143124] flex items-center gap-1.5 text-xs text-bdred-600 dark:text-bdred-400 font-bold mt-auto">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 shrink-0"></i>
            <span class="truncate">${item.location || `${district.en} Sadar, ${district.div}`}</span>
          </div>
        </div>
      </div>
    `).join('');
  }

  // 6. EXPANDED TOP-5 TOURIST ATTRACTIONS & HIGHLIGHTS (ENFORCED MINIMUM 5 CARDS)
  const tourContainer = document.getElementById('detail-tourist-cards-container');
  if (tourContainer) {
    const tourList = Array.isArray(district.tour) && district.tour.length >= 5
      ? district.tour.slice(0, 5)
      : generateDefaultTourist(district);

    tourContainer.innerHTML = tourList.map((item, idx) => `
      <div class="rounded-2xl bg-white dark:bg-[#0B1E15] border border-slate-200 dark:border-[#173728] shadow-md hover:shadow-xl hover:-translate-y-1 transition-all overflow-hidden flex flex-col group">
        <div class="relative aspect-video w-full overflow-hidden bg-slate-900">
          <img 
            src="${item.image || `images/districts/${district.slug}/tour-${idx + 1}.webp`}" 
            alt="${item.name}" 
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            loading="lazy"
            onerror="this.onerror=null; this.src='images/default/card.webp';"
          />
          <div class="absolute top-2.5 right-2.5 px-2.5 py-0.5 rounded-full text-[10px] font-extrabold bg-bdgreen-600 text-white shadow-md">
            ${item.category || 'Scenic Highlight'}
          </div>
        </div>
        <div class="p-4 sm:p-5 flex-1 flex flex-col justify-between space-y-3">
          <div>
            <div class="flex items-baseline justify-between gap-2">
              <h4 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white group-hover:text-bdgreen-500 transition-colors">
                ${item.name}
              </h4>
              ${item.nameBn ? `<span class="font-bengali text-xs font-semibold text-bdgreen-600 dark:text-bdgreen-400 shrink-0">${item.nameBn}</span>` : ''}
            </div>
            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed font-normal mt-2">
              ${item.desc}
            </p>
          </div>
          <div class="pt-3 border-t border-slate-100 dark:border-[#143124] flex items-center gap-1.5 text-xs text-bdgreen-600 dark:text-bdgreen-400 font-bold mt-auto">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 shrink-0"></i>
            <span class="truncate">${item.location || `${district.en} Scenic Zone, ${district.div}`}</span>
          </div>
        </div>
      </div>
    `).join('');
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

// Fallback generators guaranteeing exact 5-item arrays
function generateDefaultCarousel(d) {
  return [1, 2, 3, 4, 5].map(i => ({
    id: i,
    image: `images/districts/${d.slug}/carousel-${i}.webp`,
    title: `${d.en} Scenic Vista ${i}`,
    subtitle: `Explore rich biodiversity and natural heritage across ${d.div} Division`
  }));
}

function generateDefaultHistorical(d) {
  const titles = [
    "Ancient Architectural Citadel",
    "Historic Jami Mosque Sanctuary",
    "Colonial Heritage Manor & Mint",
    "Centuries-Old Archaeological Mound",
    "National Liberation Memorial"
  ];
  return titles.map((title, i) => ({
    id: i + 1,
    image: `images/districts/${d.slug}/hist-${i + 1}.webp`,
    name: `${d.en} ${title}`,
    nameBn: `${d.bn} ঐতিহাসিক প্রত্নতত্ত্ব`,
    category: "Heritage Monument",
    desc: `${title} in ${d.en} district stands as a verified historic landmark. Preserving intricate architectural design, historical archives, and cultural memory dating back through antiquity.`,
    location: `${d.en} Sadar, ${d.div} Division`
  }));
}

function generateDefaultTourist(d) {
  const titles = [
    "Scenic Waterfront Promenade",
    "Eco Forest Sanctuary & Trails",
    "Lakeside Boating & Recreation Park",
    "Sunset Hilltop Panoramic Viewpoint",
    "Cultural Heritage Center & Bazaar"
  ];
  return titles.map((title, i) => ({
    id: i + 1,
    image: `images/districts/${d.slug}/tour-${i + 1}.webp`,
    name: `${d.en} ${title}`,
    nameBn: `${d.bn} দর্শনীয় স্থান`,
    category: "Scenic Nature",
    desc: `A celebrated tourism destination in ${d.en} district. The site offers travelers scenic panoramas, peaceful eco-tourism trails, and memorable recreation surrounded by nature.`,
    location: `${d.en} Riverfront, ${d.div} Division`
  }));
}

// ==========================================
// 7. SEARCH, FILTER, AND SORT LOGIC
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
      return enMatch || bnMatch || divMatch;
    });
  }

  // 3. Sort Districts
  list.sort((a, b) => {
    switch (AppState.sortBy) {
      case 'name-asc':
        return a.en.localeCompare(b.en);
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
    filteredCountEl.textContent = `${list.length} District${list.length === 1 ? '' : 's'}`;
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

  // Fast single-pass string template injection
  container.innerHTML = list.map(item => {
    const isActive = item.id === AppState.selectedDistrictId;
    return `
      <div 
        id="district-item-${item.id}"
        onclick="navigateToDistrict(${item.id})"
        onmouseenter="handleSidebarHover(${item.id})"
        class="district-card cursor-pointer p-3 sm:p-3.5 rounded-xl transition-all duration-150 flex items-center justify-between group active:scale-[0.99] ${
          isActive 
            ? 'bg-bdgreen-100 dark:bg-[#122E21] border-2 border-bdgreen-600 dark:border-bdgreen-500 shadow-sm' 
            : 'hover:bg-slate-100 dark:hover:bg-[#0E251B] border border-transparent hover:border-slate-200 dark:hover:border-[#173728]'
        }"
      >
        <div class="flex items-center gap-3 min-w-0">
          <div class="w-8 h-8 rounded-lg flex items-center justify-center font-black text-xs shrink-0 transition-transform duration-200 group-hover:scale-105 ${
            isActive 
              ? 'bg-bdred-500 text-white shadow-sm' 
              : 'bg-slate-100 dark:bg-[#07150E] text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-[#1B3E2E] group-hover:text-bdgreen-600 dark:group-hover:text-bdgreen-400'
          }">
            ${item.id}
          </div>
          <div class="truncate">
            <div class="flex items-center gap-2">
              <span class="font-extrabold text-sm tracking-tight truncate ${isActive ? 'text-bdgreen-800 dark:text-bdgreen-300' : 'text-slate-900 dark:text-slate-100 group-hover:text-bdgreen-700 dark:group-hover:text-bdgreen-400'}">
                ${item.en}
              </span>
              <span class="font-bengali text-xs text-slate-500 dark:text-slate-400 font-semibold">${item.bn || ''}</span>
            </div>
            <div class="flex items-center gap-2 mt-0.5 text-[11px] text-slate-500 dark:text-slate-400 font-medium">
              <span class="px-1.5 py-0.2 rounded bg-slate-100 dark:bg-[#07150E] text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-[#1B3E2E]">
                ${item.div}
              </span>
              <span class="flex items-center gap-0.5">
                <i data-lucide="milestone" class="w-3 h-3 text-bdred-500 inline"></i>
                ${item.dist}
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
// 8. INTERACTIVE VECTOR SVG MAP & INSPECTOR HUD
// ==========================================
function renderVectorMap(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const viewBox = (typeof window !== 'undefined' && window.BANGLADESH_MAP_VIEWBOX) 
    ? window.BANGLADESH_MAP_VIEWBOX 
    : { w: 600, h: 848 };

  const districts = AppState.districts;
  if (!districts || districts.length === 0) return;

  const { w, h } = viewBox;

  const svgPathsHtml = districts.map(d => {
    return `<path 
      id="${containerId}-path-${d.id}"
      d="${d.svgPath || ''}"
      class="district-svg-path"
      data-id="${d.id}"
      data-en="${d.en}"
      data-bn="${d.bn}"
      data-div="${d.div}"
      data-dist="${d.dist}"
    ></path>`;
  }).join('');

  container.innerHTML = `
    <svg 
      viewBox="0 0 ${w} ${h}" 
      class="w-full h-auto max-h-[380px] sm:max-h-[500px] lg:max-h-[580px] select-none drop-shadow-md"
      xmlns="http://www.w3.org/2000/svg"
    >
      ${svgPathsHtml}
    </svg>
    
    <!-- Smart Bounded Floater Tooltip Inside Map Container -->
    <div id="${containerId}-tooltip" class="pointer-events-none absolute z-30 hidden px-3.5 py-2 rounded-xl bg-slate-900/95 dark:bg-[#0B1E15]/95 border border-bdgreen-500 text-xs text-white shadow-2xl backdrop-blur-md transition-opacity">
      <div class="flex items-center gap-2">
        <span class="tooltip-en font-black text-bdred-400 text-sm"></span>
        <span class="tooltip-bn font-bengali text-white font-semibold text-sm"></span>
      </div>
      <span class="tooltip-div text-bdgreen-300 block text-[11px] font-semibold mt-0.5"></span>
    </div>
  `;

  const paths = container.querySelectorAll('.district-svg-path');
  const tooltip = document.getElementById(`${containerId}-tooltip`);

  paths.forEach(path => {
    const districtId = Number(path.getAttribute('data-id'));
    const district = districts.find(d => d.id === districtId);
    if (!district) return;

    const handleInspect = (clientX, clientY, isTouch = false) => {
      AppState.hoveredDistrictId = district.id;

      // 1. Update Inspector HUD inside the interactive map section
      updateMapInspectorHud(district, district.id === AppState.selectedDistrictId);

      // 2. Update Modal HUD if inside modal
      updateModalInspectorHud(district);

      // 3. Highlight hovered path on map
      paths.forEach(p => {
        const pId = Number(p.getAttribute('data-id'));
        if (pId === district.id) {
          if (pId !== AppState.selectedDistrictId) {
            p.style.fill = AppState.currentTheme === 'dark' ? '#10B981' : '#006A4E';
          }
        } else if (pId !== AppState.selectedDistrictId) {
          p.style.fill = '';
        }
      });

      // 4. Position the floater tooltip strictly clamped inside map container
      if (tooltip && clientX !== undefined && clientY !== undefined) {
        const enEl = tooltip.querySelector('.tooltip-en');
        const bnEl = tooltip.querySelector('.tooltip-bn');
        const divEl = tooltip.querySelector('.tooltip-div');

        if (enEl) enEl.textContent = district.en;
        if (bnEl) bnEl.textContent = `(${district.bn})`;
        if (divEl) divEl.textContent = `${district.div} Division • ${district.dist} from Dhaka`;

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
      closeMapModal();
      navigateToDistrict(district.id);
    });
  });

  // Highlight currently selected district (turns Red)
  if (AppState.selectedDistrictId) {
    updateVectorMapActiveState(AppState.selectedDistrictId);
  }
}

function updateMapInspectorHud(district, isActive = false) {
  if (!district) return;

  const nameEn = document.getElementById('inspector-name-en');
  const nameBn = document.getElementById('inspector-name-bn');
  const divBadge = document.getElementById('inspector-division');
  const distEl = document.getElementById('inspector-distance');
  const statsEl = document.getElementById('inspector-stats');
  const openBtn = document.getElementById('inspector-open-btn');
  const badgeIcon = document.getElementById('inspector-badge-icon');

  if (nameEn) nameEn.textContent = district.en;
  if (nameBn) nameBn.textContent = `(${district.bn})`;
  if (divBadge) divBadge.textContent = `${district.div} Division`;
  if (distEl) distEl.innerHTML = `<i data-lucide="milestone" class="w-3.5 h-3.5 inline"></i> ${district.dist} from Dhaka`;
  if (statsEl) statsEl.textContent = `${district.area} • ${district.pop} pop.`;

  if (badgeIcon) {
    badgeIcon.innerHTML = isActive 
      ? `<span class="w-2.5 h-2.5 rounded-full bg-bdred-500 animate-pulse"></span>`
      : `<span class="w-2.5 h-2.5 rounded-full bg-bdgreen-600"></span>`;
  }

  if (openBtn) {
    openBtn.onclick = () => navigateToDistrict(district.id);
    openBtn.innerHTML = `<span>View ${district.en} Details</span><i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>`;
  }

  initLucideIcons();
}

function updateModalInspectorHud(district) {
  const modalName = document.getElementById('modal-inspector-name');
  const modalBn = document.getElementById('modal-inspector-bn');
  const modalDiv = document.getElementById('modal-inspector-div');
  const modalHud = document.getElementById('modal-map-inspector-hud');

  if (modalName) modalName.textContent = district.en;
  if (modalBn) modalBn.textContent = `(${district.bn})`;
  if (modalDiv) modalDiv.textContent = `• ${district.div} Division • ${district.dist} from Dhaka`;

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
// 9. MOBILE SEGMENTED VIEW CONTROLLER
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
// 10. MODAL CONTROLS & TOAST NOTIFICATION
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
  }, 2200);
}

// ==========================================
// 11. UI EVENT WIRING & LISTENERS
// ==========================================
function setupEventListeners() {
  // Theme Toggle Button
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  if (themeToggleBtn) themeToggleBtn.addEventListener('click', toggleTheme);

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

  // Keyboard Navigation (Escape key)
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
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
  document.querySelectorAll('.division-pill').forEach(pill => {
    const div = pill.getAttribute('data-division');
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
