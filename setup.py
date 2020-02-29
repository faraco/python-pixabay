from setuptools import setup
from os import path

this_dir = path.abspath(path.dirname(__file__))
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='python-pixabay',
    description='Python 3 Pixabay\'s API wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/momozor/python-pixabay',
    author='momozor',
    author_email='skelic3@gmail.com',
    version='4.2',
    license='MIT',
    py_modules=['pixabay'],
    install_requires=['requests'],
    python_requires='~=3.5',
    keywords='api development pixabay wrapper library python3',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta'
    ])
