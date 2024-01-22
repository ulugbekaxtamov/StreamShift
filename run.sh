#!/bin/bash

# Waiting PSQL
svc=$1
echo "Waiting 15 seconds for PSQL installation"
sleep 15

if [ "$svc" = "web" ]; then
  # Apply database migrations
  echo "Apply database migrations"
  alembic upgrade head

  # Start server
  echo "Starting server"
  uvicorn main:app --host 0.0.0.0 --port 8000
fi