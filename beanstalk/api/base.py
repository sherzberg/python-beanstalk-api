import requests
import json


class IncorrectSetupException(Exception):

    pass


class BeanstalkAuth(object):
    _instance = None

    def __new__(cls, domain, username, password):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, domain, username, password):
        self.domain = domain
        self.username = username
        self.password = password
        self.api_url = 'https://{0}.beanstalkapp.com/api/'.format(self.domain)

    @staticmethod
    def get_instance():
        if BeanstalkAuth._instance:
            return BeanstalkAuth._instance
        else:
            raise IncorrectSetupException("You need to run beanstalk.setup first!")


class Base():

    def _do_request(self, url, method, data):
        auth = BeanstalkAuth.get_instance()
        request_url = auth.api_url + url

        r = getattr(requests, method)(request_url,
                                      data=json.dumps(data),
                                      auth=(auth.username, auth.password),
                                      headers={'content-type': 'application/json'})
        r.raise_for_status()
        return r.json()

    def _do_get(self, url):
        return self._do_request(url, 'get', None)

    def _do_post(self, url, data):
        return self._do_request(url, 'post', data)

    def _do_put(self, url, data):
        return self._do_request(url, 'put', data)

    def _do_delete(self, url, data):
        return self._do_request(url, 'delete', data)
