from peewee import UUIDField, TextField, BigIntegerField

from src.persistence.models.base_model import BaseModel
from pgvector.peewee import VectorField

class Card(BaseModel):
    id: UUIDField()
    title: TextField()
    no_of_points: BigIntegerField()
