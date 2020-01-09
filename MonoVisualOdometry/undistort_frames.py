import cv2
import numpy as np
from MonoVisualOdometry.CameraMatrix import cameraMartix
import os
import glob

images_dir = (os.path.join(os.getcwd(),'calibFrames'))
images = glob.glob('*.jpg')
for image in images:
    cams = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while True:
        mtx, dist, rvecs, tvecs = cameraMartix(image)
        print(mtx)

        while True:
            ret, frames = cams.read()

            # cv2.imshow('frames', frames)
            print(frames.mean())

            h, w = frames.shape[:2]
            # print(h)
            # print(w)
            newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
            # print(mtx)
            # undistort
            dst = cv2.undistort(frames, mtx, None, newCameraMatrix)

            # crop
            # x, y, w, h = roi
            # dst = dst[y:y + h, x:x + w]

            cv2.imshow('undistorted frames', dst)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cams.release()
        cv2.destroyAllWindows()

# h, w = img.shape[:2]
#
# newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
#
# # undistort
# dst = cv2.undistort(img, mtx, None, newCameraMatrix)
#
# # crop
# x, y, w, h = roi
# dst = dst[y:y + h, x:x + w]