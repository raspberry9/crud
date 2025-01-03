from fastapi import APIRouter
from fastapi import Depends

from crud.settings import Settings
from crud.settings import get_settings

router = APIRouter()


@router.get('/test')
def test(settings: Settings = Depends(get_settings)):
    return {
        'CRUD_DB_URL': settings.CRUD_DB_URL,
        'CRUD_HOST': settings.CRUD_HOST,
        'CRUD_PORT': settings.CRUD_PORT,
    }
