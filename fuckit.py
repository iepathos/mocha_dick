#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.ioloop import IOLoop
from mojo.core import make_love_child
from mojo.db import setup_tables

def fuckit_makemoney():
    seadog = make_love_child()
    seadog.listen(8888)
    IOLoop.current().start()


if __name__ == '__main__':
    setup_tables()
    fuckit_makemoney()
