#!/bin/bash
# Test script for midas-brain

set -e

echo "=== Running Tests ==="

# Run tests with coverage
uv run pytest -v --tb=short

echo "=== Tests Complete ==="
