class Sequence:
    def __init__(self, file_path: str, time: int):
        self.time = time
        self.file_path = file_path
        print("Sequence init")

    def get_file_path(self):
        return self.file_path

    def get_time(self):
        return self.time
