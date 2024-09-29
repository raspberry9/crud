from fastapi import FastAPI

from crud.auth import router as api_v1_auth_router
from crud.util import get_app_version

APP_NAME = 'crud'
APP_DESCRIPTION = 'Basic Auth. and CRUD samples.'
APP_VERSION = get_app_version()


def register_api_v1_routes(fastapi_app: FastAPI):
    fastapi_app.include_router(api_v1_auth_router, prefix='/api/v1/auth', tags=['Authentications'])


def register_api_routes(fastapi_app: FastAPI) -> None:
    register_api_v1_routes(fastapi_app)


def create_app() -> FastAPI:
    fastapi_app = FastAPI(title=APP_NAME, description=APP_DESCRIPTION, version=APP_VERSION)
    register_api_routes(fastapi_app)
    return fastapi_app

app = create_app()
