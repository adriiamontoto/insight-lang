"""
This module contains functions to create and validate JWT tokens.
"""
from datetime import datetime, timedelta, timezone
from enum import StrEnum, unique

from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTClaimsError, JWTError
from uuid import UUID

from app.settings import settings
from app.utils.exceptions import InvalidCredentialsException
from app.utils.models import TokenDataSchema, TokenSchema


@unique
class TokenAudience(StrEnum):
    """
    Token audience enumeration.
    """
    AUTHENTICATION = 'authentication'


@unique
class TokenAlgorithm(StrEnum):
    """
    Token algorithm enumeration.
    """
    HS256 = 'HS256'


@unique
class TokenType(StrEnum):
    """
    Token type enumeration.
    """
    BEARER = 'bearer'


def create_token(user_id: UUID) -> TokenSchema:
    """
    Create a JWT token with the given parameters.

    Args:
        user_id (UUID): Identifier of the user.

    Returns:
        TokenSchema: JWT token.
    """
    # yapf: disable
    expiration_datetime = (datetime.now(tz=timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION_DELTA)).timestamp()
    # yapf: enable

    access_token_data = TokenDataSchema(issuer=settings.APP_NAME,
                                        user_id=user_id,
                                        audience=TokenAudience.AUTHENTICATION,
                                        creation_datetime=int(datetime.now(tz=timezone.utc).timestamp()),
                                        expiration_datetime=int(expiration_datetime))

    access_token = jwt.encode(claims=access_token_data.model_dump(mode='json'),
                              key=settings.SECRET_KEY,
                              algorithm=TokenAlgorithm.HS256)

    return TokenSchema(access_token=access_token, token_type=TokenType.BEARER)


def check_token(token: str) -> TokenDataSchema:
    """
    Validate a JWT token.

    Args:
        token (str): JWT token.
        secret_key (str): Secret key to validate the token.
        issuer (str): Who issued the token.
        audience (str, optional): Who the token is intended for. Defaults to 'authentication'.

    Raises:
        InvalidCredentialsException: If token is invalid.

    Returns:
        TokenDataSchema: Token data.
    """
    try:
        token_decoded = jwt.decode(token=token,
                                   key=settings.SECRET_KEY,
                                   algorithms=[TokenAlgorithm.HS256],
                                   issuer=settings.APP_NAME,
                                   audience=TokenAudience.AUTHENTICATION)

    except (JWTClaimsError, ExpiredSignatureError, JWTError) as exception:
        raise InvalidCredentialsException(message=f'Invalid token: {exception}.'.replace('..', '.'))

    return TokenDataSchema(issuer=token_decoded['iss'],
                           user_id=UUID(bytes=token_decoded['sub']),
                           audience=token_decoded['aud'],
                           creation_datetime=token_decoded['iat'],
                           expiration_datetime=token_decoded['exp'])
