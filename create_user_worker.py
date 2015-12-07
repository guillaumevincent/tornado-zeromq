import zmq

context = zmq.Context()
worker = context.socket(zmq.DEALER)
worker.identity = b'create-user-worker'
worker.connect("tcp://127.0.0.1:5555")

while True:
    message, id = worker.recv_multipart()
    if message == b'CreateUser':
        print(message, id)

context.destroy(0)
