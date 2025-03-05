// search bar javascript
const toggleSearch = () => {
    const searchForm = document.querySelector('.search-form');
    const searchInput = document.querySelector('.search-input');
    const searchButton = document.querySelector('.search-button');
    searchButton.addEventListener('click', () => {
        searchForm.classList.toggle('active-search');
    });
    searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'enter') {
            e.preventDefault();
            searchInput.value = '';
            searchForm.classList.remove('active-search');
        }
    });
};
toggleSearch();

// add book upload img javascript
function display() {
    let profilepic = document.getElementById("book-pic");
    let inputfile = document.getElementById("input-image");
    
    inputfile.onchange = function () {
        profilepic.src = URL.createObjectURL(inputfile.files[0]);
    }    
}

