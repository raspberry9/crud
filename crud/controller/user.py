from typing import Optional

from sqlalchemy.orm import Session

from crud.models import User
from crud.schemas.user import UserCreate


def get_user(db: Session, user_id: Optional[int] = None, email: Optional[str] = None):
    if user_id is None and email is None:
        raise ValueError('user_id or email is required')
    query = db.query(User)
    if user_id is not None:
        query = query.filter(User.id == user_id)
    if email is not None:
        query = query.filter(User.email == email)
    return query.first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, offset:int=0, limit:int=50):
    return db.query(User).offset(offset).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: User, updated_user: UserCreate):
    for key, value in updated_user.model_dump().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
