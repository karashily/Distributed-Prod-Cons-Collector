from collector_final import *
from consumer_contours import *
import random
import threading
import sys

# read n from conf file

n = int(sys.argv[1])
recv_init_port = 49162

i = 0
for j in range(n):
    cons_cont = threading.Thread(target=consumer_contours, args=[recv_init_port+i, 1314, j+1])
    cons_cont.start()
    if(j%2==1):
        i += 1

coll_final = threading.Thread(target=final_collector, args=[1314])
coll_final.start()
