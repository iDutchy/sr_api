import random
import aiohttp

from yarl import URL
from typing import Optional

from .http import HTTPClient
from .image import Image
from .pokedex import Pokedex
from .minecraft import Minecraft
from .lyrics import Lyrics
from .meme import Meme
from .quote import Quote
from .definition import Definition
from .options import Animal, Gif, Filter

class Client:
    __slots__ = ()
    http = HTTPClient()
    key = None

    @classmethod
    def init(cls, key: Optional[str] = None, *, session: Optional[aiohttp.ClientSession] = None):
        cls.http = HTTPClient(session)
        cls.key = key

    @classmethod
    def build_url(cls, path: str, query: Optional[dict] = {}):
        if cls.key:
            query['key'] = cls.key

        url = URL.build(
            scheme="https",
            host="some-random-api.ml",
            path="/"+path.lstrip("/"),
            query=query)

        return str(url)

    @classmethod
    async def close(cls):
        await cls.http.close()
