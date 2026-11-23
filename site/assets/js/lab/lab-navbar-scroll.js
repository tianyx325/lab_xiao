/*! Navbar scroll convergence + mobile drawer sync */
(function () {
  var header = document.querySelector('.page-header.header--fixed');
  if (!header) return;

  var pane = document.querySelector('.page-body');
  var scroller = null;
  if (pane) {
    var overflow = window.getComputedStyle(pane).overflowY;
    if (overflow === 'auto' || overflow === 'scroll') scroller = pane;
  }

  function onScroll() {
    var y = scroller ? scroller.scrollTop : (window.scrollY || 0);
    header.classList.toggle('scrolled', y > 0);
  }

  (scroller || window).addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  var content = document.getElementById('navbar-content');
  if (content) {
    var syncNavOpen = function () {
      document.body.classList.toggle('lab-nav-open', content.classList.contains('show'));
    };
    ['shown.bs.collapse', 'hidden.bs.collapse'].forEach(function (type) {
      content.addEventListener(type, syncNavOpen);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape' || !content.classList.contains('show')) return;
      var toggler = document.querySelector('#navbar-main .navbar-toggler[aria-expanded="true"]');
      if (toggler) {
        toggler.click();
        toggler.focus();
      }
    });
  }
})();
