from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field

from crud.schemas.post import Post


class UserBase(BaseModel):
    name: str = Field(..., example="John Doe")
    email: str = Field(..., example="john.doe@kormail.net")


class User(UserBase):
    id: int = Field(..., gt=0, example=123)
    is_active: bool
    posts: List[Post] = Field(...,
                              example=[
                                  Post(id=1, title="Hello World",
                                       description="This is a description",
                                       owner_id=123)])

    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    pass


class UsersGet(BaseModel):
    offset: int = Field(..., ge=0, example=0)
    limit: int = Field(..., gt=0, example=10)
    users: List[User]
