# YTDownloader
YTDownloader is a responsive web application built with Django that allows users to download YouTube videos easily. The page provides an intuitive interface for searching videos and downloading them in various formats.

# Current Limitation
At the moment, this tool can only download either the video without audio or the audio alone. My goal is to eventually enable the ability to download the video with the audio embedded together. I hope to implement this feature in the future.

## Features
- **Video Downloads**: Allows users to download YouTube videos in different resolutions and formats (144p, 240p, 360p, 720p, 1080p).
- **Audio Downloads**: Enables users to download the audio from the videos.
- **Intuitive Interface**: Clean and easy-to-use design to quickly find and download videos.
- **Responsive Design**: The page is mobile-friendly and adapts to desktops, tablets, and smartphones.
- **Error Handling**: Provides helpful error messages in case of invalid URLs or unavailable video formats.

## Technologies Used
- **Django**: Web framework used for the back-end structure and server-side logic.
- **HTML5**: Basic structure of the web page.
- **CSS**: Styles and layout of the user interface.
- **JavaScript**: Manages the functionality for video search and controlling the download process.
- **Bootstrap**: A front-end framework used to create a responsive and modern user interface.
- **yt-dlp**: A powerful command-line tool for downloading videos from various websites (including YouTube) and extracting the audio or video. Find more about it [here](https://github.com/yt-dlp/yt-dlp)


## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:
   
    ```bash
   git clone https://github.com/Kumati63/YTDownloader.git
   
2. Navigate to the project folder:
    ```bash
    cd YTDownloader

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
   
4. Activate the virtual environment
   
      On Windows:
  
       venv\Scripts\activate
       
      On macOS/Linux:
  
       source venv/bin/activate
       
5. Install requirements:
   
     ```bash
     pip install -r requirements.txt
     
6. Update yt-dlp to ensure it doesn't break anything:
     
     ```bash
     pip install --upgrade yt-dlp       
   
7. Run the development server
     ```bash
     python manage.py runserver
     
Once the server is running, you can access the app in your web browser at http://127.0.0.1:8000/


## Author

- **Matías Araya Olivares** - *Lead Programmer and Designer* - [Kumati63](https://github.com/Kumati63)

## Future Features

- **Audio and Video Merging**: Integrating a feature to combine video and audio into a single file.
- **Multiple Video Downloads**: Allowing the user to download multiple videos simultaneously.
- **Support for More Platforms**: Expanding support to download videos and audio from more platforms beyond YouTube (e.g., Twitter, Twitch, etc.).
