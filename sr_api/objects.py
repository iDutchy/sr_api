import io

from sr_api.http import HTTPClient

class Definition:
    __slots__ = ("word", "definition")
    def __init__(self, data):
        self.word = data.get('word')
        self.definition = data.get('definition')

# heavily inspired by https://github.com/Rapptz/discord.py/blob/master/discord/asset.py
class Image:
    __slots__ = ("url", "_http_client")

    def __init__(self, http_client: HTTPClient, url):
        self.url = url
        self._http_client = http_client

    def __str__(self):
        return self.url if self.url is not None else ''

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

class Lyrics:
    __slots__ = ("title", "author", "lyrics", "thumbnail", "link")
    def __init__(self, data):
        self.title = data.get('title')
        self.author = data.get('author')
        self.lyrics = data.get('lyrics')
        self.thumbnail = data.get('thumbnail').get('genius')
        self.link = data.get('links').get('genius')
        
        
    def save(self):
        with open(self.title +  ".txt", 'w') as f:
            return f.write(self.lyrics)

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

class Pokedex:
    __slots__ = ("name", "id", "type", "species", "abilities", 
        "height", "weight", "base_experience", "gender", "egg_groups", 
        "stats", "family", "sprites", "description", "generation")
    def __init__(self, data):
        self.name = data.get('name')
        self.id = data.get('id')
        self.type = data.get('type')
        self.species = data.get('species')
        self.abilities = data.get('abilities')
        self.height = data.get('height')
        self.weight = data.get('weight')
        self.base_experience = data.get('base_experience')
        self.gender = data.get('gender')
        self.egg_groups = data.get('egg_groups')
        self.stats = data.get('stats')
        self.family = data.get('family')
        self.sprites = data.get('sprites')
        self.description = data.get('description')
        self.generation = data.get('generation')

    @property
    def evolutionStage(self):
        return self.family.get('evolutionStage')

    @property
    def evolutionLine(self):
        return self.family.get('evolutionLine')

    @property
    def spriteNormal(self):
        return self.sprites.get('normal')

    @property
    def spriteAnimated(self):
        return self.sprites.get('animated')

    @property
    def attack(self):
        return self.stats.get('attack')

    @property
    def hp(self):
        return self.stats.get('hp')

    @property
    def defense(self):
        return self.stats.get('defense')

    @property
    def sp_atk(self):
        return self.stats.get('sp_atk')

    @property
    def sp_def(self):
        return self.stats.get('sp_def')

    @property
    def speed(self):
        return self.stats.get('speed')

    @property
    def total(self):
        return self.stats.get('total')

class Quote:
    __slots__ = ("quote", "character", "anime")
    def __init__(self, data):
        self.quote = data.get('sentence')
        self.character = data.get('characther')
        self.anime = data.get('anime')

class Minecraft:
    __slots__ = ("name", "uuid", "history")
    def __init__(self, data):
        self.name = data.get("username")
        self.uuid = data.get("uuid")
        self.history = data.get("name_history")

    @property
    def formatted_history(self):
        d = self.history
        
        formatted = ""
        for x in d:
            formatted += f"{x['changedToAt'].replace('Origanal', 'Original')} >> {x['name']}\n"
                
        return formatted
    
    @property
    def reversed_formatted_history(self):
        d = self.history
        
        formatted = ""
        for x in d[::-1]:
            formatted += f"{x['changedToAt'].replace('Origanal', 'Original')} >> {x['name']}\n"
                
        return formatted
