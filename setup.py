import os
from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

PACKAGE_NAME = 'pyntensiswmp'
HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = '0.0.1'

PACKAGES = find_packages(exclude=['tests', 'tests.*', 'dist', 'build'])

REQUIRES = []

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    license='MIT License',
    url='https://github.com/pascalhahn/pyntensiswmp',
    download_url='https://github.com/pascalhahn/pyntensiswmp/archive/'+VERSION+".tar.tar.gz",
    author='Pascal Hahn',
    author_email='ph@lxd.bz',
    description='Intensis WMP Connector',
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=REQUIRES,
    keywords=['wmp', 'intensis', 'smarthome'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Home Automation'
    ],
)
