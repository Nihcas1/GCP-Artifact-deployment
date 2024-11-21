# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Run the command to start the Flask app
CMD ["python", "app.py"]
