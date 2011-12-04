#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup, find_packages
import metadata

app_name = metadata.name
version = metadata.version

setup(
    name = app_name,
    version = version,
    packages = find_packages(),
    include_package_data = True,

    author = metadata.authors,
    author_email = metadata.author_email,
    description = metadata.description,
    long_description = metadata.long_description,
    license = "GPL",
    keywords = "vcs beanstalk",
    classifiers = [
        'Development Status :: 1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
    url = metadata.url,
    download_url = metadata.url,
)
