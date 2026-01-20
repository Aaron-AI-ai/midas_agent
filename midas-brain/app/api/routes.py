"""API route definitions."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    """Chat request model."""

    message: str
    context: dict | None = None


class ChatResponse(BaseModel):
    """Chat response model."""

    response: str
    agent: str


@router.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Process chat message through agent workflow."""
    # TODO: Integrate with agent graph
    return ChatResponse(
        response=f"Received: {request.message}",
        agent="router",
    )
