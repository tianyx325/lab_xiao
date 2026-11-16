/*! Research scroll-story — sticky index highlights the panel in view.
    IntersectionObserver picks the most-visible panel; clicking a nav item
    smooth-scrolls to it. Reduced motion: instant jumps, no active tracking. */
(function () {
  var root = document.querySelector('[data-lab-story]');
  if (!root) return;
  var panels = Array.prototype.slice.call(root.querySelectorAll('[data-story-panel]'));
  var links = Array.prototype.slice.call(root.querySelectorAll('[data-story-link]'));
  if (!panels.length || !links.length) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function setActive(i) {
    links.forEach(function (l, k) {
      l.classList.toggle('is-active', k === i);
      if (k === i) { l.setAttribute('aria-current', 'true'); }
      else { l.removeAttribute('aria-current'); }
    });
    panels.forEach(function (p, k) { p.classList.toggle('is-active', k === i); });
  }

  if ('IntersectionObserver' in window && !reduce) {
    var visible = new Map();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { visible.set(e.target, e.intersectionRatio); }
        else { visible.delete(e.target); }
      });
      var best = null;
      var bestRatio = 0;
      visible.forEach(function (ratio, target) {
        if (ratio > bestRatio) { bestRatio = ratio; best = target; }
      });
      if (best) {
        setActive(parseInt(best.getAttribute('data-story-panel'), 10));
      }
    }, { threshold: [0.25, 0.5, 0.75], rootMargin: '-15% 0px -15% 0px' });
    panels.forEach(function (p) { io.observe(p); });
  } else {
    setActive(0);
  }

  links.forEach(function (l) {
    l.addEventListener('click', function (ev) {
      var id = (l.getAttribute('href') || '').slice(1);
      var target = id && document.getElementById(id);
      if (!target) return;
      ev.preventDefault();
      target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
      setActive(links.indexOf(l));
    });
  });
})();
