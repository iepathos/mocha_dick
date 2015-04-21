# -*- coding: utf-8 -*-
from tornado.gen import coroutine
from mojo.handlers import BaseHandler
from mojo.util import template
from tornado.web import authenticated


class AdminHandler(BaseHandler):

    @authenticated
    def get(self):
        self.render(template('admin.html'))
