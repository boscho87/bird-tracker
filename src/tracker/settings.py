from dotenv import load_dotenv
import os

load_dotenv('.env.default')
load_dotenv('.env')


class Settings:

    @staticmethod
    def get_camera_id():
        return int(os.getenv('CAM_ID')) if os.getenv('CAM_ID') not in [None, ''] else 0

    @staticmethod
    def get_image_width():
        return int(os.getenv('IMAGE_WIDTH')) if os.getenv('IMAGE_WIDTH') not in [None, ''] else 640

    @staticmethod
    def get_image_height():
        return int(os.getenv('IMAGE_HEIGHT')) if os.getenv('IMAGE_HEIGHT') not in [None, ''] else 480
