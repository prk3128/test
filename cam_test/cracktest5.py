import cv2
import numpy as np

canny_lower = 200
canny_upper = 300

img = np.zeros((500,500))

crack = cv2.imread('/home/cae/Desktop/gadget-test/panel4/panel4_crack2.JPG',0)

crack2 = cv2.resize(crack,(500,500))

kernel = np.ones((3,3),np.float32)/9

crack2 = cv2.filter2D(crack2,-1,kernel)
ccrack2 = cv2.Canny(crack2,canny_lower,canny_upper)

ccrack2_contour = ccrack2.copy()
ccrack2_contour, contours, hierarchy = cv2.findContours(ccrack2_contour, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
ccrack2_contour = cv2.drawContours(ccrack2_contour, contours, -1, (255, 255, 255), 3)

lines = cv2.HoughLines(ccrack2,1,np.pi/180,90)

if lines is not None :

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

        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255),15)

result = ccrack2_contour-img

cv2.imshow("result",result)
cv2.imshow("line",img)
cv2.imshow("contour",ccrack2_contour)

cv2.waitKey(0)

cv2.destroyAllWindows()