import zmq

context = zmq.Context()

frontend = context.socket(zmq.ROUTER)
frontend.identity = b'broker'
frontend.bind("tcp://127.0.0.1:4444")

backend = context.socket(zmq.DEALER)
backend.identity = b'broker'
backend.bind("tcp://127.0.0.1:5555")

poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)
poller.register(backend, zmq.POLLIN)

id = 0
while True:
    id += 1
    try:
        sockets = dict(poller.poll())
    except:
        break

    if frontend in sockets:
        event, message = frontend.recv_multipart()
        print('Event %s from %s' % (message.decode('utf-8'), event.decode('utf-8')))
        data = '%s (id: %d)' % (message.decode('utf-8'), id)
        backend.send_multipart([message, str(id).encode('utf-8')])

frontend.close()
backend.close()
context.term()
