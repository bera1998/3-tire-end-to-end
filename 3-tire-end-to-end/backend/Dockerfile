# Use lightweight Python image
FROM python:3.11-alpine

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Expose backend port
EXPOSE 5000

# Start the backend server
CMD ["python", "app.py"]