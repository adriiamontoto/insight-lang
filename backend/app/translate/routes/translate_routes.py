"""
Text translate routes.
"""
from fastapi import APIRouter, Body, status

from app.translate.functions import translate_text
from app.translate.models import TextToTranslate, TranslatedText

router = APIRouter()


@router.post(path='',
             summary='Translate text to the specified language.',
             description='Translate text to the specified language. The language must be in BCP 47 standard.',
             responses={
                 status.HTTP_200_OK: {
                     'model': TranslatedText,
                 },
             })
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
