/**
 * Local Host — Explore Bangladesh District by District
 * Frontend Architecture & Logic
 * 
 * Features:
 * - Dedicated Home Page & Separate District Detail Page with "Back to Home"
 * - In-Map District Detail Inspector HUD & strictly bounded float box
 * - Kalpurush Bangla font and Plus Jakarta Sans typography
 * - Green (Primary) / White / Red Theme with interactive Dark / Light Mode
 * - Read-only exploration portal (all edit options removed)
 * - Dynamic BD API fetch with fallback to 64-district local schema
 * - Live real-time search & division filtering
 * - Next / Previous district navigation
 */

// ==========================================
// STATE MANAGEMENT
// ==========================================
const AppState = {
  districts: [],             // All 64 district objects
  filteredDistricts: [],     // Currently filtered/searched list
  selectedDistrictId: null,  // Active selected district ID
  hoveredDistrictId: null,   // Currently hovered district ID
  activeDivision: 'all',     // Active division filter
  searchQuery: '',           // Current search text
  sortBy: 'name-asc',        // Current sorting rule
  apiStatus: 'connecting',   // connecting | connected | fallback
  currentTheme: 'dark',      // 'dark' | 'light'
  mobileHomeTab: 'map',      // 'map' | 'list' (on mobile viewports)
};

// Storage key for theme
const THEME_KEY = 'localhost_district_theme_v1';

// ==========================================
// INITIALIZATION
// ==========================================
document.addEventListener('DOMContentLoaded', async () => {
  initTheme();
  initLucideIcons();
  setupEventListeners();

  // Load district data (Fetch API + Fallback Schema)
  await loadDistrictData();

  // Handle URL Hash Routing
  window.addEventListener('hashchange', handleRoute);
  handleRoute();
});

function initLucideIcons() {
  if (window.lucide) {
    window.lucide.createIcons();
  }
}

// ==========================================
// THEME MANAGEMENT (DARK / LIGHT TOGGLE)
// ==========================================
function initTheme() {
  const savedTheme = localStorage.getItem(THEME_KEY);
  if (savedTheme) {
    AppState.currentTheme = savedTheme;
  } else {
    AppState.currentTheme = 'dark';
  }
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
// DATA LOADING (API & FALLBACK)
// ==========================================
async function loadDistrictData() {
  const statusBeacon = document.getElementById('api-beacon');
  const statusText = document.getElementById('api-status-text');
  const countBadge = document.getElementById('api-district-count');

  // Obtain master dataset from window or fallback
  const fallbackList = (typeof window !== 'undefined' && window.DISTRICTS_DATA) 
    ? window.DISTRICTS_DATA 
    : ((typeof DISTRICTS_DATA !== 'undefined') ? DISTRICTS_DATA : []);

  let baseDistricts = [...fallbackList];

  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 4000);

    const response = await fetch('https://bdapis.com/api/v1.2/districts', {
      signal: controller.signal
    });
    clearTimeout(timeoutId);

    if (response.ok) {
      const result = await response.json();
      if (result && Array.isArray(result.data)) {
        const apiMap = new Map();
        result.data.forEach(item => {
          if (item.district) {
            apiMap.set(item.district.toLowerCase(), item);
          }
        });

        baseDistricts = baseDistricts.map(dst => {
          const apiMatch = apiMap.get(dst.en.toLowerCase());
          if (apiMatch) {
            return {
              ...dst,
              coordinates: apiMatch.coordinates || dst.coordinates,
              bn: apiMatch.districtbn || dst.bn,
            };
          }
          return dst;
        });

        AppState.apiStatus = 'connected';
        if (statusBeacon) statusBeacon.className = 'w-2.5 h-2.5 rounded-full bg-bdgreen-500 beacon-pulse shrink-0';
        if (statusText) statusText.textContent = 'BD-APIs Live Connected';
      }
    } else {
      throw new Error(`API HTTP ${response.status}`);
    }
  } catch (err) {
    console.warn('Using Local Fallback Schema for 64 districts:', err.message);
    AppState.apiStatus = 'fallback';
    if (statusBeacon) statusBeacon.className = 'w-2.5 h-2.5 rounded-full bg-bdred-500 shrink-0';
    if (statusText) statusText.textContent = 'Offline Cache Active';
  }

  AppState.districts = baseDistricts;
  if (countBadge) countBadge.textContent = `${AppState.districts.length} Districts`;

  // Render sidebar and maps
  filterAndRenderDistricts();
  renderVectorMap('empty-state-svg-map-container');
  renderVectorMap('modal-svg-map-container');

  // Set default inspector view
  if (AppState.districts.length > 0) {
    updateMapInspectorHud(AppState.districts[0]); // default to Dhaka
  }
}

