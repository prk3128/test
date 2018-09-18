import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)

font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 4
font_thickness = 5

while(cam.isOpened()) :
    ret, img = cam.read()
    img2 = img
    cv2.circle(img,(600,400),5,(0,0,255),-1)

    key=cv2.waitKey(1)

    if(key==27):
        break
    elif (key==ord('s')) :
        cv2.putText(img2,'Fired',(500,700),font,font_size,(0,0,255),font_thickness,cv2.LINE_AA)
        cv2.imshow("Scope",img2)


    cv2.imshow("Scope",img)

cam.release()
cv2.destroyAllWindows()
