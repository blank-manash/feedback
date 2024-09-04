from dotenv import load_dotenv, dotenv_values
from peewee import PostgresqlDatabase
from dataclasses import dataclass

load_dotenv()

config = dotenv_values(".env")


@dataclass
class DatabaseConfig:
    PG_DATABASE: str
    PG_HOST: str
    PG_PORT: str
    PG_USERNAME: str
    PG_PASSWORD: str

    def create():
        return DatabaseConfig(**config)


def get_database():
    db = DatabaseConfig.create()
    return PostgresqlDatabase(
        db.PG_DATABASE,
        host=db.PG_HOST,
        port=db.PG_PORT,
        user=db.PG_USERNAME,
        password=db.PG_PASSWORD,
    )
