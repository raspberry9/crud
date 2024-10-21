from fastapi import FastAPI

from crud.libs.version import get_app_version
from crud.libs.logging import getLogger

from crud.routes import register_routes

logger = getLogger(__name__)

APP_NAME = 'crud'
APP_DESCRIPTION = 'Basic Auth. and CRUD samples.'
APP_VERSION = get_app_version()


def create_app() -> FastAPI:
    fastapi_app = FastAPI(title=APP_NAME, description=APP_DESCRIPTION, version=APP_VERSION)
    register_routes(fastapi_app)
    return fastapi_app


app = create_app()
