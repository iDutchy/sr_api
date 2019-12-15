from sr_api.file import File
from sr_api.http import HTTPClient


class Meme(File):
    __slots__ = ("id", "image", "caption", "category", "_http_client")

    def __init__(self, http_client: HTTPClient, data):
        self.id = data['id']
        self.image = data['image']
        self.caption = data['caption']
        self.category = data['category']
        self._http_client = http_client
