"""
Validate that the password satisfies the security requirements.
"""
from app.settings import settings


def password_security_requirements(password: str) -> None:
    """
    Validate that the password satisfies the security requirements.

    Args:
        password (str): Password to validate.

    Raises:
        ValueError: If the password does not contain the minimum number of uppercase letters.
        ValueError: If the password does not contain the minimum number of lowercase letters.
        ValueError: If the password does not contain the minimum number of digits.
        ValueError: If the password does not contain the minimum number of special characters.
    """
    if sum(1 for char in password if char.isupper()) < int(settings.PASSWORD_MIN_UPPERCASE_LETTERS):
        raise ValueError(f'Password must contain at least {settings.PASSWORD_MIN_UPPERCASE_LETTERS} uppercase letters.')

    if sum(1 for char in password if char.islower()) < int(settings.PASSWORD_MIN_LOWERCASE_LETTERS):
        raise ValueError(f'Password must contain at least {settings.PASSWORD_MIN_LOWERCASE_LETTERS} lowercase letters.')

    if sum(1 for char in password if char.isdigit()) < int(settings.PASSWORD_MIN_DIGITS):
        raise ValueError(f'Password must contain at least {settings.PASSWORD_MIN_DIGITS} digits.')

    if sum(1 for char in password if char in settings.PASSWORD_VALID_SPECIAL_CHARACTERS) < int(
            settings.PASSWORD_MIN_SPECIAL_CHARACTERS):
        raise ValueError(
            f'Password must contain at least {settings.PASSWORD_MIN_SPECIAL_CHARACTERS} special characters.')
