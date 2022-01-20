from .client import Client
from .utils import is_premium_endpoint

def filter(option: str, url: str):
    options = (
        'greyscale', 'invert', 'invertgreyscale', 'brightness', 'threshold', 'sepia', 'red', 'green', 'blue', 'blurple',
        'pixelate', 'blur', 'gay', 'glass', 'wasted', 'triggered', 'spin', 'jail', 'blurple2')

    if option.lower() not in options:
        raise InputError(option.lower() + " is not a valid option!")

    end_url = Client.build_url("canvas/" + str(option).lower(), {"avatar": url})
    return Image(Client.http, end_url)

def youtube_comment(avatar: str, username: str, comment: str):
    url = Client.build_url("canvas/youtube-comment", {"avatar": avatar, "username": username, "comment": comment})
    return Image(Client.http, url)

def view_color(color: str):
    color = color.replace("#", '')
    url = Client.build_url("canvas/colorviewer", {"hex": color})
    return Image(Client.http, url)

async def rgb_to_hex(rgb: str):
    response = await Client.http(Client.build_url("canvas/hex", {"rgb": rgb}))
    res = response.get("hex")
    return res

async def hex_to_rgb(color_hex: str):
    response = await Client.http(Client.build_url("canvas/rgb", {"hex": color_hex}))
    return dict(response)

def lolice(avatar: str):
    url = Client.build_url("canvas/lolice", {"avatar": avatar})
    return Image(Client.http, url)

def simp_card(avatar: str):
    url = Client.build_url("canvas/simpcard", {"avatar": avatar})
    return Image(Client.http, url)

def horny_card(avatar: str):
    url = Client.build_url("canvas/horny", {"avatar": avatar})
    return Image(Client.http, url)

def its_stupid(avatar: str, dog):
    url = Client.build_url("canvas/its-so-stupid", {"avatar": avatar, "dog": dog})
    return Image(Client.http, url)