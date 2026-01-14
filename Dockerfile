# Base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app app

# Expose the port Flask uses
EXPOSE 5000

# Run Flask app
CMD ["python", "-m", "flask", "--app", "app/app.py", "run", "--host=0.0.0.0"]
