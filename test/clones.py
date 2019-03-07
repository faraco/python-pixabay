"""File containing testing structures for Python-Pixabay."""

from abc import ABC, abstractmethod

class IPixabay(ABC):
    """Blank class representation of IPixabay."""

    def __init__(self, api_key):
        pass

    @abstractmethod
    def search(self):
        pass


class Image(IPixabay):
    def search(self):
        """Searches Pixabay for images using defaults."""
        return {
            "hits": [
                {
                    "comments": 197,
                    "downloads": 350405,
                    "favorites": 762,
                    "id": 3063284,
                    "imageHeight": 4000,
                    "imageSize": 3574625,
                    "imageWidth": 6000,
                    "largeImageURL": "https://pixabay.com/get/ea35b70c2afc053ed1584d05fb1d4797e271e7d51fb70c4090f5c07eaeefb3b9d8_1280.jpg",
                    "likes": 898,
                    "pageURL": "https://pixabay.com/photos/rose-flower-petal-floral-noble-3063284/",
                    "previewHeight": 99,
                    "previewURL": "https://cdn.pixabay.com/photo/2018/01/05/16/24/rose-3063284_150.jpg",
                    "previewWidth": 150,
                    "tags": "rose, flower, petal",
                    "type": "photo",
                    "user": "annca",
                    "userImageURL": "https://cdn.pixabay.com/user/2015/11/27/06-58-54-609_250x250.jpg",
                    "user_id": 1564471,
                    "views": 556307,
                    "webformatHeight": 426,
                    "webformatURL": "https://pixabay.com/get/ea35b70c2afc053ed1584d05fb1d4797e271e7d51fb70c4090f5c07eaeefb3b9d8_640.jpg",
                    "webformatWidth": 640,
                }
            ],
            "total": 18404,
            "totalHits": 500,
        }


class Video(IPixabay):
    def search(self):
        """Searches Pixabay for videos using defaults."""
        return {
            "hits": [
                {
                    "comments": 24,
                    "downloads": 10095,
                    "duration": 23,
                    "favorites": 59,
                    "id": 2719,
                    "likes": 95,
                    "pageURL": "https://pixabay.com/videos/id-2719/",
                    "picture_id": "563977619",
                    "tags": "dandelion, flowers, yellow",
                    "type": "film",
                    "user": "FMFA",
                    "userImageURL": "https://cdn.pixabay.com/user/2016/05/06/18-47-35-699_250x250.png",
                    "user_id": 1981326,
                    "videos": {
                        "large": {
                            "height": 1080,
                            "size": 13392449,
                            "url": "https://player.vimeo.com/external/161687568.hd.mp4?s=eff398051a1dd6ceaa16b85538940b07cebede70&profile_id=119",
                            "width": 1920,
                        },
                        "medium": {
                            "height": 720,
                            "size": 7770061,
                            "url": "https://player.vimeo.com/external/161687568.hd.mp4?s=eff398051a1dd6ceaa16b85538940b07cebede70&profile_id=174",
                            "width": 1280,
                        },
                        "small": {
                            "height": 540,
                            "size": 4940642,
                            "url": "https://player.vimeo.com/external/161687568.sd.mp4?s=4feca1b7112229c1ef975f13575a65a0bfe93767&profile_id=165",
                            "width": 960,
                        },
                        "tiny": {
                            "height": 360,
                            "size": 1769296,
                            "url": "https://player.vimeo.com/external/161687568.sd.mp4?s=4feca1b7112229c1ef975f13575a65a0bfe93767&profile_id=164",
                            "width": 640,
                        },
                    },
                    "views": 22743,
                }
            ],
            "total": 64,
            "totalHits": 64,
        }
