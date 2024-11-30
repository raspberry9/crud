

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# from crud.settings import get_settings

# _engine = create_engine(get_settings().CRUD_DB_URL, echo=True)
# _session = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
# _base = declarative_base()


# def get_db():
#     db = _session()
#     try:
#         yield db
#     finally:
#         db.close()
