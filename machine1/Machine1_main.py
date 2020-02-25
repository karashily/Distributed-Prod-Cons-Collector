import sys
import threading
from Producer import *
from Consumer_otsu import *
from Collector1 import *
import numpy as np
import zmq
import time
from skimage.filters import threshold_otsu
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


conf_file = open("machine1.conf","r")
input = conf_file.readlines()
n = int(input[1])
video_path = input[3]
machine1_ip = input[5]

prod_snd = cons_rcv = 49152
init_port1 = init_port2 = 49153
inti_port3 = 49162

prod_thread = threading.Thread(target=producer, args=[video_path[0:len(video_path)-1], prod_snd, n])
prod_thread.start()

cons_num = 1
for i in range(n):
    cons_thread = threading.Thread(target=consumer_otsu, args=[cons_rcv, init_port1, cons_num])
    cons_thread.start()
    cons_num += 1
    if(i%2 == 1):
        init_port1 += 1

for i in range((n+1)//2):
    coll_thread = threading.Thread(target=collector1, args=[machine1_ip[0:len(machine1_ip)-1], init_port2, inti_port3, i+1])
    coll_thread.start()
    init_port2 += 1
    inti_port3 += 1
