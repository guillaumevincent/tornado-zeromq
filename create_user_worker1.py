import zmq
import json

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.setsockopt(zmq.SUBSCRIBE, b'CreateUser')
subscriber.connect("tcp://127.0.0.1:5555")

frontend = context.socket(zmq.DEALER)
frontend.connect("tcp://127.0.0.1:4444")

poll = zmq.Poller()
poll.register(frontend, zmq.POLLIN)
poll.register(subscriber,  zmq.POLLIN)

while True:
    print('worker 1 ready...')
    sockets = dict(poll.poll())
    if subscriber in sockets:
        [event, contents] = subscriber.recv_multipart()
        message = json.loads(contents.decode('utf-8'))
        print('Event: %s' % event)
        print('Message: %s' % message)
        frontend.send(json.dumps({'event': 'UserCreated'}).encode('utf-8'))
