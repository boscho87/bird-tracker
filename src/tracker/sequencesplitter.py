import os
import cv2
from src.tracker.entity.sequence import Sequence
from src.tracker.file_manager import FileManager


class SequenceSplitter:
    file_manager: FileManager

    def __init__(self):
        self.file_manager = FileManager()

    def splitSequenceToImages(self, sequence: Sequence):
        output_path = self.file_manager.create_recording_path()
        try:
            cap = cv2.VideoCapture(sequence.get_file_path())
            while cap.isOpened():
                ret, frame = cap.read()
                if ret == True:
                    if not os.path.exists(output_path):
                        os.makedirs(output_path)
                    path, dirs, files = next(os.walk(output_path))
                    file_count = len(files)
                    filepath = os.path.join(output_path, f'{sequence.get_time()}-{file_count + 1}.jpg')
                    cv2.imwrite(filepath, frame)
                else:
                    break
        except:
            pass
