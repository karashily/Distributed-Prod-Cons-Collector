import zmq

def final_collector(port):
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://127.0.0.1:"+str(port))
    while True:
        contours = socket.recv_pyobj()
        #TODO: append to txt file