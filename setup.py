#!/usr/bin/env python

from setuptools import setup, find_packages

app_name = 'beanstalk-api'
authors = 'Spencer Herzberg'
author_email = 'spencer.herzberg@gmail.com'
version = '1b'
release = version
description = 'This is an implementation of the Beanstalk VCS API in Python'
long_description = '''This api will allow you to manage your beanstalk vcs.
All requests are made with simple json. The results for api requests are
turned into simple dictionaries for maximum flexibility.'''
url = 'https://github.com/whelmingbytes/python-beanstalk-api'

setup(
    name=app_name,
    version=version,
    packages=find_packages(),
    include_package_data=True,
    author=authors,
    author_email=author_email,
    description=description,
    long_description=long_description,
    license="GPL",
    keywords="vcs beanstalk",
    classifiers=[
        'Development Status :: 1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    url=url,
    download_url=url,
)
