from flask import Flask, request, render_template, send_file
import os
import subprocess
import yt_dlp

app = Flask(__name__)

# Directories for file handling
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return "No file uploaded", 400
    
    video_file = os.path.join(UPLOAD_DIR, file.filename)
    file.save(video_file)

    # Convert and return the MP3 file
    return send_file(convert_to_mp3(video_file), as_attachment=True)

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    if not url:
        return "No URL provided", 400
    
    options = {
        "outtmpl": os.path.join(UPLOAD_DIR, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4"
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info)

    return send_file(convert_to_mp3(video_path), as_attachment=True)

def convert_to_mp3(video_path):
    """Convert a video file to MP3 using FFmpeg."""
    mp3_file = os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(video_path))[0] + ".mp3")
    subprocess.run(["ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", mp3_file], check=True)
    return mp3_file

if __name__ == "__main__":
    app.run(debug=True)
