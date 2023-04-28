import os

from src.tracker.entity.image import Image
from src.tracker.services.path_manager import PathManager


class TrainedRepo:
    path_manager: PathManager

    def __init__(self):
        self.path_manager = PathManager()

    def get_trained_images(self):
        output_files = []
        directory = self.path_manager.get_trained_path()
        subjects = os.listdir(directory)
        for subject in subjects:
            subject_path = os.path.join(directory, subject)
            subject_images = os.listdir(subject_path)
            for subject_image in subject_images:
                if subject_image.endswith(".jpg"):
                    image_path = os.path.join(subject_path, subject_image)
                    image = Image(image_path)
                    output_files.append(image)
        #Todo extract images in groups of subjects
        print(output_files)
        return output_files
