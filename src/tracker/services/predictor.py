import cv2
import numpy as np

from src.repository.trained_repo import TrainedRepo
from src.tracker.entity.sequence import Sequence
from src.tracker.services.path_manager import PathManager
from src.tracker.services.sequencesplitter import SequenceSplitter


class Predictor:
    def __init__(self):
        self.trained_repo = TrainedRepo()
        self.path_manager = PathManager()
        self.sequence_splitter = SequenceSplitter()
        print("Predictor init")

    def predict(self, sequence: Sequence):
        print("Predictor predict")
        sequence_images = self.sequence_splitter.split_sequence_to_images(sequence)
        sequence.set_images(sequence_images)
        trained_images = self.trained_repo.get_trained_images()
        for sequence_image in sequence_images:
            for trained_image in trained_images:
                trained_image = cv2.imread(trained_image.get_file_path())
                sequence_image = cv2.imread(sequence_image.get_file_path())
                trained_image = cv2.resize(trained_image, (sequence_image.shape[1], sequence_image.shape[0]))
                mean_squared_error = np.mean((sequence_image - trained_image) ** 2)
                threshold = 10000
                print(mean_squared_error)
                if mean_squared_error < threshold:
                    print("Match found")





        return None
