"""
This module contains the custom exception classes for the invalid credentials exception.
"""


class InvalidCredentialsException(RuntimeError):
    """
    Exception raised when the requested resource was not found.
    """

    def __init__(self, message: str = 'Invalid credentials') -> None:
        """
        Initialize the exception with the message.

        Args:
            message (str, optional): The message to be displayed. Defaults to 'Invalid credentials'.
        """
        self.message = message
        super().__init__(self.message)
