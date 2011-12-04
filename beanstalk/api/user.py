
from base import Base

class User(Base):
    
    def find(self, user_id=None):
        if user_id:
            url = 'users/{0}.json'.format(user_id)
        else:
            url = 'users.json'
            
        return self._do_request(url)