import cv2
import client
import hough
import distortion as dist

Trans = client.TrasnferClient()
Hough = hough.hough()
Dist = dist.distortion()

q=0

# construct camera object
cam = cv2.VideoCapture(0)

while(True) :
    ret, img = cam.read()

    img = Dist.Undistort(img)
    #img = img[90:340, 175:425]


    h_img = img.copy()

    h_img = Hough.HoughDetect(h_img)

    result = img[90:340, 175:425]


    if q > 20 :
        center, count = hough.CM(h_img)

        if count > 0:
            img = cv2.circle(img[90:340, 175:425], center, 50, (0, 255, 0), 5)
            img = cv2.rectangle(img, center, center, (0, 0, 255), 10)

            #cv2.imwrite('/home/cae/Desktop/crack.png',result)
            #Trans.Transfer()
        q=0

    q += 1
    print(q)

    cv2.imshow("result",result)

    if(cv2.waitKey(1)==27) :
            break

cam.release()

cv2.destroyAllWindows()