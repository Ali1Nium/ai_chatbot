# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Install system deps
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    netcat-openbsd \
    && apt-get clean

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django code
COPY . .
