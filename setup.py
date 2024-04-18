from setuptools import setup

setup(
    name='Chopper',
    version='0.1',
    description="A personalized discord server autmation bot",
    author="AcrylicMarlin",
    author_email="50shorty56@gmail.com",
    long_description=open('README.md').read(),
    install_requires = [
        'discord.py == 2.3.2',
        'asqlite @ git+https://www.github.com/Rapptz/asqlite.git',
        'setuptools',
    ],

)