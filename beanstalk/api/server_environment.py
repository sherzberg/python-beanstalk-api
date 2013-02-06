from .base import Base

class ServerEnvironment(Base):
    def __get__(self, repository_id, server_environment_id=None):
        #GET /api/{REPOSITORY_ID}/server_environments.json
        #GET /api/{REPOSITORY_ID}/server_environments/{SERVER_ENVIRONMENT_ID}.json
        if server_environment_id is None:
            url = str(repository_id) + '/server_environments.json'
        else:
            url = str(repository_id) + '/server_environments/' + str(server_environment_id) + '.json'
        return self._do_get(url)

    def find_from_repo(self, repository_id):
        return self.__get__(repository_id=repository_id)

    def get_server_environment(self, repository_id, server_environment_id):
        return self.__get__(repository_id=repository_id, server_environment_id=server_environment_id)
