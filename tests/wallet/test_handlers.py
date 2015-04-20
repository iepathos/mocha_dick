from tests.seadog_test import TestSeadogBase
import urllib


class TestWalletHandlers(TestSeadogBase):

    def test_get_unauthenticated_wallet(self):
        res = self.fetch('/wallet/',
                         method='GET',
                         follow_redirects=True)
        self.assertTrue(res.effective_url.endswith('/login/?next=%2Fwallet%2F'))
