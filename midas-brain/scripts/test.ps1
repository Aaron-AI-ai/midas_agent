# Test script for midas-brain (Windows PowerShell)

$ErrorActionPreference = "Stop"

Write-Host "=== Running Tests ===" -ForegroundColor Cyan

# Run tests
uv run pytest -v --tb=short

Write-Host "=== Tests Complete ===" -ForegroundColor Green
