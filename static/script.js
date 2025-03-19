fetch('http://127.0.0.1:5000/HeadersInfo', {
    method: 'GET',  
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => {return response.json();})
.then(data => {

    const linkedinUrl = data.linkedin;
    const steamUrl = data.steam;
    const youtubeUrl = data.youtube;
    const main_name = data.main_name;
    const description_first = data.description_first;
    const description_second = data. description_second

    document.getElementById('main-name').textContent = main_name;
    document.getElementById('description-first').textContent = description_first;
    document.getElementById('description-second').textContent = description_second;
    document.getElementById('linkedin-link').href = linkedinUrl;
    document.getElementById('steam-link').href = steamUrl;
    document.getElementById('youtube-link').href = youtubeUrl;

})
.catch(error => {
    console.error('Veri çekme hatası:', error);
});