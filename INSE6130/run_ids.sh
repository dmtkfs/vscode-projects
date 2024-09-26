#!/bin/bash

# Stop and remove the old container if it exists
docker stop secure_container && docker rm secure_container

# Build the Docker image
docker build -t ids_alpine_image .

# Run the container in detached mode
docker run -d --name secure_container ids_alpine_image
