from unittest import TestCase
from pixabay import Image, Video
import os

api_key = os.getenv('PIXABAY_API_KEY')
image = Image(api_key)
video = Video(api_key)


class TestPythonPixabay(TestCase):
    def test_image_search(self):
        self.assertEqual(image.search()["hits"], 500)

    def test_video_search(self):
        self.assertIn("hits", video.search())

    def test_custom_image_search(self):
        self.assertIn("hits", image.search(q="water", page=1))

    def test_custom_video_search(self):
        self.assertIn("hits", video.search(q="water"))
