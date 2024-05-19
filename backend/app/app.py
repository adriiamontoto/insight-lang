"""
App module.
"""
from fastapi import FastAPI, status

from app.auth.routes import router as auth_router
from app.emotions.routes import router as emotions_router
from app.settings import settings, Tags
from app.translate.routes import router as translate_router
from app.users.routes import router as users_router
from app.utils.models import MessageSchema

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
app.include_router(router=translate_router, prefix='/translate', tags=[Tags.TRANSLATE])
app.include_router(router=emotions_router, prefix='/emotions', tags=[Tags.EMOTIONS])
app.include_router(router=users_router, prefix='/user', tags=[Tags.USER])
app.include_router(router=auth_router, prefix='/auth', tags=[Tags.AUTH])


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


from app.errors import *  # noqa
