"""
MIT License

Copyright (c) 2018-2019 momozor (Momo)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from abc import ABC, abstractmethod
from requests import get


class IPixabay(ABC):
    def __init__(self, api_key):

        self.api_key = api_key
        self.root_url = "https://pixabay.com/api/"

    @abstractmethod
    def search(self):
        pass


class Image(IPixabay):
    def search(self,
               q='yellow flower',
               lang='en',
               id='',
               response_group='image_details',
               image_type='all',
               orientation='all',
               category='',
               min_width=0,
               min_height=0,
               editors_choice='false',
               safesearch='false',
               order='popular',
               page=1,
               per_page=20,
               callback='',
               pretty='false'):
        payload = {
            'key': self.api_key,
            'q': q,
            'lang': lang,
            'id': id,
            'response_group': response_group,
            'image_type': image_type,
            'orientation': orientation,
            'category': category,
            'min_width': min_width,
            'min_height': min_height,
            'editors_choice': editors_choice,
            'safesearch': safesearch,
            'order': order,
            'page': page,
            'per_page': per_page,
            'callback': callback,
            'pretty': pretty
        }

        resp = get(self.root_url, params=payload)

        if resp.status_code == 200:
            return resp.json()
        else:
            raise ValueError(resp.text)


class Video(IPixabay):
    def search(self,
               q='yellow flower',
               lang='en',
               id='',
               video_type='all',
               category='',
               min_width=0,
               min_height=0,
               editors_choice='false',
               safesearch='false',
               order='popular',
               page=1,
               per_page=20,
               callback='',
               pretty='false'):

        payload = {
            'key': self.api_key,
            'q': q,
            'lang': lang,
            'id': id,
            'video_type': video_type,
            'category': category,
            'min_width': min_width,
            'min_height': min_height,
            'editors_choice': editors_choice,
            'safesearch': safesearch,
            'order': order,
            'page': page,
            'per_page': per_page,
            'callback': callback,
            'pretty': pretty
        }

        resp = get(self.root_url + "videos/", params=payload)
        if resp.status_code == 200:
            return resp.json()
        else:
            raise ValueError(resp.text)
