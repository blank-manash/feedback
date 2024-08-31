from typing import Annotated
from fastapi import APIRouter, Body
from src.service.llm_gemini import get_response
from src.models.user_query import Ticket

router = APIRouter(prefix="/model", tags=["llm"])


@router.post("/query")
def get_llm_response(ticket: Ticket):
    return get_response(ticket.query)
