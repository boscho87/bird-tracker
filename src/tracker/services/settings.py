import platform

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

    @staticmethod
    def frames_per_shot():
        return int(os.getenv('FRAMES_PER_SHOT')) if os.getenv('FRAMES_PER_SHOT') not in [None, ''] else 60

    @staticmethod
    def get_prediction_threshold():
        return int(os.getenv('PREDICTION_THRESHOLD')) if os.getenv('PREDICTION_THRESHOLD') not in [None, ''] else 75

    @staticmethod
    def use_cap_dshow():
        use_cap_dshow = os.getenv('USE_CAP_DSHOW')
        return bool(int(use_cap_dshow)) if use_cap_dshow not in [None, ''] else False

    @staticmethod
    def get_db_file_path():
        return os.getenv('DB_FILE_PATH') if os.getenv('DB_FILE_PATH') not in [None, ''] else 'data/db.sqlite'

    @staticmethod
    def use_gpio():
        return bool(int(os.getenv('USE_GPIO'))) if os.getenv('USE_GPIO') not in [None, ''] else False
