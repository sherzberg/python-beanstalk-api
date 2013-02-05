.. image:: https://travis-ci.org/whelmingbytes/python-beanstalk-api.png?branch=master

Python Beanstalk API
====================

This is an implementation of the Beanstalk VCS API in Python.

This api will allow you to manage your beanstalk vcs. All requests are made with simple json. The results for api requests are turned into simple dictionaries for maximum flexibility.

Legal:
======

Python Beanstalk API is provided under the GPL v3. The LICENSE.txt file is a copy of the license for your review.

Prerequisites:
==============

1. A Beanstalk App user with api turned on.
   a) see http://support.beanstalkapp.com/customer/portal/articles/68111-how-can-i-enable-the-beanstalk-api)
2. Python 2.7 or up
3. Requests
   b) http://python-requests.org)

Example Usage:
==============

::

    import beanstalk

    beanstalk.setup('DOMAIN', 'USERNAME', 'PASSWORD')

    print('All users:')
    users = beanstalk.api.user.find()
    for user in users:
    print('\t'+user['user']['first_name']+' '+user['user']['last_name'])

    print('All repositories:')
    for repo in beanstalk.api.repository.find():
    print('\t'+str(repo['repository']['id'])+' '+repo['repository']['name'])

    print('All public keys:')
    for key in beanstalk.api.publickey.find():
    print '\t'+str(key['public_key']['user_id'])+' '+str(key['public_key']['name'])

    print('Permissions for user:')
    for permission in beanstalk.api.permission.find(227736):

    print '\t'+str(permission['permission']['user_id'])+' '+str(permission['permission'])
