from pytest import fixture

from alembic.config import Config as AlembicConfig
from alembic.command import upgrade as alembic_upgrade
from sqlalchemy_utils import create_database, database_exists, drop_database

from crud.settings import settings
from crud.models import engine, SessionLocal, Base


@fixture
def db():
    if database_exists(engine.url):
        drop_database(engine.url)

    create_database(engine.url)

    try:
        alembic_config = AlembicConfig(config_args={
            'url': settings.CRUD_DB_URL,
            'target_metadata': Base.metadata,
            'script_location': 'alembic',
        })

        alembic_config.set_main_option('script_location', 'alembic')
        alembic_upgrade(alembic_config, 'head')

        _db = SessionLocal()
        yield _db
        _db.close()
    finally:
        engine.dispose()
