
import os
import sys
from tornado.testing import AsyncHTTPTestCase

from mojo.config import APP_DIR, TEMPLATES_DIR, STATIC_DIR
sys.path.append(os.path.join(APP_DIR, '..'))

test_settings = {
    'template_path': TEMPLATES_DIR,
    'static_path': STATIC_DIR,
    'auto_reload': True,
    'debug': True,
    'static_path': STATIC_DIR,
    'xsrf_cookies': False,
    'cookie_secret': 'The rubber bands all point northward',
    'serve_traceback': True,
    'login_url': '/login/'
}



from mojo.core import HotWire
app = HotWire(config=test_settings)


class TestSeadogBase(AsyncHTTPTestCase):
    def setUp(self):
        super(TestSeadogBase, self).setUp()

    def get_app(self):
        return app
