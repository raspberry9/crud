from pydantic import field_validator, Field
from pydantic.networks import IPvAnyAddress

from crud.libs.settings import BaseSettings
from crud.libs.types import SQLiteDsn, PortNumber

DEFAULT_CRUD_DB_URL = 'sqlite:///./crud.db'
DEFAULT_CRUD_BIND_HOST = '127.0.0.1'
DEFAULT_CRUD_PORT = 8000


class Settings(BaseSettings):
    CRUD_DB_URL: SQLiteDsn = Field(DEFAULT_CRUD_DB_URL)
    CRUD_HOST: IPvAnyAddress = Field(DEFAULT_CRUD_BIND_HOST)
    CRUD_PORT: PortNumber = Field(DEFAULT_CRUD_PORT)


settings = Settings()


def get_settings():
    return settings
