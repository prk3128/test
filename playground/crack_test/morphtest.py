import cv2
import numpy as np
import time
import ClientAlpha as client

p=0

# canny thresh
canny_lower = 50
canny_upper = 100

# import calibration data
calib = np.load("calib.npz")
mtx = calib['mtx']
dist = calib['dist']

kernel = np.ones((3,3),np.uint8)
sharpk = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharpk2 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]])/8

# morphology line kernel
linek = np.zeros((11,11), dtype = np.uint8)
linek[5,...]=1

# construct camera object
cam = cv2.VideoCapture(0)

while(cam.isOpened()) :

    if(cv2.waitKey(1)==27) :
        break

    #time.sleep(1)

    ret, img = cam.read()

    # undistortion
    h, w = img.shape[:2]
    newcamera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    dst = cv2.undistort(img, mtx, dist, None, newcamera_mtx)
    x, y, w, h = roi
    dst = dst[y:y + h, x:x + h]
    cv2.imshow("cam", dst)

    # image gray, Blur, threshold
    gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
    #gray = cv2.equalizeHist(gray)
    #cv2.imshow("cam", gray)
    #gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 1)
    gray = cv2.filter2D(gray, -1, sharpk2)

    ret, gray = cv2.threshold(gray, 9, 255, cv2.THRESH_BINARY)
    gray = cv2.medianBlur(gray, 5)

    # morpohology
    u = gray.copy()
    v = gray.copy()
    v = np.transpose(v)

    #gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow("gray", gray)

    u = cv2.morphologyEx(u, cv2.MORPH_OPEN, linek, iterations=1)
    #u = cv2.morphologyEx(u, cv2.MORPH_OPEN, kernel, iterations=3)
    v = cv2.morphologyEx(v, cv2.MORPH_OPEN, linek, iterations=1)
    #v = cv2.morphologyEx(v, cv2.MORPH_OPEN, kernel, iterations=3)
    v = np.transpose(v)

    #ugray = gray.copy()
    #vgray = gray.copy()

    #ugray -= u
    #vgray -= v

    wgray = u|v

    #wgray = cv2.morphologyEx(wgray, cv2.MORPH_OPEN, kernel, iterations=1)
    result = gray - wgray
    #result = cv2.morphologyEx(result, cv2.MORPH_OPEN, kernel, iterations=2)
    #result = cv2.medianBlur(result, 5)
    #result = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel, iterations=1)
    #result = cv2.morphologyEx(result, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2)))
    #ret, result = cv2.threshold(result, 250, 255, cv2.THRESH_TOZERO)
    ret, result = cv2.threshold(result, 250, 255, cv2.THRESH_BINARY)
    result = result[50:,50:]

    #cv2.imshow("morph",wgray)
    cv2.imshow("result",result)

    for i in range(len(result)) :
        for j in range(len(result[i,:])) :
            p += result[i,j]
    if p > 1000 * 255 :
        cv2.imwrite('/home/cae/Desktop/crack.png',result)
        client.TransferClient()
        p=0

cam.release()

cv2.destroyAllWindows()