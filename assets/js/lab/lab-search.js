/*! Search feedback: skeleton while the index/engine loads, a friendly
    error with retry, and next-step actions on zero results. The vendor
    Fuse search remains the engine; this only owns the surrounding states. */
(function () {
  var hits = document.getElementById("search-hits");
  if (!hits) return;

  var data = hits.dataset;
  var timer = 0;

  function clearTimer() {
    clearTimeout(timer);
    hits.setAttribute("aria-busy", "false");
  }

  function skeleton() {
    if (hits.querySelector(".search-hit") || hits.querySelector(".search-no-results")) return;
    hits.setAttribute("aria-busy", "true");
    hits.innerHTML =
      '<div class="lab-search-skeleton" role="status">' +
      '<span class="sr-only">' + data.loading + "</span>" +
      '<span class="bar"></span><span class="bar"></span><span class="bar"></span>' +
      "</div>";
    clearTimeout(timer);
    timer = setTimeout(function () {
      if (hits.querySelector(".lab-search-skeleton")) showError();
    }, 6000);
  }

  function showError() {
    hits.setAttribute("aria-busy", "false");
    hits.innerHTML =
      '<div class="lab-search-error" role="alert"><p>' +
      data.error +
      '</p><button type="button" class="lab-search-retry">' +
      data.retry +
      "</button></div>";
  }

  document.addEventListener("click", function (e) {
    if (e.target.closest(".lab-search-close")) return;
    if (!e.target.closest(".js-search")) return;
    setTimeout(skeleton, 0);
  });

  hits.addEventListener("click", function (e) {
    if (e.target.closest(".lab-search-retry")) window.location.reload();
  });

  new MutationObserver(function () {
    if (hits.querySelector(".search-hit")) clearTimer();

    var empty = hits.querySelector(".search-no-results");
    if (empty && !empty.querySelector(".lab-search-empty-actions")) {
      empty.insertAdjacentHTML(
        "beforeend",
        '<div class="lab-search-empty-actions"><a href="' +
          data.browse +
          '">' +
          data.browseLabel +
          '</a><a href="' +
          data.contact +
          '">' +
          data.contactLabel +
          "</a></div>",
      );
      clearTimer();
    }
  }).observe(hits, { childList: true, subtree: true });
})();