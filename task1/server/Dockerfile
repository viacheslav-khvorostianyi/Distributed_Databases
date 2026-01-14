FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY counter_inmemory.py .
COPY counter_file.py .
COPY server.py .
COPY counter_postgres.py .

# Create directory for SQLite database
RUN mkdir -p /data

# Expose port
EXPOSE 8080

# Default command (can be overridden)
CMD ["python", "server.py", "--backend", "inmemory", "--port", "8080"]

