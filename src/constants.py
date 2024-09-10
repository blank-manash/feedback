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

    @staticmethod
    def create():
        return DatabaseConfig(
            PG_DATABASE=config.get("PG_DATABASE"),
            PG_HOST=config.get("PG_HOST"),
            PG_PORT=config.get("PG_PORT"),
            PG_USERNAME=config.get("PG_USERNAME"),
            PG_PASSWORD=config.get("PG_PASSWORD"),
        )


def get_database():
    db = DatabaseConfig.create()
    return PostgresqlDatabase(
        db.PG_DATABASE,
        host=db.PG_HOST,
        port=db.PG_PORT,
        user=db.PG_USERNAME,
        password=db.PG_PASSWORD,
    )


EMBEDDING_MODEL = "models/text-embedding-004"
EMBEDDING_DIMENSION = 768
CREATE_THRESHOLD = 0.5
MERGE_THRESHOLD = 0.95
