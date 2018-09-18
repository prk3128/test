import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(511,511),(255,0,0),5)

cv2.rectangle(img,(100,100),(400,400),(128,128,128),3)

cv2.circle(img,(250,250),150,(0,255,255),-1)

cv2.imshow('drawing',img)

cv2.waitKey(0)

cv2.destroyAllWindows()