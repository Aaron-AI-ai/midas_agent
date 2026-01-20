#!/bin/bash
# Start server script for midas-brain

set -e

echo "=== Starting Midas Brain Server ==="

# Check if .env exists
if [ ! -f .env ]; then
    echo "Error: .env file not found. Run './scripts/setup.sh' first."
    exit 1
fi

# Start the server
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
