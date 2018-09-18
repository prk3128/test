import numpy as np
import cv2

def AutoCanny(img, sigma=0.33) :
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    v = np.median(gray)

    lower = int(max(0,(1.0-sigma)*v))
    upper = int(min(255,(1.0+sigma)*v))

    canny = cv2.Canny(gray, lower, upper)

    return canny