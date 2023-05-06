import shutil

from src.repository.subject_repository import SubjectRepository
from src.tracker.entity.sequence import VideoSequence
from src.tracker.entity.subject import Subject
from src.tracker.services.path_manager import PathManager


class Trainer:
    def __init__(self):
        print("Trainer init")
        self.path_manager = PathManager()
        self.subject_repo = SubjectRepository()

    def train(self, name: str, sequence: VideoSequence):
        print("Trainer train")
        images = sequence.get_images()
        store_path = self.path_manager.get_trained_path(name)
        for image in images:
            shutil.move(image.get_file_path(), store_path)

        subject = Subject(name=name, store_path=store_path)
        self.subject_repo.create_or_update(subject)
