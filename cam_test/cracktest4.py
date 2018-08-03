import cv2
import numpy as np

canny_lower = 50
canny_upper = 100

k = np.ones((3, 3), np.float32) / 9

cam = cv2.VideoCapture(0)
cam.set(3,500)
cam.set(4,500)

while(cam.isOpened()) :
    ret, img = cam.read()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    #ret2, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    img_blur = img.copy()

    img_blur = cv2.filter2D(img_blur, -1, k)

    cimg = cv2.Canny(img, canny_lower, canny_upper)
    cimg_blur = cv2.Canny(img_blur, canny_lower, canny_upper)

    cimg, contours, hierarchy = cv2.findContours(cimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cimg = cv2.drawContours(cimg, contours, -1, (255, 255, 255), 3)

    cimg_blur, contours, hierarchy = cv2.findContours(cimg_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cimg_blur = cv2.drawContours(cimg_blur, contours, -1, (255, 255, 255), 3)

    result = cimg-cimg_blur

    result = cv2.medianBlur(result,5)

    cv2.imshow("vision", cimg)
    cv2.imshow("vision2", cimg_blur)
    cv2.imshow("vision3", result)

    if(cv2.waitKey(30)==27) :
        break

cam.release()
cv2.destroyAllWindows()