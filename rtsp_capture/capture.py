import cv2
import numpy as np
import os


# RTSP URL
rtsp_url = "rtsp://rtsp_url"
# Which transport we should we for rtsp capture
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

# Initializing video capture function with required parameters
vcap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

while(1):
    ret, frame = vcap.read()
    if ret == False:
        print("Frame is empty")
        break;
    else:
        cv2.imshow('VIDEO', frame)
        k=cv2.waitKey(1)
        if k== ord("q"):
            break