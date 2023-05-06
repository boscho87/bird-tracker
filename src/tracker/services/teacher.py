from src.repository.trained_repo import TrainedRepo
from src.repository.untrained_repo import UntrainedRepo
from src.tracker.entity.sequence import VideoSequence
from src.tracker.entity.subject import Subject
from src.tracker.services.path_manager import PathManager


class Teacher:
    path_manager: PathManager
    untrained_repo: UntrainedRepo
    trained_repo: TrainedRepo

    def __init__(self):
        self.path_manager = PathManager()
        self.untrained_repo = UntrainedRepo()
        self.trained_repo = TrainedRepo()

    # todo implement that untrained images can be fetched in a "sequence" object
    def teach_subject(self, id: int, sequence: VideoSequence):
        subject = Subject.get_by_id(id)
        image_dir = subject.get_store_path()
        for image in sequence.get_images():
            self.trained_repo.store_image(image, image_dir)

    def teach_new_subject(self, name: str, sequence: VideoSequence):
        store_path = self.trained_repo.store_sequence(sequence, name)
        self.trained_repo.store_sequence(sequence, name)
        subject = Subject.create(name=name, store_path=store_path)
        subject.save()
        return subject
