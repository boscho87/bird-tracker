import logging
from typing import List

from src.tracker.entity.image import Image
from src.tracker.entity.subject import Subject
from src.tracker.entity.video import Video
from src.tracker.services.path_manager import PathManager


class SubjectRepository:
    def __init__(self):
        self.path_manager = PathManager()

    def create_or_update(self, subject: Subject):
        if subject.trained:
            for video in subject.get_videos():
                print(f'old_filepath trained: {video.filepath}')
                new_filepath = self.path_manager.move_video_to_trained(video, subject.slug)
                print(f'new_filepath trained: {new_filepath}')
                Video(id=video.id, filepath=new_filepath, subject=subject).save()
            for image in subject.get_images():
                print(f'old_filepath trained: {image.filepath}')
                new_filepath = self.path_manager.move_image_to_trained(image, subject.slug)
                print(f'new_filepath trained: {new_filepath}')
                Image(id=image.id, filepath=new_filepath, subject=subject).save()
        else:
            for video in subject.get_videos():
                new_filepath = self.path_manager.move_video_to_untrained(video, subject.slug)
                Video(id=video.id, filepath=new_filepath, subject=subject.id).save()
            for image in subject.get_images():
                new_filepath = self.path_manager.move_image_to_untrained(image, subject.slug)
                Image(id=image.id, filepath=new_filepath, subject=subject.id).save()
        print("Saving subject")
        subject.save()
