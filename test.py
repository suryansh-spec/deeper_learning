import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(0)   #select device to read video from
mpHands = mp.solutions.hands        #define hands to detect inside mediapipe
hands = mpHands.Hands()           #define hands
mpdraw = mp.solutions.drawing_utils #module to draw | | lines between hand points 
ptime =0


while True:
    success, img = cap.read()    #main point where we read our camera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)     #opencv bydefault is BGR, so convert it to RGB
    result = hands.process(imgRGB)
    #print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:  #if this is true the below code will execute
        for handlms in result.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):  #loop for showing the id and landmarks of hand 
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)


            mpdraw.draw_landmarks(img, handlms,mpHands.HAND_CONNECTIONS)


    ctime = time.time()
    fps = 1/(ctime - ptime)  #main fps formula
    ptime = ctime


    #to display fps define the text features and coordinates
    cv2.putText(img,
                str(int(fps)),
                (10,70), cv2.FONT_HERSHEY_COMPLEX,
                3, 
                (255,0,255),3) # type: ignore

    cv2.imshow("Image", img)  
    cv2.waitKey(1)     #1ms delay between frames