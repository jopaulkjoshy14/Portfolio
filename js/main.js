// =========================================================
// JOPAUL K JOSHY — PORTFOLIO INTERACTIONS
// =========================================================

document.addEventListener("DOMContentLoaded", () => {

  const header = document.querySelector(".site-header");
  const nav = document.querySelector(".nav");
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelectorAll('.nav a[href^="#"]');
  const sections = document.querySelectorAll("main section[id]");


  // -------------------------------------------------------
  // Mobile navigation
  // -------------------------------------------------------

  if (menuToggle && nav) {
    menuToggle.addEventListener("click", () => {
      const isOpen = nav.classList.toggle("open");

      menuToggle.setAttribute("aria-expanded", String(isOpen));
    });

    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        nav.classList.remove("open");
        menuToggle.setAttribute("aria-expanded", "false");
      });
    });
  }


  // -------------------------------------------------------
  // Smooth scrolling with sticky-header offset
  // -------------------------------------------------------

  navLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      const targetId = link.getAttribute("href");

      if (!targetId || targetId === "#") return;

      const target = document.querySelector(targetId);

      if (!target) return;

      event.preventDefault();

      const headerHeight = header ? header.offsetHeight : 0;
      const targetPosition =
        target.getBoundingClientRect().top +
        window.scrollY -
        headerHeight -
        20;

      window.scrollTo({
        top: targetPosition,
        behavior: "smooth"
      });
    });
  });


  // -------------------------------------------------------
  // Active navigation link
  // -------------------------------------------------------

  const updateActiveLink = () => {
    const scrollPosition = window.scrollY + 160;

    let currentSection = "";

    sections.forEach((section) => {
      if (scrollPosition >= section.offsetTop) {
        currentSection = section.id;
      }
    });

    navLinks.forEach((link) => {
      const targetId = link.getAttribute("href").slice(1);

      link.classList.toggle(
        "active",
        targetId === currentSection
      );
    });
  };

  window.addEventListener("scroll", updateActiveLink, {
    passive: true
  });

  updateActiveLink();

});
