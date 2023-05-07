from src.tracker.entity.base_model import database
from src.tracker.entity.event import Event
from src.tracker.entity.image import Image
from src.tracker.entity.subject import Subject
from src.tracker.entity.video import Video
from src.tracker.services.path_manager import PathManager
from src.tracker.services.settings import Settings


def initialize_database():
    path_manager = PathManager()
    path_manager.create_data_dir()
    print(Settings.get_db_file_path())
    database.connect()
    database.create_tables([Subject, Event, Image, Video])
    print('Database initialized')


initialize_database()
