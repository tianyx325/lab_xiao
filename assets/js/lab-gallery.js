(() => {
  const roots = document.querySelectorAll("[data-lab-gallery-root]");
  if (!roots.length) return;

  roots.forEach((root) => {
    const viewport = root.querySelector("[data-lab-gallery-viewport]");
    const track = root.querySelector(".lab-gallery-track");
    const prev = root.querySelector(".lab-gallery-prev");
    const next = root.querySelector(".lab-gallery-next");
    if (!viewport || !track) return;

    /* One click / key press advances by a full viewport page (3 visible items). */
    const pageSize = () => viewport.clientWidth;

    const syncButtons = () => {
      if (!prev || !next) return;
      const max = Math.max(0, viewport.scrollWidth - viewport.clientWidth - 1);
      prev.disabled = viewport.scrollLeft <= 1;
      next.disabled = viewport.scrollLeft >= max;
    };

    const scrollByDir = (dir) => {
      viewport.scrollBy({ left: dir * pageSize(), behavior: "smooth" });
    };

    prev?.addEventListener("click", () => scrollByDir(-1));
    next?.addEventListener("click", () => scrollByDir(1));
    viewport.addEventListener("scroll", () => syncButtons(), { passive: true });
    window.addEventListener("resize", () => syncButtons(), { passive: true });

    viewport.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        scrollByDir(-1);
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        scrollByDir(1);
      }
    });

    syncButtons();
  });
})();
