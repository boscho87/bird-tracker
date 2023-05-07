from peewee import *
from slugify import slugify

from src.tracker.entity.base_model import BaseModel


class Subject(BaseModel):
    trained = BooleanField(default=False)
    id = AutoField()
    slug = CharField(unique=True, default=None, null=True)
    name = CharField(null=True, default=None)
    highest_mean_square_error = FloatField(null=True, default=None)

    def get_images(self):
        return list(self.images)

    def get_videos(self):
        return list(self.videos)
