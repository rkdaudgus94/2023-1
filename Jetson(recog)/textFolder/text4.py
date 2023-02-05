import cv2
import numpy as np
import easyocr

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

if cap.isOpened() == False:
    print("Unable to read camera")

else :
# 프레임 정보
    frame_width = int(cap.get(3))
    frame_heigt = int(cap.get(4))

# 캠에서 찍은 비디오 저장
out = cv2.VideoWriter('/home/hyun/video/output.avi',
                cv2.VideoWriter_fourcc(*'XVID'),
                20.0,
                (frame_width, frame_heigt))
reader = easyocr.Reader(['ko','en'],gpu = True)
time = 0
while True :
    ret, frame = cap.read()
    time += 1
    
    if ret == True :
        out.write(frame)
        cv2.imshow('frame', frame)
        if (time % 10) == 0 :   
            # rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = reader.readtext(frame)
            print(result)
        if cv2.waitKey(1) & 0xFF == 27 :
            break
    else :
        break