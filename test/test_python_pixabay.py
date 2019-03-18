from unittest import TestCase
from pixabay import Image, Video
import os

api_key = os.getenv('PIXABAY_API_KEY')
image = Image(api_key)
video = Video(api_key)


class TestPythonPixabay(TestCase):
    def test_image_search(self):
        self.assertEqual(image.search()["totalHits"], 500)

    def test_video_search(self):
        self.assertIn("hits", video.search())

    def test_custom_image_search(self):
        self.assertIn("hits", image.search(q="water", page=1, safesearch=True))
        self.assertEqual(image.search(q="apple", page=1)["hits"][0]["pageURL"],
         "https://pixabay.com/photos/apple-red-delicious-fruit-256261/")

    def test_custom_video_search(self):
        self.assertEqual(video.search(q="apple", page=1)["hits"][0]["pageURL"],
         "https://pixabay.com/videos/id-1019/")
