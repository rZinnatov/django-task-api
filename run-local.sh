#!/bin/sh

echo "Run containers"
docker-compose \
    -f ./deploy/docker-compose.yml \
    -p django-task-api \
    up #--build
