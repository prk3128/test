import cv2
import numpy as np

cam = cv2.VideoCapture(0)
ret, img = cam.read()
capture = img
temp = ord('1')

while(cam.isOpened()) :
    ret, img = cam.read()

    key=cv2.waitKey(1)

    if(key == ord('1')) :
        temp = key
    elif (key == ord('2')) :
        temp = key
    elif (key == ord('3')) :
        temp = key
    elif (key == 27) :
        break

    if (temp == ord('1')):
        capture = img
    elif (temp == ord('2')):
        capture = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    elif (temp == ord('3')):
        capture = cv2.Canny(img,500,500)

    cv2.imshow("Eyes of SY GOD",capture)

cam.release()
cv2.destroyAllWindows()