from typing import List

from pydantic import BaseModel, ConfigDict, Field

from crud.schemas.post import Post, _POST_MODEL_EXAMPLE_

_USER_BASE_MODEL_EXAMPLE_ = {
    'name': 'John Doe',
    'email': 'john.doe@kormail.net',
}

_USER_MODEL_EXAMPLE_ = _USER_BASE_MODEL_EXAMPLE_.copy()
_USER_MODEL_EXAMPLE_.update({
    'id': 123,
    'is_active': False,
    'posts': [_POST_MODEL_EXAMPLE_, ],
})

_USER_MODEL_WITH_EMPTY_POSTS_EXAMPLE_ = _USER_MODEL_EXAMPLE_.copy()
_USER_MODEL_WITH_EMPTY_POSTS_EXAMPLE_['posts'].clear()


class UserBase(BaseModel):
    name: str
    email: str

    model_config = ConfigDict(
        json_schema_extra={
            'examples': [_USER_BASE_MODEL_EXAMPLE_],
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


class CreatedUser(User):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            # 새로 생성된 직후의 사용자는 posts가 하나도 없으므로 예제에서도 제외함
            'examples': [
                _USER_MODEL_WITH_EMPTY_POSTS_EXAMPLE_,
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
