import cv2 as cv
import time
import numpy as np
import PoseModule as pm

cap = cv.VideoCapture("Data_Collection/Dip.mp4")

detector = pm.poseDetector()
count = 0
dir = 0  # direction

pTime = 0

while True:
    success, img = cap.read()
    # img = cv.imread("Videos/test.jpg") # read image
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        # detector.findAngle(img, 12, 14, 16)
        # Left Arm
        # detector.findAngle(img, 11, 13, 15)
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220,310), (650,100))
        print(angle, per)

        # check for the dumbbell curls
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
        cv.rectangle(img, (1100,100), (1175, 650), color, 3)
        cv.rectangle(img, (1100, int(bar)), (1175, 650), color, cv.FILLED)
        cv.putText(img, f'{int(per)} %', (1100, 75), cv.FONT_HERSHEY_PLAIN,4, color,4)

        # Draw Curl Count
        cv.rectangle(img,(0,450), (250,720), (0,255,0),cv.FILLED)
        cv.putText(img, str(int(count)), (45, 670), cv.FONT_HERSHEY_PLAIN, 15, (255, 0, 0, 5), 25)

        # cv.putText(img, str(int(count)), (50, 100), cv.FONT_HERSHEY_PLAIN,3, (255, 0, 0, 5),5)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (50, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0, 5), 5)

    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
