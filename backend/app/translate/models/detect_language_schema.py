"""
Detect language schema module.
"""
from pydantic import BaseModel, ConfigDict, Field


class DetectLanguage(BaseModel):
    """
    Detect language schema.
    """
    text: str = Field(default=...,
                      min_length=1,
                      description='Text to detect the language.',
                      examples=['Estoy aprendiendo a traducir textos con modelos LLM.'])

    model_config = ConfigDict(extra='forbid')
