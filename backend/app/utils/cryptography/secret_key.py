"""
Secret key utilities module.
"""
from secrets import token_hex


def generate_secret_key(length: int = 64) -> str:
    """
    Generate a secret key.

    Args:
        length (int): Length of the secret key.

    Returns:
        str: Secret key.
    """
    return token_hex(nbytes=length)
