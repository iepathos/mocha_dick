# -*- coding: utf-8 -*-
import tornado
from tornado.gen import coroutine
from mojo.util import template
from mojo.handlers import BaseHandler
from mojo.auth.user import add_user, verify_user


class AuthLoginHandler(BaseHandler):

    def get(self):
        try:
            error = self.get_argument("error")
        except:
            error = ""
        user = self.get_current_user()
        self.render(template("login.html"),
                    error=error,
                    user=user)

    @coroutine
    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        auth = yield verify_user(username, password)
        if auth:
            self.set_current_user(username)
            self.redirect(self.get_argument("next", u"/"))
        else:
            error = "Login incorrect"
            user = self.get_current_user()
            self.render(template("login.html"),
                        error=error,
                        user=user)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")


class AuthLogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))


class RegistrationHandler(BaseHandler):

    def get(self):
        self.render(template('register.html'), error='')

    @coroutine
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        rdb = yield add_user(username, password)
        if rdb.get('first_error') is None:
            # user added successfully
            # log user in and redirect
            self.set_current_user(username)
            self.redirect('/')
        else:
            error = rdb.get('first_error')
            self.render(template('register.html'), error=error)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")