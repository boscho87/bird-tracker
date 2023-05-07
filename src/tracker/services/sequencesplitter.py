import os
import cv2

from src.tracker.entity.image import Image

from src.tracker.entity.video import Video
from src.tracker.services.path_manager import PathManager


class SequenceSplitter:
    path_manager: PathManager

    def __init__(self):
        self.path_manager = PathManager()

    def video_to_image_sequence(self, video: Video) -> list:
        output_path = self.path_manager.create_image_dir_temp_path()
        images = []
        try:
            cap = cv2.VideoCapture(video.filepath)
            while cap.isOpened():
                ret, frame = cap.read()
                if ret == True:
                    path, dirs, files = next(os.walk(output_path))
                    file_count = len(files)+1
                    filepath = self.path_manager.create_image_temp_path(file_count)
                    cv2.imwrite(filepath, frame)
                    image = Image.create(filepath=filepath)
                    images.append(image)
                else:
                    break
        except Exception as e:
            print("Error while splitting sequence to images")
            print(e)
        return images
