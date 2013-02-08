from .base import Base


class Invitation(Base):
    """This class manages and creates invitations to the Beanstalk service

    Readable Attribtues:
        id           : (integer) Unique ID of the Invitation.
        account_id   : (integer) ID of the Account Invitation belongs to.
        creator_id   : (integer) ID of the User that created the Invitation.
        creator_name : (string) Name of the User that created the Invitation.
        creator_email: (string) Email address of the User that created the Invitation.
        secure_token : (string) Unique secure key that is used by a signup_url.
        signup_url   : (string) URL that can be used to finalize the invitation.
        updated_at   : (datetime) Time when the Invitation was last updated.
        created_at   : (datetime) Time when the Invitation was first added to the system.

    Writable Attributes:
        email        : (string) Required on create. Must be unique for Account.
        name         : (string) Full name. Required on create.
    """

    def find(self, invitation_id):
        """Find an invitation by invitation id"""

        url = 'invitations/{0}.json'.format(invitation_id)

        return self._do_get(url)

    def find_all(self):
        """Find all invitations"""

        url = 'invitations.json'

        return self._do_get(url)

    def create(self, email, name):
        """This method will create both User and Invitation. A usual
        invitation email with signup link will be delivered to the User
        """

        url = 'invitations.json'
        data = {
            "invitation": {
                "user": {
                    "email": email,
                    "name": name
                }
            }
        }

        return self._do_post(url, data)

    def resend(self, email):
        """This method will resend an invitation to the user's email
        address
        """

        url = 'invitations/resend/{0}.json'.format(email)

        return self._do_get(url)
