from slugify import slugify

from src.repository.subject_repository import SubjectRepository
from src.tracker.entity.subject import Subject
from src.tracker.services.path_manager import PathManager


class Trainer:
    def __init__(self):
        self.subject_repo = SubjectRepository()
        self.path_manager = PathManager()

    def example(self):
        # Todo move this to a web route, where "subjects" can be created  to train the model
        subjects = Subject.select().where(Subject.trained == False)
        for subject in subjects:
            old_slug = None
            if subject.slug:
                old_slug = subject.slug
            subject.name = "Simon mit Cap"
            subject.slug = slugify(subject.name)
            self.train(subject, old_slug)

    def train(self, subject: Subject, old_slug: str = None):
        existing_subject = Subject.get_or_none(slug=subject.slug, trained=True)
        if existing_subject:
            print("Updating existing subject")
            existing_subject.images = subject.images
            existing_subject.videos = subject.videos
            self.subject_repo.create_or_update(existing_subject)
            subject.delete_instance()
            return
        subject.trained = True
        self.subject_repo.create_or_update(subject)
        if old_slug:
            self.path_manager.remove_untrained_dir(old_slug)
