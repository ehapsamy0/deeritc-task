#!/bin/bash

echo "Building and starting Docker containers..."

docker-compose up --build -d

echo "Docker containers are up and running!"

docker-compose ps
