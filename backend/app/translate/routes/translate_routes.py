"""
Text translate routes.
"""
from fastapi import APIRouter, Body, status

from app.translate.functions import language_detection, translate_text
from app.translate.models import DetectedLanguage, DetectLanguage, TextToTranslate, TranslatedText

router = APIRouter()


@router.post(path='',
             summary='Translate text to the specified language.',
             description='Translate text to the specified language. The language must be in BCP 47 standard.',
             status_code=status.HTTP_200_OK,
             response_model=TranslatedText)
async def translate_text_route(text_to_translate: TextToTranslate = Body(default=...)) -> TranslatedText:
    """
    Translate the text to the specified language. The language must be in BCP 47 standard.

    Args:
        text_to_translate (TextToTranslate): Text to translate.

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
async def detect_language_route(detect_language: DetectLanguage = Body(default=...)) -> DetectedLanguage:
    """
    Detect the language of the text. Language is in BCP 47 standard.

    Args:
        detect_language (DetectLanguage): Text to detect the language.

    Returns:
        DetectedLanguage: Detected language. Language is in BCP 47 standard.
    """
    detected_language = language_detection(text=detect_language.text)

    return DetectedLanguage(text=detect_language.text, language=detected_language)
