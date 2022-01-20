from .client import Client
from .utils import is_premium_endpoint
from typing import Optional

@is_premium_endpoint
def amongus(username: str, avatar: str, impostor: Optional[bool] = False):
    url = Client.build_url("premium/amongus", 
        {"username": username, "avatar": avatar, "impostor": str(impostor).lower()})
    return Image(Client.http, url)

@is_premium_endpoint
def petpet(avatar: str):
    url = Client.build_url("premium/petpet", {"avatar": avatar})
    return Image(Client.http, url)

async def get_animal(name: Optional[str] = None):
    options = ("dog", "cat", "panda", "fox", "red_panda", "koala", "birb", 
                "bird", "racoon", "raccoon", "kangaroo")
    url = Client.build_url("animal" + name.lower() if name else random.choice(options))
    response = await Client.http.get(url)
    return response

async def get_image(name: Optional[str] = None):
    options = ("dog", "cat", "panda", "red_panda", "fox", "birb", "koala",
                "kangaroo", "racoon", "whale", "pikachu", "bird", "raccoon")

    if name.lower() not in options and name is not None:
        raise InputError(name.lower() + " is not a valid option!")

    if name is None:
        url = Client.build_url("img" + random.choice(options))
        response = await Client.http.get(url)
        url = response.get("link")

    else:
        url = Client.build_url("img" + name.lower())
        response = await Client.http.get(url)
        url = response.get("link")

    return Image(Client.http, url)

async def get_pokemon(name: Optional[str] = None, pokemon_id: Optional[int] = None, dym=None):
    if not name and not pokemon_id:
        raise InputError("Please provide either a name or an ID!")
    if name and pokemon_id:
        raise InputError("Please provide a name or ID, not both!")

    if name:
        qeury = {"pokemon": name}
    elif pokemon_id:
        query = {"id": pokemon_id}
    if dym:
        if Client.key is None:
            raise PremiumOnly("The dym parameter can only be used by premium users.")
        query["dym"] = dym

    response = await Client.http.get(Client.build_url("pokedex", query))
    if "error" in response:
        raise InputError("Pokémon " + name + " was not found")
    return Pokedex(response)

async def get_fact(name: str):
    options = ("cat", "dog", "panda", "koala", "fox", "bird", "racoon", "kangaroo", "elephant", "giraffe", "whale", "birb", "raccoon")
    if not name.lower() in options:
        raise InputError(name + " is not a valid option!")

    response = await Client.http.get(Client.build_url("facts" + name))
    fact = response.get("fact")
    
    return fact

async def bot_token() -> str:
    response = await Client.http.get(Client.build_url("bottoken"))
    token = response.get("token")
                                                            
    return token

async def get_gif(name: str):
    options = ("wink", "pat", "hug", "face-palm")
    if not name.lower() in options:
        raise InputError(name + " is not a valid option!")

    response = await Client.http.get(Client.build_url("animu" + name))
    url = response.get("link")

    return Image(Client.http, url)

@is_premium_endpoint
async def chatbot(text: str, uid = None):
    query = {"message": text}
    if uid:
        query += {'uid': uid}

    response = await Client.http.get(Client.build_url("chatbot", query))
    res = response.get("response")
    
    return res
    
async def mc_user(name: str):
    response = await Client.http.get(Client.build_url("mc", {"username": name}))
    
    if "error" in response:
        raise InputError(response.get("error"))
    
    return Minecraft(response)

async def get_lyrics(title: str, owo: Optional[bool] = False):
    query = {"title": title}
    if owo:
        query['cancer'] = 'true'
    response = await Client.http.get(Client.build_url("lyrics", query))
    
    if "error" in response:
        raise InputError(response.get("error"))
    
    return Lyrics(response)

async def encode_binary(text: str):
    response = await Client.http.get(Client.build_url("binary", {"text": text}))
    res = response.get("binary")
    
    return res

async def decode_binary(text: str):
    response = await Client.http.get(Client.build_url("binary", {"decode": text}))
    res = response.get("text")
    
    return res

async def encode_base64(text: str):
    response = await Client.http(Client.build_url("base64", {"encode": text}))
    res = response.get("base64")
    
    return res

async def decode_base64(text: str):
    response = await Client.http(Client.build_url("base64", {"decode": text}))
    res = response.get("text")
    
    return res

async def get_meme():
    response = await Client.http(Client.build_url("meme"))
    
    return Meme(Client.http, response)

async def anime_quote():
    response = await Client.http(Client.build_url("animu/quote"))
    
    return Quote(response)

async def define(text: str):
    response = await Client.http(Client.build_url("dictionary", {"word": text}))
    
    if "error" in response:
        raise InputError(response.get("error") + " " + text)
        
    return Definition(response)

async def get_joke():
    response = await Client.http(Client.build_url("joke"))
    res = response.get("joke")
    return res

@is_premium_endpoint
async def check_key():
    response = await Client.http(Client.build_url("key/check"))
    res = response.get("response")
    
    return res

def welcome(template, background, action_type, avatar, username, discriminator, guild_name, text_color, member_count):
        
    url = Client.build_url("welcome/img/" + str(template) + '/' + background, {
        "type": action_type,
        "avatar": avatar,
        "username": username,
        "discriminator": discriminator,
        "guildName": guild_name,
        "textcolor": text_color,
        "memberCount": member_count
        })
    
    return Image(Client.http, url)

@is_premium_endpoint
def premium_welcome(template, action_type, avatar, username, discriminator, guild_name, text_color, member_count, background_image):
    url = Client.build_url("premium/welcome/" + str(template), {
        "type": action_type,
        "avatar": avatar,
        "username": username,
        "discriminator": discriminator,
        "guildName": guild_name,
        "textcolor": text_color,
        "memberCount": member_count,
        "bg": background_image
        })
    
    return Image(Client.http, url)

@is_premium_endpoint
def rank_card(template, username, avatar, discriminator, level, current_xp, needed_xp, rank, background_image, background_color=None, text_color=None, current_xp_bar_color=None, bar_color=None):
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
        
    url = Client.build_url("premium/rankcard/" + str(template), q)
        
    return Image(Client.http, url)