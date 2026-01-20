"""Application configuration."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # API Settings
    app_name: str = "Midas Brain"
    debug: bool = False

    # Anthropic Settings
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-sonnet-4-20250514"

    # OpenAI Settings
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"

    # Server Settings
    host: str = "0.0.0.0"
    port: int = 8000


settings = Settings()
