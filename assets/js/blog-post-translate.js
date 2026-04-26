// Blog Post Language Toggle Script

document.addEventListener("DOMContentLoaded", function () {
  const langToggle = document.getElementById("langTogglePost");
  const langText = document.getElementById("langTextPost");
  const body = document.body;

  // Default language is Bangla (since body has bangla-mode class)
  let currentLang = "bn";

  if (langToggle) {
    langToggle.addEventListener("click", function () {
      // Toggle language
      if (currentLang === "bn") {
        currentLang = "en";
        body.classList.remove("bangla-mode");
        langText.textContent = "বাংলা";

        // Switch all elements to English
        switchLanguage("en");
      } else {
        currentLang = "bn";
        body.classList.add("bangla-mode");
        langText.textContent = "English";

        // Switch all elements to Bangla
        switchLanguage("bn");
      }
    });
  }

  function switchLanguage(lang) {
    // Find all elements with data-bn and data-en attributes
    const elements = document.querySelectorAll("[data-bn][data-en]");

    elements.forEach((element) => {
      const bnText = element.getAttribute("data-bn");
      const enText = element.getAttribute("data-en");

      if (lang === "bn" && bnText) {
        element.textContent = bnText;
      } else if (lang === "en" && enText) {
        element.textContent = enText;
      }
    });
  }
});
