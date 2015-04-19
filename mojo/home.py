from mojo.handlers import BaseHandler, BaseWebSocketHandler
from mojo.util import template
from tornado.web import authenticated
from mojo.wallet.wallet import get_funds
from tornado.gen import coroutine
from mojo.db import LISTENERS
import json


class HomeHandler(BaseHandler):

    @authenticated
    @coroutine
    def get(self):
        user = self.get_current_user()
        funds = yield get_funds(self.db, user)
        self.render(template('home.html'),
                    user=self.get_current_user(),
                    funds=funds)


class DataSyncHandler(BaseWebSocketHandler):

    @coroutine
    def open(self):
        LISTENERS.append(self)

    def on_message(self, message):
        self.write_message(json.dumps(message))

    def on_close(self):
        LISTENERS.remove(self)
