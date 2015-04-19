# -*- coding: utf-8 -*-

from tornado.gen import coroutine
from mojo.util import template
from mojo.handlers import BaseHandler
from mojo.wallet.wallet import deposit, get_funds
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


# class WalletFundsHandler(BaseHandler):

#     @authenticated
#     @coroutine
#     def post(self):
#         user = self.get_current_user()
#         # funds = yield get_funds(self.db, user)
#         feed = yield self.users.get(user).changes().run(self.db)
#         while (yield field.fetch_next()):
#             change = yield feed.next()
#             funds = change['new_val']['funds']
#             self.write({'funds': funds})
