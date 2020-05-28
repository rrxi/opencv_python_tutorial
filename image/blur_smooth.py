import cv2
import numpy as np

cap = cv2.VideoCapture('../video/test.mp4')

while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # simple smoothing, 损失了粒度
    kernel = np.ones((15, 15), np.float32) / 255
    smoothed = cv2.filter2D(res, -1, kernel)
    # Gaussian blurring 高斯模糊
    blur = cv2.GaussianBlur(res, (15, 15), 0)
    # Median Blur 中值模糊
    media = cv2.medianBlur(res, 15)
    # Bilateral Blur 双边模糊
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    cv2.imshow('Original', frame)
    cv2.imshow('Averaging', smoothed)
    cv2.imshow('Gaussian Blurring', blur)
    cv2.imshow('Median Blur', media)
    cv2.imshow('bilateral blur', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
