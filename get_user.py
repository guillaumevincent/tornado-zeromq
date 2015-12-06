import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b'')
socket.connect("tcp://127.0.0.1:5556")

while True:
    print('waiting...')
    message = socket.recv()
    print('received:', message)
