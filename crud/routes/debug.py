from typing_extensions import Annotated

from fastapi import APIRouter
from fastapi import Depends

from crud.settings import Settings
from crud.settings import get_settings

router = APIRouter()


@router.get("/test")
def test(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "hello": "world",
        'DB_URL': settings.DATABASE_URL,
    }