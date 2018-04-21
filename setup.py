# coding: utf-8
import os
from setuptools import setup
import bitbutter

README = open(os.path.join(os.path.dirname(__file__), 'PYPIREADME.rst')).read()
REQUIREMENTS = [
    line.strip() for line in open(
        os.path.join(os.path.dirname(__file__), 'requirements.txt')
    ).readlines()
]

setup(
    name='chainbridge',
    version=bitbutter.__version__,
    packages=['bitbutter'],
    include_package_data=True,
    license='MIT',
    description='Bitbutter API client library',
    long_description=README,
    long_description_content_type='text/x-rst',
    url='https://github.com/polyledger/chainbridge/',
    download_url='https://github.com/polyledger/chainbridge/tarball/%s'
        % (bitbutter.__version__),
    keywords=['api', 'bitbutter', 'client'],
    install_requires=REQUIREMENTS,
    author='Matthew Rosendin',
    author_email='matthew@polyledger.com',
    classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
