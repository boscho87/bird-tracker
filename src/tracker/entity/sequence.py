from src.tracker.entity.image import Image


class Sequence:
    def __init__(self, file_path: str, time: int):
        self.images = []
        self.time = time
        self.file_path = file_path
        print("Sequence init")

    def get_file_path(self):
        return self.file_path

    def get_time(self):
        return self.time

    def set_images(self, images):
        for image in images:
            isinstance(image, Image)
            self.images.append(image)

    def get_images(self):
        return self.images
