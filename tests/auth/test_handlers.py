from tests.seadog_test import TestSeadogBase
import urllib


class TestAuthHandlers(TestSeadogBase):

    def test_get_register(self):
        res = self.fetch('/register/',
                         method='GET',
                         follow_redirects=False)
        self.assertEqual(res.code, 200)

    def test_get_login(self):
        res = self.fetch('/login/',
                         method='GET',
                         follow_redirects=False)
        self.assertEqual(res.code, 200)

    # def test_post_register(self):
    #     post_args = {'username': 'batman', 'password': 'joker'}
    #     res = self.fetch('/register/',
    #                      method='POST',
    #                      body=urllib.parse.urlencode(post_args),
    #                      follow_redirects=True)
    #     self.assertEqual(res.code, 200)
    #     # print(res.headers['Set-Cookie'])
    #     # self.assertTrue(res.headers.get('Path') == '/')
