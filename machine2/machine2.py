from collector_final import *
from consumer_contours import *
import random


# read n from conf file

n = 1
recv_init_port = 49162

i = 0
cons_ids = []
for j in range(n):
    id = int(random.random())
    if(id not in cons_ids):
        consumer_contours(recv_init_port + i, 1314, id)
        cons_ids.append(id)
        if(j%2==1):
            i += 1

collector_final(1314)