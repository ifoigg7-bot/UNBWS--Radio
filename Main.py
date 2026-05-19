from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os
import random
from glob import glob

app = FastAPI()

# Находим все MP3 файлы в папке mp3
music_files = glob("mp3/*.mp3")

# Простая HTML страница с видео-плеером
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My Radio</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #0a0a0a; color: white; }
        video { width: 80%; border-radius: 12px; margin-top: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.5); }
        h1 { color: #ff0000; }
    </style>
</head>
<body>
    <h1>🎵 MY RADIO 24/7 🎵</h1>
    <video controls autoplay>
        <source src="/stream" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <p>Радио работает 24/7 с вашей музыкой и вашей картинкой</p>
</body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(content=html_content)

@app.get("/stream")
async def video_stream():
    # Путь к видеофайлу
    video_path = "video.mp4"
    if os.path.exists(video_path):
        return FileResponse(video_path, media_type="video/mp4")
    return {"error": "Video file not found. Please upload video.mp4"}
