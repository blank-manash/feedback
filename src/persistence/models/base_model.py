from peewee import Model, PostgresqlDatabase

database = PostgresqlDatabase(':memory:')
class BaseModel(Model):
    class Meta:
        database = database
        database.execute_sql()