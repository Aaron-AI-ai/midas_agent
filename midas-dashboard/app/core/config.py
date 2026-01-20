"""Application configuration."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # App Settings
    app_name: str = "Midas Dashboard"
    debug: bool = False

    # Midas Brain API
    brain_api_url: str = "http://localhost:8000"

    # Streamlit Settings
    page_title: str = "Midas Dashboard"
    page_icon: str = "📊"


settings = Settings()
