import os
import shutil
import sys
import time

from src.repository.untrained_repo import UntrainedRepo
from src.tracker.entity.event import Event
from src.tracker.services.capturer import Capturer
from src.tracker.entity.match import Match
from src.tracker.services.path_manager import PathManager
from src.tracker.services.predictor import Predictor
from src.tracker.services.sequencesplitter import SequenceSplitter
from src.tracker.services.settings import Settings


class MainLoop:
    predictor: Predictor
    capturer: Capturer
    sequence_splitter: SequenceSplitter
    untrained_repo: UntrainedRepo

    def __init__(self):
        self.predictor = Predictor()
        self.capturer = Capturer()
        self.sequence_splitter = SequenceSplitter()
        self.path_manager = PathManager()
        self.untrained_repo = UntrainedRepo()

    def execute(self):
        print("MainLoop execute")
        while True:
            sequence = self.capturer.capture()
            match = self.predictor.predict(sequence)
            event = Event.create(time=sequence.get_time())
            if isinstance(match, Match):
                save_path = self.path_manager.create_recording_path()
                match_path = match.get_sequence().get_video_path()
                output_path = os.path.join(save_path, str(sequence.get_time()) + "-match.mp4")
                shutil.copy(match_path, output_path)
                # store the sequence mp4
                # store event with path to the mp4 in the db
                # send notification @given time if there are new events
                print("Match found")
                # event.subject = match.get_subject() ##Todo implement
                event.known = True
                event.save()
                time.sleep(5)
                self.wait_for_input()
                return True

            # store the data into a db
            # send notification @given time if there are new events
            self.untrained_repo.store_sequence(sequence)
            event.save()
            print("No match found")
            time.sleep(5)
            self.wait_for_input()

    def wait_for_input(self):
        if Settings.use_gpio():
            print("Waiting for GPIO")
            self.wait_for_gpio()
        else:
            if sys.stdin.isatty():
                input("Drücke Enter, um fortzufahren...")
            else:
                print('Start with tty otherwise you got an infinite loop')
                exit(100)

    def wait_for_gpio(self):
        import RPi.GPIO as GPIO
        wire1_pin = 17
        wire2_pin = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(wire1_pin, GPIO.IN)
        GPIO.setup(wire2_pin, GPIO.IN)

        while not (GPIO.input(wire1_pin) and GPIO.input(wire2_pin)):
            pass
        GPIO.cleanup()
        return True
