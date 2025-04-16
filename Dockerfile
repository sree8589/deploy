# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy files
COPY app/ ./app/

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app/main.py"]

