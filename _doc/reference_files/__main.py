import cv2
import numpy as np
from class_indicies import class_ind
import time
import functions, setup
import os
import RPi.GPIO as GPIO
import tensorflow.lite as tflite

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)

#delete temp directory contents in case unforseen shutdown
functions.delete_temp_directory()

#load the model
t2 = time.time()
print('loading the model...')


# Load TFLite model and allocate tensors.
interpreter = tflite.Interpreter(model_path='model.tflite')
#allocate the tensors
interpreter.allocate_tensors()

#get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print('done loading')
t1 = time.time()
print(t1-t2)


while True:
    i = GPIO.input(7)
    #i=1
    if i==1:
        print('motion detected!')
        #time.sleep(2)
        t0 = time.time()
        # define a video capture object
        vid = cv2.VideoCapture(0)
        width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        writer = cv2.VideoWriter('bird_vid.mp4', cv2.VideoWriter_fourcc(*'mp4v'),20,(width,height))
        start_time = time.time()


        #capture video for specified amount of time
        capture_duration = 3 #amount of time we want the video to record for
        while( int(time.time() - start_time) < capture_duration):
            # Capture the video frame by frame
            ret, frame = vid.read()
            writer.write(frame)
            # Display the resulting frame
            #cv2.imshow('frame', frame)

        # After the loop release the cap object
        vid.release()
        writer.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        print('capturing video...')

        #once capture is complete, run each frame through the model and collect the predictions for each frame

        #open the video we just recorded
        cap = cv2.VideoCapture('bird_vid.mp4')
        if cap.isOpened() == False:
            print('ERROR FILE NOT FOUND OR WRONG CODEC USED!')


        #Save all the frames as JPGs in a temporary directory
        functions.save_as_jpg()

        #every image will get a prediction and we will collect them in a list initialized here
        predictions=[]

        #count the number of items in the directory
        path, dirs, files = next(os.walk('Temp'))
        file_count = len(files)
        print("making predictions...")

        #run each image though the model and collect results
        for i in range(1,file_count+1,10):
            # Read the image and decode to a tensor
            image_path= f'Temp/{i}.jpg'
            img = cv2.imread(image_path)
            img = cv2.resize(img,(224,224))
            #Preprocess the image to required size and cast
            input_shape = input_details[0]['shape']
            input_tensor= np.array(np.expand_dims(img,0))

            #set the tensor to point to the input data to be inferred
            input_index = interpreter.get_input_details()[0]["index"]
            interpreter.set_tensor(input_index, input_tensor)
            #Run the inference
            interpreter.invoke()
            output_details = interpreter.get_output_details()

            output_data = interpreter.get_tensor(output_details[0]['index'])
            pred = np.squeeze(output_data)

            #make the prediction
            #pred = model.predict(processed_bird_image,batch_size = 1)

            # #get the index and value of the highest prediction
            highest_pred_loc = np.argmax(pred)
            highest_pred = np.max(pred)
            #if the model is 95% confident, break the loop and use just that one prediction
            if highest_pred > 140:
                print("I'm really confident and am skipping ahead")
                break
            # if the highest prediction is fairly confident, add it to list
            elif highest_pred > 60:
                predictions.append(highest_pred_loc)
                print(f'highest confidence for this frame is {highest_pred}')
            #if the prediction is less than 85% confident, don't keep the prediction
            else:
                predictions.append('none')
                print('No confidence for the frame')
        print('Images Processed')
        t1 = time.time()

        #if we broke out of the previous loop because we were so confident, use the one prediction as the agg_pred
        if highest_pred > 140:
            agg_pred = highest_pred_loc
        else:
            # use the most_common function to get the mode of the predictions list
            agg_pred = functions.most_common(predictions)

        # get the name of the bird from the location
        if agg_pred != 'none':
            bird_name = class_ind[agg_pred]
            print(f"It's a wild {bird_name}! So cute.")
            #build and send the email
            functions.send_email(bird_name, setup.email, setup.receiver_email, setup.password, setup.port)

            #collect all the images for further training
            functions.reinforcement_learning(bird_name)
        else:
            print("sorry, I couldn't define the bird")
            #collect images for later analysis
            functions.save_undefined_birds()

        #delete temp directory contents
        functions.delete_temp_directory()
        t1 = time.time()
        print(f'Loop time {t1-t0}')
