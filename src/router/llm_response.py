from fastapi import APIRouter
from src.service.llm_gemini import get_response

router = APIRouter(prefix="/model", tags=["llm"])


@router.get("/")
def get_llm_response(text: str):
    return get_response(text)
