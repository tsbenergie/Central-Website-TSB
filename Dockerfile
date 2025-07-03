# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables to avoid Python buffering issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if needed for Streamlit or Plotly)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies first (leveraging Docker layer cache)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Set the default command to run Streamlit app
CMD ["streamlit", "run", "app/frontend/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
