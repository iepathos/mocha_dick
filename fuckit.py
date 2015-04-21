#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.ioloop import IOLoop
from mojo.core import make_love_child
from mojo.db import get_db_conn, setup_tables, rethink_listener
from tornado.gen import coroutine
import threading


@coroutine
def fuckit_makemoney():
    db_conn = yield get_db_conn()
    seadog = make_love_child(db_conn)
    seadog.listen(8888)


@coroutine
def get_hard():
    yield setup_tables()
    print('Starting Rethink Listener')
    threading.Thread(target=rethink_listener).start()


if __name__ == '__main__':
    get_hard()
    IOLoop.current().run_sync(fuckit_makemoney)
    IOLoop.current().start()
