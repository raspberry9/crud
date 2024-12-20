from typing import List

from pydantic import BaseModel, ConfigDict, Field

from crud.schemas.post import Post, _POST_MODEL_EXAMPLE_

_USER_MODEL_EXAMPLE_ = {
    'name': 'John Doe',
    'email': 'john.doe@kormail.net',
    'id': 123,
    'is_active': False,
    'posts': [_POST_MODEL_EXAMPLE_, ],
}


class UserBase(BaseModel):
    name: str
    email: str

    model_config = ConfigDict(
        json_schema_extra={
            'examples': [{
                k: v for k, v in _USER_MODEL_EXAMPLE_.items()
                 if k in {'name', 'email'}}],
        }
    )


class User(UserBase):
    id: int
    is_active: bool
    posts: List[Post]

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            'examples': [
                _USER_MODEL_EXAMPLE_,
            ],
        }
    )


class UserCreate(UserBase):
    pass


class UsersGet(BaseModel):
    offset: int = Field(..., ge=0)
    limit: int = Field(..., gt=0)
    users: List[User]

    model_config = ConfigDict(
        examples=[{
            'offset': 0,
            'limit': 10,
            'users': [_USER_MODEL_EXAMPLE_, ],
        }]
    )
