from unittest import TestCase
from pixabay import Image, Video
import os

api_key = os.getenv('PIXABAY_API_KEY')
image = Image(api_key)
video = Video(api_key)


class TestPythonPixabay(TestCase):
    def test_custom_image_search(self):
        self.assertIn(
            "hits",
            image.search(q="water",
                         page=1,
                         safesearch="true",
                         editors_choice="true"))
        self.assertEqual(
            image.search(q="apple", page=1)["hits"][0]["pageURL"],
            "https://pixabay.com/photos/apples-fruit-red-juicy-ripe-634572/"
        )
        self.assertEqual(
            image.search(q="apple",
                         page=1,
                         safesearch="false",
                         editors_choice="true")["totalHits"], 154)

    def test_custom_video_search(self):
        self.assertEqual(
            video.search(q="apple",
                         page=1,
                         safesearch="false",
                         editors_choice="true")["hits"][0]["pageURL"],
            "https://pixabay.com/videos/id-1019/")
        self.assertEqual(
            video.search(q="apple",
                         page=1,
                         safesearch="true",
                         editors_choice="true")["totalHits"], 1)
