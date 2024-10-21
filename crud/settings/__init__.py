from pydantic import field_validator, Field

from crud.libs.settings import BaseSettings
from crud.libs.database import is_valid_database_url, is_valid_sqlite_file_url


class Settings(BaseSettings):
    DATABASE_URL: str = Field('sqlite:///./default.db')

    @field_validator('DATABASE_URL')
    @classmethod
    def check_database_url(cls, value):
        if not is_valid_database_url(value) and not is_valid_sqlite_file_url(value):
            raise ValueError(f'Invalid database URL: {value}')

settings = Settings()


def get_settings():
    return settings