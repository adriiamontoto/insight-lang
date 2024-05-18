"""
This module contains the custom exception classes when the user cannot be logged and the user is already logged in.
"""


class UserCannotBeLoggedInException(RuntimeError):
    """
    Exception raised when the user cannot be logged in and is already logged in.
    """

    def __init__(self, message: str = 'User cannot be logged in.') -> None:
        """
        Initialize the exception with the message.

        Args:
            message (str, optional): The message to be displayed. Defaults to 'User cannot be logged in'.
        """
        self.message = message
        super().__init__(self.message)
