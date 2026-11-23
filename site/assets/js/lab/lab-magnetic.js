/*! Magnetic primary CTA: a 4px maximum pull toward the pointer, fine
    pointers only, disabled under prefers-reduced-motion. Zero deps. */
(function () {
  if (!window.matchMedia || !window.matchMedia("(pointer: fine)").matches) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  var pull = 0.12;
  var max = 4;

  document.querySelectorAll("[data-lab-magnetic]").forEach(function (el) {
    var raf = 0;

    function reset() {
      el.style.removeProperty("--lab-magnet-x");
      el.style.removeProperty("--lab-magnet-y");
    }

    function move(e) {
      var r = el.getBoundingClientRect();
      var dx = (e.clientX - (r.left + r.width / 2)) * pull;
      var dy = (e.clientY - (r.top + r.height / 2)) * pull;
      dx = Math.max(-max, Math.min(max, dx));
      dy = Math.max(-max, Math.min(max, dy));
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(function () {
        el.style.setProperty("--lab-magnet-x", dx + "px");
        el.style.setProperty("--lab-magnet-y", dy + "px");
      });
    }

    el.addEventListener("pointermove", move);
    el.addEventListener("pointerleave", reset);
    el.addEventListener("blur", reset);
  });
})();