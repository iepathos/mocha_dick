#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.ioloop import IOLoop
from mojo.core import make_love_child
from mojo.db import get_db_conn, setup_tables, rethink_listener
from tornado import httpserver
from mojo.config import settings
from tornado.gen import coroutine
import threading


@coroutine
def fuckit_makemoney():
    db_conn = yield get_db_conn()
    seadog = make_love_child(db_conn)
    seadog.listen(8888)


if __name__ == '__main__':
    setup_tables()
    threading.Thread(target=rethink_listener).start()
    IOLoop.current().run_sync(fuckit_makemoney)
    IOLoop.current().start()
