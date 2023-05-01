from setuptools import setup

from src.tracker.entity.base_model import database
from src.tracker.entity.event import Event
from src.tracker.entity.subject import Subject


def initialize_database():
    database.connect()
    database.create_tables([Subject, Event])



setup(
    name='bird-tracker',
    version='0.0.1',
    packages=['src'],
    url='https://github.com/boscho87/bird-tracker',
    license='MIT',
    requires=['requirements.txt'],
    author='boscho87',
    author_email='simon.d.mueller@gmail.com',
    description='Bird-Tracker - Birdly DIY Project',
)

initialize_database()
