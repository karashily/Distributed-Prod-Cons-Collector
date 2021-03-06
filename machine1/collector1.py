import sys
import numpy as np
import zmq
import time
from skimage.filters import threshold_otsu
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

def collector1(machine1_ip, port_rcv, port_snd, collector_num):
    context = zmq.Context()
    zmqSocket_rcv = context.socket(zmq.PULL)
    zmqSocket_rcv.bind("tcp://127.0.0.1:"+str(port_rcv))
    zmqSocket_snd = context.socket(zmq.PUSH)
    zmqSocket_snd.bind("tcp://{}:".format(machine1_ip)+str(port_snd))
    while True:
        data = zmqSocket_rcv.recv_pyobj()
        print("image {} received by collector".format(data['frame_number']) + str(collector_num))
        zmqSocket_snd.send_pyobj(data)
