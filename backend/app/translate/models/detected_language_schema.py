"""
Detected language schema.
"""
from pydantic import BaseModel, ConfigDict, Field


class DetectedLanguage(BaseModel):
    """
    Detected language schema.
    """
    text: str = Field(default=...,
                      description='Text to detect the language.',
                      examples=['Estoy aprendiendo a traducir textos con modelos LLM.'])

    language: str = Field(default=...,
                          description='Language of the original text as BCP 47 standard.',
                          examples=['es-ES'])

    model_config = ConfigDict(extra='forbid')
