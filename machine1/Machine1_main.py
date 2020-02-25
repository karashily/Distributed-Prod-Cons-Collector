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

n = int(sys.argv[1])
prod_snd = cons_rcv = 49152
init_port1 = init_port2 = 49153
inti_port3 = 49162

prod_thread = threading.Thread(target=producer, args=[prod_snd])
prod_thread.start()

cons_num = 1
for i in range((n+1)//2):
    for j in range(2):
        cons_thread = threading.Thread(target=consumer_otsu, args=[cons_rcv, init_port1, cons_num])
        cons_thread.start()
        cons_num += 1
    init_port1 += 1

for i in range((n+1)//2):
    coll_thread = threading.Thread(target=collector1, args=[init_port2, inti_port3, i+1])
    coll_thread.start()
    init_port2 += 1
    inti_port3 += 1
