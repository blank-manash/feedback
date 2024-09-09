from src.vectors import create_embedding, get_similarity
from src.persistence import Point, Card
from src.models import Ticket
from src.service.processor import process, creation_flow

descriptions = [
    "Page load time is significantly high on mobile devices.",
    "Images on the homepage take too long to load.",
    "Database queries are not optimized, causing delay in rendering the content.",
    "There are too many external scripts slowing down the page.",
    "User reports frequent timeout errors when navigating the website.",
    "Server response time is slow, impacting the website’s performance.",
]


def create_test_data():

    card = Card.get_by_id(pk=1)
    for desc in descriptions:
        embedding = create_embedding(desc)
        Point.create(
            card=card,
            description=desc,
            embedding=embedding,
            no_of_complaints=1,
        )


def test_embedding():
    text = "The website just sucks super slow"
    data = get_similarity(text)
    print(data)


def test_process():
    # ticket = Ticket(username="test", query="This website is slow")
    # process(ticket)
    creation_flow("This website is slow")


test_process()
