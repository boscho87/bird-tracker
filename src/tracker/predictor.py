from src.tracker.entity.sequence import Sequence
from src.tracker.file_manager import FileManager
from src.tracker.sequencesplitter import SequenceSplitter


class Predictor:
    def __init__(self):
        self.file_manager = FileManager()

        self.sequence_splitter = SequenceSplitter()
        print("Predictor init")

    def predict(self, sequence: Sequence):
        print("Predictor predict")
        self.sequence_splitter.splitSequenceToImages(sequence, self.file_manager.create_video_temp_path())
        return None
