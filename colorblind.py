import cv2 as cv
import numpy as np 

frameWidth = 1280
frameHeight = 720

cap = cv.VideoCapture(0) 
cap.set(3, frameWidth) 
cap.set(4, frameHeight) 

#Brightness
cap.set(10,150) 

def validateInput(choice):
    if(choice.isnumeric()):
        choice = int(choice)
        if(choice > 3 or choice < 1):
            choice = validateInput(input("Sorry that is not a valid selection please try again: "))
    else:
        choice = validateInput(input("Sorry that is not a valid selection please try again: "))
    return choice

print("What kind of color blindness would you like to simulate?")
print("Enter 1 for Red-green deficiency")
print("Enter 2 for Blue-yellow deficiency")
print("Enter 3 for Complete color deficiency")
choice = validateInput(input(""))

windowNames = {1 : "Red-Green Deficiency", 2: "Blue-yellow Deficiency", 3: "Complete color Deficiency"}

while True:
    ret, frame = cap.read()
    if ret:
        #frame = cv.copyMakeBorder(frame, 10, 10, 10, 10, cv.BORDER_CONSTANT, None, value = [0,0,255]) #adds a border to webcam display, just for funsies(testing)
        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow(windowNames[choice], frame)
        if cv.waitKey(25) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() 
cv.destroyAllWindows() 