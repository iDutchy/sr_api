import asyncio
import sr_api


async def main():
    image = await sr_api.get_image("red_panda")
    await image.save("panda.png")

    await sr_api.close()


asyncio.get_event_loop().run_until_complete(main())