# -*- coding: utf-8 -*-
from mojo.db import get_db_conn
from tornado.gen import coroutine
import rethinkdb as r


@coroutine
def deposit(username, funds):
    conn = yield get_db_conn()
    data = yield r.table('wallet').get(username).run(conn)
    oldfunds = data.get('funds', 0)
    newfunds = oldfunds + funds
    yield r.table('wallet').get(username).update({
            'funds': newfunds
        }).run(conn)


@coroutine
def withdraw(username, funds):
    """Returns True if withdrawal goes through, False if not."""
    conn = yield get_db_conn()
    data = yield r.table('wallet').get(username).run(conn)
    oldfunds = data.get('funds', 0)
    if oldfunds > funds:
        return False
    else:
        newfunds = oldfunds - funds
        yield r.table('wallet').get(username).update({
                'funds': newfunds
            }).run(conn)
        return True


@coroutine
def get_funds(username):
    conn = yield get_db_conn()
    data = yield r.table('wallet').get(username).run(conn)
    return data.get('funds')
