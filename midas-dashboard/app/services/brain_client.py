"""Midas Brain API client."""

import httpx

from app.core import settings


class BrainClient:
    """Client for Midas Brain API."""

    def __init__(self, base_url: str | None = None):
        """Initialize the client.

        Args:
            base_url: Base URL for the API. Defaults to settings value.
        """
        self.base_url = base_url or settings.brain_api_url

    async def health_check(self) -> dict:
        """Check API health status.

        Returns:
            Health status response.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/api/v1/health")
            response.raise_for_status()
            return response.json()

    async def chat(self, message: str, context: dict | None = None) -> dict:
        """Send chat message to agent.

        Args:
            message: User message.
            context: Optional context data.

        Returns:
            Agent response.
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/api/v1/chat",
                json={"message": message, "context": context},
            )
            response.raise_for_status()
            return response.json()

    def health_check_sync(self) -> dict:
        """Check API health status (sync version).

        Returns:
            Health status response.
        """
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/api/v1/health")
            response.raise_for_status()
            return response.json()

    def chat_sync(self, message: str, context: dict | None = None) -> dict:
        """Send chat message to agent (sync version).

        Args:
            message: User message.
            context: Optional context data.

        Returns:
            Agent response.
        """
        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/api/v1/chat",
                json={"message": message, "context": context},
            )
            response.raise_for_status()
            return response.json()
