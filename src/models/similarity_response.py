from pydantic import BaseModel, Field
from src.persistence.point import Point


class SimilarityResponse(BaseModel):
    id: int = Field(description="ID of Point")
    score: float = Field(description="Similarity score")
    content: str = Field(description="Content of Point")

    def get_point(self) -> Point:
        return Point.get_by_id(pk=self.id)
