import aiohttp
import json

from sr_api.Pokedex import Pokedex
from sr_api.Images import Image

class ApiError(Exception):
    pass

class InputError(Exception):
    pass


class ApiClient:

    async def __call_api(endpoint):
        async with aiohttp.ClientSession() as c:
            async with c.get(f'https://some-random-api.ml/{endpoint}') as r:
                return await r.json()

    async def get_pokemon(name):
        try:
            return Pokedex(__call_api(f'pokedex?pokemon={name}')
        except KeyError:
            raise InputError(f'Pokémon "{name}" was not found.')
    
    @property
    def img():
        return Image()
