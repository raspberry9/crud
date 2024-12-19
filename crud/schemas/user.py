from typing import Optional, List

from pydantic import BaseModel, Field

from crud.schemas.post import Post


class UserBase(BaseModel):
    name: str = Field(..., example="John Doe")
    email: str = Field(..., example="john.doe@kormail.net")


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int = Field(..., gt=0, example=123)
    is_active: bool
    posts: List[Post] = Field(...,
                              example=[
                                  Post(id=1, title="Hello World",
                                       description="This is a description",
                                       owner_id=123)])

    class Config:
        from_attributes = True


class UsersGet(BaseModel):
    offset: int = Field(..., ge=0, example=0)
    limit: int = Field(..., gt=0, example=10)
    users: List[User]
