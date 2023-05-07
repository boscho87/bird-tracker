from datetime import datetime

from peewee import *

from src.tracker.entity.base_model import BaseModel
from src.tracker.entity.subject import Subject


class Event(BaseModel):
    id = AutoField()
    time = DateTimeField(default=datetime.now)
    known = BooleanField(default=False)
    subject = ForeignKeyField(Subject, null=True)

