from tests.seadog_test import TestSeadogBase
# import urllib


class TestUserRegistration(TestSeadogBase):

    def test_get_unauthenticated_home(self):
        res = self.fetch('/',
                         method='GET',
                         follow_redirects=True)
        self.assertTrue(res.effective_url.endswith('/login/?next=%2F'))
