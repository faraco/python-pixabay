import pytest
from .clones import Image, Video


class TestPythonPixabay:
    @pytest.fixture
    def image_client(self):
        return Image("Blank")

    @pytest.fixture
    def video_client(self):
        return Video("Blank")

    def test_image(self, image_client):
        resp = image_client.search()
        assert resp["hits"]

    def test_video(self, video_client):
        resp = video_client.search()
        assert resp["hits"]          
