import cv2
import numpy as np


cams = cv2.VideoCapture(0)

while True:
    ret,frames = cams.read()

    cv2.imshow('frames',frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cams.release()
cv2.destroyAllWindows()