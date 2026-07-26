FROM python:3.10-slim

# System dependencies, FFmpeg, Fontconfig এবং সঠিক বাংলা/ইংরেজি ফন্ট ইনস্টল
RUN apt-get update && apt-get install -y \
    ffmpeg \
    fontconfig \
    fonts-freefont-ttf \
    fonts-noto-ui-core \
    fonts-beng-extra \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}
