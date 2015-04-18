
from tornado.web import RequestHandler, StaticFileHandler, Application
from mojo.config import settings
import tornado.web


class HelloHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")


class Application(Application):

    def __init__(self):
        handlers = [
            (r'/', HelloHandler),
            (r"/(apple-touch-icon\.png)", StaticFileHandler,
             dict(path=settings['static_path'])),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)


def make_app():
    return Application()
