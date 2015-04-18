
from tornado.web import RequestHandler
from mojo.util import template


class ListMatchesHandler(RequestHandler):

    def get(self):
        self.render(template('list_live_matches.html'))


class NewWagerHandler(RequestHandler):

    def get(self):
        self.render(template('new_wager.html'))
