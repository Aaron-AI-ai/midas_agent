#!/bin/bash
# Lint script for midas-brain

set -e

echo "=== Running Linter ==="

# Run ruff check
uv run ruff check app tests

# Run ruff format check
uv run ruff format --check app tests

echo "=== Lint Complete ==="
