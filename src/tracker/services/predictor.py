import logging
from datetime import datetime

import cv2
import numpy as np

from src.repository.subject_repository import SubjectRepository
from src.tracker.entity.event import Event
from src.tracker.entity.subject import Subject
from src.tracker.services.path_manager import PathManager
from src.tracker.services.settings import Settings


class Predictor:
    def __init__(self):
        self.path_manager = PathManager()
        self.subject_repo = SubjectRepository()

    def predict(self, current_subject: Subject):

        logging.info("Predictor predict")
        subject_images = list(current_subject.images)
        current_images = self.get_x_current_images(list(subject_images), 3)
        trained_subjects = Subject.select().where(Subject.trained == True)
        for trained_subject in trained_subjects:
            trained_images = self.get_x_current_images(trained_subject.get_images(), 3)
            subject_mean_squared_error = 0
            for trained_image in trained_images:
                trained_image_array = cv2.imread(trained_image.filepath)
                for current_image in current_images:
                    current_image_array = cv2.imread(current_image.filepath)
                    mean_squared_error = np.mean((trained_image_array - current_image_array) ** 2)
                    logging.debug("mean_squared_error: " + str(mean_squared_error))
                    if mean_squared_error > subject_mean_squared_error:
                        subject_mean_squared_error = mean_squared_error
                        trained_subject.highest_mean_square_error = mean_squared_error
                    if self.is_match(mean_squared_error):
                        print("Match found")
                        return self.create_event(mean_squared_error, trained_subject, current_subject)

        highest_mean_squared_error = 0
        sorted_subjects = self.sort_subjects_by_mse(trained_subjects)
        logging.debug("Check sorted subjects")
        for sorted_subject in sorted_subjects:
            for trained_image in trained_images:
                trained_image_array = cv2.imread(trained_image.filepath)
            for current_image in current_images:
                current_image_array = cv2.imread(current_image.filepath)
                mean_squared_error = np.mean((trained_image_array - current_image_array) ** 2)
                if mean_squared_error > highest_mean_squared_error:
                    highest_mean_squared_error = mean_squared_error
                logging.debug("mean_squared_error: " + str(mean_squared_error))
                if self.is_match(mean_squared_error):
                    return self.create_event(mean_squared_error, sorted_subject, current_subject)

        current_subject.slug = str(datetime.now().timestamp())
        current_subject.highest_mean_square_error = highest_mean_squared_error
        self.subject_repo.create_or_update(current_subject)
        Event(subject=current_subject, known=False).save()

        return None

    def create_event(self, mean_squared_error, existing_subject, current_subject):
        existing_subject.highest_mean_square_error = mean_squared_error
        existing_subject.images = current_subject.images
        existing_subject.videos = current_subject.videos
        print(len(existing_subject.get_images()))
        self.subject_repo.create_or_update(existing_subject)
        event = Event.create(subject=existing_subject, known=True)
        return event

    def sort_subjects_by_mse(self, trained_subjects):
        return sorted(trained_subjects, key=lambda x: x.highest_mean_square_error, reverse=True)

    def get_x_current_images(self, current_images, x):
        if len(current_images) <= x:
            return current_images
        num_groups = len(current_images) // x
        num_images = num_groups * x
        return [current_images[i] for i in range(0, num_images, x)]

    def is_match(self, mean_squared_error):
        return mean_squared_error < Settings.get_prediction_threshold()
