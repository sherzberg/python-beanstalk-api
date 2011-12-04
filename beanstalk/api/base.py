import urllib, urllib2, base64, json

class BeanstalkAuth(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BeanstalkAuth, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self, domain, username, password):
        self.domain = domain
        self.username = username
        self.password = password
        self.api_url = 'http://{0}.beanstalkapp.com/api/'.format(self.domain)
    
    @staticmethod
    def get_instance():
        if BeanstalkAuth._instance:
            return BeanstalkAuth._instance
        else:
            raise Exception("You need to setup this class first!")






class Base():
    
    def _do_request(self, url, data=None):
        auth = BeanstalkAuth.get_instance()
        request_url = auth.api_url+url
           
        if data:
            data_json = json.dumps(data)
            request = urllib2.Request(request_url, data_json, {'content-type': 'application/json'})
        else:
            request = urllib2.Request(request_url)
            
        base64string = base64.encodestring('%s:%s' % (auth.username, auth.password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        
        try:
            result = urllib2.urlopen(request)
        except Exception as e:
            print e
            return None

        return json.loads(result.read())
        