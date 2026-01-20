#!/bin/bash
# Production server script for midas-brain

set -e

echo "=== Starting Midas Brain Server (Production) ==="

# Check if .env exists
if [ ! -f .env ]; then
    echo "Error: .env file not found."
    exit 1
fi

# Start the server without reload
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
