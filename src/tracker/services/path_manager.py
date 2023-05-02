import os
import tempfile
import time


class PathManager:
    def __init__(self):
        print("PathManager init")
        self.project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

    def create_video_temp_path(self):
        image_path = tempfile.gettempdir()
        return os.path.abspath(image_path + "/video_" + str(int(time.time())) + ".mp4")

    def create_recording_path(self, subfolder=''):
        if subfolder:
            path = os.path.abspath(os.path.join(self.project_path, 'data', 'recordings', subfolder))
            if not os.path.exists(path):
                os.makedirs(path)
            return path

        path = os.path.abspath(os.path.join(self.project_path, 'data', 'recordings'))
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def create_untrained_path(self, subfolder=''):
        if subfolder:
            path = os.path.abspath(os.path.join(self.project_path, 'data', 'untrained', subfolder))
            if not os.path.exists(path):
                os.makedirs(path)
            return path
        path = os.path.abspath(os.path.join(self.project_path, 'data', 'untrained'))
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def create_image_temp_path(self):
        image_path = tempfile.gettempdir()
        return os.path.abspath(image_path + "/image/" + str(int(time.time())))

    def get_trained_path(self, subfolder=''):
        if subfolder:
            path = os.path.abspath(os.path.join(self.project_path, 'data', 'trained', subfolder))
            if not os.path.exists(path):
                os.makedirs(path)
            return path
        path = os.path.abspath(os.path.join(self.project_path, 'data', 'trained'))
        if not os.path.exists(path):
            os.makedirs(path)
        return path
