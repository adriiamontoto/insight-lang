"""
Database configuration file.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy_utils import create_database as create_database_command
from sqlalchemy_utils import database_exists, drop_database

from app.settings import settings

url = f'mysql+pymysql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_engine(url=url, pool_pre_ping=True, pool_recycle=3600)

session_maker = scoped_session(session_factory=sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()


def create_database() -> None:
    """
    Create database tables.
    """
    # Import all database models here
    from app.users.models import User

    print('Creating database tables ...')
    if database_exists(url=url):
        drop_database(url=url)

    create_database_command(url=url)
    Base.metadata.create_all(bind=engine)
