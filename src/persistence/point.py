from peewee import ForeignKeyField, TextField, BigIntegerField, AutoField

from src.persistence.base_model import BaseModel
from src.persistence.card import Card


class Point(BaseModel):
    description = TextField()
    no_of_complaints = BigIntegerField()
    card = ForeignKeyField(Card, backref="points")
