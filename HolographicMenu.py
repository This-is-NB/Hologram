import mediapipe as mp
import os
import time 


import cv2
from keras.models import load_model
import numpy as np


mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraws = mp.solutions.drawing_utils



# model = load_model('/facefeatures_new_model_final.h5')
model = load_model(r'C:\Users\smriti bansal\Desktop\Code\ML\Open-CV\Face_Recognition\facefeatures_new_model.h5')

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
ptime,ctime = 0,0
while True:
    _, frame = video_capture.read()
    face =  face_cascade.detectMultiScale(frame)
    
    h, w, c = frame.shape
    frameRBG = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRBG)
    
    if results.multi_hand_landmarks:
        os.system("cls")
        # print(type(results.multi_hand_landmarks[0]))
        for hnds in results.multi_hand_landmarks:
            for id , lm in enumerate(hnds.landmark):
                cx,cy  = int(lm.x * w), int(lm.y * h)
                if id==8:
                    print(cx,cy)
            
            mpDraws.draw_landmarks(frame,hnds,mphands.HAND_CONNECTIONS)
    
    if  len(face) == 0:
        cv2.putText(frame,"No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    else:
        x=face[0][0]
        y=face[0][1]
        w=face[0][2]
        h=face[0][3]
        cropped_face = frame[y:y+h, x:x+w]
        frame = cv2.rectangle(frame, (x,y),(x+w,y+h), [0,255,0], 5 )
        
        img_array = cropped_face[:,:,::-1]
                    #Our keras model used a 4D tensor, (images x height x width x channel)
                    #So changing dimension 128x128x3 into 1x128x128x3 
        img_array = cv2.resize(img_array,(224,224))
        img_array = np.expand_dims(img_array, axis=0)
        pred = model.predict(img_array)
        print(pred)
        # print(img_array.shape)
                     
        name="I don't Recognise u"
        
        if(pred[0][1]>0.9):
            name='Hey Naman'
        
        if(pred[0][0]>0.9):
            name='Hey Ayush'
        
        ptime=0
        #button
        time.sleep(1)
        ctime = time.time()
        print(ctime-ptime)
        # ptime = ctime

        
        cv2.putText(frame,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    # else:
    #     cv2.putText(frame,"No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.flip(frame,1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()