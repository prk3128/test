import cv2
import numpy as np

def GooBoundary(gray) :

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

def MakeLength(gray, points) :
    len_x = []
    len_y = []
    npic = gray.copy()
    npic[:] = 0

    for (x, y) in points[1]:
        for (u, v) in points[2]:
            if x == u:
                len_x.append(np.abs(v - y))
    for (x, y) in points[3]:
        for (u, v) in points[4]:
            if y == v:
                len_y.append(np.abs(u - x))
    for j in range(len(points[2])):
        for i in range(len(points[1])):
            npic[j, i] = np.sqrt((len_y[j] * len_x[i]))
    return len_x, len_y, npic

def CM(I) :
    cx = 0
    cy = 0
    cm = 0
    for (x,y,p) in I :
        cx = cx + (y/(p*p))
        cy = cy + (x/(p*p))
        cm = cm + 1/(p*p)
    return ((cx/cm),(cy/cm))