"""
Schema for updating an user.
"""
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.utils.cryptography import password_security_requirements
from app.utils.exceptions import ValidationException


class UpdateUser(BaseModel):
    """
    Schema for updating an user.
    """
    email: str | None = Field(default=None,
                              min_length=8,
                              max_length=320,
                              description='User email',
                              examples=['userexample@gmail.com'])

    old_password: str | None = Field(
        default=None,
        description=
        'Unhashed user old password. If provided, the new password and password_verification must also be provided.',
        examples=['P#ssW0rd@23!'])

    password: str | None = Field(
        default=None,
        min_length=8,
        max_length=64,
        description=
        'Unhashed user password. If provided the old_password and password_verification must also be provided.',
        examples=['P#ssW0rd@23!'])

    password_verification: str | None = Field(
        default=None,
        min_length=8,
        max_length=64,
        description=
        'Unhashed user password verification. If provided the old_password and new password must also be provided.',
        examples=['P#ssW0rd@23!'])

    model_config = ConfigDict(extra='forbid')

    def __init__(self, **data: dict[str, Any]) -> None:
        """
        User update schema constructor.

        Raises:
            ValidationException: If the old password, new password, and password verification are not provided together.
            ValidationException: If the user password and password verification do not match.
        """
        super().__init__(**data)

        if self.old_password is not None or\
           self.password is not None or\
           self.password_verification is not None:
            if self.old_password is None or self.password is None or self.password_verification is None:
                raise ValidationException(
                    'Old password, new password, and password verification must be provided together.')

        if self.password != self.password_verification:
            raise ValidationException('User password and password verification do not match.')

    # TODO: add email validation
    @field_validator('email')
    def email_validation(cls, value: str) -> str:
        """
        Validate that the email is valid.

        Args:
            value (str): Patient email.

        Raises:
            ValidationException: If the email is not valid.

        Returns:
            str: The patient email.
        """
        return value

    @field_validator('password')
    def password_security_requirements(cls, value: str) -> str:
        """
        Validate that the password satisfies the security requirements.

        Args:
            value (str): Patient password.

        Raises:
            ValidationException: If the password does not satisfy the security requirements.

        Returns:
            str: The patient password.
        """
        try:
            password_security_requirements(password=value)

        except ValueError as exception:
            raise ValidationException(message=str(exception))

        return value
