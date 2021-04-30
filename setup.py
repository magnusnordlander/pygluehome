from setuptools import setup

setup(
    name = 'pygluehome',
    install_requires=['asyncio', 'aiohttp>=3.7.4', 'iso8601>=0.1.14'],
    version = '0.1.0',
    description = 'A library to communicate with Glue Lock',
    author='Magnus Nordlander',
    url='https://github.com/magnusnordlander/pygluehome/',
)