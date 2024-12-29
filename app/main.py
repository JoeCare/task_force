from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import users
from db.database import setup_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Crate db tables")
    setup_db(app)
    print("DB tables created.")
    yield
    print("Application is shutting down...")

def init_app() -> FastAPI:
    app = FastAPI(title="Task Management API", version="0.1.0", lifespan=lifespan)
    app.include_router(users.router, prefix="/users", tags=["users"])
    return app

app = init_app()