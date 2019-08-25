[![Build Status](https://travis-ci.org/momozor/python-pixabay.svg?branch=master)](https://travis-ci.org/momozor/python-pixabay)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a6b8c0af5d064875a79b9fd30e89e003)](https://www.codacy.com/app/momozor/python-pixabay?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=momozor/python-pixabay&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/a6b8c0af5d064875a79b9fd30e89e003)](https://www.codacy.com/app/momozor/python-pixabay?utm_source=github.com&utm_medium=referral&utm_content=momozor/python-pixabay&utm_campaign=Badge_Coverage)
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

### Usage

I wrote a few _how to_ articles in the [project wiki](https://github.com/momozor/python-pixabay/wiki). Feel free to add more examples or scenarios to the wiki.

### Running the tests

*   Make sure you've assigned the `PIXABAY_API_KEY` environment variable with your
registered Pixabay's api key.

*   Run the following command `pytest` in the project directory.

### Maintainer and Contributors

*   This software is authored and maintained by [Momozor](https://github.com/momozor).

*   For contributors that contributed to this development of this software, see the
CONTRIBUTORS file.

### Changelog

#### 4.0

* add version 1.4 API as backward compatibility feature.

#### 3.0

*   update urllib3 in Pipfile.lock to fix vulnerability bug.

#### 2.9

*   minor readme changes

#### 2.8

*   minor doc changes

#### v2.7

*   requires requests again in case it is not supported

#### v2.6

*   remove old rst documentations

### See Also
*   [python-pixabay's Documentation](https://momozor.github.io/python-pixabay/index.html)
*   [Pixabay's API Documentation](https://pixabay.com/api/docs)

### License

This module is licensed under the MIT license. See LICENSE file for more details.
