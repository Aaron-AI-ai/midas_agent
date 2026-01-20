# Lint script for midas-dashboard (Windows PowerShell)

$ErrorActionPreference = "Stop"

Write-Host "=== Running Linter ===" -ForegroundColor Cyan

# Run ruff check
uv run ruff check app tests

# Run ruff format check
uv run ruff format --check app tests

Write-Host "=== Lint Complete ===" -ForegroundColor Green
