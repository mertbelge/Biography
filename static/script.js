document.addEventListener("DOMContentLoaded", function() {
    fetch("http://127.0.0.1:5000/HeadersInfo")
        .then(response => response.json())
        .then(data => {
            document.getElementById("main_name").innerText = data.main_name;
            document.getElementById("description").innerText = data.description_first;
        })
        .catch(error => console.error("Hata:", error));
});
