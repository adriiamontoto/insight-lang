"""
Detect emotion schema module.
"""
from pydantic import BaseModel, ConfigDict, Field


class DetectEmotion(BaseModel):
    """
    Detect emotion schema.
    """
    text: str = Field(default=...,
                      min_length=1,
                      description='Text to detect the emotion.',
                      examples=['The movie ending was unexpected and left me speechless.'])

    model_config = ConfigDict(extra='forbid')
