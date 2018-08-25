import cv2
import numpy as np
import distortion
import matplotlib.pyplot as plt
import auto_canny as auto

kernel = np.ones((3,3), np.uint8)

Dist = distortion.distortion()

cam = cv2.VideoCapture(0)

while(cam.isOpened()) :
    ret, img = cam.read()

    img = Dist.Undistort(img)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = gray[20:420, 100:500]

    gray = auto.AutoCanny(gray)

    img_dct = np.float32(gray)

    img_dct = cv2.dct(img_dct)

    img_dct = cv2.medianBlur(img_dct,5)

    #img_dct = cv2.morphologyEx(img_dct, cv2.MORPH_CLOSE, kernel, iterations=1)

    img_idct = cv2.idct(img_dct)

    img_dct = np.uint8(img_dct)
    img_idct = np.uint8(img_idct)

    result = np.hstack((gray, img_dct, img_idct))

    cv2.imshow("result",result)
    #cv2.imshow("dft shift",img)

    if cv2.waitKey(1)==27 :
        break

cv2.destroyAllWindows()

cam.release()