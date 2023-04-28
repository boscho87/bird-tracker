import os
import shutil

from src.tracker.services.capturer import Capturer
from src.tracker.entity.match import Match
from src.tracker.services.path_manager import PathManager
from src.tracker.services.predictor import Predictor
from src.tracker.services.sequencesplitter import SequenceSplitter


class MainLoop:
    predictor: Predictor
    capturer: Capturer
    sequence_splitter: SequenceSplitter

    def __init__(self):
        self.predictor = Predictor()
        self.capturer = Capturer()
        self.sequence_splitter = SequenceSplitter()
        self.path_manager = PathManager()

    def execute(self):
        print("MainLoop execute")
        sequence = self.capturer.capture()
        match = self.predictor.predict(sequence)

        if isinstance(match, Match):
            # store the sequence mp4
            # store event with path to the mp4 in the db
            # send notification @given time if there are new events
            print("Match found")
            return

        # store the sequence mp4
        images = sequence.get_images()
        for image in images:
            save_path = self.path_manager.create_untrained_path()
            target_path = os.path.join(save_path, image.get_file_name()) #todo move this
            os.makedirs(target_path)
            shutil.move(image.get_file_path(), target_path)

        # store the data into a db
        # send notification @given time if there are new events
        print("No match found")
