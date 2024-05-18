"""
Schema for showing an API key.
"""
from pydantic import BaseModel, ConfigDict, Field


class ShowApiKey(BaseModel):
    """
    Schema for showing an API key.
    """
    name: str = Field(default=..., description='Name of the newAPI key.', examples=['Development'])

    secret_key: str = Field(default=...,
                            description='Secret key of the new API key.',
                            examples=['8873344efbff3fa9a8ca3dd0b742797b0018ce3cb1d6c23b0c424060f68f6e30'])

    model_config = ConfigDict(extra='ignore')
