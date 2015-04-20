from tornado.testing import AsyncHTTPTestCase
from tornado.gen import coroutine
import rethinkdb as r
from mojo.config import APP_DIR, TEMPLATES_DIR, STATIC_DIR
from mojo.core import HotWire

test_settings = {
    'template_path': TEMPLATES_DIR,
    'static_path': STATIC_DIR,
    'auto_reload': True,
    'debug': True,
    'xsrf_cookies': False,
    'cookie_secret': 'The rubber bands all point northward',
    'serve_traceback': True,
    'login_url': '/login/'
}


db_conn = r.connect(host='localhost', port=28015, db='test')
app = HotWire(config=test_settings, db_conn=db_conn)


class TestSeadogBase(AsyncHTTPTestCase):

    def setUp(self):
        super(TestSeadogBase, self).setUp()

    def get_app(self):
        return app
