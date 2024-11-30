from  http import HTTPStatus as status
from typing import Optional, Dict

from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


class CRUDExceptionBase(BaseModel):
    status_code: int = Field(status.INTERNAL_SERVER_ERROR, hidden=True)
    error_code: int = 1000
    message: str = 'Internal Server Error'


class CRUDException(HTTPException):
    def __init__(self, error_model: BaseModel,
                 headers: Optional[Dict[str, str]] = None):
        error = error_model()

        for required_field_name in ('status_code', 'error_code', 'message'):
            if not hasattr(error, required_field_name):
                raise ValueError(f'{required_field_name} is required in error model')

        super().__init__(status_code=error.status_code,
                         detail={'msg': error.message},
                         headers=headers)
        self.error_model = error


def register_error_handlers(app: FastAPI):
    @app.exception_handler(CRUDException)
    async def crud_exception_handler(request: Request, exc: CRUDException):
        error_model = exc.error_model
        return JSONResponse(
            status_code=exc.status_code,
            content={
                'status_code': error_model.status_code,
                'error_code': error_model.error_code,
                'message': error_model.message,
            }
        )
