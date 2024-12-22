from enum import StrEnum
from  http import HTTPStatus as status
from typing import Optional, Dict, Union

from pydantic import BaseModel, ConfigDict
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


class CRUDExceptionBase(BaseModel):
    status_code: int = status.INTERNAL_SERVER_ERROR
    error_code: int = 1000
    message: str = 'Internal Server Error'

    model_config = ConfigDict(hidden=True)


class CRUDException(HTTPException):
    def __init__(self, error_model: Union[BaseModel, type],
                 headers: Optional[Dict[str, str]] = None):
        if isinstance(error_model, BaseModel):
            error = error_model
        else:
            error = error_model()

        for required_field_name in ('status_code', 'error_code', 'message'):
            if not hasattr(error, required_field_name):
                raise ValueError(f'{required_field_name} is required in error model')

        super().__init__(status_code=error.status_code,
                         detail={'msg': error.message},
                         headers=headers)
        self.error_model = error


class BadParameterDetailBase(StrEnum):
    pass


class BadParameterErrorBase(CRUDExceptionBase):
    '''Usage example:
    >>> class BadParameterDetail(BadParameterDetailBase):
    >>>     USER_ID_OR_EMAIL_REQUIRED = '%s or %s are required'
    >>> class BadParameterError(BadParameterErrorBase):
    >>>     pass
    >>> raise CRUDException(BadParameterError(BadParameterDetail.USER_ID_OR_EMAIL_REQUIRED, 'user_id', 'email'))
    '''
    def __init__(self, detail: BadParameterDetailBase, *args):
        super().__init__()
        self.detail = detail % args
    status_code: int = status.BAD_REQUEST
    error_code: int = 1010
    message: str = 'Invalid parameter'
    detail: Optional[BadParameterDetailBase] = None


def register_error_handlers(app: FastAPI):
    @app.exception_handler(CRUDException)
    async def crud_exception_handler(_: Request, exc: CRUDException):
        if isinstance(exc.error_model, BaseModel):
            error_model = exc.error_model
        else:
            error_model = exc.error_model()
        content = {
            'status_code': error_model.status_code,
            'error_code': error_model.error_code,
            'message': error_model.message,
        }
        if hasattr(error_model, 'detail') and error_model.detail is not None:
            content['detail'] = error_model.detail # .value if isinstance(error_model.detail, StrEnum) else error_model.detail
        return JSONResponse(status_code=exc.status_code, content=content)
