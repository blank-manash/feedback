from pydantic import BaseModel


class Ticket(BaseModel):
    username: str
    query: str
