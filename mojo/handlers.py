from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
import rethinkdb as r


class BaseHandler(RequestHandler):

    def initialize(self):
        self.db = self.application.db
        self.users = r.table('users')

    def get_current_user(self):
        username = self.get_secure_cookie("user")
        if username:
            return username[1:-1].decode("utf-8")
        return None


class BaseWebSocketHandler(WebSocketHandler):

    def get_current_user(self):
        username = self.get_secure_cookie("user")
        if username:
            return username[1:-1].decode("utf-8")
        return None
