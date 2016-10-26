import json
import logging
import unittest
import requests
from insights.config import Settings
from insights.configs import log_settings

LOGGER = logging.getLogger('insights')

class UserInfoAPI(unittest.TestCase):
    def setup_class(self):
	log_settings.configure()
        self.setting = Settings()
        self.session = requests.session()
        self.session.cert = self.setting.get_certs()
        self.session.verify = False
        self.base_url = self.setting.get('api', 'url')

    def test_current_user_info(self):
        """ Request current user information
        """
        self.user_info = self.session.get(self.base_url + '/me')
        LOGGER.info(self.user_info.json())
        assert self.user_info.status_code == 200
        self.text = self.user_info.text
        response = json.loads(self.text)
        account_number = response['account_number']
        assert account_number == str(477931)

    def test_product_used_by_account(self):
        """ Test products used by this current user
        """
        self.product = self.session.get(self.base_url+'/v1/account/products')
        LOGGER.info(self.product.json())
        assert self.product.status_code == 200
        product_info = json.loads(self.product.text)
        product_used = product_info[0]
        assert product_used == 'rhel'
