import logging
import os
import shutil
import subprocess
import tempfile
import time

from slugify import slugify

from src.tracker.services.settings import Settings


class PathManager:
    def __init__(self):
        logging.debug("PathManager init")
        self.project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

    def create_video_temp_path(self):
        video_path = tempfile.gettempdir()
        filename = f'0_{int(time.time())}_sequence.mp4'
        return os.path.abspath(os.path.join(video_path, filename))

    def create_image_temp_path(self, count):
        image_path = self.create_image_dir_temp_path()
        filename = f'{count}-{int(time.time())}.jpg'
        return os.path.abspath(os.path.join(image_path, filename))

    def create_image_dir_temp_path(self):
        image_path = tempfile.gettempdir()
        dir = os.path.join(image_path, 'images')
        if not os.path.exists(dir):
            os.makedirs(dir)
        return dir

    def create_recording_path(self, subfolder=''):
        if subfolder:
            path = os.path.abspath(os.path.join(self.project_path, 'data', 'recordings', subfolder))
            self.mkdir(path)
            return path
        path = os.path.abspath(os.path.join(self.project_path, 'data', 'recordings'))
        self.mkdir(path)
        return path

    def create_trained_path(self, subfolder=''):
        if subfolder:
            path = os.path.abspath(os.path.join(self.project_path, 'data', 'trained', subfolder))
            self.mkdir(path)
            return path
        path = os.path.abspath(os.path.join(self.project_path, 'data', 'trained'))
        self.mkdir(path)
        return path

    def create_untrained_path(self, subfolder=''):
        if subfolder:
            path = os.path.abspath(os.path.join(self.project_path, 'data', 'untrained', subfolder))
            self.mkdir(path)
            return path
        path = os.path.abspath(os.path.join(self.project_path, 'data', 'untrained'))
        self.mkdir(path)
        return path

    def mkdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            os.chmod(path, 0o775)
            if os.name == 'nt':
                subprocess.call(['icacls', path, '/grant', f'{Settings.get_data_group_id()}:(OI)(CI)F'])
            else:
                os.chown(path, -1, Settings.get_data_group_id())

    def move_image_to_trained(self, image, slug):
        subdir = os.path.join(slugify(slug), os.path.dirname(os.path.basename(image.filepath)))
        new_path = self.create_trained_path(subdir)
        new_file_path = os.path.join(new_path, os.path.basename(image.filepath))
        shutil.move(image.filepath, new_file_path)
        return new_file_path

    def move_video_to_trained(self, video, slug):
        subdir = os.path.join(slugify(slug), os.path.dirname(os.path.basename(video.filepath)))
        new_path = self.create_trained_path(subdir)
        new_file_path = os.path.join(new_path, os.path.basename(video.filepath))
        shutil.move(video.filepath, new_file_path)
        return new_file_path

    def move_image_to_untrained(self, image, slug):
        subdir = os.path.join(slugify(slug), os.path.dirname(os.path.basename(image.filepath)))
        new_path = self.create_untrained_path(subdir)
        new_file_path = os.path.join(new_path, slug + "_" + os.path.basename(image.filepath))
        shutil.move(image.filepath, new_file_path)
        return new_file_path

    def move_video_to_untrained(self, video, slug):
        subdir = os.path.join(slugify(slug), os.path.dirname(os.path.basename(video.filepath)))
        new_path = self.create_untrained_path(subdir)
        new_file_path = os.path.join(new_path, os.path.basename(video.filepath))
        shutil.move(video.filepath, new_file_path)
        return new_file_path

    def remove_untrained_dir(self, slug):
        path = self.create_untrained_path(slug)
        print(f'remove_untrained_dir: {path}')
        os.rmdir(path)

    def create_data_dir(self):
        return self.mkdir(os.path.abspath(os.path.join(self.project_path, 'data')))
