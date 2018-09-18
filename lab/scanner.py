import cv2
import numpy as np
import distortion
import auto_canny as auto
import hough
import newlib
import client

count = 0
kernel = np.ones((3,3), np.uint8)
Hough = hough.hough()
Dist = distortion.distortion()
Trans = client.TrasnferClient(ServerIP='192.168.0.6')

cam = cv2.VideoCapture(0)

while(cam.isOpened()) :
    I1 = []
    I2 = []
    I3 = []

    ret, img = cam.read()

    img = Dist.Undistort(img)

    img = img[90:340, 175:425]

    h, w = img.shape[:2]

    #img_h = auto.AutoCanny(img)
    img_h = Hough.HoughDetect(img)
    img_h = cv2.morphologyEx(img_h, cv2.MORPH_CLOSE, kernel, iterations=1)

    npic_0 = np.zeros((h,w), dtype=np.float32)
    npic_1 = np.zeros((h,w), dtype=np.float32)
    npic_2 = np.zeros((h,w), dtype=np.float32)
    npic_3 = np.zeros((h,w), dtype=np.float32)

    points = newlib.GooBoundary(img_h)
    for (x,y) in points[0] :
        cv2.circle(npic_0, (x,y), 1, (255, 255, 255), -1)
    cv2.imshow("Boundary",npic_0)
    key = cv2.waitKey(10)

    len_x, len_y, npic_1 = newlib.MakeLength(img_h,points)

    grad_x = (np.gradient(len_x))
    grad_y = (np.gradient(len_y))

    for j in range(len(points[2])):
        if grad_x[j] <= 10:
            grad_x[j] = 0
        if grad_y[j] <= 10:
            grad_y[j] = 0

    grad2_x = (np.gradient(grad_x))
    grad2_y = (np.gradient(grad_y))

    for j in range(len(points[2])):
        if grad2_x[j] <= 10:
            grad2_x[j] = 0
        if grad2_y[j] <= 10:
            grad2_y[j] = 0

    for j in range(len(points[2])):
        for i in range(len(points[1])):
            p = np.sqrt(grad_x[i] * grad_y[j])
            if p > 0:
                I1.append((i, j, p))
            npic_1[j, i] = p

    for j in range(len(points[2])):
        for i in range(len(points[1])):
            p = np.sqrt(grad2_x[i] * grad2_y[j])
            if p > 0:
                I2.append((i, j, p))
            npic_2[j, i] = p

    print("\nlen_x\n")
    print(len_x)
    print("\ngrad_x\n")
    print(grad_x)
    print("\ngrad2_x\n")
    print(grad2_x)
    print("")
    print(len(I1))
    print(len(I2))
    print(len(I1)-len(I2))
    if len(I1) > 160 :

        npic_1 = cv2.morphologyEx(npic_1,cv2.MORPH_DILATE,kernel,iterations=1)
        npic_2 = cv2.morphologyEx(npic_2, cv2.MORPH_DILATE, kernel, iterations=1)
        npic_3 = np.subtract(npic_2,npic_1)

        for j in range(len(points[2])):
            for i in range(len(points[1])):
                if npic_3[j,i] > 0 :
                    I3.append((i,j,npic_3[j,i]))

        cm1 = newlib.CM(I1)
        cm2 = newlib.CM(I2)
        cm3 = newlib.CM(I3)

        cm = ((cm1[0]+cm2[0]+cm3[0])/3,(cm1[1]+cm2[1]+cm3[1])/3)
        cm = tuple(np.uint8(cm))

        img = cv2.rectangle(img,cm,cm,(0,0,255),10)
        img = cv2.circle(img, cm, 100, (0, 255, 0), 10)

        if count > 200 :
            cv2.imwrite('/home/cae-lab/Desktop/result.png',img)
            #Trans.Transfer(filename='result.png')

    cv2.imshow("Detector",img)

    if count > 200 :
        count = 0
    else :
        count = count +1

    if cv2.waitKey(1)==27 :
        break

cam.release()

cv2.destroyAllWindows()