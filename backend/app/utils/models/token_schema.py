"""
This module contains the token schema.
"""
from pydantic import BaseModel, ConfigDict, Field


class TokenSchema(BaseModel):
    """
    Token schema.
    """
    access_token: str = Field(
        default=...,
        description='Access token',
        examples=[
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJpbnNpZ2h0LWxhbmciLCJzdWIiOiJkNzFhNjNlYi0zZDhkLTQyNTktYTAyNi00OWJiMmMzZDlmYTMiLCJhdWQiOiJhdXRoZW50aWNhdGlvbiIsImV4cCI6MTcxMzU2NzUzMywiaWF0IjoxNzEzNTY3MjMzfQ.3YU2hgqAjtUrGZjHXJL-V8qgpWEcc1NiZsjOgM3nUgc'
        ])

    token_type: str = Field(default=..., description='Token type', examples=['Bearer'])

    model_config = ConfigDict(extra='forbid')
