fetch('http://127.0.0.1:5000/HeadersInfo', {
    method: 'GET',  
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => {return response.json();})
.then(data => {

    let currentLanguage = "tr"; // Başlangıç dili Türkçe
    const content = {
        tr: {
            main_name: data.main_name_tr,
            description_first: data.description_first_tr,
            description_second: data.description_second_tr
        },
        eng: {
            main_name: data.main_name_eng,
            description_first: data.description_first_eng,
            description_second: data.description_second_eng
        }
    };

    const linkedinUrl = data.linkedin;
    const steamUrl = data.steam;
    const youtubeUrl = data.youtube;

    document.getElementById('linkedin-link').href = linkedinUrl;
    document.getElementById('steam-link').href = steamUrl;
    document.getElementById('youtube-link').href = youtubeUrl;

    document.getElementById('main-name').textContent = content.tr.main_name;
    document.getElementById('description-first').textContent = content.tr.description_first;
    document.getElementById('description-second').textContent = content.tr.description_second;

    document.getElementById('language-toggle').addEventListener("click", function () {
        currentLanguage = currentLanguage === "tr" ? "eng" : "tr"; 

        document.getElementById('main-name').textContent = content[currentLanguage].main_name;
        document.getElementById('description-first').textContent = content[currentLanguage].description_first;
        document.getElementById('description-second').textContent = content[currentLanguage].description_second;
    });

    document.getElementById('loading').style.display = 'none';

})
.catch(error => {
    document.getElementById('loader').style.display = 'none';
    document.getElementById('loader-error').style.display = 'block';
});