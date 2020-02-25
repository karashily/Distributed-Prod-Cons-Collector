import numpy as np
import zmq
import time
from skimage.filters import threshold_otsu
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

def producer(video_path, port, n):

    context = zmq.Context()
    zmqSocket = context.socket(zmq.PUSH)
    zmqSocket.bind("tcp://127.0.0.1:"+str(port))

    cap = cv2.VideoCapture(video_path)
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    frame_number = 1
    while(cap.isOpened()):
        ret, rgb_frame = cap.read()
        if ret == True:
            cv2.imshow('Input', rgb_frame)
            message = {'img' : rgb_frame , 'frame_number' : frame_number}
            zmqSocket.send_pyobj(message)
            frame_number += 1
            c = cv2.waitKey(1)
            if c == 27:
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
