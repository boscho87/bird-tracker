import unicodedata
import re
import cv2

#Todo do not execute the function directly
def find_camera_id():
    for i in range(0, 10):
        print("Open Cam")
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print("Cam-ID:", i)
            cap.release()
            return
    print("NO CAMS FOUND")

