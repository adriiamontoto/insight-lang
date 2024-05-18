"""
This module contains the token data schema.
"""
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID


class TokenDataSchema(BaseModel):
    """
    Token data schema class.
    """
    iss: str = Field(default=...,
                     alias='issuer',
                     description='Issuer, the entity that issued the token.',
                     examples=['insight-lang'])

    sub: UUID = Field(default=...,
                      alias='user_id',
                      description='User id, the subject of the token.',
                      examples=['d71a63eb-3d8d-4259-a026-49bb2c3d9fa3'])

    aud: str = Field(default=...,
                     alias='audience',
                     description='Audience, the intended recipient of the token.',
                     examples=['authentication'])

    exp: int = Field(default=...,
                     alias='expiration_datetime',
                     description='Datetime when token will expire (as Unix timestamp).',
                     examples=[datetime.now(tz=timezone.utc).timestamp() + 3600])

    iat: int = Field(default=...,
                     alias='creation_datetime',
                     description='Datetime when token was issued (as Unix timestamp).',
                     examples=[datetime.now(tz=timezone.utc).timestamp()])

    model_config = ConfigDict(extra='forbid')
