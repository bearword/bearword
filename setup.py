from setuptools import setup

setup(
    name='bearword',
    packages=['bearword'],
    include_package_data=True,
    install_requires=[
        'flask','zappa','awscli',
        'flask-blogging',
    ],
)
