import cv2
import numpy as np
from keras.preprocessing import image
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import setup

def most_common(list):
    '''find the most common element in a list '''
    counter = 0
    num = list[0]
    for i in list:
        curr_frequency = list.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num


def process_image(frame):
    '''process an image or frame to make it compatible with out model'''
    frame = image.img_to_array(frame)
    frame = np.expand_dims(frame, axis = 0)
    frame = frame/255
    return frame


def save_as_jpg():
    try:
        cap = cv2.VideoCapture('bird_vid.mp4')
        #"open" the video and read frame by frame 
        while cap.isOpened():
            ret,frame = cap.read()
            if ret == True:
                # create a temporary directory to hold the jpg images
                UndefinedDirectory = 'Temp'
                #check if directory exists
                if not os.path.exists(UndefinedDirectory):
                    os.makedirs(UndefinedDirectory)
                #count the number of items in the directory
                path, dirs, files = next(os.walk(UndefinedDirectory))
                file_count = len(files)
                #create file path
                filepath = os.path.join(UndefinedDirectory, f'{file_count+1}.jpg')
                # save image
                cv2.imwrite(filepath,frame)
            else:
                break
    except:
        pass


def save_undefined_birds():
    try:
        cap = cv2.VideoCapture('bird_vid.mp4')
        #"open" the video and read frame by frame 
        while cap.isOpened():
            ret,frame = cap.read()
            if ret == True:
                # create a temporary directory to hold the jpg images
                UndefinedDirectory = 'Undefined'
                #check if directory exists
                if not os.path.exists(UndefinedDirectory):
                    os.makedirs(UndefinedDirectory)
                #count the number of items in the directory
                path, dirs, files = next(os.walk(UndefinedDirectory))
                file_count = len(files)
                #create file path
                filepath = os.path.join(UndefinedDirectory, f'{file_count+1}.jpg')
                # save image
                cv2.imwrite(filepath,frame)
            else:
                break
    except:
        pass






def reinforcement_learning(bird):
    try:
        cap = cv2.VideoCapture('bird_vid.mp4')
        #"open" the video and read frame by frame 
        while cap.isOpened():
            ret,frame = cap.read()
            if ret == True:
                # first 10 images are for test
                TestDirectory = f'Reinforcement/test/{bird}'
                #check if directory exists
                if not os.path.exists(TestDirectory):
                    os.makedirs(TestDirectory)
                #count the number of items in the directory
                path, dirs, files = next(os.walk(TestDirectory))
                file_count = len(files)
                if file_count <= 9:
                    #create file path
                    filepath = os.path.join(TestDirectory, f'{file_count+200}.jpg')
                    # save image '
                    cv2.imwrite(filepath,frame)

                #stop after 50 total image
                else:
                    TrainDirectory = f'Reinforcement/train/{bird}'
                    #check if directory exists
                    if not os.path.exists(TrainDirectory):
                        os.makedirs(TrainDirectory)
                    #count the number of items in the directory
                    path, dirs, files = next(os.walk(TrainDirectory))
                    file_count = len(files)
                    if file_count > 50:
                        pass
                    #create file path    
                    filepath = os.path.join(TrainDirectory, f'{file_count+200}.jpg')
                    # Save image
                    cv2.imwrite(filepath,frame)
            else:
                break
    except:
        pass


def delete_temp_directory():
    if not os.path.exists('Temp'):
        pass
    else:
        dir = 'Temp'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))


def send_email(bird, sender_email, receiver_email, password, port):
    message = MIMEMultipart("alternative")
    message["Subject"] = f'Look! A wild {bird} has appeared!'
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
        Hi there,
        How are you?
        """


    html = """\
            <html>
            <body>
                <p>Hi,<br>
                Check out your new friend in the attachment!<br></p>
            </body>
            </html>
            """
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(setup.file_location,"rb").read() )
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(setup.file_location))
    message.attach(part)

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
