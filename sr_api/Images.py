import aiohttp
import json

async def __call_api(endpoint):
    async with aiohttp.ClientSession() as c:
        async with c.get(f'https://some-random-api.ml/{endpoint}') as r:
            return await r.json()

async def __get_api_img(img):
    base = await __call_api(f'img/{img}')
    return base['link']

class Image:
    def __init__(self):
        self.dog = __get_api_img('dog')
