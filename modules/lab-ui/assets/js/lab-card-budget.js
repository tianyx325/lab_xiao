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

  if ('ResizeObserver' in window) {
    var ro = new ResizeObserver(function (entries) {
      for (var i = 0; i < entries.length; i++) {
        tune(entries[i].target);
      }
    });
    var all = document.querySelectorAll('.lab-card--poster');
    for (var j = 0; j < all.length; j++) ro.observe(all[j]);
  }

  run();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { run(); });
})();