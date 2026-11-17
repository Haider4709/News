
document.addEventListener("DOMContentLoaded", function () {

    // Get the comment textarea and character counter
    const commentInput = document.querySelector("#commentBody");
    const characterCount = document.querySelector("#characterCount");

    // Stop if these elements do not exist
    if (!commentInput || !characterCount) {
        return;
    }

    // Update the character count
    function updateCharacterCount() {

        const currentLength = commentInput.value.length;

        characterCount.textContent = currentLength + " characters";

    }

    // Run when the user types
    commentInput.addEventListener("input", updateCharacterCount);

    // Display the initial count
    updateCharacterCount();

});
