from fastapi import APIRouter
from src.models.user_query import Ticket

router = APIRouter(prefix="/api/v1", tags=["application"])


@router.post("/create")
def create_application(query: Ticket):
    pass
