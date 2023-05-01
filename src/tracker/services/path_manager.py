import tempfile
import time
import os

class PathManager:
    def __init__(self):
        print("ImageManager init")

    def create_video_temp_path(self):
        image_path = tempfile.gettempdir()
        return os.path.abspath(image_path + "/video_" + str(int(time.time())) + ".mp4")

    def create_recording_path(self, subfolder=''):
        if subfolder:
            return os.path.abspath('./data/recordings/' + f'{subfolder}')
        return os.path.abspath('./data/recordings')

    def create_untrained_path(self, subfolder=''):
        if subfolder:
            return os.path.abspath('././data/untrained/' + f'{subfolder}')
        return os.path.abspath('./data/untrained')

    def create_image_temp_path(self):
        image_path = tempfile.gettempdir()
        return os.path.abspath(image_path + "/image/" + str(int(time.time())))

    def get_trained_path(self):
        print(os.path.abspath('./data/trained'))
        return os.path.abspath('./data/trained')
