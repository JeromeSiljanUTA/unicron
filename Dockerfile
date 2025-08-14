# Start from a slim Python base
FROM python:3.13-slim

# Install Emacs and other system deps
RUN apt-get update && apt-get install -y \
    emacs-nox \
    bash \
    git \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy your source code and scripts
COPY ./src /app/src
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "src.presentation.api:app", "--host", "0.0.0.0", "--port", "8000"]
