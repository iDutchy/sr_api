class Lyrics:
    def __init__(self, data):
        self.title = data['title']
        self.author = data['author']
        self.lyrics = data['lyrics']
        self.thumbnail = data['thumbnail']['genius']
        self.link = data['links']['genius']
        
        
    async def save(self):
        with open(self.title +  ".txt", 'w') as f:
            return f.write(self.lyrics)
