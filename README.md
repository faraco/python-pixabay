[![Build Status](https://travis-ci.org/momozor/python-pixabay.svg?branch=master)](https://travis-ci.org/momozor/python-pixabay)
[![PyPI version](https://badge.fury.io/py/python-pixabay.svg)](https://badge.fury.io/py/python-pixabay)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-pixabay.svg?color=1&label=Python)
### python-pixabay
Python 3 Pixabay's API wrapper.

### Install from PyPi
`pip install python-pixabay`

### Synopsis

```python
from pixabay import Image, Video

API_KEY = 'my_pixabay_api_key'

# image operations
image = Image(API_KEY)

# default image search
image.search()

# custom image search
ims = image.search(q='cats dogs',
             lang='es',
             image_type='photo',
             orientation='horizontal',
             category='animals',
             safesearch='true',
             order='latest',
             page=2,
             per_page=3)

print(ims)

# video operations
video = Video(API_KEY)

# default video search
video.search()

# custom video search
vis = video.search(q='cats', lang='fr',
                       video_type='animation',
                       category='animals',
                       page=1,
                       per_page=4)

print(vis)
```

### How do I use it?

I wrote a few _how to_ articles in the [project wiki](https://github.com/momozor/python-pixabay/wiki). Feel free to add more examples or scenarios to the wiki.

### Running the tests

* Make sure you've assigned the `PIXABAY_API_KEY` environment variable with your
registered Pixabay's api key.
* Run the following command `pytest` in the project directory.

### Changelog

### v2.6

* remove old rst documentations

#### v2.5

* remove slumber to use custom payload
* updated documentation to use just docstrings
* updated README.md doc
* make bool types to accept "true" or "false" to
imitate the Pixabay's API argument type

#### v2.4

* use slumber
* use default request module that was shipped with
user's installed python installation
* add more explicit metadatas to setup.py
* add basic rst doc to pixabay.api

### See Also
* [python-pixabay's Documentation](https://momozor.github.io/python-pixabay/index.html)
* [Pixabay's API Documentation](https://pixabay.com/api/docs)

### License

This module is licensed under the MIT license. See LICENSE file for more details.

### Author

* Momozor <skelic3@gmail.com>
