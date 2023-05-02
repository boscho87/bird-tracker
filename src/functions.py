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



## todo comment in english
def create_slug(string):
    # Entferne unnötige Leerzeichen am Anfang und Ende des Strings
    string = string.strip()
    # Konvertiere den String in Kleinbuchstaben
    string = string.lower()
    # Ersetze Leerzeichen durch Bindestriche oder Unterstriche
    string = re.sub(r'\s+', '-', string)
    # Entferne Sonderzeichen, Satzzeichen und diakritische Zeichen
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8')
    # Optional: Überprüfe auf eindeutige Slugs, um Kollisionen zu vermeiden
    return string
