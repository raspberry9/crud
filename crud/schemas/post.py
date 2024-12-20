from typing import Optional

from pydantic import BaseModel, ConfigDict


_POST_MODEL_EXAMPLE_ = {
    'id': 1,
    'title': 'This is a title',
    'description': 'This is a description',
    'owner_id': 123
}


class PostBase(BaseModel):
    title: str
    description: Optional[str] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    owner_id: int

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            'examples': [_POST_MODEL_EXAMPLE_, ],
        },
    )
