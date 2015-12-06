import zmq
import tornado.web
import tornado.ioloop

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5557")


class GetIndex(tornado.web.RequestHandler):
    def get(self):
        socket.send_json({'name': 'GetIndex'})
        self.write("Index")


def make_app():
    return tornado.web.Application([
        (r"/", GetIndex),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
