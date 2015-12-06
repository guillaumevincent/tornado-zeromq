import zmq

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://127.0.0.1:5557")

publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:5556")

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
        publication = '%s' %message['name']
        publisher.send(publication.encode('utf-8'))
