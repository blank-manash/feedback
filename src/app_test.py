from src.constants import get_database
from src.persistence import MODEL_LIST

db = get_database()

db.connect()
db.close()

print("Hello World")