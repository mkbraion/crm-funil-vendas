FROM python:3.12-slim

# ffmpeg é usado pelo yt-dlp quando precisa juntar vídeo + áudio.
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8000
EXPOSE 8000

# 2 workers, timeout alto porque baixar vídeo pode demorar.
CMD gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 180 app:app
