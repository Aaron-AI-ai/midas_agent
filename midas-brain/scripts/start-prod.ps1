# Production server script for midas-brain (Windows PowerShell)

$ErrorActionPreference = "Stop"

Write-Host "=== Starting Midas Brain Server (Production) ===" -ForegroundColor Cyan

# Check if .env exists
if (-not (Test-Path .env)) {
    Write-Host "Error: .env file not found." -ForegroundColor Red
    exit 1
}

# Start the server without reload
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
