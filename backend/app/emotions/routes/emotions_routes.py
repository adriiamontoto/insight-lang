"""
Text emotions detection routes.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Body, Depends, status

from app.emotions.functions import emotion_detection
from app.emotions.models import DetectedEmotion, DetectEmotion
from app.utils.cryptography import check_valid_api_key

if TYPE_CHECKING:
    from app.users.models import User

router = APIRouter()


@router.post(path='/detect-emotion',
             summary='Detect the emotion of the text.',
             description='Detect the emotion of the text.',
             status_code=status.HTTP_200_OK,
             response_model=DetectedEmotion)
async def detect_emotion_route(user: User = Depends(dependency=check_valid_api_key),
                               detect_emotion: DetectEmotion = Body(default=...)) -> DetectedEmotion:
    """
    Detect the emotion of the text.

    Args:
        user (User): User owner of the API key.
        detect_emotion (DetectEmotion): Text to detect the emotion.

    Raises:
        InvalidCredentialsException: If the API key is invalid.

    Returns:
        DetectedEmotion: Detected emotion.
    """
    detected_emotion = emotion_detection(text=detect_emotion.text)

    return DetectedEmotion(text=detect_emotion.text, emotion=detected_emotion)
