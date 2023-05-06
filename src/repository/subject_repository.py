from typing import Union, List
from src.tracker.entity.subject import Subject


class SubjectRepository:

    def create(self, subject: Subject) -> Subject:
        subject.save()
        return subject

    def get_by_id(self, subject_id: int) -> Subject:
        return Subject.get_or_none(id=subject_id)

    def get_all(self) -> List[Subject]:
        return Subject.select()

    def update(self, subject: Subject) -> Subject:
        if subject.id:
            subject.save()
            return subject
        return None

    def delete(self, subject: Subject) -> bool:
        if subject.id:
            subject.delete_instance()
            return True
        return False

    def create_or_update(self, subject: Subject) -> Union[Subject, None]:
        existing_subject = self.get_by_id(subject.id)
        if existing_subject:
            subject.id = existing_subject.id
            return self.update(subject)
        else:
            return self.create(subject)
