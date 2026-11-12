/*! Scroll-reveal: staggered fade-up + stat count-up. Zero deps, reduced-motion aware. */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced || !('IntersectionObserver' in window)) return;

  var SELECTORS = [
    '.home-section .section-head',
    '.lab-research-cards > .lab-card',
    '.lab-people-grid > *',
    '.lab-news-item'
  ];

  var els = [];
  SELECTORS.forEach(function (sel) {
    els = els.concat(Array.prototype.slice.call(document.querySelectorAll(sel)));
  });

  // Stagger within each parent group (cards cascade left-to-right / top-to-bottom)
  els.forEach(function (el) {
    var idx = Array.prototype.indexOf.call(el.parentElement.children, el);
    el.style.transitionDelay = Math.min(idx * 70, 420) + 'ms';
    el.classList.add('lab-reveal');
  });

  if (els.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('lab-reveal-in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  // Stat count-up: numbers ease from 0 to real value when visible
  var nums = Array.prototype.slice.call(document.querySelectorAll('.lab-hero-stat-num'));
  nums.forEach(function (el) {
    var to = parseInt(el.textContent, 10);
    if (isNaN(to) || to <= 0) return;
    el.setAttribute('data-count', to);
    el.textContent = '0';
    var nio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        nio.unobserve(el);
        countUp(el, to);
      });
    }, { threshold: 0.4 });
    nio.observe(el);
  });

  function countUp(el, to) {
    var t0 = null;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / 900, 1);
      el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = to;
    }
    requestAnimationFrame(step);
  }
})();
