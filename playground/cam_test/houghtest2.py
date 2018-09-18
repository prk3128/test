import numpy as np
import cv2

def get_contour_precedence(contour, cols):
    tolerance_factor = 10
    origin = cv2.boundingRect(contour)
    return ((origin[1] // tolerance_factor) * tolerance_factor) * cols + origin[0]

cam = cv2.VideoCapture(0)
cam.set(3,500)
cam.set(4,500)

while(cam.isOpened()) :
    lower_bound = np.array([0, 0, 10])
    upper_bound = np.array([255, 255, 195])

    ret, img = cam.read()

    cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    mask = cv2.inRange(img, lower_bound, upper_bound)

# mask = cv2.adaptiveThreshold(image_ori,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY_INV,33,2)

    kernel = np.ones((3, 3), np.uint8)

#Use erosion and dilation combination to eliminate false positives.
#In this case the text Q0X could be identified as circles but it is not.
    mask = cv2.erode(mask, kernel, iterations=6)
    mask = cv2.dilate(mask, kernel, iterations=3)

    closing = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    contours.sort(key = lambda x: cv2.boundingRect(x)[0])

    array = []
    ii = 1

    for c in contours:
        (x,y),r = cv2.minEnclosingCircle(c)
        center = (int(x),int(y))
        r = int(r)
        if r >= 6 and r<=10:
            cv2.circle(img,center,r,(0,255,0),2)
            array.append(center)

    cv2.imshow("preprocessed", img)

    if(cv2.waitKey(1)==27) :
        break

cam.release()
cv2.destroyAllWindows()
