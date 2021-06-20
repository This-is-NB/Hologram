import cv2
import numpy as np

# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load functions
def face_extractor(img):
    return img
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

# Initialize Webcam
cap = cv2.VideoCapture(0)
count = 0

# Collect 100 samples of your face from webcam input
flag = False
while True:

    ret, frame = cap.read()
    cv2.imshow("dddddd",frame)
    if flag:
        faceimg =  face_extractor(frame)
        if faceimg is not None:
            count += 1
            # face = cv2.resize(faceimg, (200, 200))
            face = cv2.cvtColor(faceimg, cv2.COLOR_BGR2GRAY)

            # Save file in specified directory with unique name
            file_name_path = './Pointer/' + str(count) + '.jpg'
            cv2.imwrite(file_name_path, face)

            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Cropper', face)
    
    else:
        # print("Face not found")
        pass
    if cv2.waitKey(50) == 32 : #13 is the Enter Key
        flag = True
    
    if cv2.waitKey(50) == 13 or count == 100: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()      
print("Collecting Samples Complete")