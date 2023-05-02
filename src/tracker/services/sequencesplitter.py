import os
import cv2

from src.tracker.entity.image import Image
from src.tracker.entity.sequence import Sequence
from src.tracker.services.path_manager import PathManager


class SequenceSplitter:
    path_manager: PathManager

    def __init__(self):
        self.path_manager = PathManager()

    def split_sequence_to_images(self, sequence: Sequence):
        output_path = self.path_manager.create_image_temp_path()
        images = []
        try:
            cap = cv2.VideoCapture(sequence.get_video_path())
            while cap.isOpened():
                ret, frame = cap.read()
                if ret == True:
                    if not os.path.exists(output_path):
                        os.makedirs(output_path)
                    path, dirs, files = next(os.walk(output_path))
                    file_count = len(files)
                    filepath = os.path.join(output_path, f'{file_count + 1}.jpg')
                    cv2.imwrite(filepath, frame)
                    image = Image(filepath)
                    images.append(image)
                else:
                    break
        except:
            print("Error while splitting sequence to images")

        return images
