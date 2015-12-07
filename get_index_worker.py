import zmq

context = zmq.Context()
worker = context.socket(zmq.ROUTER)
worker.identity = b'get-index-worker'
worker.connect("tcp://127.0.0.1:5555")

while True:
    identity, message, id = worker.recv_multipart()
    if message == b'GetIndex':
        print(identity, message, id)

context.destroy(0)
