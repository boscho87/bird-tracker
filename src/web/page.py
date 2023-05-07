import os

from flask import Flask, Response, jsonify

from src.tracker.services.capturer import Capturer

app = Flask(__name__)


@app.route('/images/<path:file_path>')
def untrained_images(file_path):
    ##Todo set a Limit and implement
    print("implement")


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


@app.route('/video-feed')
def video_feed():
    capturer = Capturer()
    return Response(capturer.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


class Page:
    def __init__(self):
        print("Page init")

    def run_dev(self):
        print("Page run")
        app.run(debug=True, host='0.0.0.0')

    def get(self):
        return app
