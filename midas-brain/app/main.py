"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api import router
from app.core import settings

app = FastAPI(
    title=settings.app_name,
    description="AI Agent service for Quant Agent system",
    version="0.1.0",
)

app.include_router(router, prefix="/api/v1")


@app.get("/")
async def root() -> dict:
    """Root endpoint."""
    return {
        "name": settings.app_name,
        "version": "0.1.0",
        "status": "running",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
