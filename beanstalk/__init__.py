
from api.base import BeanstalkAuth

def setup(domain, username, password):
    BeanstalkAuth(domain, username, password)
