import sys
sys.path.append('D:/anaconda3/envs/opencv430/Lib/site-packages')
import cv2
import configparser

config = configparser.ConfigParser()
config.read("config.ini",encoding='utf-8')
cameraNum = int(config['Camera']['num'])

capture = cv2.VideoCapture(cameraNum)

def CheckCameraConnection():
    true_camera_is = []  # 空の配列を用意

    # カメラ番号を0～9まで変えて、COM_PORTに認識されているカメラを探す
    for num in range(0, 10):
        cap = cv2.VideoCapture(num)
        ret, frame = cap.read()

        if ret is True:
            true_camera_is.append(num)

    return len(true_camera_is)

def ChangeCamera(num):
    with open("config.ini",mode="w") as file:
        text = "[Camera]\nnum = " + str(num)
        file.write(text)

def ReadImage():
    ret,frame = capture.read()
    if ret:
        frame = cv2.resize(frame,dsize=(960,720))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    else:
        return None

def ReleaseCapture():
    global capture
    capture.release()