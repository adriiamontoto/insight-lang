"""
Secret key utilities module.
"""
from secrets import token_hex


def generate_secret_key(length: int = 32) -> str:
    """
    Generate a secret key.

    Args:
        length (int, optional): Length of the secret key. Defaults to 32.

    Returns:
        str: Secret key.
    """
    return token_hex(nbytes=length)
