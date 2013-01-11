#!/usr/bin/env python

import os, sys
import beanstalk

domain = os.environ.get('BEANSTALK_DOMAIN')
username = os.environ.get('BEANSTALK_USERNAME')
password = os.environ.get('BEANSTALK_PASSWORD')

if not domain or not username or not password:

    print()
    print('Your environment variables are not setup properly!')
    print('Please setup BEANSTALK_DOMAIN, BEANSTALK_USERNAME, and')
    print('BEANSTALK_PASSWORD as environment variables')
    print()
    sys.exit()

beanstalk.setup(domain, username, password)

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
