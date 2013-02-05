import unittest
from mock import patch
from mock import Mock
from beanstalk.api import base
import json
import requests


class TestBeanstalkAuth(unittest.TestCase):

    def tearDown(self):
        base.BeanstalkAuth._instance = None

    def test_get_api_url(self):
        domain = 'testdomain'
        username = 'user'
        password = 'secret'

        auth = base.BeanstalkAuth(domain, username, password)

        self.assertEquals(domain, auth.domain)
        self.assertEquals(username, auth.username)
        self.assertEquals(password, auth.password)
        self.assertEquals('https://testdomain.beanstalkapp.com/api/', auth.api_url)

    def test_get_instance_no_setup(self):

        get_instance = base.BeanstalkAuth.get_instance

        self.assertRaises(base.IncorrectSetupException, get_instance)

    def test_get_instance(self):

        auth = base.BeanstalkAuth('d', 'u', 'p')

        result_auth = base.BeanstalkAuth.get_instance()

        self.assertEquals(auth, result_auth)


class TestBase(unittest.TestCase):

    @patch('requests.get')
    def test_do_request(self, mock_method):
        request_mock = Mock()
        request_mock.json.return_value = {}
        mock_method.return_value = request_mock
        domain = 'domain'
        username = 'username'
        password = 'password'

        base.BeanstalkAuth(domain, username, password)
        apiurl = base.BeanstalkAuth.get_instance().api_url
        b = base.Base()

        jsonResult = b._do_request('endpoint', 'get', None)

        mock_method.assert_called_once_with(apiurl + 'endpoint',
                                            data=json.dumps(None),
                                            auth=(username, password),
                                            headers={'content-type': 'application/json'})
        request_mock.raise_for_status.assert_called_once_with()
        request_mock.json.assert_called_once_with()
        self.assertEquals({}, jsonResult)

    @patch('requests.get')
    def test_do_request_raises_exception(self, mock_method):
        request_result = Mock()
        request_result.raise_for_status.side_effect = requests.exceptions.HTTPError()
        mock_method.return_value = request_result

        base.BeanstalkAuth('', '', '')
        b = base.Base()

        def request_method():
            return b._do_request('', 'get', '')

        self.assertRaises(requests.exceptions.HTTPError, request_method)
