/*! Back-to-top — site-wide. Appears after one screenful of scrolling; smooth
    unless the user prefers reduced motion. Every page uses the .page-body
    app-shell scroller (baseof renders the button for all page kinds). */
(function () {
  var topBtn = document.querySelector('.lab-top-btn');
  if (!topBtn) return;

  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var pane = document.querySelector('.page-body');
  var paneScrolls = function () {
    if (!pane) return false;
    var oy = window.getComputedStyle(pane).overflowY;
    return (oy === 'auto' || oy === 'scroll') &&
      pane.scrollHeight > pane.clientHeight + 1;
  };
  var onScroll = function () {
    var y = paneScrolls() ? pane.scrollTop : (window.scrollY || 0);
    topBtn.hidden = y < 480;
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  if (pane) pane.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  topBtn.addEventListener('click', function () {
    var behavior = prefersReduced.matches ? 'auto' : 'smooth';
    if (paneScrolls()) pane.scrollTo({ top: 0, behavior: behavior });
    else window.scrollTo({ top: 0, behavior: behavior });
  });
})();
