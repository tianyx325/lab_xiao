/*! Click mailto: → copy address + toast (Windows often has no mail client). */
(function () {
  function emailFromHref(href) {
    if (!href || href.indexOf("mailto:") !== 0) return "";
    try {
      return decodeURIComponent(href.replace(/^mailto:/i, "").split("?")[0].trim());
    } catch (_) {
      return href.replace(/^mailto:/i, "").split("?")[0].trim();
    }
  }

  function showToast(text) {
    var el = document.getElementById("lab-mailto-toast");
    if (!el) {
      el = document.createElement("div");
      el.id = "lab-mailto-toast";
      el.className = "lab-mailto-toast";
      el.setAttribute("role", "status");
      document.body.appendChild(el);
    }
    el.textContent = text;
    el.classList.add("is-visible");
    clearTimeout(showToast._t);
    showToast._t = setTimeout(function () {
      el.classList.remove("is-visible");
    }, 2200);
  }

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.left = "-9999px";
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand("copy") ? resolve() : reject();
      } catch (err) {
        reject(err);
      } finally {
        document.body.removeChild(ta);
      }
    });
  }

  document.addEventListener(
    "click",
    function (e) {
      var a = e.target && e.target.closest ? e.target.closest('a[href^="mailto:"]') : null;
      if (!a) return;
      var email = emailFromHref(a.getAttribute("href") || "");
      if (!email) return;

      e.preventDefault();
      copyText(email)
        .then(function () {
          showToast("已复制邮箱：" + email);
        })
        .catch(function () {
          showToast(email);
        });
    },
    true
  );
})();
