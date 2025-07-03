# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
# Use --no-cache-dir to reduce image size
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container (for FastAPI)
EXPOSE 8000
# Make port 8501 available for Streamlit
EXPOSE 8501

# Define the command to run your application.
# This will be overridden by docker-compose, but it's good practice to have it.
# The command will start the FastAPI server.
CMD ["streamlit", "run", "app/frontend/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
