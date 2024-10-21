import re

DB_URL_PATTERN = re.compile(
    r'^(?P<dialect>[a-zA-Z0-9]+)(\+(?P<driver>[a-zA-Z0-9]+))?://'  # dialect+driver
    r'(?:(?P<username>[^:/?#]+)(:(?P<password>[^@/?#]*))?@)?'  # username:password@
    r'(?P<host>[^:/?#]+)?'  # host
    r'(:(?P<port>[0-9]+))?'  # :port
    r'/(?P<database>[^/?#]+)'  # /database
    r'(\?(?P<query>[^#]*))?'  # ?query
    r'(#(?P<fragment>.*))?$'  # #fragment
)

SQLITE_URL_PATTERN = re.compile(
    r'^sqlite(\+[a-zA-Z0-9]+)?:///'  # sqlite 또는 sqlite+driver
    r'([^?#]*)'  # 파일 경로
    r'(\?(?P<query>[^#]*))?'  # ?query
    r'(#(?P<fragment>.*))?$'  # #fragment
)


def is_valid_database_url(url: str) -> bool:
    '''
    데이터베이스 URL 형식이 맞는지 검사하여 True/False로 리턴한다.
    형식: dialect+driver://username:password@host:port/database
    '''
    return bool(DB_URL_PATTERN.match(url))


def is_valid_sqlite_file_url(url: str) -> bool:
    '''
    SQLite 파일 URL 형식이 맞는지 검사하여 True/False로 리턴한다.
    형식: sqlite:///path/to/database.db 또는 sqlite+driver:///path/to/database.db
    '''
    return bool(SQLITE_URL_PATTERN.match(url))

# from typing import AsyncGenerator

# from fastapi import Depends
# from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
# from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
# from sqlalchemy.orm import DeclarativeBase, Integer, Mapped, mapped_column

# DATABASE_URL = "sqlite+aiosqlite:///./test.db"


# class Base(DeclarativeBase):
#     pass


# class User(SQLAlchemyBaseUserTableUUID, Base):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)


# engine = create_async_engine(DATABASE_URL)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session


# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)
