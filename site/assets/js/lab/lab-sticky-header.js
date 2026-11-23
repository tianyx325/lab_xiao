/*! Sticky list header: pins the title / filter band under the floating
    navbar, compresses it once stuck, and reports its height as
    --lab-sticky-h so in-list year heads stack below it instead of
    disappearing underneath. Zero deps. */
(function () {
  var el = document.querySelector('[data-lab-sticky]');
  if (!el) return;
  var root = document.documentElement;
  /* App-shell list pages scroll .page-body; otherwise the window scrolls. */
  var pane = document.querySelector('.page-body');
  var scrollRoot = null;
  if (pane) {
    var overflow = window.getComputedStyle(pane).overflowY;
    if (overflow === 'auto' || overflow === 'scroll') scrollRoot = pane;
  }

  /* 1px sentinel above the band; negative margin keeps the layout unchanged */
  var sentinel = document.createElement('div');
  sentinel.className = 'lab-sticky-sentinel';
  sentinel.setAttribute('aria-hidden', 'true');
  el.parentNode.insertBefore(sentinel, el);

  function setHeight() {
    root.style.setProperty(
      '--lab-sticky-h',
      (el.classList.contains('is-stuck') ? el.offsetHeight : 0) + 'px'
    );
  }

  var io = null;
  function createObserver() {
    var offset = 0;
    if (!scrollRoot) {
      /* Window scroll: stick under the body's top padding (navbar + gaps).
         Recomputed on resize — body padding flips 56px/48px navbar heights
         across the lg breakpoint (rotation, desktop window resize). */
      offset = parseFloat(window.getComputedStyle(document.body).paddingTop) || 0;
    }
    if (io) io.disconnect();
    io = new IntersectionObserver(function (entries) {
      var stuck = !entries[0].isIntersecting;
      if (stuck !== el.classList.contains('is-stuck')) {
        el.classList.toggle('is-stuck', stuck);
        setHeight();
      }
    }, {
      root: scrollRoot,
      rootMargin: '-' + Math.max(0, offset - 1) + 'px 0px 0px 0px',
      threshold: 0
    });
    io.observe(sentinel);
  }

  /* Resize fires in bursts; coalesce the layout reads into one frame */
  var raf = 0;
  function onResize() {
    if (raf) return;
    raf = window.requestAnimationFrame(function () {
      raf = 0;
      setHeight();
      createObserver();
    });
  }
  window.addEventListener('resize', onResize);
  setHeight();
  createObserver();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(setHeight);
})();
