from peewee import *

from src.tracker.entity.base_model import BaseModel
from src.tracker.entity.subject import Subject


class Event(BaseModel):
    id = AutoField()
    known = BooleanField(default=False)
    subject = ForeignKeyField(Subject, null=True)
    time = BigIntegerField()

