import cv2
import numpy as np

canny_lower = 200
canny_high = 300

crack2 = cv2.imread('/home/cae/Desktop/gadget-test/panel4/panel4_crack2.JPG',0)
crack2_blur = crack2.copy()

kernel = np.ones((3,3),np.float32)/9

crack2_blur = cv2.filter2D(crack2_blur,-1,kernel)

crack2 = cv2.medianBlur(crack2,5)

ccrack2 = cv2.Canny(crack2,canny_lower,canny_high)
ccrack2_blur = cv2.Canny(crack2_blur,canny_lower,canny_high)

ccrack2, contours, hierarchy = cv2.findContours(ccrack2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
ccrack2 = cv2.drawContours(ccrack2,contours,-1,(255,255,255),3)

ccrack2_blur, contours, hierarchy = cv2.findContours(ccrack2_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
ccrack2_blur = cv2.drawContours(ccrack2_blur,contours,-1,(255,255,255),3)

result = ccrack2_blur-ccrack2

result = cv2.medianBlur(result,5)

cv2.imshow("vision",ccrack2)
cv2.imshow("vision2",ccrack2_blur)
cv2.imshow("vision3",result)

cv2.waitKey(0)

cv2.destroyAllWindows()