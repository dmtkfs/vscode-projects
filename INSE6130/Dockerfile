# Use Alpine as the base image
FROM alpine:latest

# Install Python, pip, Supervisor, and required Python packages
RUN apk update && \
    apk add --no-cache \
    python3 \
    py3-pip \
    supervisor \
    procps \
    coreutils \
    py3-psutil \
    py3-watchdog

# Create directories for Supervisor logs and configuration
RUN mkdir -p /var/log/supervisor /etc/supervisor/conf.d /ids_app/logs

# Copy the configuration files and script
COPY supervisord.conf /etc/supervisord.conf
COPY ids.py /ids_app/ids.py
COPY ids.conf /etc/supervisor/conf.d/ids.conf

# Set permissions for the script
RUN chmod +x /ids_app/ids.py

# Set the command to run Supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

