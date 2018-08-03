import cv2
import numpy as np

canny_lower = 250
canny_upper= 300

panel = cv2.imread('/home/cae/Desktop/gadget-test/panel4/panel4.JPG',0)
crack1 = cv2.imread('/home/cae/Desktop/gadget-test/panel4/panel4_crack.JPG',0)
crack2 = cv2.imread('/home/cae/Desktop/gadget-test/panel4/panel4_crack2.JPG',0)

panel = cv2.resize(panel,(320,320))
crack1 = cv2.resize(crack1,(320,320))
crack2 = cv2.resize(crack2,(500,500),cv2.INTER_AREA)

#cv2.imshow("test",cv2.Canny(crack2,250,300))

panel = cv2.medianBlur(panel,5)
crack1 = cv2.medianBlur(crack1,5)
crack2 = cv2.medianBlur(crack2,5)

#cv2.imshow("test",crack2)

cpanel = cv2.Canny(panel,canny_lower,canny_upper)
ccrack1 = cv2.Canny(crack1,canny_lower,canny_upper)
ccrack2 = cv2.Canny(crack2,canny_lower,canny_upper)

test_origin = crack2
test_canny = ccrack2

cv2.imshow("canny",test_canny)

lines = cv2.HoughLines(test_canny,1,np.pi/180,100)


if lines is None :
    cv2.imshow("ROBO Vision", test_origin)

elif lines is not None :
    cv2.imshow("ROBO Vision", test_origin)
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

        cv2.line(test_canny,(x1,y1),(x2,y2),(0,0,0),11)

test_canny = cv2.resize(test_canny,(125,125))
test_canny = cv2.resize(test_canny,(250,250))
cv2.imshow("crack Detector",test_canny)

cv2.waitKey(0)

cv2.destroyAllWindows()


