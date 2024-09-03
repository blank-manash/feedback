from src.constants import get_database
from datetime import datetime
from peewee import Model, DateTimeField, BigAutoField

database = get_database()


class BaseModel(Model):
    id = BigAutoField()
    created_at = DateTimeField(default=datetime.now)
    modified_at = DateTimeField(default=datetime.now)

    class Meta:
        database = database
