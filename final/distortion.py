import cv2
import numpy as np

class distortion() :

    def __init__(self) :
        # import calibration data
        calib = np.load("calib.npz")
        self.mtx = calib['mtx']
        self.dist = calib['dist']

    def Undistort(self, img) :
        # undistortion
        h, w = img.shape[:2]
        newcamera_mtx, roi = cv2.getOptimalNewCameraMatrix(self.mtx, self.dist, (w, h), 1, (w, h))
        dst = cv2.undistort(img, self.mtx, self.dist, None, newcamera_mtx)
        x, y, w, h = roi
        dst = dst[y:y + h, x:x + w]

        return dst