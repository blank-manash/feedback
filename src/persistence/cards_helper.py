from src.persistence.models.card import Card

def create_card(title:str)->str:
    card = Card(title=title, no_of_points=0)
    return card.save()

def update_card(card_id:str, title: str)->bool:
    return (Card
            .update(title=title).where(Card.id == card_id)
            .execute()) == 1

def increase_points_on_card(card_id: int)->bool:
    return (Card.update(no_of_points=Card.no_of_points+1)
            .where(Card.id == card_id)
            .execute()) == 1

def read_card(card_id:str)->Card:
    return Card.get_by_id(card_id)