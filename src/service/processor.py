from src.models import Ticket, SimilarityResponse
from src.vectors import get_similarity
from src.persistence import Point
from global_utils import get_logger
import src.service.llm_gemini as model

logger = get_logger(__name__)


def creation_flow(point: str):
    logger.info("Creating Card")
    response = model.create_card(point)
    logger.info("Response from LLM: %s", response)


def merge_flow(content: str, reference: Point):
    logger.info("Merging Points")


def process(ticket: Ticket):
    query = ticket.query
    response: SimilarityResponse = get_similarity(query)
    result = (
        merge_flow(query, response.get_point())
        if response
        else creation_flow(query)
    )
    return result
