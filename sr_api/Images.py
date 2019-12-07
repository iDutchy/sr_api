import aiohttp
import json

async def _call_api(endpoint):
    async with aiohttp.ClientSession() as c:
        async with c.get(f'https://some-random-api.ml/{endpoint}') as r:
            return await r.json()
        
async def _get_api_img(img):
    base = await _call_api(f'img/{img}')
    return base['link']

class Image:

    @property
    async def dog(self=None):
        return await _get_api_img('dog')

    @property
    async def cat(self=None):
        return await _get_api_img('cat')

    @property
    async def bird(self=None):
        return await _get_api_img('bird')

    @property
    async def fox(self=None):
        return await _get_api_img('fox')

    @property
    async def koala(self=None):
        return await _get_api_img('koala')

    @property
    async def panda(self=None):
        return await _get_api_img('panda')

    @property
    async def redpanda(self=None):
        return await _get_api_img('red_panda')
