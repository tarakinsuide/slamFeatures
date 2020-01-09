import cv2
import os

count = 0

vidObj = cv2.VideoCapture('C://Users//Admin//PycharmProjects//SlamFeatures//MonoVisualOdometry//cameraframes.mp4')

os.chdir(os.path.join(os.getcwd(), 'calibFrames'))

while True:
    ret,frame = vidObj.read()

    if (count % 10 == 0):
        cv2.imwrite('frame'+ str(count) + '.jpg', frame)
    count += 1
    print(count)
    if count > 10000:
        break