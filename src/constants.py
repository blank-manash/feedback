from dotenv import load_dotenv, dotenv_values
from peewee import PostgresqlDatabase

load_dotenv()

config = dotenv_values(".env")


def get_database():
    feedback_db = config.get("DATABASE")
    host = config.get("HOST")
    port = config.get("PORT")
    user = config.get("USERNAME")
    password = config.get("PASSWORD")
    return PostgresqlDatabase(
        feedback_db, host=host, port=port, user=user, password=password
    )
