from sr_api.http import HTTPClient
from sr_api.image import Image

class InputError(Exception):
    pass

class Client:

    # SR API BASE PATH
    SR_API_BASE = "https://some-random-api.ml/"

    def __init__(self):
        self._http_client = HTTPClient()

    def srapi_url(self, path):
        return self.SR_API_BASE + path

    async def get_image(self, name):
        if not name in ["cat", "dog"]:
            raise InputError(f"{name} is not a valid option.")
        response = await self._http_client.get(self.srapi_url("img/" + name + "/"))
        url = response.get("link")

        return Image(self._http_client, url)

    async def close(self):
        await self._http_client.close()