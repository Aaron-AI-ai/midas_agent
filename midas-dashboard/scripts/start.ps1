# Start script for midas-dashboard (Windows PowerShell)

$ErrorActionPreference = "Stop"

Write-Host "=== Starting Midas Dashboard ===" -ForegroundColor Cyan

# Check if .env exists
if (-not (Test-Path .env)) {
    Write-Host "Error: .env file not found. Run '.\scripts\setup.ps1' first." -ForegroundColor Red
    exit 1
}

# Start Streamlit
uv run streamlit run app/main.py --server.port 8501
