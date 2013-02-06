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

   a. see http://support.beanstalkapp.com/customer/portal/articles/68111-how-can-i-enable-the-beanstalk-api)
2. Python 2.6, 2.7, or 3.2 (tox and travis-ci configuration are available)

Installation:
=============

::

    git clone git@github.com:whelmingbytes/python-beanstalk-api.git
    cd python-beanstalk-api
    pip install .

Example Usage:
==============

::

    import beanstalk

    beanstalk.setup('DOMAIN', 'USERNAME', 'PASSWORD')

    print('All users:')
    users = beanstalk.api.user.find()
    print users
