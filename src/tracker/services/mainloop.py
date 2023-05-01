import os
import shutil

from src.repository.untrained_repo import UntrainedRepo
from src.tracker.entity.event import Event
from src.tracker.services.capturer import Capturer
from src.tracker.entity.match import Match
from src.tracker.services.path_manager import PathManager
from src.tracker.services.predictor import Predictor
from src.tracker.services.sequencesplitter import SequenceSplitter


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
        sequence = self.capturer.capture()
        match = self.predictor.predict(sequence)

        event = Event.create(time=sequence.get_time())

        if isinstance(match, Match):
            save_path = self.path_manager.create_recording_path()
            os.makedirs(save_path, exist_ok=True)
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
            return

        self.untrained_repo.store_sequence(sequence)

        # store the data into a db
        # send notification @given time if there are new events
        event.save()
        print("No match found")
