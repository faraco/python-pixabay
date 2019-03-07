from setuptools import setup

with open('README.md', 'r') as fh:
    ld = fh.read()

setup(
    name='python-pixabay',
    description='Python 3 Pixabay\'s API wrapper',
    long_description=ld,
    long_description_content_type='text/markdown',
    url='https://github.com/momozor/python-pixabay',
    author='momozor',
    author_email='skelic3@gmail.com',
    version='2.2',
    license='MIT',
    py_modules=['pixabay'],
    install_requires=['slumber'],
    keywords='api development pixabay wrapper python3',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ])
