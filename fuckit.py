#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.ioloop import IOLoop
from mojo.core import make_app


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
