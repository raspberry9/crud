from enum import StrEnum
from typing import Optional
from http import HTTPStatus as status

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from crud.libs.types import PositiveInt
from crud.libs.error import CRUDException, CRUDExceptionBase, BadParameterDetailBase, BadParameterErrorBase
from crud.settings import Settings, get_settings
from crud.models import get_db
from crud.schemas.user import User, UsersGet, UserCreate, CreatedUser
from crud.controller.user import get_user as _get_user
from crud.controller.user import get_user_by_email as _get_user_by_email
from crud.controller.user import get_users as _get_users
from crud.controller.user import create_user as _create_user


router = APIRouter()

MAX_USERS_PER_PAGE = 10


class UnknownDatabaseError(CRUDExceptionBase):
    status_code: int = status.INTERNAL_SERVER_ERROR
    error_code: int = 1000
    message: str = 'Unknown database error'


class BadParameterDetail(BadParameterDetailBase):
    USER_ID_OR_EMAIL_REQUIRED = '%s or %s is required'


class BadParameterError(BadParameterErrorBase):
    error_code: int = 1010
    detail: Optional[BadParameterDetail] = None


class UserAlreadyExistsError(CRUDExceptionBase):
    status_code: int = status.CONFLICT
    error_code: int = 1020
    message: str = 'User already exists'


class UserNotFoundError(CRUDExceptionBase):
    status_code: int = status.NOT_FOUND
    error_code: int = 1021
    message: str = 'User not found'


@router.get('/', response_model=UsersGet)
def get_users(offset: int=0, limit: PositiveInt=MAX_USERS_PER_PAGE,
              _: Settings=Depends(get_settings),
              db: Session=Depends(get_db)):
    users = _get_users(db, offset, limit)
    return UsersGet(offset=offset, limit=limit, users=users)


@router.get('', response_model=User, responses={
    status.NOT_FOUND: {'model': UserNotFoundError},
    status.BAD_REQUEST: {'model': BadParameterError}
})
def get_user(user_id: Optional[int] = None,
             email: Optional[str] = None,
             _: Settings=Depends(get_settings),
             db: Session=Depends(get_db)):
    if user_id is None and email is None:
        raise CRUDException(
            # 아래는 USER_ID_OR_EMAIL_REQUIRED 내용에 user_id와 email을 넣어서 표현하는게 좋지만 args 사용 예시를 위해서
            # user_id와 email을 args로 분리했음. Better way:
            #     # BadParameterDetail.USER_ID_OR_EMAIL_REQUIRED = 'user_id or email is required'
            #     raise CRUDException(BadParameterError(BadParameterDetail.USER_ID_OR_EMAIL_REQUIRED))
            BadParameterError(BadParameterDetail.USER_ID_OR_EMAIL_REQUIRED, 'user_id', 'email'))
    user = _get_user(db, user_id, email)
    if user is None:
        raise CRUDException(UserNotFoundError)
    return user


@router.post('', response_model=CreatedUser, status_code=status.CREATED, responses={
    status.CONFLICT: {'model': UserAlreadyExistsError},
    status.INTERNAL_SERVER_ERROR: {'model': UnknownDatabaseError}
})
def create_user(input_user: UserCreate,
                _: Settings=Depends(get_settings),
                db: Session=Depends(get_db)):
    try:
        return _create_user(db, input_user)
    except IntegrityError as e:
        if 'UNIQUE constraint failed' in str(e):
            raise CRUDException(UserAlreadyExistsError) from e
        raise CRUDException(UnknownDatabaseError) from e


# TODO: update user 작성
# @router.put('', response_model=User, status_code=status.CREATED, responses={
#     status.CONFLICT: {'model': UserAlreadyExistsError},
#     status.INTERNAL_SERVER_ERROR: {'model': UnknownDatabaseError}
# })
# def update_user(input_user: UserCreate,
#                 settings: Settings=Depends(get_settings),
#                 db: Session=Depends(get_db)):
#     pass
# TODO: 권한 검사
#     return _update_user(db, input_user)
