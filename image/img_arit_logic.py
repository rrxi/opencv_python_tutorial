import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')

# 相同size的图像相加
# add = img1 + img2
add = cv2.add(img1, img2)  # 像素值超过255的，会被截断成255
# cv2.imshow('add', add)

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)  # param:img1, img1-weight, img2, img2-weight, gamma(光的测量)
# cv2.imshow('weighted', weighted)


# 不同size的图像相加
# Load two images
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# add a threshold
# mask的logo区域为白色，mask_inv的logo区域为黑色
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1_bg)

cv2.waitKey(0)
cv2.destroyAllWindows()
