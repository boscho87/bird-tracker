import time
import cv2
from src.tracker.settings import Settings
from src.tracker.file_manager import FileManager
from src.tracker.entity.sequence import Sequence



class Capturer:
    file_manager: FileManager
    image_height: int
    image_width: int
    cap: cv2.VideoCapture

    def __init__(self):
        self.file_manager = FileManager()
        self.image_height = Settings.get_image_height()
        self.image_width = Settings.get_image_width()
        print("Capturer init")
        try:
            print("Cam-ID:", Settings.get_camera_id())
            self.cap = cv2.VideoCapture(Settings.get_camera_id(), cv2.CAP_DSHOW)
        except Exception as e:
            print("Error: Webcam could not be opened")
            print(e)

    def capture(self) -> Sequence:
        print("Capturer capture")
        filename = self.file_manager.create_video_temp_path()
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.image_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.image_height)
        out = cv2.VideoWriter(filename, fourcc, 20.0, (self.image_width, self.image_height))
        # 60 Frames = 3 seconds on 20 fps Todo relolve magic number
        for i in range(60):
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Webcam could not capture frame")
                break
            out.write(frame)
        out.release()
        self.cap.release()
        cv2.destroyAllWindows()
        return Sequence(filename, time.time())
