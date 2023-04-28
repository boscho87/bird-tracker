class Image:
    filepath: str

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_file_path(self):
        return self.filepath
