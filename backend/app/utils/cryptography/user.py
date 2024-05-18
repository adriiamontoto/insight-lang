"""
User authentication functions module.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.database import session_maker
from app.users.dal import UserDAL
from app.utils.cryptography import check_token
from app.utils.exceptions import InvalidCredentialsException, UserCannotBeLoggedInException

if TYPE_CHECKING:
    from app.users.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/docs/login', auto_error=True)
not_logged_oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/docs/login', auto_error=False)


def get_current_user(token: str) -> User:
    """
    Get the current user from the token.

    Args:
        token (str): Token data.

    Raises:
        InvalidCredentialsException: If the token is invalid.
        InvalidCredentialsException: If the user is not found.

    Returns:
        User | Employee: The user that is logged in.
    """
    data = check_token(token=token)

    with session_maker() as session:
        user_dal = UserDAL(session=session)

        user = user_dal.get_user_by_id(id=data.sub)
        if user is None:
            raise InvalidCredentialsException(message=f'User with ID {data.sub} not found.')

        return user


def check_user_logged_in(token: str = Depends(dependency=oauth2_scheme)) -> User:
    """
    Checks if the user is logged in and returns it.

    Args:
        token (str, optional): User access token, if it exists.

    Raises:
        InvalidCredentialsException: If the user is not logged in.

    Returns:
        User: The user that is logged in.
    """
    if token is None:
        raise InvalidCredentialsException(message='User is not logged in.')

    return get_current_user(token=token)


def check_user_not_logged_in(token: str = Depends(dependency=not_logged_oauth2_scheme)) -> None:
    """
    Checks if the user is not logged in.

    Args:
        token (str, optional): User access token, if it exists.

    Raises:
        UserCannotBeLoggedInException: If the user is already logged in.
    """
    if token is not None:
        raise UserCannotBeLoggedInException()
