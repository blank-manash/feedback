from pgvector.peewee import VectorField

from src.persistence.models.base_model import BaseModel
from src.persistence.models.card import Card
from peewee import ForeignKeyField, UUIDField, TextField, BigIntegerField


class Point(BaseModel):
    description: TextField()
    id: UUIDField()
    no_of_complaints: BigIntegerField()
    card: ForeignKeyField(Card, backref='messages')
