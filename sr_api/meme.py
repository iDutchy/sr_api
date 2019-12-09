class Meme:
    def __init__(self, data):
        self.id = data['id']
        self.image = data['image']
        self.caption = data['caption']
        self.category = data['category']
