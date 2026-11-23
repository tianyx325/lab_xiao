/*! Scroll-reveal: staggered fade-up + stat count-up. Zero deps, reduced-motion aware. */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced || !('IntersectionObserver' in window)) return;

  var SELECTORS = [
    '.home-section .section-head',
    '.lab-research-cards > .lab-card',
    '.lab-people-grid > *',
    '.lab-news-item',
    '.lab-list-grid > .lab-list-item'
  ];

  var els = [];
  SELECTORS.forEach(function (sel) {
    els = els.concat(Array.prototype.slice.call(document.querySelectorAll(sel)));
  });

  var revealStyles = window.getComputedStyle(document.documentElement);
  var revealStep = parseFloat(revealStyles.getPropertyValue('--lab-reveal-step')) || 0;
  var revealMax = parseFloat(revealStyles.getPropertyValue('--lab-reveal-max')) || 0;
  var countDuration = parseFloat(revealStyles.getPropertyValue('--lab-count-duration')) || 1;

  // Stagger within each parent group (cards cascade left-to-right / top-to-bottom)
  els.forEach(function (el) {
    var idx = Array.prototype.indexOf.call(el.parentElement.children, el);
    el.style.transitionDelay = Math.min(idx * revealStep, revealMax) + 'ms';
    el.classList.add('lab-reveal');
  });

  if (els.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('lab-reveal-in');
          entry.target.addEventListener('transitionend', function () {
            entry.target.style.transitionDelay = '';
            entry.target.style.willChange = 'auto';
          }, { once: true });
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  // Stat count-up: visible spans ease from 0 to real value when visible.
  // The template pairs each with an .sr-only final value, so screen readers
  // never hear the intermediate numbers (spans here are aria-hidden anyway).
  var nums = Array.prototype.slice.call(document.querySelectorAll('.lab-hero-stat-count'));
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
      var p = Math.min((ts - t0) / countDuration, 1);
      el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = to;
    }
    requestAnimationFrame(step);
  }
})();
