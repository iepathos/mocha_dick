from tornado.web import RequestHandler, authenticated
from mojo.util import template


class BaseHandler(RequestHandler):

    def get_current_user(self):
        username = self.get_secure_cookie("user")
        if username:
            return username[1:-1]
        return None


class HomeHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render(template('home.html'), user=self.get_current_user())
    