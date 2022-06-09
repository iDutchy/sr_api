class Quote:
    __slots__ = ("quote", "character", "anime")
    def __init__(self, data):
        self.quote = data.get('sentence')
        self.character = data.get('character')
        self.anime = data.get('anime')
