from fastapi import FastAPI
from routers import users

def init_app() -> FastAPI:
    app = FastAPI(title="Task Management API", version="0.1.0")
    app.include_router(users.router, prefix="/users", tags=["users"])
    return app

app = init_app()