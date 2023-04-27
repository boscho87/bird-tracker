import tempfile
import time


class FileManager:
    def __init__(self):
        #Todo move the the path to the constructor
        print("ImageManager init")

    def create_video_temp_path(self):
        image_path = tempfile.gettempdir()
        return image_path + "/video_" + str(int(time.time())) + ".mp4"

    def create_recording_path(self, subfolder=''):
        if subfolder:
            return './data/recordings/' + f'{subfolder}'
        return './data/recordings'

    def create_untrained_path(self, subfolder=''):
        if subfolder:
            return './data/untrained/' + f'{subfolder}'
        return './data/untrained'
