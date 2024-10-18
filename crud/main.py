from functools import lru_cache

from fastapi import FastAPI

from crud.libs.version import get_app_version
from crud.settings import Settings

APP_NAME = 'crud'
APP_DESCRIPTION = 'Basic Auth. and CRUD samples.'
APP_VERSION = get_app_version()


def register_api_v1_routes(fastapi_app: FastAPI):
    from crud.debug import router as api_v1_debug_router
    from crud.auth import router as api_v1_auth_router

    fastapi_app.include_router(api_v1_debug_router, tags=['Debug'])
    fastapi_app.include_router(api_v1_auth_router, prefix='/api/v1/auth',
                               tags=['Authentications'])


def register_api_routes(fastapi_app: FastAPI) -> None:
    register_api_v1_routes(fastapi_app)


def create_app() -> FastAPI:
    fastapi_app = FastAPI(title=APP_NAME, description=APP_DESCRIPTION, version=APP_VERSION)
    register_api_routes(fastapi_app)
    return fastapi_app


settings = Settings()

app = create_app()
