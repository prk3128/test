import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while(cam.isOpened()) :
    ret, img = cam.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([10, 50, 50])
    upper_blue = np.array([200, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('image', img)
    cv2.imshow('mask',mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()