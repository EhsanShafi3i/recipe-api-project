FROM python:3.12.4-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    CRYPTOGRAPHY_DONT_BUILD_RUST=1 \
    DEV=true \
    PATH="/py/bin:$PATH"

# Set working directory
WORKDIR /app

# Install system dependencies (bash and curl for debugging, if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    postgresql-client \
    build-essential \
    libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements files first to leverage Docker cache
COPY ./requirements.txt ./requirements.dev.txt /app/

# Create a virtual environment and install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --no-cache-dir --upgrade pip && \
    /py/bin/pip install --no-cache-dir --index-url https://pypi.org/simple -r /app/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install --no-cache-dir --index-url https://pypi.org/simple -r /app/requirements.dev.txt; fi

# Copy the rest of the application code
COPY ./app /app/

# Create a non-root user and set permissions
RUN useradd -m django-user && \
    chown -R django-user:django-user /app /py

# Switch to the non-root user
USER django-user

# Expose the application port
EXPOSE 8000
