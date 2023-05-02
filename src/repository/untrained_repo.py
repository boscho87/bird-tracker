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
        shutil.copy(image.get_file_path(), target_path)

    def store_sequence(self, sequence: Sequence):
        print("UntrainedRepo store_sequence")
        images = sequence.get_images()
        for image in images:
            self.store_image(image, str(sequence.get_time()))

    def get_sequence(self, timestamp: int) -> Sequence:
        sequence = Sequence(None, timestamp)
        for root, dirs, files in os.walk(self.path_manager.create_untrained_path()):
            for file in files:
                filename = os.path.join(root, file)
                dirname = os.path.dirname(filename).split("\\")[-1]
                file_path = dirname + "/" + file
                image = Image(file_path)
                sequence.add_image(image)
        return sequence

    def get_sequences(self):
        sequences = []
        for root, dirs, files in os.walk(self.path_manager.create_untrained_path()):
            if root.endswith("untrained"):
                continue
            sequence = Sequence(None, root)
            sequences.append(sequence)
            for path in files:
                path = os.path.join(root, path)
                image = Image(path)
                sequence.time = image.get_file_path().split("\\")[-2]
                sequence.add_image(image)

        return sequences

    def remove_sequence(self, timestamp):
        # Todo implement
        return None
