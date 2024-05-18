"""
Schema for showing an user.
"""
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field


class ShowUser(BaseModel):
    """
    Schema for showing an user.
    """
    email: str = Field(default=..., description='User email', examples=['userexample@gmail.com'])

    creation_date: datetime = Field(default=...,
                                    description='User creation date',
                                    examples=[datetime.now(tz=timezone.utc)])

    update_date: datetime = Field(default=...,
                                  description='User last update date',
                                  examples=[datetime.now(tz=timezone.utc)])

    model_config = ConfigDict(extra='ignore')
