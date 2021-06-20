import cv2
import mediapipe as mp
import os

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraws = mp.solutions.drawing_utils

while True:
    _,frame = cap.read()
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
    cv2.flip(frame,1)
    cv2.imshow("a",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 32: #Spacebar
        break
    # break
cap.release()
cv2.destroyAllWindows