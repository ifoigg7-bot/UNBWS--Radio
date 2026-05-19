from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My Radio</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #0a0a0a; color: white; }
        video { width: 80%; border-radius: 12px; margin-top: 20px; }
        h1 { color: #ff0000; }
    </style>
</head>
<body>
    <h1>🎵 MY RADIO 24/7 🎵</h1>
    <video controls autoplay loop>
        <source src="/video.mp4" type="video/mp4">
        Ваш браузер не поддерживает видео
    </video>
</body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(content=html_content)

@app.get("/video.mp4")
async def get_video():
    if os.path.exists("video.mp4"):
        return FileResponse("video.mp4")
    return {"error": "video.mp4 not found"}
