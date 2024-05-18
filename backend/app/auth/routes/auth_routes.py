"""
Auth routes.
"""
from fastapi import APIRouter, Body, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.models import LoginSchema
from app.database import session_maker
from app.users.dal import UserDAL
from app.users.models import User
from app.utils.cryptography import check_user_not_logged_in, create_token
from app.utils.exceptions import InvalidCredentialsException
from app.utils.models import ErrorSchema, TokenSchema

router = APIRouter()


@router.post(
    '/docs/login',
    summary='User login using swagger docs',
    description=
    'User login using swagger docs. It does the same as the /auth/login endpoint, so use /auth/login for production.',
    response_model=TokenSchema,
    include_in_schema=False)
async def user_login_docs(user: User = Depends(dependency=check_user_not_logged_in),
                          login_data: OAuth2PasswordRequestForm = Depends()) -> TokenSchema:
    """
    User login using swagger docs. It does the same as the /auth/login endpoint, so use /auth/login for production.

    Args:
        user (User, optional): User to not be logged in.
        login_data (OAuth2PasswordRequestForm, optional): User login data.

    Returns:
        TokenSchema: Access token and refresh token.
    """
    return await user_login(user=user, login_data=LoginSchema(email=login_data.username, password=login_data.password))


@router.post(
    path='/login',
    summary='User login',
    description='User login. Returns an access token and refresh JWT tokens.',
    responses={
        status.HTTP_200_OK: {
            'model': TokenSchema,
        },
        status.HTTP_400_BAD_REQUEST: {
            'model': ErrorSchema,
            'content': {
                'application/json': {
                    'example': {
                        'message': 'User cannot be logged in.',
                        'error': 'Bad Request'
                    }
                }
            }
        },
        status.HTTP_401_UNAUTHORIZED: {
            'model': ErrorSchema,
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Invalid credentials. Please try again.',
                        'error': 'Unauthorized'
                    }
                }
            }
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            'model': ErrorSchema,
            'content': {
                'application/json': {
                    'example': {
                        'message':
                            'The server could not understand the request. Please check if it is correctly formatted.',
                        'error':
                            'Validation Error'
                    }
                }
            }
        }
    })
async def user_login(user: User = Depends(dependency=check_user_not_logged_in),
                     login_data: LoginSchema = Body(default=..., description='User login data')) -> TokenSchema:
    """
    User login. Returns an access JWT tokens.

    Args:
        user (User): User to not be logged in.
        login_data (LoginSchema): User login data.

    Raises:
        ValueError: If the user is already logged in.
        InvalidCredentialsException: If the credentials are invalid.

    Returns:
        TokenSchema: Access token and refresh token.
    """
    with session_maker() as session:
        user_dal = UserDAL(session=session)

        user = user_dal.get_user_by_email(email=login_data.email)
        if user is None:
            raise InvalidCredentialsException(message=f'User with email {login_data.email} not found.')

        if not user.check_password(password=login_data.password):
            raise InvalidCredentialsException(message=f'Incorrect password for user with email {login_data.email}.')

        return create_token(user_id=user.id)
