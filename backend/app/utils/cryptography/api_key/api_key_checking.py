"""
API key functionalities module.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi.security import APIKeyHeader

from app.database import session_maker
from app.utils.cryptography import api_key_hashing
from app.utils.exceptions import InvalidCredentialsException

if TYPE_CHECKING:
    from app.users.models import User

api_key_schema = APIKeyHeader(name='X-API-Key')


def get_current_user(api_key: str) -> User:
    """
    Get the current user from the token.

    Args:
        api_key (str): API key data.

    Raises:
        InvalidCredentialsException: If the token is invalid.
        InvalidCredentialsException: If the user is not found.

    Returns:
        User: The user that is logged in.
    """
    from app.users.dal import UserDAL

    with session_maker() as session:
        user_dal = UserDAL(session=session)

        result = user_dal.get_api_key_by_secret_key(secret_key=api_key_hashing(api_key=api_key))
        if result is None:
            raise InvalidCredentialsException(message='This API key does not exist.')

        result.update_last_utilization_date()
        return result.user


def check_valid_api_key(api_key: str = Depends(dependency=api_key_schema)) -> User:
    """
    Check if the a valid api key is provided and return the user.

    Args:
        api_key (str, optional): User api key, if it exists.

    Raises:
        InvalidCredentialsException: If api key is missing.

    Returns:
        User: The user that owns the api key.
    """
    if api_key is None:
        raise InvalidCredentialsException(message='API key is missing.')

    return get_current_user(api_key=api_key)
