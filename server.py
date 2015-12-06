import zmq
import tornado.web
import tornado.ioloop

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://127.0.0.1:4444")


class GetIndex(tornado.web.RequestHandler):
    def get(self):
        sender.send_json({'event': 'GetIndex'})
        self.write("Index")


class CreateUser(tornado.web.RequestHandler):
    def get(self):
        sender.send_json({'event': 'CreateUser', 'email': 'guillaume@oslab.fr'})
        self.write("CreateUser")


def make_app():
    return tornado.web.Application([
        (r"/", GetIndex),
        (r"/create_user/", CreateUser),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
