from peewee import *

from src.tracker.entity.base_model import BaseModel


class Subject(BaseModel):
    id = AutoField()
    name = CharField()


# #how to use
# # Daten erstellen
# subject = Subject.create(name='Math')
#
# # Daten abfragen
# subjects = Subject.select()
# for subject in subjects:
#     print(subject.id, subject.name)
#
# # Daten aktualisieren
# subject.name = 'Mathematics'
# subject.save()
#
# # Daten löschen
# subject.delete_instance()
