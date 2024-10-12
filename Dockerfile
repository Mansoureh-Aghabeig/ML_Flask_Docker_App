# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything inside the 'app' directory into the container's '/app' directory
COPY app/ .

# Expose the port that the Flask app runs on
EXPOSE 5053

# Set the command to run the Flask app
CMD ["python", "app.py"]
