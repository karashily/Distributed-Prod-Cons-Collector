import zmq
import sys

def final_collector(port):
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://127.0.0.1:{}".format(port))
    output_file = open("contours.txt", "a+")
    while True:
        recv_data = socket.recv_pyobj()

        frame_num = recv_data['frame_number']
        contours = recv_data['img']

        print("Contours {} Recieved".format(frame_num))        
        
        output_file.write("{}: {}\n".format(frame_num, contours))
    output_file.close()