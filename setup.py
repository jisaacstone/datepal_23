try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple utitlity for finding nearest palindromic date',
    'author': 'jisaacstone',
    'author_email': 'jisaacstone@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['datepal'],
    'scripts': [],
    'name': 'datepal',
    'test_suite': 'tests',
    'classifiers': [
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
}

setup(**config)
