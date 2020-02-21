import sys
import numpy as np
import zmq
import time
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def consumer_otsu(port_rcv, port_snd, consumer_num):
    context = zmq.Context()
    zmqSocket_rcv = context.socket(zmq.PULL)
    zmqSocket_rcv.connect("tcp://127.0.0.1:"+str(port_rcv))
    zmqSocket_snd = context.socket(zmq.PUSH)
    zmqSocket_snd.connect("tcp://127.0.0.1:"+str(port_snd))


    img_gray = rgb2gray(zmqSocket_rcv.recv_pyobj())
    thresh = threshold_otsu(img_gray)
    binary_img = np.zeros((img_gray.shape[0],img_gray.shape[1]))
    binary_img[img_gray >= thresh] = 1
    zmqSocket_snd.send_pyobj(binary_img)

consumer_otsu(5557, 5558, 1)
