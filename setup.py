# -*- coding: utf-8 -*-
import os
from distutils.core import setup
import typograf_model

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-typograf-model',
    version=typograf_model.__version__,
    packages=['typograf_model'],
    url='https://github.com/akadan47/django-typograf-model',
    license='MIT',
    author='Denis Popov',
    author_email='akadan47@gmail.com',
    description='Processing django model fields with ALS typograf',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.3',
    ],
)