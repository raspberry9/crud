import uvicorn
from fastapi import FastAPI

from crud.libs.version import get_app_version
from crud.libs.logging import getLogger
from crud.libs.error import register_error_handlers

from crud.settings import get_settings
from crud.routes import register_routes

logger = getLogger(__name__)
settings = get_settings()


def create_app() -> FastAPI:
    fastapi_app = FastAPI(title='crud', description='Basic Auth. and CRUD samples.', version=get_app_version())
    register_routes(fastapi_app)
    register_error_handlers(fastapi_app)
    return fastapi_app


app = create_app()


def main():
    uvicorn.run(app, host=settings.CRUD_HOST, port=settings.CRUD_PORT)


if __name__ == '__main__':
    main()
