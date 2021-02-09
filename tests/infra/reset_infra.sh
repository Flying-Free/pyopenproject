#!/bin/sh

docker-compose down
docker system prune -af --volumes
docker-compose up -d