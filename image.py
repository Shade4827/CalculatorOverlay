import sys
sys.path.append('D:/anaconda3/envs/opencv430/Lib/site-packages')
import cv2

capture = cv2.VideoCapture(0)

def ChangeCamera(num):
    capture = cv2.VideoCapture(num)

def ReadImage():
    ret,frame = capture.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

def releaseCapture():
    capture.release()

#while(True):
#    ret,frame = capture.read()
#    cv2.imshow('camera',frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

#capture.release()
#cv2.destroyAllWindows()