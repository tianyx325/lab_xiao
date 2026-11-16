/*! Navbar scroll shadow effect */
(function () {
  var header = document.querySelector('.page-header.header--fixed');
  if (!header) return;

  /* List and detail pages scroll .page-body, not the window. */
  var pane = document.querySelector('.page-body');
  var scroller = null;
  if (pane) {
    var overflow = window.getComputedStyle(pane).overflowY;
    if (overflow === 'auto' || overflow === 'scroll') scroller = pane;
  }

  function onScroll() {
    var y = scroller ? scroller.scrollTop : (window.scrollY || 0);
    if (y > 10) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  (scroller || window).addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
