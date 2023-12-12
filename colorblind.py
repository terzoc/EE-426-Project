import cv2 as cv
import numpy as np 

#Height and width of webcam resolution
frameWidth = 1280
frameHeight = 720

#Set up video capture from webcam
cap = cv.VideoCapture(0) 
cap.set(3, frameWidth) 
cap.set(4, frameHeight) 
cap.set(10,150) #Brightness

#Window names based on user input
windowNames = {0: "Normal Vision", 1 : "Red-Green Deficiency", 2: "Blue-yellow Deficiency", 3: "Complete color Deficiency"}

#Validates user input
def validateInput(choice):
    if(choice.isnumeric()):
        choice = int(choice)
        if(choice > 3):
            choice = validateInput(input("Sorry that is not a valid selection please try again: "))
    else:
        choice = validateInput(input("Sorry that is not a valid selection please try again: "))
    return choice

#Gets user input
print("What kind of color blindness would you like to simulate?")
print("Enter 0 for Normal Vision")
print("Enter 1 for Red-green deficiency")
print("Enter 2 for Blue-yellow deficiency")
print("Enter 3 for Complete color deficiency")
choice = validateInput(input(""))

#Main loop
while True:
    ret, frame = cap.read()
    if ret:
        #frame = cv.copyMakeBorder(frame, 10, 10, 10, 10, cv.BORDER_CONSTANT, None, value = [0,0,255]) #adds a border to webcam display, just for funsies(testing)
        match choice:
            case 0:
                #Normal Vision, no change
                pass
            case 1:
                #Red-green deficiency
                blindColors = frame[:, :, 2]
                blindColors += frame[:,:, 1]
                blindColors = cv.subtract(blindColors, 10)

                frame = blindColors
                # frame[:, :, 2] = 0
                # frame[:, :, 1] = 0

                # blindColors = np.expand_dims(blindColors, axis=-1)
                # frame += blindColors

                # # red[:, :, 1] = 0
                # hsv = cv.cvtColor(red, cv.COLOR_BGR2HSV)
                # hsv[:, :, 1] = hsv[:, :, 1] * 0.25
                # # red = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

                # frame[:, :, 2] = 0
                # # frame[:, :, 1] = 0
                # frame = red

            case 2:
                #Blue-yellow deficiency
                pass
            case 3:
                #Complete color deficiency
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow(windowNames[choice], frame)
        if cv.waitKey(25) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() 
cv.destroyAllWindows() 