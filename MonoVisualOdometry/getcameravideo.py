import cv2

# camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('cameraframes.mp4', codec, 20.0, (640,480))

while True:
    ret, frame = camera.read()

    cv2.imshow('camera_feed',frame)


    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
out.release()
cv2.destroyAllWindows()


