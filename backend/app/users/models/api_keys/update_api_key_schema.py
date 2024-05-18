"""
Schema for updating an API key.
"""
from pydantic import BaseModel, ConfigDict, Field


class UpdateApiKey(BaseModel):
    """
    Schema for updating an API key.
    """
    name: str | None = Field(default=None,
                             min_length=3,
                             max_length=64,
                             description='Name of the newAPI key.',
                             examples=['Development'])

    model_config = ConfigDict(extra='forbid')
