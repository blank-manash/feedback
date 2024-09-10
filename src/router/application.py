from fastapi import APIRouter
from src.models.user_query import Ticket
from src.service import processor
from src.global_utils import get_logger

router = APIRouter(prefix="/api/v1", tags=["application"])

logger = get_logger(__name__)


@router.post("/create")
def create_application(query: Ticket):
    logger.info("Recieved Ticket for Processing")
    route = processor.process(query)
    return {"status": "success", "route": route}
