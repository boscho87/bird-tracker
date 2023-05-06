import logging
import os
import tempfile
import time

from src.tracker.services.settings import Settings


class PathManager:
    def __init__(self):
        logging.debug("PathManager init")
        self.project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

    def create_video_temp_path(self):
        image_path = tempfile.gettempdir()
        return os.path.abspath(image_path + "/video_" + str(int(time.time())) + ".mp4")

    def create_recording_path(self, subfolder=''):
        if subfolder:
            path = os.path.abspath(os.path.join(self.project_path, 'data', 'recordings', subfolder))
            self.mkdir(path)
            return path
        path = os.path.abspath(os.path.join(self.project_path, 'data', 'recordings'))
        self.mkdir(path)
        return path

    def create_untrained_path(self, subfolder=''):
        if subfolder:
            path = os.path.abspath(os.path.join(self.project_path, 'data', 'untrained', subfolder))
            self.mkdir(path)
            return path
        path = os.path.abspath(os.path.join(self.project_path, 'data', 'untrained'))
        self.mkdir(path)
        return path

    def create_image_temp_path(self):
        image_path = tempfile.gettempdir()
        return os.path.abspath(image_path + "/image/" + str(int(time.time())))

    def get_trained_path(self, subfolder=''):
        if subfolder:
            path = os.path.abspath(os.path.join(self.project_path, 'data', 'trained', subfolder))
            self.mkdir(path)
            return path
        path = os.path.abspath(os.path.join(self.project_path, 'data', 'trained'))
        self.mkdir(path)
        return path

    def mkdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            os.chmod(path, 0o775)
            os.chown(path, -1, Settings.get_data_group_id())
