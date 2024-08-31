from fastapi import FastAPI
from src.router import llm_response

app = FastAPI()

app.include_router(llm_response.router)


@app.get("/")
def hello():
    return "Hello World!"
