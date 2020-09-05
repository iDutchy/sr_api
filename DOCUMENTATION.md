# SR_Api

Welcome, and thank you for using this api wrapper! This wrapper is completely async! Please note that I am not the creator of some-random-api. I only made this api wrapper! I also want to thank ir-3 for helping me get started with this.

For any questions and support for the wrapper, you can visit the [Discord support server](https://discord.gg/wZSH7pz "Devision")
 
## Getting Started:

To begin with, you'll have to install the package by doing one of the following commands:
- `pip install -U sr_api`
- `python -m pip -U install sr_api`
 
Or you can install directly from source by doing one of the following commands:
- `pip install -U git+https://github.com/iDutchy/sr_api`
- `python -m pip install -U git+https://github.com/iDutchy/sr_api`
 
After that, you will have to create the client:
```python
import sr_api

client = sr_api.Client()
```
Or if you have premium, provide your premium key like this:
```python
import sr_api

client = sr_api.Client("premium key here")
```
 
For future reference in this documentation: when referring to 'client' we refer to what has been defined above!
 
  
## Using the wrapper:
 
All available endpoints you can use.
  
### *await* client.get_image(animal)
---
Get a random animal image.

**Available options:** `dog`, `cat`, `panda`, `red_panda`, `fox`, `birb`, `koala`, `kangaroo`, `racoon`, `whale`, `pikachu`  
**Parameters:**\
**- animal** *(string)*: The animal you want to get an image from.
   
**Return type:** [Image](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#image "Image object attributes") *(object)*

### *await* client.get_fact(animal)
---
Get a random animal fact.

**Available options:** `cat`, `dog`, `koala`, `fox`, `bird`, `elephant`, `panda`, `racoon`, `kangaroo`, `giraffe`, `whale`
  
**Parameters:**\
**- animal** *(string)*: The animal you want to get a random fact from.
   
**Return type:** string

### *await* client.bot_token()
---
Get a random bots token. *These are not real and can not be used to make a real bot*

**Return type:** string

### *await* client.get_gif(option)
---
Get a random funny gif.

**Available options:** `wink`, `pat`, `hug`, `face-palm`

**Parameters:**\
**- option** *(string)*: The type of gif you want.

**Return type:** [Image](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#image "Image object attributes") *(object)*

### *await* client.chatbot(text)
---
Talk with the chatbot.

**Parameters:**\
**- text** *(string)*: Your line to the bot.

**Return type:** string

### *await* client.mc_user(username)
---
Get the username history and UUID from a minecraft user.

**Parameters:**\
**- username** *(string)*: Name of the minecraft user.

**Return type:** [MCuser](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#mcuser "MCuser object attributes") *(object)*

### *await* client.get_pokemon(pokemon)
---
Search for a pokemon in the pokedex.

**Parameters:**\
**- pokemon** *(string)*: Name of the pokémon.

**Return type:** [Pokemon](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#pokemon "Pokemon object attributes") *(object)*

### *await* client.encode_binary(text)
---
Encode text in binary.

**Parameters:**\
**- text** *(string)*: Text you want to encode.

**Return type:** string

### *await* client.decode_binary(binary)
---
Decode binary to text.

**Parameters:**\
**- binary** *(string)*: Binary you want to decode.

**Return type:** string

### *await* client.encode_base64(text)
---
Encode text in base64.

**Parameters:**\
**- text** *(string)*: Text you want to encode.

**Return type:** string

### *await* client.decode_base64(text)
---
Decode base64 to text.

**Parameters:**\
**- text** *(string)*: Text you want to decode.

**Return type:** string

### *await* client.get_lyrics(title)
---
Get the lyrics from a song.

**Parameters:**\
**- title** *(string)*: Title of the song you want to get lyrics from.

**Return type:** [Lyrics](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#lyrics "Lyrics object attributes") *(object)*

### *await* client.get_meme()
---
Get a random meme.

**Return type:** [Meme](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#meme "Meme object attributes") *(object)*

### *await* client.anime_quote()
---
Get a random quote from an anime.

**Return type:** [Quote](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#quote "Quote object attributes") *(object)*

### *await* client.get_joke()
---
Get a random joke.

**Return type:** string

### *await* client.define(word)
---
Get the definition from a word.

**Parameters:**\
**- word** *(string)*: The word you want to define.

**Return type:** [Definition](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#definition "Definition object attributes") *(object)*

### *await* client.filter(option, url)
---
**Available options:** `gay`, `wasted`, `greyscale`, `invert`, `triggered`, `blur`, `blurple`, `glass`, `pixelate`, `sepia`, `spin`, `invertgreyscale`, `brightness`, `threshold`, `red`, `green`, `blue`

**Parameters:**\
**- option** *(string)*: The type of image manipulation you want to use.\
**- url** *(string)*: The url from the image you want to manipulate.

**Return type:** string (url)

## *await* client.youtube_comment(avatar, username, comment)
---
Generate a fake youtube comment.

**Parameters:**\
**- avatar** *(string)*: The avatar you want to use.\
**- username** *(string)*: The username for the comment.\
**- comment** *(string)*: The content of the comment.

**Return type:** [Image](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#image "Image object attributes") *(object)*

### *await* client.view_color(color)
---
View a color.

**Parameters:**\
**- color** *(string)*: The color you want an image of. Example: `"123456"`

**Return type:** [Image](https://github.com/iDutchy/sr_api/blob/master/DOCUMENTATION.md#image "Image object attributes") *(object)*

### *await* client.rgb_to_hex(color_hex)
---
Convert RGB to HEX

**Parameters:**\
**- color_hex** *(string)*: The RGB value you want to convert. Example: `"255,255,255"`

**Return type:** string

### *await* client.hex_to_rgb(color_hex)
---
Convert HEX to RGB

**Parameters:**\
**- color_hex** *(string)*: The HEX value you want to convert. Example: `"123456"`

**Return type:** dict ("r", "g", "b")

---
---
---

## Objects

Here is explained what attributes the returned objects have

### Image
---
The object returned from `client.get_image()`,  `client.get_gif()`, `client.youtube_comment()` and `client.view_color()`

#### Image.url
The url of the image

#### *await* Image.read()
This will return a bytes object from the image

#### *await* Image.save(filepath)
Locally save the image.\
**Note:** 'filepath' requires a *full* path! e.g. `/home/John/myimage.png`

### Lyrics
---
The object returned from `client.get_lyrics()`

#### Lyrics.title
The title of the song

#### Lyrics.author
The author of the song

#### Lyrics.lyrics
The full lyrics of the song

#### Lyrics.thumbnail
A thumbnail of the song

#### Lyrics.link
A link to the songs Genius page

#### Lyrics.save()
This will locally save a `.txt` file of the lyrics

### Meme
---
The object returned from `client.get_meme()`

#### Meme.id
The ID of the meme

#### Meme.image
URL of the meme's image

#### Meme.caption
Description of the meme

#### Meme.category
The category the meme belongs to

#### *await* Meme.save(filepath)
Locally save an image of the meme.\
**Note:** 'filepath' requires a *full* path! e.g. `/home/John/meme.png`

### MCuser
---
The object returned from `client.mc_user()`

#### MCuser.name
Minecraft username

#### MCuser.uuid
The users UUID

#### MCuser.history
This will return a *list* of *dicts* with the users name history and date it was changed.

#### MCuser.formatted_history
A pre formatted list of the users name history

#### MCuser.reversed_formatted_history
A pre formatted list of the users name history in reversed order

### Quote
---
The object returned from `client.anime_quote()`

#### Quote.quote
The characters quote

#### Quote.character
The character the quote is from

#### Quote.anime
The anime show the character/quote is from

### Definition
The object returned from `client.define()`

#### Definition.word
The word that is being defined

#### Definition.definition
The definition of the word

### Pokemon
---
The object returned from `client.get_pokemon()`

#### Pokemon.name
The name of the pokémon

#### Pokemon.id
The ID of the pokémon

#### Pokemon.type
Returns a *list* of the types

#### Pokemon.abilities
Returns a *list* of the pokémons abilities

#### Pokemon.height
The pokémons height

#### Pokemon.weight
The pokémons weight

#### Pokemon.base_experience
The base experience of the pokémon

#### Pokemon.gender
Returns a *list* of the pokémons genders

#### Pokemon.egg_groups
Returns a *list* of the pokémons egg groups

#### Pokemon.hp
The pokémons HP stats

#### Pokemon.attack
The pokémons Attack stats

#### Pokemon.defense
The pokémons Defense stats

#### Pokemon.sp_atk
The pokémons Special Attack stats

#### Pokemon.sp_def
The pokémons Special Defense stats

#### Pokemon.speed
The pokémons Speed stats

#### Pokemon.total
The pokémons total stats

#### Pokemon.evolutionStage
The pokémons evolution stage

#### Pokemon.evolutionLine
Returns a *list* of the pokémons evolution line

#### Pokemon.spriteNormal
A `.png` url of the pokémons character

#### Pokemon.spriteAnimated
A `.gif` url of the pokémons character

#### Pokemon.description
A description of the pokémon

#### Pokemon.generation
The generation the pokémon is from
