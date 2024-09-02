from peewee import ForeignKeyField, TextField, BigIntegerField, AutoField

from src.persistence.models.base_model import BaseModel
from src.persistence.models.card import Card


class Point(BaseModel):
    id: AutoField()
    description: TextField()
    no_of_complaints: BigIntegerField()
    card: ForeignKeyField(Card, backref='messages')
