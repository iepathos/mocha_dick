from tests.seadog_test import TestSeadogBase
# import urllib


class TestUserRegistration(TestSeadogBase):

    def test_get_home(self):
        res = self.fetch('/',
                         method='GET',
                         follow_redirects=True)
        self.assertEqual(res.code, 200)
