import asyncio
from sr_api.client import Client


async def main():
    client = Client()

    image = await client.get_image("red_panda")
    await image.save("panda.png")

    await client.close()


asyncio.get_event_loop().run_until_complete(main())
