from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean

from crud.settings import get_settings

engine = create_engine(get_settings().CRUD_DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


class Post(Base):
    __tablename__ = "posts"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String(255), nullable=False)
    description = mapped_column(String(255))
    owner_id = mapped_column(Integer, ForeignKey("users.id"))
    owner = relationship("User",back_populates="posts")


class User(Base):
    __tablename__ = 'users'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False)
    email = mapped_column(String(255), unique=True, nullable=False)
    posts = relationship(Post, back_populates="owner", cascade='delete')
    is_active = mapped_column(Boolean,default=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
