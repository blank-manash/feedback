from peewee import ForeignKeyField, TextField, BigIntegerField
from pgvector.peewee import VectorField
from src.persistence.base_model import BaseModel
from src.persistence.card import Card
from src.constants import EMBEDDING_DIMENSION


class Point(BaseModel):
    description = TextField()
    no_of_complaints = BigIntegerField()
    card = ForeignKeyField(Card, backref="points")
    embedding = VectorField(dimensions=EMBEDDING_DIMENSION)
