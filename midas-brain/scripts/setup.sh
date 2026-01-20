#!/bin/bash
# Setup script for midas-brain

set -e

echo "=== Midas Brain Setup ==="

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    pip install uv
fi

# Create virtual environment and install dependencies
echo "Creating virtual environment..."
uv sync

# Copy .env.example to .env if not exists
if [ ! -f .env ]; then
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo "Please update .env with your API keys"
fi

echo "=== Setup Complete ==="
echo "Run './scripts/start.sh' to start the server"
