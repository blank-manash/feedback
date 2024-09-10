from pydantic import BaseModel
from enum import Enum


class TextResponse(BaseModel):
    text: str


class ProcessRoute(Enum):
    CREATION = "creation"
    MERGE = "merge"
    ADDITION = "addition"
