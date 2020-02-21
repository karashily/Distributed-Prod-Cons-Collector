import numpy as np
import zmq
import time
from skimage.filters import threshold_otsu
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def producer(port):
    img = io.imread('images.jpeg')
    context = zmq.Context()
    zmqSocket = context.socket(zmq.PUSH)
    zmqSocket.bind("tcp://127.0.0.1:"+str(port))
    while True:
        zmqSocket.send_pyobj(img)

producer(5557)
