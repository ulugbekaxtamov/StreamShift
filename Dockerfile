FROM python:3.10-buster
ENV PYTHONUNBUFFERED=1

# Update packages and install ffmpeg
RUN apt update && \
    apt install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY requirements.txt .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . .

# Uncomment the CMD line if you want to run the server as the default command
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
