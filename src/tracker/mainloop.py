from src.tracker.capturer import Capturer
from src.tracker.entity.match import Match
from src.tracker.file_manager import FileManager
from src.tracker.predictor import Predictor
from src.tracker.sequencesplitter import SequenceSplitter


class MainLoop:
    predictor: Predictor
    capturer: Capturer
    sequence_splitter: SequenceSplitter

    def __init__(self):
        self.predictor = Predictor()
        self.capturer = Capturer()
        self.sequence_splitter = SequenceSplitter()
        self.file_manager = FileManager()

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

        self.sequence_splitter.splitSequenceToImages(sequence, self.file_manager.create_untrained_path())
        # store the data into a db
        # send notification @given time if there are new events
        print("No match found")
