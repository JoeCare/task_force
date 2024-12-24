from fastapi import FastAPI


@app.get("/", tags=["root"])
def root():
    return {"message": "root"}


def init_app() -> FastAPI:
    app = FastAPI(title="Task Management API", version="0.1.0")
    return app

app = init_app()