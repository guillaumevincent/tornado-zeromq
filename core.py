import zmq

import json

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://127.0.0.1:4444")

publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:5555")

poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)
poller.register(publisher, zmq.POLLIN)

while True:
    try:
        socks = dict(poller.poll())
    except KeyboardInterrupt:
        break

    if receiver in socks:
        message = receiver.recv_json()
        print(message)
        publisher.send_multipart([message['event'].encode('utf-8'), json.dumps(message).encode('utf-8')])
