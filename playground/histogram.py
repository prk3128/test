import cv2
import numpy as np
import distortion

Dist = distortion.distortion()

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

cam = cv2.VideoCapture(0)

while(cam.isOpened()) :
    ret, img = cam.read()

    img = Dist.Undistort(img)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    c_img = clahe.apply(gray)

    h_img = cv2.equalizeHist(gray)

    result = np.hstack((c_img,gray,h_img))

    ret, result = cv2.threshold(result, 160, 255, 0)
    cv2.imshow("result",result)

    if (cv2.waitKey(1)==27) :
        break

cv2.destroyAllWindows()

cam.release()