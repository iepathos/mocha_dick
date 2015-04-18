# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, 'mojo')
TEMPLATES_DIR = os.path.join(APP_DIR, 'templates')
STATIC_DIR = os.path.join(APP_DIR, "static")

RETHINK_HOST = 'localhost'
RETHINK_PORT = 28015

settings = {
    'template_path': TEMPLATES_DIR,
    'static_path': STATIC_DIR,
    'auto_reload': True,
    'debug': True,
    'static_path': STATIC_DIR,
    'xsrf_cookies': True,
    'cookie_secret': 'The rubber bands all point northward',
    'serve_traceback': True,
    'login_url': '/login/'
}
