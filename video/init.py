import numpy as np
import cv2

#cap = cv2.VideoCapture("/data/downloads/2020-05-27_17-09-52.mp4")
cap = cv2.VideoCapture("rtsp://192.168.1.93:554/live.sdp")
ret, frame = cap.read()
while ret:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release();
cv2.destoryAllWindows()
