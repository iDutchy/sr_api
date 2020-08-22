import io

from sr_api.http import HTTPClient


# heavily inspired by https://github.com/Rapptz/discord.py/blob/master/discord/asset.py
class Image:
    __slots__ = ("url", "_http_client")

    def __init__(self, http_client: HTTPClient, url):
        self._http_client = http_client
        self.url = url

    async def read(self):
        return await self._http_client.get(self.url)

    async def save(self, fp, seek_start=True):
        data = await self.read()
        if isinstance(fp, io.IOBase) and fp.writable():
            written = fp.write(data)

            if seek_start:
                fp.seek(0)

            return written
        else:
            with open(fp, 'wb') as f:
                return f.write(data)
