from distutils.core import setup

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sacrinasdk'))

long_description="""
Python library for Sacrina API
  """

license='Sacrina Lisence'

url='https://github.com/sacrina/Sacrina-Python/'

setup(
  name='Sacrina-Python',
  version= '0.1',
  author='Sacrina',
  author_email='admin@sacrina.com',
  packages=['sacrinasdk'],
  scripts=[],
  url=url,
  license=license,
  description='',
  long_description='',
  package_data={'sacrinasdk': ['data/*.crt.pem']},
  install_requires=['requests>=1.0.0', 'six>=1.0.0', 'pyopenssl>=0.15'],
  classifiers=[
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  keywords=['sacrina', 'rest', 'sdk']
)
