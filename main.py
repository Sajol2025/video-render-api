import subprocess
from fastapi import FastAPI

app = FastAPI()

# Render Health Check (HEAD method)
@app.head("/")
def head_root():
    return {"status": "ok"}

# Base Route
@app.get("/")
def read_root():
    return {"message": "Video Render API with FFmpeg & Fonts is Live!"}

# (Sample) Video Edit Route - বাংলা ও ইংরেজি টেক্সট ব্যবহারের ফন্ট পাথ দেওয়া আছে
@app.post("/render")
def render_video():
    # বাংলা ফন্টের পাথ: /usr/share/fonts/truetype/noto/NotoSansBengali-Regular.ttf
    # ফ্রি ফন্টের পাথ: /usr/share/fonts/truetype/freefont/FreeSans.ttf
    
    return {
        "status": "ready",
        "bengali_font_path": "/usr/share/fonts/truetype/noto/NotoSansBengali-Regular.ttf",
        "english_font_path": "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
    }
