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
    AUTH = 'Auth'
    USER = 'User'
    TRANSLATE = 'Translate'


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

    # Security Variables
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRATION_DELTA: int  # in minutes

    ## Password Hashing Variables
    HASHING_TIME_COST: int
    HASHING_MEMORY_COST: int
    HASHING_PARALLELISM: int
    HASHING_HASH_LENGTH: int

    ## Password Requirements
    PASSWORD_MIN_UPPERCASE_LETTERS: int
    PASSWORD_MIN_LOWERCASE_LETTERS: int
    PASSWORD_MIN_DIGITS: int
    PASSWORD_MIN_SPECIAL_CHARACTERS: int
    PASSWORD_VALID_SPECIAL_CHARACTERS: str

    # Database Variables
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str


settings = Settings()  # Automatically loads settings from .env file
