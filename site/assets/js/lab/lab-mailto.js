/*! mailto: — copy address + toast; on touch also allow the native mail app. */
(function () {
  /* Toast prefix follows the page language (html lang is a Locale such as
     zh-Hans / en-US); the address itself is always shown verbatim. */
  function copiedLabel() {
    var lang = (document.documentElement.getAttribute("lang") || "").toLowerCase();
    return lang.indexOf("en") === 0 ? "Email copied: " : "已复制邮箱：";
  }

  /* Distinguish failure from success — showing the bare address made the
     toast read as "copied" even when the clipboard write was rejected. */
  function copyFailedLabel() {
    var lang = (document.documentElement.getAttribute("lang") || "").toLowerCase();
    return lang.indexOf("en") === 0 ? "Copy failed, please copy manually: " : "复制失败，请手动复制：";
  }

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

  function isCoarsePointer() {
    try {
      return window.matchMedia("(pointer: coarse)").matches;
    } catch (_) {
      return "ontouchstart" in window;
    }
  }

  document.addEventListener(
    "click",
    function (e) {
      var a = e.target && e.target.closest ? e.target.closest('a[href^="mailto:"]') : null;
      if (!a) return;
      var email = emailFromHref(a.getAttribute("href") || "");
      if (!email) return;

      // Phones/tablets: let mailto: open the mail app; still copy as a convenience.
      // Fine pointers (desktop): Windows often has no client — copy only.
      if (!isCoarsePointer()) {
        e.preventDefault();
      }

      copyText(email)
        .then(function () {
          showToast(copiedLabel() + email);
        })
        .catch(function () {
          showToast(copyFailedLabel() + email);
        });
    },
    true
  );
})();
