
from tornado.web import StaticFileHandler, Application
from mojo.config import settings
import tornado.web
from mojo.handlers import HomeHandler
from mojo.auth.handlers import AuthLoginHandler, AuthLogoutHandler, RegistrationHandler


class HotWire(Application):

    def __init__(self, config):
        handlers = [
            (r'/', HomeHandler),
            (r'/register/', RegistrationHandler),
            (r'/login/', AuthLoginHandler),
            (r'/logout/', AuthLogoutHandler),
            (r'/(apple-touch-icon\.png)', StaticFileHandler,
             dict(path=config['static_path'])),
        ]
        tornado.web.Application.__init__(self, handlers, **config)


def make_love_child():
    return HotWire(config=settings)
