"""
MIT License

Copyright (c) 2018-2019 Momozor

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
from slumber import API


class IPixabay(ABC):
    """Abstract class for Pixabay"""
    def __init__(self, api_key):
        """
        :param api_key :type str Pixabay's API key.
        See https://pixabay.com/api/docs/ for more details."""
        self.api_key = api_key
        self.api = API("https://pixabay.com/")

    @abstractmethod
    def search(self):
        pass


class Image(IPixabay):
    """This class handles all image operations"""
    def search(
        self,
        q="yellow flower",
        lang="en",
        image_type="all",
        orientation="all",
        category="",
        min_width=0,
        min_height=0,
        editors_choice="false",
        safesearch="false",
        order="popular",
        page=1,
        per_page=20,
        callback="",
        pretty="false"):
        """returns image API data in dict

        Image search
        
        :param q :type str :desc A URL encoded search term. If omitted,
        all images are returned. This value may not exceed 100 characters.
        Example: "yellow+flower"

        :param lang :type str :desc 	Language code of the language to be searched in. 
        Accepted values: cs, da, de, en, es, fr, id, it, hu, nl, no, pl, pt, ro, sk, fi,
        sv, tr, vi, th, bg, ru, el, ja, ko, zh
        Default: "en"
        For more info, see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

        :param image_type :type str :desc Filter results by image type.
        Accepted values: "all", "photo", "illustration", "vector"
        Default: "all"

        :param orientation :type str :desc

        Code Example
        >>> from pixabay import Image
        >>> image = Image("api_key")
        >>> image.search(q="apple", page=1)
        """
        return self.api.api.get(
            key=self.api_key,
            q=q,
            lang=lang,
            image_type=image_type,
            orientation=orientation,
            category=category,
            min_width=min_width,
            min_height=min_height,
            editors_choice=editors_choice,
            safesearch=safesearch,
            order=order,
            page=page,
            per_page=per_page,
            callback=callback,
            pretty=pretty,
        )


class Video(IPixabay):
    def search(
        self,
        q="yellow flower",
        lang="en",
        id="",
        video_type="all",
        category="",
        min_width=0,
        min_height=0,
        editors_choice="false",
        safesearch="false",
        order="popular",
        page=1,
        per_page=20,
        callback="",
        pretty="false",
    ):

        return self.api.api.videos.get(
            key=self.api_key,
            q=q,
            lang=lang,
            id=id,
            video_type=video_type,
            category=category,
            min_width=min_width,
            min_height=min_height,
            editors_choice=editors_choice,
            safesearch=safesearch,
            order=order,
            page=page,
            per_page=per_page,
            callback=callback,
            pretty=pretty,
        )
