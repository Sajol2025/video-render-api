FROM python:3.10-slim

# System dependencies & FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# python -m uvicorn ব্যবহার করলে uvicorn not found এরর আর আসবে না
CMD python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}
