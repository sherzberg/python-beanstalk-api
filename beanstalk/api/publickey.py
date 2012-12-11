
from .base import Base

class PublicKey(Base):
    
    def find(self, id=None, user_id=None):
        if user_id:
            url = 'public_keys.json?user_id={0}'.format(user_id)
        elif id:
            url = 'public_keys/{0}.json'.format(id)
        else:
            url = 'public_keys.json'
        
        return self._do_get(url)
    
    def create(self, content, name=None, user_id=None):
        url = 'public_keys.json'
        data = {
                'public_key':{
                    'content': content
                    }
                }
        if name:
            data['public_key']['name'] = name
        
        return self._do_post(url, data)