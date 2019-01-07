from setuptools import setup

with open('README.md', 'r') as f:
    ld = f.read()

setup(
    name='python-pixabay',
    description='Python 3 Pixabay\'s API wrapper',
    long_description=ld,
    long_description_content_type='text/markdown',
    url='https://github.com/momozor/python-pixabay',
    author='momozor',
    author_email='skelic3@gmail.com',
    version='2.0',
    license='MIT',
    py_modules=['pixabay'],
    install_requires=['requests'],
    keywords='api development pixabay wrapper python2 python3')
