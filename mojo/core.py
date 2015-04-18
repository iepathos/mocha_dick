
from tornado.web import RequestHandler, Application, url


class HelloHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")


def make_app():
    return Application([
        url(r"/", HelloHandler),
    ])
