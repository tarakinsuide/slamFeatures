import numpy as np
import cv2
import glob
import os

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

mean_error = 0

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.


src = os.getcwd()
print(src)
os.chdir(os.path.join(os.getcwd(), 'calibFrames'))

images = glob.glob('*.jpg')



count = 0
for fname in images:
    # print(fname)
    objpoints = [] # 3d point in real world space
    imgpoints = []  # 2d points in image plane.
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,6),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        # print(objp)
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
        print(fname)
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

        h,w = img.shape[:2]

        newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

        #undistort
        dst = cv2.undistort(img, mtx, None, newCameraMatrix)

        #crop
        x,y,w,h = roi
        dst = dst[y:y+h, x:x+w]
        # cv2.imwrite("%fname", dst)
        # count += 1

        # print("path",os.path)

        print(mtx)
        print(newCameraMatrix)
        print(dist)
        # print(rvecs)
        # print(tvecs)
        # cv2.imshow('img',dst)
        # cv2.waitKey(0)

        for i in range(len(objpoints)):
            imgpoints2,_ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
            error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
            mean_error += error

        print("total error: ", mean_error/len(objpoints))
