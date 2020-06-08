import io

from sr_api.http import HTTPClient

class Meme:
    __slots__ = ("id", "image", "caption", "category", "_http_client")
    def __init__(self, http_client: HTTPClient, data):
        self.id = data.get('id')
        self.image = data.get('image')
        self.caption = data.get('caption')
        self.category = data.get('category')
        self._http_client = http_client


    async def read(self):
        return await self._http_client.get(self.image)

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
