import cv2
import numpy as np
import auto_canny as auto

class hough() :
    def __init__(self) :
        self.linek = np.zeros((5,5), dtype=np.uint8)
        self.linek[2, ...] = 1
        self.kernel = np.ones((3,3),np.uint8)

    def HoughDetect(self,img) :
        h, w = img.shape[:2]

        img = cv2.medianBlur(img,5)

        img = auto.AutoCanny(img)

        img_line = np.zeros((h,w))

        img_contour, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img_contour = cv2.drawContours(img_contour, contours, -1, (255, 255, 255), 3)

        lines = cv2.HoughLines(img,1,np.pi/1440,180)

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

                cv2.line(img_line, (x1, y1), (x2, y2), (255, 255, 255), 5)

        result = img_contour-img_line
        result = result[90:340, 175:425]

        #result = cv2.morphologyEx(result, cv2.MORPH_ERODE, self.kernel, iterations=2)
        #result = cv2.morphologyEx(result, cv2.MORPH_OPEN, self.linek, iterations=1)

        return result

def CM(gray, size1 = (100,100), size2 = (250,250)  ) :

    (h1,w1) = size1
    (h2,w2) = size2

    gray = cv2.resize(gray,size1)
    I = []
    cx = 0
    cy = 0
    count = 0

    for x in range(w1) :
        for y in range(h1) :
            if gray[y,x] > 0 :
                I.append((x,y))

    for (x,y) in I :
        cx = cx + x
        cy = cy + y
        count += 1

    if count :
        cx = np.int(cx*(w2/w1)/count)
        cy = np.int(cy*(h2/h1)/count)

        return (cx,cy), count

    return (0,0), count