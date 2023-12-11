import cv2 as cv
import numpy as np 

frameWidth = 1280
frameHeight = 720

cap = cv.VideoCapture(0) 
cap.set(3, frameWidth) 
cap.set(4, frameHeight) 

#Brightness
cap.set(10,150) 

while True:
    ret, frame = cap.read()
    if ret:
        #frame = cv.copyMakeBorder(frame, 10, 10, 10, 10, cv.BORDER_CONSTANT, None, value = [0,0,255]) #adds a border to webcam display, just for funsies(testing)
        cv.imshow("Result", frame)
        if cv.waitKey(25) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() 
cv.destroyAllWindows() 