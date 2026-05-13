// Position-on-hover for footnote tooltips (.source-marker, .override-marker).
//
// CSS keeps the tooltip hidden by default. JS toggles `.is-open` on hover /
// focus and writes inline `position: fixed; top; left;` so the tooltip can
// escape Starlight's ancestor overflow (sidebars clip absolute children).
//
// Position rules:
//   - Centered horizontally on the marker.
//   - Above the marker by default; flips below if it would clip the article's
//     top edge.
//   - Left/right edges clamped to the article container so the tooltip never
//     overlaps the sidebars or the page rails.

(function () {
  const MARKER_SELECTOR = "sup.source-marker, sup.override-marker";
  const TOOLTIP_SELECTOR = ".source-marker-tooltip, .override-marker-tooltip";
  const EDGE_PAD = 12;
  const GAP = 8;

  function findArticleRect(marker) {
    // Starlight wraps the page body in <main>; the inner article gets a
    // .sl-markdown-content wrapper. Either is a reasonable bound — prefer
    // the inner one so we don't extend the tooltip under the right TOC rail.
    const container =
      marker.closest(".sl-markdown-content") ||
      marker.closest("main") ||
      document.body;
    return container.getBoundingClientRect();
  }

  // Selectors for elements pinned to the top of the viewport. Used to
  // compute the lowest bottom edge so the tooltip sits below all of them
  // rather than sliding under any one. Add new selectors here if more
  // sticky bars appear (page-action toolbar, banner, etc.).
  const STICKY_TOP_SELECTORS = [
    "header.header", // main site header
    "mobile-starlight-toc nav", // narrow-viewport "On this page" sticky strip
  ];

  function findTopBoundary() {
    let bottom = 0;
    for (const sel of STICKY_TOP_SELECTORS) {
      document.querySelectorAll(sel).forEach((el) => {
        const r = el.getBoundingClientRect();
        // Only count visible elements near the top of the viewport.
        if (r.height > 0 && r.top < 200) {
          if (r.bottom > bottom) bottom = r.bottom;
        }
      });
    }
    return bottom;
  }

  function positionTooltip(marker) {
    const tooltip = marker.querySelector(TOOLTIP_SELECTOR);
    if (!tooltip) return;

    // Make visible offscreen so we can measure final dimensions.
    tooltip.classList.add("is-open");
    tooltip.style.position = "fixed";
    tooltip.style.left = "-9999px";
    tooltip.style.top = "0";
    tooltip.style.transform = "none";
    tooltip.style.bottom = "auto";
    tooltip.style.margin = "0";

    const markerRect = marker.getBoundingClientRect();
    const tipRect = tooltip.getBoundingClientRect();
    const articleRect = findArticleRect(marker);

    // Horizontal: center on marker, then clamp to article edges.
    let left = markerRect.left + markerRect.width / 2 - tipRect.width / 2;
    const minLeft = articleRect.left + EDGE_PAD;
    const maxLeft = articleRect.right - tipRect.width - EDGE_PAD;
    if (left < minLeft) left = minLeft;
    if (left > maxLeft) left = Math.max(minLeft, maxLeft);

    // Vertical: above marker by default; flip below if would clip the
    // sticky header (the visible top edge of the article area). The
    // article's own top can be far negative when the page is scrolled,
    // so we floor on the header's bottom edge instead.
    const topFloor = Math.max(articleRect.top, findTopBoundary());
    let top = markerRect.top - tipRect.height - GAP;
    if (top < topFloor + EDGE_PAD) {
      top = markerRect.bottom + GAP;
    }

    tooltip.style.left = left + "px";
    tooltip.style.top = top + "px";
  }

  function hideTooltip(marker) {
    const tooltip = marker.querySelector(TOOLTIP_SELECTOR);
    if (!tooltip) return;
    tooltip.classList.remove("is-open");
    tooltip.removeAttribute("style");
  }

  function bind(marker) {
    marker.addEventListener("mouseenter", () => positionTooltip(marker));
    marker.addEventListener("mouseleave", () => hideTooltip(marker));
    marker.addEventListener("focus", () => positionTooltip(marker));
    marker.addEventListener("blur", () => hideTooltip(marker));
  }

  function init() {
    document.querySelectorAll(MARKER_SELECTOR).forEach(bind);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // Starlight does client-side navigation; re-bind after each page swap.
  document.addEventListener("astro:page-load", init);
})();
