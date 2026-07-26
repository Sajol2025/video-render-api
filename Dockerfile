FROM python:3.10-slim

# System dependencies, FFmpeg, Fontconfig এবং প্রয়োজনীয় ফন্ট ইনস্টল
RUN apt-get update && apt-get install -y \
    ffmpeg \
    fontconfig \
    fonts-freefont-ttf \
    fonts-noto-bench-bengali \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render Dynamic PORT অনুযায়ী Server রান করবে
CMD python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}
