import os

from flask import Flask, render_template, send_from_directory, Response

from src.tracker.services.capturer import Capturer

app = Flask(__name__)


@app.route('/images/<path:file_path>')
def untrained_images(file_path):
    untrained_dirs = "../../data/untrained"
    return send_from_directory(untrained_dirs, file_path)


@app.route('/')
def index():
    untrained_dirs = "../../data/untrained"
    all_files = []
    # Todo get from repositroy
    for root, dirs, files in os.walk(untrained_dirs):
        for file in files:
            filename = os.path.join(root, file)
            dirname = os.path.dirname(filename).split("\\")[-1]
            file_path = dirname + "/" + file
            all_files.append(file_path)
    return render_template('index.html', files=all_files)


@app.route('/video_feed')
def video_feed():
    capturer = Capturer()
    return Response(capturer.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
