import cv2 as cv
import time
import numpy as np
import PoseModule as pm

#cap = cv.VideoCapture("Data_Collection/tiasquat.mp4")
#cap = cv.VideoCapture("Data_Collection/squat.mp4")
#cap = cv.VideoCapture("Data_Collection/squat2.mp4")
#cap = cv.VideoCapture("Data_Collection/squatA.MP4") #model confuse with the person who spot the squat
#cap = cv.VideoCapture("Data_Collection/squatB.MP4")#model confuse with the person who spot the squat
#cap = cv.VideoCapture("Data_Collection/squatC.MP4")
#cap = cv.VideoCapture("Data_Collection/squatE.MP4")
#cap = cv.VideoCapture("Data_Collection/squatF.MP4")
cap = cv.VideoCapture("Data_Collection/squatG.MP4")
#cap = cv.VideoCapture("Data_Collection/squatH.MP4")
#cap = cv.VideoCapture("Data_Collection/squatI.MP4")
#cap = cv.VideoCapture("Data_Collection/squatJ.MP4")

detector = pm.poseDetector()
count = 0
dir = 0  # direction


pTime = 0

while True:
    success, img = cap.read()
    #img = cv.imread("Data_Collection/body.jpg") # read image
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        #righta=detector.findAngle(img, 12, 14, 16)
        #lefta= detector.findAngle(img, 11, 13, 15)
        angle = detector.findAngle(img, 24, 26, 30)
        if angle < 170:
          per = np.interp(angle, (80, 150),(0, 100))
        elif angle >180:
          per =np.interp(angle, (208, 280), (0, 100))
        bar = np.interp(angle, (200, 288), (650,100))
        print(angle)

        # counting squat reps
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
       # print(count)

        # Draw Bar
        #cv.rectangle(img, (1000,100), (800, 650), color, 3)
        #cv.rectangle(img, (1000, int(bar)), (800, 650), color, cv.FILLED)
        #cv.putText(img, f'{int(per)} %', (800, 75), cv.FONT_HERSHEY_PLAIN,4, color,4)

        # Draw Curl Count
        #cv.rectangle(img,(0,450), (50,720), (0,255,0),cv.FILLED)
        cv.putText(img, str(int(angle))+'degree', (20, 1800), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 0, 5), 10)
        cv.putText(img, str(int(count))+'rep', (20, 1600), cv.FONT_HERSHEY_PLAIN,5, (0, 0, 0, 5),5)




    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
