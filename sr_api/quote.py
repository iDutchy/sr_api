class Quote:
    __slots__ = ("quote", "character", "anime")

    def __init__(self, data):
        self.quote = data['sentence']
        self.character = data['characther']
        self.anime = data['anime']
