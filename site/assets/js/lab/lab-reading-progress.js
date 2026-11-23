/*! Reading progress fallback. CSS scroll-driven animation handles modern
    browsers; this keeps the 1px line alive elsewhere and under reduced
    motion (where the CSS animation is disabled). Zero deps. */
(function () {
  var bar = document.querySelector(".lab-reading-progress span");
  if (!bar) return;

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var supported =
    window.CSS && CSS.supports && CSS.supports("animation-timeline: scroll()");
  if (supported && !reduce) return;

  var pane = document.querySelector(".page-body");
  var scrolls = false;
  if (pane) {
    var overflow = window.getComputedStyle(pane).overflowY;
    scrolls = overflow === "auto" || overflow === "scroll";
  }

  function update() {
    var el = scrolls ? pane : document.scrollingElement || document.documentElement;
    var max = el.scrollHeight - el.clientHeight;
    var p = max > 0 ? Math.min(1, Math.max(0, el.scrollTop / max)) : 0;
    bar.style.setProperty("--lab-read-progress", p);
  }

  (scrolls ? pane : window).addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update, { passive: true });
  update();
})();