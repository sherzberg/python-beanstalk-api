
from .base import Base

class Permission(Base):
    
    def find(self,user_id=None):
        url = 'permissions/{0}.json'.format(user_id)
        
        return self._do_request(url, method='get')
    
    def create(self, user_id=None, repository_id=None, read=None, write=None, server_environment=None):
        url = 'permissions.json'
        data = {
                'permission':{}
                }
        if user_id:
            data['permission']['user_id'] = user_id
        if repository_id:
            data['permission']['repository_id'] = repository_id
        if read:
            data['permission']['read'] = read
        if write:
            data['permission']['write'] = write
        if server_environment:
            data['permission']['server_environment'] = server_environment
        
        return self._do_request(url, method='post', data=data)