import sys
sys.path.append('D:/anaconda3/envs/opencv430/Lib/site-packages')
import cv2

capture = cv2.VideoCapture(0)

while(True):
    ret,frame = capture.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()