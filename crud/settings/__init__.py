from crud.libs.settings import BaseSettings
from crud.settings.database import DatabaseSettingsMixin


class Settings(BaseSettings, DatabaseSettingsMixin):
    pass


settings = Settings()


def get_settings():
    return settings
