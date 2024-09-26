#!/bin/bash

# Stop and remove the old container if it exists
docker stop secure_container && docker rm secure_container

# Build the Docker image without cache
docker build --no-cache -t ids_alpine_image .

# Run the container in detached mode with necessary volume mounts
docker run -d \
  --name secure_container \
  -v /var/log:/host_var_log:ro \
  ids_alpine_image

