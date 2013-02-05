from .base import Base

class Environment(Base):
    
    def find(self, repository_id, environment_id=None):
        if environment_id:
            url = str(repository_id) + '/server_environments/' + str(environment_id) + '.json'
        else:
            url = str(repository_id) + '/server_environments.json'
        return self._do_get(url)

    def find_all(self, repository_id):
        return self.find(repository_id)

    def create(self, repository_id, name, branch_name, automatic=False):
        url = str(repository_id) + '/server_environments.json'
        data = {
            'server_environment': {
                "name": name, 
                "automatic": automatic,
                "branch_name": branch_name
            }
        }
        return self._do_post(url, data)

    def update(self, repository_id, environment_id, update_data):
        url = str(repository_id) + '/server_environments/' + str(environment_id) + '.json'
        data = {
                'server_environment' : update_data
        }
        return self._do_put(url, data)
