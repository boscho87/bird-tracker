import logging

from peewee import *

from src.tracker.services.settings import Settings

database = SqliteDatabase(Settings.get_db_file_path())


class BaseModel(Model):
    class Meta:
        logging.debug('BaseModel Meta')
        logging.debug(Settings.get_db_file_path())
        database = database
        legacy_table_names = False
