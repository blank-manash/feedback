from peewee import TextField, BigIntegerField, AutoField

from src.persistence.models.base_model import BaseModel


class Card(BaseModel):
    id: AutoField()
    title: TextField()
    no_of_points: BigIntegerField()
