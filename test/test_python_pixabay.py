from unittest import TestCase
from pixabay import Image, Video
import os

api_key = os.environ["PIXABAY_KEY"]
image = Image(api_key)
video = Video(api_key)


class pixabay_testcase(TestCase):
    def test_image_search(self):
        self.assertIn("hits", image.search())

    def test_video_search(self):
        self.assertIn("hits", video.search())

    def test_custom_image_search(self):
        self.assertIn("hits", image.search(q="water", page=30))

    def test_custom_video_search(self):
        self.assertIn("hits", video.search(q="water"))
