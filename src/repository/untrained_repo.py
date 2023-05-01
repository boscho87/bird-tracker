import os
import shutil

from src.tracker.entity.image import Image
from src.tracker.entity.sequence import Sequence
from src.tracker.services.path_manager import PathManager


class UntrainedRepo:
    path_manager: PathManager

    def __init__(self):
        print("UntrainedRepo init")
        self.path_manager = PathManager()

    def store_image(self, image: Image, prefix: str):
        save_path = os.path.join(self.path_manager.create_untrained_path(), prefix)
        file_name = prefix + "-" + image.get_file_name()
        target_path = os.path.join(save_path, file_name)
        os.makedirs(save_path, exist_ok=True)
        shutil.copy(image.get_file_path(), target_path)

    def store_sequence(self, sequence: Sequence):
        print("UntrainedRepo store_sequence")
        images = sequence.get_images()
        for image in images:
            self.store_image(image, str(sequence.get_time()))

    def get_sequence(self, timestamp):
        # Todo implement
        return None

    def get_sequences(self):
        # Todo retrun all untrained sequences (limit by eg. 20)
        return None

    def remove_sequence(self, timestamp):
        # Todo implement
        return None
