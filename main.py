import os
import subprocess
import uuid
import shlex
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse

app = FastAPI()

UPLOAD_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"status": "Dynamic FFmpeg Video Engine Ready"}

@app.post("/render")
async def render_dynamic_video(
    image1: UploadFile = File(None),
    image2: UploadFile = File(None),
    audio: UploadFile = File(None),
    ffmpeg_cmd: str = Form(...)  # n8n থেকে পুরো FFmpeg কমান্ড আসবে
):
    job_id = str(uuid.uuid4())[:8]
    saved_files = {}

    # ইনপুট ফাইলগুলো সেভ করা (যদি পাঠানো হয়)
    if image1:
        path = f"temp_{job_id}_img1_{image1.filename}"
        with open(path, "wb") as f: f.write(await image1.read())
        saved_files["{image1}"] = path

    if image2:
        path = f"temp_{job_id}_img2_{image2.filename}"
        with open(path, "wb") as f: f.write(await image2.read())
        saved_files["{image2}"] = path

    if audio:
        path = f"temp_{job_id}_audio_{audio.filename}"
        with open(path, "wb") as f: f.write(await audio.read())
        saved_files["{audio}"] = path

    output_path = os.path.join(UPLOAD_DIR, f"output_{job_id}.mp4")

    # n8n থেকে আসা কমান্ডের ভেতরের প্লেসহোল্ডার যেমন {image1}, {audio} আসল ফাইল পাথে রিপ্লেস করা
    final_cmd = ffmpeg_cmd
    for placeholder, file_path in saved_files.items():
        final_cmd = final_cmd.replace(placeholder, file_path)
    
    final_cmd = final_cmd.replace("{output}", output_path)

    # কমান্ড রান করা
    try:
        # shlex.split দিয়ে কমান্ড নিরাপদভাবে পার্স করা
        cmd_args = shlex.split(final_cmd)
        subprocess.run(cmd_args, check=True)
    finally:
        # সাময়িক সোর্স ফাইল মুছে ফেলা
        for p in saved_files.values():
            if os.path.exists(p): os.remove(p)

    return FileResponse(output_path, media_type="video/mp4", filename=f"video_{job_id}.mp4")
