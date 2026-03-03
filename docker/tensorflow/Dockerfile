# Use official Python image
FROM python:3.11-slim

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install TensorFlow
RUN pip install tensorflow

# Copy project files (optional)
COPY . .

# Default command
CMD ["python3"]

#  -- BUILD COPYPASTE -- 
# docker build -t tf-env ./tensorflow

