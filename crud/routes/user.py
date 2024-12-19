from typing_extensions import List
from http import HTTPStatus as status

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from crud.libs.types import PositiveInt
from crud.libs.error import CRUDException, CRUDExceptionBase
from crud.settings import Settings, get_settings
from crud.models import get_db
from crud.schemas.user import User, UsersGet, UserCreate
from crud.controller.user import get_user as _get_user
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
    error_code: int = 1010
    message: str = 'User already exists'


class UserNotFoundError(CRUDExceptionBase):
    status_code: int = status.NOT_FOUND
    error_code: int = 1020
    message: str = 'User not found'


@router.get('/', response_model=UsersGet)
def get_users(offset: int=0, limit: PositiveInt=MAX_USERS_PER_PAGE,
              settings: Settings=Depends(get_settings),
              db: Session=Depends(get_db)):
    '''
    http://127.0.0.1:8000/api/v1/user/?offset=0&limit=10
    '''
    users = _get_users(db, offset, limit)

    return UsersGet(offset=offset, limit=limit, users=users)


@router.get('', response_model=User, responses={
            status.NOT_FOUND: {'model': UserNotFoundError},
            })
def get_user(user_id: int,
             settings: Settings=Depends(get_settings),
             db: Session=Depends(get_db)):
    user = _get_user(db, user_id)
    if user is None:
        raise CRUDException(UserNotFoundError)
    return user


@router.post('', response_model=User, status_code=status.CREATED,
            responses={
                status.CONFLICT: {'model': UserAlreadyExistsError},
                status.INTERNAL_SERVER_ERROR: {'model': UnknownDatabaseError},
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


# TODO: update user 작성
# @router.put('', response_model=User, status_code=status.CREATED,
#             responses={
#                 status.CONFLICT: {'model': UserAlreadyExistsError},
#                 status.INTERNAL_SERVER_ERROR: {'model': UnknownDatabaseError},
#             })
# def update_user(input_user: UserCreate,
#                 settings: Settings=Depends(get_settings),
#                 db: Session=Depends(get_db)):
# TODO: 권한 검사
#     return _update_user(db, input_user)
