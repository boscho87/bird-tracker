import os
import shutil

from src.functions import create_slug
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
            if os.path.isdir(subject_path):
                subject_images = os.listdir(subject_path)
                for subject_image in subject_images:
                    if subject_image.endswith(".jpg"):
                        image_path = os.path.join(subject_path, subject_image)
                        image = Image(image_path)
                        output_files.append(image)
        # Todo extract images in groups of subjects
        print("Es gibt " + str(len(output_files)) + " Bilder zu prüfen")
        return output_files

    def get_subjects(self):
        # Todo implement return a collection of images the collection should contain images & species id and name
        return None

    def store_image(self, image: Image, image_path):
        target_path = os.path.join(image_path, image.get_file_name())
        shutil.copy(image.get_file_path(), target_path)

    def store_sequence(self, sequence, name):
        image_path = self.path_manager.get_trained_path(create_slug(name))
        images = sequence.get_images()
        for image in images:
            self.store_image(image, str(sequence.get_time()))

        return image_path