// ==========================================
// PAGE ROUTING & NAVIGATION (HOME vs DETAIL PAGE)
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

  // Otherwise show Home Page
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
    void viewHome.offsetWidth; // reflow
    viewHome.classList.add('animate-slide-up');
  }
  if (viewDetails) viewDetails.classList.add('hidden');

  // Restore active mobile tab (map vs list)
  setMobileHomeTab(AppState.mobileHomeTab || 'map');

  // Ensure maps are drawn and active state cleared or updated
  renderVectorMap('empty-state-svg-map-container');
  window.scrollTo({ top: 0, behavior: 'smooth' });
  initLucideIcons();
}

function showDistrictDetailsPage(district) {
  AppState.selectedDistrictId = district.id;

  const viewHome = document.getElementById('view-home');
  const viewDetails = document.getElementById('view-details');

  if (viewHome) viewHome.classList.add('hidden');
  if (viewDetails) {
    viewDetails.classList.remove('hidden');
    viewDetails.classList.remove('animate-slide-up');
    void viewDetails.offsetWidth; // reflow
    viewDetails.classList.add('animate-slide-up');
  }

  // Populate Details
  populateDistrictDetails(district);

  // Update map active highlights
  updateVectorMapActiveState(district.id);

  // Update Inspector HUD as active
  updateMapInspectorHud(district, true);

  window.scrollTo({ top: 0, behavior: 'smooth' });
  initLucideIcons();
}

