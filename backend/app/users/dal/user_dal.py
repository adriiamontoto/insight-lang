"""
User Data Access Layer
"""
from sqlalchemy.orm import Session
from uuid import UUID

from app.users.models import ApiKey, User
from app.utils.exceptions import ValidationException


class UserDAL():
    __session: Session

    def __init__(self, session: Session) -> None:
        """
        Create a new UserDAL instance.

        Args:
            session (Session): Database session.
        """
        self.__session = session

    def get_user_by_id(self, id: UUID) -> User | None:
        """
        Get a user by ID.

        Args:
            id (UUID): User ID.

        Returns:
            User: User if it exists, None otherwise.
        """
        return self.__session.query(User).filter(User.id == str(id)).first()

    def get_user_by_email(self, email: str) -> User | None:
        """
        Get a user by email.

        Args:
            email (str): User email.

        Returns:
            User: User if it exists, None otherwise.
        """
        return self.__session.query(User).filter(User.email == email).first()

    def create_user(self, email: str, password: str) -> User:
        """
        Create a new user.

        Args:
            email (str): User email.
            password (str): User password.

        Raises:
            ValidationException: If the user with the new email already exists.

        Returns:
            User: Created user.
        """
        if self.get_user_by_email(email=email):
            raise ValidationException(message=f'User with email {email} already exists.')

        user = User(email=email, password=password)

        self.__session.add(instance=user)
        self.__session.commit()

        return user

    def update_user(self, user: User, email: str | None = None, password: str | None = None) -> User:
        """
        Update a user.

        Args:
            user (User): User to update.
            email (str | None, optional): New email. Defaults to None.
            password (str | None, optional): New password. Defaults to None.

        Raises:
            ValidationException: If the user with the new email already exists.

        Returns:
            User: Updated user.
        """
        if email is not None:
            if self.get_user_by_email(email=email) and email != user.email:
                raise ValidationException(message='User with this email already exists.')

        user_hash = hash(user)

        if email is not None:
            if email != user.email:
                user.email = email

        if password is not None:
            user.update_password(new_password=password)

        if user_hash != hash(user):
            self.__session.add(instance=user)
            self.__session.commit()

        return user

    def delete_user(self, user: User) -> None:
        """
        Delete a user.

        Args:
            user (User): User to delete.
        """
        self.__session.delete(instance=user)
        self.__session.commit()

    def get_api_key_by_id(self, id: UUID) -> ApiKey | None:
        """
        Get an API key by ID.

        Args:
            id (UUID): API key ID.

        Returns:
            User: API key if it exists, None otherwise.
        """
        return self.__session.query(ApiKey).filter(ApiKey.id == str(id)).first()

    def get_api_key_by_secret_key(self, secret_key: str) -> ApiKey | None:
        """
        Get an API key by secret key.

        Args:
            secret_key (str): API key secret key.

        Returns:
            ApiKey: API key if it exists, None otherwise.
        """
        return self.__session.query(ApiKey).filter(ApiKey.secret_key == secret_key).first()

    def create_api_key(self, user: User, name: str, secret_key: str) -> ApiKey:
        """
        Create a new API key.

        Args:
            user (User): User who owns the API key.
            name (str): API key name.
            secret_key (str): API key secret key.

        Returns:
            ApiKey: Created API key.
        """
        api_key = ApiKey(user=user, name=name, secret_key=secret_key)

        self.__session.add(instance=api_key)
        self.__session.commit()

        return api_key

    def update_api_key(self, api_key: ApiKey, name: str | None = None) -> ApiKey:
        """
        Update an API key.

        Args:
            api_key (ApiKey): API key to update.
            name (str | None, optional): New name. Defaults to None.

        Returns:
            ApiKey: Updated API key.
        """
        api_key_hash = hash(api_key)

        if name is not None:
            if name != api_key.name:
                api_key.name = name

        if api_key_hash != hash(api_key):
            self.__session.add(instance=api_key)
            self.__session.commit()

        return api_key

    def delete_api_key(self, api_key: ApiKey) -> None:
        """
        Delete an API key.

        Args:
            api_key (ApiKey): API key to delete.
        """
        self.__session.delete(instance=api_key)
        self.__session.commit()
