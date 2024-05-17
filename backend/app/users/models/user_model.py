"""
User DB model.
"""
from datetime import datetime, timezone
from typing import Any
from typing_extensions import override

from sqlalchemy import Column, DateTime, Index, String
from sqlalchemy.ext.hybrid import hybrid_property
from uuid import UUID, uuid4

from app.database import Base
from app.utils.cryptography import password_checking, password_hashing


class User(Base):
    __tablename__ = 'User'

    # ID of the row
    __id = Column('id', String(length=36), primary_key=True)

    # Email of the user
    __email = Column('email', String(length=320), nullable=False, unique=True, index=True)

    # Hashed password of the user
    __password = Column('password', String(length=256), nullable=False)

    # User creation date
    __creation_date = Column('creation_date', DateTime, nullable=False)

    # User last update date
    __update_date = Column('update_date', DateTime, nullable=False)

    email_index = Index('user_email_index', __email)

    def __init__(self, email: str, password: str) -> None:
        """
        Create a new user.

        Args:
            email (str): Email of the user.
            password (str): Unhashed password of the user.
        """
        self.__id = uuid4()
        self.__email = email
        self.update_password(new_password=password)

        self.__creation_date = datetime.now(tz=timezone.utc)
        self.__update_date = datetime.now(tz=timezone.utc)

    @override
    def __eq__(self, other: Any) -> bool:
        """
        Check if User object is equal to another object.

        Args:
            other (Any): Object to compare.

        Returns:
            bool: True if User object equal, to the other object, False otherwise.
        """
        return type(self) is type(other) and dict(self) == dict(other)

    @override
    def __hash__(self) -> int:
        """
        Get hash of the User object.

        Returns:
            int: Hash of the User object.
        """
        return hash(str(dict(self)))

    def __iter__(self) -> dict:
        """
        Get user as a dict for private use.
        Private use means that the dict will contain sensitive information.

        Returns:
            dict: Product as dict.
        """
        yield 'id', str(self.__id),
        yield 'email', self.__email,
        yield 'password', self.__password,  # Hashed password!
        yield 'creation_date', self.__creation_date,
        yield 'update_date', self.__update_date,

    def __update_update_date(self) -> None:
        """
        Update the update date of the user.
        """
        self.__update_date = datetime.now(tz=timezone.utc)

    def check_password(self, password: str) -> bool:
        """
        Check if the password is correct.

        Args:
            password (str): Unhashed password to check.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return password_checking(password=password, hashed_password=self.__password)

    def update_password(self, new_password: str) -> None:
        """
        Update the password of the user.

        Args:
            password (str): New password of the user.
        """
        self.__password = password_hashing(password=new_password)
        self.__update_update_date()

    @hybrid_property
    def id(self) -> UUID:
        """
        Get the ID of the user.

        Returns:
            UUID: ID of the user.
        """
        return self.__id

    @id.setter
    def id(self, value: Any) -> None:
        raise AttributeError('User id is a read-only attribute.')

    @hybrid_property
    def email(self) -> str:
        """
        Get the email of the user.

        Returns:
            str: Email of the user.
        """
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        """
        Set the email of the user.

        Args:
            value (str): New email of the user.
        """
        self.__email = value
        self.__update_update_date()

    @hybrid_property
    def password(self) -> str:
        raise AttributeError('User password cannot be accessed directly. You can use check_password method.')

    @password.setter
    def password(self, value: Any) -> None:
        raise AttributeError('User password is a read-only attribute. You can use update_password method.')

    @hybrid_property
    def creation_date(self) -> datetime:
        """
        Get the creation date of the user.

        Returns:
            datetime: Creation date of the user.
        """
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value: Any) -> None:
        raise AttributeError('User creation date is a read-only attribute.')

    @hybrid_property
    def update_date(self) -> datetime:
        """
        Get the update date of the user.

        Returns:
            datetime: Update date of the user.
        """
        return self.__update_date

    @update_date.setter
    def update_date(self, value: Any) -> None:
        raise AttributeError('User update date is a read-only attribute.')
