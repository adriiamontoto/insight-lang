"""
Translated text schema.
"""
from pydantic import BaseModel, ConfigDict, Field


class TranslatedText(BaseModel):
    """
    Translated text schema.
    """
    original_text: str = Field(default=...,
                               description='Original text.',
                               examples=['Estoy aprendiendo a traducir textos con modelos LLM.'])

    text: str = Field(default=...,
                      description='Translated text.',
                      examples=['I am learning to translate texts with LLM models.'])

    language: str = Field(default=...,
                          description='Language of the text to translate as BCP 47 standard.',
                          examples=['en-US'])

    model_config = ConfigDict(extra='forbid')
