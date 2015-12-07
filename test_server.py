import json

import zmq

import time

import random

context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.identity = b'frontend'
socket.connect('tcp://127.0.0.1:4444')


while True:
    message = random.choice([{'event': 'CreateUser'}, {'event': 'GetIndex'},{'event': 'GetIndex'}, {'event': 'GetIndex'}])
    socket.send(json.dumps(message).encode('utf-8'))
    print(message)
    time.sleep(1)
