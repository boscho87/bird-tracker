from peewee import *
from slugify import slugify

from src.tracker.entity.base_model import BaseModel


class Subject(BaseModel):
    slug = CharField(unique=True, index=True)
    name = CharField()
    store_path = CharField()
    sequences = []

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

