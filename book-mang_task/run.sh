#!/bin/bash

echo "Building and starting Docker containers..."

# Build and start the containers in detached mode
docker-compose up --build -d

echo "Docker containers are up and running!"

# Check if containers are running
docker-compose ps
