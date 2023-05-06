from peewee import CharField, AutoField, ForeignKeyField

from src.tracker.entity.base_model import BaseModel
from src.tracker.entity.subject import Subject


class Video(BaseModel):
    id = AutoField()
    filepath = CharField(unique=True, index=True)
    videos = ForeignKeyField(Subject, backref='videos', null=True, default=None)
