
from .base import Base

class Repository(Base):
    
    def find(self, id=None):
        if id:
            url = 'repositories/{0}.json'.format(id)
        else:
            url = 'repositories.json'
            
        return self._do_request(url)
    
    def create(self, name, title, color_label='label-white', vcs='subversion',  create_structure=False):
        url = 'repositories.json'
        data = {
                'repository': {
                               'name': name,
                               'title': title,
                               'type_id': vcs,
                               'color_label': color_label
                               }
                }

        return self._do_request(url, data)