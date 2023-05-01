from peewee import *

from src.tracker.services.settings import Settings

database = SqliteDatabase(Settings.get_db_file_path())


class BaseModel(Model):
    class Meta:
        database = database
        legacy_table_names = False
