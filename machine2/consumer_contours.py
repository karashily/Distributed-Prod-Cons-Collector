import zmq
import cv2

def consumer_contours(recv_port, send_port, consumer_id):
    context = zmq.Context()
    
    recv_socket = context.socket(zmq.PULL)
    recv_socket.connect("tcp://127.0.0.1:"+str(recv_port))
    
    send_socket = context.socket(zmq.PUSH)
    send_socket.connect("tcp://127.0.0.1:"+str(send_port))

    while True: 
        img = recv_socket.recv_pyobj()
        contours = cv2.findContours(img, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
        send_socket.send_pyobj(contours)
