"""
Schema for showing an API key.
"""
from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID


class ShowApiKey(BaseModel):
    """
    Schema for showing an API key.
    """
    id: UUID = Field(default=..., description='ID of the API key.', examples=['a3186a65-fd74-40ab-88c4-e1a91145f0fc'])

    name: str = Field(default=..., description='Name of the newAPI key.', examples=['Development'])

    secret_key: str = Field(default=...,
                            description='Secret key of the new API key.',
                            examples=['8873344efbff3fa9a8ca3dd0b742797b0018ce3cb1d6c23b0c424060f68f6e30'])

    model_config = ConfigDict(extra='ignore')
