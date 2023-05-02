from src.tracker.entity.base_model import database
from src.tracker.entity.event import Event
from src.tracker.entity.subject import Subject
from src.tracker.services.settings import Settings


def initialize_database():
    print(Settings.get_db_file_path())
    database.connect()
    database.create_tables([Subject, Event])
    print('Database initialized')

initialize_database()
