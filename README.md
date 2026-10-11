# Local Host — Explore Bangladesh District by District (Offline-First Edition) 🇧🇩

> A 100% self-hosted, local-first interactive vector map and district profile exploration platform for all 64 districts of Bangladesh. Zero external API dependencies, executing purely out of local memory buffers and optimized static assets.

---

## 🌟 Key Features

- **100% Self-Hosted & Offline-First**:
  - Zero external API fetch calls (completely removed `bdapis.com` dynamic fetch loops).
  - All district metadata, coordinates, statistics, and SVG vector paths execute directly from local memory buffers (`window.LOCAL_DISTRICTS` and `window.MAP_PATHS`).
  - Native streaming of local `.webp` photography and local Kalpurush (`.woff2`) Bengali typography.

- **Cinematic District Hero Banner**:
  - Full-width, high-impact panoramic hero banner (`h-80 sm:h-96 lg:h-[440px]`) at the top of each district profile.
  - Dark gradient fade overlay (`from-slate-950 via-slate-950/45 to-transparent`).
  - Crisp bilingual typography: Large English name with authentic localized Bengali name in Kalpurush font.
  - Interactive badges: Division indicator, geographic coordinates, and instant *"Locate on Vector Map"* button.

- **Smooth Pure CSS Scroll-Snap Carousel**:
  - 5-image horizontal panoramic carousel placed immediately beneath the transit breakdown.
  - Built with pure CSS scroll-snapping structures (`flex overflow-x-auto snap-x snap-mandatory shrink-0`) for friction-free touch/drag/trackpad swiping without external libraries.

- **Enforced Top-5 Cards (Historical & Tourist Sections)**:
  - **Historical Places & Heritage**: Top 5 verified monuments and heritage sites with dedicated local `.webp` image frames, detailed paragraph-length descriptions, and bottom-anchored map pin tags.
  - **Tourist Attractions & Highlights**: Top 5 scenic landscapes, lakeside promenades, and cultural attractions with local `.webp` imagery and location indicators.

- **Interactive Vector SVG Map**:
  - Full vector polygon rendering of all 64 districts of Bangladesh.
  - Real-time hover / touch inspection (**Flag Green** hover, **Flag Red** active selection).
  - Boundary-clamped floating tooltip strictly constrained within the map container.
  - Dedicated **In-Map District Inspector HUD** displaying live district telemetry with one-click profile routing.

- **Dynamic Mobile & Desktop Screen Optimization**:
  - **Desktop (≥ 1024px)**: Sticky dual-column grid (`sticky top-20 max-h-[calc(100vh-6rem)] overflow-y-auto`) keeping search filters accessible while the vector map remains locked in view.
  - **Mobile (< 1024px)**: Dynamic Segmented View Controller (`[ 🗺️ Interactive Map View ]` vs `[ 📋 64 Districts List ]`) to prevent infinite vertical scrolling fatigue on mobile viewports.
  - **Touch Ergonomics**: All interactive elements maintain a minimum height of `≥42px`.
  - **Zero-Jank DOM**: Single-pass raw template injection (`.innerHTML`) for instant rendering.

- **National Identity & Theming**:
  - Bangladesh Flag color palette: Forest Green (`#006A4E` / `#059669`), Sun Red (`#F42A41`), and clean neutral surfaces.
  - Interactive **Dark Mode ↔ Light Mode** toggle with instant persistence via `localStorage`.
  - Local **Kalpurush** Bengali font (`fonts/kalpurush.woff2`) and **Plus Jakarta Sans** for English.

---

## 📁 Rigid Offline Project Structure

```text
EzzeMap/
├── data/
│   ├── bangladesh-map-viewbox.js   # Absolute map layout tracking coordinates (viewBox 0 0 600 848)
│   ├── map-paths.js                # Core SVG path polygon vector arrays for all 64 districts
│   └── main-info/                  # Modular text information catalogs
│       ├── catalog.js              # Comprehensive base schemas for all 64 districts
│       ├── dhaka.js                # Reference production schema (5 hist + 5 tour + 5 carousel)
│       ├── cox-s-bazar.js          # Detailed production schema
│       └── [remaining-districts].js# Modular schemas for all districts
├── images/
│   ├── default/
│   │   ├── hero.webp               # High-res fallback panoramic hero banner
│   │   └── card.webp               # High-res fallback location card graphic
│   └── districts/
│       └── [district-slug]/
│           ├── hero.webp           # Full-width cinematic hero graphic
│           ├── carousel-1.webp ... carousel-5.webp  # Snap slider panoramas
│           ├── hist-1.webp     ... hist-5.webp      # Historical monuments
│           └── tour-1.webp     ... tour-5.webp      # Tourist attractions
├── fonts/
│   └── kalpurush.woff2             # Local Bengali typography package
├── index.html                      # Unified responsive interface blueprint
├── app.js                          # Reactive application controller, router, & state manager
├── server.js                       # Native Node.js streaming HTTP server
├── district-data.js            # Legacy vector database (retained for backward compatibility)
└── README.md                       # Platform documentation
```

---

## 🚀 Getting Started

### 1. Launch with Native Node.js Server
Clone the repository and launch the built-in streaming server:
```bash
git clone https://github.com/ImranHasan13421/EzzeMap.git
cd EzzeMap
node server.js
```
Then navigate to:
```
http://localhost:3000
```

### 2. Static Hosting / Offline Deployment
The application has **zero runtime dependencies**. You can open `index.html` directly in any modern browser or host it on GitHub Pages, Vercel, Netlify, or Nginx.

---

## 🛠️ Technology Stack

- **Frontend Core**: Vanilla HTML5, Vanilla JavaScript (ES6+), URL Hash Routing (`#/district/<slug>`)
- **Styling**: Tailwind CSS (with custom Bangladesh Flag palette and responsive typography)
- **Typography**: Local Kalpurush Bengali Font (`fonts/kalpurush.woff2`) + Plus Jakarta Sans
- **Vector Graphics**: Native SVG paths (`data/map-paths.js`)
- **Image Formats**: High-performance binary `.webp`
- **Streaming Driver**: Native Node.js `http`, `fs`, `path` (Zero npm package dependencies)

---

## 📄 License
MIT License. Free for open-source exploration, cultural archiving, and educational use.

