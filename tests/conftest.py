from pytest import fixture

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_DATABASE_URL = "sqlite:///./debug.db"


@fixture(scope='session', autouse=True)
def db():
    from sqlalchemy_utils import create_database, database_exists, drop_database

    engine = create_engine(TEST_DATABASE_URL, echo=True)
    TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # _db = {
    #     'engine': engine,
    #     'session': TestSessionLocal,
    # }

    if database_exists(engine.url):
        drop_database(engine.url)

    create_database(engine.url)

    try:
        # from alembic import context
        from alembic.config import Config as AlembicConfig
        # from alembic.environment import EnvironmentContext
        from alembic.command import upgrade as alembic_upgrade, downgrade as alembic_downgrade

        from crud.models import Base

        alembic_config = AlembicConfig( config_args={
            'url': TEST_DATABASE_URL,
            'target_metadata': Base.metadata,
            'script_location': 'alembic',
        })

        # alembic_config.env = EnvironmentContext(alembic_config, None, fn=alembic_upgrade

        print('!!!!!', 2)

        # with context.begin_transaction():
        # alembic_config = context.config

        alembic_config.set_main_option('sqlalchemy.url', TEST_DATABASE_URL)
        alembic_config.set_main_option('script_location', 'alembic')
        alembic_upgrade(alembic_config, 'head')

        yield TestSessionLocal()
    finally:
        engine.dispose()
