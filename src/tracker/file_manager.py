import tempfile
import time


class FileManager:
    def __init__(self):
        print("ImageManager init")

    def create_video_temp_path(self):
        image_path = tempfile.gettempdir()
        return image_path + "/video_" + str(int(time.time())) + ".mp4"

    def create_recording_path(self):
        return './recordings'
