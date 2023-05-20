import logging

from flask import Flask, Response, jsonify

from src.repository.subject_repository import SubjectRepository
from src.tracker.services.capturer import Capturer

app = Flask(__name__)


@app.route('/images/<path:file_path>')
def untrained_images(file_path):
    ##Todo set a Limit and implement
    print("implement")


@app.route('/untrained')
def untrained():
    ##Todo set a Limit
    subject_repository = SubjectRepository()
    captures = []
    for subject in subject_repository.get_untrained(1, 50):
        for image in subject.get_images():
            captures = image.filepath

    return jsonify(captures)



@app.route('/video-feed')
def video_feed():
    capturer = Capturer()
    return Response(capturer.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


class Page:
    def __init__(self):
        logging.debug("Page init")

    def run_dev(self):
        logging.debug("Page run_dev")
        app.run(debug=True, host='0.0.0.0')

    def get(self):
        return app
