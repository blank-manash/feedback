import uvicorn
from fastapi import FastAPI
from src.router import application

app = FastAPI()

app.include_router(application.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
