import random
import aiohttp

from yarl import URL

from .http import HTTPClient
from .image import Image
from .pokedex import Pokedex
from .minecraft import Minecraft
from .lyrics import Lyrics
from .meme import Meme
from .quote import Quote
from .definition import Definition
from .options import Animal, Gif, Filter

class InputError(Exception):
    __slots__ = ()
    pass

class PremiumOnly(Exception):
    __slots__ = ()
    pass

class Client:

    __slots__ = ("_http_client", "key")

    # SR API BASE PATH
    WEBSITE = "https://some-random-api.ml/"

    def __init__(self, key=None, *, session: aiohttp.ClientSession = None):
        self._http_client = HTTPClient(session)
        self.key = key

    def srapi_url(self, path, query={}):
        if self.key:
            query['key'] = self.key

        url = URL.build(
            scheme="https",
            host="some-random-api.ml",
            path="/"+path.lstrip("/"),
            query=query)

        return str(url)

    def amongus(self, username, avatar):
        if self.key is None:
            raise PremiumOnly("This endpoint can only be used by premium users.")

        url = self.srapi_url("premium/amongus", {"username": username, "avatar": avatar})
        return Image(self._http_client, url)

    async def get_image(self, name=None):
        options = ("dog", "cat", "panda", "red_panda", "fox", "birb", "koala",
                   "kangaroo", "racoon", "whale", "pikachu")

        if name.lower() not in options and name is not None:
            raise InputError(name.lower() + " is not a valid option!")

        if name is None:
            response = await self._http_client.get(self.srapi_url("img/" + random.choice(options)))
            url = response.get("link")

        else:
            response = await self._http_client.get(self.srapi_url("img/" + name.lower()))
            url = response.get("link")

        return Image(self._http_client, url)
    
    async def get_pokemon(self, name=None, pokemon_id=None):
        if not name and not pokemon_id:
            raise InputError("Please provide either a name or an ID!")
        if name and pokemon_id:
            raise InputError("Please provide a name or ID, not both!")

        if name:
            q = {"pokemon": name}
        elif pokemon_id:
            q = {"id": pokemon_id}

        response = await self._http_client.get(self.srapi_url("pokedex", q))
        if "error" in response:
            raise InputError("Pokémon " + name + " was not found")
        return Pokedex(response)
    
    async def get_fact(self, name):
        options = ("cat", "dog", "panda", "koala", "fox", "bird", "racoon", "kangaroo", "elephant", "giraffe", "whale")
        if not name.lower() in options:
            raise InputError(name + " is not a valid option!")

        response = await self._http_client.get(self.srapi_url("facts/" + name))
        fact = response.get("fact")
        
        return fact
    
    async def bot_token(self):
        response = await self._http_client.get(self.srapi_url("bottoken"))
        token = response.get("token")
                                                              
        return token
    
    async def get_gif(self, name):
        options = ("wink", "pat", "hug", "face-palm")
        if not name.lower() in options:
            raise InputError(name + " is not a valid option!")

        response = await self._http_client.get(self.srapi_url("animu/" + name))
        url = response.get("link")

        return Image(self._http_client, url)
    
    async def chatbot(self, text):
        response = await self._http_client.get(self.srapi_url("chatbot", {"message": text}))
        res = response.get("response")
        
        return res
        
    async def mc_user(self, name):
        response = await self._http_client.get(self.srapi_url("mc", {"username": name}))
        
        if "error" in response:
            raise InputError(response.get("error"))
        
        return Minecraft(response)
    
    async def get_lyrics(self, title, owo=False):
        q = {"title": title}
        if owo:
            q['cancer'] = 'true'
        response = await self._http_client.get(self.srapi_url("lyrics", q))
        
        if "error" in response:
            raise InputError(response.get("error"))
        
        return Lyrics(response)

    async def encode_binary(self, text):
        response = await self._http_client.get(self.srapi_url("binary", {"text": text}))
        res = response.get("binary")
        
        return res
    
    async def decode_binary(self, text):
        response = await self._http_client.get(self.srapi_url("binary", {"decode": text}))
        res = response.get("text")
        
        return res
    
    async def encode_base64(self, text):
        response = await self._http_client.get(self.srapi_url("base64", {"encode": text}))
        res = response.get("base64")
        
        return res
    
    async def decode_base64(self, text):
        response = await self._http_client.get(self.srapi_url("base64", {"decode": text}))
        res = response.get("text")
        
        return res
    
    async def get_meme(self):
        response = await self._http_client.get(self.srapi_url("meme"))
        
        return Meme(self._http_client, response)
    
    async def anime_quote(self):
        response = await self._http_client.get(self.srapi_url("animu/quote"))
        
        return Quote(response)
    
    async def define(self, text):
        response = await self._http_client.get(self.srapi_url("dictionary", {"word": text}))
        
        if "error" in response:
            raise InputError(response.get("error") + " " + text)
            
        return Definition(response)

    async def get_joke(self):
        response = await self._http_client.get(self.srapi_url("joke"))
        res = response.get("joke")
        return res

    def filter(self, option, url):
        options = (
            'greyscale', 'invert', 'invertgreyscale', 'brightness', 'threshold', 'sepia', 'red', 'green', 'blue', 'blurple',
            'pixelate', 'blur', 'gay', 'glass', 'wasted', 'triggered', 'spin')

        if option.lower() not in options:
            raise InputError(option.lower() + " is not a valid option!")

        end_url = self.srapi_url("canvas/" + str(option).lower(), {"avatar": url})
        return Image(self._http_client, end_url)

    def youtube_comment(self, avatar, username, comment):
        url = self.srapi_url("canvas/youtube-comment", {"avatar": avatar, "username": username, "comment": comment})
        return Image(self._http_client, url)

    def view_color(self, color):
        color = color.replace("#", '')
        url = self.srapi_url("canvas/colorviewer", {"hex": color})
        return Image(self._http_client, url)

    async def rgb_to_hex(self, rgb):
        response = await self._http_client.get(self.srapi_url("canvas/hex", {"rgb": rgb}))
        res = response.get("hex")
        return res

    async def hex_to_rgb(self, color_hex):
        response = await self._http_client.get(self.srapi_url("canvas/rgb", {"hex": color_hex}))
        return dict(response)

    async def close(self):
        await self._http_client.close()
