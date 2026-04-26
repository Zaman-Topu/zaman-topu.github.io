// Blog Page JavaScript

// Language Toggle
let currentLang = "en"; // Start with English (cards already have correct defaults in HTML)

const langToggle = document.getElementById("langToggle");
const langText = document.getElementById("langText");

function switchLanguage() {
  currentLang = currentLang === "en" ? "bn" : "en";

  // Update toggle button text
  langText.textContent = currentLang === "en" ? "বাংলা" : "English";

  // Update all elements with data attributes
  document.querySelectorAll("[data-en], [data-bn]").forEach((element) => {
    const text = element.getAttribute(`data-${currentLang}`);
    if (text) {
      if (element.tagName === "INPUT") {
        element.placeholder = text;
      } else {
        element.textContent = text;
      }
    }
  });

  // Update placeholder for search
  const searchInput = document.getElementById("searchInput");
  const placeholder = searchInput.getAttribute(
    `data-placeholder-${currentLang}`,
  );
  if (placeholder) {
    searchInput.placeholder = placeholder;
  }

  // Toggle Bangla font class on body
  if (currentLang === "bn") {
    document.body.classList.add("bangla-mode");
  } else {
    document.body.classList.remove("bangla-mode");
  }
}

langToggle.addEventListener("click", switchLanguage);

// Don't auto-switch on load - let cards show their default language from HTML

// Category Filter
const filterTags = document.querySelectorAll(".filter-tag");
const blogCards = document.querySelectorAll(".blog-card");
const emptyState = document.getElementById("emptyState");

filterTags.forEach((tag) => {
  tag.addEventListener("click", () => {
    // Remove active class from all tags
    filterTags.forEach((t) => t.classList.remove("active"));

    // Add active class to clicked tag
    tag.classList.add("active");

    const category = tag.getAttribute("data-category");
    filterCards(category);
  });
});

function filterCards(category) {
  let visibleCount = 0;

  blogCards.forEach((card) => {
    const cardCategory = card.getAttribute("data-category");

    if (category === "all" || cardCategory === category) {
      card.style.display = "flex";
      visibleCount++;
    } else {
      card.style.display = "none";
    }
  });

  // Show/hide empty state
  if (visibleCount === 0) {
    emptyState.style.display = "block";
    document.querySelector(".blog-grid").style.display = "none";
  } else {
    emptyState.style.display = "none";
    document.querySelector(".blog-grid").style.display = "grid";
  }
}

// Search Functionality
const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("input", (e) => {
  const searchTerm = e.target.value.toLowerCase();
  let visibleCount = 0;

  blogCards.forEach((card) => {
    const title = card
      .querySelector(".blog-card-title")
      .textContent.toLowerCase();
    const excerpt = card
      .querySelector(".blog-card-excerpt")
      .textContent.toLowerCase();
    const category = card
      .querySelector(".category-badge")
      .textContent.toLowerCase();

    // Get active filter category
    const activeFilter = document
      .querySelector(".filter-tag.active")
      .getAttribute("data-category");
    const cardCategory = card.getAttribute("data-category");

    // Check if matches search and filter
    const matchesSearch =
      title.includes(searchTerm) ||
      excerpt.includes(searchTerm) ||
      category.includes(searchTerm);
    const matchesFilter =
      activeFilter === "all" || cardCategory === activeFilter;

    if (matchesSearch && matchesFilter) {
      card.style.display = "flex";
      visibleCount++;
    } else {
      card.style.display = "none";
    }
  });

  // Show/hide empty state
  if (visibleCount === 0) {
    emptyState.style.display = "block";
    document.querySelector(".blog-grid").style.display = "none";
  } else {
    emptyState.style.display = "none";
    document.querySelector(".blog-grid").style.display = "grid";
  }
});

// Smooth scroll for internal links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  });
});

// Add entrance animation on load
window.addEventListener("load", () => {
  const cards = document.querySelectorAll(".blog-card");
  cards.forEach((card, index) => {
    setTimeout(() => {
      card.style.opacity = "0";
      card.style.transform = "translateY(30px)";
      card.style.transition = "all 0.6s cubic-bezier(0.25, 0.8, 0.25, 1)";

      setTimeout(() => {
        card.style.opacity = "1";
        card.style.transform = "translateY(0)";
      }, 50);
    }, index * 100);
  });
});
