from peewee import *

from src.tracker.entity.base_model import BaseModel


class Subject(BaseModel):
    id = AutoField()
    name = CharField()
    store_path = CharField()
    sequences = []
