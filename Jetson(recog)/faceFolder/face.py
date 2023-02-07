import cv2

def gstreamer_pipeline(
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=30,
    flip_method=0,
    ) :
    return (
    capture_width,
    capture_height,
    display_width,
    display_height,
    framerate,
    flip_method,
    )

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method = 0), cv2.CAP_GSTREAMER)

if cap.isOpened() == False :
    print("Unable open camera")

else :
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

out 