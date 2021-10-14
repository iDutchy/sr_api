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

    def amongus(self, username, avatar, impostor = False):
        if self.key is None:
            raise PremiumOnly("This endpoint can only be used by premium users.")

        url = self.srapi_url("premium/amongus", {"username": username, "avatar": avatar, "impostor": str(impostor).lower()})
        return Image(self._http_client, url)
    
    def petpet(self, avatar):
        if self.key is None:
            raise PremiumOnly("This endpoint can only be used by premium users.")

        url = self.srapi_url("premium/petpet", {"avatar": avatar})
        return Image(self._http_client, url)
    
    async def get_animal(self, name=None):
        options = ("dog", "cat", "panda", "fox", "red_panda", "koala", "birb", 
                   "bird", "racoon", "raccoon", "kangaroo")
        response = await self._http_client.get(self.srapi_url("animal/" + name.lower() if name else random.choice(options)))
        return response

    async def get_image(self, name=None):
        options = ("dog", "cat", "panda", "red_panda", "fox", "birb", "koala",
                   "kangaroo", "racoon", "whale", "pikachu", "bird", "raccoon")

        if name.lower() not in options and name is not None:
            raise InputError(name.lower() + " is not a valid option!")

        if name is None:
            response = await self._http_client.get(self.srapi_url("img/" + random.choice(options)))
            url = response.get("link")

        else:
            response = await self._http_client.get(self.srapi_url("img/" + name.lower()))
            url = response.get("link")

        return Image(self._http_client, url)
    
    async def get_pokemon(self, name=None, pokemon_id=None, dym=None):
        if not name and not pokemon_id:
            raise InputError("Please provide either a name or an ID!")
        if name and pokemon_id:
            raise InputError("Please provide a name or ID, not both!")

        if name:
            q = {"pokemon": name}
        elif pokemon_id:
            q = {"id": pokemon_id}
        if dym:
            if self.key is None:
                raise PremiumOnly("The dym parameter can only be used by premium users.")
            q += {"dym": dym}

        response = await self._http_client.get(self.srapi_url("pokedex", q))
        if "error" in response:
            raise InputError("Pokémon " + name + " was not found")
        return Pokedex(response)
    
    async def get_fact(self, name):
        options = ("cat", "dog", "panda", "koala", "fox", "bird", "racoon", "kangaroo", "elephant", "giraffe", "whale", "birb", "raccoon")
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
    
    async def chatbot(self, text, uid=None):
        if self.key is None:
            raise PremiumOnly("This endpoint can only be used by premium users.")
            
        query = {"message": text}
        if uid:
            query += {'uid': uid}

        response = await self._http_client.get(self.srapi_url("chatbot", query))
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
            'pixelate', 'blur', 'gay', 'glass', 'wasted', 'triggered', 'spin', 'jail', 'blurple2', 'comrade', 'passed')

        if option.lower() not in options:
            raise InputError(option.lower() + " is not a valid option!")

        end_url = self.srapi_url("canvas/" + str(option).lower(), {"avatar": url})
        return Image(self._http_client, end_url)

    def youtube_comment(self, avatar, username, comment):
        url = self.srapi_url("canvas/youtube-comment", {"avatar": avatar, "username": username, "comment": comment})
        return Image(self._http_client, url)

    def tweet(self, avatar, username, display_name, comment):
        url = self.srapi_url("canvas/tweet", {"avatar": avatar, "username": username, "displayname": display_name, "comment": comment})
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
    
    def color_filter(self, avatar, color):
        color = color.replace("#", '')
        url = self.srapi_url("canvas/color", {"avatar": avatar, "color": color})
        return Image(self._http_client, url)

    def lolice(self, avatar):
        url = self.srapi_url("canvas/lolice", {"avatar": avatar})
        return Image(self._http_client, url)
    
    def simp_card(self, avatar):
        url = self.srapi_url("canvas/simpcard", {"avatar": avatar})
        return Image(self._http_client, url)
    
    def horny_card(self, avatar):
        url = self.srapi_url("canvas/horny", {"avatar": avatar})
        return Image(self._http_client, url)
    
    def its_stupid(self, avatar, dog):
        url = self.srapi_url("canvas/its-so-stupid", {"avatar": avatar, "dog": dog})
        return Image(self._http_client, url)
    
    async def check_key(self):
        if self.key is None:
            raise PremiumOnly("This endpoint can only be used by premium users.")

        response = await self._http_client.get(self.srapi_url("key/check"))
        res = response.get("response")
        
        return res
    
    def welcome(template, background, action_type, avatar, username, discriminator, guild_name, text_color, member_count):
            
        url = self.srapi_url("welcome/img/" + str(template) + '/' + background, {
            "type": action_type,
            "avatar": avatar,
            "username": username,
            "discriminator": discriminator,
            "guildName": guild_name,
            "textcolor": text_color,
            "memberCount": member_count
            })
        
        return Image(self._http_client, url)
    
    def premium_welcome(template, action_type, avatar, username, discriminator, guild_name, text_color, member_count, background_image):
        if self.key is None:
            raise PremiumOnly("This endpoint can only be used by premium users.")
            
        url = self.srapi_url("premium/welcome/" + str(template), {
            "type": action_type,
            "avatar": avatar,
            "username": username,
            "discriminator": discriminator,
            "guildName": guild_name,
            "textcolor": text_color,
            "memberCount": member_count,
            "bg": background_image
            })
        
        return Image(self._http_client, url)
    
    def rank_card(template, username, avatar, discriminator, level, current_xp, needed_xp, rank, background_image, background_color=None, text_color=None, current_xp_bar_color=None, bar_color=None):
        if self.key is None:
            raise PremiumOnly("This endpoint can only be used by premium users.")
            
        q = {
            "username": username,
            "avatar": avatar,
            "discriminator": discriminator,
            "level": level,
            "cxp": current_xp,
            "nxp": needed_xp,
            "rank": rank,
            "bg": background_image
            }
        
        if background_color is not None:
            q += {"cbg": background_color}
        if text_color is not None:
            q += {"ctext": text_color}
        if current_xp_bar_color is not None:
            q += {"ccxp": current_xp_bar_color}
        if bar_color is not None:
            q += {"cbar": bar_color}
            
        url = self.srapi_url("premium/rankcard/" + str(template), q)
            
        return Image(self._http_client, url)

    async def close(self):
        await self._http_client.close()
