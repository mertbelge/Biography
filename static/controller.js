
export function get_API_IP(){
 return fetch("static/config.json")
    .then(response => {
        if (!response.ok) {
            document.getElementById('loader').style.display = 'none';
            document.getElementById('loader-error').style.display = 'block';
        }
        return response.json();
    })
    .then(config => {return config.API_IP})
    .catch(error => {
        document.getElementById('loader').style.display = 'none';
        document.getElementById('loader-error').style.display = 'block';
    })
    };
