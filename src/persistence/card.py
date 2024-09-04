from peewee import TextField, IntegerField

from src.persistence.base_model import BaseModel


class Card(BaseModel):
    title = TextField()
    point_count = IntegerField()
