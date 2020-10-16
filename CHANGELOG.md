## v1.1.3 - Oktober 16, 2020
* Fix pokedex sprites and evolution line

### v1.1.2 - Oktober 16, 2020
* OwOify lyrics with `client.get_lyrics(title, owo=True)`
* Pass your own `aiohttp.ClientSession` so you dont have to separately close sr_api's session with `client = sr_api.Client(session=mysession)`
* Fixed a typo in the docs
* Add examples

### v1.1.1 - Oktober 14, 2020
* Fixed the big mistake I made
* gave access to sr_api.InputError and sr_api.PremiumOnly

### v1.1.0 - Oktober 14, 2020
* Fixed client token error
* Added amongus endpoint
* Client.view_color is no longer a coroutine
* Client.youtube_comment is no longer a coroutine
* Client.filter is no longer a coroutine

### v1.0.6 - September 6, 2020
* `Client.filter()` now returns an `Image` object

### v1.0.5 - September 6, 2020
* Added `spin` back because apparently SRA didnt document it.

### v1.0.4 - September 6, 2020
* Fixed type where you couldn't use the `greyscale` filter
* Removed `spin` from filter method, unsure how it even got there

### v1.0.3 - September 5, 2020
* You can now get the url from methods that return an `Image` object by casting the object to `str`

### v1.0.2 - September 5, 2020
* Fixed passing a key in `Client`

### v1.0.1 - September 5, 2020
* Added "key" to `Client.__slots__`

### v1.0 - September 5, 2020
* Renamed `Client.beta()` to `Client.filter()` since its no longer a beta feature
* Added `whale` and `pikachu` to `Client.get_image()`
* Added `invertgreyscale`, `brightness`, `threshold`, `red`, `green` & `blue` to `Client.filter()`
* Added `Client.youtube_comment()`
* Added `Client.view_color()`
* Added `Client.rgb_to_hex()`
* Added `Client.hex_to_rgb()`
* Added `Client.get_joke()`
* Added support for using premium. Provide your premium key in the Client init like `client = sr_api.Client("key here")`. Dont provide a key if you dont have one.
* Removed `Client.get_pikachu()` which is now available in `Client.get_image()`

### v0.4 - January 3, 2020
* Fixed issue with beta endpoint

### v0.3 - December 15, 2019
* Fixed last update where I forgot to change a crucial part

### v0.2 - December 15, 2019
* Fixed where `Meme.read()` and `Meme.save()` used `self.url` in stead of `self.image`

### v0.1 - December 10, 2019
* Initial release
