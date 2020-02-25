from collector_final import *
from consumer_contours import *
import random
import threading
import sys

# read n from conf file

conf = open("machine2.conf", "r").read().split('\n')

n = int(conf[1])
machine1_ip = conf[3]

print(n, machine1_ip)

# n = int(sys.argv[1])
recv_init_port = 49162
"192.168.43.223"
i = 0
for j in range(n):
    cons_cont = threading.Thread(target=consumer_contours, args=[machine1_ip, recv_init_port+i, 1314, j+1])
    cons_cont.start()
    if(j%2==1):
        i += 1

coll_final = threading.Thread(target=final_collector, args=[1314])
coll_final.start()
