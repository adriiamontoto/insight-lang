"""
Text translate routes.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Body, Depends, status

from app.translate.functions import language_detection, translate_text
from app.translate.models import DetectedLanguage, DetectLanguage, TextToTranslate, TranslatedText
from app.utils.cryptography import check_valid_api_key

if TYPE_CHECKING:
    from app.users.models import User

router = APIRouter()


@router.post(path='',
             summary='Translate text to the specified language.',
             description='Translate text to the specified language. The language must be in BCP 47 standard.',
             status_code=status.HTTP_200_OK,
             response_model=TranslatedText)
async def translate_text_route(user: User = Depends(dependency=check_valid_api_key),
                               text_to_translate: TextToTranslate = Body(default=...)) -> TranslatedText:
    """
    Translate the text to the specified language. The language must be in BCP 47 standard.

    Args:
        user (User): User owner of the API key.
        text_to_translate (TextToTranslate): Text to translate.

    Raises:
        InvalidCredentialsException: If the API key is invalid.

    Returns:
        TranslatedText: Translated text.
    """
    translated_text = translate_text(text=text_to_translate.text, language=text_to_translate.language)

    return TranslatedText(original_text=text_to_translate.text,
                          text=translated_text,
                          language=text_to_translate.language)


@router.post(path='/detect-language',
             summary='Detect the language of the text.',
             description='Detect the language of the text. Language is in BCP 47 standard.',
             status_code=status.HTTP_200_OK,
             response_model=DetectedLanguage)
async def detect_language_route(user: User = Depends(dependency=check_valid_api_key),
                                detect_language: DetectLanguage = Body(default=...)) -> DetectedLanguage:
    """
    Detect the language of the text. Language is in BCP 47 standard.

    Args:
        user (User): User owner of the API key.
        detect_language (DetectLanguage): Text to detect the language.

    Raises:
        InvalidCredentialsException: If the API key is invalid.

    Returns:
        DetectedLanguage: Detected language. Language is in BCP 47 standard.
    """
    detected_language = language_detection(text=detect_language.text)

    return DetectedLanguage(text=detect_language.text, language=detected_language)
