import unittest
from insights.config import Settings
from fauxfactory import gen_string
import logging
from insights.session import Session
from insights.configs import log_settings
from insights.utils.util import Util

LOGGER = logging.getLogger('insights_api')


class RegisterationAPITestCase(unittest.TestCase):

    @classmethod
    def setup_class(self):
        self.setting = Settings()
        session_instance = Session()
        log_settings.configure()
        self.session = session_instance.get_session()
        self.base_url = self.setting.get('api', 'url')
        self.system_id  = gen_string('alphanumeric', 10)
        self.hostname = 'hostname_{0}'.format(gen_string('alpha', 12))
        print 'Hostname: {0}, System_id: {1}'.format(self.hostname,
                                                           self.system_id)

    def setup_method(self, method):
        Util.print_testname(type(self).__name__, method)

    def test_register_machine(self):
        """Test if the system is registered"""
        register = self.session.post(self.base_url + '/v1/systems',
                                     data = {'system_id':self.system_id,
                                             'hostname':self.hostname})
        LOGGER.info(register.json())
        assert register.status_code == 201

    def test_unregister_machine(self):
        """Test if the above registered system has been unregistered and not 
        checking in.
        """
        unregister = self.session.delete(self.base_url + '/v1/systems/' +
                                         self.system_id)
        assert unregister.status_code == 204
        check_if_unregistered = self.session.get(self.base_url + '/v1/systems/' +
                                          self.system_id)
        response = check_if_unregistered.json()
        LOGGER.info(response)
        assert response['isCheckingIn'] == False
        assert response['unregistered_at'] is not None
        reports = self.session.get(self.base_url + '/v1/reports?system_id=' +
                                          self.system_id)
        print reports.json()
        print reports.status_code
