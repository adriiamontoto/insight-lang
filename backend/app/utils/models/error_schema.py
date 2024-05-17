"""
This module contains the Pydantic schema for the error response.
"""
from pydantic import BaseModel, ConfigDict, Field


class ErrorSchema(BaseModel):
    """
    Error response schema.
    """
    message: str = Field(
        default=...,
        description='The message to be displayed.',
        examples=['The server could not understand the request. Please check if it is correctly formatted.'])

    error: str = Field(default=..., description='The error type.', examples=['Validation Error'])

    model_config = ConfigDict(extra='forbid')
