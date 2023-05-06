import logging

import cv2

from src.tracker.entity.video import Video
from src.tracker.services.settings import Settings
from src.tracker.services.path_manager import PathManager


class Capturer:
    path_manager: PathManager
    image_height: int
    image_width: int

    def __init__(self):
        self.retired = None
        self.path_manager = PathManager()
        self.image_height = Settings.get_image_height()
        self.image_width = Settings.get_image_width()

    def capture(self):
        filename = self.path_manager.create_video_temp_path()
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        cap = self.get_capture()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.image_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.image_height)
        out = cv2.VideoWriter(filename, fourcc, 20.0, (self.image_width, self.image_height))
        # 60 Frames = 3 seconds on 20 fps Todo resolve magic number
        for i in range(Settings.frames_per_shot()):
            ret, frame = cap.read()
            if not ret:
                logging.error("Webcam could not capture frame")
                break
            out.write(frame)
        out.release()
        cap.release()
        cv2.destroyAllWindows()
        video = Video()
        video.filepath = filename
        return video

    def get_capture(self):
        try:
            logging.debug("Cam-ID: " + str(Settings.get_camera_id()))
            if Settings.use_cap_dshow():
                logging.debug("Using CAP_DSHOW")
                return cv2.VideoCapture(Settings.get_camera_id(), cv2.CAP_DSHOW)
            else:
                logging.debug("Using default webcam config")
                return cv2.VideoCapture(Settings.get_camera_id())
        except Exception as e:
            logging.exception(f"Error: Webcam could not be opened [{e}]")

    def generate_frames(self):
        camera = self.get_capture()
        while True:
            success, frame = camera.read()
            if not success:
                break
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
