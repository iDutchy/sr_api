import io


class File:
    # abstract class that all file based classes inherit from
    __slots__ = ()

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
