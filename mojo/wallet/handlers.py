# -*- coding: utf-8 -*-

from tornado.gen import coroutine
from mojo.util import template
from mojo.handlers import BaseHandler
from mojo.wallet.wallet import deposit
from tornado.web import authenticated


class WalletHandler(BaseHandler):

    @authenticated
    def get(self):
        self.render(template('wallet.html'))

    @authenticated
    @coroutine
    def post(self):
        yield deposit(self.db, self.get_current_user(), 100)
        self.redirect('/')
