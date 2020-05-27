import sys
sys.path.append('D:/anaconda3/envs/opencv430/Lib/site-packages')
import cv2

capture = cv2.VideoCapture(0)

def CheckCameraConnection():
    true_camera_is = []  # 空の配列を用意

    # カメラ番号を0～9まで変えて、COM_PORTに認識されているカメラを探す
    for cameraNum in range(0, 10):
        cap = cv2.VideoCapture(cameraNum)
        ret, frame = cap.read()

        if ret is True:
            true_camera_is.append(cameraNum)

    return len(true_camera_is)

def ChangeCamera(num):
    global capture
    capture.release()
    capture = cv2.VideoCapture(num)

def ReadImage():
    ret,frame = capture.read()
    frame = cv2.resize(frame,dsize=(960,720))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

def ReleaseCapture():
    global capture
    capture.release()