"""
ApiKey DB model.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, TYPE_CHECKING
from typing_extensions import override

from sqlalchemy import Column, DateTime, ForeignKey, Index, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from uuid import UUID, uuid4

from app.database import Base
from app.utils.cryptography import api_key_hashing

if TYPE_CHECKING:
    from app.users.models import User


class ApiKey(Base):
    __tablename__ = 'ApiKey'

    # ID of the row
    __id = Column('id', String(length=36), primary_key=True)

    # Name of the API key
    __name = Column('name', String(length=64), nullable=False)

    # Secret key
    __secret_key = Column('secret_key', String(length=256), nullable=False, index=True)

    # Public key
    __public_key = Column('public_key', String(length=13), nullable=False)

    # Owner of the API key
    __user_id = Column('user_id', String(length=36), ForeignKey('User.id'), nullable=False)
    __user = relationship('User', back_populates='_User__api_keys', lazy='joined')

    # API key creation date
    __creation_date = Column('creation_date', DateTime, nullable=False)

    # API key last utilization date
    __last_utilization_date = Column('last_utilization_date', DateTime, nullable=True)

    # Indexes
    __secret_key_index = Index('api_key_secret_key_index', __secret_key)
    __user_index = Index('api_key_user_index', __user_id)

    def __init__(self, name: str, secret_key: str, user: User) -> None:
        """
        Create a new API key.

        Args:
            name (str): Name of the API key.
            secret_key (str): Secret key of the API key.
            user (User): Owner of the API key.
        """
        self.__id = uuid4()
        self.__name = name
        self.__secret_key = api_key_hashing(api_key=secret_key)
        self.__public_key = f'{secret_key[:5]}...{secret_key[-5:]}'
        self.__user = user

        self.__creation_date = datetime.now(tz=timezone.utc)
        self.__last_utilization_date = None

    @override
    def __eq__(self, other: Any) -> bool:
        """
        Check if ApiKey object is equal to another object.

        Args:
            other (Any): Object to compare.

        Returns:
            bool: True if ApiKey object equal, to the other object, False otherwise.
        """
        return type(self) is type(other) and dict(self) == dict(other)

    @override
    def __hash__(self) -> int:
        """
        Get hash of the ApiKey object.

        Returns:
            int: Hash of the ApiKey object.
        """
        return hash(str(dict(self)))

    def __iter__(self) -> dict:
        """
        Get api key as a dict for private use.
        Private use means that the dict will contain sensitive information.

        Returns:
            dict: Product as dict.
        """
        yield 'id', str(self.__id),
        yield 'name', self.__name,
        yield 'secret_key', self.__secret_key,
        yield 'public_key', self.__public_key,
        yield 'user', str(self.__user.id),
        yield 'creation_date', self.__creation_date,
        yield 'last_utilization_date', self.__last_utilization_date

    def update_last_utilization_date(self) -> None:
        """
        Update the last utilization date of the api key.
        """
        self.__last_utilization_date = datetime.now(tz=timezone.utc)

    @hybrid_property
    def id(self) -> UUID:
        """
        Get the ID of the api key.

        Returns:
            UUID: ID of the api key.
        """
        return self.__id

    @id.setter
    def id(self, value: Any) -> None:
        raise AttributeError('ApiKey id is a read-only attribute.')

    @hybrid_property
    def name(self) -> str:
        """
        Get the name of the api key.

        Returns:
            str: Name of the api key.
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Set the name of the api key.

        Args:
            value (str): New name of the api key.
        """
        self.__name = value

    @hybrid_property
    def secret_key(self) -> str:
        """
        Get the hashed secret key of the api key.

        Returns:
            str: Hashed secret key of the api key.
        """
        return self.__secret_key

    @secret_key.setter
    def secret_key(self, value: Any) -> None:
        raise AttributeError('ApiKey secret key cannot be updated.')

    @hybrid_property
    def public_key(self) -> str:
        """
        Get the public key of the api key.

        Returns:
            str: Public key of the api key.
        """
        return self.__public_key

    @public_key.setter
    def public_key(self, value: Any) -> None:
        raise AttributeError('ApiKey public key is a read-only attribute.')

    @hybrid_property
    def user(self) -> User:
        """
        Get the owner of the api key.

        Returns:
            User: Owner of the api key.
        """
        return self.__user

    @user.setter
    def user(self, value: Any) -> None:
        raise AttributeError('ApiKey user is a read-only attribute.')

    @hybrid_property
    def creation_date(self) -> datetime:
        """
        Get the creation date of the api key.

        Returns:
            datetime: Creation date of the api key.
        """
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value: Any) -> None:
        raise AttributeError('ApiKey creation date is a read-only attribute.')

    @hybrid_property
    def last_utilization_date(self) -> datetime:
        """
        Get the last utilization date of the api key.

        Returns:
            datetime: Last utilization date of the api key.
        """
        return self.__last_utilization_date

    @last_utilization_date.setter
    def last_utilization_date(self, value: Any) -> None:
        raise AttributeError('ApiKey last utilization date is a read-only attribute.')
