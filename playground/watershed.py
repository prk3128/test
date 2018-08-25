import cv2
import numpy as np
from scipy.ndimage import label
import distortion

kernel = np.ones((3,3), np.uint8)

Dist = distortion.distortion()

cam = cv2.VideoCapture(0)

while(cam.isOpened()) :
    ret, img = cam.read()

    img = Dist.Undistort(img)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow("thresh",thr)

#    opening = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel, iterations=2)
#    cv2.imshow("opening",opening)

    border = cv2.dilate(thr, kernel, iterations=1)

    border = border - cv2.erode(border, None)
    cv2.imshow("border",border)
    dt = cv2.distanceTransform(thr, cv2.DIST_L2, 5)
    dt = ( ( dt-dt.min() )/ ( dt.max()-dt.min() )*255).astype(np.uint8)
    ret, dt = cv2.threshold(dt, 180, 255, cv2.THRESH_BINARY)

    cv2.imshow("distance",dt)

    marker, ncc = label(dt)
    marker = marker*(255/ncc)

    marker[border==255] = 255
    marker = marker.astype(np.int32)
    cv2.watershed(img, marker)

    marker[marker==-1] = 0
    marker = marker.astype(np.uint8)
    marker = 255-marker

    marker[marker != 255] = 0
    marker = cv2.dilate(marker.astype(np.float32), None)
    img[marker==255] = (0,0,255)

    cv2.imshow("watershed",img)

    if(cv2.waitKey(1)==27) :
        break

cv2.destroyAllWindows()

cam.release()
