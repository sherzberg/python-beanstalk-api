
from base import Base

class Repository(Base):
    
    def find(self, id=None):
        if id:
            url = 'repositories/{0}.json'.format(id)
        else:
            url = 'repositories.json'
            
        return self._do_request(url)