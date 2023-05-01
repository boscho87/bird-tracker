from src.tracker.entity.image import Image


class Sequence:
    def __init__(self, video_path: str = None, time: int = 0, images=None):
        if images is None:
            images = []
        self.images = images
        self.time = time
        self.file_path = video_path
        print("Sequence init")

    def get_video_path(self):
        return self.file_path

    def get_time(self):
        return self.time

    def set_images(self, images):
        for image in images:
            isinstance(image, Image)
            self.images.append(image)

    def get_images(self):
        return self.images
