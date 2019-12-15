from sr_api.file import File
from sr_api.http import HTTPClient


# heavily inspired by https://github.com/Rapptz/discord.py/blob/master/discord/asset.py
class Image(File):
    __slots__ = ("url", "_http_client")

    def __init__(self, http_client: HTTPClient, url):
        self.url = url
        self._http_client = http_client
