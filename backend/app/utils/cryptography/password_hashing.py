"""
This module contains functions to hash and check passwords.
"""
from argon2 import PasswordHasher, Type
from argon2.exceptions import VerifyMismatchError

from app.settings import settings


def password_hashing(password: str) -> str:
    """
    Hash the password of the customer.

    Args:
        password (str): Password of the customer.

    Returns:
        str: Hashed password of the customer with hex encoding.
    """
    return PasswordHasher(
        time_cost=settings.HASHING_TIME_COST,
        memory_cost=settings.HASHING_MEMORY_COST,
        parallelism=settings.HASHING_PARALLELISM,
        hash_len=settings.HASHING_HASH_LENGTH,
        type=Type.ID,
    ).hash(password=bytes(password, 'utf-8'))


def password_checking(password: str, hashed_password: str) -> bool:
    """
    Check if the password and the hashed password are the same.

    Args:
        password (str): Password to check.
        hashed_password (str): Hashed password to compare.

    Returns:
        bool: True if password is correct, False otherwise.
    """
    try:
        return PasswordHasher(
            time_cost=settings.HASHING_TIME_COST,
            memory_cost=settings.HASHING_MEMORY_COST,
            parallelism=settings.HASHING_PARALLELISM,
            hash_len=settings.HASHING_HASH_LENGTH,
            type=Type.ID,
        ).verify(hash=bytes(hashed_password, 'utf-8'), password=bytes(password, 'utf-8'))

    except VerifyMismatchError:
        return False
