import cv2
import numpy as np

class morph() :

    def __init__(self) :

        # kernel
        self.linek = np.zeros((11, 11), dtype=np.uint8)
        self.linek[5, ...] = 1
        self.kernel = np.ones((3,3),np.uint8)
        self.sharpk2 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]])/8
        self.iter = 1

    def MorphDetect(self, img) :
        # image gray, Blur, threshold
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = cv2.filter2D(gray, -1, self.sharpk2)

        ret, gray = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
        gray = cv2.medianBlur(gray, 5)

        # morpohology
        u = gray.copy()
        v = gray.copy()
        v = np.transpose(v)

        u = cv2.morphologyEx(u, cv2.MORPH_OPEN, self.linek, iterations=self.iter)
        v = cv2.morphologyEx(v, cv2.MORPH_OPEN, self.linek, iterations=self.iter)
        v = np.transpose(v)

        wgray = u|v

        result = gray - wgray
        #result = wgray

        #ret, result = cv2.threshold(result, 240, 255, cv2.THRESH_BINARY)
        #result = result[50:,50:]

        return result