import cv2
import numpy as np

from src.repository.trained_repo import TrainedRepo
from src.tracker.entity.match import Match
from src.tracker.entity.sequence import Sequence
from src.tracker.services.path_manager import PathManager
from src.tracker.services.sequencesplitter import SequenceSplitter
from src.tracker.services.settings import Settings


class Predictor:
    def __init__(self):
        self.trained_repo = TrainedRepo()
        self.path_manager = PathManager()
        self.sequence_splitter = SequenceSplitter()
        print("Predictor init")

    def predict(self, sequence: Sequence):
        print("Predictor predict")
        current_images = self.sequence_splitter.split_sequence_to_images(sequence)
        sequence.set_images(current_images)
        trained_images = self.trained_repo.get_trained_images()
        for sequence_image in current_images:
            sequence_image_array = cv2.imread(sequence_image.get_file_path())
            for trained_image in trained_images:
                trained_image_array = cv2.imread(trained_image.get_file_path())
                #    trained_image_resized = cv2.resize(trained_image_array, (sequence_image_array.shape[1], sequence_image_array.shape[0]))
                mean_squared_error = np.mean((trained_image_array - sequence_image_array) ** 2)
                threshold = Settings.get_prediction_threshold()
                print(mean_squared_error)
                if mean_squared_error < threshold:
                    return Match('name', 10, sequence)

        return True
