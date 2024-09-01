import uuid

from src.persistence.models.point import Point

def create_point(description: str,card_id:str) -> str:
    _id = uuid.uuid4()
    point = Point(id=_id, description=description, card_id=card_id, no_of_complaints = 0)
    return point.save()

def update_point(point_id:str,description: str,card_id:str) -> bool:
    return (Point
            .update(description=description,card_id=card_id)
            .where(Point.id == point_id)
            .execute()) == 1

def increase_complaints_on_card(card_id:str) -> int:
    return (Point
            .update(no_of_complaints = Point.no_of_complaints+1)
            .where(Point.id == card_id)
            .execute()) == 1

def read_point(point_id:str) -> Point:
    return Point.get_by_id(point_id)

def delete_point(point_id:str) -> bool:
    return (Point
            .delete()
            .where(Point.id == point_id)
            .execute()) == 1

