from collector_final import *
from consumer_contours import *
import random


# read n from conf file

n = 5

cons_ids = []
while (len(cons_ids) < n):
    id = int(random.random())
    if(id not in cons_ids):
        consumer_contours(recv_port, 1314, id)
        cons_ids.append(id)

collector_final(1314)