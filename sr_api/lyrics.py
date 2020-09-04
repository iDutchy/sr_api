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
