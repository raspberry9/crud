from sqlalchemy.orm import Session

from crud.models import Post
from crud.schemas.post import PostCreate


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def get_posts(db: Session, offset:int=0, limit: int=50):
    return db.query(Post).offset(offset).limit(limit).all()


def create_user_post(db:Session, post:PostCreate, user_id : int):
    db_post = Post(**post.model_dump(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: Session, post: Post, updated_post: PostCreate):
    for key, value in updated_post.model_dump().items():
        setattr(post, key, value)
    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, post: Post):
    db.delete(post)
    db.commit()
