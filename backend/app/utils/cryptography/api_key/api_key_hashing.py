"""
This module contains functions to hash and check api keys.
"""
from argon2 import PasswordHasher, Type

from app.settings import settings


def api_key_hashing(api_key: str) -> str:
    """
    Hash the api key of the user.

    Args:
        api keys (str): Api key of the user.

    Returns:
        str: Hashed api key of the user with hex encoding.
    """
    return PasswordHasher(
        time_cost=settings.HASHING_TIME_COST,
        memory_cost=settings.HASHING_MEMORY_COST,
        parallelism=settings.HASHING_PARALLELISM,
        hash_len=settings.HASHING_HASH_LENGTH,
        type=Type.ID,
    ).hash(password=bytes(api_key, 'utf-8'), salt=bytes(settings.SECRET_KEY, 'utf-8'))
