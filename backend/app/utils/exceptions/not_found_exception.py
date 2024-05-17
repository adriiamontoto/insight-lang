"""
This module contains the custom exception classes for the not found exceptions.
"""


class NotFoundException(RuntimeError):
    """
    Exception raised when the requested resource was not found.
    """

    def __init__(self, message: str = 'Resource not found') -> None:
        """
        Initialize the exception with the message.

        Args:
            message (str, optional): The message to be displayed. Defaults to 'Resource not found'.
        """
        self.message = message
        super().__init__(self.message)
