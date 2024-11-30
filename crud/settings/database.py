from pydantic import field_validator, Field

from crud.libs.database import is_valid_database_url, is_valid_sqlite_file_url


DEFAULT_CRUD_DB_URL = 'sqlite:///./crud.db'


class DatabaseSettingsMixin:  # pylint: disable=too-few-public-methods
    CRUD_DB_URL: str = Field(DEFAULT_CRUD_DB_URL)

    @field_validator('CRUD_DB_URL')
    @classmethod
    def check_database_url(cls, value):
        if not is_valid_database_url(value) and not is_valid_sqlite_file_url(value):
            raise ValueError(f'Invalid database URL: {value}')
