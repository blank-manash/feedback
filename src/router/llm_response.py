from fastapi import APIRouter


router = APIRouter(prefix="/model", tags=["llm"])


@router.get("/")
def get_llm_response():
    return "This response is from LLM"
