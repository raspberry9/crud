import re

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# from crud.settings import get_settings

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

# _engine = create_engine(get_settings().CRUD_DB_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
# Base = declarative_base()


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


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
