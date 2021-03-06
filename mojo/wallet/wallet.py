# -*- coding: utf-8 -*-
from tornado.gen import coroutine
import rethinkdb as r


@coroutine
def deposit(conn, username, funds):
    data = yield r.table('users').get(username).run(conn)
    if data is None:
        oldfunds = 0
    else:
        oldfunds = data.get('funds', 0)
    newfunds = oldfunds + funds
    yield r.table('users').get(username).update({
            'funds': newfunds
        }).run(conn)


@coroutine
def withdraw(conn, username, funds):
    """Returns True if withdrawal goes through, False if not."""
    data = yield r.table('users').get(username).run(conn)
    if data is None:
        oldfunds = 0
    else:
        oldfunds = data.get('funds', 0)
    if oldfunds > funds:
        return False
    else:
        newfunds = oldfunds - funds
        yield r.table('users').get(username).update({
                'funds': newfunds
            }).run(conn)
        return True


@coroutine
def get_funds(conn, username):
    data = yield r.table('users').get(username).run(conn)
    if data is None:
        return 0
    else:
        return data.get('funds', 0)
