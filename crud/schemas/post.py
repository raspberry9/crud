from typing import Optional

from pydantic import BaseModel, ConfigDict



class PostBase(BaseModel):
    title: str
    description: Optional[str] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
