
from .base import Base

class Repository(Base):
    
    def find(self, id=None):
        if id:
            url = 'repositories/{0}.json'.format(id)
        else:
            url = 'repositories.json'
            
        return self._do_get(url)

    def find_by_name(self, repository_name):
        repos = self.find()
        for repo in repos:
            if repo['repository']['name'] == repository_name:
                return repo
        return None

    def get_id_by_name(self, repository_name):
        repo = self.find_by_name(repository_name)
        if repo is not None:
            return repo['repository']['id']
    
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

        return self._do_post(url, data)
