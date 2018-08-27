import cv2
import client
import morph
import hough
import distortion as dist

Trans = client.TrasnferClient()
Morph = morph.morph()
Hough = hough.hough(50,100)
Dist = dist.distortion()

#bright = cv2.imread("./bright.jpg")
#bright = cv2.cvtColor(bright,cv2.COLOR_BGR2GRAY)

#width, height = bright.shape[:2]

#for i in range(width):
#    for j in range(height):
#        bright[i, j] = 255-bright[i, j]

p=0
q=0

# construct camera object
cam = cv2.VideoCapture(0)

while(True) :
    ret, img = cam.read()

    #img = cv2.imread('001_crack.jpg')
#    q += 1

    dst = Dist.Undistort(img)

    if(cv2.waitKey(1)==27) :
        break
    #dst = cv2.resize(dst,(500,500))

#    dst=cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
#    dst = bright-dst

#    for i in range(width):
#        for j in range(height):
#            dst[i, j] = -255+dst[i, j]
    #   dst = cv2.equalizeHist(dst)
    cv2.imshow("cam", dst)

    #m_img = dst.copy()
    #h_img = dst.copy()

    #m_img = Morph.MorphDetect(m_img)
    #h_img = Hough.HoughDetect(h_img)

    #m_img = cv2.resize(m_img,(300,300))
    #result = h_img-m_img
    #result = dst
    #cv2.imshow("Morph",m_img)
    #cv2.imshow("Hough",h_img)
    #cv2.imshow("result",result)

#    if q > 500 :
#
#        for i in range(len(result)) :
#            for j in range(len(result[i,:])) :
#                p += result[i,j]
#
#        if p > 1000 * 255 :
#            cv2.imwrite('/home/cae/Desktop/crack.png',result)
#            Trans.Transfer()
#            p=0
#            q=0

cam.release()

cv2.destroyAllWindows()