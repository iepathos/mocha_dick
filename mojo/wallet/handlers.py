# -*- coding: utf-8 -*-

from tornado.gen import coroutine
from mojo.util import template
from mojo.handlers import BaseHandler


class WalletHandler(BaseHandler):
    # show wallet
    def get(self):
        self.render(template('wallet.html'))

    # deposit funds
    def post(self):
        pass
