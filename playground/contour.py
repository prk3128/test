import cv2
import distortion as distort
import numpy as np

Dist = distort.distortion()
cam = cv2.VideoCapture(0)

while(cam.isOpened()) :
    ret, img = cam.read()

    dst = Dist.Undistort(img)

    con1 = dst.copy()
    con2 = dst.copy()

    gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)

    ret, gray = cv2.threshold(gray, 200, 255, 0)

    a, contours1, b = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    a, contours2, b = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89)

    cv2.drawContours(con1, contours1[1], -1, (0,0,255), 5)
    cv2.drawContours(con2, contours2, -1, (0, 0, 255), 5)
    cv2.imshow("thresh", gray)
    cv2.imshow("TREE",con1)
    cv2.imshow("CCOMP",con2)

    if(cv2.waitKey(1)==27) :
        break

cv2.destroyAllWindows()

cam.release()