from .base import Base


class User(Base):
    """This class manages and creates Users

    Readable Attributes:
        id        : (integer) Unique ID of the User.
        account_id: (integer) ID of teh Account user belongs to.
        login     : (string) Username. Unique per Account.
        email     : (string) Email Address. Unique per Account.
        name      : (string) Full Name.
        first_name: (string) First Name.
        last_name : (string) Last Name.
        owner     : (boolean) True if User has created the Account initially.
        admin     : (boolean) True if user has admin privileges in the Account.
        timezone  : (string) User's preferred time zone.
        updated_at: (datetime) Time when the User was last updated.
        created_at: (datetime) Time when the User was first added to the system.

    Writable Attributes:
        login     : (string) Writable only on create. Always required and must be unique.
        email     : (string) Required on create.
        name      : (string) Required on create.
        password  : (string) Required on create.
        admin     : (boolean) Optional.
        timezone  : (string) Optional.
        """

    def find(self, user_id=None):
        """This method finds a specific user by ID"""
        if user_id:
            url = 'users/{0}.json'.format(user_id)
        else:
            url = 'users.json'

        return self._do_get(url)

    def find_all(self, page=None, per_page=30):
        """This method finds all users. This method supports pagination that is disabled
        by default.
        """

        url = 'users.json'

        if page:
            url += '?page={0}&per_page?{1}'.format(page, per_page)

        return self._do_get(url)

    def create(self, login, name, email, password, admin=False, timezone=None):
        """This method will create a User"""

        url = 'users.json'

        data = {
            'user': {
                'login': login,
                'name': name,
                'email': email,
                'password': password
            }
        }

        if admin:
            data['user']['admin'] = True

        if timezone:
            data['user']['timezone'] = timezone

        return self._do_post(url, data)

    def update(self, id, first_name=None, last_name=None, email=None, password=None, admin=None):
        """This method will update a User"""

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

    def delete(self, id):
        """This method will delete a User"""

        url = 'users/{0}.json'.format(id)

        return self._do_delete(url)
