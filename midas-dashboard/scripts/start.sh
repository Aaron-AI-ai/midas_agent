#!/bin/bash
# Start script for midas-dashboard

set -e

echo "=== Starting Midas Dashboard ==="

# Check if .env exists
if [ ! -f .env ]; then
    echo "Error: .env file not found. Run './scripts/setup.sh' first."
    exit 1
fi

# Start Streamlit
uv run streamlit run app/main.py --server.port 8501
