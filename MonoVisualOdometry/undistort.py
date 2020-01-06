import cv2
import numpy as np


img = cv2.imread('IMG_20200106_161751537.jpg')
img2 = cv2.imread('IMG_20200106_161755849.jpg')

cv2.resize(img, (720,480))

cv2.imshow('img1', img)
cv2.imshow('img2', img2)


cv2.waitKey(0)
cv2.destroyAllWindows()