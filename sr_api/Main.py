import aiohttp
import json

from sr_api.Pokedex import Pokedex
from sr_api.Images import Image

class ApiError(Exception):
    pass

class InputError(Exception):
    pass


class ApiClient:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def __call_api(self, endpoint):
        async with aiohttp.ClientSession() as c:
            async with c.get(f'https://some-random-api.ml/{endpoint}') as r:
                return await r.json()

    async def get_pokemon(self, name):
        try:
            return Pokedex(await self.__call_api(f'pokedex?pokemon={name}')
        except KeyError:
            raise InputError(f'Pokémon "{name}" was not found.')
    
    @property
    def img(self):
        return Image()
