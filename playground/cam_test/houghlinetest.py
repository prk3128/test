import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,360)
cam.set(5,1)

background = np.zeros((360, 640, 3), np.uint8)

index = 0

while(cam.isOpened()) :
    ret, img = cam.read()
    origin = img.copy()
    background = np.zeros((360, 640, 3), np.uint8)
    '''
    if(index < 3) :
        index += 1
    else :
        background = np.zeros((255, 255, 3), np.uint8)
        index=0
    '''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 250, 300)
    lines = cv2.HoughLines(canny,1,np.pi/180,100)
    #img_canny = cv2.Canny(img, 250, 250)

    if lines is None :
        cv2.imshow("Original", origin)

    elif lines is not None :
        cv2.imshow("Original", origin)
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)

            x0 = a*rho
            y0 = b*rho

            x1 = int(x0+1000*(-b))
            y1 = int(y0+1000*(a))

            x2 = int(x0-1000*(-b))
            y2 = int(y0-1000*(a))

            cv2.line(background,(x1,y1),(x2,y2),(255,255,255),2)
            cv2.line(img, (x1,y1),(x2,y2),(255,255,255),2)

    canny = cv2.resize(canny,(255,255))
    background = cv2.resize(background,(255,255))
    cv2.imshow("vision",background)
    cv2.imshow("vision2",img)
    cv2.imshow("Canny",canny)

    if(cv2.waitKey(1)==27) :
        break

cam.release()
cv2.destroyAllWindows()