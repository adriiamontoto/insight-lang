"""
Schema for creating an API key.
"""
from pydantic import BaseModel, ConfigDict, Field


class CreateApiKey(BaseModel):
    """
    Schema for creating an API key.
    """
    name: str = Field(default=...,
                      min_length=3,
                      max_length=64,
                      description='Name of the newAPI key.',
                      examples=['Development'])

    model_config = ConfigDict(extra='forbid')
