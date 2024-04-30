FROM python:3.11.0

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the Django application code
COPY ./KAP_Backend /app

# Set working directory
WORKDIR /app


# Copy entrypoint script
COPY ./entrypoint.sh /

# Make entrypoint script executable
RUN chmod +x /entrypoint.sh

# Set entrypoint command
ENTRYPOINT ["/entrypoint.sh"]