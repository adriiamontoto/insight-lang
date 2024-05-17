"""
Settings module for the app.
"""
from enum import StrEnum, unique

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(override=True)


@unique
class Tags(StrEnum):
    GENERAL = 'General'


class Settings(BaseSettings):
    """
    Settings class for the app.
    """
    # Application Variables
    APP_NAME: str
    APP_VERSION: str

    # Backend Variables
    BACKEND_PORT: int
    AI_MODEL: str
    OPENAI_API_KEY: str

    # Database Variables
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str


settings = Settings()  # Automatically loads settings from .env file
