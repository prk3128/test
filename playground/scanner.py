import cv2
import numpy as np
import distortion
import auto_canny as auto
import hough

kernel = np.ones((3,3), np.uint8)
Hough = hough.hough()
Dist = distortion.distortion()

def dp(gray) :

    j, i = gray.shape[:2]

    point_x1 = []
    point_x2 = []
    point_y1 = []
    point_y2 = []

    for x in range(i) :
        for y in range(j) :
            if gray[y,x] == 255 :
                point_x1.append((x,y))
                break
            else :
                if y==j-1 :
                    point_x1.append((x, j-1))
                    break

    for x in range(i) :
        for y in range(j) :
            if gray[j-1-y,x] == 255 :
                point_x2.append((x, j-1-y))
                break
            else :
                if y==j-1 :
                    point_x2.append((x,0))
                    break

    for y in range(j) :
        for x in range(i) :
            if gray[y,x] == 255 :
                point_y1.append((x,y))
                break
            else :
                if x==i-1 :
                    point_y1.append((i-1, y))
                    break

    for y in range(j) :
        for x in range(i) :
            if gray[y,i-1-x] == 255 :
                point_y2.append((i-1-x, y))
                break
            else :
                if x==i-1 :
                    point_y2.append((0, y))
                    break
    points = point_x1+point_x2+point_y1+point_y2

    return tuple([points,point_x1,point_x2,point_y1,point_y2])
def MK(gray, points) :
    len_x = []
    len_y = []
    npic = gray.copy()
    npic[:] = 0

    for (x, y) in points[1]:
        for (u, v) in points[2]:
            if x == u:
                len_y.append(np.abs(v - y))
    for (x, y) in points[3]:
        for (u, v) in points[4]:
            if y == v:
                len_x.append(np.abs(u - x))
    for j in range(len(points[2])):
        for i in range(len(points[1])):
            npic[j, i] = np.sqrt((len_x[i] * len_y[j]))
    return len_x, len_y, npic

def CM(I) :
    cx = 0
    cy = 0
    cm = 0
    for (x,y,p) in I :
        cx = cx + (y)
        cy = cy + (x)
        cm = cm + 1
    return ((cx/cm),(cy/cm))

cam = cv2.VideoCapture(0)

while(cam.isOpened()) :

    count = 0

    ret, img = cam.read()

    img = Dist.Undistort(img)

    #gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)

    img = img[90:340, 175:425]
    img_h = Hough.HoughDetect(img)
    img_h = cv2.morphologyEx(img_h, cv2.MORPH_CLOSE, kernel, iterations=1)
    img_g = auto.AutoCanny(img)
    cv2.imshow("canny_img",img_g)
    img_g = cv2.morphologyEx(img_g, cv2.MORPH_CLOSE, kernel, iterations=1)
    pic = img_g.copy()
    pic[:] = 0
    pic2 = img_g.copy()
    pic2[:] = 0
    npic_1 = img_g.copy()
    npic_1[:] = 0
    npic_2 = img_g.copy()
    npic_2[:] = 0

    points1 = dp(img_g)
    points2 = dp(img_h)

    for (x,y) in points1[0] :
        cv2.circle(pic,(x,y),1,(255,255,255),-1)
    for (x,y) in points2[0] :
        cv2.circle(pic2,(x,y),1,(255,255,255),-1)



    key = cv2.waitKey(10)

    if(key==ord('s')) :
        I1 = []
        I2 = []

        len_x1, len_y1, npic_1 = MK(img_g,points1)
        len_x2, len_y2, npic_2 = MK(img_h,points2)
        diff_x1 = np.abs(np.diff(len_x1,n=2))
        diff_y1 = np.abs(np.diff(len_y1,n=2))
        diff_x2 = np.abs(np.diff(len_x2,n=2))
        diff_y2 = np.abs(np.diff(len_y2,n=2))

#        for j in range(len(points1[2])-2):
#            if diff_x1[j] <= 10 :
#                diff_x1[j] = 0
#            if diff_y1[j] <= 10 :
#                diff_y1[j] = 0
#        for j in range(len(points1[2])-2):
#            if diff_x2[j] <= 10 :
#                diff_x2[j] = 0
#            if diff_y2[j] <= 10 :
#                diff_y2[j] = 0

        print("\ngray")
        print(len_x1)
        print("")
        print("\ngray_diff")
        print(diff_y1)
        print("")
        print("\nhough")
        print(diff_y2)
        print("")

        npic_1[:,:] = 0
        npic_2[:,:] = 0

        for j in range(len(points1[2])-2):
            for i in range(len(points1[1])-2):
                p = np.sqrt((diff_x1[i] * diff_y1[j]))
                if p > 0 :
                    I1.append((i,j,p))
                npic_1[j,i] = p


        for j in range(len(points2[2])-2):
            for i in range(len(points2[1])-2):
                p = np.sqrt((diff_x1[i] * diff_y1[j]))
                if p > 0:
                    I2.append((i, j, p))
                npic_2[j, i] = p
        cm1 = CM(I1)
        cm2 = CM(I2)

        #cv2.circle(pic,tuple(np.uint8(cm1)),25,(255,255,255),10)
        img = cv2.rectangle(img,tuple(np.uint8(cm2)),tuple(np.uint8(cm2)),(125,125,125),10)
        img = cv2.circle(img, tuple(np.uint8(cm2)), 50, (0, 0, 255), 10)
        #ret, npic = cv2.threshold(npic,240,255,cv2.THRESH_BINARY)
        #npic_diff = np.transpose(npic_diff)
        cv2.imshow("Detector",img)
        cv2.imshow("gray_diff",npic_1)
        cv2.imshow("hough_diff",npic_2)

    if key==27 :
        break

    cv2.imshow("gray",pic)

    cv2.imshow("hough",pic2)

cam.release()

cv2.destroyAllWindows()