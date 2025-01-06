# YTDownloader

YTDownloader is a responsive web application built with Django that allows users to download YouTube videos easily. The page provides an intuitive interface for searching videos and downloading them in various formats.

# Problems

Although it is working, it can only download the video without audio. I couldn't get it to download the video with the audio embedded together, nor could I download the audio separately.

## Features
- **Video Downloads**: Allows users to download YouTube videos in different resolutions and formats.
- **Intuitive Interface**: Clean and easy-to-use design to quickly find and download videos.
- **Responsive**: The page is mobile-friendly and adapts to desktops, tablets, and smartphones.

## Technologies Used
- **HTML5**: Basic structure of the web page.
- **CSS**: Styles and layout of the user interface.
- **JavaScript**: Functionality for video search and managing downloads.
- **Django**: Framework used for the back-end structure and server-side logic.

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
       
5. Install yt-dlp:
   
     Allow download of videos and audio.
   
     ```bash
     pip install yt-dlp
   
7. Run the development server
     ```bash
     python manage.py runserver

   
## Author

- **Matías Araya Olivares** - *Lead Programmer and Designer* - [Kumati63](https://github.com/Kumati63)
