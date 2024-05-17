"""
Text to translate schema.
"""
from langcodes import standardize_tag
from langcodes.tag_parser import LanguageTagError
from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.utils.exceptions import ValidationException


class TextToTranslate(BaseModel):
    """
    Text to translate schema.
    """
    text: str = Field(default=...,
                      min_length=1,
                      description='Text to translate.',
                      examples=['Estoy aprendiendo a traducir textos con modelos LLM.'])

    language: str = Field(default=...,
                          description='Language of the text to translate as BCP 47 standard.',
                          examples=['en-US'])

    model_config = ConfigDict(extra='forbid')

    @field_validator('language')
    def validate_language(cls, language: str) -> str:
        """
        Validate that the language field is a valid BCP 47 language.

        Args:
            values (str): Language field value.

        Raises:
            ValidationException: If the language field is not a valid BCP 47 language.

        Returns:
            str: Language field value.
        """
        try:
            return standardize_tag(tag=language)

        except LanguageTagError as exception:
            raise ValidationException(message=exception)
