import sys
import numpy as np
import zmq
import time
from skimage.filters import threshold_otsu
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def collector1(port_rcv, port_snd, collector_num):
    context = zmq.Context()
    zmqSocket_rcv = context.socket(zmq.PULL)
    zmqSocket_rcv.bind("tcp://127.0.0.1:"+str(port_rcv))

    img = zmqSocket_rcv.recv_pyobj()
    plt.figure()
    plot_img = plt.imshow(img)
    plt.title("this image collected by collector number: "+str(collector_num))
    plt.show()

collector1(5558, 5559, 1)
