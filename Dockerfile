# Start with an official FastAPI Python image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# ınstall necessary libraries
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download FastSAM model
RUN wget "https://huggingface.co/spaces/An-619/FastSAM/resolve/main/weights/FastSAM.pt"  --directory-prefix app/services/weights --content-disposition

# Copy the application code
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
