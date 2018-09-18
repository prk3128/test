import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 1280)  # CV_CAP_PROP_FRAME_WIDTH
cam.set(4, 720)  # CV_CAP_PROP_FRAME_HEIGHT
# cam.set(5,0) #CV_CAP_PROP_FPS

ret, vid = cam.read()
#img = cv2.flip(img,0)

fps=15
width = vid.shape[1]
height = vid.shape[0]

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('/home/cae/Desktop/videotest.avi',fourcc, fps, (width,height))

while (cam.isOpened()):

    ret, vid = cam.read()  # 캠 이미지 불러오기

    #gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Cam Viewer", vid)  # 불러온 이미지 출력하기

    key=cv2.waitKey(1)

    if key == 27:
        break  # esc to quit
    elif key == ord('s'):
        output.write(vid)

cam.release()
output.release()
cv2.destroyAllWindows()
