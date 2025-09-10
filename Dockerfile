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

# Create writable directory
RUN mkdir -p /app/writable

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