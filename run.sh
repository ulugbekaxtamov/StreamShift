#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
alembic upgrade head

# Start server
echo "Starting server"
uvicorn main:app --host 0.0.0.0 --port 8000
