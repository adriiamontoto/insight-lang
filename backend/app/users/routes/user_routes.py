"""
User routes.
"""
from fastapi import APIRouter, Body, Depends, status

from app.database import session_maker
from app.users.dal import UserDAL
from app.users.models import CreateUser, ShowUser, UpdateUser, User
from app.utils.cryptography import check_user_logged_in, check_user_not_logged_in
from app.utils.exceptions import ValidationException
from app.utils.models import ErrorSchema, MessageSchema

router = APIRouter()


@router.get(
    path='',
    summary='Get current user account.',
    description='Get current user account.',
    responses={
        status.HTTP_200_OK: {
            'model': ShowUser,
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
async def get_user(user: User = Depends(dependency=check_user_logged_in)) -> ShowUser:
    """
    Get current user account.

    Args:
        user (User): Current logged in user.

    Raises:
        InvalidCredentialsException: If user is not logged in.

    Returns:
        ShowUser: User information.
    """
    return ShowUser(**dict(user))


@router.post(
    path='',
    summary='Create new user account.',
    description='Create new user account.',
    responses={
        status.HTTP_201_CREATED: {
            'model': ShowUser,
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
async def create_user(not_logged_user: User = Depends(dependency=check_user_not_logged_in),
                      user_data: CreateUser = Body(default=..., description='New user data')) -> ShowUser:
    """
    Create new user account.

    Args:
        user_data (CreateUser): New user data.

    Raises:
        UserCannotBeLoggedInException: If user is already logged in.

    Returns:
        ShowUser: New user.
    """
    with session_maker() as session:
        user_dal = UserDAL(session=session)

        new_user = user_dal.create_user(email=user_data.email, password=user_data.password)

        return ShowUser(**dict(new_user))


@router.put(path='',
            summary='Update current user account.',
            description='Update current user account.',
            responses={
                status.HTTP_200_OK: {
                    'model': ShowUser,
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
                                'message': 'Old password is incorrect.',
                                'error': 'Validation Error'
                            }
                        }
                    }
                }
            })
async def update_user(user_to_update: User = Depends(dependency=check_user_logged_in),
                      user_data: UpdateUser = Body(default=..., description='Updated user data')) -> ShowUser:
    """
    Update actual user account.

    Args:
        user_to_update (User): Current logged in user.
        user_data (UpdateUser): Updated user data.

    Raises:
        InvalidCredentialsException: If user is not logged in.
        ValidationException: If old password is incorrect.

    Returns:
        ShowUser: Updated user.
    """
    with session_maker() as session:
        user_dal = UserDAL(session=session)

        if user_data.password is not None:
            if not user_to_update.check_password(password=user_data.old_password):
                raise ValidationException(message='User old password is incorrect.')

        updated_user = user_dal.update_user(user=user_to_update, email=user_data.email, password=user_data.password)

        return ShowUser(**dict(updated_user))


@router.delete(
    path='',
    summary='Delete current user account.',
    description='Delete current user account.',
    responses={
        status.HTTP_200_OK: {
            'model': MessageSchema,
            'content': {
                'application/json': {
                    'example': {
                        "message": 'User with id d71a63eb-3d8d-4259-a026-49bb2c3d9fa3 deleted.'
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
async def delete_user(user: User = Depends(dependency=check_user_logged_in)) -> MessageSchema:
    """
    Delete current user account.

    Args:
        user (User): Current logged in user.

    Raises:
        InvalidCredentialsException: If user is not logged in.

    Returns:
        MessageSchema: Message about the operation.
    """
    with session_maker() as session:
        user_dal = UserDAL(session=session)

        user_dal.delete_user(user=user)

    return MessageSchema(message=f'User with id {user.id} has been deleted.')
