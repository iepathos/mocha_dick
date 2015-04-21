# -*- coding: utf-8 -*-

from tornado.gen import coroutine
from mojo.util import template, error_404
from mojo.handlers import BaseHandler
from tornado.web import authenticated
from mojo.csgo.matches import add_match, update_score, get_match, toggle_match_live


class MakeMatchHandler(BaseHandler):

    @authenticated
    def get(self):
        error = ''
        self.render(template('make_match.html'), error=error)

    @authenticated
    @coroutine
    def post(self):
        # TODO: admin check make new match
        name = self.get_argument('name')
        teama = self.get_argument('teama')
        teamb = self.get_argument('teamb')
        start = self.get_argument('start')
        rdb = yield add_match(self.db, name, teama, teamb, start)
        if rdb.get('first_error') is None:
            self.redirect('/run/match/%s' % name)
        else:
            error = rdb.get('first_error')
            self.render(template('make_match.html'), error=error)


class RunMatchHandler(BaseHandler):

    @authenticated
    @coroutine
    def get(self, name):
        match = yield get_match(self.db, name)
        if match is None or len(match) == 0:
            error_404(self)
        self.render(template('run_match.html'), match=match)

    @authenticated
    @coroutine
    def post(self):
        name = self.get_argument('name')
        score = self.get_argument('score')
        rdb = yield update_score(self.db, name, score)


class LiveMatchHandler(BaseHandler):

    @authenticated
    @coroutine
    def post(self):
        name = self.get_argument('name')
        yield toggle_match_live(self.db, name)
        self.redirect('/run/match/%s' % name)


class ListMatchesHandler(BaseHandler):

    @authenticated
    def get(self):
        pass
