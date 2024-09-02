from datetime import datetime
from src.constants import get_database

from peewee import Model, PostgresqlDatabase, DateTimeField

database =  get_database()

class BaseModel(Model):
    class Meta:
        database = database
        created_at: DateTimeField(default=datetime.utcnow)
        modified_at: DateTimeField(default=datetime.utcnow)
