"""
Schema for the user login data.
"""
from pydantic import BaseModel, ConfigDict, Field


class LoginSchema(BaseModel):
    """
    Schema for the user login data.
    """
    email: str = Field(default=..., description='User email', examples=['userexample@gmail.com'])

    password: str = Field(default=..., description='Unhashed user password', examples=['P#ssW0rd@23!'])

    model_config = ConfigDict(extra='forbid')
