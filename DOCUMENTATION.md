# SR_Api

Welcome, and thank you for using this api wrapper! This wrapper is completely async! Please note that I am not the creator of some-random-api. I only made this api wrapper! I also want to thank ir-3 for helping me get started with this.
 
## Getting Started:

To begin with, you'll habe to install the package by doing one of the following commands:
- `pip install -U sr_api`
- `python -m pip -U install sr_api`
 
Or you can install directly from source by doing one of the following commands:
- `pip install -U git+https://github.com/iDutchy/sr_api`
- `python -m pip install -U git+https://github.com/iDutchy/sr_api`
 
After that, you will have to create the client:
```python
from sr_api.client import Client

client = Client()
```
 
For future reference in this documentation: when referring to 'client' we refer to what has been defined above!
 
  
## Using the wrapper:
 
  
  
### *await* client.get_image(option)
---
**Available options:** `cat`, `dog`, `koala`, `fox`, `birb`, `red_panda`, `panda`, `racoon`, `kangaroo`
  
**Parameters:**\
**- option** *(string)*: The animal you want to get an image from.
   
**Return type:** Image *(object)*

### *await* client.get_fact(option)
---
**Available options:** `cat`, `dog`, `koala`, `fox`, `bird`, `elephant`, `panda`, `racoon`, `kangaroo`, `giraffe`, `whale`
  
**Parameters:**\
**- option** *(string)*: The animal you want to get a random fact from.
   
**Return type:** string

### *await* client.bot_token()
---
**Return type:** string

### *await* client.get_gif(option)
---
**Available options:** `wink`, `pat`, `hug`, `face-palm`

**Parameters:**\
**- option** *(string)*: The type of gif you want.

**Return type:** Image *(object)*

### *await* client.chatbot(text)
---
**Parameters:**\
**- text** *(string)*: Your line to the bot.

**Return type:** string

### *await* client.mc_user(username)
---
**Parameters:**\
**- username** *(string)*: Name of the minecraft user.

**Return type:** MCuser *(object)*
