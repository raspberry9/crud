from typing_extensions import List
from http import HTTPStatus as status

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


from crud.libs.error import CRUDException, CRUDExceptionBase
from crud.settings import Settings, get_settings
from crud.models import get_db
from crud.schemas.user import User, UserCreate
from crud.controller.user import get_users as _get_users
from crud.controller.user import create_user as _create_user


router = APIRouter()

MAX_USERS_PER_PAGE = 10


class UnknownDatabaseError(CRUDExceptionBase):
    status_code: int = status.INTERNAL_SERVER_ERROR
    error_code: int = 1000
    message: str = 'Unknown database error'


class UserAlreadyExistsError(CRUDExceptionBase):
    status_code: int = status.CONFLICT
    error_code: int = 1001
    message: str = 'User already exists'


@router.get('/users/', response_model=List[User])
def get_users(offset: int=0, limit: int=MAX_USERS_PER_PAGE,
              settings: Settings=Depends(get_settings),
              db: Session=Depends(get_db)):
    users = _get_users(db, offset, limit)
    return users


@router.put('/users/', response_model=User, status_code=status.CREATED,
            responses={
                status.CONFLICT: {'model': UserAlreadyExistsError},
            })
def create_user(input_user: UserCreate,
                settings: Settings=Depends(get_settings),
                db: Session=Depends(get_db)):
    try:
        return _create_user(db, input_user)
    except IntegrityError as e:
        if 'UNIQUE constraint failed' in str(e):
            raise CRUDException(UserAlreadyExistsError)
        else:
            raise CRUDException(UnknownDatabaseError)
