document.getElementById('sf_submit').addEventListener('click', fetchMediaDetails);

function fetchMediaDetails() {
    const url = document.getElementById('sf_url').value;

    if (!url) {
        alert('Please, put a valid URL.');
        return;
    }

    // Mostrar el spinner de carga
    document.getElementById('loading-spinner').style.display = 'block';
    document.getElementById('media-info').style.display = 'none'; // Ocultar detalles mientras se carga

    // La URL de tu API Django
    const apiUrl = `/get_media_info/?url=${encodeURIComponent(url)}`;

    // Solicitar información sobre el video y audio
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            // Ocultar el spinner una vez se recibe la respuesta
            document.getElementById('loading-spinner').style.display = 'none';

            if (data.error) {
                alert(data.error);
            } else {
                // Mostrar el título y la miniatura
                document.getElementById('media-title').textContent = data.title;
                document.getElementById('media-thumbnail').src = data.thumbnail;

                // Mostrar las opciones de descarga de video
                const videoOptionsDiv = document.getElementById('video-options');
                const audioOptionsDiv = document.getElementById('audio-options');
                videoOptionsDiv.innerHTML = ''; // Limpiar las opciones anteriores
                audioOptionsDiv.innerHTML = '';

                // Crear los botones de descarga para video
                data.video_formats.forEach(format => {
                    const option = document.createElement('button');
                    option.textContent = `Download Video ${format.quality}`;
                    option.classList.add('btn', 'btn-primary', 'w-100', 'my-1');
                    option.onclick = function(event) {
                        event.preventDefault();
                        window.open(format.url, '_blank');
                    };
                    videoOptionsDiv.appendChild(option);
                });

                // Crear los botones de descarga para audio
                data.audio_formats.forEach(format => {
                    const option = document.createElement('button');
                    option.textContent = `Download Audio ${format.quality}`;
                    option.classList.add('btn', 'btn-secondary', 'w-100', 'my-1');
                    option.onclick = function(event) {
                        event.preventDefault();
                        window.open(format.url, '_blank');
                    };
                    audioOptionsDiv.appendChild(option);
                });

                // Mostrar la sección con los detalles del media
                document.getElementById('media-info').style.display = 'block';
            }
        })
        .catch(error => {
            console.error('Error fetching media details:', error);
            alert('Error fetching the media details.');
            document.getElementById('loading-spinner').style.display = 'none';
        });
}
