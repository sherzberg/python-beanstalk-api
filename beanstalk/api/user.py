from .base import Base


class User(Base):

    def find(self, user_id=None):
        if user_id:
            url = 'users/{0}.json'.format(user_id)
        else:
            url = 'users.json'

        return self._do_get(url)

    def create(self, login, first_name, last_name, email, password, admin=False):
        url = 'users.json'

        data = {
            'user': {
                'login': login,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password
            }
        }
        if admin:
            data['user']['admin'] = True

        return self._do_post(url, data)

    def update(self, id, first_name=None, last_name=None, email=None, password=None, admin=None):
        url = 'users/{0}.json'.format(id)
        data = {
            'user': {}
        }

        if first_name:
            data['user']['first_name'] = first_name

        if last_name:
            data['user']['last_name'] = last_name

        if email:
            data['user']['email'] = email

        if password:
            data['user']['password'] = password

        if admin is not None:
            data['user']['admin'] = admin

        print(data)

        return self._do_put(url, data=data)
