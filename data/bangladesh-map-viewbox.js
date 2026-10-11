/**
 * Bangladesh Vector Map ViewBox Coordinates
 * Absolute boundary definitions for geographic SVG polygon mapping
 */
const BANGLADESH_MAP_VIEWBOX = {
  w: 600,
  h: 848
};

// Global memory registry
if (typeof window !== 'undefined') {
  window.BANGLADESH_MAP_VIEWBOX = BANGLADESH_MAP_VIEWBOX;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { BANGLADESH_MAP_VIEWBOX };
}
