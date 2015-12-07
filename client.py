import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.identity = b'frontend'
socket.connect('tcp://127.0.0.1:4444')

while True:
    event = random.choice([b'CreateUser', b'GetIndex', b'GetIndex', b'GetIndex', b'GetIndex'])
    socket.send(event)
    print('Emit %s event' % event)
    time.sleep(1)
