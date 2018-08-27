import cv2

cam = cv2.VideoCapture('/home/cae/Desktop/videotest.avi')

while (cam.isOpened()):

    ret, img = cam.read()

    if(ret==True) :
        cv2.imshow('GodSY',img)
          # 불러온 이미지 출력하기

        if cv2.waitKey(100)==27 :
            break
    else :
        break

cam.release()

cv2.destroyAllWindows()