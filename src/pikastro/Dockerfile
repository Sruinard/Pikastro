# Use the official Python image as the base image
FROM --platform=linux/amd64 python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the content of the local src directory to the working directory
COPY . .

# Install any dependencies
RUN pip install .

# Expose the port that your app will run on
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "pikastro.app.main:app", "--host", "0.0.0.0", "--port", "8080"]