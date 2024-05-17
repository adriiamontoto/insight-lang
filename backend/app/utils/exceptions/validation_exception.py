"""
This module contains the custom exception class for the validation exception.
"""


class ValidationException(RuntimeError):
    """
    Exception raised when there is a validation exception.
    """

    def __init__(self, message: str = 'Validation error') -> None:
        """
        Initialize the exception with the message.

        Args:
            message (str, optional): The message to be displayed. Defaults to 'Validation error'.
        """
        self.message = message
        super().__init__(self.message)
