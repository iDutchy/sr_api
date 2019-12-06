import aiohttp
import json

from sr_api.Pokedex import Pokedex
from sr_api.Images import Image

class ApiError(Exception):
    pass

class InputError(Exception):
    pass


class ApiClient:

    async def __call_api(self, endpoint):
        async with aiohttp.ClientSession() as c:
            async with c.get(f'https://some-random-api.ml/{endpoint}') as r:
                return await r.json()

    async def get_pokemon(self, name):
        result = await self.__call_api(f'pokedex?pokemon={name}')
        if result['error']:
            raise InputError(f'Pokémon "{name}" was not found.')
        return Pokedex(result)
    
    @property
    def img(self):
        return Image()
