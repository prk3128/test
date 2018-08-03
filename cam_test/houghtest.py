import cv2
import numpy as np
import argparse

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,360)
#ap = argparse.ArgumentParser()
#ap.add_argument("-i","--image",required=True, help="Path to the image")
#args = vars(ap.parse_args())

#image = cv2.imread('/home/cae/Desktop/test.jpg')

while(cam.isOpened()):
    ret, img = cam.read()
    output = img.copy()
    gray=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)
    gray = cv2.medianBlur(gray, 5)

    canny = cv2.Canny(gray, 60, 195)

    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,1,np.array([[]]),60,195,0,0)

    if circles is not None :
        circles = np.round(circles[0, : ]).astype("int")

        for (x,y,r) in circles :
            cv2.circle(output,(x,y),r,(0,0,255),4)
            cv2.rectangle(output,(x-5,y-5),(x+5,y+5),(0,128,255),-1)

    cv2.imshow("output",output)
    cv2.imshow("Canny",canny)

    if(cv2.waitKey(1)==27):
        break

cam.release()
cv2.destroyAllWindows()