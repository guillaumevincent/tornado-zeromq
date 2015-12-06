import zmq

import json

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.setsockopt(zmq.SUBSCRIBE, b'GetIndex')
subscriber.connect("tcp://127.0.0.1:5555")

while True:
    [event, contents] = subscriber.recv_multipart()
    message = json.loads(contents.decode('utf-8'))
    print('Event: %s' % event)
    print('Message: %s' % message)
