import cv2
import numpy as np

termination = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1,2)

objpoints = []
imgpoints = []

count = 0

cam = cv2.VideoCapture(0)

while(cam.isOpened()) :
    ret, img = cam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    key = cv2.waitKey(1)

    if key == ord('s') :
        ret, corners = cv2.findChessboardCorners(gray, (9,6), None)

        if ret == True :
           objpoints.append(objp)
           cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), termination)
           imgpoints.append(corners)

           cv2.drawChessboardCorners(img, (9,6), corners, ret)
           count += 1
           print('[ %d ]' %count)

    elif key == 27 :
        break

    if (count > 49) :
        break

    cv2.imshow("img", img)

cam.release()

cv2.destroyAllWindows()

print('Camera Calibration data saving')

print('Please Wait.....')

ret, mtx, dist, rvecs, tvec =cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

np.savez('calib.npz', ret=ret, mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvec)

print('Camera Calibration data saved')