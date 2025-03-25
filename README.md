# MP4 to MP3 Converter (Local Web App)  

A simple **web application** that allows you to:  
Upload **MP4 files** and convert them to **MP3**  
Paste **YouTube URLs** to extract and download audio as MP3  

##  Features  
- **Local Web Interface** (Runs on your PC)  
- **MP4 Upload & Conversion**  
- **YouTube URL Support** (via `yt-dlp`)  
- **Fast Audio Extraction** (using `FFmpeg`)  

---

## Installation  

### 1 - Install Python 
- Download & install Python 
- Make sure `pip` is installed (`python -m ensurepip`)  

### 2 - Install Dependencies  
Open a terminal and run:  
pip install flask ffmpeg-python yt-dlp

### 3 - Install FFmpeg

Download from ffmpeg.org and add to your PATH

## How to run 
- Open a terminal in the project folder
- Run the app with: python app.py
- Go to your browser and open: http://127.0.0.1:5000/
