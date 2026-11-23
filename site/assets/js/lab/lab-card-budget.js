/*! Poster-card text budget: a 1-line title gets a 3-line summary, a 2-line
    title gets 2 lines — so the fixed-height card never clips its text.
    Zero deps; re-measures on resize, after webfonts settle, and whenever a
    card changes size (e.g. paged-out items being revealed). */
(function () {
  function tune(card) {
    var title = card.querySelector('.lab-card-title');
    var summary = card.querySelector('.lab-card-summary');
    if (!title || !summary || !card.getClientRects().length) return;
    var cs = window.getComputedStyle(title);
    var lh = parseFloat(cs.lineHeight);
    if (!lh || isNaN(lh)) lh = parseFloat(cs.fontSize) * 1.4;
    /* scrollHeight reports the unclamped text height (clamp caps clientHeight) */
    var lines = Math.max(1, Math.round(title.scrollHeight / lh));
    var clamp = lines > 1 ? '2' : '3';
    summary.style.webkitLineClamp = clamp;
    summary.style.lineClamp = clamp;
  }

  function run(root) {
    var cards = (root || document).querySelectorAll('.lab-card--poster');
    for (var i = 0; i < cards.length; i++) tune(cards[i]);
  }

  var timer;
  window.addEventListener('resize', function () {
    clearTimeout(timer);
    timer = setTimeout(function () { run(); }, 150);
  });

  /* Client-rendered grids (hub search/filter re-render via innerHTML)
     dispatch lab:grid-change — re-measure the fresh cards here. */
  document.addEventListener('lab:grid-change', function (ev) {
    run(ev.target);
  });

  if ('ResizeObserver' in window) {
    var ro = new ResizeObserver(function (entries) {
      for (var i = 0; i < entries.length; i++) {
        tune(entries[i].target);
      }
    });
    var observed = typeof WeakSet === 'function' ? new WeakSet() : null;
    var observeAll = function (root) {
      var cards = (root || document).querySelectorAll('.lab-card--poster');
      for (var j = 0; j < cards.length; j++) {
        if (observed && !observed.has(cards[j])) {
          observed.add(cards[j]);
          ro.observe(cards[j]);
        }
      }
    };
    observeAll(document);
    /* Re-observe cards added later (lab-hub-search results) */
    document.addEventListener('lab:grid-change', function (ev) {
      observeAll(ev.target);
    });
  }

  run();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { run(); });
})();