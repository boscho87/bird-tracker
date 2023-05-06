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
            # Todo FIX ORM, why only ids are returned
            video = self.capturer.capture()
            images = self.sequence_splitter.video_to_image_sequence(video)
            subject = Subject.create(images=images, videos=[video])
            event = self.predictor.predict(subject)

            if isinstance(event, Event):
                # Todo save logic into repository
                logging.info("Match found")

                # save_path = self.path_manager.create_recording_path()
                # match_path = match.get_sequence().get_video_path()
                # output_path = os.path.join(save_path, str(video_sequence.get_time()) + "-.mp4")
                # shutil.copy(match_path, output_path)
                # logging.info("Match found")
                ## event.subject = match.get_subject() ##Todo implement
                # event.known = True
                # event.save()
                # logging.debug("Pause for 5 seconds")
                # time.sleep(Settings.get_pause_time())
                # self.wait_for_input()
                return True

            return False
            # store the data into a db
            # send notification @given time if there are new events
            self.untrained_repo.store_sequence(video_sequence)
            event.save()
            print("No match found")
            print("Pause for 5 seconds")
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
