FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=signbank.settings.docker

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ffmpeg \
        sqlite3 \
        git \
        libmagic1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create necessary directories
RUN mkdir -p /app/writable/database \
    && mkdir -p /app/writable/media \
    && mkdir -p /app/writable/static \
    && mkdir -p /app/writable/upload \
    && mkdir -p /app/writable/glossvideo \
    && mkdir -p /app/writable/sensevideo \
    && mkdir -p /app/writable/annotatedvideo \
    && mkdir -p /app/writable/glossimage \
    && mkdir -p /app/writable/comments \
    && mkdir -p /app/writable/handshapeimage \
    && mkdir -p /app/writable/othermedia \
    && mkdir -p /app/writable/import_images \
    && mkdir -p /app/writable/import_videos \
    && mkdir -p /app/writable/api_video_archives \
    && mkdir -p /app/writable/import_other_media \
    && mkdir -p /app/writable/packages \
    && mkdir -p /app/writable/eaf \
    && mkdir -p /app/writable/eafs \
    && mkdir -p /app/writable/metadata_eafs \
    && mkdir -p /app/writable/test_data \
    && mkdir -p /app/writable/video_backups \
    && mkdir -p /app/writable/prullenmand \
    && mkdir -p /app/writable/ecv \
    && mkdir -p /app/writable/attachments

# Make the develop script executable
RUN chmod +x /app/bin/develop.py

# Copy and make entrypoint executable
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

# Expose port
EXPOSE 8000

# Run the application
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python", "bin/develop.py", "runserver", "0.0.0.0:8000"]