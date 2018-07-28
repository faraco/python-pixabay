from setuptools import setup

with open('README.md', 'r') as f:
    ld = f.read()

setup(name='python-pixabay',
      description='Python 2 & 3 Pixabay\'s API wrapper',
      long_description=ld,
      long_description_content_type='text/markdown',
      url ='https://github.com/faraco/python-pixabay',
      author='faraco',
      author_email='skelic3@gmail.com',
      version='1.4',
      license='MIT',
      py_modules=['python_pixabay'],
      install_requires=['requests'],
      keywords='api development pixabay wrapper python2 python3'
)
