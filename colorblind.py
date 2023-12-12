import cv2 as cv
import numpy as np 

#Color multiplers, change how and to what extent red and green are modified
redMultiplier = 0.5
greenMultiplier = 1.5

#Height and width of webcam resolution
frameWidth = 1280
frameHeight = 720

#Set up video capture from webcam
cap = cv.VideoCapture(0) 
cap.set(3, frameWidth) 
cap.set(4, frameHeight) 
cap.set(10,150) #Brightness

#Window names based on user input
windowNames = {0: "Normal Vision", 1 : "Red-green deficiency", 2: "Complete color Deficiency"}

#Validates user input
def validateInput(choice):
    if(choice.isnumeric()):
        choice = int(choice)
        if(choice > 2):
            choice = validateInput(input("Sorry that is not a valid selection please try again: "))
    else:
        choice = validateInput(input("Sorry that is not a valid selection please try again: "))
    return choice

#Gets user input
print("What kind of color blindness would you like to simulate?")
print("Enter 0 for Normal Vision")
print("Enter 1 for Red-green deficiency")
print("Enter 2 for Complete color deficiency")
choice = validateInput(input(""))

#Main loop
while True:
    #Read frame from webcam
    ret, frame = cap.read()
    if ret:
        match choice:
            case 0:
                #Normal Vision, no change
                pass
            case 1:
                #Red-green deficiency
                img = frame.copy().astype(np.float32)
                img[:, :, 2] = np.clip(img[:, :, 2] * redMultiplier, 0.0, 255.0)
                img[:, :, 1] = np.clip(img[:, :, 1] * greenMultiplier, 0.0, 255.0)
                frame = img.astype(np.uint8)
            case 2:
                #Complete color deficiency
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #Display frame and listen for exit keypress Q
        cv.imshow(windowNames[choice], frame)
        if cv.waitKey(25) & 0xFF == ord('q'): 
            break
    else:
        break

#Shutdown
cap.release() 
cv.destroyAllWindows() 