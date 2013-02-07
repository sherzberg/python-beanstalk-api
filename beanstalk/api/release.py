from .base import Base

class Release(Base):
    def __get__(self, repository_id=None, release_id=None):
        if repository_id is None:
            url = 'releases.json'
        elif release_id is None:
            url = str(repository_id) + '/releases.json'
        else:
            url = str(repository_id) + '/releases/' + str(release_id) + '.json'
        return self._do_get(url)

    def find_all(self):
        return self.__get__()

    def find_from_repo(self, repository_id):
        return self.__get__(repository_id=repository_id)

    def get_release(self, repository_id, release_id):
        return self.__get__(repository_id=repository_id, release_id=release_id)

    def deploy(self, repository_id, environment_id, message, revision):
        url = str(repository_id) + '/releases.json?environment_id=' + str(environment_id)
        data = {
            'release': {
                'comment': message,
                'revision': str(revision)
            }
        }
        self._do_post(url, data)
    
