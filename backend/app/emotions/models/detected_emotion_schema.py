"""
Detected emotion schema.
"""
from pydantic import BaseModel, ConfigDict, Field


class DetectedEmotion(BaseModel):
    """
    Detected emotion schema.
    """
    text: str = Field(default=...,
                      description='Text to detect the emotion.',
                      examples=['The movie ending was unexpected and left me speechless.'])

    emotion: str = Field(default=..., description='Detected emotion of the text.', examples=['surprised'])

    model_config = ConfigDict(extra='forbid')
