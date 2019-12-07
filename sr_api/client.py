from sr_api.http import HTTPClient
from sr_api.image import Image
from sr_api.pokedex import Pokedex

class Client:

    # SR API BASE PATH
    SR_API_BASE = "https://some-random-api.ml/"

    def __init__(self):
        self._http_client = HTTPClient()

    def srapi_url(self, path):
        return self.SR_API_BASE + path

    async def get_image(self, name):
        response = await self._http_client.get(self.srapi_url("img/" + name + "/"))
        url = response.get("link")

        return Image(self._http_client, url)
    
    async def get_pokemon(self, name):
        response = await self._http_client.get(self.srapi_url("pokedex?pokemon=" + name))
        return Pokedex(self._http_client, response)

    async def close(self):
        await self._http_client.close()
