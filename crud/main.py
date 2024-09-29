from fastapi import FastAPI


def register_api_v1_routes(app:FastAPI):
    from crud.api.v1.auth import router as api_v1_auth_router
    app.include_router(api_v1_auth_router, prefix='/api/v1/auth', tags=['Authentications'])


def register_api_routes(app: FastAPI) -> None:
    register_api_v1_routes(app)


def create_app() -> FastAPI:
    app = FastAPI()
    register_api_routes(app)
    return app

app = create_app()
