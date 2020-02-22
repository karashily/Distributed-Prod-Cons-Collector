import numpy as np
import zmq
import time
from skimage.filters import threshold_otsu
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

def producer(port):

    context = zmq.Context()
    zmqSocket = context.socket(zmq.PUSH)
    zmqSocket.bind("tcp://127.0.0.1:"+str(port))

    cap = cv2.VideoCapture(0)
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, rgb_frame = cap.read()
        cv2.imshow('Input', rgb_frame)
        zmqSocket.send_pyobj(rgb_frame)
        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
