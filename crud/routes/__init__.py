from fastapi import FastAPI

from crud.routes.debug import router as debug_router
# from crud.routes.auth import router as auth_router
from crud.routes.user import router as user_router


def register_routes(fastapi_app: FastAPI):
    fastapi_app.include_router(debug_router, tags=['Debug'])
    # fastapi_app.include_router(auth_router, prefix='/api/v1/auth',
    #                            tags=['Authentications'])

    fastapi_app.include_router(user_router, prefix='/api/v1/user',
                               tags=['Users'])
