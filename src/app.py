from fastapi import FastAPI
from src.router import application

app = FastAPI()

app.include_router(application.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
