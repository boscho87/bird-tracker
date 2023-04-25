from src.tracker.capturer import Capturer
from src.tracker.entity.match import Match
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

    def execute(self):
        print("MainLoop execute")
        sequence = self.capturer.capture()
        # check if we know the bird
        match = self.predictor.predict(sequence)

        if isinstance(match, Match):
            # store the sequence mp4
            # store event with path to the mp4 in the db
            # send notification @given time if there are new events
            print("Match found")
            return

        self.sequence_splitter.splitSequenceToImages(sequence)
        print("No match found")
        # wenn es keinen match gibt, sequence/bilder für späteres training speichern
        # counter in der DB erhöhen
        # Von Zeit zu Zeit notification senden, dass es bilder fürs training gibt
