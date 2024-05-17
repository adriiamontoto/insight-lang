"""
App module.
"""
from fastapi import FastAPI, status

from app.settings import settings, Tags
from app.utils.models import MessageSchema

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)


@app.get(path='/',
         tags=[Tags.GENERAL],
         summary='Root endpoint.',
         description='Get a welcome message.',
         status_code=status.HTTP_200_OK,
         response_model=MessageSchema)
async def welcome() -> MessageSchema:
    """
    Get a welcome message.

    Returns:
        MessageSchema: Welcome message.
    """
    return MessageSchema(message=f'Welcome to {settings.APP_NAME} API. For more information please refer to /docs')
