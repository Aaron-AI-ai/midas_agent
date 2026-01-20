# Setup script for midas-brain (Windows PowerShell)

$ErrorActionPreference = "Stop"

Write-Host "=== Midas Brain Setup ===" -ForegroundColor Cyan

# Check if uv is installed
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "Installing uv..." -ForegroundColor Yellow
    pip install uv
}

# Create virtual environment and install dependencies
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
uv sync

# Copy .env.example to .env if not exists
if (-not (Test-Path .env)) {
    Write-Host "Creating .env from .env.example..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "Please update .env with your API keys" -ForegroundColor Red
}

Write-Host "=== Setup Complete ===" -ForegroundColor Green
Write-Host "Run '.\scripts\start.ps1' to start the server"
