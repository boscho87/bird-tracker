import logging
import sys
import time

from src.tracker.entity.event import Event
from src.tracker.entity.subject import Subject
from src.tracker.services.capturer import Capturer
from src.tracker.services.path_manager import PathManager
from src.tracker.services.predictor import Predictor
from src.tracker.services.sequencesplitter import SequenceSplitter
from src.tracker.services.settings import Settings


class MainLoop:
    predictor: Predictor
    capturer: Capturer
    sequence_splitter: SequenceSplitter

    def __init__(self):
        self.capturer = Capturer()
        self.predictor = Predictor()
        self.sequence_splitter = SequenceSplitter()
        self.path_manager = PathManager()

    def execute(self):
        logging.debug("MainLoop execute")
        while True:
            video = self.capturer.capture()
            images = self.sequence_splitter.video_to_image_sequence(video)
            subject = Subject.create(images=images, videos=[video], trained=False)
            event = self.predictor.predict(subject)
            print("event: " + str(event))
            print("Todo remove close")
            exit(0)
            if isinstance(event, Event):
                logging.info("Match found")
                logging.debug("Event: " + str(event.subject.slug))
                continue

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
