
// ========================================
// 1. SMOOTH SCROLLING
// ========================================

document.addEventListener("DOMContentLoaded", function () {

    // Select all links that start with #
    const anchorLinks = document.querySelectorAll('a[href^="#"]');

    // Add a click event to each link
    anchorLinks.forEach(function (link) {

        link.addEventListener("click", function (event) {

            const targetId = link.getAttribute("href");

            // Ignore empty links such as href="#"
            if (targetId === "#") {
                return;
            }

            // Find the target section
            const targetSection = document.querySelector(targetId);

            // Scroll if the section exists
            if (targetSection) {
                event.preventDefault();

                targetSection.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }

        });

    });

});
