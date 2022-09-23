const activePage = window.location.pathname;
const allLi = document.querySelectorAll(".nav-link")
var span
allLi.forEach(element => {
    span = element.getElementsByTagName("span")[0].innerText.toLowerCase()
    if (activePage.includes(span)) {
        element.classList.add("active")
    }
});