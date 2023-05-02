import time
import cv2

from src.tracker.services.sequencesplitter import SequenceSplitter
from src.tracker.services.settings import Settings
from src.tracker.services.path_manager import PathManager
from src.tracker.entity.sequence import Sequence


class Capturer:
    path_manager: PathManager
    image_height: int
    image_width: int
    sequence_splitter: SequenceSplitter

    def __init__(self):
        self.retired = None
        self.path_manager = PathManager()
        self.image_height = Settings.get_image_height()
        self.image_width = Settings.get_image_width()
        self.sequence_splitter = SequenceSplitter()
        print("Capturer init")

    def capture(self) -> Sequence:
        print("Capturer capture")
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
                print("Error: Webcam could not capture frame")
                break
            out.write(frame)
        out.release()
        cap.release()
        cv2.destroyAllWindows()
        sequence = Sequence(filename, int(time.time_ns() / 1000000000))
        images = self.sequence_splitter.split_sequence_to_images(sequence)
        sequence.set_images(images)
        return sequence

    def get_capture(self):
        try:
            print("Cam-ID:", Settings.get_camera_id())
            if Settings.use_cap_dshow():
                print("Using CAP_DSHOW")
                return cv2.VideoCapture(Settings.get_camera_id(), cv2.CAP_DSHOW)
            else:
                print("Using default")
                return cv2.VideoCapture(Settings.get_camera_id())
        except Exception as e:
            print("Error: Webcam could not be opened")
            print(e)

    def generate_frames(self):
        camera = self.get_capture()  # Öffnet die Kamera
        while True:
            success, frame = camera.read()  # Liest ein Frame von der Kamera
            if not success:
                break
            # Konvertiert das Frame in ein JPEG-Bild
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # Generiert das nächste Frame
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
