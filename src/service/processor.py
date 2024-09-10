from src.models import Ticket, SimilarityResponse, CreateResponse, ProcessRoute
from src.vectors import get_similarity, create_embedding
from src.persistence import Point, Card
from src.global_utils import get_logger
from typing import Optional
import src.service.llm_gemini as model
from src.constants import CREATE_THRESHOLD, MERGE_THRESHOLD

logger = get_logger(__name__)


def creation_flow(point: str) -> ProcessRoute.CREATION:
    logger.info("Creating Card")
    response: CreateResponse = model.create_card(point)
    # Card will be unique because card depends on point
    # If point is distinct, then card will be unique
    card = Card.create(title=response.card_title, point_count=1)
    Point.create(
        description=response.point_content,
        embedding=create_embedding(response.point_content),
        card=card,
        no_of_complaints=1,
    )
    return ProcessRoute.CREATION


def merge_flow(content: str, reference: SimilarityResponse) -> ProcessRoute:
    score: float = reference.score
    point: Point = reference.get_point()
    card: Card = point.card
    card.point_count += 1
    card.save()
    if score < MERGE_THRESHOLD:
        sanitized_content = model.sanitize_text(content)
        Point.create(
            description=sanitized_content,
            embedding=create_embedding(sanitized_content),
            card=card,
            no_of_complaints=1,
        )
        return ProcessRoute.MERGE
    else:
        point.no_of_complaints += 1
        point.save()
        return ProcessRoute.ADDITION


def process(ticket: Ticket) -> ProcessRoute:
    query = ticket.query
    response: Optional[SimilarityResponse] = get_similarity(query)
    if not response:
        return creation_flow(query)

    score = response.score

    logger.info(
        f"Similarity Response Score: {score}, user_point: {query}, reference_point: {response.content}"
    )
    if score < CREATE_THRESHOLD:
        return creation_flow(query)

    return merge_flow(query, response)
