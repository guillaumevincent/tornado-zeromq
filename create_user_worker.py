import zmq

context = zmq.Context()
worker = context.socket(zmq.ROUTER)
worker.identity = b'create-user-worker'
worker.connect("tcp://127.0.0.1:5555")

while True:
    identity, message, id = worker.recv_multipart()
    if message == b'CreateUser':
        print(identity, message, id)

context.destroy(0)
