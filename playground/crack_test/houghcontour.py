import cv2
import numpy as np

canny_lower = 100
canny_upper = 150

calib = np.load("/home/cae/PycharmProjects/crack_test/calib.npz")

mtx = calib['mtx']
dist = calib['dist']

cam = cv2.VideoCapture(0)

while(cam.isOpened()) :

    ret, img = cam.read()

    h, w = img.shape[:2]

    newcamera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

    udst = cv2.undistort(img, mtx, dist, None, newcamera_mtx)

    x, y, w, h = roi

    udst = udst[y:y+h, x:x+h]

    udst = cv2.cvtColor(udst,cv2.COLOR_BGR2GRAY)

    udst = cv2.medianBlur(udst,5)

    udst = cv2.Canny(udst,canny_lower,canny_upper)

    udst = cv2.resize(udst,(500,500))

    cv2.imshow("CAM",udst)

    img_line = np.zeros((500,500))

    img_contour, contours, hierarchy = cv2.findContours(udst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img_contour = cv2.drawContours(img_contour, contours, -1, (255, 255, 255), 3)

    lines = cv2.HoughLines(udst,1,np.pi/180,90)

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

            cv2.line(img_line, (x1, y1), (x2, y2), (255, 255, 255), 8)

    result = (img_contour)-(img_line)

    cv2.imshow("hough lines",img_line)
    cv2.imshow("contour",img_contour)
    cv2.imshow("result",result)

    if(cv2.waitKey(1)==27) :
        break

cam.release()
cv2.destroyAllWindows()