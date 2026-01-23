#!/bin/bash
# Setup script for midas-dashboard

set -e

echo "=== Midas Dashboard Setup ==="

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
    echo "Please update .env with your settings"
fi

echo "=== Setup Complete ==="
echo "Run './scripts/start.sh' to start the dashboard"
