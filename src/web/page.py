import os

from flask import Flask, render_template, send_from_directory, Response, jsonify

from src.repository.untrained_repo import UntrainedRepo
from src.tracker.services.capturer import Capturer
from src.tracker.services.path_manager import PathManager

app = Flask(__name__)


@app.route('/images/<path:file_path>')
def untrained_images(file_path):
    path_manager = PathManager()
    untrained_dir = path_manager.create_untrained_path()
    return send_from_directory(untrained_dir, file_path)


@app.route('/untrained')
def untrained():
    ##Todo set a Limit
    untrained_repo = UntrainedRepo()
    sequences = untrained_repo.get_sequences()
    captures = {}
    for sequence in sequences:
        capture_files = []
        for image in sequence.get_images():
            capture_files.append(image.get_file_name())
        captures[sequence.time] = capture_files
    return jsonify(captures)


@app.route('/video_feed')
def video_feed():
    capturer = Capturer()
    return Response(capturer.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
