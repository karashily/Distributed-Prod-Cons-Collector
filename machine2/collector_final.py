import zmq
import sys

def final_collector(port):
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://127.0.0.1:"+str(port))
    while True:
        recv_data = socket.recv_pyobj()
        
        frame_num = recv_data['frame_number']
        contours = recv_data['contours']

        output_file = open("contours.txt", "w+")
        output_file.write("{}: {}\n".format(frame_num, contours))