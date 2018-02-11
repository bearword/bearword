from setuptools import setup, find_packages

VERSION = '0.1.1'

setup(
    version=VERSION,
    name='bearword',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask','zappa','awscli',
        'flask-login',
    ],
)
