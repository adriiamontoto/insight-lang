"""
User routes.
"""
from fastapi import APIRouter, Body, Depends, Path, status
from uuid import UUID

from app.database import session_maker
from app.users.dal import UserDAL
from app.users.models import CreateApiKey, CreateUser, ShowApiKey, ShowUser, UpdateApiKey, UpdateUser, User
from app.utils.cryptography import check_user_logged_in, check_user_not_logged_in, generate_secret_key
from app.utils.exceptions import NotFoundException, ValidationException
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
                        "message": 'User with id d71a63eb-3d8d-4259-a026-49bb2c3d9fa3 has been deleted.'
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


@router.get(
    path='/api-key/{api_key_id}',
    summary='Get an API key for the current user.',
    description='Get an API key for the current user.',
    responses={
        status.HTTP_200_OK: {
            'model': ShowApiKey,
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
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorSchema,
            'content': {
                'application/json': {
                    'example': {
                        'message': 'API key with id a3186a65-fd74-40ab-88c4-e1a91145f0fc not found.',
                        'error': 'Not Found'
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
async def get_api_key(user: User = Depends(dependency=check_user_logged_in),
                      api_key_id: UUID = Path(default=...,
                                              description='API key id to get.',
                                              examples=['a3186a65-fd74-40ab-88c4-e1a91145f0fc'])) -> ShowApiKey:
    """
    Get an API key for the current user.

    Args:
        user (User): Current logged in user.
        api_key_id (UUID): API key id to get.

    Raises:
        InvalidCredentialsException: If user is not logged in.
        NotFoundException: If API key with the given ID is not found.
        NotFoundException: If API key does not belong to the current user.

    Returns:
        ShowApiKey: API key information.
    """
    with session_maker() as session:
        user_dal = UserDAL(session=session)

        api_key = user_dal.get_api_key_by_id(id=api_key_id)
        if api_key is None:
            raise NotFoundException(message=f'API key with id {api_key_id} not found')

        if api_key.user.id != user.id:
            raise NotFoundException(message=f'API key with id {api_key_id} not found')

        return_value = ShowApiKey(**dict(api_key))
        return_value.secret_key = api_key.public_key

        return return_value


@router.post(
    path='/api-key',
    summary='Create an API key for the current user.',
    description='Create an API key for the current user.',
    responses={
        status.HTTP_200_OK: {
            'model': ShowApiKey,
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
async def create_api_key(user: User = Depends(dependency=check_user_logged_in),
                         api_key_data: CreateApiKey = Body(default=..., description='API key data')) -> ShowApiKey:
    """
    Create an API key for the current user.

    Args:
        user (User): User who owns the API key.
        api_key_data (CreateApiKey): API key data.

    Raises:
        InvalidCredentialsException: If user is not logged in.

    Returns:
        ShowApiKey: Created API key.
    """
    with session_maker() as session:
        user_dal = UserDAL(session=session)

        secret_key = generate_secret_key()
        api_key = user_dal.create_api_key(user=user, name=api_key_data.name, secret_key=secret_key)

        return_value = ShowApiKey(**dict(api_key))
        return_value.secret_key = secret_key

        return return_value


@router.put(
    path='/api-key/{api_key_id}',
    summary='Update an API key for the current user.',
    description='Update an API key for the current user.',
    responses={
        status.HTTP_200_OK: {
            'model': ShowApiKey,
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
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorSchema,
            'content': {
                'application/json': {
                    'example': {
                        'message': 'API key with id a3186a65-fd74-40ab-88c4-e1a91145f0fc not found.',
                        'error': 'Not Found'
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
async def update_api_key(user: User = Depends(dependency=check_user_logged_in),
                         api_key_id: UUID = Path(default=...,
                                                 description='API key id to update.',
                                                 examples=['a3186a65-fd74-40ab-88c4-e1a91145f0fc']),
                         api_key_data: UpdateApiKey = Body(default=..., description='API key data')) -> ShowApiKey:
    """
    Update an API key for the current user.

    Args:
        user (User): Current logged in user.
        api_key_id (UUID): API key id to update.
        api_key_data (UpdateApiKey): Updated API key data.

    Raises:
        InvalidCredentialsException: If user is not logged in.
        NotFoundException: If API key with the given ID is not found.
        NotFoundException: If API key does not belong to the current user.

    Returns:
        ShowApiKey: Updated API key.
    """
    with session_maker() as session:
        user_dal = UserDAL(session=session)

        api_key = user_dal.get_api_key_by_id(id=api_key_id)
        if api_key is None:
            raise NotFoundException(message=f'API key with id {api_key_id} not found')

        if api_key.user.id != user.id:
            raise NotFoundException(message=f'API key with id {api_key_id} not found')

        api_key = user_dal.update_api_key(api_key=api_key, name=api_key_data.name)

        return_value = ShowApiKey(**dict(api_key))
        return_value.secret_key = api_key.public_key

        return return_value


@router.delete(
    path='/api-key/{api_key_id}',
    summary='Delete an API key for the current user.',
    description='Delete an API key for the current user.',
    responses={
        status.HTTP_200_OK: {
            'model': MessageSchema,
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Api key with id a3186a65-fd74-40ab-88c4-e1a91145f0fc has been deleted.'
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
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorSchema,
            'content': {
                'application/json': {
                    'example': {
                        'message': 'API key with id a3186a65-fd74-40ab-88c4-e1a91145f0fc not found.',
                        'error': 'Not Found'
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
async def delete_api_key(user: User = Depends(dependency=check_user_logged_in),
                         api_key_id: UUID = Path(default=...,
                                                 description='API key id to delete.',
                                                 examples=['a3186a65-fd74-40ab-88c4-e1a91145f0fc'])) -> MessageSchema:
    """
    Delete an API key for the current user.

    Args:
        user (User): Current logged in user.

    Raises:
        InvalidCredentialsException: If user is not logged in.
        NotFoundException: If API key with the given ID is not found.
        NotFoundException: If API key does not belong to the current user.

    Returns:
        MessageSchema: Message about the operation.
    """
    with session_maker() as session:
        user_dal = UserDAL(session=session)

        api_key = user_dal.get_api_key_by_id(id=api_key_id)
        if api_key is None:
            raise NotFoundException(message=f'API key with id {api_key_id} not found')

        if api_key.user.id != user.id:
            raise NotFoundException(message=f'API key with id {api_key_id} not found')

        user_dal.delete_api_key(api_key=api_key)

        return MessageSchema(message=f'API key with id {api_key_id} has been deleted.')
