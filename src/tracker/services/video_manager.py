import cv2

from src.tracker.services.settings import Settings


class VideoManager:
    def __init__(self):
        print("VideoCapture init")

    def get_video_capture(self):
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
