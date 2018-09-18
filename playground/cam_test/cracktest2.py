import cv2
import numpy as np

canny_lower = 50
canny_upper= 100

index = 0

cam = cv2.VideoCapture(0)
cam.set(3,500)
cam.set(4,500)
cam.set(cv2.CAP_PROP_FPS,30)

while(cam.isOpened()) :
    ret, img = cam.read()
    origin = img.copy()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #img = img[50:450,50:450]
    #img = cv2.medianBlur(img,5)
    #img = cv2.medianBlur(img,5)
    #img = cv2.GaussianBlur(img,(5,5),0)

    cimg = cv2.Canny(img,canny_lower,canny_upper)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100, np.array([[]]), 60, 195, 0, 0)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv2.circle(origin, (x, y), r, (0, 0, 255), 4)
            cv2.rectangle(origin, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    lines = cv2.HoughLines(cimg,1,np.pi/180,90)

    if lines is None :
        cv2.imshow("ROBO Vision", origin)
        cv2.imshow("vision",img)
    if lines is not None :
        cv2.imshow("ROBO Vision", origin)
        cv2.imshow("vision", img)

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

            cv2.line(cimg, (x1, y1), (x2, y2), (0, 0, 0),15)
    cimg = cimg[50:450,50:450]

    cv2.imshow("Crack Detector",cimg)

    if(cv2.waitKey(20)==27) :
        break

cam.release()
cv2.destroyAllWindows()