from .base import Base


class Invitation(Base):

    def find(self, invitation_id):
        url = 'invitations/{0}.json'.format(invitation_id)

        return self._do_get(url)

    def find_all(self):
        url = 'invitations.json'

        return self._do_get(url)

    def create(self, email, first_name, last_name):
        url = 'invitations.json'
        data = {
            "invitation": {
                "user": {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name
                }
            }
        }

        return self._do_post(url, data)

    def resend(self, user_id):
        url = 'invitations/resend/{0}.json'.format(user_id)

        return self._do_get(url)
