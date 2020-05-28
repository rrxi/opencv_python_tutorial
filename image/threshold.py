import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
#retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) # param: img, threshold, maximum, type of threshold; 对于弱光图片通常选择较低的threshold值
# 使用灰度将图像变得简单
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)

#使用自适应阈值化，将改变阈值，能够解决弯曲的页面
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#Otsu阈值不能很好的解决问题
retval2, threshold2 = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('Adaptive threshold', th)
cv2.imshow('Otsu threshold', threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()