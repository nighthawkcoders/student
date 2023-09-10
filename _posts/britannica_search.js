function searchBritannica() {
    // Get the search query from the input field
    const query = document.getElementById('searchQuery').value;

    // Construct the Britannica search URL
    const britannicaURL = `https://www.britannica.com/search?query=${encodeURIComponent(query)}`;

    // Open a new tab/window with the Britannica search results
    window.open(britannicaURL, '_blank');
}
