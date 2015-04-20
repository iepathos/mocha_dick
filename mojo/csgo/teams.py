# -*- coding: utf-8 -*-
from tornado.gen import coroutine
import rethinkdb as r


@coroutine
def add_team(conn, name, player1, player2, player3, player4, player5):
    insert = yield r.table('matches').insert({
            'id': name,
            'player1': player1,
            'player2': player2,
            'player3': player3,
            'player4': player4,
            'player5': player5
        }).run(conn)
    return insert

