
from tornado.web import StaticFileHandler, Application
from mojo.config import settings
import tornado.web
from mojo.auth.handlers import AuthLoginHandler, AuthLogoutHandler, RegistrationHandler
from mojo.wallet.handlers import WalletHandler
from mojo.home import HomeHandler, DataSyncHandler
from mojo.admin.handlers import AdminHandler
from mojo.csgo.handlers import MakeMatchHandler, RunMatchHandler, LiveMatchHandler


class HotWire(Application):

    def __init__(self, config, db_conn):
        handlers = [
            (r'/', HomeHandler),
            (r'/register/', RegistrationHandler),
            (r'/login/', AuthLoginHandler),
            (r'/logout/', AuthLogoutHandler),
            (r'/wallet/', WalletHandler),
            (r'/datasync/', DataSyncHandler),
            (r'/admin/', AdminHandler),
            (r'/make/match/', MakeMatchHandler),
            (r'/run/match/(?P<name>[^\/]+)', RunMatchHandler),
            (r'/toggle/match/live/', LiveMatchHandler),
            (r'/(apple-touch-icon\.png)', StaticFileHandler,
             dict(path=config['static_path'])),
        ]
        tornado.web.Application.__init__(self, handlers, **config)

        self.db = db_conn


def make_love_child(db_conn):
    return HotWire(config=settings, db_conn=db_conn)
