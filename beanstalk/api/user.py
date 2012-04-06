
from base import Base

class User(Base):
    
    def find(self, user_id=None):
        if user_id:
            url = 'users/{0}.json'.format(user_id)
        else:
            url = 'users.json'
            
        return self._do_request(url)
    
    def create(self, login, email, first_name, last_name, password):
        url = 'users.json'
        data = {
                'user': {
                               'login': login,
                               'email': email,
                               'first_name': first_name,
                               'last_name': last_name,
                               'password': password
                               }
                }

        return self._do_request(url, data)