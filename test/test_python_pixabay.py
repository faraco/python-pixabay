from unittest import TestCase
from pixabay import Image, Video, Pixabay
import os

api_key = os.getenv('PIXABAY_API_KEY')
image = Image(api_key)
video = Video(api_key)

pix = Pixabay(api_key)


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
            "https://pixabay.com/photos/apple-red-delicious-fruit-256261/")
        self.assertEqual(
            image.search(q="apple",
                         page=1,
                         safesearch="false",
                         editors_choice="true")["totalHits"], 143)

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

    def test_custom_old_image_search(self):
        self.assertIn(
            "hits",
            pix.image_search(q="water",
                             page=1,
                             safesearch="true",
                             editors_choice="true"))
        self.assertEqual(
            pix.image_search(q="apple", page=1)["hits"][0]["pageURL"],
            "https://pixabay.com/photos/apple-red-delicious-fruit-256261/")
        self.assertEqual(
            pix.image_search(q="apple",
                             page=1,
                             safesearch="false",
                             editors_choice="true")["totalHits"], 143)

    def test_custom_old_video_search(self):
        self.assertEqual(
            pix.video_search(q="apple",
                             page=1,
                             safesearch="false",
                             editors_choice="true")["hits"][0]["pageURL"],
            "https://pixabay.com/videos/id-1019/")
        self.assertEqual(
            pix.video_search(q="apple",
                             page=1,
                             safesearch="true",
                             editors_choice="true")["totalHits"], 1)
