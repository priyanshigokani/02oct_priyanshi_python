const toggleSearch = () => {
    const searchForm = document.querySelector('.search-form');
    const searchInput = document.querySelector('.search-input');
    const searchButton = document.querySelector('.search-button');

    // Toggle search bar visibility when clicking the search button
    searchButton.addEventListener('click', (event) => {
        event.preventDefault();
        event.stopPropagation(); // Prevent unwanted bubbling
        searchForm.classList.toggle('active-search');
        searchInput.focus(); // Auto-focus on input when opened
    });

    // Handle form submission properly
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            searchForm.submit(); // ✅ Ensure form submits
        }
    });

    // Close search bar when clicking outside
    document.addEventListener('click', (event) => {
        if (!searchForm.contains(event.target) && !searchButton.contains(event.target)) {
            searchForm.classList.remove('active-search');
        }
    });

    // Ensure search input keeps previous value after searching
    document.addEventListener("DOMContentLoaded", () => {
        if (searchInput.value.trim() !== "") {
            searchForm.classList.add("active-search"); // Keep search bar open if there's a query
        }
    });
};

// Initialize function
toggleSearch();


// add book upload img javascript
function display() {
    let profilepic = document.getElementById("book-pic");
    let inputfile = document.getElementById("input-image");
    
    inputfile.onchange = function () {
        profilepic.src = URL.createObjectURL(inputfile.files[0]);
    }    
}

