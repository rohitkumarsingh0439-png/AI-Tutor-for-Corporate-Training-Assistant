"""Application configuration. Never print or expose secret values."""

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent

# Load local environment settings if a .env file exists.
# Existing environment variables remain available.
load_dotenv(PROJECT_ROOT / ".env")

APP_TITLE = "AI Tutor for Corporate Training Assistant"
APP_SUBTITLE = "Workplace learning, skills development and training analytics"


def is_openai_configured() -> bool:
    """Return whether an API key is available without revealing its value."""
    return bool(os.getenv("OPENAI_API_KEY", "").strip())


def get_openai_model() -> str:
    """Return the configured model name, if one has been supplied."""
    return os.getenv("OPENAI_MODEL", "").strip()