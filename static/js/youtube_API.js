// verify if the "Search" button was clicked
document.getElementById('sf_submit').addEventListener('click', fetchVideoDetails);

// Function to fetch the details of the video searched
function fetchVideoDetails() {
    // Get the url of the video
    const url = document.getElementById('sf_url').value;
    // Send the url to the function 'extractVideoId' to get the unique id of the video
    const videoId = extractVideoId(url);

    // If there is no unique id it does not enter
    if (videoId) {

        const apiUrl = `https://www.googleapis.com/youtube/v3/videos?id=${videoId}&key=AIzaSyB6h_fsk-mfiyHkDWmyVQoU-XKOhutLAl0&part=snippet,contentDetails`;

        // fetch the video details
        fetch(apiUrl)
            // Give the response in a json format
            .then(response => response.json())
            .then(data => {
                if (data.items.length > 0) {
                    const videoData = data.items[0];
                    const title = videoData.snippet.title;
                    const duration = videoData.contentDetails.duration;
                    const thumbnailUrl = videoData.snippet.thumbnails.high.url;

                    document.getElementById('video-title').textContent = title;
                    document.getElementById('video-thumbnail').src = thumbnailUrl;

                    // Show details of the video
                    document.getElementById('video-info').style.display = 'block';
                } else {
                    alert('Video not found.');
                }
            })
            .catch(error => {
                console.error('Error fetching video details:', error);
                alert('Error fetching the video details.');
            });
    } else {
        alert('Please, put a valid URL.');
    }
}

// Function to extract the unique id of the video
function extractVideoId(url) {
    const regex = /(?:https?:\/\/(?:www\.)?youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)([a-zA-Z0-9_-]{11}))|(?:https?:\/\/youtu\.be\/([a-zA-Z0-9_-]{11}))$/;
    const match = url.match(regex);
    return match ? (match[1] || match[2]) : null;
}
