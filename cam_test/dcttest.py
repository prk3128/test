import cv2
import numpy as np

img1 = cv2.imread("/home/cae/Desktop/panel2.JPG",0)
img2 = cv2.imread("/home/cae/Desktop/panel2_extended.JPG",0)
img3 = cv2.imread("/home/cae/Desktop/panel2_extended_crack.JPG",0)

img1 = cv2.Canny(img1,250,300)
img2 = cv2.Canny(img2,250,300)
img3 = cv2.Canny(img3,250,300)

cv2.imshow("vision",img2)
cv2.imshow("crack",img3)

img1 = cv2.resize(img1,(32,32))
img2 = cv2.resize(img2,(32,32))
img3 = cv2.resize(img3,(32,32))

img1 = cv2.resize(img1,(255,255))
img2 = cv2.resize(img2,(255,255))
img3 = cv2.resize(img3,(255,255))

imf1 = np.float32(img1)
imf2 = np.float32(img2)
imf3 = np.float32(img3)

img1_dct = cv2.dct(imf1)
img2_dct = cv2.dct(imf2)
img3_dct = cv2.dct(imf3)

img1 = np.uint8(img1_dct)
img2 = np.uint8(img2_dct)
img3 = np.uint8(img3_dct)

cv2.imshow('panel2',img1)
cv2.imshow('panel2_extended',img2)
cv2.imshow('panel2_extended_crack',img3)

cv2.waitKey(0)

cv2.destroyAllWindows()