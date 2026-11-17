
document.addEventListener("DOMContentLoaded", function () {
    const searchInputs = [
        document.querySelector("#articleSearch"),
        document.querySelector("#navbarSearch")
    ].filter(Boolean);

    const articleCards = document.querySelectorAll("[data-searchable]");

    if (searchInputs.length === 0) {
        return;
    }

    const urlParams = new URLSearchParams(window.location.search);
    const initialQuery = urlParams.get("q") || "";

    searchInputs.forEach(function (input) {
        input.value = initialQuery;
    });

    function filterArticles(searchText) {
        const query = searchText.toLowerCase().trim();

        articleCards.forEach(function (card) {
            const articleText = card.textContent.toLowerCase();

            card.style.display = articleText.includes(query) ? "" : "none";
        });
    }

    searchInputs.forEach(function (input) {
        input.addEventListener("input", function () {
            searchInputs.forEach(function (otherInput) {
                otherInput.value = input.value;
            });

            filterArticles(input.value);
        });
    });

    filterArticles(initialQuery);
});
