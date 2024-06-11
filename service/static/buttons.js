// var ct = document.getElementById("CODE_TEXT_SAMPLE");
function changeLanguage() {
    var lang = document.getElementById("coding_language");
    c = document.getElementById("printed_code");
    c.className = '';
    // c.innerHTML = ct.innerHTML;
    c.classList.add(lang.value);
    // c.style = "background-color: red;";
    Prism.highlightElement(c);
}