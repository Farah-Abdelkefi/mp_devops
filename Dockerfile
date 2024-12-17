FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Add a non-root user and switch to it
RUN useradd -m appuser
USER appuser

# Copy application files (use .dockerignore to exclude sensitive files)
COPY --chown=appuser:appuser . /app

# Install dependencies
RUN pip install pytest

# Run the application
CMD ["python", "username_generator.py"]
