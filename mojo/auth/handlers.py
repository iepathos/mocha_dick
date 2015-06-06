# -*- coding: utf-8 -*-
import tornado
from tornado.gen import coroutine
from mojo.util import template, verify_key, WRONG_KEY
from mojo.handlers import BaseHandler
from mojo.auth.user import add_user, verify_user


class AuthBaseHandler(BaseHandler):

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")


class AuthLoginHandler(AuthBaseHandler):

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
        email = self.get_argument("email", "")
        password = self.get_argument("password", "")
        auth = yield verify_user(self.db, email, password)
        if auth:
            self.set_current_user(email)
            self.redirect(self.get_argument("next", u"/"))
        else:
            error = "Login incorrect"
            user = self.get_current_user()
            self.render(template("login.html"),
                        error=error,
                        user=user)


class APIBaseHandler(AuthBaseHandler):
    def check_xsrf_cookie(self):
        pass


class APILoginHandler(APIBaseHandler):

    @coroutine
    def post(self):
        email = self.get_argument("email", "")
        password = self.get_argument("password", "")
        key = self.get_argument("key", "")
        if verify_key(key):
            auth = yield verify_user(self.db, email, password)
            if auth:
                self.set_current_user(email)
                r = {
                    'status_code': 200,
                }
            else:
                r = {
                    'error': 'Email and password did not authenticate.',
                    'status_code': 401,
                }
        else:
            r = WRONG_KEY
        self.write(r)


class APIRegistrationHandler(APIBaseHandler):

    @coroutine
    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        key = self.get_argument("key", "")
        if verify_key(key):
            rdb = yield add_user(self.db, email, password)
            if rdb.get('first_error') is None:
                # user added successfully
                # log user in and redirect
                self.set_current_user(email)
                r = {
                    'status_code': 201,
                }
            else:
                # error = rdb.get('first_error')
                error = 'Error adding user to database.'
                r = {
                    'error': error,
                    'status_code': 500,
                }
        else:
            r = WRONG_KEY
        self.write(r)


class AuthLogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))


class RegistrationHandler(AuthBaseHandler):

    def get(self):
        self.render(template('register.html'), error='')

    @coroutine
    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        rdb = yield add_user(self.db, email, password)
        if rdb.get('first_error') is None:
            # user added successfully
            # log user in and redirect
            self.set_current_user(email)
            self.redirect('/')
        else:
            # error = rdb.get('first_error')
            error = 'Error adding user to database.'
            self.render(template('register.html'), error=error)
