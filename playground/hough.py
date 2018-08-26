import cv2
import numpy as np
import auto_canny as auto

class hough() :
    def __init__(self,canny_lower=100,canny_upper=150) :
        self.canny_lower = canny_lower
        self.canny_upper = canny_upper
        self.linek = np.zeros((5,5), dtype=np.uint8)
        self.linek[2, ...] = 1
        self.kernel = np.ones((3,3),np.uint8)

    def HoughDetect(self,img) :
#        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #h, w = img.shape[:2]
        img = cv2.medianBlur(img,5)
        img = auto.AutoCanny(img)
#        img = cv2.Canny(img,self.canny_lower,self.canny_upper)

        #img = cv2.resize(img,(300,300))

        img_line = np.zeros((250,250))

        img_contour, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img_contour = cv2.drawContours(img_contour, contours, -1, (255, 255, 255), 1)
        #cv2.imshow("contour",img_contour)
        lines = cv2.HoughLines(img,1,np.pi/1440,90)

        if lines is not None:

            for line in lines:
                rho, theta = line[0]
                a = np.cos(theta)
                b = np.sin(theta)

                x0 = a * rho
                y0 = b * rho

                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))

                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))

                cv2.line(img_line, (x1, y1), (x2, y2), (255, 255, 255), 3)
        #cv2.imshow("line",img_line)
        result = img_contour-img_line

#        result = cv2.morphologyEx(result, cv2.MORPH_ERODE, self.kernel, iterations=2)
        #result = cv2.morphologyEx(result, cv2.MORPH_OPEN, self.linek, iterations=1)

        return result