# Use a slim Python base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy cron job definition
COPY cron/apply_interest_cron /etc/cron.d/apply_interest_cron

# Give execution rights and register cron job
RUN chmod 0644 /etc/cron.d/apply_interest_cron && \
    crontab /etc/cron.d/apply_interest_cron

# Ensure logs are available
RUN touch /var/log/interest.log

# Set PYTHONPATH so Python can find the package
ENV PYTHONPATH=/app

# Start cron and keep container running
CMD ["cron", "-f"]

