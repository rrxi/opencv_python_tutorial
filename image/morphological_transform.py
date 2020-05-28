import cv2
import numpy as np

# 形态变换常常成对出现
# Erosion(侵蚀)&Dilation(扩张)
# Erosion: 如果卷积核对应的原图像的所有像素值都为1,那么中心元素就保持原来的像素值,否则为0；
#          常用于去除白噪声,可以断开两个连在一起的物体
# Dilation:


cap = cv2.VideoCapture('red.mp4')

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()