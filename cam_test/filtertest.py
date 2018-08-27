import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,320)
cam.set(5,10)

while(cam.isOpened()) :
    ret, img = cam.read()

    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(img,(5,5),0)
    median = cv2.medianBlur(img,5)
    median = cv2.medianBlur(img,5)
    biblur = cv2.bilateralFilter(img,9,75,75)

    canny = cv2.Canny(img,250,300)
    blur = cv2.Canny(blur,250,300)
    median = cv2.Canny(median,250,300)
    biblur = cv2.Canny(biblur,250,300)

    lines = cv2.HoughLines(median, 1, np.pi / 180, 100)
    #img_canny = cv2.Canny(img, 250, 250)

    if lines is None:
        cv2.imshow("Original", canny)

    elif lines is not None:
        cv2.imshow("Original", canny)
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

            cv2.line(median, (x1, y1), (x2, y2), (0, 0, 0), 13)

    #cv2.imshow("blur",blur)
    cv2.imshow("median",median )
    #cv2.imshow("biblur",biblur)
    #cv2.imshow("canny",canny)

    if(cv2.waitKey(1)==27) :
        break

cam.release()
cv2.destroyAllWindows()