// ==========================================
// FILTER, SEARCH, AND SORT LOGIC
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
      const bnMatch = d.bn.includes(q);
      const divMatch = d.div.toLowerCase().includes(q);
      return enMatch || bnMatch || divMatch;
    });
  }

  // 3. Sort
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
        const areaA = parseFloat(a.area.replace(/,/g, '')) || 0;
        const areaB = parseFloat(b.area.replace(/,/g, '')) || 0;
        return areaB - areaA;
      }
      case 'pop-desc': {
        const popA = parseFloat(a.pop) || 0;
        const popB = parseFloat(b.pop) || 0;
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

  container.innerHTML = list.map(item => {
    const isActive = item.id === AppState.selectedDistrictId;
    return `
      <div 
        id="district-item-${item.id}"
        onclick="navigateToDistrict(${item.id})"
        onmouseenter="handleSidebarHover(${item.id})"
        class="district-card cursor-pointer p-3 rounded-xl transition-all duration-200 flex items-center justify-between group ${
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
              <span class="font-bengali text-xs text-slate-500 dark:text-slate-400 font-semibold">${item.bn}</span>
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
          <i data-lucide="chevron-right" class="w-4 h-4 transition-transform duration-200 ${isActive ? 'text-bdred-500 translate-x-1' : 'text-slate-400 group-hover:text-slate-600 dark:group-hover:text-slate-300'}"></i>
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
    // highlight on map with hover styling
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
// POPULATE DETAIL PAGE
// ==========================================
function populateDistrictDetails(district) {
  // Breadcrumb
  document.getElementById('breadcrumb-division').textContent = `${district.div} Division`;
  document.getElementById('breadcrumb-district').textContent = `${district.en} (${district.bn})`;

  // Hero Section
  document.getElementById('detail-name-en').textContent = district.en;
  document.getElementById('detail-name-bn').textContent = district.bn;
  document.getElementById('detail-division-badge').textContent = `${district.div} Division`;
  document.getElementById('detail-coordinates').textContent = district.coordinates;
  document.getElementById('detail-tagline').textContent = `${district.en} (${district.bn}) is a renowned administrative and historical district located under ${district.div} Division.`;

  // Key Metric 4-Grid
  document.getElementById('detail-est-year').textContent = district.est || '1984';
  document.getElementById('detail-total-area').textContent = district.area || 'N/A';
  document.getElementById('detail-total-pop').textContent = district.pop || 'N/A';
  document.getElementById('detail-distance').textContent = district.dist || 'N/A';

  // Route Section
  const routeEl = document.getElementById('detail-route-text');
  if (routeEl) {
    routeEl.textContent = district.route 
      ? `Route details coming soon... ${district.route}`
      : 'Route details coming soon... Direct highway transit and railway corridors connect from Dhaka.';
  }

  // Section 7: Historical Places
  const histContainer = document.getElementById('detail-historical-cards-container');
  if (histContainer) {
    if (district.hist && district.hist.length > 0) {
      histContainer.innerHTML = district.hist.map(item => `
        <div class="p-4 rounded-xl bg-slate-50 dark:bg-[#07150E] border border-slate-200 dark:border-[#173728] hover:border-bdred-500 hover:-translate-y-0.5 transition-all group">
          <div class="flex items-center justify-between mb-2">
            <h4 class="font-extrabold text-sm text-slate-900 dark:text-slate-100 group-hover:text-bdred-500 transition-colors">${item.name}</h4>
            <span class="text-[10px] px-2 py-0.5 rounded-full bg-bdred-100 dark:bg-bdred-950/60 text-bdred-700 dark:text-bdred-400 border border-bdred-200 dark:border-bdred-900 font-bold">Historical Landmark</span>
          </div>
          <p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed font-normal">${item.desc}</p>
        </div>
      `).join('');
    } else {
      histContainer.innerHTML = `
        <div class="col-span-2 p-6 rounded-xl bg-slate-50 dark:bg-[#07150E] border border-slate-200 dark:border-[#173728] text-center text-slate-500 text-xs">
          Historical landmarks archive for ${district.en} is being curated.
        </div>
      `;
    }
  }

  // Section 8: Tourist Attractions
  const tourContainer = document.getElementById('detail-tourist-cards-container');
  if (tourContainer) {
    if (district.tour && district.tour.length > 0) {
      tourContainer.innerHTML = district.tour.map(item => `
        <div class="p-4 rounded-xl bg-slate-50 dark:bg-[#07150E] border border-slate-200 dark:border-[#173728] hover:border-bdgreen-500 hover:-translate-y-0.5 transition-all group">
          <div class="flex items-center justify-between mb-2">
            <h4 class="font-extrabold text-sm text-slate-900 dark:text-slate-100 group-hover:text-bdgreen-600 dark:group-hover:text-bdgreen-400 transition-colors">${item.name}</h4>
            <span class="text-[10px] px-2 py-0.5 rounded-full bg-bdgreen-100 dark:bg-bdgreen-950/80 text-bdgreen-800 dark:text-bdgreen-300 border border-bdgreen-300 dark:border-bdgreen-700 font-bold">${item.cat || 'Attraction'}</span>
          </div>
          <p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed font-normal">${item.desc}</p>
        </div>
      `).join('');
    } else {
      tourContainer.innerHTML = `
        <div class="col-span-2 p-6 rounded-xl bg-slate-50 dark:bg-[#07150E] border border-slate-200 dark:border-[#173728] text-center text-slate-500 text-xs">
          Tourist highlights for ${district.en} are currently in editorial review.
        </div>
      `;
    }
  }

  // Next / Prev button wiring
  const currentId = district.id;
  const prevId = currentId > 1 ? currentId - 1 : 64;
  const nextId = currentId < 64 ? currentId + 1 : 1;

  const prevBtn = document.getElementById('prev-district-btn');
  const nextBtn = document.getElementById('next-district-btn');

  if (prevBtn) prevBtn.onclick = () => navigateToDistrict(prevId);
  if (nextBtn) nextBtn.onclick = () => navigateToDistrict(nextId);
}

// ==========================================
// INTERACTIVE VECTOR SVG MAP & INSPECTOR HUD
// ==========================================
function renderVectorMap(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const viewBox = (typeof window !== 'undefined' && window.BANGLADESH_MAP_VIEWBOX) 
    ? window.BANGLADESH_MAP_VIEWBOX 
    : ((typeof BANGLADESH_MAP_VIEWBOX !== 'undefined') ? BANGLADESH_MAP_VIEWBOX : { w: 600, h: 848 });

  const districts = (typeof window !== 'undefined' && window.DISTRICTS_DATA) 
    ? window.DISTRICTS_DATA 
    : ((typeof DISTRICTS_DATA !== 'undefined') ? DISTRICTS_DATA : AppState.districts);

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

    // Common inspection handler for both Desktop MouseMove and Mobile TouchStart
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

      // 4. Position the floater tooltip STRICTLY CLAMPED inside container
      if (tooltip && clientX !== undefined && clientY !== undefined) {
        const enEl = tooltip.querySelector('.tooltip-en');
        const bnEl = tooltip.querySelector('.tooltip-bn');
        const divEl = tooltip.querySelector('.tooltip-div');

        if (enEl) enEl.textContent = district.en;
        if (bnEl) bnEl.textContent = `(${district.bn})`;
        if (divEl) divEl.textContent = `${district.div} Division • ${district.dist} from Dhaka`;

        tooltip.classList.remove('hidden');

        // Bounding box calculation relative to map container
        const rect = container.getBoundingClientRect();
        const tooltipWidth = tooltip.offsetWidth || 180;
        const tooltipHeight = tooltip.offsetHeight || 55;

        let posX = clientX - rect.left + 15;
        let posY = clientY - rect.top + 15;

        // Strict clamp inside container boundaries
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
      
      // If a district is currently selected, restore HUD to that district
      if (AppState.selectedDistrictId) {
        const selected = districts.find(d => d.id === AppState.selectedDistrictId);
        if (selected) updateMapInspectorHud(selected, true);
      }
    });

    // Click Interaction: Navigates directly to the district profile page!
    path.addEventListener('click', (e) => {
      closeMapModal();
      navigateToDistrict(district.id);
    });
  });

  // Highlight currently selected district (turns Red)
  if (AppState.selectedDistrictId) {
    updateVectorMapActiveState(AppState.selectedDistrictId);
  }
}

/**
 * Updates the In-Map District Detail Inspector HUD box
 * Ensures viewers clearly see the district name (English & Kalpurush),
 * division, distance, and quick metrics right in the map section.
 */
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
// MODAL CONTROLS (VECTOR MAP)
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

// ==========================================
// TOAST NOTIFICATIONS
// ==========================================
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
  }, 2500);
}

// ==========================================
// EVENT LISTENERS & UI WIRING
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

  // In-Map Inspector HUD Click interaction
  const mapInspectorHud = document.getElementById('map-inspector-hud');
  if (mapInspectorHud) {
    mapInspectorHud.addEventListener('click', (e) => {
      if (e.target.closest('#inspector-open-btn')) return;
      const targetId = AppState.hoveredDistrictId || AppState.selectedDistrictId || 1;
      navigateToDistrict(targetId);
    });
  }

  // Keyboard navigation
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

/**
 * Mobile Tab Switcher: Toggles between Interactive Map and 64 Districts List on mobile
 */
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
